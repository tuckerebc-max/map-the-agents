# sondera-ai/sondera-coding-agent-hooks

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 9efefedd249e @ 5bba1d792787685d

## Summary (orientation draft, not independently verified)

Selected evidence records: The harness coordinates three guardrail subsystems: a YARA-X signature engine (always on and the only deterministic one), an optional LLM secure-code policy classifier, and optional LLM information-flow sensitivity labeling. The Cedar policy engine combines guardrail signals with entity state from a Turso (SQLite) local store and returns Allow, Deny, or Escalate adjudications back through the hook adapter.

## Source coverage

Source coverage (partial): 6 of 11 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 17 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

17 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] The harness coordinates three guardrail subsystems: a YARA-X signature engine (always on and the only deterministic one), an optional LLM secure-code policy classifier, and optional LLM information-flow sensitivity labeling. -- evidence: [docs/architecture.md#L10-L17](https://github.com/sondera-ai/sondera-coding-agent-hooks/blob/9efefedd249ee23c48608070978dd1a08a3be1ff/docs/architecture.md#L10-L17)
  - [observation/documented] The Cedar policy engine combines guardrail signals with entity state from a Turso (SQLite) local store and returns Allow, Deny, or Escalate adjudications back through the hook adapter. -- evidence: [docs/architecture.md#L25-L29](https://github.com/sondera-ai/sondera-coding-agent-hooks/blob/9efefedd249ee23c48608070978dd1a08a3be1ff/docs/architecture.md#L25-L29)
- design-choices (4 claim(s)):
  - [observation/documented] Agent-specific tool names normalize to shared event types (Claude's Bash, Cursor's shell hook, Copilot's and Gemini's bash all become ShellCommand), so one Cedar rule set governs every supported agent. -- evidence: [docs/architecture.md#L45-L51](https://github.com/sondera-ai/sondera-coding-agent-hooks/blob/9efefedd249ee23c48608070978dd1a08a3be1ff/docs/architecture.md#L45-L51)
  - [observation/documented] Agent execution is modeled as a trajectory of typed events in four categories: Action (pre-execution), Observation (post-execution), Control (lifecycle), and State (environment snapshots). -- evidence: [docs/architecture.md#L38-L43](https://github.com/sondera-ai/sondera-coding-agent-hooks/blob/9efefedd249ee23c48608070978dd1a08a3be1ff/docs/architecture.md#L38-L43), [docs/architecture.md#L35-L36](https://github.com/sondera-ai/sondera-coding-agent-hooks/blob/9efefedd249ee23c48608070978dd1a08a3be1ff/docs/architecture.md#L35-L36)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: CI runs cargo fmt --check, clippy with -D warnings, cargo doc, cargo test --locked --workspace, cargo deny check, and buf lint/format from crates/schema/proto; working conventions live in AGENTS.md. -- evidence: [docs/development.md#L20-L21](https://github.com/sondera-ai/sondera-coding-agent-hooks/blob/9efefedd249ee23c48608070978dd1a08a3be1ff/docs/development.md#L20-L21), [docs/development.md#L9-L11](https://github.com/sondera-ai/sondera-coding-agent-hooks/blob/9efefedd249ee23c48608070978dd1a08a3be1ff/docs/development.md#L9-L11), [docs/development.md#L14-L14](https://github.com/sondera-ai/sondera-coding-agent-hooks/blob/9efefedd249ee23c48608070978dd1a08a3be1ff/docs/development.md#L14-L14), [docs/development.md#L17-L18](https://github.com/sondera-ai/sondera-coding-agent-hooks/blob/9efefedd249ee23c48608070978dd1a08a3be1ff/docs/development.md#L17-L18), [docs/development.md#L56-L58](https://github.com/sondera-ai/sondera-coding-agent-hooks/blob/9efefedd249ee23c48608070978dd1a08a3be1ff/docs/development.md#L56-L58)
  - [observation/documented] Repository development practice: integration tests needing a reachable model provider are #[ignore]d by default and run explicitly with `cargo test -- --ignored` once the configured provider is up. -- evidence: [docs/development.md#L23-L25](https://github.com/sondera-ai/sondera-coding-agent-hooks/blob/9efefedd249ee23c48608070978dd1a08a3be1ff/docs/development.md#L23-L25)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] Hook adapters speak stdin/stdout JSON with each agent, normalize the payload, and forward it over gRPC to `sondera serve` on loopback TCP, 127.0.0.1:50051 by default. -- evidence: [docs/architecture.md#L5-L8](https://github.com/sondera-ai/sondera-coding-agent-hooks/blob/9efefedd249ee23c48608070978dd1a08a3be1ff/docs/architecture.md#L5-L8)
  - [observation/documented] `sondera serve` runs two gRPC surfaces on one address: `sondera.harness.v1` for Cedar-backed adjudication and `sondera.console.v1` for agent and trajectory reads over the same store. -- evidence: [docs/getting-started.md#L40-L43](https://github.com/sondera-ai/sondera-coding-agent-hooks/blob/9efefedd249ee23c48608070978dd1a08a3be1ff/docs/getting-started.md#L40-L43), [docs/getting-started.md#L38-L38](https://github.com/sondera-ai/sondera-coding-agent-hooks/blob/9efefedd249ee23c48608070978dd1a08a3be1ff/docs/getting-started.md#L38-L38)
- memory-state (1 claim(s)):
  - [observation/documented] Trajectories persist in a Turso (SQLite) store defaulting to ~/.sondera/trajectories/trajectories.db, overridable via --db; the console reads agents and trajectories from the same store. -- evidence: [docs/configuration.md#L32-L37](https://github.com/sondera-ai/sondera-coding-agent-hooks/blob/9efefedd249ee23c48608070978dd1a08a3be1ff/docs/configuration.md#L32-L37), [docs/development.md#L29-L47](https://github.com/sondera-ai/sondera-coding-agent-hooks/blob/9efefedd249ee23c48608070978dd1a08a3be1ff/docs/development.md#L29-L47), [docs/getting-started.md#L49-L54](https://github.com/sondera-ai/sondera-coding-agent-hooks/blob/9efefedd249ee23c48608070978dd1a08a3be1ff/docs/getting-started.md#L49-L54), [docs/getting-started.md#L40-L43](https://github.com/sondera-ai/sondera-coding-agent-hooks/blob/9efefedd249ee23c48608070978dd1a08a3be1ff/docs/getting-started.md#L40-L43)
- orchestration: unknown (no source-linked claim submitted for this facet)
More evidence: [full detail](sondera-coding-agent-hooks.detail.md)

Metadata and full claim list: [full detail](sondera-coding-agent-hooks.detail.md)
Human notes ([notes](sondera-coding-agent-hooks.notes.md), never overwritten by build)

[Back to map index](../../index.md)
