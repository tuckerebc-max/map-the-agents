# build-your-own-coding-agent (`build-your-own-coding-agent`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: yanhua1010
- License: MIT
- Language: TypeScript/Node.js
- Interface: install=cd steps/01-minimal-loop && npm install && npm start (Node.js 20+; requires DeepSeek or GLM API key)
- Model providers: DeepSeek, GLM (Zhipu), Kimi (Chinese domestic LLM APIs)
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: False (reported)
  - hooks: False (reported)
  - plan_mode: False (reported)

Repository map entry: [yanhua1010/build-your-own-coding-agent](../../repos/yanhua1010/build-your-own-coding-agent.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Educational tutorial series that reverse-engineers three industrial-grade open-source coding agents (pi, codex, grok-build) layer by layer, teaching you to build a working mini-agent from ~100 lines up — using exclusively Chinese domestic LLM APIs, making it accessible to developers in China without needing OpenAI/Anthropic access.

(captured site page body (agents/build-your-own-coding-agent.md), not a verified repo-code finding)
build-your-own-coding-agent is an educational repository that dissects how production coding agents work, publishing condensed architecture notes alongside runnable code for each layer. The series targets Chinese-speaking developers and reverse-engineers three open-source agents — pi, Codex, and grok-build — explaining the agent loop, LLM API contracts, tool-calling mechanics, and context management step by step, with articles distributed through a WeChat public account and X. All exercises run against Chinese domestic providers (DeepSeek, GLM, Kimi), which removes the OpenAI/Anthropic access barrier for developers in China and distinguishes it from Western equivalents of the same tutorial genre. The audience is developers who want to understand agent internals rather than ship a product, and the repository is early-stage and small (33 stars, recent creation). It is classified as educational material rather than a harness because nothing here is a tool others adopt for daily coding.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/build-your-own-coding-agent.md)
