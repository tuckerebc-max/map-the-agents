# ade-cli User-Agent format

Every HTTP request ade-cli makes to the ADE API (parse and extract, submit
and poll alike) carries a structured `User-Agent` header so the platform can
distinguish CLI traffic from raw API calls and SDKs.

## Format

```
ade-cli/<version> (<os> <arch>) python/<major.minor> httpx/<version> command/<name> [host/<agent>] term/<terminal>
```

Example:

```
ade-cli/0.1.2 (Darwin arm64) python/3.12 httpx/0.28.1 command/parse host/claude-code term/iterm
```

## Tokens

| Token | Value | Source |
| --- | --- | --- |
| `ade-cli/<version>` | Installed CLI version — the same version number `ade version` reports, or `unknown` when the frozen app carries no metadata record | `importlib.metadata.version("ade-cli")` |
| `(<os> <arch>)` | Platform comment: OS name and machine architecture | `platform.system()`, `platform.machine()` — e.g. `Darwin arm64`, `Linux x86_64`, `Windows AMD64` |
| `python/<major.minor>` | Python runtime, major.minor only | `sys.version_info` |
| `httpx/<version>` | Installed HTTP client library version | `httpx.__version__` — the module attribute, not `importlib.metadata`: frozen builds bundle no dependency dist-info (issue #97) |
| `command/<name>` | The CLI command the user invoked — `parse` or `extract` today. Names the *invoking* command: the standalone parse job that `extract -d` runs first still says `command/extract` | Required `command` field on the gateway (`src/ade_cli/gateway.py`) |
| `probe/auth` | Present only on the login credential check (ADR-0007): the empty-batch `POST /v2/telemetry` that `ade auth login` sends to verify a key before storing it. Distinguishes these requests from real ledger uploads in request logs | `gateway.verify_credential` (`src/ade_cli/gateway.py`) |
| `host/<agent>` | The agent host running the CLI (`claude-code`, `codex`, `gemini-cli`, `cursor`) — omitted outside any agent | Surface detection (`src/ade_cli/surface.py`); vocabulary in `docs/telemetry.md` |
| `term/<terminal>` | The terminal hosting the CLI (`iterm`, `vscode`, `tmux`, `ci`, …), with coarse buckets `terminal` (unknown tty) and `non-tty` (piped/scripted) | Surface detection (`src/ade_cli/surface.py`); vocabulary in `docs/telemetry.md` |

## Parsing rules for the platform side

- Match CLI traffic on the leading `ade-cli/` product token; take the version
  from the same token.
- Tokens are space-separated; the parenthesized platform comment always sits
  second and is the only token containing a space.
- Per-command usage of API-bound commands is queryable from the `command/`
  token alone — group request-log rows by its value.
- The string is **append-only extensible**: future ade-cli versions add
  further `key/value` tokens at the end (planned: a host-app token).
  Parsers must ignore tokens they do not recognize and must not assume
  any particular token is last.

## Companion header: `X-Source: cli`

Alongside the User-Agent, every request carries `X-Source: cli` (#49). The
platform relays `X-Source` verbatim into the `source` column of the recorded
`inference_history` row, so CLI rows are separable from raw-API ones without
parsing the User-Agent. The UA remains the carrier for the fine-grained
dimensions (version, os, host app, terminal, command).

## Where it is built

One place: `src/ade_cli/useragent.py` (`user_agent()`), attached to every
request by the gateway (`src/ade_cli/gateway.py`). Extensions pass extra
`(key, value)` pairs to `user_agent()` rather than concatenating strings
elsewhere.
