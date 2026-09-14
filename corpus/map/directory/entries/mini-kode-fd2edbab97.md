# Mini-Kode (`mini-kode`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: minmaxflow
- License: MIT
- Language: TypeScript
- Interface: platforms=CLI; install=npm install -g mini-kode; set MINIKODE_API_KEY/MINIKODE_BASE_URL/MINIKODE_MODEL env vars; run mini-kode
- Model providers: OpenAI-compatible APIs including DeepSeek, GLM (Zhipu), any OpenAI-compatible via custom base URL
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: unknown (unknown)
  - subagents: False (reported)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [minmaxflow/mini-kode](../../repos/minmaxflow/mini-kode.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Educational AI coding agent CLI (~14K lines of production code) purpose-built for learning how modern coding agents work internally - a manageable scale between toy demos and production behemoths. Clean architecture with comprehensive comments, streaming responses, human-in-the-loop permission approval, unified tool system, and a modern React/Ink terminal UI.

(captured site page body (agents/mini-kode.md), not a verified repo-code finding)
Mini-Kode addresses the learning gap between toy agents (a few hundred lines) and production harnesses too large to read: at roughly fourteen thousand lines of TypeScript it is a working agent whose internals can actually be studied. The loop streams from any OpenAI-compatible endpoint (DeepSeek and GLM verified in the README), dispatches a unified tool system for files, search, and command execution behind two-layer permission approval, and reads AGENTS.md at startup for persistent project conventions — mirroring the conventions-file pattern of production agents. Architecture is deliberately legible: separate modules for tools, permissions, LLM, sessions, and UI, written for readers rather than throughput, with a DeepWiki walkthrough accompanying the code. A roadmap of session persistence, subagents, and context caching marks the gaps between it and production harnesses. Developers use it to learn how coding agents are assembled and as a base for their own experiments rather than for daily production work.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/mini-kode.md)
