# violetdelia/codex-multi-agents

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 8779b4add624 @ 8b769d053e53f0ae

## Summary (orientation draft, not independently verified)

Selected evidence records: The toolkit exposes a roster-management CLI, codex-multi-agents-list.sh, supporting at least -file, -status, -add (with -name and -type), and -init flags per the README examples. A task CLI, codex-multi-agents-task.sh, operates on a TODO file and supports -new (with -from, -to, -worktree, -log, -info), -dispatch, -done, -pause, -continue, and -status -task-list operations.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 9 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

9 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows (2 claim(s)):
  - [observation/documented] The README recommends a task pipeline template: spec task, implementation task, review/re-review task, merge task, and sync-confirmation task. -- evidence: [README.md#L117-L119](https://github.com/violetDelia/codex-multi-agents/blob/8779b4add624ef7dcda3cee138563a41db416e74/README.md#L117-L119)
  - [observation/documented] Dispatch messages are advised to always state the worktree path (verified to exist), an acceptance command such as a pytest invocation, and to use -pause and ask when blocked. -- evidence: [README.md#L77-L81](https://github.com/violetDelia/codex-multi-agents/blob/8779b4add624ef7dcda3cee138563a41db416e74/README.md#L77-L81), [README.md#L121-L124](https://github.com/violetDelia/codex-multi-agents/blob/8779b4add624ef7dcda3cee138563a41db416e74/README.md#L121-L124)
- skills-patterns (1 claim(s)):
  - [observation/documented] The toolkit is packaged as a skill under skills/codex-multi-agents, with example files (agents-lists.md, TODO.md, commands-quickstart.md, common-guides.md), a SKILL.md, and an EXTENSIONS.md covering division of labor, dispatch, blocking, merge, and sync strategies. -- evidence: [README.md#L148-L151](https://github.com/violetDelia/codex-multi-agents/blob/8779b4add624ef7dcda3cee138563a41db416e74/README.md#L148-L151), [README.md#L11-L12](https://github.com/violetDelia/codex-multi-agents/blob/8779b4add624ef7dcda3cee138563a41db416e74/README.md#L11-L12)
- interfaces (3 claim(s)):
  - [observation/documented] The toolkit exposes a roster-management CLI, codex-multi-agents-list.sh, supporting at least -file, -status, -add (with -name and -type), and -init flags per the README examples. -- evidence: [README.md#L60-L63](https://github.com/violetDelia/codex-multi-agents/blob/8779b4add624ef7dcda3cee138563a41db416e74/README.md#L60-L63), [README.md#L15-L16](https://github.com/violetDelia/codex-multi-agents/blob/8779b4add624ef7dcda3cee138563a41db416e74/README.md#L15-L16), [README.md#L51-L52](https://github.com/violetDelia/codex-multi-agents/blob/8779b4add624ef7dcda3cee138563a41db416e74/README.md#L51-L52), [README.md#L55-L57](https://github.com/violetDelia/codex-multi-agents/blob/8779b4add624ef7dcda3cee138563a41db416e74/README.md#L55-L57)
  - [observation/documented] A task CLI, codex-multi-agents-task.sh, operates on a TODO file and supports -new (with -from, -to, -worktree, -log, -info), -dispatch, -done, -pause, -continue, and -status -task-list operations. -- evidence: [README.md#L27-L31](https://github.com/violetDelia/codex-multi-agents/blob/8779b4add624ef7dcda3cee138563a41db416e74/README.md#L27-L31), [README.md#L84-L86](https://github.com/violetDelia/codex-multi-agents/blob/8779b4add624ef7dcda3cee138563a41db416e74/README.md#L84-L86), [README.md#L88-L90](https://github.com/violetDelia/codex-multi-agents/blob/8779b4add624ef7dcda3cee138563a41db416e74/README.md#L88-L90), [README.md#L41-L43](https://github.com/violetDelia/codex-multi-agents/blob/8779b4add624ef7dcda3cee138563a41db416e74/README.md#L41-L43), [README.md#L34-L38](https://github.com/violetDelia/codex-multi-agents/blob/8779b4add624ef7dcda3cee138563a41db416e74/README.md#L34-L38), [README.md#L19-L24](https://github.com/violetDelia/codex-multi-agents/blob/8779b4add624ef7dcda3cee138563a41db416e74/README.md#L19-L24)
- memory-state (1 claim(s)):
  - [inference/documented] Task state appears persisted in the TODO file passed via -file, and markdown log files (used with -new and -done in the examples) appear to record task history. -- evidence: [README.md#L84-L86](https://github.com/violetDelia/codex-multi-agents/blob/8779b4add624ef7dcda3cee138563a41db416e74/README.md#L84-L86), [README.md#L88-L90](https://github.com/violetDelia/codex-multi-agents/blob/8779b4add624ef7dcda3cee138563a41db416e74/README.md#L88-L90), [README.md#L41-L43](https://github.com/violetDelia/codex-multi-agents/blob/8779b4add624ef7dcda3cee138563a41db416e74/README.md#L41-L43), [README.md#L34-L38](https://github.com/violetDelia/codex-multi-agents/blob/8779b4add624ef7dcda3cee138563a41db416e74/README.md#L34-L38), [README.md#L19-L24](https://github.com/violetDelia/codex-multi-agents/blob/8779b4add624ef7dcda3cee138563a41db416e74/README.md#L19-L24)
- orchestration (1 claim(s)):
  - [observation/documented] The system coordinates work among named roles (e.g. 管理员 dispatching to 小王) via a shared agents-list file and per-task worktree paths. -- evidence: [README.md#L27-L31](https://github.com/violetDelia/codex-multi-agents/blob/8779b4add624ef7dcda3cee138563a41db416e74/README.md#L27-L31), [README.md#L11-L12](https://github.com/violetDelia/codex-multi-agents/blob/8779b4add624ef7dcda3cee138563a41db416e74/README.md#L11-L12), [README.md#L19-L24](https://github.com/violetDelia/codex-multi-agents/blob/8779b4add624ef7dcda3cee138563a41db416e74/README.md#L19-L24)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies: unknown (no source-linked claim submitted for this facet)
- limitations (1 claim(s)):
More evidence: [full detail](codex-multi-agents.detail.md)

Metadata and full claim list: [full detail](codex-multi-agents.detail.md)
Human notes ([notes](codex-multi-agents.notes.md), never overwritten by build)

[Back to map index](../../index.md)
