# Telemetry: surface detection, the local usage ledger, and shipping

## Surface tokens (#50)

Per invocation, `ade_cli/surface.py` classifies the surface hosting the
CLI from the environment and tty state — a pure function, total over its
inputs: unknown environments map to coarse buckets, never an error, and
detection never blocks a command.

Two independent dimensions, both reported when both apply (Claude Code
launched from iTerm is `host/claude-code term/iterm`):

### `host/<token>` — agent host (omitted outside any agent)

| Token | Detected via |
| --- | --- |
| `claude-code` | `CLAUDECODE`, `CLAUDE_CODE_ENTRYPOINT` |
| `codex` | `CODEX_SANDBOX`, `CODEX_THREAD_ID` |
| `gemini-cli` | `GEMINI_CLI` |
| `cursor` | `CURSOR_AGENT`, `CURSOR_TRACE_ID` |

### `term/<token>` — terminal (always present)

| Token | Detected via |
| --- | --- |
| `ci` | `CI` and per-system flags (`GITHUB_ACTIONS`, `GITLAB_CI`, `CIRCLECI`, `BUILDKITE`, `JENKINS_URL`, `TEAMCITY_VERSION`) |
| `tmux` | `TMUX` (masks the outer terminal), `TERM_PROGRAM=tmux` |
| `iterm` | `TERM_PROGRAM=iTerm.app`, `ITERM_SESSION_ID` |
| `apple-terminal` | `TERM_PROGRAM=Apple_Terminal` |
| `vscode` | `TERM_PROGRAM=vscode` |
| `warp` | `TERM_PROGRAM=WarpTerminal` |
| `wezterm` | `TERM_PROGRAM=WezTerm`, `WEZTERM_EXECUTABLE` |
| `ghostty` | `TERM_PROGRAM=ghostty`, `GHOSTTY_RESOURCES_DIR` |
| `hyper` | `TERM_PROGRAM=Hyper` |
| `kitty` | `KITTY_WINDOW_ID` |
| `alacritty` | `ALACRITTY_WINDOW_ID` |
| `windows-terminal` | `WT_SESSION` |
| `konsole` | `KONSOLE_VERSION` |
| `gnome-terminal` | `GNOME_TERMINAL_SCREEN` |
| `vte` | `VTE_VERSION` (VTE-based terminals not otherwise named) |
| `terminal` | coarse bucket: a tty, but no marker matched |
| `non-tty` | coarse bucket: no tty — piped, scripted, headless |

Precedence within the terminal dimension: `ci` > `tmux` > `TERM_PROGRAM`
values > marker variables > coarse buckets. Only values in the tables
become tokens — arbitrary environment text never rides into telemetry.
The marker set drifts as agent hosts evolve; extend the tables in
`surface.py` and this vocabulary together.

### Where the tokens go

- Appended to the identity `User-Agent` as additional `key/value` tokens
  after the command token (e.g. `… command/parse host/claude-code
  term/iterm`) — see `docs/user-agent.md` for the full header format.
- Recorded on every usage-ledger event (#52) as the `host` and `term`
  fields.

## Usage ledger (#52)

Every command run — including store-served commands that never touch the
API — appends one event to a local ledger. Inspectable offline; shipping
to the platform is #53, below.

- **Location**: `<ADE_HOME>/telemetry.jsonl` (default
  `~/.ade/telemetry.jsonl`), one JSON object per line, keys sorted.
- **Hook**: the root command group's `main` (`ade_cli/telemetry.py`) —
  the single entry point of every invocation, so success, failure, and
  usage error all record exactly one event with no per-command wiring.

### Event shape

```json
{
  "command": "auth login",
  "duration_ms": 42,
  "env": "production",
  "exit_code": 0,
  "flags": ["--env", "--json"],
  "host": "claude-code",
  "idempotent_key": "0f1e2d3c4b5a69788766554433221100",
  "outcome": "success",
  "term": "iterm",
  "ts": 1784774107.53,
  "version": "0.1.2"
}
```

| Field | Meaning |
| --- | --- |
| `command` | Space-joined command path (`parse`, `auth login`); `(root)` for a bare/flag-only invocation, `(unknown)` when nothing resolves — the typed text is never recorded |
| `flags` | Flag *names* used, first-seen order — never flag values, arguments, paths, URLs, schema or document contents, or key material |
| `outcome` | `success` (0), `failure` (1), `usage-error` (2), `pending` (3), `rate-limited` (4) per output.py's exit vocabulary; unknown codes read as `failure` |
| `exit_code` | The raw exit code behind `outcome` |
| `duration_ms` | Whole-invocation wall time, integer milliseconds |
| `host` / `term` | Surface tokens from the tables above (`host` is `null` outside any agent) |
| `env` | The API target this invocation actually addresses — it can change between commands, so every event records it. An `ADE_ENDPOINT` override wins and is recorded by where the traffic goes: a known environment's URL maps back to its name, anything else records `custom` (the URL itself is a value and never recorded). Without an override: the resolved environment name (`--env` flag → `ADE_ENV` → `production`); a name outside the known set records `unknown`, never the typed text. Deliberately not the same notion as `meta.json`'s `environment` (the credential/item-id namespace, which `ADE_ENDPOINT` does not change) — the ledger segments by actual target |
| `version` | Installed ade-cli version |
| `ts` | Unix epoch seconds at record time |
| `idempotent_key` | Minted once at record time (a random 32-hex token): the platform-side dedup handle for at-least-once shipping. Rows written before #53 have none; shipping derives a deterministic content hash instead |
| `shipped` | `true` once the platform acknowledged the row (absent until then) — local bookkeeping, never uploaded |

Names never values, structurally: the command path and flag names come
from classifying raw argv against the registered command tree — a token
is recorded only when it matches a registered command name or a
*declared* option name of a command on that path (name part only;
`=value` dropped). Everything else — arguments, values shaped like
flags, typo'd flags — is skipped.

### Never in the way

Appends are a single `O_APPEND` write (atomic at this size) under the
ledger lock (`<ADE_HOME>/.telemetry.lock`, shared with shipping's
rewrites and never held across the network), every telemetry failure is
swallowed, and an unwritable or corrupt ledger never changes a command's
behavior, output, or exit code.

## Shipping to the platform (#53)

After a command's own event is appended, the whole unshipped backlog
ships to the platform's `POST /v2/telemetry` (`ade_cli/shipping.py`) —
the 40th invocation carries events 31–40. The flush runs after the
command's output and exit code are already decided, and is as silent as
the ledger itself: offline, failed, or unauthenticated uploads leave the
rows buffered for a later run and change nothing observable.

- **Partitioned by environment.** Each event ships to the environment it
  targeted (its `env` field), authenticated with *that* environment's
  stored credential — ADE keys verifiably do not cross environments. The
  `ADE_API_KEY` override applies only to the invocation's own credential
  namespace. A partition without a usable credential stays buffered;
  `custom` ships only while an `ADE_ENDPOINT` override addresses it, and
  `unknown` never ships. A stored OAuth token is used as-is: a flush
  never refreshes and never prompts.
- **Wire shape.** One flush is one POST per environment: a JSON array of
  at most 500 records, each `{idempotent_key, ts, properties}` — `ts`
  the *original* record time in epoch seconds, `properties` the event
  fields above (never the `shipped` mark). The request carries the
  standard identity User-Agent and `X-Source: cli`, with a short
  timeout (5 s) instead of the API commands' generous one; a
  transport-level failure abandons the remaining partitions so an
  offline machine pays one failed connect.
- **At-least-once, deduplicable.** The gateway returns 200 only after
  every record in the batch is logged; acknowledged rows are then marked
  `shipped` and never re-send. A lost 200 re-uploads under the same
  `idempotent_key`, so the rare duplicate is filterable server-side.
- **Bounded either way.** Rotation rewrites the ledger oldest-first past
  a size cap (256 KiB) or an age cap (30 days) — shipped or not, upload
  succeeding or never — so the file stays bounded offline-forever and
  under upload opt-out alike. Marking and rotation happen under the
  ledger lock the appender shares, so a rewrite can never lose a racing
  append; corrupt lines are preserved as-is (only the size cap takes
  them) and never uploaded.

One other caller uses this route: `ade auth login` verifies a candidate
API key with an *empty* batch to the same `POST /v2/telemetry`
(ADR-0007) — the one authenticated route that is free and
side-effect-free. That probe carries no telemetry data (`[]` records
nothing), declares itself with a `probe/auth` User-Agent token
(`docs/user-agent.md`) so request logs can tell it from a real upload,
and ignores the opt-outs below: it is an auth check, not a ledger
upload.

### Opt-out

`ADE_TELEMETRY=0` or the [`DO_NOT_TRACK`](https://consoledonottrack.com)
convention (set to anything but empty or `0`) disables the ledger — and
with it the upload — entirely: no file is written, no request is made.
`ADE_TELEMETRY_UPLOAD=0` disables the upload alone; the ledger keeps
recording locally and rotation keeps it bounded. The identity User-Agent
itself (#48) stays always-on, standard CLI practice.
