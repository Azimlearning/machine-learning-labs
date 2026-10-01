# Plan — P0 Environment and GitHub

> Phase P0 of `refdocs/teb3123-ml-PRD.md` §6. Execution doc: `refdocs/execution/2026-10-01-p0-environment-and-github.md`.
> A plan says **what and why**. The execution doc says **how and in what order**. Keep them separate — when they merge, both stop being read.

## Why this exists

Labs start with code in the next session (Feature Extraction, Ch. 2–3), and lab marks depend on a working GitHub repo (TA, 2026-09-25). The TA's weekend task is the GitHub SSH setup. This phase gets a working Python environment and a pushable repo in place so lab time goes on code.

## What's already covered (no work needed)

- Anaconda is installed at `C:\Users\User\anaconda3` (conda 26.5.3) — observed 2026-10-01.
- Git 2.47 and gh 2.94 are installed, and `user.name`/`user.email` are set — observed.
- The `ML LAB/` folder skeleton, `requirements.txt` and all docs were scaffolded on 2026-10-01.
- `git init` and `.gitignore` were done by the scaffold (see CHANGELOG); no commit has been made.

## Scope

**In:**
- Create conda env `ml` (Python 3.12) and install `requirements.txt`, including torch.
- Download the 11 Kaggle datasets into `ML LAB/all_datasets/`.
- Create an SSH key, register it on GitHub, verify `ssh -T git@github.com`.
- Create the GitHub repo, add the SSH remote, and (only if the user asks) make the first commit and push.
- Compare against the TA's reference layout once it is readable.

**Out (and why):**
- Any lab notebook work — worked notebooks are not provided yet.
- Version-pinning `requirements.txt` — the lab notes ship it unpinned; revisit if installs drift.
- GitHub CLI auth (`gh auth login`) — the TA asked for SSH; `gh` is optional.

## Approach

Do it in the order that unblocks the most: environment first (needed by every lab), SSH next (the TA's task, quick to verify), datasets in parallel (manual downloads), and push last because it needs the user's go-ahead. Each step has a command that proves it worked.

## Risks & unknowns

| Risk / unknown | Confidence | Mitigation |
|---|---|---|
| Python 3.12 packages resolve for all seven requirements, including torch | Medium — lab notes say CPU torch works; not tried here | Install in `ml`; if torch fails, record the error verbatim and ask |
| SSH steps match the TA's video | Medium — commands are the standard GitHub procedure; the video was not watched | Cross-check against the video; the verify step (`ssh -T`) is the real test |
| Windows OpenSSH agent vs Git Bash's own ssh disagree about the key | Medium | Run `ssh -T git@github.com` in the same shell used to push |
| PowerShell blocks scripts or the agent service won't start | Low–medium | Admin PowerShell for the service step; follow the video if it differs |
| TA's repo layout differs from lab notes §2.1 | Unknown — repo returned 404 | Ask for the link or access; adjust layout via an ADR |
| Repo name, visibility, TA access | Unknown (A-07) | Ask the TA before the first push |
| Native Windows vs WSL | Assumed Windows (A-01) | Confirm with the user |

## Definition of done

This phase is done when every line below is true and has been *observed*, not assumed:

- `conda activate ml` then `python --version` prints Python 3.12.x.
- `python -c "import numpy, pandas, matplotlib, sklearn, joblib, torch"` runs without error inside `ml`.
- All 11 dataset files exist in `ML LAB/all_datasets/` and match the names in the lab notes.
- `ssh -T git@github.com` reports successful authentication.
- The repo exists on GitHub with the SSH remote configured locally (`git remote -v`).
- If the user asked for it: the first push succeeded and the files are visible on GitHub, with no datasets, PDFs or `.venv` included.
