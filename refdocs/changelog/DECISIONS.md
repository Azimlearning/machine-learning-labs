# Architectural Decisions — TEB3123 Machine Learning

> Record decisions here so they aren't re-debated in future sessions.
> Format: **Decision** → **Why** → **Trade-offs / what was rejected**.
> Canonical one-line list lives in `refdocs/teb3123-ml-PRD.md` §7; this file expands the load-bearing ones under the same id.

An ADR is worth writing when the decision (a) is expensive to reverse, (b) will look arbitrary to a future reader, or (c) had a real alternative someone will propose again. Everything else is just a commit message.

---

## D-01 — Workspace root is `Machine Learning/`; lab tree inside `ML LAB/`

- **Decision:** Git root and docs at `Machine Learning/`. `all_datasets/`, `all_experiments/`, `models/`, `results/` and `requirements.txt` live in `ML LAB/`, which stands in for the lab notes' `UTP-MACHINE-LEARNING/`.
- **Why:** The user already keeps all lab material in `ML LAB/` and asked to match the lab notes' layout inside it.
- **Trade-offs:** The repo layout may differ from the TA's reference repo (not readable, see A-03). If the TA expects `all_experiments/` at the repo root, move `ML LAB/`'s contents up and update every path in the docs.

## D-02 — Conda env `ml`, Python 3.12, pip for packages

- **Decision:** `conda create -n ml python=3.12`, then `pip install -r "ML LAB/requirements.txt"`.
- **Why:** Anaconda is already installed and works. Lab notes Route B prescribes exactly this, and the course libraries (notably torch) support 3.12. Anaconda's base is Python 3.14 and has no torch, and installing into `base` is discouraged.
- **Trade-offs / rejected:** The user first picked a `venv` on Python 3.12 (Route A), then switched once Anaconda was found installed. A venv would have needed a separate Python 3.12 install. Python 3.13 (installed) was rejected as less safe for torch wheels; this is cautious rather than verified.

## D-04 — Four subagents

- **Decision:** `doc-keeper`, `lab-runner`, `lecture-notes-explainer` (read-only), `codebase-explorer` (read-only).
- **Why:** The user accepted the full offered set. Each maps to a recurring task: closing sessions, verifying a notebook, answering from slides, searching notebooks.
- **Trade-offs:** Every agent definition costs context each session; prune any that go unused.

## D-05 — Binding workflow rules

- **Decision:** No commit or push unasked; fit preprocessing on training rows only; never hand-edit `models/` or `results/`; explain rather than just solve.
- **Why:** User accepted all four. Labs are graded from GitHub, so pushes must be deliberate; the leakage rule is the course's central evaluation principle (Ch. 3.7).
- **Trade-offs:** "Explain, don't just solve" makes sessions slower by design.

## D-06 — No secret-guard hook

- **Decision:** No `PreToolUse` secret hook; `.gitignore` also excludes key-shaped files.
- **Why:** The project has no API keys or `.env`. The only secret is the SSH private key in `~/.ssh`, outside the repo.
- **Trade-offs:** If a Kaggle API token or similar is added later, add `assets/check_secrets.py` from the `/newproject` skill and write an ADR.

## D-07 — Preflight Q5 is the requirements.txt invariant

- **Decision:** "New import means new `requirements.txt` line" is the project invariant, enforced as prose.
- **Why:** The first half (the notebook) runs on this machine, so the break only appears on someone else's clean environment.
- **Trade-offs:** Not mechanically checkable cheaply, so no hook. A script comparing imports to requirements could be added later.

(D-03 is a layout convention and is recorded only in the PRD log.)

---

## Working assumptions (`ASSUMED:`)

Not decisions — guesses made to keep moving. Each one must be confirmed or killed before anything load-bearing is built on it. When one is resolved, delete it here and write a real ADR above.

- **A-01** ASSUMED: native Windows, not WSL.
- **A-02** ASSUMED: datasets, `ML LECTURE/` and lab PDFs are not committed (git-ignored).
- **A-03** ASSUMED: the TA's repo layout matches lab notes §2.1 (repo not readable).
- **A-04** Unknown: lab-to-week mapping and project topic.
- **A-05** ASSUMED: the upcoming Feature Extraction lab is Lab 1.
- **A-06** ASSUMED: notebooks read data via `../all_datasets/` from `all_experiments/`.
- **A-07** Partly resolved: public repo `Azimlearning/machine-learning-labs` (user wrote `machaine-learning-labs`; treated as a typo). Unknown: TA's required name and collaborator access.
- **A-08** ASSUMED: `models/` and `results/` are committed as lab evidence.
- **A-09** ASSUMED: Windows SSH video is `YT5YimhyX18`, macOS is `ACvE5Uy7ZB0` (inferred from message order).
