# PUNK (`punk`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: multiplexer
- Provider/maker: PUNK
- License: unknown
- Language: JavaScript (Node.js CLI), React Native/Expo (app)
- Interface: install=App: TestFlight invite; CLI: npm i -g @punkcode/cli, then punk connect and scan QR code from phone app
- Model providers: Claude/Anthropic (wraps Claude Code)
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: False (reported)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: True (reported)

No repository record: repository source unavailable in this directory capture, not an absence of capability.

## Description

Highlight (site page `what_makes_it_special`): iPhone app acting as remote control for Claude Code running on your laptop - phone is terminal, laptop is mainframe. Decouples execution from control: agents run locally but you direct them from your phone anywhere. Lock-screen approval, AI voice input (4x faster than typing), multiple parallel sessions, multiple connected devices, outbound-only TLS relay (no open ports, no data stored). Skills, ...

(captured site page body (agents/punk.md), not a verified repo-code finding)
PUNK separates where an agent runs from where a human directs it: Claude Code sessions execute on your laptop while your iPhone becomes the control terminal, letting you approve permission requests from the lock screen, read streaming output, and switch between parallel sessions from anywhere. The CLI connects outbound over TLS with no open ports, and a relay with no persistent database means conversation data passes through and disappears rather than sitting on a server. Skills, MCP servers, and slash commands remain manageable from the phone, and execution modes — Plan, Ask, Auto, Dangerous — map to how much autonomy you grant remotely. The CLI keeps the Mac awake and connected, so long agent runs continue in a backpack with the lid closed. It is built for developers who run Claude Code locally but want to supervise it away from the desk.
Sources: [published index (sha256:5b67dbf818cd)](https://alltheagents.org/agents.json); [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/punk.md)
