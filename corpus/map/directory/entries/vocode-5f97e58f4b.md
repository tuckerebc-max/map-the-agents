# Vocode (`vocode`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: vocodedev
- License: MIT
- Language: Python
- Interface: install=pip
- Model providers: OpenAI, Anthropic
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: n/a (reported)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry (renamed): original lead [vocodedev/vocode-python](https://github.com/vocodedev/vocode-python) (source: backing, field: `source_code_url`) now resolves to [vocodedev/vocode-core](../../repos/vocodedev/vocode-core.md) (github id 606164768, verified [https://github.com/vocodedev/vocode-core](https://github.com/vocodedev/vocode-core)).

## Description

Highlight (site page `what_makes_it_special`): Open-source library for building voice-based LLM apps (phone calls, Zoom meetings) with real-time streaming conversations, transcription, and synthesis integrations.

(captured site page body (agents/vocode.md), not a verified repo-code finding)
Vocode exists to remove the plumbing from real-time voice LLM applications: managing interruptible streaming audio, transcription, and synthesis across many vendors. It provides a modular Python pipeline where pluggable transcription backends (Deepgram, AssemblyAI, Whisper, Google, Azure) feed an LLM from OpenAI or Anthropic, whose output goes to pluggable speech synthesis from ElevenLabs, Azure, Polly, Cartesia, and others, deployable to phone calls, Zoom meetings, and system audio. A companion React SDK covers browser-side voice interfaces. The repo has been seeking community maintainers, indicating the core team has moved on. It serves developers embedding outbound-call or voice-assistant flows into their own applications.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/vocode.md)
