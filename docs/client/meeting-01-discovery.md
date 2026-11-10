# Meeting 1: discovery

*One file per meeting, newest first, written by the scribe within 24 hours. Only the requirements listed as confirmed count as requirements of the project.*

| | |
|---|---|
| **Date and session** | 10 November 2026, S03, in class |
| **Duration** | 20 minutes |
| **Product Owner · scribe** | Iñigo · Claude |
| **Also present** | Codex |
| **Export** | [exports/2026-11-10-discovery.md](exports/2026-11-10-discovery.md) |

**What we wanted to learn**

- How Unai runs an evaluation today, from dataset to number.
- Which mistakes hurt most if nobody notices.
- What "reproduce an experiment" means to him.

**Questions and answers**

| # | Question | Answer |
|---|---|---|
| 1 | Walk us through the last evaluation you ran. | A JSONL file with 80 EusTrivia questions, a prompt pasted into a script, Latxa answers in a CSV, then a spreadsheet to count. The spreadsheet is called results_FINAL_v7.xlsx. |
| 2 | What do you lose when you come back to a result a month later? | Which prompt and which model version produced it. He has thrown away results for that reason. |
| 3 | What happens when the model does not answer? | Today it becomes an empty cell and the spreadsheet counts it as wrong. He wants to know how many questions were not answered. |
| 4 | How do you know which option the model chose? | He reads the answer. The model writes a sentence, not a letter. Sometimes it is not clear, and he decides by hand. |
| 5 | How do you compare two runs? | Side by side in the spreadsheet, by hand, question by question. That is what takes the most time. |
| 6 | What does "reproduce this experiment" mean to you? | Being able to see exactly what was run and run it again. He knows the answers may differ. |
| 7 | Who else sees the results? | A colleague who only wants a table with the number and the number of failures. |

**Confirmed requirements**

| Id | Requirement (a need, not a solution) | Why it matters to the client | Priority |
|---|---|---|---|
| CR-01 | Every result records the dataset version, prompt, model and settings that produced it | Results without this are thrown away | must |
| CR-02 | Questions that got no valid answer are counted as failures, shown next to the score, never as wrong answers | The score is otherwise wrong and nobody notices | must |
| CR-03 | A new run never overwrites an earlier one | He has lost runs that way | must |
| CR-04 | Two runs can be compared question by question, failures included | This is the slowest part of his work today | must |
| CR-05 | The model's free-text answer is mapped to one of the options; if that is not possible, the question is a failure | He decides by hand today | must |
| CR-06 | A run can be exported as CSV | His colleague and his spreadsheet keep working | should |
| CR-07 | "Reproduce" means recovering the exact configuration, not identical answers | Sets what we promise | should |

**Open points**

- Which second model, if any, he wants to compare Latxa with.
- Whether datasets other than EusTrivia will arrive in the same format.

**Next steps**

- Refinement meeting on Friday 13 November with the 12 user stories.
- Specification review on Monday 16 November, before the client is switched off.
