# LineCodePro (`linecodepro`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: LangLang03
- License: GPL-3.0-or-later
- Language: Java
- Interface: install=Download prebuilt APK from GitHub Releases (sideload) or build with Gradle: ./gradlew :app:assembleDebug
- Model providers: OpenAI-compatible, Anthropic, Codex (OpenAI), Local GGUF (llama.cpp)
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: False (reported)
  - subagents: True (reported)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [langlang03/linecodepro](../../repos/langlang03/linecodepro.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Self-hosted, on-device AI coding workspace/assistant for Android 8.0+. Runs a real tool-call loop where models can read/edit files, run shell commands (via Termux/SSH/IPC), search the web, generate images, and dispatch sub-agents. Supports custom MCP-HTTP tools (mcpx_*), custom agents (agentx_*), and pluggable IPC terminal providers, plus local on-device llama.cpp GGUF inference.

(captured site page body (agents/linecodepro.md), not a verified repo-code finding)
LineCodePro brings a Claude Code-style tool loop to Android, where nearly all coding agents assume a desktop: models read/edit/delete files, run shell commands through Termux, SSH, or a sandboxed IPC terminal-provider app, search the web, and dispatch sub-agents, with every write producing a DiffRecord for inline review. Inference runs against OpenAI-compatible, Anthropic, or Codex protocols, or entirely on-device through llama.cpp GGUF models, so the tool works without any cloud dependency. Custom MCP-HTTP tools and custom agents register through an extensions screen, and a pluggable AIDL terminal-provider interface lets any third-party app supply the shell. Android-toting developers who want their coding agent self-hosted and on-device use the sideloaded APK or build from source.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/linecodepro.md)
