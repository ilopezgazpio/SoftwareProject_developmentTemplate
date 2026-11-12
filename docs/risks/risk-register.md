# Risk register · Team Hiru

*At least five risks, each with an owner and a mitigation. P = probability, I = impact, both from 1 (low) to 3 (high). Updated at every review.*

| Id | Risk (what could happen, and its effect) | P | I | Owner | Mitigation | Status |
|---|---|---|---|---|---|---|
| R-01 | Latxa keys arrive late or the rate limit blocks a run, so the live path cannot be shown | 2 | 2 | Codex | Everything works first with the replay provider; the live path is a configuration switch | open |
| R-02 | Mapping free-text answers to options is unreliable, so the accuracy is wrong without anyone noticing | 3 | 3 | Iñigo | Unreadable answers are failures, never guesses; the failure count is always shown next to the score | open |
| R-03 | A member is unavailable for a week, so their tasks stop | 2 | 2 | Claude | At most two cards per person; every document is in the repository, not on a laptop | open |
| R-04 | After 17 November the client is switched off and we discover a question we never asked | 3 | 2 | Iñigo | Specification review on 16 November with the full list of stories; open points recorded and decided by the Product Owner | open |
| R-05 | A key or the dataset is committed by mistake | 1 | 3 | Codex | `.env` and `data/` in `.gitignore`; `.env.example` without values; the reviewer checks every pull request | open |
