# Event A
From the linked artefact, select 15 Java examples that your group did not use at M2. Prioritise a mix of clear pattern instances, variants/partial implementations and non-pattern lookalikes. Apply your M2 recognition method unchanged and determine where it transfers and where it breaks.

## Changes from RQ1 / Held-out cases 
| Design Pattern | Number of Positive Samples | Number of Negative Samples |
| :- | :- | :- |
| Factory Method | 0 (all 11 used for RQ1) | 15 |
| Prototype | 7 | 8 |
| Singleton | 7 | 8 |

## Event A vs M2
**What holds:**\
Everything transferred without errors, with the main change being the dataset used for testing.  
**What doesn't hold:**\
The Event A embeddings had to be transformed using the same scaler fitted on the RQ1 dataset in M2. This ensured that both datasets used the same normalisation, making their embeddings directly comparable.   
**Evidence for the interpretation:**\
Lack of errors in the implementation.  
The results obtained from Event A were worse than those from RQ1. One explanation is that Event A was transformed using the scaler fitted on RQ1, meaning its embeddings were not guaranteed to fall within the same distribution or range as the RQ1 embeddings. This could result in Event A samples lying further away from the RQ1 embeddings in the feature space, making it more difficult for KNN to identify suitable neighbours and accurately classify the samples.

## For Excel

### Prediction before execution
Chosen Examples for Event A: 
NOTE: for Factory Method, we do not have any remaining unseen positive samples so cannot produce a mixed test set of 15 unseen samples as requested in Event A. As the test set for a model does not require an equal or even mixed division, we will use only unseen negative samples.
Factory Method: 15 unused negative samples, as there are no remaining unseen positive samples
Prototype: equal division of positive and negative unseen samples, about 7-8 of each
Singleton: equal division of positive and negative unseen samples, about 7-8 each

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
Event A Results:
Precision:
Factory Method: 1.0
Prototype: 0.553
Singleton: 0.553

Recall:
Factory Method: 0.67
Prototype: 0.53
Singleton: 0.53

F1 Score:
Factory Method: 0.80
Prototype: 0.521
Singleton: 0.521

The results obtained from Event A were worse than those from RQ1. One explanation is that Event A was transformed using the scaler fitted on RQ1, meaning its embeddings were not guaranteed to fall within the same distribution or range as the RQ1 embeddings. This could result in Event A samples lying further away from the RQ1 embeddings in the feature space, making it more difficult for KNN to identify suitable neighbours and accurately classify the samples.

### Identified Refactoring Technique
The recognition method is currently implemented separately for each design pattern being tested, resulting in significant code duplication. Implementing the Extract Class refactoring technique to separate the recognition method and make it reusable will solve the duplication issue and make it easier to refactor and update in future.