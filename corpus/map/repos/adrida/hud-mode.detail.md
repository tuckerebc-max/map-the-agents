# adrida/hud-mode -- full detail

[Back to orientation](hud-mode.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/adrida/hud-mode/98571ccf71015216d34cd8f37df8bf15e7e3f1f9/278eae6eb4afb581.json](../../../wiki/dossiers/adrida/hud-mode/98571ccf71015216d34cd8f37df8bf15e7e3f1f9/278eae6eb4afb581.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] Gauges include status flag, model, mode, effort, message count, elapsed time, tokens, live subagents, session cost, context size, and on-disk conversation size, flowing onto a second aligned row when needed. -- evidence: [README.md#L93-L110](https://github.com/adrida/hud-mode/blob/98571ccf71015216d34cd8f37df8bf15e7e3f1f9/README.md#L93-L110) (`clm_8859f337611be4389bc9dd459e9974b2a148b55970b5e0b86991a43e9435736d`)

## design-choices (3 claim(s))

- [observation/documented] Instruments and the activity line update in place rather than scrolling; the prompt bar stays writable so messages typed mid-turn queue and fire when the answer lands. -- evidence: [README.md#L14-L17](https://github.com/adrida/hud-mode/blob/98571ccf71015216d34cd8f37df8bf15e7e3f1f9/README.md#L14-L17) (`clm_691a1f4d399a669cfd4fdcde4402f2b469d32be029b3ea301d9bc41312e76650`)
- [observation/documented] When the agent stops, the full answer is shown with rendered markdown and clickable links; sending a follow-up recompacts the screen back to instruments and prompt bar. -- evidence: [README.md#L19-L21](https://github.com/adrida/hud-mode/blob/98571ccf71015216d34cd8f37df8bf15e7e3f1f9/README.md#L19-L21) (`clm_44b73d9791847cb149e34abad4b4193dcf7d251564a4be32500869ce5b6b173e`)
- [observation/documented] The project claims zero dependencies, including a from-scratch QR encoder verified module-for-module against a reference implementation. -- evidence: [README.md#L93-L110](https://github.com/adrida/hud-mode/blob/98571ccf71015216d34cd8f37df8bf15e7e3f1f9/README.md#L93-L110), [README.md#L3-L8](https://github.com/adrida/hud-mode/blob/98571ccf71015216d34cd8f37df8bf15e7e3f1f9/README.md#L3-L8) (`clm_193656ecc5ce2d0a371f8622ccc4fdf9329990f7d4cb0bf067c0e392f1154577`)

## workflows (1 claim(s))

- [observation/documented] `hud install` wires a skills directory, a settings.json hook (backed up), codex prompt and AGENTS.md entries, and an opencode command file; `hud uninstall` removes all of it. -- evidence: [README.md#L122-L125](https://github.com/adrida/hud-mode/blob/98571ccf71015216d34cd8f37df8bf15e7e3f1f9/README.md#L122-L125) (`clm_205c45bbb4306f8bd90047cf9fcba9c8b38d82ee217f29aa361ff16a90717f2f`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (4 claim(s))

- [observation/documented] The product is a terminal HUD for coding agents, installed globally via npm and launched with the `hud` command, optionally with a prompt argument. -- evidence: [README.md#L42-L46](https://github.com/adrida/hud-mode/blob/98571ccf71015216d34cd8f37df8bf15e7e3f1f9/README.md#L42-L46), [README.md#L3-L8](https://github.com/adrida/hud-mode/blob/98571ccf71015216d34cd8f37df8bf15e7e3f1f9/README.md#L3-L8), [README.md#L29-L31](https://github.com/adrida/hud-mode/blob/98571ccf71015216d34cd8f37df8bf15e7e3f1f9/README.md#L29-L31) (`clm_044844796196b44f0ae926f10df9febb9bc042d73bbc4fbd774039a47e3b4088`)
- [observation/documented] Supports three engines: OpenCode (default), Claude Code, and Codex; `hud default claude` changes the engine used by bare `hud`. -- evidence: [README.md#L42-L46](https://github.com/adrida/hud-mode/blob/98571ccf71015216d34cd8f37df8bf15e7e3f1f9/README.md#L42-L46), [README.md#L48-L51](https://github.com/adrida/hud-mode/blob/98571ccf71015216d34cd8f37df8bf15e7e3f1f9/README.md#L48-L51), [README.md#L3-L8](https://github.com/adrida/hud-mode/blob/98571ccf71015216d34cd8f37df8bf15e7e3f1f9/README.md#L3-L8) (`clm_2bd1c0968d43df304d907c7b5e6946743afb83ae528a989dcfd5145a1133db61`)
- [observation/documented] Launch flags include `-m/--model`, `-e/--effort`, and `--danger`, with engine-specific values; `-r` resumes the last or a specific session. -- evidence: [README.md#L42-L46](https://github.com/adrida/hud-mode/blob/98571ccf71015216d34cd8f37df8bf15e7e3f1f9/README.md#L42-L46), [README.md#L53-L54](https://github.com/adrida/hud-mode/blob/98571ccf71015216d34cd8f37df8bf15e7e3f1f9/README.md#L53-L54) (`clm_8b4c970057b2f5984635737b68b0ba1b5cf40501a052387fba718cb65d88e6b5`)
- [observation/documented] Interactive commands at the prompt include /model, /effort, /mode, /gauges, /links, /qr, /new, /danger, /id, /exit, and /hud to toggle to the engine's full TUI. -- evidence: [README.md#L58-L75](https://github.com/adrida/hud-mode/blob/98571ccf71015216d34cd8f37df8bf15e7e3f1f9/README.md#L58-L75) (`clm_73ad36a8f1c4ca1d92badf7ed5a981df7df7f9094892a3aecf8f53382cd6ae47`)

## memory-state (1 claim(s))

- [observation/documented] Shared agent links persist in a per-session ledger at ~/.claude/hud/links/ across restarts, and gauge selections persist in ~/.claude/hud/config.json. -- evidence: [README.md#L93-L110](https://github.com/adrida/hud-mode/blob/98571ccf71015216d34cd8f37df8bf15e7e3f1f9/README.md#L93-L110) (`clm_3cf87527646756963f3db01c74162e9b3f3b0fb21a20d97f62408392d97c454e`)

## orchestration (2 claim(s))

- [observation/documented] hud drives each CLI headless through its JSON event stream (e.g. `opencode run --format json`, `claude -p --output-format stream-json`, `codex exec --json`) and resumes sessions via each engine's own resume mechanism. -- evidence: [README.md#L83-L87](https://github.com/adrida/hud-mode/blob/98571ccf71015216d34cd8f37df8bf15e7e3f1f9/README.md#L83-L87), [README.md#L114-L120](https://github.com/adrida/hud-mode/blob/98571ccf71015216d34cd8f37df8bf15e7e3f1f9/README.md#L114-L120) (`clm_1727cac146f16a84ce041e2539180c8022e2b3392d88aba4c221ae593ce297f3`)
- [observation/documented] The full-TUI handback uses a sentinel file ~/.claude/hud/handoff.json watched by the wrapper, written per-engine via a hook, an AGENTS.md rule, or a command template. -- evidence: [README.md#L114-L120](https://github.com/adrida/hud-mode/blob/98571ccf71015216d34cd8f37df8bf15e7e3f1f9/README.md#L114-L120) (`clm_ec4a37b6926f2ed10319150ee5c96119d3c772a6ee6aaaa121d7ae6de0477c3c`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Requires Node >= 18 and at least one of opencode, claude, or codex on the PATH. -- evidence: [README.md#L37-L38](https://github.com/adrida/hud-mode/blob/98571ccf71015216d34cd8f37df8bf15e7e3f1f9/README.md#L37-L38) (`clm_095d2b2117c26395a87995bb7449f852a385c304e5adf5afa63e30afa7e953df`)

## limitations (1 claim(s))

- [observation/documented] Roadmap items indicate in-hud permission approvals, streaming partial narration text, zero-token codex handback, and per-directory engine memory are not yet implemented. -- evidence: [README.md#L129-L132](https://github.com/adrida/hud-mode/blob/98571ccf71015216d34cd8f37df8bf15e7e3f1f9/README.md#L129-L132) (`clm_a505ad138af12de25ef8e90d7fc86fb1c50dddf1487e9659a11140a6db7aa13b`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

