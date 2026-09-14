# weilin0723/purrcode

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 156d83206ed7 @ f386a16ac8aceb42

## Summary (orientation draft, not independently verified)

The architecture defines four subsystems: PawGate (policy/judgment/authorization), Claw (tool execution and sandboxing), Whisker (repository context and risk signals), and NineLives (checkpoints, recovery, rollback). Model output is treated as a proposal, never authority: every native action is bound to a durable authorization, re-checked before execution, and followed by recorded validation; repository content, model output, and downloaded skills are untrusted. Evidence coverage: 121 of 152 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 34 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The architecture defines four subsystems: PawGate (policy/judgment/authorization), Claw (tool execution and sandboxing), Whisker (repository context and risk signals), and NineLives (checkpoints, recovery, rollback). -- evidence: [docs/src/architecture.md#L9-L14](https://github.com/Weilin0723/PurrCode/blob/156d83206ed74a89398c0adf8d4fccd3e070ae59/docs/src/architecture.md#L9-L14), [docs/architecture.md#L3-L5](https://github.com/Weilin0723/PurrCode/blob/156d83206ed74a89398c0adf8d4fccd3e070ae59/docs/architecture.md#L3-L5)
- design-choices (2 claim(s)):
  - [observation/documented] Model output is treated as a proposal, never authority: every native action is bound to a durable authorization, re-checked before execution, and followed by recorded validation; repository content, model output, and downloaded skills are untrusted. -- evidence: [README.md#L24-L24](https://github.com/Weilin0723/PurrCode/blob/156d83206ed74a89398c0adf8d4fccd3e070ae59/README.md#L24-L24), [docs/src/architecture.md#L38-L43](https://github.com/Weilin0723/PurrCode/blob/156d83206ed74a89398c0adf8d4fccd3e070ae59/docs/src/architecture.md#L38-L43)
  - [observation/documented] Actions are strongly typed (Command, RepositoryRead, WriteFile, DeleteFile, ExternalTool) with no shell-string parsing in the trusted path; ExternalTool actions are MCP-only and always require approval. -- evidence: [docs/architecture.md#L43-L50](https://github.com/Weilin0723/PurrCode/blob/156d83206ed74a89398c0adf8d4fccd3e070ae59/docs/architecture.md#L43-L50), [docs/architecture.md#L38-L41](https://github.com/Weilin0723/PurrCode/blob/156d83206ed74a89398c0adf8d4fccd3e070ae59/docs/architecture.md#L38-L41)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: repository checks run cargo fmt --check, clippy with -D warnings, cargo test --workspace, plus npm tests for the purrcode package and TypeScript SDK and Python unittest discovery for the Python SDK. -- evidence: [README.md#L172-L179](https://github.com/Weilin0723/PurrCode/blob/156d83206ed74a89398c0adf8d4fccd3e070ae59/README.md#L172-L179)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The product exposes a terminal Workbench (bare `purrcode`), a native Rust desktop IDE (`purrcode ide`/`gui`), and a browser Studio client (`purrcode studio`) for daemon health, sessions, and environment inspection. -- evidence: [README.md#L116-L116](https://github.com/Weilin0723/PurrCode/blob/156d83206ed74a89398c0adf8d4fccd3e070ae59/README.md#L116-L116), [README.md#L30-L32](https://github.com/Weilin0723/PurrCode/blob/156d83206ed74a89398c0adf8d4fccd3e070ae59/README.md#L30-L32)
  - [observation/documented] TUI slash commands include /connect (provider discovery/import), /mode (Ask/Plan/Build/Review), /permission (Ask/Auto/Full Access), and /ide; one-shot commands include plan, run, review, approve, doctor, sessions, resume, and rollback. -- evidence: [README.md#L120-L126](https://github.com/Weilin0723/PurrCode/blob/156d83206ed74a89398c0adf8d4fccd3e070ae59/README.md#L120-L126), [README.md#L132-L133](https://github.com/Weilin0723/PurrCode/blob/156d83206ed74a89398c0adf8d4fccd3e070ae59/README.md#L132-L133), [README.md#L136-L139](https://github.com/Weilin0723/PurrCode/blob/156d83206ed74a89398c0adf8d4fccd3e070ae59/README.md#L136-L139), [README.md#L142-L144](https://github.com/Weilin0723/PurrCode/blob/156d83206ed74a89398c0adf8d4fccd3e070ae59/README.md#L142-L144)
- memory-state (1 claim(s)):
  - [observation/documented] Authorization is stored in append-only SQLite with exact action/constraint digest verification and atomic single-use consumption; NineLives owns durable events, checkpoints, restart reconciliation, and conservative recovery that never blindly replays interrupted actions. -- evidence: [docs/implementation-status.md#L7-L12](https://github.com/Weilin0723/PurrCode/blob/156d83206ed74a89398c0adf8d4fccd3e070ae59/docs/implementation-status.md#L7-L12), [docs/architecture.md#L9-L18](https://github.com/Weilin0723/PurrCode/blob/156d83206ed74a89398c0adf8d4fccd3e070ae59/docs/architecture.md#L9-L18), [docs/architecture.md#L3-L5](https://github.com/Weilin0723/PurrCode/blob/156d83206ed74a89398c0adf8d4fccd3e070ae59/docs/architecture.md#L3-L5), [docs/src/architecture.md#L38-L43](https://github.com/Weilin0723/PurrCode/blob/156d83206ed74a89398c0adf8d4fccd3e070ae59/docs/src/architecture.md#L38-L43)
- orchestration (1 claim(s)):
More evidence: [full detail](purrcode.detail.md)

Metadata and full claim list: [full detail](purrcode.detail.md)
Human notes ([notes](purrcode.notes.md), never overwritten by build)

[Back to map index](../../index.md)
