# agentlas-ai/agentlas-os

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit dcd9dd800f65 @ 9dd257fdc1d230aa

## Summary (orientation draft, not independently verified)

The snapshot documents Agentlas Core Engine Meta-Agent Team, a Markdown-first meta-agent system with four builder routes that generate or repair portable Agentlas-compatible agent/team packages, plus a changelog describing a shipped Hephaestus/Agentlas runtime with measured behaviors, permission policies, and packaging limits. Evidence coverage: 68 of 400 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 12 of 15 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 13 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

13 claim(s) across 10 facet(s); 3 facet(s) unknown.

- specifications (3 claim(s)):
  - [observation/documented] The agent's mission is to route rough agent, team, or package requests to the right core builder and produce a portable Agentlas-compatible package. -- evidence: [agent.md#L5-L6](https://github.com/agentlas-ai/Agentlas-OS/blob/dcd9dd800f65d9b7ee1823cd096fc96cb4e7fc22/agent.md#L5-L6)
  - [observation/documented] Inputs include a user goal plus optional target project path, repository, ZIP, prompt, existing agent, runtime requirements, and a public/private boundary. -- evidence: [agent.md#L10-L13](https://github.com/agentlas-ai/Agentlas-OS/blob/dcd9dd800f65d9b7ee1823cd096fc96cb4e7fc22/agent.md#L10-L13)
- components (1 claim(s)):
  - [observation/documented] Four core builders are defined: single-agent-builder, multi-agent-team-builder, agentlas-packager, and session-agent-builder, each with a distinct role such as converting exported sessions into reviewed reusable candidates. -- evidence: [ARCHITECTURE.md#L23-L34](https://github.com/agentlas-ai/Agentlas-OS/blob/dcd9dd800f65d9b7ee1823cd096fc96cb4e7fc22/ARCHITECTURE.md#L23-L34), [agent.md#L17-L23](https://github.com/agentlas-ai/Agentlas-OS/blob/dcd9dd800f65d9b7ee1823cd096fc96cb4e7fc22/agent.md#L17-L23)
- design-choices (1 claim(s)):
  - [observation/documented] The canonical core is runtime-neutral, with adapters translating the same core into each runtime and adapters instructed not to contain private logic missing from the canonical core. -- evidence: [ARCHITECTURE.md#L186-L186](https://github.com/agentlas-ai/Agentlas-OS/blob/dcd9dd800f65d9b7ee1823cd096fc96cb4e7fc22/ARCHITECTURE.md#L186-L186), [ARCHITECTURE.md#L38-L38](https://github.com/agentlas-ai/Agentlas-OS/blob/dcd9dd800f65d9b7ee1823cd096fc96cb4e7fc22/ARCHITECTURE.md#L38-L38), [ARCHITECTURE.md#L197-L198](https://github.com/agentlas-ai/Agentlas-OS/blob/dcd9dd800f65d9b7ee1823cd096fc96cb4e7fc22/ARCHITECTURE.md#L197-L198)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: the packaging flow runs a Hephaestus security scan, adds .agentlas contracts, removes private or unsafe material, and verifies the package via scripts/verify-package.sh; CI contract gates such as scripts/verify-host-authority-contract.sh run in the cross-platform-wiring workflow. -- evidence: [ARCHITECTURE.md#L202-L216](https://github.com/agentlas-ai/Agentlas-OS/blob/dcd9dd800f65d9b7ee1823cd096fc96cb4e7fc22/ARCHITECTURE.md#L202-L216), [ARCHITECTURE.md#L222-L230](https://github.com/agentlas-ai/Agentlas-OS/blob/dcd9dd800f65d9b7ee1823cd096fc96cb4e7fc22/ARCHITECTURE.md#L222-L230), [CHANGELOG.md#L17-L27](https://github.com/agentlas-ai/Agentlas-OS/blob/dcd9dd800f65d9b7ee1823cd096fc96cb4e7fc22/CHANGELOG.md#L17-L27)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] Runtime adapter surfaces include codex/marketplace.json, .claude/commands, GEMINI.md files, a root AGENTS.md for generic tools, and a bin/ontology CLI for local-first storage/search/graph/memory. -- evidence: [ARCHITECTURE.md#L188-L195](https://github.com/agentlas-ai/Agentlas-OS/blob/dcd9dd800f65d9b7ee1823cd096fc96cb4e7fc22/ARCHITECTURE.md#L188-L195)
  - [observation/documented] The product exposes an MCP tool agentlas_resolve_plugins and a plugins tool-search command; tool search ranks servers before tools and loads input schemas only for the chosen tool. -- evidence: [CHANGELOG.md#L82-L97](https://github.com/agentlas-ai/Agentlas-OS/blob/dcd9dd800f65d9b7ee1823cd096fc96cb4e7fc22/CHANGELOG.md#L82-L97), [CHANGELOG.md#L159-L170](https://github.com/agentlas-ai/Agentlas-OS/blob/dcd9dd800f65d9b7ee1823cd096fc96cb4e7fc22/CHANGELOG.md#L159-L170)
- memory-state (1 claim(s)):
  - [observation/documented] Durable memory writes go through Memory Events and Memory Tickets, and generated packages may include memory-map, memory-tickets, and vault-reference files; recall counters and semantic index state serialize read-modify-writes. -- evidence: [ARCHITECTURE.md#L40-L105](https://github.com/agentlas-ai/Agentlas-OS/blob/dcd9dd800f65d9b7ee1823cd096fc96cb4e7fc22/ARCHITECTURE.md#L40-L105), [agent.md#L45-L66](https://github.com/agentlas-ai/Agentlas-OS/blob/dcd9dd800f65d9b7ee1823cd096fc96cb4e7fc22/agent.md#L45-L66), [CHANGELOG.md#L49-L62](https://github.com/agentlas-ai/Agentlas-OS/blob/dcd9dd800f65d9b7ee1823cd096fc96cb4e7fc22/CHANGELOG.md#L49-L62)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
  - [observation/documented] The permissionPolicy schema accepts a host mode for network, shell, fileRead.mode, and mcp.mode, where the package declares no tool ceiling and the host runtime decides at execution time, emitting enforcement receipts. -- evidence: [CHANGELOG.md#L17-L27](https://github.com/agentlas-ai/Agentlas-OS/blob/dcd9dd800f65d9b7ee1823cd096fc96cb4e7fc22/CHANGELOG.md#L17-L27)
- evaluation (1 claim(s)):
More evidence: [full detail](agentlas-os.detail.md)

Metadata and full claim list: [full detail](agentlas-os.detail.md)
Human notes ([notes](agentlas-os.notes.md), never overwritten by build)

[Back to map index](../../index.md)
