# awslabs/cli-agent-orchestrator

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 948c3d8004fa @ e8d798b8201b64d1

## Summary (orientation draft, not independently verified)

The evidence consists solely of CHANGELOG.md entries for awslabs/cli-agent-orchestrator, documenting an agent-orchestration product with multiple CLI providers, MCP-based orchestration tools, memory/self-learning features, a web UI, and security fixes. Claims below are documented observations from the changelog; no code or contributor-workflow evidence is present. Evidence coverage: 203 of 400 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 3 of 59 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] The project ships a cao-mcp-server that exposes orchestration tools such as assign, handoff, report_outcome, list_outcomes, and store_lesson to agents over MCP. -- evidence: [CHANGELOG.md#L131-L136](https://github.com/awslabs/cli-agent-orchestrator/blob/948c3d8004faa9f2f61b1c65dcde19291d7e072b/CHANGELOG.md#L131-L136)
  - [observation/documented] Multiple agent CLI providers are supported, including MiniMax Code (mcode), Oh My Pi (omp), xAI Grok Build CLI (grok_cli), Cursor CLI, and Antigravity CLI (agy). -- evidence: [CHANGELOG.md#L432-L432](https://github.com/awslabs/cli-agent-orchestrator/blob/948c3d8004faa9f2f61b1c65dcde19291d7e072b/CHANGELOG.md#L432-L432), [CHANGELOG.md#L62-L69](https://github.com/awslabs/cli-agent-orchestrator/blob/948c3d8004faa9f2f61b1c65dcde19291d7e072b/CHANGELOG.md#L62-L69), [CHANGELOG.md#L450-L450](https://github.com/awslabs/cli-agent-orchestrator/blob/948c3d8004faa9f2f61b1c65dcde19291d7e072b/CHANGELOG.md#L450-L450)
- design-choices (1 claim(s)):
  - [observation/documented] Sessions run in tmux terminals with a conductor concept: a session's first (oldest surviving) terminal is normally its conductor, and five consumers depend on that ordering. -- evidence: [CHANGELOG.md#L129-L129](https://github.com/awslabs/cli-agent-orchestrator/blob/948c3d8004faa9f2f61b1c65dcde19291d7e072b/CHANGELOG.md#L129-L129)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] CLI commands cao agent assign|handoff|send-message|status|result|cancel exist as a fallback when a terminal's MCP connection is unavailable, sharing an orchestration module with the MCP tools. -- evidence: [CHANGELOG.md#L107-L112](https://github.com/awslabs/cli-agent-orchestrator/blob/948c3d8004faa9f2f61b1c65dcde19291d7e072b/CHANGELOG.md#L107-L112)
  - [observation/documented] A Web UI provides a Profiles tab for browsing, creating, editing, cloning, and deleting agent profiles over profile management APIs, plus memory-system and fleet-panel views. -- evidence: [CHANGELOG.md#L12-L15](https://github.com/awslabs/cli-agent-orchestrator/blob/948c3d8004faa9f2f61b1c65dcde19291d7e072b/CHANGELOG.md#L12-L15), [CHANGELOG.md#L476-L476](https://github.com/awslabs/cli-agent-orchestrator/blob/948c3d8004faa9f2f61b1c65dcde19291d7e072b/CHANGELOG.md#L476-L476), [CHANGELOG.md#L428-L428](https://github.com/awslabs/cli-agent-orchestrator/blob/948c3d8004faa9f2f61b1c65dcde19291d7e072b/CHANGELOG.md#L428-L428)
- memory-state (2 claim(s)):
  - [observation/documented] The system includes a memory layer with typed relationship storage, memory plugins for Claude Code, Kiro, and Codex, and a wiki with self-healing via 'cao memory heal'. -- evidence: [CHANGELOG.md#L288-L288](https://github.com/awslabs/cli-agent-orchestrator/blob/948c3d8004faa9f2f61b1c65dcde19291d7e072b/CHANGELOG.md#L288-L288), [CHANGELOG.md#L426-L426](https://github.com/awslabs/cli-agent-orchestrator/blob/948c3d8004faa9f2f61b1c65dcde19291d7e072b/CHANGELOG.md#L426-L426), [CHANGELOG.md#L452-L452](https://github.com/awslabs/cli-agent-orchestrator/blob/948c3d8004faa9f2f61b1c65dcde19291d7e072b/CHANGELOG.md#L452-L452)
  - [observation/documented] An opt-in self-learning loop captures outcomes, performs retrospection, and promotes instructions; a skills/cao-learning skill instructs agents how to use it. -- evidence: [CHANGELOG.md#L25-L32](https://github.com/awslabs/cli-agent-orchestrator/blob/948c3d8004faa9f2f61b1c65dcde19291d7e072b/CHANGELOG.md#L25-L32), [CHANGELOG.md#L280-L280](https://github.com/awslabs/cli-agent-orchestrator/blob/948c3d8004faa9f2f61b1c65dcde19291d7e072b/CHANGELOG.md#L280-L280)
- orchestration (1 claim(s)):
  - [observation/documented] Orchestration includes supervisor/worker flows, a run engine with durable run journal and playback, frozen execution manifests with plan approval, and a cross-node fleet coordinator. -- evidence: [CHANGELOG.md#L460-L460](https://github.com/awslabs/cli-agent-orchestrator/blob/948c3d8004faa9f2f61b1c65dcde19291d7e072b/CHANGELOG.md#L460-L460), [CHANGELOG.md#L464-L464](https://github.com/awslabs/cli-agent-orchestrator/blob/948c3d8004faa9f2f61b1c65dcde19291d7e072b/CHANGELOG.md#L464-L464), [CHANGELOG.md#L79-L79](https://github.com/awslabs/cli-agent-orchestrator/blob/948c3d8004faa9f2f61b1c65dcde19291d7e072b/CHANGELOG.md#L79-L79), [CHANGELOG.md#L105-L105](https://github.com/awslabs/cli-agent-orchestrator/blob/948c3d8004faa9f2f61b1c65dcde19291d7e072b/CHANGELOG.md#L105-L105)
- tools-permissions (1 claim(s)):
  - [observation/documented] The grok_cli provider offers native hard tool restrictions, and network egress is gated behind a web_fetch tool category; per-role tool-restriction examples are provided. -- evidence: [CHANGELOG.md#L85-L85](https://github.com/awslabs/cli-agent-orchestrator/blob/948c3d8004faa9f2f61b1c65dcde19291d7e072b/CHANGELOG.md#L85-L85), [CHANGELOG.md#L62-L69](https://github.com/awslabs/cli-agent-orchestrator/blob/948c3d8004faa9f2f61b1c65dcde19291d7e072b/CHANGELOG.md#L62-L69), [CHANGELOG.md#L436-L436](https://github.com/awslabs/cli-agent-orchestrator/blob/948c3d8004faa9f2f61b1c65dcde19291d7e072b/CHANGELOG.md#L436-L436)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
More evidence: [full detail](cli-agent-orchestrator.detail.md)

Metadata and full claim list: [full detail](cli-agent-orchestrator.detail.md)
Human notes ([notes](cli-agent-orchestrator.notes.md), never overwritten by build)

[Back to map index](../../index.md)
