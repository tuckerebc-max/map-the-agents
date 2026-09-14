---
access: public
aliases: []
claim_ids:
- clm_2f73e3534f4d034ea74a842c21d192a3cf37611f8178ba13f00d613de01ff20c
- clm_4266081afd5994302ccb482d77ac5360b01263cbbb2837e39a5d2a87987bdc0f
- clm_5ccbe47424035d9d64d35fded32cec0662a3b007defd5b728d24a679c4480d97
- clm_66a42e99517dd335fb6d8a39cdd4f7b3874a3659a9f51ccffecf9ad3b8677f14
- clm_6b701738db42bec296373cb7b0ab3c02bdf18a8fa259d260498b10a4358e02e6
- clm_9863cfd26a467fda82c4be1692baa297cbbfc4b1d2d687a3b1a956b577ca97ad
- clm_a84d860c2cac79f2946f6e52b58fc3557c40546367a737cb01469930a65c3d68
- clm_b7d0ba4811f8358ebb573999b823f55d887046a8bf107e752c12962c5c0fb96a
- clm_c69eea4ce00cf55055f8c61303a45d7386ac62373f342711e500d89e89a0a926
- clm_df8297d21f6e72e24420ed12e4df86bf1f31b26078d5dbc39c99cb0682027512
- clm_fffa944e55dfe362466200e6a7bbb1db41fb64b225659644cd48a53718565b9a
maturity: draft
page_id: pg_1dff3fe7641254a086577c6520b73407
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_d1f4bd3f9cfe5d84a3d44e8511326d34
title: getpaseo/paseo/README.md @ d1b705a0cd91
updated_at: '2026-09-14T01:51:08Z'
---

# getpaseo/paseo/README.md @ d1b705a0cd91

<!-- rcw:begin owner=source:src_d1f4bd3f9cfe5d84a3d44e8511326d34 block=evidence -->
- Paseo exposes a CLI with commands like `paseo run --provider`, `paseo ls`, `paseo attach`, and `paseo send` for launching and interacting with agents from the terminal. [@claim:clm_2f73e3534f4d034ea74a842c21d192a3cf37611f8178ba13f00d613de01ff20c]
- Plugins run with access to the daemon machine and connected clients, so users are warned to install only code they trust. [@claim:clm_4266081afd5994302ccb482d77ac5360b01263cbbb2837e39a5d2a87987bdc0f]
- The CLI can target a remote daemon with `--host`, where `--cwd` is interpreted as a path on that host. [@claim:clm_5ccbe47424035d9d64d35fded32cec0662a3b007defd5b728d24a679c4480d97]
- Paseo is self-hosted: agents run on the user's own machine with their existing dev environment, tools, configs, and skills. [@claim:clm_66a42e99517dd335fb6d8a39cdd4f7b3874a3659a9f51ccffecf9ad3b8677f14]
- The daemon supports a plugin system: TypeScript plugins adding themes, panels, commands, settings screens, and providers, installed via `paseo plugin add <source>` from a local directory or Git repo. [@claim:clm_6b701738db42bec296373cb7b0ab3c02bdf18a8fa259d260498b10a4358e02e6]
- The monorepo includes packages/server (daemon with agent orchestration, WebSocket API, MCP server), packages/app (Expo client), packages/cli, packages/desktop (Electron), packages/relay, and packages/website. [@claim:clm_9863cfd26a467fda82c4be1692baa297cbbfc4b1d2d687a3b1a956b577ca97ad]
- Paseo requires at least one external agent CLI (Claude Code, Codex, GitHub Copilot, OpenCode, or Pi) installed and configured with credentials. [@claim:clm_a84d860c2cac79f2946f6e52b58fc3557c40546367a737cb01469930a65c3d68]
- A TypeScript SDK package `@getpaseo/client` connects over WebSocket (e.g. ws://127.0.0.1:6767/ws) and lets code create agents with a provider, cwd, and prompt, then await their result. [@claim:clm_b7d0ba4811f8358ebb573999b823f55d887046a8bf107e752c12962c5c0fb96a]
- Paseo ships skills installable via `npx skills add getpaseo/paseo`, including /paseo-handoff, /paseo-advisor, and /paseo-committee for agent-to-agent delegation and review patterns. [@claim:clm_c69eea4ce00cf55055f8c61303a45d7386ac62373f342711e500d89e89a0a926]
- A local daemon manages the coding agents, and clients (desktop, mobile, web, CLI) connect to it; agents can also run in parallel on the user's machines. [@claim:clm_df8297d21f6e72e24420ed12e4df86bf1f31b26078d5dbc39c99cb0682027512]
- The README states Paseo has no telemetry, tracking, or forced log-ins, describing a privacy-first stance. [@claim:clm_fffa944e55dfe362466200e6a7bbb1db41fb64b225659644cd48a53718565b9a]
<!-- rcw:end owner=source:src_d1f4bd3f9cfe5d84a3d44e8511326d34 block=evidence -->

## Researcher notes

