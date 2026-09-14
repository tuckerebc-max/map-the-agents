# ramarlina/agx

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit e674cec11088 @ 14a96526364b8134

## Summary (orientation draft, not independently verified)

AGX is a local CLI/dashboard/desktop workspace for running coding agents (Claude, Codex, Gemini, Ollama) across tickets, repos, and PRs, with checkpointed state in SQLite and human approval gates. Evidence is mostly README documentation plus a GitHub-integration implementation plan; no shipped source code is included in the slices. Evidence coverage: 158 of 301 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 3 of 4 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 14 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

14 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The architecture comprises a SQLite (WAL mode) state layer with durable checkpoints, a CLI plus daemon handling provider tool calls, filesystem edits, and worktree isolation, and a decision layer for human gate transitions and review flow. -- evidence: [README.md#L131-L133](https://github.com/ramarlina/agx/blob/e674cec110883774508aee1ee1ca355827563725/README.md#L131-L133)
- design-choices (3 claim(s)):
  - [observation/documented] Work is checkpointed at every step so restarts resume where the user left off, and resuming is described as constant-cost regardless of thread age. -- evidence: [README.md#L127-L127](https://github.com/ramarlina/agx/blob/e674cec110883774508aee1ee1ca355827563725/README.md#L127-L127)
  - [observation/documented] Agents pause for explicit human approve/reject before anything irreversible, and PR review begins with a first pass from a reviewer agent. -- evidence: [README.md#L112-L119](https://github.com/ramarlina/agx/blob/e674cec110883774508aee1ee1ca355827563725/README.md#L112-L119)
- workflows (3 claim(s)):
  - [observation/documented] Repository development practice: the repo is an npm workspace with apps/local (Next.js dashboard), apps/desktop (Electron), lib, commands, and cloud-runtime; dev commands include `npm run local:dev`, `local:build`, `board:bundle`, and Electron `build:mac`. -- evidence: [README.md#L205-L213](https://github.com/ramarlina/agx/blob/e674cec110883774508aee1ee1ca355827563725/README.md#L205-L213), [README.md#L217-L220](https://github.com/ramarlina/agx/blob/e674cec110883774508aee1ee1ca355827563725/README.md#L217-L220), [README.md#L203-L203](https://github.com/ramarlina/agx/blob/e674cec110883774508aee1ee1ca355827563725/README.md#L203-L203), [README.md#L231-L235](https://github.com/ramarlina/agx/blob/e674cec110883774508aee1ee1ca355827563725/README.md#L231-L235), [README.md#L224-L227](https://github.com/ramarlina/agx/blob/e674cec110883774508aee1ee1ca355827563725/README.md#L224-L227)
  - [observation/documented] Repository development practice: contributions are welcomed via GitHub Discussions and Issues, with PRs made by forking main, adding tests, and submitting. -- evidence: [README.md#L250-L250](https://github.com/ramarlina/agx/blob/e674cec110883774508aee1ee1ca355827563725/README.md#L250-L250), [README.md#L252-L254](https://github.com/ramarlina/agx/blob/e674cec110883774508aee1ee1ca355827563725/README.md#L252-L254)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] AGX ships as a CLI, a local web dashboard, and a macOS desktop app from one repository. -- evidence: [README.md#L57-L57](https://github.com/ramarlina/agx/blob/e674cec110883774508aee1ee1ca355827563725/README.md#L57-L57)
  - [observation/documented] The CLI exposes provider chat commands such as `agx claude -p`, `agx codex -p`, `agx gemini -p`, and `agx ollama -p`, with single-letter aliases c, x, g, o. -- evidence: [README.md#L147-L152](https://github.com/ramarlina/agx/blob/e674cec110883774508aee1ee1ca355827563725/README.md#L147-L152)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
  - [observation/documented] The product claims fully local operation with an activity log, signed actions, and destructive-command safeguards. -- evidence: [README.md#L135-L135](https://github.com/ramarlina/agx/blob/e674cec110883774508aee1ee1ca355827563725/README.md#L135-L135), [README.md#L112-L119](https://github.com/ramarlina/agx/blob/e674cec110883774508aee1ee1ca355827563725/README.md#L112-L119)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
More evidence: [full detail](agx.detail.md)

Metadata and full claim list: [full detail](agx.detail.md)
Human notes ([notes](agx.notes.md), never overwritten by build)

[Back to map index](../../index.md)
