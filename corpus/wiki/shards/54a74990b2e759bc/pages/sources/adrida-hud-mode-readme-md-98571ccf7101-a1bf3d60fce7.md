---
access: public
aliases: []
claim_ids:
- clm_044844796196b44f0ae926f10df9febb9bc042d73bbc4fbd774039a47e3b4088
- clm_095d2b2117c26395a87995bb7449f852a385c304e5adf5afa63e30afa7e953df
- clm_1727cac146f16a84ce041e2539180c8022e2b3392d88aba4c221ae593ce297f3
- clm_193656ecc5ce2d0a371f8622ccc4fdf9329990f7d4cb0bf067c0e392f1154577
- clm_205c45bbb4306f8bd90047cf9fcba9c8b38d82ee217f29aa361ff16a90717f2f
- clm_2bd1c0968d43df304d907c7b5e6946743afb83ae528a989dcfd5145a1133db61
- clm_3cf87527646756963f3db01c74162e9b3f3b0fb21a20d97f62408392d97c454e
- clm_44b73d9791847cb149e34abad4b4193dcf7d251564a4be32500869ce5b6b173e
- clm_691a1f4d399a669cfd4fdcde4402f2b469d32be029b3ea301d9bc41312e76650
- clm_73ad36a8f1c4ca1d92badf7ed5a981df7df7f9094892a3aecf8f53382cd6ae47
- clm_8859f337611be4389bc9dd459e9974b2a148b55970b5e0b86991a43e9435736d
- clm_8b4c970057b2f5984635737b68b0ba1b5cf40501a052387fba718cb65d88e6b5
- clm_a505ad138af12de25ef8e90d7fc86fb1c50dddf1487e9659a11140a6db7aa13b
- clm_ec4a37b6926f2ed10319150ee5c96119d3c772a6ee6aaaa121d7ae6de0477c3c
maturity: draft
page_id: pg_6a4871b576be584095efa1bf3d60fce7
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_6f9f4ad4d35352fdbddc65280f637215
title: adrida/hud-mode/README.md @ 98571ccf7101
updated_at: '2026-09-14T01:29:51Z'
---

# adrida/hud-mode/README.md @ 98571ccf7101

<!-- rcw:begin owner=source:src_6f9f4ad4d35352fdbddc65280f637215 block=evidence -->
- The product is a terminal HUD for coding agents, installed globally via npm and launched with the `hud` command, optionally with a prompt argument. [@claim:clm_044844796196b44f0ae926f10df9febb9bc042d73bbc4fbd774039a47e3b4088]
- Requires Node >= 18 and at least one of opencode, claude, or codex on the PATH. [@claim:clm_095d2b2117c26395a87995bb7449f852a385c304e5adf5afa63e30afa7e953df]
- hud drives each CLI headless through its JSON event stream (e.g. `opencode run --format json`, `claude -p --output-format stream-json`, `codex exec --json`) and resumes sessions via each engine's own resume mechanism. [@claim:clm_1727cac146f16a84ce041e2539180c8022e2b3392d88aba4c221ae593ce297f3]
- The project claims zero dependencies, including a from-scratch QR encoder verified module-for-module against a reference implementation. [@claim:clm_193656ecc5ce2d0a371f8622ccc4fdf9329990f7d4cb0bf067c0e392f1154577]
- `hud install` wires a skills directory, a settings.json hook (backed up), codex prompt and AGENTS.md entries, and an opencode command file; `hud uninstall` removes all of it. [@claim:clm_205c45bbb4306f8bd90047cf9fcba9c8b38d82ee217f29aa361ff16a90717f2f]
- Supports three engines: OpenCode (default), Claude Code, and Codex; `hud default claude` changes the engine used by bare `hud`. [@claim:clm_2bd1c0968d43df304d907c7b5e6946743afb83ae528a989dcfd5145a1133db61]
- Shared agent links persist in a per-session ledger at ~/.claude/hud/links/ across restarts, and gauge selections persist in ~/.claude/hud/config.json. [@claim:clm_3cf87527646756963f3db01c74162e9b3f3b0fb21a20d97f62408392d97c454e]
- When the agent stops, the full answer is shown with rendered markdown and clickable links; sending a follow-up recompacts the screen back to instruments and prompt bar. [@claim:clm_44b73d9791847cb149e34abad4b4193dcf7d251564a4be32500869ce5b6b173e]
- Instruments and the activity line update in place rather than scrolling; the prompt bar stays writable so messages typed mid-turn queue and fire when the answer lands. [@claim:clm_691a1f4d399a669cfd4fdcde4402f2b469d32be029b3ea301d9bc41312e76650]
- Interactive commands at the prompt include /model, /effort, /mode, /gauges, /links, /qr, /new, /danger, /id, /exit, and /hud to toggle to the engine's full TUI. [@claim:clm_73ad36a8f1c4ca1d92badf7ed5a981df7df7f9094892a3aecf8f53382cd6ae47]
- Gauges include status flag, model, mode, effort, message count, elapsed time, tokens, live subagents, session cost, context size, and on-disk conversation size, flowing onto a second aligned row when needed. [@claim:clm_8859f337611be4389bc9dd459e9974b2a148b55970b5e0b86991a43e9435736d]
- Launch flags include `-m/--model`, `-e/--effort`, and `--danger`, with engine-specific values; `-r` resumes the last or a specific session. [@claim:clm_8b4c970057b2f5984635737b68b0ba1b5cf40501a052387fba718cb65d88e6b5]
- Roadmap items indicate in-hud permission approvals, streaming partial narration text, zero-token codex handback, and per-directory engine memory are not yet implemented. [@claim:clm_a505ad138af12de25ef8e90d7fc86fb1c50dddf1487e9659a11140a6db7aa13b]
- The full-TUI handback uses a sentinel file ~/.claude/hud/handoff.json watched by the wrapper, written per-engine via a hook, an AGENTS.md rule, or a command template. [@claim:clm_ec4a37b6926f2ed10319150ee5c96119d3c772a6ee6aaaa121d7ae6de0477c3c]
<!-- rcw:end owner=source:src_6f9f4ad4d35352fdbddc65280f637215 block=evidence -->

## Researcher notes

