# violetdelia/codex-multi-agents -- full detail

[Back to orientation](codex-multi-agents.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/violetdelia/codex-multi-agents/8779b4add624ef7dcda3cee138563a41db416e74/8b769d053e53f0ae.json](../../../wiki/dossiers/violetdelia/codex-multi-agents/8779b4add624ef7dcda3cee138563a41db416e74/8b769d053e53f0ae.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (2 claim(s))

- [observation/documented] The README recommends a task pipeline template: spec task, implementation task, review/re-review task, merge task, and sync-confirmation task. -- evidence: [README.md#L117-L119](https://github.com/violetDelia/codex-multi-agents/blob/8779b4add624ef7dcda3cee138563a41db416e74/README.md#L117-L119) (`clm_5061463f4cbc54d88c9be68960b0be61c4c4c68493a0d3b812b06a570d58383a`)
- [observation/documented] Dispatch messages are advised to always state the worktree path (verified to exist), an acceptance command such as a pytest invocation, and to use -pause and ask when blocked. -- evidence: [README.md#L77-L81](https://github.com/violetDelia/codex-multi-agents/blob/8779b4add624ef7dcda3cee138563a41db416e74/README.md#L77-L81), [README.md#L121-L124](https://github.com/violetDelia/codex-multi-agents/blob/8779b4add624ef7dcda3cee138563a41db416e74/README.md#L121-L124) (`clm_a9c7deeeb1cfb2ba1e62ba78e4c86421b9a837a710bf5edf59f3d6d3dc94b70d`)

## skills-patterns (1 claim(s))

- [observation/documented] The toolkit is packaged as a skill under skills/codex-multi-agents, with example files (agents-lists.md, TODO.md, commands-quickstart.md, common-guides.md), a SKILL.md, and an EXTENSIONS.md covering division of labor, dispatch, blocking, merge, and sync strategies. -- evidence: [README.md#L148-L151](https://github.com/violetDelia/codex-multi-agents/blob/8779b4add624ef7dcda3cee138563a41db416e74/README.md#L148-L151), [README.md#L11-L12](https://github.com/violetDelia/codex-multi-agents/blob/8779b4add624ef7dcda3cee138563a41db416e74/README.md#L11-L12) (`clm_970d2baab40f6bc72574d106ee2f9a2071820e73da5437f807a70ac2b4fa02a6`)

## interfaces (3 claim(s))

- [observation/documented] The toolkit exposes a roster-management CLI, codex-multi-agents-list.sh, supporting at least -file, -status, -add (with -name and -type), and -init flags per the README examples. -- evidence: [README.md#L60-L63](https://github.com/violetDelia/codex-multi-agents/blob/8779b4add624ef7dcda3cee138563a41db416e74/README.md#L60-L63), [README.md#L15-L16](https://github.com/violetDelia/codex-multi-agents/blob/8779b4add624ef7dcda3cee138563a41db416e74/README.md#L15-L16), [README.md#L51-L52](https://github.com/violetDelia/codex-multi-agents/blob/8779b4add624ef7dcda3cee138563a41db416e74/README.md#L51-L52), [README.md#L55-L57](https://github.com/violetDelia/codex-multi-agents/blob/8779b4add624ef7dcda3cee138563a41db416e74/README.md#L55-L57) (`clm_5180424416e410768227d15de4d4d541104dee7a7a555ac457bea5f6fdbb687f`)
- [observation/documented] A task CLI, codex-multi-agents-task.sh, operates on a TODO file and supports -new (with -from, -to, -worktree, -log, -info), -dispatch, -done, -pause, -continue, and -status -task-list operations. -- evidence: [README.md#L27-L31](https://github.com/violetDelia/codex-multi-agents/blob/8779b4add624ef7dcda3cee138563a41db416e74/README.md#L27-L31), [README.md#L84-L86](https://github.com/violetDelia/codex-multi-agents/blob/8779b4add624ef7dcda3cee138563a41db416e74/README.md#L84-L86), [README.md#L88-L90](https://github.com/violetDelia/codex-multi-agents/blob/8779b4add624ef7dcda3cee138563a41db416e74/README.md#L88-L90), [README.md#L41-L43](https://github.com/violetDelia/codex-multi-agents/blob/8779b4add624ef7dcda3cee138563a41db416e74/README.md#L41-L43), [README.md#L34-L38](https://github.com/violetDelia/codex-multi-agents/blob/8779b4add624ef7dcda3cee138563a41db416e74/README.md#L34-L38), [README.md#L19-L24](https://github.com/violetDelia/codex-multi-agents/blob/8779b4add624ef7dcda3cee138563a41db416e74/README.md#L19-L24) (`clm_e7738045c10138a0f299fd3b1a852532864a066a2e8030764e0051a6bb0f2e29`)
- [observation/documented] A tmux-based communication CLI, codex-multi-agents-tmux.sh, provides -init-env to initialize an agent session and -talk with -from/-to/-agents-list/-message/-log to send messages between agents. -- evidence: [README.md#L108-L113](https://github.com/violetDelia/codex-multi-agents/blob/8779b4add624ef7dcda3cee138563a41db416e74/README.md#L108-L113), [README.md#L104-L105](https://github.com/violetDelia/codex-multi-agents/blob/8779b4add624ef7dcda3cee138563a41db416e74/README.md#L104-L105) (`clm_06991b2811b02eaca5c47dcf1d64959573cd7d114bff4735993285b6ca0cc04b`)

## memory-state (1 claim(s))

- [inference/documented] Task state appears persisted in the TODO file passed via -file, and markdown log files (used with -new and -done in the examples) appear to record task history. -- evidence: [README.md#L84-L86](https://github.com/violetDelia/codex-multi-agents/blob/8779b4add624ef7dcda3cee138563a41db416e74/README.md#L84-L86), [README.md#L88-L90](https://github.com/violetDelia/codex-multi-agents/blob/8779b4add624ef7dcda3cee138563a41db416e74/README.md#L88-L90), [README.md#L41-L43](https://github.com/violetDelia/codex-multi-agents/blob/8779b4add624ef7dcda3cee138563a41db416e74/README.md#L41-L43), [README.md#L34-L38](https://github.com/violetDelia/codex-multi-agents/blob/8779b4add624ef7dcda3cee138563a41db416e74/README.md#L34-L38), [README.md#L19-L24](https://github.com/violetDelia/codex-multi-agents/blob/8779b4add624ef7dcda3cee138563a41db416e74/README.md#L19-L24) (`clm_ed4e2989e3bbc3befb9f60c765a6a6131e9dabf6c6d270576a45e31fc262c310`)

## orchestration (1 claim(s))

- [observation/documented] The system coordinates work among named roles (e.g. 管理员 dispatching to 小王) via a shared agents-list file and per-task worktree paths. -- evidence: [README.md#L27-L31](https://github.com/violetDelia/codex-multi-agents/blob/8779b4add624ef7dcda3cee138563a41db416e74/README.md#L27-L31), [README.md#L11-L12](https://github.com/violetDelia/codex-multi-agents/blob/8779b4add624ef7dcda3cee138563a41db416e74/README.md#L11-L12), [README.md#L19-L24](https://github.com/violetDelia/codex-multi-agents/blob/8779b4add624ef7dcda3cee138563a41db416e74/README.md#L19-L24) (`clm_b72d01d9c33d35a0b75aa168d9c0a31ccba70a8278b64d852a5705827c70772e`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## limitations (1 claim(s))

- [observation/documented] Documented failure modes include 'target session not found' (fixed by running tmux -init-env first), 'worktree not found' (create or fix the path before dispatch), and 'task already exists in running list' when re-dispatching a running task. -- evidence: [README.md#L141-L144](https://github.com/violetDelia/codex-multi-agents/blob/8779b4add624ef7dcda3cee138563a41db416e74/README.md#L141-L144), [README.md#L128-L134](https://github.com/violetDelia/codex-multi-agents/blob/8779b4add624ef7dcda3cee138563a41db416e74/README.md#L128-L134), [README.md#L136-L139](https://github.com/violetDelia/codex-multi-agents/blob/8779b4add624ef7dcda3cee138563a41db416e74/README.md#L136-L139) (`clm_c452aa956a39f8404b20cf3c0bceeec0b7dd010581c04abf18816276f59cb8fe`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

