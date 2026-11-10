# Product vision · LM Evaluation Platform

| | |
|---|---|
| **Team** | Hiru |
| **Project and client** | P2 · Unai, computational linguist, Basque language-model evaluation |

## 1. Product goal

A small tool with which Unai runs an evaluation of a language model on a multiple-choice dataset and, a month later, still knows exactly what produced every number.

## 2. Vision

**For** researchers who evaluate language models on Basque datasets, **who** today keep results in CSV files and a spreadsheet, **the** LM Evaluation Platform **is a** command-line tool **that** records every run with its full configuration, counts failures honestly and compares two runs question by question. **Unlike** the spreadsheet, **our product** never loses a run and never scores a non-answer as a wrong answer.

## 3. Line of research

Evaluation of Basque and multilingual language models at HiTZ, using the EusTrivia sample (80 questions) and the Latxa model through its API.

## 4. Users

| Who | What they need | Confirmed in |
|---|---|---|
| Unai, the researcher | Run, record and compare evaluations without losing anything | CR-01 to CR-05, CR-07 |
| His colleague, a reader of results | A table with the score and the number of failures | CR-06 |

## 5. Epics

| Epic | Goal | Confirmed requirements | Priority |
|---|---|---|---|
| E1 · Datasets and experiments | Register a dataset and define an experiment so that every run is identifiable | CR-01, CR-03, CR-07 | must |
| E2 · Run and record | Run an experiment, offline or live, and record every answer and every failure | CR-01, CR-02, CR-05 | must |
| E3 · Inspect and compare | See scores with honest counts, browse failures, compare two runs, export | CR-02, CR-04, CR-06 | should |

## 6. Scope

**In:** one dataset format (JSONL), multiple-choice tasks, the Latxa provider and a replay provider with recorded answers, saved runs as files, a command-line interface, CSV export.

**Out:** training or fine-tuning, full benchmark suites, LLM-as-a-judge, dashboards, byte-identical repeatability, a web interface, any comparison that needs a live API call.

## 7. Data

| Data | Source | Licence | Size | Where it is kept (not in Git) |
|---|---|---|---|---|
| EusTrivia sample, 80 questions | Instructors, eGela | Course use only | 80 rows, JSONL | `data/`, downloaded by each member |
| Recorded Latxa answers to the 80 questions | Instructors, eGela | Course use only | 80 answers, JSON | `tests/fixtures/`, committed: these are the replay answers |

## 8. Success criteria

- Unai runs the 80 questions offline from the recorded answers and gets the score with the failure count next to it.
- He opens any saved run and sees its dataset version, prompt, model and settings.
- He compares two runs and sees, per question, where they differ, failures included.
