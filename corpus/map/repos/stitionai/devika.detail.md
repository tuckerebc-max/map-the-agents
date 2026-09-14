# stitionai/devika -- full detail

[Back to orientation](devika.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/stitionai/devika/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/201e280ced5e9941.json](../../../wiki/dossiers/stitionai/devika/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/201e280ced5e9941.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] Devika's documented architecture includes a web chat UI, an Agent Core orchestrating planning and execution, specialized sub-agents, LLM integration, browser interaction, project/state management, and a database layer. -- evidence: [docs/architecture/ARCHITECTURE.md#L31-L38](https://github.com/stitionai/devika/blob/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/docs/architecture/ARCHITECTURE.md#L31-L38), [docs/architecture/README.md#L5-L13](https://github.com/stitionai/devika/blob/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/docs/architecture/README.md#L5-L13) (`clm_c01d4593d3c981c9ef79be09549b11dc4cf1fc31cc8b3357d63fb78d62e153af`)
- [observation/documented] Each sub-agent is implemented as a separate Python class and communicates with LLMs via Jinja2 prompt templates, following a render-query-validate-return pattern. -- evidence: [docs/architecture/ARCHITECTURE.md#L67-L67](https://github.com/stitionai/devika/blob/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/docs/architecture/ARCHITECTURE.md#L67-L67), [docs/architecture/ARCHITECTURE.md#L119-L124](https://github.com/stitionai/devika/blob/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/docs/architecture/ARCHITECTURE.md#L119-L124) (`clm_622d45aa66c0f7e051e9bfcd0bd046cde791790c992cd8d7dd934e255462c8eb`)

## design-choices (2 claim(s))

- [observation/documented] Stated design principles include modularity via specialized agents, pluggable LLMs and services, persistence for pause/resume and auditing, and real-time transparency of the agent's thought process to the user. -- evidence: [docs/architecture/ARCHITECTURE.md#L246-L249](https://github.com/stitionai/devika/blob/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/docs/architecture/ARCHITECTURE.md#L246-L249) (`clm_ddd283470e3650deea1e05350d740f41f84009a25061643cfc909d39a2f3b6e9`)
- [observation/documented] Agents are designed to be stateless and idempotent where possible, with state and history managed centrally by the Agent Core and passed into agents as needed. -- evidence: [docs/architecture/ARCHITECTURE.md#L126-L126](https://github.com/stitionai/devika/blob/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/docs/architecture/ARCHITECTURE.md#L126-L126) (`clm_2ef8170cd13868481f5a1cc711be6664a05135f2cbd9dcb5048a2370e1121e50`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] Browser automation is provided by Browser and Crawler classes built on Playwright (Chromium), supporting navigation, DOM queries, content extraction, screenshots, and an LLM-driven action loop (e.g. CLICK or TYPE commands) over live pages. -- evidence: [docs/architecture/ARCHITECTURE.md#L154-L157](https://github.com/stitionai/devika/blob/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/docs/architecture/ARCHITECTURE.md#L154-L157), [docs/architecture/ARCHITECTURE.md#L147-L152](https://github.com/stitionai/devika/blob/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/docs/architecture/ARCHITECTURE.md#L147-L152), [docs/architecture/ARCHITECTURE.md#L159-L163](https://github.com/stitionai/devika/blob/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/docs/architecture/ARCHITECTURE.md#L159-L163) (`clm_89017ea5798b949442207ac1ef8d483e87e6eb39ea8761c48b4340ddc3709084`)
- [observation/documented] Devika integrates external services through GitHub and Netlify wrapper classes for git operations (clone, listing repos) and deploying web apps, returning deployed site URLs to the user. -- evidence: [docs/architecture/ARCHITECTURE.md#L218-L219](https://github.com/stitionai/devika/blob/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/docs/architecture/ARCHITECTURE.md#L218-L219), [docs/architecture/ARCHITECTURE.md#L221-L226](https://github.com/stitionai/devika/blob/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/docs/architecture/ARCHITECTURE.md#L221-L226), [docs/architecture/ARCHITECTURE.md#L215-L216](https://github.com/stitionai/devika/blob/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/docs/architecture/ARCHITECTURE.md#L215-L216) (`clm_49b8fe536eac252e34cf122a6ad079b9c1d8818b99b8afd95bd176e16f50c2da`)

## memory-state (1 claim(s))

- [observation/documented] Project metadata and agent state (steps, internal monologue, browser/terminal interactions, token usage) are persisted in SQLite via SQLModel, enabling multi-project work, session continuity, auditing, and resume after interruptions. -- evidence: [docs/architecture/ARCHITECTURE.md#L195-L200](https://github.com/stitionai/devika/blob/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/docs/architecture/ARCHITECTURE.md#L195-L200), [docs/architecture/ARCHITECTURE.md#L206-L209](https://github.com/stitionai/devika/blob/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/docs/architecture/ARCHITECTURE.md#L206-L209), [docs/architecture/ARCHITECTURE.md#L179-L181](https://github.com/stitionai/devika/blob/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/docs/architecture/ARCHITECTURE.md#L179-L181), [docs/architecture/ARCHITECTURE.md#L202-L204](https://github.com/stitionai/devika/blob/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/docs/architecture/ARCHITECTURE.md#L202-L204) (`clm_90899b63be99daf23563bbde8a4a20e8f08584d2892cbdbe472bb33f86c51198`)

## orchestration (1 claim(s))

- [observation/documented] The Agent Core runs a loop where a user prompt goes to the Planner for a step plan, the Researcher extracts search queries, web results are formatted, and the Coder generates code saved to disk; follow-up prompts route through an Action agent to Runner, Feature, Patcher, or Reporter agents. -- evidence: [ARCHITECTURE.md#L46-L56](https://github.com/stitionai/devika/blob/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/ARCHITECTURE.md#L46-L56), [docs/architecture/ARCHITECTURE.md#L46-L56](https://github.com/stitionai/devika/blob/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/docs/architecture/ARCHITECTURE.md#L46-L56) (`clm_3c9ab9f86d4953be3311393b64c74883d9e292d0b0a6f77c785a66283b291de8`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] Devika supports multiple LLM providers including Claude, GPT-4/GPT-3, Gemini, Mistral, Groq, and self-hosted models via Ollama, with a unified LLM class abstracting provider APIs; the README recommends the Claude 3 family for optimal performance. -- evidence: [ARCHITECTURE.md#L136-L139](https://github.com/stitionai/devika/blob/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/ARCHITECTURE.md#L136-L139), [docs/architecture/ARCHITECTURE.md#L132-L134](https://github.com/stitionai/devika/blob/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/docs/architecture/ARCHITECTURE.md#L132-L134), [README.md#L45-L53](https://github.com/stitionai/devika/blob/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/README.md#L45-L53) (`clm_14bdfab44509b1b44797209d949e2219ac69d15dfa2219608fb568681b4235c9`)
- [observation/documented] Runtime requirements are Python >= 3.10 and < 3.12, Node.js >= 18, and bun; Playwright is installed for browser capabilities, and API keys (OpenAI, Claude, Bing, Google, Netlify, etc.) are configured via a config.toml file and the UI settings page. -- evidence: [README.md#L137-L137](https://github.com/stitionai/devika/blob/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/README.md#L137-L137), [README.md#L63-L68](https://github.com/stitionai/devika/blob/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/README.md#L63-L68), [README.md#L139-L148](https://github.com/stitionai/devika/blob/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/README.md#L139-L148), [README.md#L98-L118](https://github.com/stitionai/devika/blob/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/README.md#L98-L118) (`clm_1d7a27b8b04ec56728b0ac5bdb318ef6fa6ba9df9294894b80e6d8f7977c6f1d`)

## limitations (1 claim(s))

- [observation/documented] The README states the project is in a very early development/experimental stage with many unimplemented or broken features at the time of writing. -- evidence: [README.md#L13-L14](https://github.com/stitionai/devika/blob/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/README.md#L13-L14) (`clm_a4fae0888b325dc2e1ba1e5a692f4777f4377a53e981e12205ce66a880022664`)

## relevance (1 claim(s))

- [observation/documented] Devika is positioned as an open-source alternative to Cognition AI's Devin, with the stated goal of matching and eventually beating Devin's SWE-bench score; the README also points to Opcode as its successor iteration. -- evidence: [README.md#L36-L37](https://github.com/stitionai/devika/blob/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/README.md#L36-L37), [README.md#L1-L1](https://github.com/stitionai/devika/blob/80bb343cbe4a4e5f5a0ba08d2524920139baceb6/README.md#L1-L1) (`clm_281ba8de7fae4deccd59510211fefbd5ec291a194aa052e328aba38ef476de70`)

