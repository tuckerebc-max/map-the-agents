# juggler (`juggler`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: juggler-ai
- License: AGPL-3.0, Apache-2.0
- Language: Go
- Interface: install=binary
- Model providers: Claude Code, OpenAI, GitHub Copilot, Gemini, Mistral, Z.ai, Ollama, OpenRouter, Deepseek
- Feature flags (directory-reported):
  - mcp_support: yes (yes)
  - plugin_support: yes (yes)
  - claude_code_plugin: no (no)
  - subagents: yes (yes)
  - hooks: no (no)
  - plan_mode: partial (reported)

Repository map entry: [juggler-ai/juggler](../../repos/juggler-ai/juggler.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Visual GUI workbench with Miller-column (Finder-style) navigation; sessions are editable, branching trees (not linear transcripts); persistent and stateful including paused approval states surviving restarts; everything is an inspectable extension/plugin; multi-client architecture (native desktop app + browser tabs sync to same live session); runs locally, remotely, or both

(captured site page body (agents/juggler.md), not a verified repo-code finding)
Juggler treats an agent session as a manipulable data structure rather than a transcript: sessions branch, backtrack, and edit, with pending approval dialogs persisting across restarts. The Go backend (no Electron) serves a native desktop app and browser clients against the same session, so a phone can watch a run started on a laptop. Every layer is inspectable — system prompts, token counts, what past turns actually sent — and tools, slash commands, and loop strategies ship as JavaScript extensions under Apache-2.0 so closed-source extensions remain possible. Its author is the developer behind JUCE and Tracktion, and the project is a one-person side project now spanning worktrees, SSH, and sandboxing on its roadmap.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/juggler.md)
