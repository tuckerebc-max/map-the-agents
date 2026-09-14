# dimitrigeelen/agentic-engineering-framework

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 35aaaaedc1c3 @ a8e042de383354ce

## Summary (orientation draft, not independently verified)

Selected evidence records: The framework's core principle is traceability: nothing gets done without a task, with conversations, decisions, and artefacts captured in a record called the Context Fabric. A Component Fabric maps how code pieces relate, making a change's blast radius visible before the change rather than after.

## Source coverage

Source coverage (partial): 6 of 19 candidate file(s) selected (selection incomplete); repository tree truncated (partial listing). Claims by basis: 13 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

13 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] A Component Fabric maps how code pieces relate, making a change's blast radius visible before the change rather than after. -- evidence: [README.md#L39-L43](https://github.com/DimitriGeelen/agentic-engineering-framework/blob/35aaaaedc1c32269079b32de14aa31a7bebe2a54/README.md#L39-L43)
- design-choices (1 claim(s)):
  - [observation/documented] The framework's core principle is traceability: nothing gets done without a task, with conversations, decisions, and artefacts captured in a record called the Context Fabric. -- evidence: [README.md#L32-L37](https://github.com/DimitriGeelen/agentic-engineering-framework/blob/35aaaaedc1c32269079b32de14aa31a7bebe2a54/README.md#L32-L37)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The product exposes a `fw` CLI (about 60 verbs across 11 sections) including work-on, audit, recall, fabric blast-radius, handover, serve, tier0 approve, and mcp lifecycle commands. -- evidence: [README.md#L698-L717](https://github.com/DimitriGeelen/agentic-engineering-framework/blob/35aaaaedc1c32269079b32de14aa31a7bebe2a54/README.md#L698-L717)
  - [observation/documented] A Framework MCP server exposes 22 capabilities (16 read-only, 6 agent-authority) to external agents; five sovereignty-bound verbs are deliberately never registered, and agent-authority tools shell out through bin/fw so the same gates fire. -- evidence: [README.md#L502-L507](https://github.com/DimitriGeelen/agentic-engineering-framework/blob/35aaaaedc1c32269079b32de14aa31a7bebe2a54/README.md#L502-L507)
- memory-state (2 claim(s)):
  - [observation/documented] Three memory layers persist across sessions: working memory in .context/working/, project memory in .context/project/, and episodic memory of completed tasks in .context/episodic/. -- evidence: [README.md#L251-L255](https://github.com/DimitriGeelen/agentic-engineering-framework/blob/35aaaaedc1c32269079b32de14aa31a7bebe2a54/README.md#L251-L255), [README.md#L392-L395](https://github.com/DimitriGeelen/agentic-engineering-framework/blob/35aaaaedc1c32269079b32de14aa31a7bebe2a54/README.md#L392-L395)
  - [observation/documented] `fw recall` searches learnings, patterns, decisions, and episodics by meaning rather than keyword, and `fw handover --commit` writes a structured handover the next session reads on start. -- evidence: [README.md#L392-L395](https://github.com/DimitriGeelen/agentic-engineering-framework/blob/35aaaaedc1c32269079b32de14aa31a7bebe2a54/README.md#L392-L395), [README.md#L267-L269](https://github.com/DimitriGeelen/agentic-engineering-framework/blob/35aaaaedc1c32269079b32de14aa31a7bebe2a54/README.md#L267-L269), [README.md#L271-L273](https://github.com/DimitriGeelen/agentic-engineering-framework/blob/35aaaaedc1c32269079b32de14aa31a7bebe2a54/README.md#L271-L273)
- orchestration (1 claim(s)):
  - [observation/documented] The framework wraps an external TermLink binary for cross-terminal, cross-host worker sessions, with bus manifest/read, dispatch send over SSH, and pickup verbs for coordination. -- evidence: [README.md#L489-L491](https://github.com/DimitriGeelen/agentic-engineering-framework/blob/35aaaaedc1c32269079b32de14aa31a7bebe2a54/README.md#L489-L491), [README.md#L493-L500](https://github.com/DimitriGeelen/agentic-engineering-framework/blob/35aaaaedc1c32269079b32de14aa31a7bebe2a54/README.md#L493-L500)
- tools-permissions (3 claim(s)):
  - [observation/documented] A PreToolUse hook intercepts file modifications and refuses edits when no active task is set; build tasks with placeholder acceptance criteria are blocked (policy G-020). -- evidence: [README.md#L222-L225](https://github.com/DimitriGeelen/agentic-engineering-framework/blob/35aaaaedc1c32269079b32de14aa31a7bebe2a54/README.md#L222-L225), [README.md#L230-L231](https://github.com/DimitriGeelen/agentic-engineering-framework/blob/35aaaaedc1c32269079b32de14aa31a7bebe2a54/README.md#L230-L231)
  - [observation/documented] A tiered authority model: Tier 0 destructive commands need human approval via `fw tier0 approve`, Tier 1 edits need an active task, Tier 2 exceptions are single-use and logged, Tier 3 read-only is pre-approved. -- evidence: [README.md#L333-L338](https://github.com/DimitriGeelen/agentic-engineering-framework/blob/35aaaaedc1c32269079b32de14aa31a7bebe2a54/README.md#L333-L338)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
More evidence: [full detail](agentic-engineering-framework.detail.md)

Metadata and full claim list: [full detail](agentic-engineering-framework.detail.md)
Human notes ([notes](agentic-engineering-framework.notes.md), never overwritten by build)

[Back to map index](../../index.md)
