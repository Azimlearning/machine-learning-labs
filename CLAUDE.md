# TEB3123 Machine Learning — Claude Context

> Read this file at the start of every session, then run through `.claude/memory/preflight.md` — it's the six-question gate that turns these rules into something you actually did. Course workspace for TEB3123 Machine Learning (UTP, Sept 2026): weekly labs, a project and two tests, with lab and project work graded through a GitHub repo.
> The PRD is the source of truth; this file is the short operating brief; preflight is the gate. Keep all three short.

---

## Order of authority (when docs conflict, surface it — don't resolve silently)

0. `refdocs/STATUS.md` — **where we are right now.** Phase checklist + the current lab's progress. Check this first, every session.
1. `refdocs/teb3123-ml-PRD.md` — **what & why.** Owns scope, structure, roadmap, Decision Log.
2. `refdocs/changelog/DECISIONS.md` — **settled calls.** Read before re-debating a choice.
3. `refdocs/plans/*.md` — **what to build & why.**
4. `refdocs/execution/*.md` — **how & in what order.**
5. `refdocs/guides/` — **operational reference.** `env_setup.md` (environment, GitHub SSH), `checklist.md` (pre-push).
6. `refdocs/teb3123-ml-sources.md` — **raw research** (course material, datasets, links).

If two docs disagree, stop and ask. Don't pick one and move on.

---

## Mandatory rules

### 1. Update the changelog after every session
After any session that changed code, made a decision, or modified a plan, add an entry to **`refdocs/changelog/CHANGELOG.md`** (format is in that file). Do not skip. Even a one-line fix gets a one-line entry.

### 2. Plan before you build
Before starting a lab or the project, a **plan doc** (`refdocs/plans/`) and an **execution doc** (`refdocs/execution/`) must exist. If they don't, create them before writing code (`/plan-feature`).

### 3. Log decisions as ADRs
New design decision → add an ADR to `refdocs/changelog/DECISIONS.md` (Decision → Why → Rejected/Trade-off). Mark unresolved assumptions `ASSUMED:` and surface them at the next checkpoint.

### 4. Keep docs current
If you deviate from a plan during execution, update the execution doc to match reality. Stale docs are worse than no docs.

### 5. Never commit or push without asking
Labs and the project are graded from the GitHub repo, so every commit and push is deliberate. Stage nothing and push nothing until the user says so.

### 6. Explain, don't just solve
Labs carry marks and Tests 1 and 2 follow. When writing lab code, say why each step is there (what it prevents or enables) so the user can reproduce it unaided.

---

## The hard constraints (these are mechanism, not preference)

1. **Graded through GitHub.** "Your lab submissions and project will be assessed via your GitHub repo; any students who fail to do so will not get marks for the labs." (TA, WhatsApp 2026-09-25). No repo, no lab marks.
2. **Fit data-dependent steps on training rows only.** Split first; learn imputers, scalers, encoders, selectors and thresholds inside a `Pipeline` on the training split; apply unchanged to validation/test. The test set is used once, at the end (lab notes Ch. 3.5–3.7).
3. **Do not hand-edit generated outputs.** Notebooks write models and cards to `ML LAB/models/` and evidence to `ML LAB/results/labNN/`. Re-run the notebook instead of editing the output (lab notes §2.1).
4. **Raw data is read-only.** Keep source files unchanged; clean via a scripted transformation or a copy. On `FileNotFoundError`, fix the path and working directory — do not move files into the project root (lab notes §2.2.1, Ch. 3.4.2).
5. **One environment, pip only.** Conda env `ml` (Python 3.12), packages from `ML LAB/requirements.txt` via `pip`. Never mix conda and pip for the same package; never install into `base`. CPU is sufficient (lab notes §2.5–2.6).
6. **requirements.txt invariant.** A new third-party `import` in any notebook or script means a line in `ML LAB/requirements.txt` in the same change (see preflight Q5).
7. **Attendance counts.** Lab attendance carries marks, and missing three sessions without prior approval means barred from the final exam (Lecture 1; TA, 2026-09-25).

---

## Stack

Python 3.12, conda env `ml`. numpy, pandas, matplotlib, scikit-learn, joblib, jupyter, torch (CPU; Labs 7–8). Source of record for versions: `ML LAB/requirements.txt` (currently unpinned).

## Surfaces

Single repo, single app. Workspace root is `Machine Learning/` (docs, `.claude/`, git). All lab work lives in `ML LAB/`, which plays the role of the lab notes' `UTP-MACHINE-LEARNING/` root. `ML LECTURE/` holds slides (local only).

## Running it

| What | Command | Notes |
|---|---|---|
| Open a conda shell | Start menu → *Anaconda PowerShell Prompt* | `conda` is **not** on PATH in a normal terminal |
| Create env (once) | `conda create -n ml python=3.12` | Not created yet — see P0 plan |
| Activate (every session) | `conda activate ml` | Check: `python -c "import sys; print(sys.executable)"` |
| Install deps (once, after activate) | `pip install -r "ML LAB/requirements.txt"` | Do not re-run unless requirements change |
| Notebooks | `jupyter notebook` from `ML LAB/all_experiments/` | Worked notebooks are not in the folder yet |
| Env python without activating | `C:\Users\User\anaconda3\envs\ml\python.exe` | Only exists once `ml` is created |

---

## Build sequence

P0 environment + GitHub → P1 Lab 1 (features) → P2 Lab 2 (supervised workflow) → P3 Lab 3 (models) → P4 Lab 4 (clustering/PCA) → P5 Lab 5 (anomaly/limited labels) → P6 Lab 6 (RL) → P7 Lab 7 (CNN) → P8 Lab 8 (LSTM) → P9 Project and tests. Dates are driven by the course calendar (Test 1 wk 5, Project brief wk 6, Test 2 wk 10, Project due wk 10, presentations wk 11–12, final wk 13–14); see PRD §6.

**Never build the second of anything until the first is green end-to-end.**

---

## When blocked

- **Open question:** check the PRD's Open Questions section. If unresolved, write your assumption to `DECISIONS.md` as `ASSUMED:`, proceed, surface at the next checkpoint.
- **Doc conflict:** stop. Quote both passages and ask. Don't pick silently.
- **Ambiguous spec:** prefer the option that matches the lab notes and the TA's reference repo. Log the choice.

---

*Companion brief to `refdocs/teb3123-ml-PRD.md`. Last updated: 2026-10-01.*
