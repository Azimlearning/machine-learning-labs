# Execution — P0 Environment and GitHub

> Plan: `refdocs/plans/2026-10-01-p0-environment-and-github.md`. Tasks run top to bottom. Each task carries its own **Verify** step, and a task is not done until its Verify actually passes — not when the code compiles.
> If reality diverges from this doc, **edit this doc** (CLAUDE.md rule 4). A stale execution doc is worse than none.

## Before starting

- Anaconda installed (observed). Use **Anaconda PowerShell Prompt**, because `conda` is not on PATH elsewhere.
- Internet access; a Kaggle account (for dataset downloads) and a GitHub account.
- No commit or push happens without the user's explicit go-ahead (CLAUDE.md rule 5).

---

## Task 1 — Create the `ml` environment

**Files:** none (creates `C:\Users\User\anaconda3\envs\ml`).

```powershell
conda create -n ml python=3.12
conda activate ml
```

**Verify:** `python --version` prints `Python 3.12.x`, and `python -c "import sys; print(sys.executable)"` prints a path containing `envs\ml`.

## Task 2 — Install dependencies

**Files:** reads `ML LAB/requirements.txt` (numpy, pandas, matplotlib, scikit-learn, joblib, jupyter, torch).

```powershell
cd "C:\Users\User\Documents\UTP COURSE\Machine Learning\ML LAB"
python -m pip install --upgrade pip
pip install -r requirements.txt
```

The torch download is large. If any package fails, copy the error verbatim into the changelog and stop; do not mix in `conda install`.

**Verify:** `python -c "import numpy, pandas, matplotlib, sklearn, joblib, torch; print(torch.__version__, sklearn.__version__)"` prints two versions and no traceback. Also `jupyter --version` runs.

## Task 3 — Download datasets

**Files:** `ML LAB/all_datasets/*` (git-ignored except its README).

Open each link in `ML LAB/all_datasets/README.md`, download, extract, and copy the CSVs into `all_datasets/`. Keep `optical_recognition_handwritten_digits.zip` as a ZIP. Filenames must match the lab notes exactly, including capitalisation; rename only if the Kaggle name differs, and note it in the README.

**Verify:** `Get-ChildItem "ML LAB\all_datasets"` lists the 11 expected items from the README table (10 CSVs, counting the two Bike Sharing files, plus the digits ZIP).

## Task 4 — Create and register an SSH key

**Files:** `~/.ssh/id_ed25519` and `.pub` (outside the repo).

Follow the TA's Windows video, cross-checking with `refdocs/guides/env_setup.md` §GitHub SSH. Copy only the `.pub` file's contents to GitHub → Settings → SSH and GPG keys.

**Verify:** `ssh -T git@github.com` prints `Hi <username>! You've successfully authenticated, but GitHub does not provide shell access.` Run it in the same shell you will use to push.

## Task 5 — Create the repo and remote

**Files:** `.git/config`.

Create an empty repository on GitHub (no README, so histories don't diverge). Ask the TA for the expected name (the reference repo is `MACHINE-LEARNING`) and visibility. Then:

```powershell
cd "C:\Users\User\Documents\UTP COURSE\Machine Learning"
git remote add origin git@github.com:<your-username>/<repo-name>.git
git branch -M main
```

**Verify:** `git remote -v` shows the SSH URL for fetch and push.

## Task 6 — First commit and push (only on the user's go-ahead)

Before asking, run `git status` and confirm no dataset, PDF, `.venv`, `.env*` or key file is staged. Use the "Before pushing" section of `refdocs/guides/checklist.md`. After approval: `git add -A`, review `git status`, commit, then `git push -u origin main`.

**Verify:** the repo page on GitHub shows `CLAUDE.md`, `README.md`, `refdocs/`, `.claude/` and `ML LAB/` with its READMEs and `requirements.txt`, and **no** datasets, PDFs or `.venv`.

## Task 7 — Reconcile with the TA's layout

Once the TA's repo is readable, compare its tree with the README's Project layout. If it differs, write an ADR (supersedes D-01 if needed) and adjust.

**Verify:** a written comparison in the changelog, or an explicit "TA repo still not readable".

---

## Wrap-up (do not skip)

- [ ] `refdocs/STATUS.md` — phase table updated, verification ledger updated with what was actually run
- [ ] `refdocs/changelog/CHANGELOG.md` — session entry added
- [ ] `refdocs/changelog/DECISIONS.md` — any new ADR, any resolved `ASSUMED:`
- [ ] This doc updated to match what actually happened
- [ ] Plan and execution index rows in `plans/README.md` and `execution/README.md` updated
