# LM Evaluation Platform · Team Hiru

Software Project (Language Technologies) · Master HAP/LAP · EHU · 2026-27
Project **P2 · Language Model Evaluation Platform** · Client: **Unai**, computational linguist (played by Latxa)

> **This repository is a worked example.** It shows what a team's repository looks like at the
> Sprint 1 review (S06, 17 November): which files exist, where they live, who writes them and how
> the board and the issues are used. It is deliberately small. Copy its **structure**, not its
> content: your client, your project and your decisions are different.

## The team

| Member | Role in sprint 1 | Belbin roles (P / M) | Looks after |
|---|---|---|---|
| Iñigo | Product Owner | Co-ordinator / Shaper | the client, the order of the backlog, the vision |
| Claude | Scrum Master | Plant / Monitor Evaluator | the board, the sprint plan, the retrospective |
| Codex | Developer | Implementer / Completer Finisher | the skeleton, the risk register, checking documents |

Roles rotate at the start of sprint 2. See [docs/team/team-charter.md](docs/team/team-charter.md).

## What is where

| Folder | What it holds | Written by |
|---|---|---|
| `docs/team/` | Team charter: roles, rules, how we decide, signatures | the whole team, S02 |
| `docs/belbin/` | Belbin roles of each member and the team diagnosis | Claude, S02 |
| `docs/client/` | One log per meeting with Unai, plus the exported conversations | Iñigo (Product Owner) |
| `docs/product/` | Product vision | Iñigo |
| `docs/backlog/` | Product backlog: 3 epics, 12 user stories. Each one is also a GitHub issue | Claude |
| `docs/requirements/` | Stakeholders, two use cases, constraints | Codex |
| `docs/uml/` | Component diagram and deployment diagram | Claude |
| `docs/risks/` | Risk register | Codex |
| `docs/sprints/` | Sprint plan, sprint report and retrospective, one set per sprint | Claude |
| `docs/board/` | How we use the GitHub project board, with a snapshot | Claude |
| `lmeval/` | Dummy Python skeleton: one module per component of the diagram, nothing implemented | Codex |
| `scripts/` | `create_issues.py`: creates the labels, issues and board on GitHub from the backlog files | Claude |

## Sprint 1 checklist

What eGela asks for on 17 November, and where it is here.

| Deliverable | File | Status on 12 Nov |
|---|---|---|
| Team charter | `docs/team/team-charter.md` | done |
| Product vision | `docs/product/vision.md` | done |
| Client meeting logs with confirmed requirements | `docs/client/meeting-01-discovery.md` | done; refinement and specification review meetings pending |
| 10 to 15 user stories as issues | `docs/backlog/product-backlog.md` and the Issues tab | done |
| Requirements (use cases, stories, constraints) | `docs/requirements/requirements.md` | in review |
| Architecture (component and deployment diagrams) | `docs/uml/` | done |
| Risk register | `docs/risks/risk-register.md` | in review |
| Sprint 1 plan with the definition of done | `docs/sprints/sprint-1-plan.md` | done |
| Sprint 1 report | `docs/sprints/sprint-1-report.md` | at S06 |
| Retrospective 1 | `docs/sprints/retrospective-1.md` | at S06 |

We keep every document as Markdown so GitHub renders it and every change is visible in the
history. For the eGela submission each document is exported to PDF (opening it on GitHub and
printing to PDF is enough).

## How we work in Git during sprint 1

- `main` holds what has been reviewed. We work on the branch `Sprint1`. At the sprint review the
  branch is merged into `main` through a pull request, reviewed by a member who did not write it.
- Every member commits with their own GitHub account. That is the evidence of who did what.
- Every story and every task is an issue. The board shows where each one is; move your own cards.
- Keys and data never enter the repository: `.env` and `data/` are ignored. `.env.example` lists
  the variables without values.
- No code is expected in sprint 1. The skeleton exists only so the diagrams and the code use the
  same names.

## Running the skeleton

```bash
python -m lmeval
```

It prints the components and says that nothing is implemented yet. That is correct for sprint 1.
