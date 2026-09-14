# alihamzaazam/repomon -- full detail

[Back to orientation](repomon.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/alihamzaazam/repomon/e655d18f83d86bc00120e6bbcd1d046dfde16a5a/8834abe468e940fd.json](../../../wiki/dossiers/alihamzaazam/repomon/e655d18f83d86bc00120e6bbcd1d046dfde16a5a/8834abe468e940fd.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] A background daemon, repomond, owns SQLite, file watchers, the git layer, and the agent runtime, exposing a JSON-RPC API over a Unix socket or Windows named pipe; desktop, TUI, and iOS clients are thin clients over that API. -- evidence: [README.md#L142-L144](https://github.com/AliHamzaAzam/repomon/blob/e655d18f83d86bc00120e6bbcd1d046dfde16a5a/README.md#L142-L144) (`clm_524e24a6a7b7d98405dabc6ab3a2d14fb0045269972a724e5472e6790557475e`)
- [observation/documented] The workspace is split into crates: repomon-core (data model, gix git layer, SQLite store, watchers, usage ledger, agent runtime), repomon-daemon, repomon-tui, repomon-mcp, repomon-host, and a Tauri desktop app. -- evidence: [README.md#L146-L153](https://github.com/AliHamzaAzam/repomon/blob/e655d18f83d86bc00120e6bbcd1d046dfde16a5a/README.md#L146-L153) (`clm_dda6addfa466aaeaaf3f2016eac0db62456bb0267af458fbdc3a84f201acf740`)

## design-choices (4 claim(s))

- [observation/documented] Supervision is off by default globally and per lane; enabling requires both the master switch in config.toml and an enabled lane policy, with the master switch overriding every lane. -- evidence: [docs/agent-supervision.md#L93-L96](https://github.com/AliHamzaAzam/repomon/blob/e655d18f83d86bc00120e6bbcd1d046dfde16a5a/docs/agent-supervision.md#L93-L96), [docs/agent-supervision.md#L3-L5](https://github.com/AliHamzaAzam/repomon/blob/e655d18f83d86bc00120e6bbcd1d046dfde16a5a/docs/agent-supervision.md#L3-L5) (`clm_6cb0005c4f3bbe77e2cb89d994ccb59743ee7f108488d2f602832152233747f1`)
- [observation/documented] Default supervision policy auto-approves only repo-scoped command_exec and file_write dialogs; network, credential, deletion, push, install, device, and unknown classes default to hold, and nothing auto-denies out of the box. -- evidence: [docs/agent-supervision.md#L75-L85](https://github.com/AliHamzaAzam/repomon/blob/e655d18f83d86bc00120e6bbcd1d046dfde16a5a/docs/agent-supervision.md#L75-L85), [docs/agent-supervision.md#L87-L89](https://github.com/AliHamzaAzam/repomon/blob/e655d18f83d86bc00120e6bbcd1d046dfde16a5a/docs/agent-supervision.md#L87-L89) (`clm_0c93d16ffc6c42fa8cf73a911418a0b992c8f7b8034f7383dba3350375d9c919`)
- [observation/documented] A hardcoded always-escalate veto (force pushes, rm -rf-shaped deletions, git reset --hard, git clean -f, sudo rm) overrides any policy, including explicit auto_approve mappings and learned rules. -- evidence: [docs/agent-supervision.md#L194-L230](https://github.com/AliHamzaAzam/repomon/blob/e655d18f83d86bc00120e6bbcd1d046dfde16a5a/docs/agent-supervision.md#L194-L230) (`clm_0d9583528c0eb2effcd94126de2120503c10542ba6e69be3ffcbfa9117777403`)
- [observation/documented] supervision.set is deliberately excluded from the remote WebSocket bridge allowlist, so granting auto-approval authority is a local-only decision; agents' MCP tools are read-only with no approval power. -- evidence: [docs/agent-supervision.md#L288-L292](https://github.com/AliHamzaAzam/repomon/blob/e655d18f83d86bc00120e6bbcd1d046dfde16a5a/docs/agent-supervision.md#L288-L292), [docs/agent-supervision.md#L307-L310](https://github.com/AliHamzaAzam/repomon/blob/e655d18f83d86bc00120e6bbcd1d046dfde16a5a/docs/agent-supervision.md#L307-L310) (`clm_441fa662b21ce733bb38dd8462d6e533adc012ee6712f76cff3829b152b497a3`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: the README's development section instructs contributors to run `cargo test --workspace` for Rust and `bun install && bun run test` in apps/desktop for the frontend. -- evidence: [README.md#L157-L161](https://github.com/AliHamzaAzam/repomon/blob/e655d18f83d86bc00120e6bbcd1d046dfde16a5a/README.md#L157-L161) (`clm_78b2b6d9b8a8efa983299bf38d8bb084ae8a4e965e51d873644bb78627038d42`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The daemon exposes a JSON-RPC API documented for writing custom clients, plus an MCP server (`repomond mcp`) that exposes the fleet to agents. -- evidence: [README.md#L89-L97](https://github.com/AliHamzaAzam/repomon/blob/e655d18f83d86bc00120e6bbcd1d046dfde16a5a/README.md#L89-L97), [README.md#L146-L153](https://github.com/AliHamzaAzam/repomon/blob/e655d18f83d86bc00120e6bbcd1d046dfde16a5a/README.md#L146-L153) (`clm_c1c2cde733d9b5b5d8c24084ed815352b39a5a007fc47e97f0b95cf0f5b3cdbe`)
- [observation/documented] Supervision methods live under a `supervision.*` JSON-RPC namespace (get, set, audit, status, nudge) on the local daemon socket. -- evidence: [docs/agent-supervision.md#L276-L282](https://github.com/AliHamzaAzam/repomon/blob/e655d18f83d86bc00120e6bbcd1d046dfde16a5a/docs/agent-supervision.md#L276-L282), [docs/agent-supervision.md#L274-L274](https://github.com/AliHamzaAzam/repomon/blob/e655d18f83d86bc00120e6bbcd1d046dfde16a5a/docs/agent-supervision.md#L274-L274) (`clm_bbc6ea2fa91e6b90bdd70dd3b8b41d2cf8944fc73499770c312450d8921cfdd9`)

## memory-state (2 claim(s))

- [observation/documented] Repomon writes its own SQLite database in a platform data directory (overridable via REPOMON_DATA_DIR) and a Repomind home normally at ~/repomind when that feature is enabled. -- evidence: [README.md#L81-L81](https://github.com/AliHamzaAzam/repomon/blob/e655d18f83d86bc00120e6bbcd1d046dfde16a5a/README.md#L81-L81) (`clm_751e7923e7d7a16bb7c90fcc6b8379a8f3727d3fc9858473ad04b462fbe64e49`)
- [observation/documented] Every supervision action or skipped action writes exactly one row to a durable supervision_log SQLite table recording trigger, decision, keys sent, outcome, and pane excerpt. -- evidence: [docs/agent-supervision.md#L244-L263](https://github.com/AliHamzaAzam/repomon/blob/e655d18f83d86bc00120e6bbcd1d046dfde16a5a/docs/agent-supervision.md#L244-L263), [docs/agent-supervision.md#L241-L242](https://github.com/AliHamzaAzam/repomon/blob/e655d18f83d86bc00120e6bbcd1d046dfde16a5a/docs/agent-supervision.md#L241-L242), [docs/agent-supervision.md#L265-L270](https://github.com/AliHamzaAzam/repomon/blob/e655d18f83d86bc00120e6bbcd1d046dfde16a5a/docs/agent-supervision.md#L265-L270) (`clm_95053e1125715e34605a2c8e58ce8c0483e90e29a7b70e1ba5280aadf078fed3`)

## orchestration (1 claim(s))

- [observation/documented] Agents run in durable session windows: tmux windows on macOS/Linux, or a per-window detached repomon-agent-host.exe ConPTY process on Windows; because the session backend owns the process, agents survive daemon and TUI restarts. -- evidence: [docs/agents.md#L25-L30](https://github.com/AliHamzaAzam/repomon/blob/e655d18f83d86bc00120e6bbcd1d046dfde16a5a/docs/agents.md#L25-L30), [README.md#L77-L77](https://github.com/AliHamzaAzam/repomon/blob/e655d18f83d86bc00120e6bbcd1d046dfde16a5a/README.md#L77-L77), [docs/agents.md#L18-L19](https://github.com/AliHamzaAzam/repomon/blob/e655d18f83d86bc00120e6bbcd1d046dfde16a5a/docs/agents.md#L18-L19) (`clm_8903dba059f744044a80f0807bb1fb45139ed91524474b83883b5f644e2b322f`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The standalone CLI requires Git on every platform and tmux on macOS/Linux; Windows uses a bundled ConPTY host, and the desktop app bundles the daemon, CLI/TUI, and portable tmux so no separate installs are needed. -- evidence: [README.md#L32-L32](https://github.com/AliHamzaAzam/repomon/blob/e655d18f83d86bc00120e6bbcd1d046dfde16a5a/README.md#L32-L32), [README.md#L63-L63](https://github.com/AliHamzaAzam/repomon/blob/e655d18f83d86bc00120e6bbcd1d046dfde16a5a/README.md#L63-L63) (`clm_177b77535d127cf3546e9461131a733a6e2fa39035738e7c5ffbfcd8fa510a30`)

## limitations (1 claim(s))

- [observation/documented] Live agent processes survive app and daemon restarts but not an OS reboot; current desktop downloads lack an OS-level code signature, and the iOS companion is built but not yet released. -- evidence: [README.md#L77-L77](https://github.com/AliHamzaAzam/repomon/blob/e655d18f83d86bc00120e6bbcd1d046dfde16a5a/README.md#L77-L77) (`clm_dfe945c83df1f7dd6c9ad4a4764524f027fea138b908f0dc7cbb9c15afa9e326`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

