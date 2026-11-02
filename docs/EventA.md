# Event A
From the linked artefact, select 15 Java examples that your group did not use at M2. Prioritise a mix of clear pattern instances, variants/partial implementations and non-pattern lookalikes. Apply your M2 recognition method unchanged and determine where it transfers and where it breaks.

## Changes from RQ1 / Held-out cases
Changes we've made since RQ1:
- **FIX 1: train and score on the real labels.** The original used predicted_labels as both training and test labels. The kNN classifier was scored against another kNN's predictions rather than the ground truth, which produced 1.0 scores. \
The fix uses program_labels, the real labels taken from the folders.

- **FIX 2: use stratified 5-fold cross-validation instead of one 80/20 split.** A 20% test split of 22 or 30 files leaves only 5 or 6 test files, so a single error moves F1 by about 0.2. The split also wasn't stratified, so class balance in the test set was down to chance. \
The fix uses StratifiedKFold with cross_val_predict and the same KNeighborsClassifier(n_neighbors=3), so every file is tested exactly once.

- **FIX 3: skip files that appear in both classes.** Factory Method's factorymethod (3).java is identical to nonfm (11).java, and Singleton's singleton (3).java is identical to nons (14).java. \
Each of these is labelled both 1 and 0. When loading, a non-pattern file is now skipped if its content matches a pattern file.

- **FIX 4: load files in sorted order.** The original read each folder with os.listdir(), whose order depends on the operating system. \
The fix sorts the listing with the notebook's existing _natural_key, so their order is fixed.  

| Design Pattern | Number of Positive Samples | Number of Negative Samples |
| :- | :- | :- |
| Factory Method | 0 (all 11 used for RQ1) | 15 |
| Prototype | 7 | 8 |
| Singleton | 7 | 8 |

## Event A vs M2
**What holds:**\
**What doesn't hold:**\
**Evidence for the interpretation:**

## For Excel

### Prediction before execution
Chosen Examples for Event A: 
NOTE: for Factory Method, we do not have any remaining unseen positive samples so cannot produce a mixed test set of 15 unseen samples as requested in Event A. As the test set for a model does not require an equal or even mixed division, we will use only unseen negative samples.
Factory Method: 15 unused negative samples, as there are no remaining unseen positive samples
Prototype: equal division of positive and negative unseen samples, about 7-8 of each
Singleton: equal division of positive and negative unseen samples, about 7-8 each

The code was fixed to use real ground-truth labels, stratified 5-fold cross-validation for more reliable evaluation, and to skip duplicate files that appear in both pattern and non-pattern classes. It also sorts files consistently to ensure reproducible results across different operating systems.

Prediction: We predict that our results for Event A will be very similar if not identical to those of our bounded reproduction (M2) as Event A doesn't request any change in the model architecture or training, only inferencing with unseen samples from the same source dataset.

Precision:
Factory Method: ~0.8-1.0
Prototype: ~0.8-1.0
Singleton: ~0.8-1.0

Recall:
Factory Method: ~0.8-1.0
Prototype: ~0.8-1.0
Singleton: ~0.8-1.0

F1 Score:
Factory Method: ~0.8-1.0
Prototype: ~0.8-1.0
Singleton: ~0.8-1.0

### Result / Decision

### Concrete Design Problem

### Alternatives considered

### Chosen intervention / no-change decision








