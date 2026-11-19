# Results

The evaluation covers RoBERTa-based recognition of Factory Method, Prototype, and Singleton in Java source code. The tables show the reported precision, recall, and F1 scores for each stage.

## RQ1 (M2 bounded reproduction)

The reproduction used 15 positive and 15 negative examples each for Prototype and Singleton. Factory Method used 11 positive and 11 negative examples because the dataset contained only 11 positives for that pattern.

| Design pattern | Expected precision | Expected recall | Expected F1 | Reproduced precision | Reproduced recall | Reproduced F1 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Factory Method | 0.87 | 0.77 | 0.78 | 0.64 | 0.80 | 0.71 |
| Prototype | 0.88 | 0.84 | 0.84 | 1.00 | 1.00 | 1.00 |
| Singleton | 0.92 | 0.90 | 0.91 | 1.00 | 1.00 | 1.00 |

The original implementation used earlier k-nearest neighbours (kNN) predictions as reference labels. This makes the perfect scores for Prototype and Singleton unreliable as measures of performance against ground truth. The reproduction also used stratified splits, which may contribute to differences from the expected results. [RQ1 notes](RQ1.md)

## Event A (held-out examples)

The M2 recognition pipeline ran on unseen examples using the scaler fitted on the RQ1 data. The predicted range was approximately 0.80–1.00 for each metric.

| Design pattern | Positive examples | Negative examples | Precision | Recall | F1 |
| --- | ---: | ---: | ---: | ---: | ---: |
| Factory Method | 0 | 15 | 1.00 | 0.67 | 0.80 |
| Prototype | 7 | 8 | 0.553 | 0.53 | 0.521 |
| Singleton | 7 | 8 | 0.553 | 0.53 | 0.521 |

Prototype and Singleton fell below the predicted range on all three metrics. A shift in the distribution of the held-out embeddings is one possible explanation. All Factory Method positives had already been used in RQ1, so its reported scores reflect a test set containing only negative examples and provide no evidence about detecting unseen positive cases. [Event A notes](EventA.md)

## M4 (Extract Class refactoring)

Extract Class moved the duplicated recognition logic into a shared class. Verification matched the corrected M2 implementation in `RQ1_fixed.ipynb` across all three patterns.

| Design pattern | Precision | Recall | F1 |
| --- | ---: | ---: | ---: |
| Factory Method | 0.90 | 0.90 | 0.90 |
| Prototype | 0.94 | 0.93 | 0.93 |
| Singleton | 0.86 | 0.86 | 0.86 |

These scores are the single-file reference for Event B. [M4 notes](M4.md)

## Event B (multi-file examples)

For Event B, the loader grouped the related Java files in a folder into a single sample. The classifier correctly identified that sample as Factory Method. On the single-file examples, precision, recall, and F1 matched the M4 results for Factory Method, Prototype, and Singleton. [Event B notes](EventB.md)
