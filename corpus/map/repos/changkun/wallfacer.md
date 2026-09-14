# changkun/wallfacer

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 9acd2b092578 @ d09ab0b6a912ca08

## Summary (orientation draft, not independently verified)

Wallfacer is a local, open-source autonomous engineering platform combining chat, spec, task-board, and code abstraction levels with pluggable agent harnesses; evidence is mostly README documentation plus BUGS.md and contributor instructions.

## Source coverage

Source coverage (partial): 3 of 46 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 14 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

14 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Wallfacer is described as an autonomous engineering platform spanning chat, specs, task boards, and code, with agents operating at every abstraction level. -- evidence: [README.md#L13-L13](https://github.com/changkun/wallfacer/blob/9acd2b0925789ec6d7a54a1d94feb40b8fca752f/README.md#L13-L13)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (2 claim(s)):
  - [observation/documented] Specs serve as an intermediate representation: ideas become structured, versioned, reviewable specs that agents reason about and implement against, rather than going straight to code. -- evidence: [README.md#L33-L33](https://github.com/changkun/wallfacer/blob/9acd2b0925789ec6d7a54a1d94feb40b8fca752f/README.md#L33-L33)
  - [observation/documented] Specs follow a seven-state lifecycle (vague, drafted, validated, testing, complete, plus stale and archived) with a dependency DAG and atomic dispatch and undo. -- evidence: [README.md#L95-L95](https://github.com/changkun/wallfacer/blob/9acd2b0925789ec6d7a54a1d94feb40b8fca752f/README.md#L95-L95), [README.md#L136-L139](https://github.com/changkun/wallfacer/blob/9acd2b0925789ec6d7a54a1d94feb40b8fca752f/README.md#L136-L139)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: AGENTS.md requires a reproducible test for every bug fix, frequent small-scope commits, specs before big features, and register-specific writing conventions. -- evidence: [AGENTS.md#L1-L7](https://github.com/changkun/wallfacer/blob/9acd2b0925789ec6d7a54a1d94feb40b8fca752f/AGENTS.md#L1-L7)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The CLI surface includes wallfacer run, status, spec, auth, web, and doctor, with -help flags per command. -- evidence: [README.md#L65-L65](https://github.com/changkun/wallfacer/blob/9acd2b0925789ec6d7a54a1d94feb40b8fca752f/README.md#L65-L65), [README.md#L213-L219](https://github.com/changkun/wallfacer/blob/9acd2b0925789ec6d7a54a1d94feb40b8fca752f/README.md#L213-L219)
  - [observation/documented] The planning chat exposes slash commands such as /create, /validate, /break-down, and /dispatch to drive the spec lifecycle. -- evidence: [README.md#L95-L95](https://github.com/changkun/wallfacer/blob/9acd2b0925789ec6d7a54a1d94feb40b8fca752f/README.md#L95-L95)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (2 claim(s)):
  - [observation/documented] Execution is built from agents (sub-roles like impl, test, commit-msg, title, oversight), flows composing agents into pipelines, tasks that pick a flow, and scheduled routines. -- evidence: [README.md#L103-L106](https://github.com/changkun/wallfacer/blob/9acd2b0925789ec6d7a54a1d94feb40b8fca752f/README.md#L103-L106)
  - [observation/documented] Each task runs as a host process in its own git worktree, enabling parallel agent execution without conflicts. -- evidence: [README.md#L116-L116](https://github.com/changkun/wallfacer/blob/9acd2b0925789ec6d7a54a1d94feb40b8fca752f/README.md#L116-L116), [README.md#L35-L35](https://github.com/changkun/wallfacer/blob/9acd2b0925789ec6d7a54a1d94feb40b8fca752f/README.md#L35-L35)
- tools-permissions (1 claim(s)):
  - [observation/documented] Users control agent autonomy per task, spec, or project, from fully autonomous loops (implement, test, commit, push) to stepping in at any point. -- evidence: [README.md#L31-L31](https://github.com/changkun/wallfacer/blob/9acd2b0925789ec6d7a54a1d94feb40b8fca752f/README.md#L31-L31)
- evaluation (1 claim(s)):
  - [observation/documented] The product provides oversight tooling: per-task event timelines, diffs against the default branch, AI-generated oversight summaries, and token/cost tracking by task, activity, and turn. -- evidence: [README.md#L132-L132](https://github.com/changkun/wallfacer/blob/9acd2b0925789ec6d7a54a1d94feb40b8fca752f/README.md#L132-L132), [README.md#L126-L126](https://github.com/changkun/wallfacer/blob/9acd2b0925789ec6d7a54a1d94feb40b8fca752f/README.md#L126-L126)
- dependencies (1 claim(s)):
  - [observation/documented] The product is harness-agnostic, working with Claude Code, Codex, Cursor, OpenCode, and Pi via a pluggable harness layer, and users bring their own LLM provider. -- evidence: [README.md#L15-L15](https://github.com/changkun/wallfacer/blob/9acd2b0925789ec6d7a54a1d94feb40b8fca752f/README.md#L15-L15), [README.md#L41-L41](https://github.com/changkun/wallfacer/blob/9acd2b0925789ec6d7a54a1d94feb40b8fca752f/README.md#L41-L41)
- limitations (2 claim(s)):
More evidence: [full detail](wallfacer.detail.md)

Metadata and full claim list: [full detail](wallfacer.detail.md)
Human notes ([notes](wallfacer.notes.md), never overwritten by build)

[Back to map index](../../index.md)
