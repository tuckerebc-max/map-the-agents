# getpaseo/paseo -- full detail

[Back to orientation](paseo.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/getpaseo/paseo/d1b705a0cd91617a5707fae25d80cb0be3057950/412941229c6b93c1.json](../../../wiki/dossiers/getpaseo/paseo/d1b705a0cd91617a5707fae25d80cb0be3057950/412941229c6b93c1.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The monorepo includes packages/server (daemon with agent orchestration, WebSocket API, MCP server), packages/app (Expo client), packages/cli, packages/desktop (Electron), packages/relay, and packages/website. -- evidence: [README.md#L171-L176](https://github.com/getpaseo/paseo/blob/d1b705a0cd91617a5707fae25d80cb0be3057950/README.md#L171-L176), [CLAUDE.md#L11-L16](https://github.com/getpaseo/paseo/blob/d1b705a0cd91617a5707fae25d80cb0be3057950/CLAUDE.md#L11-L16) (`clm_9863cfd26a467fda82c4be1692baa297cbbfc4b1d2d687a3b1a956b577ca97ad`)

## design-choices (2 claim(s))

- [observation/documented] Paseo is self-hosted: agents run on the user's own machine with their existing dev environment, tools, configs, and skills. -- evidence: [README.md#L44-L48](https://github.com/getpaseo/paseo/blob/d1b705a0cd91617a5707fae25d80cb0be3057950/README.md#L44-L48) (`clm_66a42e99517dd335fb6d8a39cdd4f7b3874a3659a9f51ccffecf9ad3b8677f14`)
- [observation/documented] The README states Paseo has no telemetry, tracking, or forced log-ins, describing a privacy-first stance. -- evidence: [README.md#L44-L48](https://github.com/getpaseo/paseo/blob/d1b705a0cd91617a5707fae25d80cb0be3057950/README.md#L44-L48) (`clm_fffa944e55dfe362466200e6a7bbb1db41fb64b225659644cd48a53718565b9a`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributors must run typecheck and lint after every change, run only the specific vitest file they changed (never the full suite locally), and push to CI for full-suite verification. -- evidence: [CLAUDE.md#L118-L141](https://github.com/getpaseo/paseo/blob/d1b705a0cd91617a5707fae25d80cb0be3057950/CLAUDE.md#L118-L141), [CLAUDE.md#L93-L103](https://github.com/getpaseo/paseo/blob/d1b705a0cd91617a5707fae25d80cb0be3057950/CLAUDE.md#L93-L103) (`clm_c23e96086ce2f2ce61e3545c3e5bfa5f750660f0de1a8284832580bc615eae56`)

## skills-patterns (1 claim(s))

- [observation/documented] Paseo ships skills installable via `npx skills add getpaseo/paseo`, including /paseo-handoff, /paseo-advisor, and /paseo-committee for agent-to-agent delegation and review patterns. -- evidence: [README.md#L163-L165](https://github.com/getpaseo/paseo/blob/d1b705a0cd91617a5707fae25d80cb0be3057950/README.md#L163-L165), [README.md#L157-L159](https://github.com/getpaseo/paseo/blob/d1b705a0cd91617a5707fae25d80cb0be3057950/README.md#L157-L159), [README.md#L155-L155](https://github.com/getpaseo/paseo/blob/d1b705a0cd91617a5707fae25d80cb0be3057950/README.md#L155-L155) (`clm_c69eea4ce00cf55055f8c61303a45d7386ac62373f342711e500d89e89a0a926`)

## interfaces (4 claim(s))

- [observation/documented] Paseo exposes a CLI with commands like `paseo run --provider`, `paseo ls`, `paseo attach`, and `paseo send` for launching and interacting with agents from the terminal. -- evidence: [README.md#L113-L113](https://github.com/getpaseo/paseo/blob/d1b705a0cd91617a5707fae25d80cb0be3057950/README.md#L113-L113), [README.md#L119-L121](https://github.com/getpaseo/paseo/blob/d1b705a0cd91617a5707fae25d80cb0be3057950/README.md#L119-L121), [README.md#L115-L117](https://github.com/getpaseo/paseo/blob/d1b705a0cd91617a5707fae25d80cb0be3057950/README.md#L115-L117) (`clm_2f73e3534f4d034ea74a842c21d192a3cf37611f8178ba13f00d613de01ff20c`)
- [observation/documented] The CLI can target a remote daemon with `--host`, where `--cwd` is interpreted as a path on that host. -- evidence: [README.md#L124-L125](https://github.com/getpaseo/paseo/blob/d1b705a0cd91617a5707fae25d80cb0be3057950/README.md#L124-L125) (`clm_5ccbe47424035d9d64d35fded32cec0662a3b007defd5b728d24a679c4480d97`)
- [observation/documented] A TypeScript SDK package `@getpaseo/client` connects over WebSocket (e.g. ws://127.0.0.1:6767/ws) and lets code create agents with a provider, cwd, and prompt, then await their result. -- evidence: [README.md#L131-L131](https://github.com/getpaseo/paseo/blob/d1b705a0cd91617a5707fae25d80cb0be3057950/README.md#L131-L131), [README.md#L136-L137](https://github.com/getpaseo/paseo/blob/d1b705a0cd91617a5707fae25d80cb0be3057950/README.md#L136-L137), [README.md#L139-L143](https://github.com/getpaseo/paseo/blob/d1b705a0cd91617a5707fae25d80cb0be3057950/README.md#L139-L143), [README.md#L145-L146](https://github.com/getpaseo/paseo/blob/d1b705a0cd91617a5707fae25d80cb0be3057950/README.md#L145-L146) (`clm_b7d0ba4811f8358ebb573999b823f55d887046a8bf107e752c12962c5c0fb96a`)
- [observation/documented] The daemon supports a plugin system: TypeScript plugins adding themes, panels, commands, settings screens, and providers, installed via `paseo plugin add <source>` from a local directory or Git repo. -- evidence: [README.md#L52-L53](https://github.com/getpaseo/paseo/blob/d1b705a0cd91617a5707fae25d80cb0be3057950/README.md#L52-L53) (`clm_6b701738db42bec296373cb7b0ab3c02bdf18a8fa259d260498b10a4358e02e6`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (1 claim(s))

- [observation/documented] A local daemon manages the coding agents, and clients (desktop, mobile, web, CLI) connect to it; agents can also run in parallel on the user's machines. -- evidence: [README.md#L61-L61](https://github.com/getpaseo/paseo/blob/d1b705a0cd91617a5707fae25d80cb0be3057950/README.md#L61-L61), [README.md#L42-L42](https://github.com/getpaseo/paseo/blob/d1b705a0cd91617a5707fae25d80cb0be3057950/README.md#L42-L42) (`clm_df8297d21f6e72e24420ed12e4df86bf1f31b26078d5dbc39c99cb0682027512`)

## tools-permissions (1 claim(s))

- [observation/documented] Plugins run with access to the daemon machine and connected clients, so users are warned to install only code they trust. -- evidence: [README.md#L55-L57](https://github.com/getpaseo/paseo/blob/d1b705a0cd91617a5707fae25d80cb0be3057950/README.md#L55-L57) (`clm_4266081afd5994302ccb482d77ac5360b01263cbbb2837e39a5d2a87987bdc0f`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Paseo requires at least one external agent CLI (Claude Code, Codex, GitHub Copilot, OpenCode, or Pi) installed and configured with credentials. -- evidence: [README.md#L67-L71](https://github.com/getpaseo/paseo/blob/d1b705a0cd91617a5707fae25d80cb0be3057950/README.md#L67-L71), [README.md#L65-L65](https://github.com/getpaseo/paseo/blob/d1b705a0cd91617a5707fae25d80cb0be3057950/README.md#L65-L65) (`clm_a84d860c2cac79f2946f6e52b58fc3557c40546367a737cb01469930a65c3d68`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

