# tartarusai-cli (`tartarusai-cli`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: Tartarus-AI
- License: MIT
- Language: unknown
- Interface: platforms=CLI; install=curl -sSf https://dash.tartarusai.dev/tartarus-setup.sh | bash (macOS/Linux); PowerShell zip download (Windows); or binaries from GitHub Releases
- Model providers: TartarusAI (proprietary uncensored model)
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: n/a (reported)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [tartarus-ai/tartarusai-cli](../../repos/tartarus-ai/tartarusai-cli.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Uncensored-no policy filter between you and your code. Does work mainstream agents refuse (pentest PoCs for patched CVEs, deobfuscation, credential rotation tools). 256K context, crypto-only billing, no card on file, ~30s activation. Explicitly not a malware factory, piracy tool, or politics bot. Binary distribution only (no source in repo).

(captured site page body (agents/tartarusai-cli.md), not a verified repo-code finding)
tartarusai-cli is the terminal client for a hosted coding-agent service that competes on policy: it advertises itself as an uncensored agent that will handle work mainstream tools decline, such as writing proof-of-concept exploits for already-patched CVEs, deobfuscating samples, and building credential-rotation tooling in lab environments. The client is a MIT-licensed OpenCode fork shipped as a static binary with a setup script for macOS/Linux and a Windows zip; it connects only to TartarusAI's own hosted backend using an account API token, with no BYOK support, and billing is cryptocurrency-only with a 14-day refund window. The project states explicit boundaries — no malware development, no DRM circumvention, no attacking systems you do not own — and runs 256K-context sessions over whole repositories. Security researchers and CTF players who keep hitting refusal walls elsewhere are the intended users.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/tartarusai-cli.md)
