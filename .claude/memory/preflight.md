# Preflight — TEB3123 Machine Learning Session Start

> Read this at the start of every session, before touching code.
> One page, six questions, then you can build. CLAUDE.md is the reference; this is the gate.

---

## 1. Where are we?

Open `refdocs/STATUS.md`. Find the current phase and the one next action.
If STATUS's claims and the files disagree, **that's the session's first task** — not the thing you were about to do.

---

## 2. What am I about to touch?

| Area | Path | Rule |
|---|---|---|
| Lab notebooks and scripts | `ML LAB/all_experiments/` | Run from this folder; data paths go `../all_datasets/…` (ASSUMED until a worked notebook confirms) |
| Raw datasets | `ML LAB/all_datasets/` | Read-only; files are git-ignored |
| Saved models | `ML LAB/models/` | Written by notebooks — don't hand-edit |
| Evidence | `ML LAB/results/labNN/` | Written by notebooks — don't hand-edit |
| Slides, lab PDFs | `ML LECTURE/`, `ML LAB/*.pdf` | Local reference only; git-ignored |
| Docs / agent config | `refdocs/`, `.claude/`, `CLAUDE.md` | Committed |

Only the lab you are working on. Don't edit another lab's notebook "while you're there".

---

## 3. Does a plan exist for what I'm about to build?

A lab or the project → a plan doc in `refdocs/plans/` **and** an execution doc in `refdocs/execution/`.
If neither exists, write them first (`/plan-feature`). If one exists but reality has moved, update it before building on it.

---

## 4. Has this already been decided?

Skim `refdocs/changelog/DECISIONS.md` before re-opening a choice. If your plan contradicts an ADR, you need a new ADR that says why — not a silent reversal.

Check the open `ASSUMED:` list at the bottom of that file. If today's work is load-bearing on one of them, **confirm it before you build**, not after.

---

## 5. Am I about to add an import or package?

A new third-party `import` in any notebook or script needs a line in `ML LAB/requirements.txt` in the same change, or the TA's clean-environment run will fail with `ModuleNotFoundError`. Install with `pip` inside the `ml` env — never `conda install` the same package. This is prose-only: the check isn't mechanical, so no hook enforces it.

---

## 6. Will I close the session properly?

`/session-end` — changelog entry, STATUS phase table, verification ledger, any new ADR.
The changelog entry is mandatory after any session that changed code, made a decision, or modified a plan. Even a one-line fix gets a one-line entry. **No commit or push unless the user asks.**

---

## Quick links

| Doc | Purpose |
|---|---|
| `refdocs/STATUS.md` | Where the work actually is |
| `CLAUDE.md` | Operating brief — rules, constraints, stack |
| `refdocs/teb3123-ml-PRD.md` | Scope, structure, roadmap, decision log |
| `refdocs/changelog/DECISIONS.md` | Settled calls — read before re-debating |
| `refdocs/guides/env_setup.md` | Conda env and GitHub SSH setup |
| `refdocs/guides/checklist.md` | Pre-push checklist |
| `refdocs/plans/` · `refdocs/execution/` | What/why · how/in what order |
