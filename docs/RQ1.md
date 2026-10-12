# RQ1 
How well can RoBERTa identify Gang of Four patterns in Java source code?
NEW: How well can RoBERTa identify three Gang of Four patterns (Factory Method, Prototype, Singleton) in Java source code across 30 examples (15 true, 15 false) each?

## Bounded Sample/Case IDs (?)
We will reproduce the paper's results for RoBERTa for three Gang of Four patterns: Factory Method, Prototype, and Singleton. For each design pattern, we will choose 30 fixed random Java source code examples from the given dataset, with 15 true cases and 15 false cases for each.

## Method/Metric or Decision Rule
Our evaluation metrics will be Precision, Recall, and mainly F1 Score.

## Expected Result Before Reproduction
| Design Pattern | Precision | Recall | F1 Score |
| :- | :- | :- | :- |
| Factory Method | 0.87 | 0.77 | 0.78 |
| Prototype | 0.88 | 0.84 | 0.84 |
| Singleton | 0.92 | 0.9 | 0.91 |

### For Excel:
Precision:  
Factory Method: 0.87  
Prototype: 0.88  
Singleton: 0.92

Recall:  
Factory Method: 0.77  
Prototype: 0.84  
Singleton: 0.9

F1 Score:  
Factory Method: 0.78  
Prototype: 0.84  
Singleton: 0.91

**NOTE**: Factory Method only had 11 truth samples in the dataset, so we use an 11-11 split instead of 15-15 for this design pattern.

## Reproduction Results
| Design Pattern | Precision | Recall | F1 Score |
| :- | :- | :- | :- |
| Factory Method | 0.64 | 0.80 | 0.71 |
| Prototype | 1.0 | 1.0 | 1.0 |
| Singleton | 1.0 | 1.0 | 1.0 |

### For Excel:
Results of 1.0 are due to small dataset size.
Precision:  
Factory Method: 0.64  
Prototype: 1.0  
Singleton: 1.0

Recall:  
Factory Method: 0.80  
Prototype: 1.0  
Singleton: 1.0

F1 Score:  
Factory Method: 0.71  
Prototype: 1.0  
Singleton: 1.0  
