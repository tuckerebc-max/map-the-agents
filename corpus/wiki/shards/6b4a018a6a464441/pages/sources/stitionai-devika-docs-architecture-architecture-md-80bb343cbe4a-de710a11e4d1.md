---
access: public
aliases: []
claim_ids:
- clm_14bdfab44509b1b44797209d949e2219ac69d15dfa2219608fb568681b4235c9
- clm_2ef8170cd13868481f5a1cc711be6664a05135f2cbd9dcb5048a2370e1121e50
- clm_3c9ab9f86d4953be3311393b64c74883d9e292d0b0a6f77c785a66283b291de8
- clm_49b8fe536eac252e34cf122a6ad079b9c1d8818b99b8afd95bd176e16f50c2da
- clm_622d45aa66c0f7e051e9bfcd0bd046cde791790c992cd8d7dd934e255462c8eb
- clm_89017ea5798b949442207ac1ef8d483e87e6eb39ea8761c48b4340ddc3709084
- clm_90899b63be99daf23563bbde8a4a20e8f08584d2892cbdbe472bb33f86c51198
- clm_c01d4593d3c981c9ef79be09549b11dc4cf1fc31cc8b3357d63fb78d62e153af
- clm_ddd283470e3650deea1e05350d740f41f84009a25061643cfc909d39a2f3b6e9
maturity: draft
page_id: pg_9485354f64be55a4b7abde710a11e4d1
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_182c87c260b85aec966fa770f29052f6
title: stitionai/devika/docs/architecture/ARCHITECTURE.md @ 80bb343cbe4a
updated_at: '2026-09-14T02:43:27Z'
---

# stitionai/devika/docs/architecture/ARCHITECTURE.md @ 80bb343cbe4a

<!-- rcw:begin owner=source:src_182c87c260b85aec966fa770f29052f6 block=evidence -->
- Devika supports multiple LLM providers including Claude, GPT-4/GPT-3, Gemini, Mistral, Groq, and self-hosted models via Ollama, with a unified LLM class abstracting provider APIs; the README recommends the Claude 3 family for optimal performance. [@claim:clm_14bdfab44509b1b44797209d949e2219ac69d15dfa2219608fb568681b4235c9]
- Agents are designed to be stateless and idempotent where possible, with state and history managed centrally by the Agent Core and passed into agents as needed. [@claim:clm_2ef8170cd13868481f5a1cc711be6664a05135f2cbd9dcb5048a2370e1121e50]
- The Agent Core runs a loop where a user prompt goes to the Planner for a step plan, the Researcher extracts search queries, web results are formatted, and the Coder generates code saved to disk; follow-up prompts route through an Action agent to Runner, Feature, Patcher, or Reporter agents. [@claim:clm_3c9ab9f86d4953be3311393b64c74883d9e292d0b0a6f77c785a66283b291de8]
- Devika integrates external services through GitHub and Netlify wrapper classes for git operations (clone, listing repos) and deploying web apps, returning deployed site URLs to the user. [@claim:clm_49b8fe536eac252e34cf122a6ad079b9c1d8818b99b8afd95bd176e16f50c2da]
- Each sub-agent is implemented as a separate Python class and communicates with LLMs via Jinja2 prompt templates, following a render-query-validate-return pattern. [@claim:clm_622d45aa66c0f7e051e9bfcd0bd046cde791790c992cd8d7dd934e255462c8eb]
- Browser automation is provided by Browser and Crawler classes built on Playwright (Chromium), supporting navigation, DOM queries, content extraction, screenshots, and an LLM-driven action loop (e.g. CLICK or TYPE commands) over live pages. [@claim:clm_89017ea5798b949442207ac1ef8d483e87e6eb39ea8761c48b4340ddc3709084]
- Project metadata and agent state (steps, internal monologue, browser/terminal interactions, token usage) are persisted in SQLite via SQLModel, enabling multi-project work, session continuity, auditing, and resume after interruptions. [@claim:clm_90899b63be99daf23563bbde8a4a20e8f08584d2892cbdbe472bb33f86c51198]
- Devika's documented architecture includes a web chat UI, an Agent Core orchestrating planning and execution, specialized sub-agents, LLM integration, browser interaction, project/state management, and a database layer. [@claim:clm_c01d4593d3c981c9ef79be09549b11dc4cf1fc31cc8b3357d63fb78d62e153af]
- Stated design principles include modularity via specialized agents, pluggable LLMs and services, persistence for pause/resume and auditing, and real-time transparency of the agent's thought process to the user. [@claim:clm_ddd283470e3650deea1e05350d740f41f84009a25061643cfc909d39a2f3b6e9]
<!-- rcw:end owner=source:src_182c87c260b85aec966fa770f29052f6 block=evidence -->

## Researcher notes

