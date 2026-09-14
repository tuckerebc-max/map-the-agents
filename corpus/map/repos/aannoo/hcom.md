# aannoo/hcom

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit fabb309b57cb @ 66e9c15eec3dd6cb

## Summary (orientation draft, not independently verified)

hcom is a single-binary Rust CLI that lets coding agents message, observe, spawn, and fork each other via hooks and a local SQLite database, with an MQTT-based relay for cross-device sync. Evidence covers the README product docs and the relay command implementation; one prior claim about a Rust 1.88+ build requirement was dropped as unsupported. Evidence coverage: 166 of 230 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 16 documented, 2 code-inspected. A current commit is not the same as complete source coverage.

## Facets

18 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] hcom is a CLI that coding agents use to message, watch, and spawn each other across terminals, implemented as a single Rust binary with no background services. -- evidence: [README.md#L9-L9](https://github.com/aannoo/hcom/blob/fabb309b57cb33b39c69b773cd759723a10e94b5/README.md#L9-L9), [README.md#L15-L15](https://github.com/aannoo/hcom/blob/fabb309b57cb33b39c69b773cd759723a10e94b5/README.md#L15-L15)
- components (5 claim(s)):
  - [observation/documented] Hooks record agent activity to a local SQLite database and deliver messages from it; messages arrive mid-turn between tool calls or wake idle agents. -- evidence: [README.md#L97-L97](https://github.com/aannoo/hcom/blob/fabb309b57cb33b39c69b773cd759723a10e94b5/README.md#L97-L97), [README.md#L103-L103](https://github.com/aannoo/hcom/blob/fabb309b57cb33b39c69b773cd759723a10e94b5/README.md#L103-L103)
  - [observation/documented] Hooks are installed into config dirs under ~/ (or HCOM_DIR) on first run, and hook-less AI tools can join by running `hcom start`. -- evidence: [README.md#L116-L116](https://github.com/aannoo/hcom/blob/fabb309b57cb33b39c69b773cd759723a10e94b5/README.md#L116-L116), [README.md#L114-L114](https://github.com/aannoo/hcom/blob/fabb309b57cb33b39c69b773cd759723a10e94b5/README.md#L114-L114)
- design-choices (1 claim(s)):
  - [observation/documented] Collision detection is on by default: if two agents edit the same file within 30 seconds, both are notified. -- evidence: [README.md#L112-L112](https://github.com/aannoo/hcom/blob/fabb309b57cb33b39c69b773cd759723a10e94b5/README.md#L112-L112)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: contributors build with cargo build && cargo test, set dev_root to run a local build, and run `just ci` as the local CI gate; the codebase is Rust. -- evidence: [README.md#L432-L432](https://github.com/aannoo/hcom/blob/fabb309b57cb33b39c69b773cd759723a10e94b5/README.md#L432-L432), [README.md#L434-L439](https://github.com/aannoo/hcom/blob/fabb309b57cb33b39c69b773cd759723a10e94b5/README.md#L434-L439)
  - [observation/documented] Repository development practice: building from source uses git clone, cargo build, and cargo test; local builds can be symlinked into ~/.cargo/bin or selected via the dev_root config. -- evidence: [README.md#L395-L399](https://github.com/aannoo/hcom/blob/fabb309b57cb33b39c69b773cd759723a10e94b5/README.md#L395-L399), [README.md#L407-L409](https://github.com/aannoo/hcom/blob/fabb309b57cb33b39c69b773cd759723a10e94b5/README.md#L407-L409), [README.md#L413-L417](https://github.com/aannoo/hcom/blob/fabb309b57cb33b39c69b773cd759723a10e94b5/README.md#L413-L417)
- skills-patterns (1 claim(s)):
  - [observation/documented] Bundled workflow scripts include `hcom run confess` (honesty self-eval with an independent calibrator and judge), `debate` (judge-coordinated rounds), and `fatcow` (headless file-reading agent); custom *.sh/*.py scripts in ~/.hcom/scripts/ are auto-discovered. -- evidence: [README.md#L381-L381](https://github.com/aannoo/hcom/blob/fabb309b57cb33b39c69b773cd759723a10e94b5/README.md#L381-L381), [README.md#L383-L383](https://github.com/aannoo/hcom/blob/fabb309b57cb33b39c69b773cd759723a10e94b5/README.md#L383-L383), [README.md#L377-L377](https://github.com/aannoo/hcom/blob/fabb309b57cb33b39c69b773cd759723a10e94b5/README.md#L377-L377), [README.md#L379-L379](https://github.com/aannoo/hcom/blob/fabb309b57cb33b39c69b773cd759723a10e94b5/README.md#L379-L379)
- interfaces (3 claim(s)):
  - [observation/documented] The CLI includes commands such as hcom send, list, term, events --wait, kill, r (resume), f (fork), config, and a TUI dashboard launched by bare `hcom`. -- evidence: [README.md#L272-L277](https://github.com/aannoo/hcom/blob/fabb309b57cb33b39c69b773cd759723a10e94b5/README.md#L272-L277), [README.md#L295-L302](https://github.com/aannoo/hcom/blob/fabb309b57cb33b39c69b773cd759723a10e94b5/README.md#L295-L302)
  - [observation/documented] Launch flags include --tag, --terminal, --dir, --headless, --device (remote spawn via relay), --hcom-prompt, and --hcom-system-prompt; unknown flags are forwarded to the underlying tool. -- evidence: [README.md#L281-L289](https://github.com/aannoo/hcom/blob/fabb309b57cb33b39c69b773cd759723a10e94b5/README.md#L281-L289), [README.md#L291-L291](https://github.com/aannoo/hcom/blob/fabb309b57cb33b39c69b773cd759723a10e94b5/README.md#L291-L291)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
More evidence: [full detail](hcom.detail.md)

Metadata and full claim list: [full detail](hcom.detail.md)
Human notes ([notes](hcom.notes.md), never overwritten by build)

[Back to map index](../../index.md)
