# echovic/blade-code -- full detail

[Back to orientation](blade-code.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/echovic/blade-code/8917e4e0ef6112f3cd47314e45c898284e99fd86/4784f9b274c8ce01.json](../../../wiki/dossiers/echovic/blade-code/8917e4e0ef6112f3cd47314e45c898284e99fd86/4784f9b274c8ce01.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The repository layout places the agent core and execution loop in packages/cli/src/agent, the pi-ai adapter in services/pi, a TypeBox-based tool system, a Hono web server, and a React+Vite web UI. -- evidence: [README.md#L130-L145](https://github.com/echoVic/blade-code/blob/8917e4e0ef6112f3cd47314e45c898284e99fd86/README.md#L130-L145) (`clm_8d60816fe7a3c7c586d50d095029cd8d434adea918445aa4b9662b93ee352a5d`)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributors clone the repo and run 'bun install && bun run dev' to develop locally, and a CONTRIBUTING.md guide is referenced. -- evidence: [README.md#L7-L10](https://github.com/echoVic/blade-code/blob/8917e4e0ef6112f3cd47314e45c898284e99fd86/README.md#L7-L10), [README.md#L160-L163](https://github.com/echoVic/blade-code/blob/8917e4e0ef6112f3cd47314e45c898284e99fd86/README.md#L160-L163) (`clm_f2ee48ade199175ce7a65363c17f2a84e0440065382924263e8e339f0e193de8`)

## skills-patterns (1 claim(s))

- [observation/documented] Skills are described as a dynamic prompt extension mechanism that lets the AI automatically invoke specialized capabilities based on user requests. -- evidence: [docs/guides/skills.md#L3-L3](https://github.com/echoVic/blade-code/blob/8917e4e0ef6112f3cd47314e45c898284e99fd86/docs/guides/skills.md#L3-L3) (`clm_fc2e3d1ae7a9eb33814956c7638799d84107c262fe66a3718b7be1b250a62f2f`)

## interfaces (2 claim(s))

- [observation/documented] The product ships as an interactive CLI ('blade'), a Web UI ('blade web'), a headless HTTP server ('blade serve'), non-interactive modes '--headless' with JSONL output, and a single-turn '--print' mode. -- evidence: [README.md#L101-L111](https://github.com/echoVic/blade-code/blob/8917e4e0ef6112f3cd47314e45c898284e99fd86/README.md#L101-L111), [README.md#L69-L70](https://github.com/echoVic/blade-code/blob/8917e4e0ef6112f3cd47314e45c898284e99fd86/README.md#L69-L70) (`clm_31614ee8d45f114e1f5cfd704bfde4cf8aff960ddd190bad2d3339953db9b9e9`)
- [observation/documented] In-session slash commands include /model add and /model switch, /cost, /compact, /btw for side questions, /memory list, /tasks, and /goal to start Goal mode. -- evidence: [README.md#L115-L124](https://github.com/echoVic/blade-code/blob/8917e4e0ef6112f3cd47314e45c898284e99fd86/README.md#L115-L124) (`clm_56362f1b1d86421c033df958698df75f390bad0c74f09e68a7484887539641ba`)

## memory-state (5 claim(s))

- [observation/documented] Auto Memory persists project knowledge across sessions: the first 200 lines of MEMORY.md are injected into the system prompt at session start, knowledge is saved via MemoryWrite, and read on demand via MemoryRead. -- evidence: [docs/en/guides/memory.md#L3-L3](https://github.com/echoVic/blade-code/blob/8917e4e0ef6112f3cd47314e45c898284e99fd86/docs/en/guides/memory.md#L3-L3), [docs/guides/memory.md#L7-L10](https://github.com/echoVic/blade-code/blob/8917e4e0ef6112f3cd47314e45c898284e99fd86/docs/guides/memory.md#L7-L10) (`clm_097d52dc731c2067688fce6326641425aee963780a6113d91f017f50460fc29b`)
- [observation/documented] Memory files live under ~/.blade/projects/{escaped-path}/memory/ with per-project isolation, containing a MEMORY.md index plus topic files such as patterns.md, debugging.md, and architecture.md. -- evidence: [docs/en/guides/memory.md#L54-L54](https://github.com/echoVic/blade-code/blob/8917e4e0ef6112f3cd47314e45c898284e99fd86/docs/en/guides/memory.md#L54-L54), [docs/guides/memory.md#L42-L49](https://github.com/echoVic/blade-code/blob/8917e4e0ef6112f3cd47314e45c898284e99fd86/docs/guides/memory.md#L42-L49) (`clm_976351d3841cf1ad125995382e27520cf79dcf3f83d8ece9dde30b8470177012`)
- [observation/documented] Full compaction extracts explicitly marked entries (remember:, convention:, lesson:, fixed:) into topic files, capped at 20 entries, 500 code points each, 8,000 total, with deduplication, in-process and file locks, atomic replacement, and 0600 permissions. -- evidence: [docs/guides/memory.md#L27-L31](https://github.com/echoVic/blade-code/blob/8917e4e0ef6112f3cd47314e45c898284e99fd86/docs/guides/memory.md#L27-L31), [docs/guides/memory.md#L33-L36](https://github.com/echoVic/blade-code/blob/8917e4e0ef6112f3cd47314e45c898284e99fd86/docs/guides/memory.md#L33-L36), [docs/en/guides/memory.md#L34-L39](https://github.com/echoVic/blade-code/blob/8917e4e0ef6112f3cd47314e45c898284e99fd86/docs/en/guides/memory.md#L34-L39) (`clm_54af29809cd6886c86c2654963fe36ffaa75e34b4d862fbcb7bdf9d231fc959c`)
- [observation/documented] Memory safety mechanisms include rejecting credential-like content (password, token, sk-*, AWS key IDs, PEM headers), forbidding '..' or '/' in topic names, and content-free projections so TUI/Web/ACP/Headless receive only outcome, entry count, and topic names. -- evidence: [docs/guides/memory.md#L63-L71](https://github.com/echoVic/blade-code/blob/8917e4e0ef6112f3cd47314e45c898284e99fd86/docs/guides/memory.md#L63-L71), [docs/en/guides/memory.md#L66-L75](https://github.com/echoVic/blade-code/blob/8917e4e0ef6112f3cd47314e45c898284e99fd86/docs/en/guides/memory.md#L66-L75) (`clm_94b1a84daf77ef3fbb376bb8c700084eb42cd3f20287f81060ee0ad603def074`)
- [observation/documented] Auto Memory can be disabled with BLADE_AUTO_MEMORY=0; the documented default is enabled (BLADE_AUTO_MEMORY=1). -- evidence: [docs/en/guides/memory.md#L120-L120](https://github.com/echoVic/blade-code/blob/8917e4e0ef6112f3cd47314e45c898284e99fd86/docs/en/guides/memory.md#L120-L120), [docs/guides/memory.md#L116-L116](https://github.com/echoVic/blade-code/blob/8917e4e0ef6112f3cd47314e45c898284e99fd86/docs/guides/memory.md#L116-L116), [docs/en/guides/memory.md#L123-L124](https://github.com/echoVic/blade-code/blob/8917e4e0ef6112f3cd47314e45c898284e99fd86/docs/en/guides/memory.md#L123-L124), [docs/guides/memory.md#L119-L120](https://github.com/echoVic/blade-code/blob/8917e4e0ef6112f3cd47314e45c898284e99fd86/docs/guides/memory.md#L119-L120) (`clm_c0566dab291991e25532c6b552c071fd876eb1e22ab3a9b3fa70101d7287e1c1`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (4 claim(s))

- [observation/documented] The runtime offers four permission modes (default, autoEdit, plan, yolo); Shift+Tab cycles the first three in the TUI, while yolo requires an explicit command, launch argument, or setting. -- evidence: [docs/en/configuration/permissions.md#L17-L18](https://github.com/echoVic/blade-code/blob/8917e4e0ef6112f3cd47314e45c898284e99fd86/docs/en/configuration/permissions.md#L17-L18), [docs/configuration/permissions.md#L17-L18](https://github.com/echoVic/blade-code/blob/8917e4e0ef6112f3cd47314e45c898284e99fd86/docs/configuration/permissions.md#L17-L18) (`clm_1e9b4a1f8073d7f2ea1b51736a8a23674daacae454333973dc5e4ea907efed5d`)
- [observation/documented] Permission rules use Tool(param:value) syntax with picomatch * and ** wildcards, evaluated in order deny > allow > ask > default (ask), covering file paths, Bash commands, and WebFetch/WebSearch URL patterns. -- evidence: [docs/en/configuration/permissions.md#L131-L143](https://github.com/echoVic/blade-code/blob/8917e4e0ef6112f3cd47314e45c898284e99fd86/docs/en/configuration/permissions.md#L131-L143), [docs/en/configuration/permissions.md#L13-L13](https://github.com/echoVic/blade-code/blob/8917e4e0ef6112f3cd47314e45c898284e99fd86/docs/en/configuration/permissions.md#L13-L13), [docs/en/configuration/permissions.md#L67-L84](https://github.com/echoVic/blade-code/blob/8917e4e0ef6112f3cd47314e45c898284e99fd86/docs/en/configuration/permissions.md#L67-L84), [docs/en/configuration/permissions.md#L65-L65](https://github.com/echoVic/blade-code/blob/8917e4e0ef6112f3cd47314e45c898284e99fd86/docs/en/configuration/permissions.md#L65-L65) (`clm_b6afab1e67a0dbdef4bb09a92a7b3dad69c815b14b93c8d8e84b2fe246e4f4a2`)
- [observation/documented] When a rule resolves to ask, a confirmation dialog offers Once/Session/Project/Deny; Session authorizations live only in runtime memory and expire with the session, while Project writes the rule to .blade/settings.local.json. -- evidence: [docs/en/configuration/permissions.md#L163-L164](https://github.com/echoVic/blade-code/blob/8917e4e0ef6112f3cd47314e45c898284e99fd86/docs/en/configuration/permissions.md#L163-L164), [docs/en/configuration/permissions.md#L151-L159](https://github.com/echoVic/blade-code/blob/8917e4e0ef6112f3cd47314e45c898284e99fd86/docs/en/configuration/permissions.md#L151-L159), [docs/en/configuration/permissions.md#L168-L168](https://github.com/echoVic/blade-code/blob/8917e4e0ef6112f3cd47314e45c898284e99fd86/docs/en/configuration/permissions.md#L168-L168) (`clm_d3915434ca37350a01dd12891fc7cf3cc2da35a40846decc6a922a366962f851`)
- [observation/documented] A maxTurns setting caps model rounds (0 disables, -1 unlimited, N>0 limits); recovery paths such as output-length correction, Stop hooks, and mid-turn input cannot bypass it, and non-interactive callers without a continuation callback receive max_turns_exceeded. -- evidence: [docs/en/configuration/permissions.md#L217-L217](https://github.com/echoVic/blade-code/blob/8917e4e0ef6112f3cd47314e45c898284e99fd86/docs/en/configuration/permissions.md#L217-L217), [docs/en/configuration/permissions.md#L215-L215](https://github.com/echoVic/blade-code/blob/8917e4e0ef6112f3cd47314e45c898284e99fd86/docs/en/configuration/permissions.md#L215-L215), [docs/en/configuration/permissions.md#L211-L213](https://github.com/echoVic/blade-code/blob/8917e4e0ef6112f3cd47314e45c898284e99fd86/docs/en/configuration/permissions.md#L211-L213) (`clm_688557c894870f0a0af1d0b7298c49ddf2b214c57287e5eacd675ecb1a47a8b6`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The runtime uses the pi-ai library to unify 38+ model providers (OpenAI, Anthropic, DeepSeek, Google, Bedrock) with model metadata fetched dynamically from the pi-ai catalog. -- evidence: [README.md#L93-L95](https://github.com/echoVic/blade-code/blob/8917e4e0ef6112f3cd47314e45c898284e99fd86/README.md#L93-L95), [README.md#L34-L45](https://github.com/echoVic/blade-code/blob/8917e4e0ef6112f3cd47314e45c898284e99fd86/README.md#L34-L45) (`clm_9dc05de35934eee74b658c016c9fba0b0203167a8f5ae3bc948454c1814ce0c9`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

