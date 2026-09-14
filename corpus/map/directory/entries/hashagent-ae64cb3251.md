# HashAgent (`hashagent`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: mason131928
- License: MIT
- Language: TypeScript
- Interface: platforms=Web; install=Open https://hashagent.pages.dev/ in a WebGPU-capable browser
- Model providers: local WebGPU models (Llama 3.2 1B, Qwen, Phi-4, SmolLM class, 360M-8B)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [mason131928/hashagent](../../repos/mason131928/hashagent.md) (source: backing, field: `source_code_url`).

Discrepancy between directory sources (not overwritten):

- category: published=, backing=agent, page=other

## Description

Highlight (site page `what_makes_it_special`): A complete AI agent encoded as one URL hash fragment: name, emoji, system prompt, greeting, model, and temperature live in the link, and inference runs locally in the browser via WebGPU, with no account, no tracking, and no inference server. Optional web search and page reading go through an open-source gateway that never sees the conversation.

(captured site page body (agents/hashagent.md), not a verified repo-code finding)
HashAgent compresses an entire agent into a shareable URL. The agent's definition — a name, an emoji, a system prompt, an opening message, a model choice, and a temperature — is serialized into the URL's hash fragment, so opening the link reconstructs the agent with zero server-side state; a QR code is generated when the URL is short enough. Models run entirely in the browser through WebGPU, ranging from a 360M safe-mode default up to 8B-parameter options for capable hardware, with vision-ready variants handling images and camera input. Conversations are ephemeral by default (or kept on-device), and the only online component is an optional open-source gateway for web search and page reading, which can see the query or URL but never the conversation and can be switched off. It is a general browser agent builder rather than a repo-scale coding tool: no file editing, terminal, or workspace tools are exposed.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/hashagent.md)
