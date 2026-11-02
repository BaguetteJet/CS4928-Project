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
**What doesn't hold:**\
**Evidence for the interpretation:**

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

### Concrete Design Problem

The recognition method is currently implemented separately for each design pattern being tested, resulting in significant code duplication.

Duplicated code introduces several maintainability issues:

- **Increased maintenance effort:** Changes, improvements, or fixes must be manually applied to all duplicated code.
- **Risk of inconsistencies:** If changes are not applied consistently across all implementations, different design patterns may end up using slightly different versions of the recognition method, which could affect test results.
- **Greater likelihood of errors:** Repeatedly modifying the same logic in multiple locations increases the possibility of introducing errors or overlooking an implementation.
- **Reduced scalability:** As more design patterns are added to the evaluation, additional copies of the recognition method may be required, further increasing code complexity and maintenance overhead.
- **Poor code reusability:** The duplicated implementation makes it difficult to reuse or extend the recognition functionality independently of the individual design patterns.

### Alternatives considered

Refactoring Techniques:

1. Extract Method
    - Extract duplicated recognition logic into a one shared method.
    - Reduces code duplication and maintenance effort.
    - Less suitable for managing multiple related functions independently.

2. Extract Class
    - Move the recognition logic, into a dedicated class.
    - Separates recognition functionality from individual design pattern implementations.
    - Makes individual functions easier to modify, maintain and extend. 
    - Introduces some additional class structure.

### Chosen intervention / no-change decision

**Extract Class** was selected because the recognition process consists of multiple related functions and loops.

- Centralises recognition functionality in one location.
- Eliminates duplicated code across design patterns.
- Allows individual functions to be modified independently.
- Improves maintainability, reusability and extensibility.
- Ensures consistent recognition behaviour across implementations.






