# oracle-devrel/oracle-ai-developer-hub

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 3317c535db76 @ 6eaeb11cc5dd8d7d

## Summary (orientation draft, not independently verified)

The repository is a hub of technical resources (apps, notebooks, guides, workshops, partner examples) for building AI applications and agents on Oracle AI Database and OCI services, including an agent-memory notebook collection and a documented choose-your-path friction-pass validation with recorded OAMP quirks. Evidence coverage: 108 of 149 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 12 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] The hub is organized into key areas: apps (reference implementations), notebooks, guides, workshops, and partner-contributed resources, each referenced under its own named path in the README. -- evidence: [README.md#L108-L108](https://github.com/oracle-devrel/oracle-ai-developer-hub/blob/3317c535db76ed698fa92e32a65acd5e5f2769bc/README.md#L108-L108), [README.md#L7-L7](https://github.com/oracle-devrel/oracle-ai-developer-hub/blob/3317c535db76ed698fa92e32a65acd5e5f2769bc/README.md#L7-L7), [README.md#L27-L27](https://github.com/oracle-devrel/oracle-ai-developer-hub/blob/3317c535db76ed698fa92e32a65acd5e5f2769bc/README.md#L27-L27), [README.md#L93-L93](https://github.com/oracle-devrel/oracle-ai-developer-hub/blob/3317c535db76ed698fa92e32a65acd5e5f2769bc/README.md#L93-L93), [README.md#L11-L11](https://github.com/oracle-devrel/oracle-ai-developer-hub/blob/3317c535db76ed698fa92e32a65acd5e5f2769bc/README.md#L11-L11), [README.md#L51-L51](https://github.com/oracle-devrel/oracle-ai-developer-hub/blob/3317c535db76ed698fa92e32a65acd5e5f2769bc/README.md#L51-L51)
  - [observation/documented] A dedicated agent-memory notebook collection covers the oracleagentmemory package, including a developer guide, benchmarks, and end-to-end examples for OpenAI Agents SDK, Claude Agent SDK, and LangGraph. -- evidence: [README.md#L66-L66](https://github.com/oracle-devrel/oracle-ai-developer-hub/blob/3317c535db76ed698fa92e32a65acd5e5f2769bc/README.md#L66-L66), [README.md#L64-L64](https://github.com/oracle-devrel/oracle-ai-developer-hub/blob/3317c535db76ed698fa92e32a65acd5e5f2769bc/README.md#L64-L64)
- design-choices (1 claim(s)):
  - [observation/documented] A decision tree in oamp.md maps memory shapes to tools: OAMP for conversational per-user durable memory, OracleVS for fixed RAG corpora, OracleChatHistory for simple chat logs, and SQL tables for counters and audit trails. -- evidence: [docs/cyp-friction-pass/2026-05-05-oamp-retrofit.md#L131-L138](https://github.com/oracle-devrel/oracle-ai-developer-hub/blob/3317c535db76ed698fa92e32a65acd5e5f2769bc/docs/cyp-friction-pass/2026-05-05-oamp-retrofit.md#L131-L138)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributions are made by forking the repository and submitting pull requests, and contributors are asked to install pre-commit hooks that auto-format code with Ruff for Python and Prettier for JS/TS/JSON/YAML/Markdown. -- evidence: [README.md#L154-L154](https://github.com/oracle-devrel/oracle-ai-developer-hub/blob/3317c535db76ed698fa92e32a65acd5e5f2769bc/README.md#L154-L154), [README.md#L129-L129](https://github.com/oracle-devrel/oracle-ai-developer-hub/blob/3317c535db76ed698fa92e32a65acd5e5f2769bc/README.md#L129-L129), [README.md#L156-L157](https://github.com/oracle-devrel/oracle-ai-developer-hub/blob/3317c535db76ed698fa92e32a65acd5e5f2769bc/README.md#L156-L157), [README.md#L125-L125](https://github.com/oracle-devrel/oracle-ai-developer-hub/blob/3317c535db76ed698fa92e32a65acd5e5f2769bc/README.md#L125-L125)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] A shared oamp_helpers module exposes make_oamp_client, make_oamp_thread, and add_turn convenience functions, with auto-extraction enabled only when OCI_GENAI_API_KEY is set, otherwise degrading to manual-add mode. -- evidence: [docs/cyp-friction-pass/2026-05-05-oamp-retrofit.md#L8-L16](https://github.com/oracle-devrel/oracle-ai-developer-hub/blob/3317c535db76ed698fa92e32a65acd5e5f2769bc/docs/cyp-friction-pass/2026-05-05-oamp-retrofit.md#L8-L16)
- memory-state (1 claim(s)):
  - [observation/documented] The agent-memory notebooks present Oracle AI Database as a unified memory core serving conversation history, durable facts, and entity state instead of separate vector, key-value, and relational stores. -- evidence: [README.md#L64-L64](https://github.com/oracle-devrel/oracle-ai-developer-hub/blob/3317c535db76ed698fa92e32a65acd5e5f2769bc/README.md#L64-L64)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation (2 claim(s)):
  - [observation/documented] An OAMP Benchmarks notebook measures token cost, latency, and response quality of OAMP versus naive flat-history memory across 80 scripted turns with three agent variants. -- evidence: [README.md#L68-L74](https://github.com/oracle-devrel/oracle-ai-developer-hub/blob/3317c535db76ed698fa92e32a65acd5e5f2769bc/README.md#L68-L74)
More evidence: [full detail](oracle-ai-developer-hub.detail.md)

Metadata and full claim list: [full detail](oracle-ai-developer-hub.detail.md)
Human notes ([notes](oracle-ai-developer-hub.notes.md), never overwritten by build)

[Back to map index](../../index.md)
