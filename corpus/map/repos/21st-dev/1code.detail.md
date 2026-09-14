# 21st-dev/1code -- full detail

[Back to orientation](1code.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/21st-dev/1code/9f1bc76fa4372c18c565b5a4f8daf38ae3595f0e/963ce7c3d14e2d9a.json](../../../wiki/dossiers/21st-dev/1code/9f1bc76fa4372c18c565b5a4f8daf38ae3595f0e/963ce7c3d14e2d9a.json)

## specifications (1 claim(s))

- [observation/documented] 1Code is described as an open-source coding agent client for running Claude Code, Codex, and other coding agents locally or in the cloud. -- evidence: [README.md#L5-L5](https://github.com/21st-dev/1code/blob/9f1bc76fa4372c18c565b5a4f8daf38ae3595f0e/README.md#L5-L5) (`clm_2c1418464554370fa222e5945a48440de3adc2f7908f05a958673857acaa47eb`)

## components (2 claim(s))

- [observation/documented] Documented features include a Kanban board for visualizing agent sessions and a built-in Git client supporting staging, diffs, and pull request creation. -- evidence: [README.md#L11-L34](https://github.com/21st-dev/1code/blob/9f1bc76fa4372c18c565b5a4f8daf38ae3595f0e/README.md#L11-L34) (`clm_6be633ef9a04445b47b6ac21a74d95342d4e8a48c76fcb5c87a2ba884c15be3c`)
- [observation/code-inspected] The terminal session module's spawnPty function catches a failed PTY spawn and retries once using a fallback shell constant. -- evidence: [src/main/lib/terminal/session.ts#L93-L113](https://github.com/21st-dev/1code/blob/9f1bc76fa4372c18c565b5a4f8daf38ae3595f0e/src/main/lib/terminal/session.ts#L93-L113) (`clm_c40781fb933966ef803589514c83dce6dbfe827b64c85f0fd24f227e27051828`)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (1 claim(s))

- [observation/documented] The README states automations can be triggered from GitHub, Linear, or Slack events, or run manually from git events. -- evidence: [README.md#L109-L109](https://github.com/21st-dev/1code/blob/9f1bc76fa4372c18c565b5a4f8daf38ae3595f0e/README.md#L109-L109) (`clm_15e033e9723e27160d29fcd09d0a504cfbc1e9330990f5dff131e3ddd7517803`)

## skills-patterns (1 claim(s))

- [observation/documented] Documented features include custom skills and slash commands, plus custom sub-agents shown with a visual task display in the sidebar. -- evidence: [README.md#L11-L34](https://github.com/21st-dev/1code/blob/9f1bc76fa4372c18c565b5a4f8daf38ae3595f0e/README.md#L11-L34) (`clm_ce239e5e9a3dcaeb22d19f0e7795adcff00aa5ae323a7465ad9043879cc64b32`)

## interfaces (1 claim(s))

- [observation/documented] The documented feature list includes a model selector for switching providers and an integrated terminal panel toggled with a Cmd+J shortcut. -- evidence: [README.md#L11-L34](https://github.com/21st-dev/1code/blob/9f1bc76fa4372c18c565b5a4f8daf38ae3595f0e/README.md#L11-L34) (`clm_dc9b5565709c8481200df0a339c2cff82c7000b618190c0eaf6dcb2787927c2b`)

## memory-state (1 claim(s))

- [observation/documented] The documented feature list states the product supports persistent memory through CLAUDE.md and AGENTS.md files. -- evidence: [README.md#L11-L34](https://github.com/21st-dev/1code/blob/9f1bc76fa4372c18c565b5a4f8daf38ae3595f0e/README.md#L11-L34) (`clm_ea082ac3d1db9558150e3a2503a753be96a62b3c3a6e983e5f3a6877532c748d`)

## orchestration (1 claim(s))

- [observation/documented] Documentation states each chat session runs in its own isolated git worktree, and background agents execute in cloud sandboxes while the local machine sleeps. -- evidence: [README.md#L88-L88](https://github.com/21st-dev/1code/blob/9f1bc76fa4372c18c565b5a4f8daf38ae3595f0e/README.md#L88-L88), [README.md#L44-L48](https://github.com/21st-dev/1code/blob/9f1bc76fa4372c18c565b5a4f8daf38ae3595f0e/README.md#L44-L48) (`clm_cb5dd25cabee6bc339b4b00834d40adf08328069ce2729e5bdb68e330a4807c3`)

## tools-permissions (1 claim(s))

- [observation/documented] Plan mode documentation states the agent's proposed plan must be reviewed and approved, or modified, by the user before the agent acts. -- evidence: [README.md#L77-L82](https://github.com/21st-dev/1code/blob/9f1bc76fa4372c18c565b5a4f8daf38ae3595f0e/README.md#L77-L82) (`clm_5d0bbb369dbb78f9f312e8a919ce26b70d5bb21503412e1448e6e9cef58a8a34`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Build-from-source documentation states Python 3.11 is recommended for native module rebuilds, and setuptools must be installed manually on Python 3.12 and newer. -- evidence: [README.md#L153-L155](https://github.com/21st-dev/1code/blob/9f1bc76fa4372c18c565b5a4f8daf38ae3595f0e/README.md#L153-L155) (`clm_f70cccd960512aff24e806378e6e6fc0005ba58c69e3a619dbff327713cb99fe`)

## limitations (1 claim(s))

- [observation/code-inspected] The terminal session code falls back to the user's home directory when the requested working directory does not exist or is not a directory. -- evidence: [src/main/lib/terminal/session.ts#L32-L43](https://github.com/21st-dev/1code/blob/9f1bc76fa4372c18c565b5a4f8daf38ae3595f0e/src/main/lib/terminal/session.ts#L32-L43), [src/main/lib/terminal/session.ts#L21-L30](https://github.com/21st-dev/1code/blob/9f1bc76fa4372c18c565b5a4f8daf38ae3595f0e/src/main/lib/terminal/session.ts#L21-L30) (`clm_564579a9f71ccada4484d242508daab0129317e508cbb1891f4323eff056298c`)

## relevance (1 claim(s))

- [observation/documented] The README comparison names diff previews, an integrated Git client, and viewing changes before they land as 1Code features. -- evidence: [README.md#L54-L54](https://github.com/21st-dev/1code/blob/9f1bc76fa4372c18c565b5a4f8daf38ae3595f0e/README.md#L54-L54) (`clm_c75fcee7c0aed4d6591b8514ba48d5a8100ba28fd689f267ad5918bd70228660`)

