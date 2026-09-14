# coding_agent_account_manager (`coding-agent-account-manager`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: Dicklesworthstone
- License: MIT
- Language: Go
- Interface: platforms=CLI; install=Homebrew (brew install dicklesworthstone/tap/caam), Scoop, curl install script, Go install, or build from source
- Model providers: Claude Code (Claude Max), Codex CLI (GPT Pro), Gemini CLI (Gemini Ultra, legacy), Antigravity CLI, Grok Build (xAI); fixed-cost subscriptions only, not API keys
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: False (reported)
  - hooks: False (reported)
  - plan_mode: False (reported)

Repository map entry: [dicklesworthstone/coding_agent_account_manager](../../repos/dicklesworthstone/coding_agent_account_manager.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Sub-100ms OAuth token file swapping to instantly switch between fixed-cost subscription accounts (Claude Max, GPT Pro, Gemini Ultra) when hitting rate limits without browser re-auth. Features smart rotation algorithms, cooldown tracking, isolated/shallow profiles for parallel sessions, and automatic failover via \`caam run\`.

(captured site page body (agents/coding-agent-account-manager.md), not a verified repo-code finding)
Subscription coding agents stop at usage ceilings, and the official recovery path is a slow browser re-authentication that breaks flow and parallel workflows. caam treats stored OAuth credential files as swappable state: it backs up each CLI's auth files (Claude Code, Codex, Gemini CLI, Antigravity, Grok Build) into a local vault and restores a different account's files on demand in under 100 milliseconds, with no browser round trip. A rotation engine tracks cooldowns and health per account, \`caam run\` wraps the underlying CLI and fails over automatically on rate limits, and isolated profiles let parallel sessions run against separate accounts. The Go CLI works offline with no daemons, exposes JSON output for use by other agents, and manages fixed-cost subscriptions rather than metered API keys. Individual developers and orchestrator operators running many parallel agent sessions are its users.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/coding-agent-account-manager.md)
