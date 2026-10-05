**CS4928 Project P01: Design Pattern Recognition with Large Language Models**

_Primary | A. OO Design, Patterns & Refactoring_

| **Item**       | **Details**                                                                   |
| -------------- | ----------------------------------------------------------------------------- |
| Assigned study | Pandey et al., "Design pattern recognition: a study of large language models" |
| Venue / year   | Empirical Software Engineering (2025)                                         |
| Language route | Java direct                                                                   |
| Expected setup | Low-Medium                                                                    |

**Paper:** <https://link.springer.com/article/10.1007/s10664-025-10625-1>

**Authors' replication package:** <https://github.com/sushantkumar007007/Design-Pattern-Recognition-using-Large-Language-Models->

# Your bounded starting task

On a fixed set of 30 Java examples covering three GoF patterns and matched non-pattern controls, repeat one pattern-recognition experiment with a fixed prompt and report precision, recall, F1 and the main error types. Do not reproduce the whole paper.

Sampling/freeze rule: before the main M2 analysis, record the exact case/project/file identifiers used. Unless the bounded task names a different exact set, take the first 30 eligible items in stable order (case ID, then file path, then chronological ID). Do not choose examples because they produce a preferred result. If fewer than 30 eligible items exist, use all and record that fact.

# Recommended research questions

- RQ1. How accurately does a modern LLM recognise selected GoF patterns in our bounded Java set?
- RQ2. Which structural/contextual features explain recognition errors?

You may refine wording during Lab 3 so the RQs match your exact bounded unit of analysis. Keep two RQs unless a third one is clearly necessary and manageable.

# Week 5: what to do first

1. Open the paper and linked artefact; locate the paper section/RQ/result that your bounded task corresponds to.
2. Confirm the bounded sample identifiers and enter them in the shared group workbook before running the main analysis.
3. Freeze RQ1/RQ2, method, metric/decision rule, expected result and non-reproduction condition.
4. Run only the minimum scripts/builds needed for the bounded target. Do not recreate a large research infrastructure when published data/output directly supports the target.
5. Keep raw/intermediate output, script/command version and repository/tag references needed to audit your result.

# Evidence you must keep

- Exact paper/artefact version or access date and bounded sample IDs.
- Commands/scripts/notebook cells or a clear manual coding rule.
- Raw/intermediate result supporting every quantitative/qualitative claim.
- Any deviation from the paper and the most important threat/limitation.
- Repository commits/tags and tests/verification for any design/refactoring/modernisation work.
- Only brief material AI-use notes when AI changed a decision or result interpretation.

# Important scope rule

Keep to the bounded task; do not reproduce the whole paper. Use the smallest public artefact route that still answers the RQs. If a genuine external artefact fails, record the failure and follow the module contingency; do not invent results.