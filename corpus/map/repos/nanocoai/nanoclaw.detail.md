# nanocoai/nanoclaw -- full detail

[Back to orientation](nanoclaw.md)

## Origins

- alltheagents.org-site-pages

## Projects

- Observatory

Full evidence record (JSON): [wiki/dossiers/nanocoai/nanoclaw/3f9ed607b7e7a4872747295f75286f1c377d7c33/2c4c789497c747f6.json](../../../wiki/dossiers/nanocoai/nanoclaw/3f9ed607b7e7a4872747295f75286f1c377d7c33/2c4c789497c747f6.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] A single Node host process routes messages through an entity model (user → messaging group → agent group → session), writes to the session's inbound.db, and wakes the container; the agent-runner inside polls inbound.db and writes responses to outbound.db. -- evidence: [README.md#L192-L192](https://github.com/nanocoai/nanoclaw/blob/3f9ed607b7e7a4872747295f75286f1c377d7c33/README.md#L192-L192), [docs/architecture.md#L41-L54](https://github.com/nanocoai/nanoclaw/blob/3f9ed607b7e7a4872747295f75286f1c377d7c33/docs/architecture.md#L41-L54) (`clm_b0512fa8f2a4e24a724468625dae4e1396e9841d5f0c833e633d2e64e78ee19b`)

## design-choices (2 claim(s))

- [observation/documented] Agents run in their own Linux/Docker containers with filesystem isolation, so bash commands execute inside the container rather than on the host, and only explicitly mounted directories are visible. -- evidence: [README.md#L223-L223](https://github.com/nanocoai/nanoclaw/blob/3f9ed607b7e7a4872747295f75286f1c377d7c33/README.md#L223-L223), [README.md#L38-L38](https://github.com/nanocoai/nanoclaw/blob/3f9ed607b7e7a4872747295f75286f1c377d7c33/README.md#L38-L38), [README.md#L77-L77](https://github.com/nanocoai/nanoclaw/blob/3f9ed607b7e7a4872747295f75286f1c377d7c33/README.md#L77-L77), [README.md#L91-L98](https://github.com/nanocoai/nanoclaw/blob/3f9ed607b7e7a4872747295f75286f1c377d7c33/README.md#L91-L98) (`clm_d2866fc2a317926ad5a529b800892795ec60cba25fe09f6ac154b8290e0332ca`)
- [observation/documented] The project deliberately avoids configuration files; customization is done by asking Claude Code to modify the small codebase, or via a guided /customize command. -- evidence: [README.md#L227-L227](https://github.com/nanocoai/nanoclaw/blob/3f9ed607b7e7a4872747295f75286f1c377d7c33/README.md#L227-L227), [README.md#L156-L156](https://github.com/nanocoai/nanoclaw/blob/3f9ed607b7e7a4872747295f75286f1c377d7c33/README.md#L156-L156), [README.md#L163-L163](https://github.com/nanocoai/nanoclaw/blob/3f9ed607b7e7a4872747295f75286f1c377d7c33/README.md#L163-L163) (`clm_28579e58674e33a6e8f89efc1cc0252bfa4cfd45fdc96b1a136e1d1e17113835`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributions to the base are limited to security fixes, bug fixes, and clear improvements; new capabilities must be contributed as skills on the channels/providers branches or as self-contained skills, per CONTRIBUTING.md. -- evidence: [README.md#L258-L258](https://github.com/nanocoai/nanoclaw/blob/3f9ed607b7e7a4872747295f75286f1c377d7c33/README.md#L258-L258), [README.md#L260-L260](https://github.com/nanocoai/nanoclaw/blob/3f9ed607b7e7a4872747295f75286f1c377d7c33/README.md#L260-L260) (`clm_c3b585fce0a4bdfafe1446200faa88091e102ee59c7b5329d22b494bb9ea2f39`)

## skills-patterns (1 claim(s))

- [observation/documented] Trunk ships only the registry and infrastructure; channel adapters and alternative providers live on long-lived channels/providers branches and are installed into a user's fork via /add-<name> skills that copy modules, wire registration, and pin dependencies. -- evidence: [README.md#L85-L85](https://github.com/nanocoai/nanoclaw/blob/3f9ed607b7e7a4872747295f75286f1c377d7c33/README.md#L85-L85), [README.md#L171-L171](https://github.com/nanocoai/nanoclaw/blob/3f9ed607b7e7a4872747295f75286f1c377d7c33/README.md#L171-L171) (`clm_7fe1e3da4664ce173ee2ee745448164f9e13daaf3af7559af2ed9735b99e7484`)

## interfaces (2 claim(s))

- [observation/documented] Channel adapters return platform channel and thread IDs without knowing agent-group or session IDs; the host maps those to the entity model, and session mode (shared vs per-thread) is configured per channel. -- evidence: [docs/architecture.md#L66-L66](https://github.com/nanocoai/nanoclaw/blob/3f9ed607b7e7a4872747295f75286f1c377d7c33/docs/architecture.md#L66-L66), [docs/architecture.md#L68-L71](https://github.com/nanocoai/nanoclaw/blob/3f9ed607b7e7a4872747295f75286f1c377d7c33/docs/architecture.md#L68-L71) (`clm_0a9999bbecfbc32b5ad876ad92b8f80df1c1c23a3cb02262cdde6bcfe8d6b913`)
- [observation/documented] Outbound file delivery is tool-based: the agent calls a dedicated send_file MCP tool, the runner stages files in an outbox directory per messages_out row, messages_out references filenames only, and the host delivers and cleans up after delivery. -- evidence: [docs/architecture.md#L191-L191](https://github.com/nanocoai/nanoclaw/blob/3f9ed607b7e7a4872747295f75286f1c377d7c33/docs/architecture.md#L191-L191), [docs/architecture.md#L175-L175](https://github.com/nanocoai/nanoclaw/blob/3f9ed607b7e7a4872747295f75286f1c377d7c33/docs/architecture.md#L175-L175), [docs/architecture.md#L193-L193](https://github.com/nanocoai/nanoclaw/blob/3f9ed607b7e7a4872747295f75286f1c377d7c33/docs/architecture.md#L193-L193) (`clm_ca771bd2d75b19d4e5bd756e879dc1671c48ed1ebbffa94ae91b3d99a80670b1`)

## memory-state (2 claim(s))

- [observation/documented] Each session has a pair of mounted SQLite files as the only host-container IO mechanism: inbound.db (host-written, container read-only) and outbound.db (container-written), each with exactly one writer and journal_mode=DELETE rather than WAL. -- evidence: [docs/architecture.md#L12-L17](https://github.com/nanocoai/nanoclaw/blob/3f9ed607b7e7a4872747295f75286f1c377d7c33/docs/architecture.md#L12-L17), [docs/architecture.md#L7-L10](https://github.com/nanocoai/nanoclaw/blob/3f9ed607b7e7a4872747295f75286f1c377d7c33/docs/architecture.md#L7-L10) (`clm_a2cfc3d5e8b5fad6be3ea1ade00ae9e126b3ff59a102c5e335d9b7bb92917470`)
- [observation/documented] Message sequence numbers use disjoint parity — even seqs written by the host in messages_in, odd by the container in messages_out — forming a single monotonic id across both tables. -- evidence: [docs/architecture.md#L201-L206](https://github.com/nanocoai/nanoclaw/blob/3f9ed607b7e7a4872747295f75286f1c377d7c33/docs/architecture.md#L201-L206) (`clm_ac85fef8ab0b3c532266b493b6cbacd14a03c5af010738ce47bc22edfb44fd33`)

## orchestration (1 claim(s))

- [observation/documented] The host acts as orchestrator: it spawns containers on wakeUpAgent when none exists, kills idle containers after a timeout, and runs a ~60s sweep for stale detection, due-message wake, delivery, and recurrence insertion. -- evidence: [docs/architecture.md#L269-L273](https://github.com/nanocoai/nanoclaw/blob/3f9ed607b7e7a4872747295f75286f1c377d7c33/docs/architecture.md#L269-L273), [docs/architecture.md#L143-L145](https://github.com/nanocoai/nanoclaw/blob/3f9ed607b7e7a4872747295f75286f1c377d7c33/docs/architecture.md#L143-L145) (`clm_835405c6e6d8fa3adf1c998bdc9deffa9583ea1094a2bc657f7500bc30cf8bb4`)

## tools-permissions (1 claim(s))

- [observation/documented] Agents never hold raw API keys; outbound requests route through OneCLI's Agent Vault, which injects credentials at request time and enforces per-agent policies and rate limits. -- evidence: [README.md#L223-L223](https://github.com/nanocoai/nanoclaw/blob/3f9ed607b7e7a4872747295f75286f1c377d7c33/README.md#L223-L223), [README.md#L91-L98](https://github.com/nanocoai/nanoclaw/blob/3f9ed607b7e7a4872747295f75286f1c377d7c33/README.md#L91-L98) (`clm_03711d486d1699152d9c7c0c9caf5820a30a3f0bcca9ea4f7e460650be1b4408`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Requirements are macOS or Linux (Windows via WSL2), Node.js 22+, pnpm 10+, Docker, and Claude Code for /customize, /debug, setup error recovery, and /add-<channel> skills; the installer installs Node and pnpm if missing. -- evidence: [README.md#L181-L184](https://github.com/nanocoai/nanoclaw/blob/3f9ed607b7e7a4872747295f75286f1c377d7c33/README.md#L181-L184), [README.md#L48-L48](https://github.com/nanocoai/nanoclaw/blob/3f9ed607b7e7a4872747295f75286f1c377d7c33/README.md#L48-L48) (`clm_0c69316f38b290f83bf63f84a1148423f8cd56b9cc4947362696e3ad1dac316c`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

