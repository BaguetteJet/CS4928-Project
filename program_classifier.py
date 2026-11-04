import os
import re
import torch
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import precision_score, recall_score, f1_score
from transformers import RobertaTokenizer, RobertaModel
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import StratifiedKFold, cross_val_predict  # FIX 2
from collections import Counter
from sklearn.metrics.pairwise import cosine_distances, euclidean_distances
from tqdm import tqdm

def _natural_key(name):
    """Sort 'foo (2).java' before 'foo (10).java'."""
    return [int(part) if part.isdigit() else part.lower()
        for part in re.split(r"(\d+)", name)]

class ProgramClassifier:
    def __init__(self, java_programs_folder, distance_metric='euclidean', n_splits=5, n_neighbors=3, random_state=2137, device=None):
        self.java_programs_folder = java_programs_folder
        self.distance_metric = distance_metric
        self.n_neighbors = n_neighbors
        self.n_splits = n_splits
        self.random_state = random_state
        self.device = device if device else ("cuda" if torch.cuda.is_available() else "cpu")

        # Initialize the RoBERTa tokenizer and model
        self.tokenizer = RobertaTokenizer.from_pretrained("roberta-base")
        self.model = RobertaModel.from_pretrained("roberta-base").to(self.device).eval()

        # Initialize lists to store Java programs and their corresponding labels
        self.java_programs = []
        self.program_labels = []
        self.program_files = []

        self.class_folders = {"non-pattern": 0, "pattern": 1}

    # Function to extract embeddings from text
    def get_embeddings(self, text):
        inputs = self.tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=512)
        inputs = {k: v.to(self.device) for k, v in inputs.items()}

        with torch.no_grad():
            outputs = self.model(**inputs)

        return outputs.last_hidden_state.mean(dim=1).cpu().numpy()

    # Function to calculate the distance matrix based on the chosen metric
    def calculate_distance_matrix(self, embeddings, metric='cosine'):
        if metric == 'cosine':
            return cosine_distances(embeddings)
        elif metric == 'euclidean':
            return euclidean_distances(embeddings)
        else:
            raise ValueError(f"Unrecognized metric: {metric}")

    # Function to load Java programs and their labels from the specified folders
    def load_programs(self):
        self.java_programs = []
        self.program_labels = []
        self.program_files = []

        # FIX 3: read the pattern files first so a non-pattern file with identical content
        # (same file labelled both 1 and 0) can be skipped.
        pattern_folder = os.path.join(self.java_programs_folder, "pattern")
        pattern_texts = set()
        for program_file in os.listdir(pattern_folder):
            with open(os.path.join(pattern_folder, program_file), "r", encoding="iso-8859-1") as f:
                pattern_texts.add(f.read())

        for folder_name, label in self.class_folders.items():
            folder_path = os.path.join(self.java_programs_folder, folder_name)

            # FIX 4: sort so the file order (and therefore the CV folds) is the same on every OS
            # ORIGINAL: for program_file in os.listdir(folder_path):
            for program_file in sorted(os.listdir(folder_path), key=_natural_key):
                file_path = os.path.join(folder_path, program_file)

                if os.path.isfile(file_path):
                    with open(file_path, "r", encoding="iso-8859-1") as f:
                        # FIX 3: skip label-conflicting duplicates
                        # ORIGINAL: java_programs.append(f.read())
                        program_text = f.read()
                    if label == 0 and program_text in pattern_texts:
                        print(f"FIX 3: skipping {program_file}, identical to a file in pattern/ (label conflict)")
                        continue
                    self.java_programs.append(program_text)

                    self.program_labels.append(label)
                    self.program_files.append(program_file)

        print(Counter(self.program_labels))

    # Calculate embeddings for the Java programs line by line and take the mean
    def generate_program_embeddings(self):
        program_embeddings = []
        for program in tqdm(self.java_programs, desc="Generating embeddings"):
            lines = program.split('\n')
            line_embeddings = [self.get_embeddings(line) for line in lines if line.strip()]
            program_embeddings.append(np.mean(line_embeddings, axis=0))

        return program_embeddings

    # Run the classification process
    def run_classification(self):
        # Load Java programs
        self.load_programs()

        # Calculate embeddings
        program_embeddings = self.generate_program_embeddings()

        # Apply standard scaling to normalize the embeddings
        scaler = StandardScaler()
        normalized_embeddings = scaler.fit_transform(np.vstack(program_embeddings))

        # Calculate the distance matrix based on the chosen metric
        distance_matrix = self.calculate_distance_matrix(normalized_embeddings, metric=self.distance_metric)

        # FIX 1: the original block created pseudo-labels with a leave-one-out kNN vote and then
        # used them as the "true" labels for training and testing. It is no longer used; the
        # real labels (program_labels) are used instead.

        # FIX 2: one unstratified 80/20 split (5-6 test files) replaced with stratified 5-fold
        # cross-validation, so every file is predicted exactly once by a model that did not see it.

        y_test = np.array(self.program_labels)  # FIX 1: real labels
        files_test = self.program_files

        # Apply k-nearest neighbor classification
        knn = KNeighborsClassifier(n_neighbors=self.n_neighbors)
        cv = StratifiedKFold(n_splits=self.n_splits, shuffle=True, random_state=self.random_state)  # FIX 2
        predictions = cross_val_predict(knn, normalized_embeddings, y_test, cv=cv)  # FIX 2

        # Calculate precision, recall, and f-score
        precision = precision_score(y_test, predictions, average='weighted')
        recall = recall_score(y_test, predictions, average='weighted')
        f1 = f1_score(y_test, predictions, average='weighted')

        # Store results
        results = {
            "predictions": predictions,
            "true_labels": y_test,
            "files": files_test,
            "precision": precision,
            "recall": recall,
            "f1": f1,
            "normalized_embeddings": normalized_embeddings,
            "distance_matrix": distance_matrix
        }

        return results

    # Print the results
    def print_results(self, results):
        for filename, prediction, true_label in zip(results["files"], results["predictions"], results["true_labels"]):
            print(
                f"File: {filename}, "
                f"Predicted Label: {prediction}, "
                f"True Label: {true_label}"
            )

        print(f"Precision: {results['precision']}, Recall: {results['recall']}, F-score: {results['f1']}")
