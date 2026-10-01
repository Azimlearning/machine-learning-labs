# TEB3123 Machine Learning — Build Status

> **Read this first to know where we are.** Updated at the end of every build session. Phases and scope come from `refdocs/teb3123-ml-PRD.md` §6. Don't reorder phases without updating this file and saying why (CLAUDE.md "keep docs current").

**Build philosophy:** One lab at a time, in order. A lab is done when its notebook runs top to bottom from a clean kernel, its evidence is in `results/labNN/`, and it is pushed to GitHub.

**Right now:** Nothing is built. This project was scaffolded on 2026-10-01 — the docs, agent config, folder skeleton and the P0 plan exist; no lab code does. The next session starts at `refdocs/plans/2026-10-01-p0-environment-and-github.md`.

---

## Phase checklist

| Phase | Scope | Status |
|---|---|---|
| P0 | Environment + GitHub (conda `ml`, datasets, SSH, remote, first push) | ⬜ Not started |
| P1 | Lab 1 — features (Ch. 2–3) | ⬜ Not started |
| P2 | Lab 2 — supervised workflow | ⬜ Not started |
| P3 | Lab 3 — supervised models | ⬜ Not started |
| P4 | Lab 4 — clustering and PCA | ⬜ Not started |
| P5 | Lab 5 — anomaly detection, limited labels | ⬜ Not started |
| P6 | Lab 6 — reinforcement learning | ⬜ Not started |
| P7 | Lab 7 — CNN | ⬜ Not started |
| P8 | Lab 8 — LSTM | ⬜ Not started |
| P9 | Project and Tests 1–2 | ⬜ Not started |

Status vocabulary — use these exactly, and never round up:
- ⬜ **Not started**
- 🔶 **In progress** — say precisely what works and what doesn't
- ✅ **Done** — built *and* verified. If it compiles but was never run, it is not done.
- ⛔ **Blocked** — name the blocker and who/what unblocks it

---

## P0 — Environment + GitHub (current phase)

| Item | Approach | Status |
|---|---|---|
| Anaconda present | Already installed at `C:\Users\User\anaconda3` (conda 26.5.3, base Python 3.14.6) | ✅ Observed 2026-10-01 |
| Git identity | `user.name` and `user.email` already set globally | ✅ Observed 2026-10-01 |
| Conda env `ml` | Created at `C:\Users\User\anaconda3\envs\ml` (Python 3.12.14) | ✅ Done 2026-10-01 |
| Dependencies | `pip install -r requirements.txt` inside `ml` (numpy 2.5.3, pandas 3.0.6, scikit-learn 1.9.1, torch 2.14.1+cpu) | ✅ Done 2026-10-01 |
| Datasets | TA's `all_datasets.zip` extracted into `ML LAB/all_datasets/` (12 files) | ✅ Done 2026-10-01 |
| GitHub SSH key | No key in `~/.ssh` (only `known_hosts`) | ⬜ Not started |
| GitHub repo + remote | Public repo `Azimlearning/machine-learning-labs` created; `origin` set to the HTTPS URL (switch to SSH after the key exists) | 🔶 Repo exists, nothing pushed |
| First commit and push | Only when the user asks | ⬜ Not started |
| Compare with TA's layout | TA repo not readable (404) | ⛔ Needs the repo link or access |

---

## Verification ledger

What has actually been run, not what has been written. A row here needs a real command and a real result.

| Date | What was verified | How | Result |
|---|---|---|---|
| 2026-10-01 | Anaconda installed | `C:\Users\User\anaconda3\Scripts\conda.exe --version`, `conda env list` | conda 26.5.3; only `base` exists |
| 2026-10-01 | Base env course packages | `pip list` in anaconda base | numpy, pandas, matplotlib, scikit-learn, joblib, jupyter present; **torch absent** |
| 2026-10-01 | Python 3.12 availability | `py -0` | Only 3.13 registered; 3.12 not installed globally |
| 2026-10-01 | `ml` env works | `envs\ml\python.exe -c "import numpy, pandas, matplotlib, sklearn, joblib, torch"`; `-m jupyter --version` | Python 3.12.14; all imports succeed; torch is CPU-only (cuda False); jupyter present |
| 2026-10-01 | Datasets extracted | Python `zipfile.extractall`, then `ls -l ML LAB/all_datasets` | 11 CSVs + digits ZIP present, names match lab notes §2.1; git-ignored |
| 2026-10-01 | GitHub repo | `gh repo create ... --public`, then `gh repo view --json visibility,description,url` | PUBLIC, description set, url https://github.com/Azimlearning/machine-learning-labs; empty |
| 2026-10-01 | SSH key state | `ls ~/.ssh` | `known_hosts` only, no key pair |

---

## Known gaps

- Worked notebooks (`labNN_*_worked.ipynb`) and `predict_passenger.py` have not been provided; the TA presumably distributes them.
- No test suite and no linter; a lab is checked by running its notebook from a clean kernel.
- `requirements.txt` is unpinned (copied from the lab notes), so installs may drift between machines.
- Lab-to-week mapping, project topic and project brief are unknown until the brief (wk 6).
- No file-structure doc: the planned layout lives in `README.md`; write one once there are notebooks to describe.
- The hook layer is deliberately empty (D-06); revisit if an API key ever enters the project.
