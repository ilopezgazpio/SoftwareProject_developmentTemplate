# Product backlog · Team Hiru

*Three epics and twelve user stories. Each story is also a GitHub issue with the same id, created from the user story template. The Product Owner sets the priority label; the team estimates the points. Stories are not implemented in sprint 1: this sprint produces the specification.*

Priority: must / should / could · Points: 1, 2, 3, 5, 8 · Source: confirmed requirement CR-nn in `docs/client/meeting-01-discovery.md`.

## E1 · Datasets and experiments

**Labels:** epic
**Goal:** register a dataset and define an experiment so that every run is identifiable. Requirements CR-01, CR-03, CR-07.

### US-01 · Register a dataset

**Labels:** story, must, E1

**As a** researcher, **I want** to register the EusTrivia sample from a JSONL file under a version id **so that** every run says which dataset version it used.

**Source:** CR-01 · Epic E1

**Acceptance criteria**
- Given a JSONL file with 80 questions, when I register it as `eustrivia-sample` version `2026-11`, then the tool lists it with its id, version and number of questions.
- Given a file with a malformed line, when I register it, then the tool refuses it and tells me the line number.

**Planning:** must · 3 points · sprint 2

### US-02 · Write a prompt template

**Labels:** story, must, E1

**As a** researcher, **I want** to write a prompt template with placeholders for the question and its options **so that** the same prompt is used for every question and recorded with the run.

**Source:** CR-01 · Epic E1

**Acceptance criteria**
- Given a template with `{question}` and `{options}`, when I preview it on question 1, then I see the filled prompt.
- Given a template without `{question}`, when I save it, then the tool refuses it and says which placeholder is missing.

**Planning:** must · 2 points · sprint 2

### US-03 · Define an experiment

**Labels:** story, must, E1

**As a** researcher, **I want** to define an experiment as a dataset version, a prompt template, a provider and model, and its parameters **so that** a run is produced from a configuration I can read.

**Source:** CR-01 · Epic E1

**Acceptance criteria**
- Given a registered dataset and a saved prompt, when I define an experiment with provider `replay` and temperature 0, then the tool saves it and shows me the full configuration.
- Given an experiment, when I run it twice, then two runs exist and the first is unchanged.

**Planning:** must · 3 points · sprint 2

### US-04 · Open a saved run

**Labels:** story, must, E1

**As a** researcher, **I want** to open any saved run and see the exact configuration that produced it **so that** a month later I still know what I ran.

**Source:** CR-01, CR-03, CR-07 · Epic E1

**Acceptance criteria**
- Given a saved run, when I open it, then I see dataset id and version, prompt, provider, model and version if known, parameters and date.
- Given a saved run, when any later run is made, then the saved run's files are unchanged.

**Planning:** must · 2 points · sprint 2

## E2 · Run and record

**Labels:** epic
**Goal:** run an experiment, offline or live, and record every answer and every failure. Requirements CR-01, CR-02, CR-05.

### US-05 · Run offline from recorded answers

**Labels:** story, must, E2

**As a** researcher, **I want** to run an experiment with the recorded Latxa answers **so that** I can work and demonstrate without the live service.

**Source:** CR-02 · Epic E2

**Acceptance criteria**
- Given the recorded answers in `tests/fixtures/`, when I run the experiment with provider `replay`, then all 80 questions get a result without any network call.
- Given a question with no recorded answer, when I run, then that question is recorded as a failure, not skipped.

**Planning:** must · 5 points · sprint 2

### US-06 · Run against the live Latxa API

**Labels:** story, must, E2

**As a** researcher, **I want** to run an experiment against the Latxa API with my personal key **so that** I get genuine answers for a new prompt.

**Source:** CR-01 · Epic E2

**Acceptance criteria**
- Given a key in `.env` and provider `latxa`, when I run the experiment, then every question is sent once and the run stays under 40 requests per minute.
- Given no key in the environment, when I run with provider `latxa`, then the tool stops before the first request and tells me which variable to set.

**Planning:** must · 5 points · sprint 3

### US-07 · Record failures as failures

**Labels:** story, must, E2

**As a** researcher, **I want** timeouts, refusals and unreadable answers recorded as failures with their reason **so that** they never enter the score as wrong answers.

**Source:** CR-02 · Epic E2

**Acceptance criteria**
- Given a question whose request times out, when the run finishes, then that question has status `failure`, reason `timeout`, and no predicted option.
- Given a run with 3 failures, when I see its score, then the score is over 77 questions and "3 failures" is shown next to it.

**Planning:** must · 3 points · sprint 2

### US-08 · Map a free-text answer to an option

**Labels:** story, must, E2

**As a** researcher, **I want** the model's sentence mapped to one of the options, or marked unreadable, **so that** I do not decide by hand.

**Source:** CR-05 · Epic E2

**Acceptance criteria**
- Given the answer "Erantzuna Bilbo da" and the options A Bilbo, B Donostia, when the result is recorded, then the predicted option is A and the raw answer is kept.
- Given an answer that names two options or none, when the result is recorded, then the question is a failure with reason `unreadable`.

**Planning:** must · 5 points · sprint 2

## E3 · Inspect and compare

**Labels:** epic
**Goal:** see scores with honest counts, browse failures, compare two runs and export. Requirements CR-02, CR-04, CR-06.

### US-09 · List runs with honest scores

**Labels:** story, must, E3

**As a** researcher, **I want** a list of my runs with the accuracy over valid answers and the number of failures next to it **so that** I never read a score without its denominator.

**Source:** CR-02 · Epic E3

**Acceptance criteria**
- Given two saved runs, when I list runs, then each line shows id, date, model, accuracy, valid answers and failures.
- Given a run with 80 failures, when I list runs, then its accuracy is shown as not available, not as 0.

**Planning:** must · 3 points · sprint 3

### US-10 · Browse the failures of a run

**Labels:** story, should, E3

**As a** researcher, **I want** to see the failed questions of a run with the raw answer and the reason **so that** I can tell a model problem from a prompt problem.

**Source:** CR-02 · Epic E3

**Acceptance criteria**
- Given a run with failures, when I open its failures, then I see for each one the question id, the reason and the raw answer if any.
- Given a run without failures, when I open its failures, then I see "no failures".

**Planning:** should · 2 points · sprint 3

### US-11 · Compare two runs question by question

**Labels:** story, must, E3

**As a** researcher, **I want** to compare two runs on the same dataset question by question **so that** I see exactly where they differ, failures included.

**Source:** CR-04 · Epic E3

**Acceptance criteria**
- Given two runs on the same dataset version, when I compare them, then I see per question both predicted options, both statuses and whether they agree.
- Given two runs on different dataset versions, when I compare them, then the tool refuses and says why.

**Planning:** must · 5 points · sprint 3

### US-12 · Export a run as CSV

**Labels:** story, should, E3

**As a** colleague of the researcher, **I want** a run exported as CSV **so that** I can read the results in my spreadsheet.

**Source:** CR-06 · Epic E3

**Acceptance criteria**
- Given a saved run, when I export it, then I get one CSV row per question with id, predicted option, correct option, status and reason.
- Given the export, when I open it in a spreadsheet, then the score and failure count match what the tool shows.

**Planning:** should · 2 points · sprint 3
