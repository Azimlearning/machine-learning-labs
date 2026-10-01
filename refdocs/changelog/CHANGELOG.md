# TEB3123 Machine Learning — Changelog

> Mandatory session log. Add an entry after **every** session where code changed, a decision was made, or a plan was modified. Newest first. Even a one-line fix gets a one-line entry.

Entry format:
```
### YYYY-MM-DD — [short summary of session goal]
- **Changed:** what files/components were touched and why
- **Decided:** any architectural or design decisions and the reasoning
- **Deviations:** anything that differed from the plan, and why
- **Verified:** what was actually run, and the result (not "should work")
- **Known issues / next steps:** what was left open
```

Those five lines are the floor, not the ceiling. Add these when the session earns them — a debugging session in particular is unreadable without the first two:
- **Reported:** the symptom in the user's own words, before you knew the cause
- **Diagnosed:** what you found, and how you proved it — the reproduction, not the hypothesis
- **Trade-off:** what this change costs, and who it costs it to
- **Noted, not changed:** something you found and deliberately left alone, so the next session doesn't re-investigate it

Rules that make this file worth keeping:
- **"Verified" means a command was run.** Name it and give the result. If nothing was run, write "nothing verified this session" — that is useful information.
- **Deviations are the most valuable line.** A plan that changed silently is a plan nobody will trust next time.
- **Write what you learned, not what you touched.** "Fixed the player" ages into nothing. "The provider's iframe navigates the top context, which sandbox flags block" is still worth reading in six months.
- Don't rewrite history. Corrections go in a new entry that references the old one.

---

## [Unreleased]

### 2026-10-01 — Environment, datasets, GitHub repo
- **Changed:** Created conda env `ml` (Python 3.12.14) and installed `requirements.txt`; extracted the TA's `all_datasets.zip` into `ML LAB/all_datasets/`; added `/all_datasets.zip` to `.gitignore`; rewrote `README.md` with student details and a per-lab table; created the public GitHub repo and set `origin`; renamed the git branch to `main`.
- **Decided:** Repo name `machine-learning-labs` (the user typed `machaine-learning-labs`, treated as a typo; rename is one `gh repo rename`). Remote uses HTTPS for now because no SSH key exists yet.
- **Deviations:** P0 task 5 planned an SSH remote; HTTPS is in use until the key is created.
- **Verified:** `envs\ml\python.exe -c "import numpy, pandas, matplotlib, sklearn, joblib, torch"` succeeded (torch 2.14.1+cpu); `gh repo view` shows PUBLIC with the description. Nothing pushed; no commit made.
- **Known issues / next steps:** SSH key still to create (user's task); first commit and push awaits the user's go-ahead; TA's repo layout still unread.

### 2026-10-01 — Project scaffolded
- **Changed:** Created the project doc system — `refdocs/` (PRD, STATUS, sources, guides/, changelog/DECISIONS, plans/, execution/), `CLAUDE.md`, `README.md`, `.gitignore`, `.claude/` (settings, agents, commands, memory/preflight), and the `ML LAB/` skeleton (folder READMEs, `requirements.txt` copied from lab notes). No lab code yet.
- **Decided:** Lab tree inside `ML LAB/` (D-01); conda env `ml` on Python 3.12 (D-02, after finding Anaconda already installed); four subagents (D-04); four binding workflow rules (D-05); no secret hook (D-06); requirements.txt invariant as preflight Q5 (D-07).
- **Deviations:** The user first chose a venv, then switched to conda after the Anaconda check. TA's reference repo returned 404, so its layout was not read.
- **Verified:** Anaconda state, installed Pythons and `~/.ssh` contents were checked with real commands (see STATUS verification ledger). Nothing else to verify — no code exists yet.
- **Known issues / next steps:** Nine `ASSUMED:` items are open (PRD §8). Next session starts from `refdocs/plans/2026-10-01-p0-environment-and-github.md`.
