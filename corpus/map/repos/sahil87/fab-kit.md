# sahil87/fab-kit

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 7284adb0be5d @ f72bfce7b5fd26a6

## Summary (orientation draft, not independently verified)

Fab Kit is a markdown-prompt toolkit for AI-assisted coding built around a 6-stage change pipeline, slash-command skills for AI agents, a fab CLI, git-worktree parallelism, and git-committed project memory. Evidence is README documentation only; no evaluation or runtime code is shown. Evidence coverage: 142 of 383 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 83 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 14 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

14 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (2 claim(s)):
  - [observation/documented] Changes move through six stages — intake, apply, review, hydrate, ship, review-PR — each producing a persistent artifact such as intake.md, plan.md, or a PR. -- evidence: [README.md#L7-L7](https://github.com/sahil87/fab-kit/blob/7284adb0be5d6af553d44e708c82568465263a18/README.md#L7-L7), [README.md#L61-L68](https://github.com/sahil87/fab-kit/blob/7284adb0be5d6af553d44e708c82568465263a18/README.md#L61-L68)
  - [observation/documented] Each change is a self-contained folder under fab/changes/ holding intake.md, plan.md, and a .status.yaml state file symlinked at the repo root while active. -- evidence: [README.md#L76-L81](https://github.com/sahil87/fab-kit/blob/7284adb0be5d6af553d44e708c82568465263a18/README.md#L76-L81)
- components (1 claim(s)):
  - [observation/documented] The kit includes the fab CLI router (init/upgrade-repo/sync), companion tools wt for worktrees and idea for backlogs, and batch orchestration for parallel AI agents. -- evidence: [README.md#L7-L7](https://github.com/sahil87/fab-kit/blob/7284adb0be5d6af553d44e708c82568465263a18/README.md#L7-L7), [README.md#L105-L112](https://github.com/sahil87/fab-kit/blob/7284adb0be5d6af553d44e708c82568465263a18/README.md#L105-L112)
- design-choices (3 claim(s)):
  - [observation/documented] Prompts are plain markdown with no SDK and no vendor lock-in, and the kit works with Claude Code, Codex, Cursor, and Windsurf. -- evidence: [README.md#L7-L7](https://github.com/sahil87/fab-kit/blob/7284adb0be5d6af553d44e708c82568465263a18/README.md#L7-L7)
  - [observation/documented] A project constitution (fab/project/constitution.md) with MUST/SHOULD/MUST NOT rules is checked by every plan and review; it and config.yaml are the only required of five config files. -- evidence: [README.md#L397-L397](https://github.com/sahil87/fab-kit/blob/7284adb0be5d6af553d44e708c82568465263a18/README.md#L397-L397), [README.md#L369-L371](https://github.com/sahil87/fab-kit/blob/7284adb0be5d6af553d44e708c82568465263a18/README.md#L369-L371)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: building Fab Kit from source requires Go for the binaries under src/go/ and the just task runner for build, test, and release recipes. -- evidence: [README.md#L122-L125](https://github.com/sahil87/fab-kit/blob/7284adb0be5d6af553d44e708c82568465263a18/README.md#L122-L125)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] Skills are slash commands typed into an AI agent's chat (/fab-* in Claude Code, $fab-* in Codex), not terminal commands; each command runs one pipeline stage. -- evidence: [README.md#L418-L418](https://github.com/sahil87/fab-kit/blob/7284adb0be5d6af553d44e708c82568465263a18/README.md#L418-L418), [README.md#L229-L229](https://github.com/sahil87/fab-kit/blob/7284adb0be5d6af553d44e708c82568465263a18/README.md#L229-L229), [README.md#L235-L235](https://github.com/sahil87/fab-kit/blob/7284adb0be5d6af553d44e708c82568465263a18/README.md#L235-L235)
  - [observation/documented] The fab CLI exposes subcommands including sync, config show/explain/set, doctor, operator, and batch new/switch/archive for worktree tab management. -- evidence: [README.md#L478-L489](https://github.com/sahil87/fab-kit/blob/7284adb0be5d6af553d44e708c82568465263a18/README.md#L478-L489)
- memory-state (1 claim(s)):
  - [observation/documented] Learnings from each change are saved into docs/memory/, a domain-organized knowledge base committed to git and shared across the team; /docs-hydrate-memory can bootstrap it from Notion, Linear, or local files. -- evidence: [README.md#L333-L333](https://github.com/sahil87/fab-kit/blob/7284adb0be5d6af553d44e708c82568465263a18/README.md#L333-L333), [README.md#L346-L349](https://github.com/sahil87/fab-kit/blob/7284adb0be5d6af553d44e708c82568465263a18/README.md#L346-L349)
- orchestration (3 claim(s)):
  - [observation/documented] Parallelism relies on git worktree isolation: wt create makes an isolated worktree, fab sync runs automatically in each new worktree, and self-contained change folders avoid shared state. -- evidence: [README.md#L265-L265](https://github.com/sahil87/fab-kit/blob/7284adb0be5d6af553d44e708c82568465263a18/README.md#L265-L265), [README.md#L223-L223](https://github.com/sahil87/fab-kit/blob/7284adb0be5d6af553d44e708c82568465263a18/README.md#L223-L223), [README.md#L327-L329](https://github.com/sahil87/fab-kit/blob/7284adb0be5d6af553d44e708c82568465263a18/README.md#L327-L329)
More evidence: [full detail](fab-kit.detail.md)

Metadata and full claim list: [full detail](fab-kit.detail.md)
Human notes ([notes](fab-kit.notes.md), never overwritten by build)

[Back to map index](../../index.md)
