# ruvnet/ruflo

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: github-rename-resolution, alltheagents.org-backing, github-verified-rename - Projects: navy-yard, Observatory
Formerly: ruvnet/claude-flow (github id 995029641).
Latest snapshot: commit b02c0cacec22 @ 43f85fd862fff196

## Summary (orientation draft, not independently verified)

Ruflo is an agent harness distributed as an npm CLI and Claude Code plugins, exposing MCP servers, swarm orchestration, HNSW vector memory, and agent federation; a roadmap documents known gaps such as skipped integration tests and hardcoded memory paths. Evidence coverage: 130 of 302 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 67 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The README catalogs 35 plugins across categories including core/orchestration, memory, intelligence, testing, security, and domain-specific (e.g. ruflo-swarm, ruflo-rag-memory, ruflo-neural-trader). -- evidence: [README.md#L83-L84](https://github.com/ruvnet/ruflo/blob/b02c0cacec225deea01f586b66a9694393369432/README.md#L83-L84), [README.md#L109-L115](https://github.com/ruvnet/ruflo/blob/b02c0cacec225deea01f586b66a9694393369432/README.md#L109-L115), [README.md#L99-L105](https://github.com/ruvnet/ruflo/blob/b02c0cacec225deea01f586b66a9694393369432/README.md#L99-L105), [README.md#L88-L95](https://github.com/ruvnet/ruflo/blob/b02c0cacec225deea01f586b66a9694393369432/README.md#L88-L95), [README.md#L119-L124](https://github.com/ruvnet/ruflo/blob/b02c0cacec225deea01f586b66a9694393369432/README.md#L119-L124), [README.md#L128-L131](https://github.com/ruvnet/ruflo/blob/b02c0cacec225deea01f586b66a9694393369432/README.md#L128-L131), [README.md#L160-L164](https://github.com/ruvnet/ruflo/blob/b02c0cacec225deea01f586b66a9694393369432/README.md#L160-L164)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: CLAUDE.local.md documents maintainer steps for updating the IPFS/Pinata plugin registry (fetch registry, edit entries, pin via Pinata API, update LIVE_REGISTRY_CID) and warns never to hardcode API keys or commit .env. -- evidence: [CLAUDE.local.md#L25-L25](https://github.com/ruvnet/ruflo/blob/b02c0cacec225deea01f586b66a9694393369432/CLAUDE.local.md#L25-L25), [CLAUDE.local.md#L19-L23](https://github.com/ruvnet/ruflo/blob/b02c0cacec225deea01f586b66a9694393369432/CLAUDE.local.md#L19-L23)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] Ruflo exposes a CLI (npx ruflo) and an MCP server; the README shows registering it in Claude Code via 'claude mcp add claude-flow -- npx ruflo@latest mcp start'. -- evidence: [README.md#L196-L197](https://github.com/ruvnet/ruflo/blob/b02c0cacec225deea01f586b66a9694393369432/README.md#L196-L197)
  - [observation/documented] Two install paths exist: Claude Code plugins (slash commands, zero workspace files) versus full CLI init which scaffolds .claude/, .claude-flow/, CLAUDE.md, hooks, and an MCP server. -- evidence: [README.md#L60-L66](https://github.com/ruvnet/ruflo/blob/b02c0cacec225deea01f586b66a9694393369432/README.md#L60-L66)
- memory-state (1 claim(s)):
  - [observation/documented] Memory uses an HNSW-indexed AgentDB; the README cites measured ~1.9x faster at N=20k versus brute force with recall@10 near 0.99, noting ANN ties or loses at small N. -- evidence: [README.md#L203-L217](https://github.com/ruvnet/ruflo/blob/b02c0cacec225deea01f586b66a9694393369432/README.md#L203-L217)
- orchestration (2 claim(s)):
  - [observation/documented] Swarm coordination supports hierarchical, mesh, and adaptive topologies with consensus, and the architecture diagram shows a Queen-led coordination layer above 100+ specialized agents. -- evidence: [README.md#L352-L374](https://github.com/ruvnet/ruflo/blob/b02c0cacec225deea01f586b66a9694393369432/README.md#L352-L374), [README.md#L203-L217](https://github.com/ruvnet/ruflo/blob/b02c0cacec225deea01f586b66a9694393369432/README.md#L203-L217)
  - [observation/documented] Agent federation lets agents on different machines discover, authenticate (mTLS + ed25519), and exchange work, with PII stripped from outbound messages and per-trust-level policies (BLOCK, REDACT, HASH, PASS). -- evidence: [README.md#L284-L284](https://github.com/ruvnet/ruflo/blob/b02c0cacec225deea01f586b66a9694393369432/README.md#L284-L284), [README.md#L293-L299](https://github.com/ruvnet/ruflo/blob/b02c0cacec225deea01f586b66a9694393369432/README.md#L293-L299)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation (1 claim(s)):
  - [observation/documented] A SOTA comparator benchmark suite compares ruflo against LangGraph, AutoGen, and CrewAI on metrics like cold start, single turn, and RSS, with published matrix JSON for darwin and linux. -- evidence: [README.md#L384-L391](https://github.com/ruvnet/ruflo/blob/b02c0cacec225deea01f586b66a9694393369432/README.md#L384-L391), [README.md#L393-L393](https://github.com/ruvnet/ruflo/blob/b02c0cacec225deea01f586b66a9694393369432/README.md#L393-L393)
- dependencies (1 claim(s)):
More evidence: [full detail](ruflo.detail.md)

Metadata and full claim list: [full detail](ruflo.detail.md)
Human notes ([notes](ruflo.notes.md), never overwritten by build)

[Back to map index](../../index.md)
