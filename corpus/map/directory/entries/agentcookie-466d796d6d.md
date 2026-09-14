# agentcookie (`agentcookie`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: mvanhorn
- License: MIT
- Language: Go
- Interface: platforms=Desktop, Web; install=binary, go install
- Model providers: none (cookie/session sync utility; no LLM integration)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [mvanhorn/agentcookie](../../repos/mvanhorn/agentcookie.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Cookie session sync tool for AI agents — continuously syncs Mac's Chrome cookie sessions to a Linux box (or second Mac) where agents run, over Tailscale, so agents wake up already authenticated. Handles the hard parts: macOS Keychain decryption, Chrome App-Bound Encryption on source, live CDP injection into Chrome's in-memory store on Linux sink. Pairing-derived per-peer keys, AES-256-GCM, per-CLI secrets ...

(captured site page body (agents/agentcookie.md), not a verified repo-code finding)
Coding agents that drive a browser hit a login wall the moment they run on a machine where the human never signed in, and headless re-authentication defeats bot defenses. agentcookie keeps a Linux box's Chrome cookie store in sync with a Mac's continuously over Tailscale, decrypting the macOS Keychain on the source and injecting cookies live over the Chrome DevTools Protocol into the sink's in-memory session, so Puppeteer, Playwright, or browserUse automations wake up already authenticated. Transport is end-to-end encrypted (AES-256-GCM with pairing-derived per-peer keys), and a secrets bus carries bearer tokens and API keys to CLIs separately. Developers running browser-driving agents on remote machines are the users; DBSC-bound sessions like Google deliberately do not sync.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/agentcookie.md)
