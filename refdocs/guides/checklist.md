# Pre-Push Checklist — TEB3123 Machine Learning

> Run the relevant section before pushing or calling a phase done.
> Not every item applies to every change — use judgement based on what actually changed. But read the list; that's where you notice the thing you forgot.

---

## Every change

- [ ] **It was actually run.** Not "it looks right" — executed, and the result observed. If it wasn't run, say so rather than implying otherwise.
- [ ] **Build passes** — no build step in this project.
- [ ] **Tests pass** — no test suite yet, tracked in STATUS Known gaps. In place of tests: Jupyter → *Restart Kernel and Run All Cells* finishes with no error.
- [ ] **Lint/type check clean** — no linter configured.
- [ ] **No secrets staged** — `git status` shows no `.env*`, no key file; no key literal in the diff
- [ ] **No stray debug output** left in the diff — print statements, commented-out experiments
- [ ] **Changelog entry added** — `refdocs/changelog/CHANGELOG.md`, including an honest **Verified** line
- [ ] **STATUS.md reflects reality** — the phase table doesn't round up, and the verification ledger has a row for what you just ran
- [ ] **Docs match what you built** — if the work diverged from the execution doc, that doc is edited, not left stale

---

## New dependency

- [ ] Line added to `ML LAB/requirements.txt` (installed with `pip` inside `ml`)
- [ ] Recorded in `refdocs/teb3123-ml-sources.md` with why it was chosen
- [ ] Its actual docs were read — the API was not recalled from memory

---

## Architectural decision

- [ ] ADR in `refdocs/changelog/DECISIONS.md` — Decision → Why → Trade-offs/rejected
- [ ] Same id added to the PRD's §7 Decision Log
- [ ] Any `ASSUMED:` it resolves is deleted from the assumptions list

---

## Before pushing a lab submission

- [ ] Notebook ran top to bottom from a clean kernel, no errors
- [ ] **Leakage check:** the split happens first; every imputer, scaler, encoder and selector is fitted on training rows only, inside a `Pipeline`; the test set was used once
- [ ] `results/labNN/` and `models/` hold what that run generated — nothing hand-edited
- [ ] No dataset, `.venv`, lecture slide or lab PDF is staged (`git status`)
- [ ] `requirements.txt` includes every import the notebook uses
- [ ] You can explain each step of the notebook without looking at it
- [ ] The user said to commit and push (CLAUDE.md rule 5)
- [ ] After the push, the lab is visible on GitHub in the layout the TA expects
