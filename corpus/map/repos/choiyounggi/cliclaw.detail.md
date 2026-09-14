# choiyounggi/cliclaw -- full detail

[Back to orientation](cliclaw.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/choiyounggi/cliclaw/6a5e048a5abf41dc7a94285f67def78b3637e5e3/16445cc7ff31dba2.json](../../../wiki/dossiers/choiyounggi/cliclaw/6a5e048a5abf41dc7a94285f67def78b3637e5e3/16445cc7ff31dba2.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The codebase is organized as a bot.ts daemon entry point, a cli.ts entry point, and lib/ modules for audit logging, confirm IPC, danger patterns, launchd, streaming, rate limiting, and agent path resolution. -- evidence: [DEVELOPMENT.md#L26-L53](https://github.com/choiyounggi/cliclaw/blob/6a5e048a5abf41dc7a94285f67def78b3637e5e3/DEVELOPMENT.md#L26-L53) (`clm_f773ff00213ac273eabbc940dd3f09365ffb3721635ff6402d05c11660b67429`)

## design-choices (2 claim(s))

- [observation/documented] Agent paths are auto-discovered at startup in three passes (well-known dirs, newest nvm node's bin, login-shell PATH) with no absolute paths in config.json; undetected agents are skipped. -- evidence: [README.md#L181-L181](https://github.com/choiyounggi/cliclaw/blob/6a5e048a5abf41dc7a94285f67def78b3637e5e3/README.md#L181-L181), [README.md#L176-L179](https://github.com/choiyounggi/cliclaw/blob/6a5e048a5abf41dc7a94285f67def78b3637e5e3/README.md#L176-L179) (`clm_85c5f9ad51568446521e5f03cb69d0c9719b7871fe9ec9a6bcb1725922d99a2a`)
- [observation/documented] Secrets written to bot.log/bot.err are pre-redacted, covering Telegram bot tokens, npm tokens, GitHub PATs, and exact matches of the live config token. -- evidence: [README.md#L221-L225](https://github.com/choiyounggi/cliclaw/blob/6a5e048a5abf41dc7a94285f67def78b3637e5e3/README.md#L221-L225) (`clm_2626bd94a913d3340e717fb2be2fb07f3da599b23548c19a6f450588749b9d2d`)

## workflows (3 claim(s))

- [observation/documented] Repository development practice: contributors must pass bun test (222+ cases) and tsc --noEmit, add unit tests for new features, discuss changes over 30 lines via issue/RFC first, and PRs are validated by a GitHub Actions Test workflow on macOS-latest. -- evidence: [CONTRIBUTING.md#L20-L25](https://github.com/choiyounggi/cliclaw/blob/6a5e048a5abf41dc7a94285f67def78b3637e5e3/CONTRIBUTING.md#L20-L25), [CONTRIBUTING.md#L7-L14](https://github.com/choiyounggi/cliclaw/blob/6a5e048a5abf41dc7a94285f67def78b3637e5e3/CONTRIBUTING.md#L7-L14) (`clm_4661b5a785b967c259542fdcbe3f7eab9697708fdf9928ded1b0dc0ba38f40e7`)
- [observation/documented] Repository development practice: coding conventions require Bun 1.x runtime with zero runtime dependencies (devDeps only), strict TypeScript, lib/<feature>.ts module separation, vitest-API tests in __tests__/, and no direct console.log. -- evidence: [CONTRIBUTING.md#L29-L35](https://github.com/choiyounggi/cliclaw/blob/6a5e048a5abf41dc7a94285f67def78b3637e5e3/CONTRIBUTING.md#L29-L35) (`clm_55ea977c16de5557918064215e91782372e37ac200758c90d22974476d25a55c`)
- [observation/documented] Repository development practice: releases are made by npm version bump, pushing tags, and publishing a GitHub release, which triggers publish.yml to npm publish after verifying the tag matches package.json version. -- evidence: [README.md#L324-L327](https://github.com/choiyounggi/cliclaw/blob/6a5e048a5abf41dc7a94285f67def78b3637e5e3/README.md#L324-L327), [README.md#L318-L318](https://github.com/choiyounggi/cliclaw/blob/6a5e048a5abf41dc7a94285f67def78b3637e5e3/README.md#L318-L318) (`clm_bad0c7b2c258d4ed4fd5e7b26ee6d8538f44048c537c6fe9eb58c6241c60201c`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The product exposes CLI commands including init, start, install-launchd, uninstall-launchd, upgrade, version, logs (--audit/--err), doctor, and help. -- evidence: [README.md#L113-L123](https://github.com/choiyounggi/cliclaw/blob/6a5e048a5abf41dc7a94285f67def78b3637e5e3/README.md#L113-L123) (`clm_81c31614b9fb5fb724525e934646fdde8bf6d8b02f40600a922824656463243c`)
- [observation/documented] In Telegram, slash commands switch the active agent, show status/health, stop jobs, reset sessions, toggle safety, set model overrides, and toggle Claude plan mode; other text or photos are sent as prompts. -- evidence: [README.md#L127-L140](https://github.com/choiyounggi/cliclaw/blob/6a5e048a5abf41dc7a94285f67def78b3637e5e3/README.md#L127-L140) (`clm_ec9ec23e0b1fb679bb5705f9b9a5fe12c17002427d51c62a37defbeb7df2e047`)

## memory-state (1 claim(s))

- [observation/documented] All state lives under ~/.cliclaw/ (relocatable via CLICLAW_HOME): config.json, a bot.pid single-instance lock, safety.json, per-chat session metadata and per-agent session directories, logs, and a .sock confirm-gate IPC socket. -- evidence: [README.md#L167-L167](https://github.com/choiyounggi/cliclaw/blob/6a5e048a5abf41dc7a94285f67def78b3637e5e3/README.md#L167-L167), [README.md#L147-L147](https://github.com/choiyounggi/cliclaw/blob/6a5e048a5abf41dc7a94285f67def78b3637e5e3/README.md#L147-L147), [README.md#L149-L165](https://github.com/choiyounggi/cliclaw/blob/6a5e048a5abf41dc7a94285f67def78b3637e5e3/README.md#L149-L165) (`clm_ce16b8dd6be5209e248cd85ecf067aaceb2c9648eca37e77aa3336e1031ecf1b`)

## orchestration (1 claim(s))

- [observation/documented] The daemon is built for unattended operation: single-instance lock, dormant retry every 60s on broken config instead of crash looping, graceful shutdown notifying chats, process-group kills on /stop, and retention sweeps of stale uploads/sessions (default 30 days). -- evidence: [README.md#L236-L245](https://github.com/choiyounggi/cliclaw/blob/6a5e048a5abf41dc7a94285f67def78b3637e5e3/README.md#L236-L245) (`clm_8524e624e31fdec7c73db44fe6d1b8179fc6367680ca86064c133ed74d9177a9`)

## tools-permissions (2 claim(s))

- [observation/documented] Safety mode (on by default) re-confirms dangerous Bash commands via Telegram inline Allow/Deny buttons, auto-denies on no response, and denies Claude reads of sensitive files like ~/.ssh and .env; custom regexes can be added. -- evidence: [README.md#L184-L187](https://github.com/choiyounggi/cliclaw/blob/6a5e048a5abf41dc7a94285f67def78b3637e5e3/README.md#L184-L187) (`clm_4d70ba6a4833b67b5c534f24b6c670bf0f3c1c0c507d7d1e55be5ab25eaefcc8`)
- [observation/documented] Per-agent headless policies: Claude runs with bypassPermissions (plan mode optional), Codex defaults to workspace-write sandbox, Pi uses default mode, and Gemini defaults to auto_edit approvalMode without confirm-gate integration. -- evidence: [README.md#L208-L211](https://github.com/choiyounggi/cliclaw/blob/6a5e048a5abf41dc7a94285f67def78b3637e5e3/README.md#L208-L211) (`clm_d509676e2b8a7e1886e59291c4a9515035cb36d0404d3bb6ea8422b035157bd6`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The product requires Bun 1.x on macOS and at least one installed, authenticated coding CLI; it spawns those CLIs as child processes and is published as the npm package @younggichoi/cliclaw. -- evidence: [README.md#L58-L59](https://github.com/choiyounggi/cliclaw/blob/6a5e048a5abf41dc7a94285f67def78b3637e5e3/README.md#L58-L59), [README.md#L55-L55](https://github.com/choiyounggi/cliclaw/blob/6a5e048a5abf41dc7a94285f67def78b3637e5e3/README.md#L55-L55), [README.md#L43-L49](https://github.com/choiyounggi/cliclaw/blob/6a5e048a5abf41dc7a94285f67def78b3637e5e3/README.md#L43-L49) (`clm_6b0f6bfd8f09cffcf262b1cdfd8c96dcedfa65f4ca9c8ddfb420e2c012e49244`)

## limitations (1 claim(s))

- [observation/documented] Documented limits: regex-based danger classification is imperfect, no body-text streaming for Codex/Pi/Gemini, Gemini lacks confirm-gate integration, photos only (no voice/files), one concurrent job per chat, 1:1 chats only, and macOS only. -- evidence: [README.md#L299-L306](https://github.com/choiyounggi/cliclaw/blob/6a5e048a5abf41dc7a94285f67def78b3637e5e3/README.md#L299-L306) (`clm_ddf1ac5184967454f4261cf8e61e148a934ab6b3041f037512d3fb8f3766d1b1`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

