# oxgeneral/orch

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit c066dc013e98 @ 63003115ba6c9391

## Summary (orientation draft, not independently verified)

Selected evidence records: ORCH exposes a CLI including commands such as orch init, doctor, agent add/list, org deploy/export, task add/assign/cancel, team create, goal add, msg send/broadcast, run, serve, status, logs, and tui. The package can be imported as a library; the core reportedly has no dependency on the CLI/TUI layers, letting users build their own interface on top.

## Source coverage

Source coverage (partial): 3 of 10 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 16 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

16 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (3 claim(s)):
  - [observation/documented] The documented source layout includes domain (models, state machine), application (orchestrator engine, services, event bus), infrastructure (adapters, file storage, process management, LiquidJS templates, git worktree workspace), cli (Commander.js), and tui (Ink + React). -- evidence: [readme.md#L606-L618](https://github.com/oxgeneral/ORCH/blob/c066dc013e98e08d753ce204e604e04621dd4167/readme.md#L606-L618)
  - [observation/documented] Eight adapters are documented: Claude Code, OpenCode, Codex, Pi, Cursor, Grok, Antigravity, and Shell, where the shell adapter wraps any terminal CLI tool as an agent. -- evidence: [readme.md#L334-L334](https://github.com/oxgeneral/ORCH/blob/c066dc013e98e08d753ce204e604e04621dd4167/readme.md#L334-L334), [readme.md#L711-L711](https://github.com/oxgeneral/ORCH/blob/c066dc013e98e08d753ce204e604e04621dd4167/readme.md#L711-L711)
- design-choices (2 claim(s)):
  - [observation/documented] Each agent works in an isolated git worktree on its own branch, and code reaches main only after explicit user approval through a mandatory review step in the task state machine. -- evidence: [readme.md#L198-L198](https://github.com/oxgeneral/ORCH/blob/c066dc013e98e08d753ce204e604e04621dd4167/readme.md#L198-L198), [readme.md#L684-L684](https://github.com/oxgeneral/ORCH/blob/c066dc013e98e08d753ce204e604e04621dd4167/readme.md#L684-L684)
  - [observation/documented] Tasks flow through a state machine (todo → in_progress → review → done) with validated transitions, and no code merges without approval. -- evidence: [readme.md#L265-L270](https://github.com/oxgeneral/ORCH/blob/c066dc013e98e08d753ce204e604e04621dd4167/readme.md#L265-L270), [readme.md#L272-L272](https://github.com/oxgeneral/ORCH/blob/c066dc013e98e08d753ce204e604e04621dd4167/readme.md#L272-L272)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns (1 claim(s)):
  - [observation/documented] After installation, an `/orch` skill is reportedly available in Claude Code, translating natural-language requests into orch commands for agents, tasks, goals, and runs. -- evidence: [readme.md#L144-L144](https://github.com/oxgeneral/ORCH/blob/c066dc013e98e08d753ce204e604e04621dd4167/readme.md#L144-L144), [readme.md#L150-L150](https://github.com/oxgeneral/ORCH/blob/c066dc013e98e08d753ce204e604e04621dd4167/readme.md#L150-L150)
- interfaces (4 claim(s)):
  - [observation/documented] ORCH exposes a CLI including commands such as orch init, doctor, agent add/list, org deploy/export, task add/assign/cancel, team create, goal add, msg send/broadcast, run, serve, status, logs, and tui. -- evidence: [readme.md#L553-L557](https://github.com/oxgeneral/ORCH/blob/c066dc013e98e08d753ce204e604e04621dd4167/readme.md#L553-L557), [readme.md#L542-L546](https://github.com/oxgeneral/ORCH/blob/c066dc013e98e08d753ce204e604e04621dd4167/readme.md#L542-L546), [readme.md#L484-L488](https://github.com/oxgeneral/ORCH/blob/c066dc013e98e08d753ce204e604e04621dd4167/readme.md#L484-L488), [readme.md#L530-L535](https://github.com/oxgeneral/ORCH/blob/c066dc013e98e08d753ce204e604e04621dd4167/readme.md#L530-L535), [readme.md#L506-L511](https://github.com/oxgeneral/ORCH/blob/c066dc013e98e08d753ce204e604e04621dd4167/readme.md#L506-L511), [readme.md#L564-L573](https://github.com/oxgeneral/ORCH/blob/c066dc013e98e08d753ce204e604e04621dd4167/readme.md#L564-L573), [readme.md#L495-L499](https://github.com/oxgeneral/ORCH/blob/c066dc013e98e08d753ce204e604e04621dd4167/readme.md#L495-L499), [readme.md#L518-L523](https://github.com/oxgeneral/ORCH/blob/c066dc013e98e08d753ce204e604e04621dd4167/readme.md#L518-L523)
  - [observation/documented] The package can be imported as a library; the core reportedly has no dependency on the CLI/TUI layers, letting users build their own interface on top. -- evidence: [readme.md#L592-L592](https://github.com/oxgeneral/ORCH/blob/c066dc013e98e08d753ce204e604e04621dd4167/readme.md#L592-L592)
- memory-state (1 claim(s)):
  - [observation/documented] Storage is file-based using YAML/JSON/JSONL, and agents communicate through direct messages, team broadcasts, and a shared context store. -- evidence: [readme.md#L255-L255](https://github.com/oxgeneral/ORCH/blob/c066dc013e98e08d753ce204e604e04621dd4167/readme.md#L255-L255), [readme.md#L606-L618](https://github.com/oxgeneral/ORCH/blob/c066dc013e98e08d753ce204e604e04621dd4167/readme.md#L606-L618)
- orchestration (3 claim(s)):
  - [observation/documented] A CTO-style agent decomposes a high-level goal into tasks and delegates them; failed tasks auto-retry with exponential backoff and stalled agents are killed and re-queued by zombie detection. -- evidence: [readme.md#L240-L240](https://github.com/oxgeneral/ORCH/blob/c066dc013e98e08d753ce204e604e04621dd4167/readme.md#L240-L240), [readme.md#L244-L244](https://github.com/oxgeneral/ORCH/blob/c066dc013e98e08d753ce204e604e04621dd4167/readme.md#L244-L244)
More evidence: [full detail](orch.detail.md)

Metadata and full claim list: [full detail](orch.detail.md)
Human notes ([notes](orch.notes.md), never overwritten by build)

[Back to map index](../../index.md)
