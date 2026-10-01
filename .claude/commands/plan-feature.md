---
description: Write the plan + execution doc pair required before starting a lab or the project
argument-hint: [which lab or task]
allowed-tools: Read, Write, Glob, Grep, Bash
---

Produce the plan/execution pair CLAUDE.md requires before any lab or project work, for: $ARGUMENTS

First read `refdocs/STATUS.md`, the PRD, `refdocs/changelog/DECISIONS.md`, and the lab material this would touch (the worked notebook, the relevant lab PDF, the datasets involved). Check whether an existing plan already covers it — if so, say so instead of writing a duplicate.

Write two files, matching the structure of the existing docs in those directories:
- `refdocs/plans/YYYY-MM-DD-<slug>.md` — what and why: scope in/out with reasons, approach, a risk table with honest confidence levels, and a definition of done phrased as observable facts.
- `refdocs/execution/YYYY-MM-DD-<slug>.md` — how and in what order: numbered tasks, each naming the files it touches and carrying its own **Verify** step with a real command and expected result.

Where a task depends on a library's behavior, its first step is "read the actual docs" — do not encode an API you're recalling from memory. Bake the leakage rule into any task that fits a transformer. Add the new rows to both README indexes.

Do not implement anything. Return both paths and the task order.
