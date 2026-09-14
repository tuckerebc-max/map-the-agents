# klaatai/klaatcode

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 062c4ac89a5a @ ff92e7ef075c9d71

## Summary (orientation draft, not independently verified)

Selected evidence records: The CLI can run as an HTTP server (`klaatcode serve --port 4200`) exposing /v1/health, /v1/info, /v1/chat and /v1/run with SSE streaming, and `klaatcode web` serves a browser UI on the same server. The client is described as a thin terminal to the hosted Klaatu service, which performs routing, model health tracking, pricing, and code-graph indexing server-side.

## Source coverage

Source coverage (partial): 2 of 5 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 19 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

19 claim(s) across 10 facet(s); 3 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (5 claim(s)):
  - [observation/documented] The client is described as a thin terminal to the hosted Klaatu service, which performs routing, model health tracking, pricing, and code-graph indexing server-side. -- evidence: [README.md#L46-L46](https://github.com/KlaatAI/klaatcode/blob/062c4ac89a5a6de38f87cb402f3ba63b959e73e8/README.md#L46-L46)
  - [observation/documented] Requests are classified and routed across cost tiers (nano, fast, code, reason, heavy, opt-in titan), with automatic escalation on harder tasks and de-escalation when the daily cap is spent. -- evidence: [README.md#L150-L150](https://github.com/KlaatAI/klaatcode/blob/062c4ac89a5a6de38f87cb402f3ba63b959e73e8/README.md#L150-L150), [README.md#L169-L169](https://github.com/KlaatAI/klaatcode/blob/062c4ac89a5a6de38f87cb402f3ba63b959e73e8/README.md#L169-L169), [README.md#L160-L167](https://github.com/KlaatAI/klaatcode/blob/062c4ac89a5a6de38f87cb402f3ba63b959e73e8/README.md#L160-L167)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributions follow CONTRIBUTING.md for dev setup and the PR process, and `bun run bench:selfcheck` must pass before a PR is reviewed. -- evidence: [README.md#L542-L542](https://github.com/KlaatAI/klaatcode/blob/062c4ac89a5a6de38f87cb402f3ba63b959e73e8/README.md#L542-L542)
- skills-patterns (1 claim(s)):
  - [observation/documented] Skills are reusable prompt templates saved as .md files in .klaatai/skills/ (project) or ~/.klaatai/skills/ (global), invoked via /skill commands; hooks run shell commands on lifecycle events and before_tool hooks can block tool calls. -- evidence: [README.md#L327-L327](https://github.com/KlaatAI/klaatcode/blob/062c4ac89a5a6de38f87cb402f3ba63b959e73e8/README.md#L327-L327), [README.md#L304-L304](https://github.com/KlaatAI/klaatcode/blob/062c4ac89a5a6de38f87cb402f3ba63b959e73e8/README.md#L304-L304), [README.md#L306-L310](https://github.com/KlaatAI/klaatcode/blob/062c4ac89a5a6de38f87cb402f3ba63b959e73e8/README.md#L306-L310), [README.md#L314-L314](https://github.com/KlaatAI/klaatcode/blob/062c4ac89a5a6de38f87cb402f3ba63b959e73e8/README.md#L314-L314)
- interfaces (4 claim(s)):
  - [observation/documented] The CLI can run as an HTTP server (`klaatcode serve --port 4200`) exposing /v1/health, /v1/info, /v1/chat and /v1/run with SSE streaming, and `klaatcode web` serves a browser UI on the same server. -- evidence: [README.md#L425-L427](https://github.com/KlaatAI/klaatcode/blob/062c4ac89a5a6de38f87cb402f3ba63b959e73e8/README.md#L425-L427), [README.md#L434-L434](https://github.com/KlaatAI/klaatcode/blob/062c4ac89a5a6de38f87cb402f3ba63b959e73e8/README.md#L434-L434), [README.md#L429-L432](https://github.com/KlaatAI/klaatcode/blob/062c4ac89a5a6de38f87cb402f3ba63b959e73e8/README.md#L429-L432)
  - [observation/documented] The CLI is a full MCP client supporting stdio and Streamable HTTP transports, with OAuth 2.1 (discovery, dynamic client registration, PKCE) for remote servers requiring auth, managed via /mcp. -- evidence: [README.md#L286-L287](https://github.com/KlaatAI/klaatcode/blob/062c4ac89a5a6de38f87cb402f3ba63b959e73e8/README.md#L286-L287), [README.md#L289-L289](https://github.com/KlaatAI/klaatcode/blob/062c4ac89a5a6de38f87cb402f3ba63b959e73e8/README.md#L289-L289), [README.md#L284-L284](https://github.com/KlaatAI/klaatcode/blob/062c4ac89a5a6de38f87cb402f3ba63b959e73e8/README.md#L284-L284)
- memory-state (2 claim(s)):
  - [observation/documented] Sessions are saved as transcripts in ~/.klaatai/sessions/ with /sessions, /resume, and /export commands; a background pass distills durable project and user facts into ~/.klaatai/memory/ that loads at session start. -- evidence: [CHANGELOG.md#L12-L14](https://github.com/KlaatAI/klaatcode/blob/062c4ac89a5a6de38f87cb402f3ba63b959e73e8/CHANGELOG.md#L12-L14), [README.md#L259-L264](https://github.com/KlaatAI/klaatcode/blob/062c4ac89a5a6de38f87cb402f3ba63b959e73e8/README.md#L259-L264), [README.md#L257-L257](https://github.com/KlaatAI/klaatcode/blob/062c4ac89a5a6de38f87cb402f3ba63b959e73e8/README.md#L257-L257)
  - [observation/documented] Context management includes mechanical per-request compaction, noise-filtered command output, attention-ordered history, tier-scaled compaction budgets, and a self-check that snapshots critical state before summarizing and verifies it after. -- evidence: [README.md#L236-L243](https://github.com/KlaatAI/klaatcode/blob/062c4ac89a5a6de38f87cb402f3ba63b959e73e8/README.md#L236-L243)
- orchestration (1 claim(s)):
More evidence: [full detail](klaatcode.detail.md)

Metadata and full claim list: [full detail](klaatcode.detail.md)
Human notes ([notes](klaatcode.notes.md), never overwritten by build)

[Back to map index](../../index.md)
