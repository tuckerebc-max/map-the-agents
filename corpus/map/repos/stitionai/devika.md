# stitionai/devika

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 80bb343cbe4a @ 201e280ced5e9941

## Summary (orientation draft, not independently verified)

The snapshot consists of README and architecture documentation describing Devika, an open-source agentic AI software engineer modeled after Devin, with a multi-agent architecture (Planner, Researcher, Coder, etc.), LLM/browser/service integrations, and SQLite-backed persistence. No source code is included in the evidence, so all claims are documentation-based. Evidence coverage: 132 of 137 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 10 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] Devika's documented architecture includes a web chat UI, an Agent Core orchestrating planning and execution, specialized sub-agents, LLM integration, browser interaction, project/state management, and a database layer. -- evidence: [docs/architecture/ARCHITECTURE.md#L31-L38](https://github.com/stitionai/devika/blob/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/docs/architecture/ARCHITECTURE.md#L31-L38), [docs/architecture/README.md#L5-L13](https://github.com/stitionai/devika/blob/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/docs/architecture/README.md#L5-L13)
  - [observation/documented] Each sub-agent is implemented as a separate Python class and communicates with LLMs via Jinja2 prompt templates, following a render-query-validate-return pattern. -- evidence: [docs/architecture/ARCHITECTURE.md#L67-L67](https://github.com/stitionai/devika/blob/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/docs/architecture/ARCHITECTURE.md#L67-L67), [docs/architecture/ARCHITECTURE.md#L119-L124](https://github.com/stitionai/devika/blob/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/docs/architecture/ARCHITECTURE.md#L119-L124)
- design-choices (2 claim(s)):
  - [observation/documented] Stated design principles include modularity via specialized agents, pluggable LLMs and services, persistence for pause/resume and auditing, and real-time transparency of the agent's thought process to the user. -- evidence: [docs/architecture/ARCHITECTURE.md#L246-L249](https://github.com/stitionai/devika/blob/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/docs/architecture/ARCHITECTURE.md#L246-L249)
  - [observation/documented] Agents are designed to be stateless and idempotent where possible, with state and history managed centrally by the Agent Core and passed into agents as needed. -- evidence: [docs/architecture/ARCHITECTURE.md#L126-L126](https://github.com/stitionai/devika/blob/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/docs/architecture/ARCHITECTURE.md#L126-L126)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] Browser automation is provided by Browser and Crawler classes built on Playwright (Chromium), supporting navigation, DOM queries, content extraction, screenshots, and an LLM-driven action loop (e.g. CLICK or TYPE commands) over live pages. -- evidence: [docs/architecture/ARCHITECTURE.md#L154-L157](https://github.com/stitionai/devika/blob/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/docs/architecture/ARCHITECTURE.md#L154-L157), [docs/architecture/ARCHITECTURE.md#L147-L152](https://github.com/stitionai/devika/blob/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/docs/architecture/ARCHITECTURE.md#L147-L152), [docs/architecture/ARCHITECTURE.md#L159-L163](https://github.com/stitionai/devika/blob/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/docs/architecture/ARCHITECTURE.md#L159-L163)
  - [observation/documented] Devika integrates external services through GitHub and Netlify wrapper classes for git operations (clone, listing repos) and deploying web apps, returning deployed site URLs to the user. -- evidence: [docs/architecture/ARCHITECTURE.md#L218-L219](https://github.com/stitionai/devika/blob/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/docs/architecture/ARCHITECTURE.md#L218-L219), [docs/architecture/ARCHITECTURE.md#L221-L226](https://github.com/stitionai/devika/blob/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/docs/architecture/ARCHITECTURE.md#L221-L226), [docs/architecture/ARCHITECTURE.md#L215-L216](https://github.com/stitionai/devika/blob/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/docs/architecture/ARCHITECTURE.md#L215-L216)
- memory-state (1 claim(s)):
  - [observation/documented] Project metadata and agent state (steps, internal monologue, browser/terminal interactions, token usage) are persisted in SQLite via SQLModel, enabling multi-project work, session continuity, auditing, and resume after interruptions. -- evidence: [docs/architecture/ARCHITECTURE.md#L195-L200](https://github.com/stitionai/devika/blob/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/docs/architecture/ARCHITECTURE.md#L195-L200), [docs/architecture/ARCHITECTURE.md#L206-L209](https://github.com/stitionai/devika/blob/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/docs/architecture/ARCHITECTURE.md#L206-L209), [docs/architecture/ARCHITECTURE.md#L179-L181](https://github.com/stitionai/devika/blob/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/docs/architecture/ARCHITECTURE.md#L179-L181), [docs/architecture/ARCHITECTURE.md#L202-L204](https://github.com/stitionai/devika/blob/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/docs/architecture/ARCHITECTURE.md#L202-L204)
- orchestration (1 claim(s)):
  - [observation/documented] The Agent Core runs a loop where a user prompt goes to the Planner for a step plan, the Researcher extracts search queries, web results are formatted, and the Coder generates code saved to disk; follow-up prompts route through an Action agent to Runner, Feature, Patcher, or Reporter agents. -- evidence: [ARCHITECTURE.md#L46-L56](https://github.com/stitionai/devika/blob/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/ARCHITECTURE.md#L46-L56), [docs/architecture/ARCHITECTURE.md#L46-L56](https://github.com/stitionai/devika/blob/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/docs/architecture/ARCHITECTURE.md#L46-L56)
More evidence: [full detail](devika.detail.md)

Metadata and full claim list: [full detail](devika.detail.md)
Human notes ([notes](devika.notes.md), never overwritten by build)

[Back to map index](../../index.md)
