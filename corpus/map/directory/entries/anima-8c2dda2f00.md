# Anima (`anima`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: Fullive-AI
- License: Apache-2.0
- Language: Python, TypeScript
- Interface: install=docker
- Model providers: OpenAI-compatible (OpenAI, DeepSeek, Doubao, Anthropic via proxy, local Ollama)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: yes (yes)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: yes (yes)

Repository map entry: [fullive-ai/anima](../../repos/fullive-ai/anima.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Open-source Agent OS for hardware intelligence that discovers smart home devices, maintains device state, and uses an LLM Brain to plan context-aware actions within safety boundaries. Zero-config auto device discovery (Xiaomi QR login), evidence-based layered long-term memory that learns user preferences, domain-specific Skill knowledge packages per device type, and local-first runtime. Currently supports Xiaomi/Mi Home (MIoT) devices.

(captured site page body (agents/anima.md), not a verified repo-code finding)
Anima (Latin for soul) gives smart homes an LLM brain that discovers devices on the local network, maintains their state, and plans actions within explicit skill boundaries and safety rules — conservative by default for high-risk devices like locks. A LangGraph planner merges environment state, device state, long-term memory (candidate facts promoted to confirmed), and skill packages into action plans executed through protocol adapters, currently Xiaomi MIoT with QR-login token handling. Any OpenAI-compatible provider works (OpenAI, DeepSeek, Doubao, Ollama), and a React dashboard plus REST API expose the loop. Apache-2.0, Docker-first deployment, only six commits since its June 2026 debut but 1.1k stars, with Matter/Home Assistant adapters and multi-user permissions on the roadmap.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/anima.md)
