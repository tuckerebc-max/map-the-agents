# Fable Orchestrator

[![CI](https://github.com/Rylaa/fable5-opus5-orchestrator/actions/workflows/ci.yml/badge.svg)](https://github.com/Rylaa/fable5-opus5-orchestrator/actions/workflows/ci.yml)

A Claude Code plugin that makes the chair ask first: every question a job raises goes to you at the start, in rounds, before anything is planned, delegated or edited. Four hooks enforce it so it does not depend on the model remembering.

## Install

```
/plugin marketplace add Rylaa/fable5-opus5-orchestrator
/plugin install orchestrator@fable-orchestrator
```

Restart Claude Code afterwards. Needs `python3` on PATH; macOS and Linux only.

## How a session runs

1. **You give the chair a job.**
2. **It asks questions — all of them at the start.** It reads the repo first, then asks in rounds until no question is left open and a worker's spec could be written without guessing. Nothing is asked mid-implementation.
3. **It writes the ledger** — the answers under `## Clarified`, then every requirement as one checkbox line in `./.workflow/LEDGER.md`.
4. **It does the work** — directly, or through workers. Workers cannot ask you anything, which is why step 2 exists.
5. **It closes** — every ledger box ticked or deferred with your approval; the first turn-end with open items is held.

Skip step 2, 3 or 5 and a hook stops you.

## The four gates

| # | Gate | Fires when | What unblocks it |
|---|------|------------|------------------|
| 1 | Clarify (PreToolUse) | a spawn over the threshold, ledger has no real answers | `## Clarified` with answered `Q -> A` lines and a `Branch:` line |
| 2 | Spawn (PreToolUse) | spawn prompt over 1500 chars, no active ledger | any `.workflow/LEDGER*.md` with numbered checkbox items |
| 3 | Task list (PreToolUse) | 3rd tracker task, still no ledger (fires once) | same: ask, then write the ledger |
| 4 | Close (Stop) | turn ends with open items (fires once per session) | finish them, defer with your approval, or say so |

Never gated: short spawns, forks, and teammates. A fully closed ledger from an earlier session does not disarm anything; retire one by renaming it `LEDGER-<topic>-archive.md`.

## The `## Clarified` record

The protocol is [`skills/clarify/SKILL.md`](skills/clarify/SKILL.md). It scans seven axes (scope edge, acceptance, constraints, whose call each choice is, priority conflicts, contact with existing code, failure behaviour), asks only what would change the code, never asks what the repo answers, and always asks one thing: does the work land on the branch checked out now, or a new one?

```markdown
## Clarified
- Q1: does this replace the old exporter, or run beside it? -> beside it, for one release
- Q2: is the CSV column order part of the contract? -> yes, downstream parses by position
- Branch: main, the checkout in place
```

The hook reads it by four rules and names the one that failed: every bullet's last `?` has its `->` answer; no `Assumption:` line; at least one answered question; a `Branch:` line. Plain bullets only. A checkbox line ends the section; a template in a code fence or an HTML comment is an example, not a record.

## The ledger

```markdown
- [ ] 1. Every explicit requirement, one line each
- [ ] 2. Implicit expectations and constraints too
- [x] 3. Marked done once it is done
- [~] 4. deferred: user approved postponing this
```

Phases cite item numbers and discoveries are appended.

## Configuration

Optional, under `"env"` in `~/.claude/settings.json`.

| Env var | Default | Meaning |
|---------|---------|---------|
| `LEDGER_GUARD_THRESHOLD` | 1500 | spawn-guard gate, in chars |
| `LEDGER_GUARD_CLARIFY` | on | `0` disables the clarify gate |
| `LEDGER_GUARD_TASKS` | 3 | Nth ledgerless tracker task denied; `0` off |
| `LEDGER_GUARD_STOP_MODE` | once-per-session | `every-turn` blocks on every turn |
| `FABLE_ORCH_METRICS` | on | `0` disables the local metrics log |
| `FABLE_ORCH_SWARM_CLEANUP` | on | `0` disables teammate reaping |
| `FABLE_ORCH_TEAMMATE_IDLE_H` | 1 | reap teammate panes idle for N hours; `0` off |

Finished teammates are reaped automatically at session end and on a rate-limited idle sweep. Metrics go to `~/.claude/fable-orch/metrics.jsonl`; `python3 scripts/stats.py` prints the summary.

## Tests

```
python3 -m pytest tests/ -q
```

The hooks are stdin/stdout JSON filters, so the tests run them end to end as subprocesses, and a second layer pins the core text and the skill against the decisions that produced them.

## Limitations

- Hooks check shape, not fidelity: the clarify gate proves questions were answered in the documented shape, not that the right ones were asked.
- Enforcement is only as strong as the host's hook pipeline; verify once on your setup.

## License

MIT
