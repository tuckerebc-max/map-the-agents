# hud

**A compact heads-up display for your coding agent.** Instruments while it
works, the answer when it stops - for
[OpenCode](https://opencode.ai),
[Claude Code](https://docs.claude.com/en/docs/claude-code), and
[Codex](https://github.com/openai/codex).
Zero dependencies.

<p align="center">
  <img src="https://raw.githubusercontent.com/adrida/hud-mode/main/docs/hud-demo.gif" alt="hud demo: a real claude code session drowns in its own output, /hud collapses it into the deck, then three builds run with live instruments and a message queued mid-turn" width="680">
</p>

The instruments and the activity line update in place - no scrolling wall of
tool calls. The prompt bar is **always writable**: hit enter mid-turn and
your message queues, firing the moment the answer lands. `esc` interrupts
without losing the session.

When it stops, the answer lands in full - markdown rendered, links
clickable - and you reply right there. Sending a follow-up recompacts the
screen back to just instruments and prompt bar.

<img src="https://raw.githubusercontent.com/adrida/hud-mode/main/docs/hud-answer.svg" alt="hud when the agent stops: the full answer in a framed panel with rendered markdown and a clickable link, instruments below, prompt bar ready" width="100%">

## Install

One command:

```sh
npm install -g adrida/hud-mode && hud install
```

`hud install` walks you through it: your default agent, echo setup for
opencode if you want it, and where /hud lives - then wires the handback
into all three CLIs.

Requires Node ≥ 18 and at least one of `opencode`, `claude`, `codex` on your
PATH.

## Use

```sh
hud                       # your default engine (opencode out of the box)
hud "fix the failing CI"  # or start with a prompt
hud -r                    # resume the last session in this directory
hud -r <session-id>       # resume a specific session

hud claude "fix the CI"   # same deck, claude code autopilot
hud codex -r              # same deck, codex - resume last session
hud default claude        # make bare `hud` fly claude code from now on
```

Launch flags: `-m/--model`, `-e/--effort`, `--danger` (engine-specific
values).

At the `❯` prompt:

| command   | effect |
|-----------|--------|
| `<text>`  | send - or queue it while the agent is working |
| `tab`     | hide / show the current answer |
| `esc`     | interrupt the running turn (session survives) |
| `↑` `↓`   | recall previously typed messages (persisted) |
| `/hud`    | open this session in the full CLI |
| `/model`  | switch model - engine-specific ids · `/model reset` |
| `/effort` | reasoning effort - engine-specific levels |
| `/mode`   | permission / sandbox mode - engine-specific |
| `/gauges` | choose your instruments - `/gauges mdl,msg,tok,t` (saved) |
| `/open`   | print the full answer into the scrollback |
| `/links`  | every url the agent has shared, clickable |
| `/qr`     | show/hide a qr code to this repo - share it |
| `/new`    | start a fresh session |
| `/danger` | skip approvals/sandboxing (sandboxes only) |
| `/id`     | print the session id |
| `/exit`   | quit |

## The toggle

`/hud` works in both directions. From the hud it opens the same session in
the engine's full TUI; from the full TUI you come back - same session,
nothing lost, terminal wiped clean:

| engine | drive | resume | come back with |
|--------|-------|--------|----------------|
| OpenCode | `opencode run --format json` | `-s <id>` / `-c` | `/hud` - a custom command writes the handoff locally at expansion time (near-zero tokens) |
| Claude Code | `claude -p --output-format stream-json` | `--resume <id>` | `/hud` - a `UserPromptSubmit` hook intercepts it **before the model** (zero tokens, ~150 ms) |
| Codex | `codex exec --json` | `exec resume <id>` / `--last` | type `hud` (no slash - a global `AGENTS.md` rule handles it), or quit the TUI |

Quitting any full TUI (ctrl+c) always returns to the hud too.

## Instruments

- `STS` status flag (`NORM` / `PERM` / `INTR` / `FAULT`) · `MDL` model ·
  `MODE` permission/sandbox mode · `EFF` reasoning effort · `MSG` messages ·
  `T+` elapsed · `TOK` output tokens (reasoning included) · `AGT` live
  subagents · `USD` session cost (where the engine reports it) · `CTX`
  context size · `DSK` conversation size on disk (claude, codex)
- The cluster flows onto a second aligned row rather than dropping gauges.
- The activity line shows what the agent is doing right now (`READ`,
  `EDIT`, `EXEC`, `SCAN`, `NET`, `AGENT`, `PLAN`, `THINK`…); the `┄` line
  carries its own narration.
- Links the agent shares go into a per-session ledger
  (`~/.claude/hud/links/`), survive restarts, and - like file paths in the
  activity line - are OSC 8 hyperlinks: cmd/ctrl-clickable in iTerm2,
  Ghostty, WezTerm, Kitty, and friends.
- `/qr` renders a scannable QR code (a from-scratch, zero-dependency
  encoder, verified module-for-module against a reference implementation).
- The panel is yours: `/gauges mdl,msg,tok,t` shows only those instruments,
  in that order, persisted in `~/.claude/hud/config.json` alongside your
  `defaultEngine`. `/gauges reset` brings everything back.

## How it works

No forks, no patches. `hud` drives each CLI headless through its JSON event
stream, maps events onto the shared instruments, and continues one real
session per conversation via the engine's own resume mechanism - which is
also what makes the full-TUI toggle lossless. The handback is a sentinel
file (`~/.claude/hud/handoff.json`) that the wrapper watches while a full
TUI is open; each engine gets its most native way of writing it (hook /
AGENTS.md rule / command template).

`hud install` touches: `~/.claude/skills/hud/`, a hook entry in
`~/.claude/settings.json` (backed up to `.hud-backup`),
`~/.codex/prompts/hud.md`, a marker-guarded block in `~/.codex/AGENTS.md`,
and `~/.config/opencode/commands/hud.md`. `hud uninstall` removes all of it.

## Roadmap

- [ ] In-hud permission approvals (via the Agent SDK)
- [ ] Streaming partial text into the narration line
- [ ] Zero-token codex handback (plugin hooks)
- [ ] Per-directory engine memory for bare `hud`

## License

MIT - built by [tracer](https://tracerml.ai)
