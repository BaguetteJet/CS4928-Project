# Event B
A new requirement adds a second variation point that was not present when you made the Week 9 design decision. Apply the requirement to your current design and determine whether the earlier pattern/no-pattern decision makes the change easier or harder.
The new requirement is that your design-pattern recognition approach should now support Java examples where the pattern is implemented across multiple related classes/files, rather than just individual files, while still supporting the original cases.

## Two Realistic Responses
| Option | What it does | Trade-off |
| :- | :- | :- |
| No structural change | Concatenate each java file into one file as a data-prep step, outside the classifier | 0 lines of code change, but multi-file folders would still be silently skipped |
| Small change in `load_programs` | If an entry is a folder, join the .java files inside and treat as one sample | ~10 lines of code change, loses explicit file and class boundaries, so the relationships between classes aren't modelled |

## Our Chosen Response : ~10 line change in `load_programs`
In `load_programs` we chose to replace the `if os.path.isfile(file_path)` with a helper that handles both single .java files and folders of .java files.

## Week 9 Decision: Supported
Our Week 9 design decision to use Extract Class refactoring method is supported as it kept our changes in response to Event B limited to one method in one file. Before applying the Extract Class method, the change would need to be duplicated in three different places to respond to Event B.

--- 

## For Excel

### Prediction / Expected Pressure

The expected pressure only applies to the input-loading of the RoBERTa model. The Week 9 implementation as is silently skips a multi-file example. We expect that the kNN and cross-validation stages will need no change and that the single-file results will remain the same, as follows:

| Design Pattern | Precision | Recall | F1 Score |
| :- | :- | :- | :- |
| Factory Method | 0.90 | 0.90 | 0.90 |
| Prototype | 0.94 | 0.93 | 0.93 |
| Singleton | 0.86 | 0.86 | 0.86 |

### Response / Accepted Trade-off
In `load_programs` we chose to replace the `if os.path.isfile(file_path)` with a helper that handles both single .java files and folders of multiple .java files. The accepted trade-off is that the file and class boundaries are lost when files are joined. For our model, this is not a big issue as its generates embeddings line-by-line and does not look at structural relationships.

### Main Limitation / Threat
The main threat is construct validity. The recognition method embeds each line independently and averages the embeddings, meaning it recognises semantic similarity but not structural relationships between classes that define a design pattern.

## Results
The Week 9 implementation crashes when using a multi-file sample, returning an `IsADirectoryError`. After our change to the file loader, when run on single file samples from each design pattern, the results from Week 9 remain the same. 
Results using a dataset with an added multi-file sample achieves a score of 0.909 for the Factory Method design pattern. The multi-file eventB sample was successfully loaded as a single sample and correctly classified as Factory Method.
We cannot compare these results directly with Week 9 as the added sample changes the cross validation folds, but the successful run provides evidence our implementation supports examples where the pattern is implemented across multiple related files.



