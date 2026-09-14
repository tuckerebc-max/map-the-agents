# Rowboat (`rowboat`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: rowboatlabs
- License: Apache-2.0
- Language: TypeScript
- Interface: platforms=IDE, Web; install=Desktop installers for macOS/Windows/Linux from rowboatlabs.com/downloads or GitHub releases; optional API keys (Deepgram, ElevenLabs, Exa, Composio) configured in ~/.rowboat/config
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: yes (yes)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: unknown (unknown)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [rowboatlabs/rowboat](../../repos/rowboatlabs/rowboat.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Long-lived memory is the organizing primitive: email, meetings, Slack, and assistant conversations are indexed into an Obsidian-style backlinked graph, and event- or schedule-triggered agents act from that context — including a code mode that drives parallel Claude Code or Codex sessions.

(captured site page body (agents/rowboat.md), not a verified repo-code finding)
Rowboat started as an AI app-builder project and repositioned as a local-first "AI coworker": a desktop app that indexes the user's work into a persistent, backlinked knowledge graph rather than retrieving cold from a vector store on each question. Around that Brain sit working surfaces — an email client that triages and drafts with work context, a meeting note-taker with live transcription, an isolated browser for web tasks, and composable apps — all stored locally as plain Markdown. Background agents fire on events or schedules and can browse, search, and write code, with code mode dispatching parallel sessions to Claude Code or Codex. It is Apache-2.0, runs models locally via Ollama or LM Studio or via hosted API keys, and stores everything as local Markdown. YC S24-backed, it is used by people who want an always-on assistant with memory without shipping their data to a SaaS.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/rowboat.md)
