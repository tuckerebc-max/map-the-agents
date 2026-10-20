# CLI Commands

The unified `@cortexkit/aft` CLI works across every supported harness:

| Command | What it does |
|---|---|
| `npx @cortexkit/aft@latest setup` | Interactive first-time setup — auto-detects installed harnesses and registers AFT with each |
| `npx @cortexkit/aft@latest doctor` | Read-only health check across all detected harnesses (host install, plugin registration, binary cache, ONNX, config) |
| `npx @cortexkit/aft@latest doctor --fix` | Auto-fix what doctor can: register missing plugin entries, download a missing `aft` binary, repair ONNX Runtime |
| `npx @cortexkit/aft@latest doctor lsp <file>` | Show exactly which LSP servers AFT would spawn for a file, where each binary resolves, and why a server failed to start |
| `npx @cortexkit/aft@latest doctor --clear` | Interactive cache cleanup — pick which caches to clear (plugin packages, binary, LSP, semantic) |
| `npx @cortexkit/aft@latest doctor --issue` | Collect diagnostics and open a GitHub issue with sanitized logs |
| `npx @cortexkit/aft@latest backups purge --path <p> [--session <id>] [--yes]` | Remove undo backups early for a file or directory, a session, or both (dry run unless `--yes`) |

Add `--harness opencode` or `--harness pi` to any command to target one harness explicitly.

---

**`setup`** — Registers AFT with each installed harness (edits the harness config to enable
the AFT plugin). When multiple harnesses are detected, prompts you to pick which ones to
configure. It then shows a checklist of features (search and navigation tools, editing tools,
the `bash` tool and its settings, the three indexes, GitHub read and write) and saves your
choices to `~/.config/cortexkit/aft.jsonc`, keeping its comments and other keys. Rerun it, or
run `doctor --reconfigure`, to change them. For scripts, three modes skip the prompts:

- `aft setup --plan` prints every feature with its default, your value and its current state
  (`off`, `building`, `ready`, `unavailable`) as JSON.
- `aft setup --answers <file|->` applies `{"plan_version":1,"selections":{"<feature-id>":true}}`;
  features you leave out keep their setting.
- `aft setup --yes` saves the defaults for settings your file does not have yet.

All three accept `--harness opencode|pi|omp`.

### OpenCode 2 host tools

After the feature choices, `setup` offers to disable OpenCode 2's own `shell`
and `patch` tool plugins so agents use AFT's `bash` and `apply_patch`. It adds
`-opencode.tool.shell` and `-opencode.tool.patch` under `plugins` in
`opencode.json(c)`. Removing the plugins removes their tool-name-specific hooks
as well as their tools; AFT keeps its own tool names.

Each default follows its AFT replacement: when `bash` or `apply_patch` is in
`disabled_tools`, setup defaults to keeping the corresponding host tool. The
shell default also respects `bash: false`, `bash.enabled: false`, and AFT being
disabled as a whole. `--yes` and non-terminal runs apply these defaults without
asking. Answering no restores a previously removed host plugin.

`doctor` reports each host tool separately. `doctor --fix` adds a missing removal
entry only while AFT's replacement is enabled; it never restores a host plugin
automatically. Rerun setup to restore one. OpenCode 1 is not changed.

With the host patch plugin disabled, AFT supplies the same model-specific
editing surface: model IDs containing `gpt-`, but not `gpt-4` or `oss`, get
`apply_patch` rather than AFT's `edit` and `write`. Other models get AFT's `edit`
and `write` rather than `apply_patch`. The gate only removes tools AFT registered,
so disabling AFT's `edit` leaves the host's edit tool alone. AFT's `apply_patch`
uses the OpenCode 2 `edit` permission action, so existing edit rules cover it.

**`doctor`** — Read-only health check. Reports host install state, plugin registration,
plugin cache version, binary cache, config parse errors, ONNX Runtime availability (for
semantic search), storage directory sizes, and log file status. Exits non-zero when
something needs attention so it can be wired into CI scripts. Pure inspection — nothing
is modified.

**`doctor --fix`** — Applies the fixes doctor would otherwise just report. Registers
missing plugin entries in your harness config, pins the OpenCode plugin entry to this CLI's
exact version (for example `@cortexkit/aft-opencode@0.58.0`, never `@latest`) and updates a
plugin older than the CLI, downloads the matching `aft` binary if
`~/.cache/aft/bin` is empty (run this after `--clear` or after wiping the cache to recover
without opening a session), and repairs ONNX Runtime version mismatches by clearing AFT's
managed ONNX cache so the next bridge launch redownloads. Each step asks confirmation
before mutating state.

**`doctor lsp <file>`** — Per-file LSP triage. Shows which servers AFT registered for the
file's extension, where each binary resolves (Python workspace virtualenv, project
`node_modules/.bin`, `lsp_paths_extra`, `PATH`, or not found), whether the workspace root marker
resolves walking up from the file, the spawn outcome, and the diagnostics returned (if any). Use
this when `lsp_diagnostics` returns `total: 0` and you can't tell whether the file is genuinely
clean or no server ever spawned. Pass `--harness opencode` or `--harness pi` if you have both
plugins installed and need to disambiguate. Example output:

```
$ npx @cortexkit/aft@latest doctor lsp ./python/main.py

Server attempts:
  ✗ ty
    Binary: ty (NOT FOUND in workspace virtualenv, node_modules/.bin, lsp_paths_extra, or PATH)
    Workspace root: /repo/python (markers: requirements.txt)
    Status: binary not installed
    Action: Install with `uv tool install ty` or `pip install ty`.
```

**`doctor --clear`** — Walks you through interactive cache cleanup. Useful when you're on
an old version and updating doesn't seem to take effect (some harness installers cache npm
packages aggressively), or when you want to reset the LSP server cache to force a fresh
download. Targets harness plugin cache, binary cache, downloaded LSP servers, and semantic
index storage.

**`doctor --issue`** — Collects a full diagnostic report and sanitizes secrets, your username,
and home path out of the logs. It always writes the report to `./aft-issue-<timestamp>.md`
first and prompts you to review it. Only after you confirm does it submit via `gh` (when
installed); otherwise it opens the prefilled new-issue page in your browser. Nothing is sent
without your explicit confirmation.

**`backups purge`** — Removes undo backups before they would expire on their own. Backups
normally go away only when a file's undo history passes 20 entries or when a session has been
idle for 72 hours, so a long-running session keeps every backup it made, including the copies
taken by a large delete. The native binary runs the same command as `aft backups purge`.

```
aft backups purge [--path <file-or-dir>] [--session <id>] [--harness <name>] [--yes] [--json]
```

- `--path` selects every backup recorded for that file, or for anything under that directory,
  in every session and harness. Paths are resolved the way AFT records them (absolute,
  symlinks in parent directories resolved) and compared by whole path components, so
  `--path /a/b` never matches `/a/bc`.
- `--session` selects every backup of one session. With `--path` too, only that session's
  backups under the path are selected.
- `--harness` narrows to one harness storage namespace (`opencode`, `pi`, `runner`, or an
  `mcp--…`/`fed--…` directory name). The default is all of them.
- At least one of `--path` or `--session` is required.
- Without `--yes` the command is a dry run: it prints what it examined and what it would
  remove (backup stacks, entries, files, bytes, database rows, the sessions affected, and a
  few sample paths) and removes nothing. With `--yes` it also prints what it removed.
- `--json` prints the same report as JSON.

The command exits non-zero when any selected backup could not be fully removed and lists
each one, saying whether undo can still see it or only leftover files remain.

When an AFT daemon is running it holds backup history in memory, so the command sends the
purge to the daemon, which clears its memory, the backup files and the database rows
together. With no daemon the command performs the purge itself using the same locks. If a
daemon is running but the purge through it fails, the command stops rather than purging
behind its back. Afterwards, undo for a purged file reports that there is no undo history.

```
$ aft backups purge --path ~/projects/engram/keystore
aft backups purge: dry run, nothing removed (rerun with --yes to remove)
ran by: daemon
storage: /Users/me/.local/share/cortexkit/aft
filter: path=/Users/me/projects/engram/keystore session=any harness=any
examined: 2 namespace(s) [opencode, pi], 9 session dir(s), 12410 disk stack(s), 12410 database stack(s), 12130 cached stack(s), 0 skipped
matched: 12124 stack(s), 12124 entries, 24248 file(s), 3214567890 byte(s), 12124 database row(s), 1 session(s) [ses_abc]
sample paths:
  /Users/me/projects/engram/keystore/a.key
```
