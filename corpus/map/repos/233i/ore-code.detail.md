# 233i/ore-code -- full detail

[Back to orientation](ore-code.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/233i/ore-code/b36da0c05720cd033af68bdda75bb79acc5c5010/f358b98138f19402.json](../../../wiki/dossiers/233i/ore-code/b36da0c05720cd033af68bdda75bb79acc5c5010/f358b98138f19402.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The product combines a TypeScript agent runtime, a React/Tauri desktop app, and a Rust OS boundary handling local file, shell, process, Git, keychain, artifact, and MCP operations. -- evidence: [README.md#L36-L36](https://github.com/233i/ore-code/blob/b36da0c05720cd033af68bdda75bb79acc5c5010/README.md#L36-L36) (`clm_5e9a4abb38fbb022c3f0df4f8ac59f39754a0c63292f71b953c29492e9db0671`)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributors use Node 22 (pinned in .node-version), pnpm 11.x, Rust stable, and Tauri 2 prerequisites; local checks run via pnpm ci:local plus per-package test/typecheck/lint filters. -- evidence: [README.md#L106-L109](https://github.com/233i/ore-code/blob/b36da0c05720cd033af68bdda75bb79acc5c5010/README.md#L106-L109), [docs/API_AND_COMPATIBILITY.md#L92-L95](https://github.com/233i/ore-code/blob/b36da0c05720cd033af68bdda75bb79acc5c5010/docs/API_AND_COMPATIBILITY.md#L92-L95), [README.md#L91-L95](https://github.com/233i/ore-code/blob/b36da0c05720cd033af68bdda75bb79acc5c5010/README.md#L91-L95), [docs/API_AND_COMPATIBILITY.md#L97-L97](https://github.com/233i/ore-code/blob/b36da0c05720cd033af68bdda75bb79acc5c5010/docs/API_AND_COMPATIBILITY.md#L97-L97) (`clm_c14e7f109651ea3e49cff611ddc04cb7cde8f774ee49df32be11ebec6d009c7c`)

## skills-patterns (2 claim(s))

- [observation/documented] Skills are user-level reusable workflow instructions stored at ~/.ore-code/skills/<skill-id>/SKILL.md; each skill auto-registers a slash command and its content is injected into the current prompt. -- evidence: [docs/06-skill-system.md#L7-L9](https://github.com/233i/ore-code/blob/b36da0c05720cd033af68bdda75bb79acc5c5010/docs/06-skill-system.md#L7-L9), [docs/06-skill-system.md#L24-L24](https://github.com/233i/ore-code/blob/b36da0c05720cd033af68bdda75bb79acc5c5010/docs/06-skill-system.md#L24-L24), [docs/06-skill-system.md#L3-L3](https://github.com/233i/ore-code/blob/b36da0c05720cd033af68bdda75bb79acc5c5010/docs/06-skill-system.md#L3-L3), [docs/06-skill-system.md#L30-L30](https://github.com/233i/ore-code/blob/b36da0c05720cd033af68bdda75bb79acc5c5010/docs/06-skill-system.md#L30-L30) (`clm_9f339a154cef17c117c94f754284d95930942068fa1df8146c525fa2b1710aa4`)
- [observation/documented] Skills are documentation-like instructions, not plugin code, and do not execute arbitrary scripts; actual file, shell, and git actions still go through existing tools and the approval system. -- evidence: [docs/06-skill-system.md#L3-L3](https://github.com/233i/ore-code/blob/b36da0c05720cd033af68bdda75bb79acc5c5010/docs/06-skill-system.md#L3-L3), [docs/06-skill-system.md#L30-L30](https://github.com/233i/ore-code/blob/b36da0c05720cd033af68bdda75bb79acc5c5010/docs/06-skill-system.md#L30-L30) (`clm_b0b688b5223542f70b6e1affc3ef31aa9e227600fad64d59f97e4e36264da7cd`)

## interfaces (2 claim(s))

- [observation/documented] The workspace includes packages for protocol event schemas, tool specs with approval policy, agent engine with model adapters, JSONL session/artifact state storage, and a scenario-replay harness. -- evidence: [docs/API_AND_COMPATIBILITY.md#L7-L14](https://github.com/233i/ore-code/blob/b36da0c05720cd033af68bdda75bb79acc5c5010/docs/API_AND_COMPATIBILITY.md#L7-L14), [README.md#L76-L85](https://github.com/233i/ore-code/blob/b36da0c05720cd033af68bdda75bb79acc5c5010/README.md#L76-L85) (`clm_b8b92e706647bc2da089c036db9800cd51594a2cea2e1193fd673d4bb526f71b`)
- [observation/documented] Runtime events are designed to be append-only from a reader's perspective, with new event types added in the protocol package first and older sessions expected to load when optional fields are missing. -- evidence: [docs/API_AND_COMPATIBILITY.md#L36-L39](https://github.com/233i/ore-code/blob/b36da0c05720cd033af68bdda75bb79acc5c5010/docs/API_AND_COMPATIBILITY.md#L36-L39), [docs/API_AND_COMPATIBILITY.md#L34-L34](https://github.com/233i/ore-code/blob/b36da0c05720cd033af68bdda75bb79acc5c5010/docs/API_AND_COMPATIBILITY.md#L34-L34) (`clm_38f589340cab9f702f267afa51b4abc3e707adcfb205437a7506c0a4ff3efb48`)

## memory-state (1 claim(s))

- [observation/documented] The agent offers context-control features including history compression, context briefing, checkpoint summaries, usage visibility, and provider-aware request shaping for long conversations. -- evidence: [README.md#L42-L44](https://github.com/233i/ore-code/blob/b36da0c05720cd033af68bdda75bb79acc5c5010/README.md#L42-L44) (`clm_faca359b6c675c559e5b0a3f9006150f49ad43feb988e541c7580caf4f9c42c3`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] The runtime can execute local tools such as Git, shell/process commands, tests, diagnostics, code execution, and MCP servers when the user permits them, with an approval system meant to surface higher-risk actions. -- evidence: [PRIVACY.md#L39-L39](https://github.com/233i/ore-code/blob/b36da0c05720cd033af68bdda75bb79acc5c5010/PRIVACY.md#L39-L39), [PRIVACY.md#L41-L41](https://github.com/233i/ore-code/blob/b36da0c05720cd033af68bdda75bb79acc5c5010/PRIVACY.md#L41-L41) (`clm_f83c4e30d05255870a6a39cce0a2acf884639bc2c1452bba197111ef51b3d964`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Configuration supports DeepSeek, Mimo, Ark Coding, or custom endpoints via ~/.ore-code/config.toml, with API keys kept in the OS keychain and user-level MCP servers in ~/.ore-code/mcp.json. -- evidence: [README.md#L46-L48](https://github.com/233i/ore-code/blob/b36da0c05720cd033af68bdda75bb79acc5c5010/README.md#L46-L48), [README.md#L122-L124](https://github.com/233i/ore-code/blob/b36da0c05720cd033af68bdda75bb79acc5c5010/README.md#L122-L124) (`clm_3a4502f9d5bb5014aa1a41046bcf33e64185419b3ca075cdbfad23d58d5e87f4`)

## limitations (3 claim(s))

- [observation/documented] The current release does not read project-level .ore-code/config.toml files; only user-level configuration is supported. -- evidence: [README.md#L126-L126](https://github.com/233i/ore-code/blob/b36da0c05720cd033af68bdda75bb79acc5c5010/README.md#L126-L126) (`clm_5cde1f24e4b81236bf9bb3d9e5e815fd601cbcb5e325cc05dcd459832bc8c489`)
- [observation/documented] The macOS build is ad-hoc signed and not notarized because the project does not yet use an Apple Developer ID certificate, so macOS may block the app on first launch. -- evidence: [README.md#L63-L63](https://github.com/233i/ore-code/blob/b36da0c05720cd033af68bdda75bb79acc5c5010/README.md#L63-L63) (`clm_c7582ede32b4a53f771a0d589cdfafe6f08f504879d23c78bba42508b7bc2710`)
- [observation/documented] The shipped release provides a macOS Apple Silicon installer; the Windows x64 build is listed as pending and must be built separately in a Windows environment. -- evidence: [README.md#L46-L48](https://github.com/233i/ore-code/blob/b36da0c05720cd033af68bdda75bb79acc5c5010/README.md#L46-L48), [README.md#L54-L57](https://github.com/233i/ore-code/blob/b36da0c05720cd033af68bdda75bb79acc5c5010/README.md#L54-L57) (`clm_b8ae567a59542113674b21e6503fa4e46a708c65bb185c3d19d64cdb2a1d4fbc`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

