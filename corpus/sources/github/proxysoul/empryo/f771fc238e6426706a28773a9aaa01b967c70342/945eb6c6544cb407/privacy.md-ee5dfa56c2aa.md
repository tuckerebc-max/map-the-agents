# Privacy

SoulForge is a **local-first** AI coding tool. This document describes exactly what data flows where, so you can verify the privacy model directly against the source.

## TL;DR

- SoulForge runs entirely on your machine.
- There is no SoulForge backend. No telemetry. No analytics. No usage tracking.
- Code from your project is sent **only** to the LLM providers you choose to enable.
- API keys live in `~/.soulforge/secrets.json` (file mode `0600`) or your OS keychain.
- Sessions, repo map, and memory are SQLite databases under `~/.soulforge/` and `<project>/.soulforge/`.

## What gets sent over the network

Three categories, all on actions you initiate:

### 1. LLM provider API calls

Every chat turn, tool call result, and dispatched subagent talks to the LLM provider you've selected. The request payload contains:

- The system prompt (varies by mode — see [`src/core/prompts/`](src/core/prompts/))
- The conversation history for the current session
- The current Soul Map / repo map injection (file list, exported symbol names)
- File contents you asked the agent to read
- Tool definitions and tool call results

This is the **same as every other AI coding tool**. Cursor, Claude Code, Aider, Continue all do this. The provider you pick (Anthropic, OpenAI, Google, etc.) is the destination.

You can verify the exact payload at runtime — set `BUN_DEBUG=1` and look at the network requests, or read [`src/core/agents/forge.ts`](src/core/agents/forge.ts) and the provider adapters in [`src/core/llm/providers/`](src/core/llm/providers/).

### 2. Web search (opt-in, with approval prompt)

When the agent decides to search the web (`web_search` tool), SoulForge prompts you for approval before each search. The search query goes to the configured search backend (Brave, DuckDuckGo, or Tavily) — never to SoulForge servers (there are none).

Disable: set `webSearch: false` in `~/.soulforge/config.json` or run with `--no-web-search`.

### 3. Page fetches (opt-in, with approval prompt)

When the agent decides to fetch a URL (`fetch_page` tool), it prompts you. The fetch goes to the URL you approve, optionally through Jina Reader for HTML cleanup.

## What does NOT leave your machine

- Your file system contents, except files the agent explicitly reads and includes in an LLM request you initiated.
- Repo map, memory database, sessions — all in SQLite under `~/.soulforge/`.
- API keys — stored locally in `~/.soulforge/secrets.json` (mode `0600`) or in your OS keychain when available.
- Bug reports, error traces, performance metrics — none of this is collected. SoulForge has no telemetry.
- Your usage patterns — when you type, what you ask, which models you use. Nobody is watching.

## What's in `~/.soulforge/`

```
~/.soulforge/
├── secrets.json          # API keys, mode 0600 (you only)
├── config.json           # global config
├── memory.db             # global persistent memory (SQLite)
├── sessions/             # session JSONL files (per project)
├── lsp-servers/          # auto-installed LSP servers
└── installs/             # auto-installed tooling (nvim, etc.)
```

Per-project data lives in `<your-project>/.soulforge/`:

```
<project>/.soulforge/
├── config.json           # project-specific config
├── memory.db             # project-scoped memory
└── repomap.db            # SQLite repo map (FTS5, PageRank scores)
```

## Sensitive file blocking

By default, SoulForge refuses to read files matching these patterns (the agent gets an empty result, even if it asks):

- `.env`, `.env.*`
- `*.pem`, `*.key`, `id_rsa*`, `id_dsa*`, `id_ecdsa*`, `id_ed25519*`
- `credentials`, `credentials.json`
- `.npmrc`, `.netrc`, `.pgpass`
- Anything matching the user's `/privacy add` patterns

The list is in [`src/core/security/forbidden.ts`](src/core/security/forbidden.ts). Add your own patterns with `/privacy add <glob>` in the TUI or via the `forbidden` field in `~/.soulforge/config.json`.

## Hearth (remote control)

The optional Hearth daemon exposes SoulForge to a paired Telegram or Discord bot you set up on your own account. When enabled:

- Messages you send from your phone go through Telegram's / Discord's servers (their privacy policies apply).
- The Hearth daemon runs locally on your machine.
- Your code never leaves your host.

Disable: don't pair Hearth, or run `/hearth unpair`.

## License-key validation (future)

The codebase has scaffolding for a future "Pro" tier with license-key validation. **Today, no license check happens.** When/if a Pro tier ships:

- Validation will be a single HTTP call to a license server on startup.
- The check will not transmit any project content — only the license key.
- The Pro features will run locally; no cloud execution.

## Verifying the privacy story

You don't have to take this document's word for it. SoulForge is open source. Audit paths:

1. Read [`src/core/llm/`](src/core/llm/) for every outbound network call.
2. Read [`src/core/agents/forge.ts`](src/core/agents/forge.ts) for what gets sent to LLMs.
3. Read [`src/core/security/forbidden.ts`](src/core/security/forbidden.ts) for sensitive-file blocking.
4. Run with `BUN_DEBUG=1` to see every HTTP request live.
5. Use any local network monitor (Little Snitch, Wireshark) to confirm.

If you find an unintended data flow, please report via [SECURITY.md](SECURITY.md).

## Data deletion

Everything SoulForge stores is in `~/.soulforge/` and `<project>/.soulforge/`. Delete those directories and SoulForge has nothing on you.
