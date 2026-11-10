# The board

The GitHub project board is the single place that says what each person is doing. The sprint plan says what we intended; the board says what is happening.

## Columns

| Column | Meaning | Who moves the card |
|---|---|---|
| Backlog | Product backlog stories not in this sprint | the Product Owner |
| Sprint 1 | Chosen for this sprint, nobody has started | anyone, when signing up |
| In progress | Someone is working on it. At most two per person | the owner |
| Review | The result is in the repository; another member has to check it | the owner |
| Done | The definition of done is met and the issue is closed | the reviewer |

## Snapshot on 12 November

| Backlog | Sprint 1 | In progress | Review | Done |
|---|---|---|---|---|
| US-01 to US-12 | T-08 Refinement meeting (Iñigo) | | T-05 Use cases and requirements (Codex) | T-01 Team charter |
| | T-09 Specification review (Iñigo) | | T-07 Risk register (Codex) | T-02 Discovery meeting |
| | T-10 Sprint report and retrospective (Claude) | | | T-03 Product vision |
| | | | | T-04 Product backlog |
| | | | | T-06 Diagrams |

## Creating the board

Labels, milestone, issues and the board are created once from the backlog files with
`python scripts/create_issues.py OWNER/REPO`. After that, everything happens on GitHub.
