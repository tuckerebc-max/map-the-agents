# EchoCoding (`echocoding`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: launsion-boop
- License: MIT
- Language: TypeScript/JavaScript (Node.js 18+)
- Interface: platforms=CLI, Web; install=npm i -g echocoding && echocoding install --auto --start && echocoding doctor
- Model providers: TTS: Volcengine cloud (21 voices), Kokoro 82M local (103 voices), macOS say/Linux espeak (fallback). ASR: Volcengine V3 BigModel (cloud), Paraformer (local), browser MediaRecorder (Studio)
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: True (reported)
  - subagents: True (reported)
  - hooks: True (reported)
  - plan_mode: False (reported)

Repository map entry: [launsion-boop/echocoding](../../repos/launsion-boop/echocoding.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Adds an immersive audio layer to AI coding agents — 23 sound effects, ambient soundscapes, TTS speech, and ASR voice Q&A. 'Pipes, not brains' philosophy: the AI agent decides when and what to say; EchoCoding just provides the audio infrastructure (say / ask / sfx). Three audio layers: discrete SFX, continuous ambient soundscapes, and voice interaction. MCP Server (stdio) with ...

(captured site page body (agents/echocoding.md), not a verified repo-code finding)
Long agent sessions are easy to ignore: you switch windows and only find out a task finished — or failed — when you look back. EchoCoding gives the session an audio channel without touching the agent's logic: hooks fire sound effects for tool actions, an ambient layer signals editing/reading/thinking state, and TTS speaks at milestones while ASR listens for spoken replies through a floating HUD. The agent decides what to say; EchoCoding only handles the pipes, which is why it installs with one line and no API keys of its own. Developers who run hands-off sessions — or prefer audio over window-switching — are the intended users.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/echocoding.md)
