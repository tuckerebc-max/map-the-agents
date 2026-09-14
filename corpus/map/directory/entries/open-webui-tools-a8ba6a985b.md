# Open-Webui-Tools (`open-webui-tools`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: Haervwe
- License: MIT
- Language: Python
- Interface: platforms=Web; install=web (Open WebUI Hub or copy py files into Workspace)
- Model providers: Ollama, OpenAI, OpenRouter, MiniMax, Google Gemini/Veo, Hugging Face, Cloudflare Workers AI, Atlas Cloud
- Feature flags (directory-reported):
  - mcp_support: yes (Planner Agent v3 with MCP support, connection deduplication, parallelism patches) (yes)
  - plugin_support: n/a (is itself a collection of Open WebUI tools) (reported)
  - claude_code_plugin: no (no)
  - subagents: yes (Planner Agent v3 specialized subagents: Web Search, Image Gen, Knowledge, Code Interpreter, Terminal) (yes)
  - hooks: no (no)
  - plan_mode: yes (ENABLE_PLAN_APPROVAL pauses for user review before executing) (yes)

Repository map entry: [haervwe/open-webui-tools](../../repos/haervwe/open-webui-tools.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Modular collection of 20+ tools, function pipes, and filters extending Open WebUI into an AI workstation. Standout is Planner Agent v3 — advanced autonomous agent with agentic planning, parallel subagent execution, MCP integration, visual execution tracking, interactive UI modals, and native Open WebUI integration. Covers research, creative generation (music/image/video), and smart routing (Semantic Router with dynamic vision re-routing).

(captured site page body (agents/open-webui-tools.md), not a verified repo-code finding)
Open WebUI ships as a chat front end, and operators who self-host it often want search, media generation, and autonomous behavior without assembling each integration from scratch. This repository packages 20-plus components as Open WebUI's native tools, function pipes, and filters: search utilities (arXiv, Perplexica, SearxNG, SerpBase), image/video/music generation via ComfyUI, Hugging Face, and Google Veo, and utility filters such as a semantic router that picks the model automatically. The centerpiece, Planner Agent v3, is an autonomous pipe with agentic planning, dependency-aware task trees, parallel subagents for web search, image generation, RAG, code interpretation, and terminal work, an optional plan-approval gate, and MCP server support with connection deduplication. Installation is a click from the Open WebUI Community page or manual paste into the Workspace. Self-hosters of Open WebUI who want an AI workstation rather than a chat window are the audience, and most tools need third-party API keys.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/open-webui-tools.md)
