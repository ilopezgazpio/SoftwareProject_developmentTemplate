# Requirements · LM Evaluation Platform

*Stakeholders, two use cases and the constraints. The user stories with their acceptance criteria are in `docs/backlog/product-backlog.md` and in the issues; they are not repeated here.*

## 1. Stakeholders

| Stakeholder | Interest | How we involve them |
|---|---|---|
| Unai, researcher | Runs evaluations and trusts the numbers | Client meetings until 17 November |
| His colleague | Reads a table with score and failures | Through Unai, CR-06 |
| HiTZ | Provides the Latxa API under its conditions | Personal keys, 40 requests per minute, no personal data in prompts |
| Instructors | Assess process and product | Reviews at S06, midterm and final |

## 2. Use cases

### UC-1 · Run an experiment

| | |
|---|---|
| **Actor** | Researcher |
| **Precondition** | A dataset is registered, a prompt template and an experiment are defined |
| **Main flow** | 1. The researcher starts the experiment. 2. The tool builds the prompt for each question. 3. The provider answers each prompt. 4. The tool maps each answer to an option. 5. The tool saves the run with its configuration and every per-question result. 6. The tool shows accuracy over valid answers and the number of failures. |
| **Alternative flows** | 3a. The provider times out or refuses: the question is recorded as a failure with its reason, the run continues. 4a. The answer cannot be mapped: the question is recorded as a failure, reason `unreadable`. |
| **Postcondition** | A new run exists. No earlier run has changed. |
| **Stories** | US-03, US-05, US-06, US-07, US-08, US-09 |

### UC-2 · Compare two runs

| | |
|---|---|
| **Actor** | Researcher |
| **Precondition** | Two saved runs on the same dataset version |
| **Main flow** | 1. The researcher chooses two runs. 2. The tool pairs their results by question id. 3. The tool shows, per question, both predicted options, both statuses and whether they agree. 4. The researcher exports the comparison or a run as CSV. |
| **Alternative flows** | 2a. The runs use different dataset versions: the tool refuses and says why. |
| **Postcondition** | Nothing is changed. |
| **Stories** | US-04, US-10, US-11, US-12 |

## 3. Constraints

- Python and GitHub. A command-line tool; no web interface in this course.
- The Latxa API is a shared service: personal keys, at most 40 requests per minute, errors handled, never called from automated tests.
- The whole demonstration runs from the recorded answers, with no network.
- Keys, data files and personal data never enter the repository.
- Runs are immutable once saved.
