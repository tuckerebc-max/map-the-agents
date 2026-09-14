# Weaver

> **Lightweight coordination and optional shared context for coding agents.**

[![CI](https://github.com/sean35mm/weaver/actions/workflows/ci.yml/badge.svg)](https://github.com/sean35mm/weaver/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/github/license/sean35mm/weaver)](./LICENSE)

**Docs:** <https://sean35mm.github.io/weaver/> · **For agents:** [`llms.txt`](https://sean35mm.github.io/weaver/llms.txt)

Claude Code, Codex, OpenCode, Pi, and ordinary terminals can work in one repo without naturally
sharing context. Weaver gives them one local commons:

- a token-cheap `status → task → claim → done` coordination loop;
- live sessions, advisory file claims, and recent activity;
- optional, revision-safe Markdown scratchpads for collaborating workstreams; and
- durable **Repository Facts** for verified knowledge that should survive a task.

```console
$ weaver status
3 other active sessions
  claude-code   refactor the auth module       12s ago
  codex         add a Google OAuth provider     just now
⚠ src/auth/** claimed by claude-code — coordinate or work elsewhere

$ weaver scratchpad list  # optional shared workstream context
#7 OAuth rollout  [active] r12 · 2 attached
```

Weaver is a CLI over a local SQLite store. There is no cloud account, remote sync, coordination
daemon, or MCP server. Git remains authoritative for code; the CLI remains authoritative for
coordination. OpenCode gets optional native tools, but those tools invoke the same CLI contract.

## Install

```sh
curl -fsSL https://raw.githubusercontent.com/sean35mm/weaver/main/install.sh | sh
weaver --version
weaver init
```

The self-contained binary supports macOS and Linux on arm64/x64 (use WSL2 on Windows). It installs
to `~/.local/bin/weaver`; users do not need Node, npm, a server, or an account.

`weaver init` installs a versioned, managed agent protocol:

- **Project** (`--project`): this checkout's `CLAUDE.md` and `AGENTS.md`.
- **Global** (`--global`): `~/.claude/CLAUDE.md`, `~/.config/opencode/AGENTS.md`, and
  `~/.codex/AGENTS.md` for every repo read by those harnesses.
- **Harness integrations** (`--hooks`): ownership-safe Claude Code hooks and the OpenCode plugin,
  at the same project/global scope. Interactive init asks; scripts must pass `--hooks` explicitly.

Managed blocks and the plugin carry protocol/template versions. Re-running `init` refreshes stale
Weaver-owned content in place and preserves text outside the managed block. A foreign
`.opencode/plugins/weaver.js` is never overwritten. Restart OpenCode after installing or refreshing
its plugin.

## Coordination-lite workflow

Agents receive this workflow from the managed protocol:

```sh
weaver status

# Only after repository writes are authorized:
weaver task "add OAuth callback validation"
weaver claim 'src/auth/**' --reason "callback and token validation"

weaver fact "OAuth callbacks are validated in AuthService" --path 'src/auth/**'
weaver preflight --staged
weaver done
```

Read-only and plan-only sessions stop after `status` unless it or the user identifies a relevant
existing pad; they may read that pad without attaching or mutating it. For write work, pads are
optional. Use one when sessions are collaborating, a handoff/resumption is planned, a conflict or
shared decision needs a record, the work matches an active pad, or the user asks. Complexity or
duration alone does not require one.

When a pad is useful, attach after `task` and before `claim` (claims snapshot the current
attachment), then keep it curated:

```sh
weaver task "add OAuth callback validation"
weaver scratchpad list
weaver scratchpad read 7 --headings
weaver scratchpad use 7
weaver claim 'src/auth/**' --reason "callback and token validation"
printf '%s\n' 'Use PKCE for every browser flow.' |
  weaver scratchpad edit-section 7 Decisions --from - --revision 12
```

Every mutation creates a revision. Passing `--revision` prevents a stale writer from replacing a
newer edit; on conflict, re-read and merge deliberately. `use` attaches the current session and
worktree, so the rich UI can show that pad's agents, claims, and activity.

Pads move through **active → archived** or **trash**, with restore/recover operations. Archive only
when the whole workstream is complete. Agents may
trash only empty, duplicate, or demonstrably obsolete pads, with a reason and current revision,
and never while another live session is attached. There is no individual permanent-purge command.

Full guide: [Scratchpads](https://sean35mm.github.io/weaver/guides/scratchpads/).

## Rich local UI and terminal access

```sh
weaver scratchpads                     # rich/source Markdown editor; opens automatically
weaver scratchpads --open=browser      # force the normal browser launcher
weaver scratchpads --open=cmux         # prefer an optional cmux browser pane, fall back to browser
weaver scratchpads --no-open           # headless: print the capability URL
weaver scratchpads --port 8080
weaver watch                           # terminal-only live coordination view
```

`dashboard`, `view`, and `ui` are aliases for `scratchpads`. The web app supports WYSIWYG and
Markdown source modes, autosave with revision conflict handling, search, revision history, and pad
lifecycle actions. It shows attached sessions, claims, activity, and Repository Facts alongside
the document. It binds only to loopback and uses an unguessable launch capability; the capability
is removed from browser history after startup.

The first invocation owns one foreground server—and at most one Weaver-managed cmux surface—for
the effective project store and OS user. Later invocations reuse that server; its port wins. Git
worktrees with the same repo identity and `WEAVER_HOME` share it, while another home or user has a
separate instance. `--no-open` only prints the URL, `--open=browser` may open another ordinary tab,
and `auto`/`cmux` ask the owner to focus its managed cmux surface. Browsers do not expose reliable
tab deduplication.

On macOS and Linux Weaver uses the normal system browser launcher (`open`/`xdg-open`). cmux is
optional and auto-detected. For SSH, containers, or other headless use, pass `--no-open`. For an
ordinary terminal editor, use `weaver scratchpad edit <id> --revision <n>` with `$VISUAL` or
`$EDITOR`.

## Repository Facts

Facts are verified, lasting repo knowledge—not task progress:

```sh
weaver fact "AuthService owns token refresh" --path 'src/auth/**' --tag architecture
weaver facts auth --path src/auth/login.ts --json
weaver fact "AuthService moved to src/core/auth" --update 12
weaver forget 17 "the Docker test setup was removed"
weaver forget --undo 17
```

`note` and `notes` remain compatibility aliases for `fact` and `facts`. The SQLite table is still
named `notes`, and upgrades do not rewrite that data. Prefer Fact terminology in new instructions,
automation, and discussion.

## OpenCode tools

`weaver init --hooks` installs a generated ESM plugin using OpenCode's official `tool` hook from
`@opencode-ai/plugin`; the installed file has no dependency on the Weaver npm package. It provides:

```text
weaver_scratchpad_list       weaver_scratchpad_read
weaver_scratchpad_create     weaver_scratchpad_use
weaver_scratchpad_edit_section
weaver_scratchpad_rename     weaver_scratchpad_archive
weaver_scratchpad_restore    weaver_scratchpad_trash
weaver_scratchpad_recover
weaver_facts_list            weaver_fact_record
weaver_fact_forget
```

These tools expose fixed operations, not arbitrary argv. Scratchpad Markdown travels on stdin;
CLI reads use JSON and bounded output; mutations require explicit revisions where concurrency
matters. Tool failures surface clear revision, lifecycle, and conflict errors. The plugin also
injects OpenCode's session id into shell commands, logs edits best-effort, appends advisory conflict
context, and calls `done` when a session is deleted.

## Claims and conflicts

Claims are advisory and TTL-bound. `claim` exit `1` means the claim **was recorded** and an overlap
was found—do not repeat it. Read the other session's intent, claims, activity, and pad; work
elsewhere if possible; proceed only when demonstrably harmless; otherwise ask the user how to
split the work. Known different-worktree overlaps are informational because files are isolated,
but may still collide during integration.

Use one bounded check before delivery:

```sh
weaver preflight --staged       # commit
weaver preflight --upstream     # push
weaver preflight --base main    # PR-sized diff
```

## Command map

```text
Scratchpads:
  scratchpad list|create|read|find|use (optional workstream context)
  scratchpad replace|append|edit-section|rename|edit|history
  scratchpad archive|restore|trash|recover
  scratchpads [--port N] [--no-open] [--open=auto|browser|cmux]

Coordination:
  status, task, claim, release, check, preflight, done
  fact/facts (preferred), note/notes (aliases), forget
  log, activity, watch

Setup and maintenance:
  init [--project|--global] [--hooks|--no-hooks]
  disable, enable, deinit [--project|--global] [--purge]
  config, audit, doctor, upgrade, uninstall
```

See the [exact CLI reference](https://sean35mm.github.io/weaver/reference/commands/).

## Local security and privacy

- Stores live under `~/.weaver/`, one SQLite database per repository identity.
- Scratchpads, Facts, intents, reasons, and summaries are plaintext local authored data. Do not put
  secrets, credentials, personal data, or sensitive customer data in them.
- There is no telemetry. Content-free local command usage events support `weaver audit` and are not
  transmitted.
- The only network operations are install/upgrade downloads from GitHub.
- The scratchpad web server is temporary, authenticated by a launch capability, and loopback-only.
- The capability stays in owner memory, the private control exchange, and launch URLs; it is not
  persisted to SQLite or a lock file.
- `deinit --purge` deletes one repo's store. Uninstall without `--keep-data` cleans the effective
  `WEAVER_HOME`: the default `~/.weaver` may be recursively removed after safety checks, while an
  explicit home loses only validated Weaver DB/sidecar files and keeps unrelated files and the
  directory. `--keep-data` removes only the binary. Unsafe or active/uncertain targets are refused.

## Store schema upgrades

`weaver upgrade` replaces the standalone binary after checksum verification. The first subsequent
store open migrates older stores to the current schema v6 automatically. The v4 → v5 step adds
scratchpad tables and nullable attribution while preserving existing notes/Repository Facts
unchanged; the v5 → v6 step adds scoped dashboard leases.

After upgrading, rerun `weaver init` at the scope you used before (`--project` or `--global`), add
`--hooks` if you installed integrations, and restart OpenCode. cmux is optional; a normal browser,
headless URL, terminal CLI, or `$EDITOR` all work without it.

## Learn more

- [Quickstart](https://sean35mm.github.io/weaver/getting-started/quickstart/)
- [Scratchpads guide](https://sean35mm.github.io/weaver/guides/scratchpads/)
- [Using Weaver from an agent](https://sean35mm.github.io/weaver/guides/using-from-an-agent/)
- [OpenCode plugin](https://sean35mm.github.io/weaver/guides/opencode-plugin/)
- [Conflict model](https://sean35mm.github.io/weaver/concepts/conflicts/)
- [Architecture](https://sean35mm.github.io/weaver/reference/architecture/)
- [Machine-readable docs](https://sean35mm.github.io/weaver/for-llms/)

Contributing: [`CONTRIBUTING.md`](./CONTRIBUTING.md) · Releases: [`RELEASING.md`](./RELEASING.md)

## License

MIT.
