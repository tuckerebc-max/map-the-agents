# openinterpreter/openinterpreter -- full detail

[Back to orientation](openinterpreter.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/openinterpreter/openinterpreter/860153a5318d54e91111af2699136540cf4fc610/5584e08deae693c9.json](../../../wiki/dossiers/openinterpreter/openinterpreter/860153a5318d54e91111af2699136540cf4fc610/5584e08deae693c9.json)

## specifications (1 claim(s))

- [observation/documented] The project describes itself as a fork of OpenAI's Codex focused on emulating the agent harness that gets the best performance from low-cost models. -- evidence: [README.md#L47-L47](https://github.com/openinterpreter/openinterpreter/blob/860153a5318d54e91111af2699136540cf4fc610/README.md#L47-L47) (`clm_502e0bfc07f58f526d8ac2b2cba4799bb0ecc9cba616da1ea02a97b05b7fceae`)

## components (1 claim(s))

- [observation/documented] The product ships a QA skill that can drive web apps in a real browser via agent-browser or operate native apps via trycua. -- evidence: [README.md#L101-L101](https://github.com/openinterpreter/openinterpreter/blob/860153a5318d54e91111af2699136540cf4fc610/README.md#L101-L101) (`clm_d7b9486e6cfb860a0f62c3d700c971b7ec5e17eacb747a04c55a7a45fc91422a`)

## design-choices (1 claim(s))

- [observation/documented] Portability is a stated product goal: shared AGENTS.md, `.agents/skills` directories, MCP, ACP, and the Codex exec protocol are preferred, with `~/.openinterpreter` reserved for config and runtime state lacking shared standards. -- evidence: [README.md#L89-L94](https://github.com/openinterpreter/openinterpreter/blob/860153a5318d54e91111af2699136540cf4fc610/README.md#L89-L94), [README.md#L84-L87](https://github.com/openinterpreter/openinterpreter/blob/860153a5318d54e91111af2699136540cf4fc610/README.md#L84-L87) (`clm_239abd2d6b9914731550e176c18fb836cb84912c972f099379828ef1a7bb66ce`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: provider and model membership is generated rather than maintained as Rust lists, refreshed from `codex-rs` with `python3 scripts/write_provider_catalog.py`, and a `scripts/test-codex-sdk-compat.sh` script provides a local provider-free compatibility check. -- evidence: [README.md#L134-L139](https://github.com/openinterpreter/openinterpreter/blob/860153a5318d54e91111af2699136540cf4fc610/README.md#L134-L139), [README.md#L80-L80](https://github.com/openinterpreter/openinterpreter/blob/860153a5318d54e91111af2699136540cf4fc610/README.md#L80-L80) (`clm_7e8143552cce71c9bb0c6de3217ca379f828d8b4cb6a83c00de7e16fb27e8c66`)

## skills-patterns (1 claim(s))

- [observation/documented] Skills live in shared `.agents/skills` or `~/.agents/skills` directories; legacy product-specific skill directories remain readable for compatibility. -- evidence: [README.md#L89-L94](https://github.com/openinterpreter/openinterpreter/blob/860153a5318d54e91111af2699136540cf4fc610/README.md#L89-L94) (`clm_ed6d237a89577ba47c72a9369f169b5442a03bae9762ab3cfabe0596bd01de42`)

## interfaces (4 claim(s))

- [observation/documented] A `/harness` TUI command switches the active harness among listed modes including native, claude-code, kimi-code, qwen-code, deepseek-tui, swe-agent, and minimal. -- evidence: [README.md#L49-L49](https://github.com/openinterpreter/openinterpreter/blob/860153a5318d54e91111af2699136540cf4fc610/README.md#L49-L49), [README.md#L54-L64](https://github.com/openinterpreter/openinterpreter/blob/860153a5318d54e91111af2699136540cf4fc610/README.md#L54-L64), [README.md#L51-L52](https://github.com/openinterpreter/openinterpreter/blob/860153a5318d54e91111af2699136540cf4fc610/README.md#L51-L52) (`clm_f66d2049e19841f61aa7cd559f21a9b6523a74bacd502f945f740efe37036cef`)
- [observation/documented] The product runs as an Agent Client Protocol agent via `interpreter acp` and speaks the Codex exec protocol, allowing a one-line Codex SDK binary override to `interpreter`. -- evidence: [README.md#L70-L70](https://github.com/openinterpreter/openinterpreter/blob/860153a5318d54e91111af2699136540cf4fc610/README.md#L70-L70), [README.md#L72-L73](https://github.com/openinterpreter/openinterpreter/blob/860153a5318d54e91111af2699136540cf4fc610/README.md#L72-L73), [README.md#L80-L80](https://github.com/openinterpreter/openinterpreter/blob/860153a5318d54e91111af2699136540cf4fc610/README.md#L80-L80), [README.md#L75-L78](https://github.com/openinterpreter/openinterpreter/blob/860153a5318d54e91111af2699136540cf4fc610/README.md#L75-L78) (`clm_09ac983a39b4d65f13385126ea847a3ed2410dd8a2f86da2e62339d6adfb81d1`)
- [observation/documented] Installation is via a shell script on macOS/Linux and a PowerShell script on Windows; a session starts by typing `i` or `interpreter` in the terminal. -- evidence: [README.md#L33-L35](https://github.com/openinterpreter/openinterpreter/blob/860153a5318d54e91111af2699136540cf4fc610/README.md#L33-L35), [README.md#L43-L43](https://github.com/openinterpreter/openinterpreter/blob/860153a5318d54e91111af2699136540cf4fc610/README.md#L43-L43), [README.md#L31-L31](https://github.com/openinterpreter/openinterpreter/blob/860153a5318d54e91111af2699136540cf4fc610/README.md#L31-L31), [README.md#L37-L37](https://github.com/openinterpreter/openinterpreter/blob/860153a5318d54e91111af2699136540cf4fc610/README.md#L37-L37), [README.md#L39-L41](https://github.com/openinterpreter/openinterpreter/blob/860153a5318d54e91111af2699136540cf4fc610/README.md#L39-L41) (`clm_01b6ccd6ecf6c879cab94da94e4746db6ba95e6da55b89ada882dbce83cc8c4b`)
- [observation/documented] MCP servers are configured under `[mcp_servers]` supporting stdio commands and streamable HTTP servers via `url`, with per-server default tool approval modes. -- evidence: [docs/config.md#L185-L185](https://github.com/openinterpreter/openinterpreter/blob/860153a5318d54e91111af2699136540cf4fc610/docs/config.md#L185-L185), [docs/config.md#L177-L183](https://github.com/openinterpreter/openinterpreter/blob/860153a5318d54e91111af2699136540cf4fc610/docs/config.md#L177-L183), [docs/config.md#L187-L191](https://github.com/openinterpreter/openinterpreter/blob/860153a5318d54e91111af2699136540cf4fc610/docs/config.md#L187-L191), [docs/config.md#L175-L175](https://github.com/openinterpreter/openinterpreter/blob/860153a5318d54e91111af2699136540cf4fc610/docs/config.md#L175-L175) (`clm_1044290e3e54ffa96294ef734e6292c9db6720574e2542bf2b07d5be7f26ee19`)

## memory-state (1 claim(s))

- [observation/documented] AGENTS.md instructions are loaded from a global path (`~/.openinterpreter/AGENTS.md`) and project files from repo root to the current directory, with closer files taking precedence and a `project_doc_max_bytes` cap. -- evidence: [docs/agents_md.md#L30-L30](https://github.com/openinterpreter/openinterpreter/blob/860153a5318d54e91111af2699136540cf4fc610/docs/agents_md.md#L30-L30), [docs/agents_md.md#L52-L54](https://github.com/openinterpreter/openinterpreter/blob/860153a5318d54e91111af2699136540cf4fc610/docs/agents_md.md#L52-L54), [docs/agents_md.md#L32-L35](https://github.com/openinterpreter/openinterpreter/blob/860153a5318d54e91111af2699136540cf4fc610/docs/agents_md.md#L32-L35), [docs/agents_md.md#L37-L38](https://github.com/openinterpreter/openinterpreter/blob/860153a5318d54e91111af2699136540cf4fc610/docs/agents_md.md#L37-L38) (`clm_05dde6133be9fd587d66671183a2404cfec7e440b612a5d1c8769983ecd10b03`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (3 claim(s))

- [observation/documented] An execution policy labels each command as safe, unsafe, or forbid before it runs; forbid blocks outright, safe runs without prompting, and unsafe defers to the approval mode. -- evidence: [docs/execpolicy.md#L45-L47](https://github.com/openinterpreter/openinterpreter/blob/860153a5318d54e91111af2699136540cf4fc610/docs/execpolicy.md#L45-L47), [docs/execpolicy.md#L6-L7](https://github.com/openinterpreter/openinterpreter/blob/860153a5318d54e91111af2699136540cf4fc610/docs/execpolicy.md#L6-L7), [docs/execpolicy.md#L42-L43](https://github.com/openinterpreter/openinterpreter/blob/860153a5318d54e91111af2699136540cf4fc610/docs/execpolicy.md#L42-L43), [docs/execpolicy.md#L9-L13](https://github.com/openinterpreter/openinterpreter/blob/860153a5318d54e91111af2699136540cf4fc610/docs/execpolicy.md#L9-L13) (`clm_b53cc0e6518c4d47f6ba310d2a520907f1b717633cd63127d8bf0137f8844c62`)
- [observation/documented] Sandbox modes (read-only, workspace-write, danger-full-access) and approval policies (untrusted, on-request, never) are separate controls; OS enforcement uses Seatbelt on macOS and Bubblewrap/seccomp on Linux/WSL, failing closed when a policy cannot be enforced. -- evidence: [docs/sandbox.md#L83-L84](https://github.com/openinterpreter/openinterpreter/blob/860153a5318d54e91111af2699136540cf4fc610/docs/sandbox.md#L83-L84), [docs/sandbox.md#L15-L19](https://github.com/openinterpreter/openinterpreter/blob/860153a5318d54e91111af2699136540cf4fc610/docs/sandbox.md#L15-L19), [docs/sandbox.md#L77-L81](https://github.com/openinterpreter/openinterpreter/blob/860153a5318d54e91111af2699136540cf4fc610/docs/sandbox.md#L77-L81), [docs/sandbox.md#L74-L75](https://github.com/openinterpreter/openinterpreter/blob/860153a5318d54e91111af2699136540cf4fc610/docs/sandbox.md#L74-L75), [docs/sandbox.md#L6-L6](https://github.com/openinterpreter/openinterpreter/blob/860153a5318d54e91111af2699136540cf4fc610/docs/sandbox.md#L6-L6), [docs/sandbox.md#L35-L39](https://github.com/openinterpreter/openinterpreter/blob/860153a5318d54e91111af2699136540cf4fc610/docs/sandbox.md#L35-L39), [docs/sandbox.md#L8-L9](https://github.com/openinterpreter/openinterpreter/blob/860153a5318d54e91111af2699136540cf4fc610/docs/sandbox.md#L8-L9) (`clm_7e403e331726693a0b7735f24a9cc8b48413a32c41d5d46af13b4e5e6b23409f`)
- [observation/documented] Permission profiles offer finer-grained filesystem and network rules than sandbox_mode, including workspace roots, deny globs for secret files, per-domain network allow/deny, and Unix socket exceptions; network starts disabled. -- evidence: [docs/permissions.md#L111-L111](https://github.com/openinterpreter/openinterpreter/blob/860153a5318d54e91111af2699136540cf4fc610/docs/permissions.md#L111-L111), [docs/permissions.md#L37-L40](https://github.com/openinterpreter/openinterpreter/blob/860153a5318d54e91111af2699136540cf4fc610/docs/permissions.md#L37-L40), [docs/permissions.md#L51-L53](https://github.com/openinterpreter/openinterpreter/blob/860153a5318d54e91111af2699136540cf4fc610/docs/permissions.md#L51-L53), [docs/permissions.md#L80-L80](https://github.com/openinterpreter/openinterpreter/blob/860153a5318d54e91111af2699136540cf4fc610/docs/permissions.md#L80-L80), [docs/permissions.md#L13-L17](https://github.com/openinterpreter/openinterpreter/blob/860153a5318d54e91111af2699136540cf4fc610/docs/permissions.md#L13-L17), [docs/permissions.md#L45-L49](https://github.com/openinterpreter/openinterpreter/blob/860153a5318d54e91111af2699136540cf4fc610/docs/permissions.md#L45-L49), [docs/permissions.md#L6-L9](https://github.com/openinterpreter/openinterpreter/blob/860153a5318d54e91111af2699136540cf4fc610/docs/permissions.md#L6-L9) (`clm_e70cd037b6c851d649093a7e66fe0506d004c0e28859cf8e1c301c9fd2265797`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] Configuration is read from TOML files at user level (`~/.openinterpreter/config.toml`) and trusted project level (`.openinterpreter/config.toml`), with CLI `-c` overrides applying per invocation. -- evidence: [docs/config.md#L19-L19](https://github.com/openinterpreter/openinterpreter/blob/860153a5318d54e91111af2699136540cf4fc610/docs/config.md#L19-L19), [docs/config.md#L9-L11](https://github.com/openinterpreter/openinterpreter/blob/860153a5318d54e91111af2699136540cf4fc610/docs/config.md#L9-L11), [docs/config.md#L6-L7](https://github.com/openinterpreter/openinterpreter/blob/860153a5318d54e91111af2699136540cf4fc610/docs/config.md#L6-L7), [docs/config.md#L13-L13](https://github.com/openinterpreter/openinterpreter/blob/860153a5318d54e91111af2699136540cf4fc610/docs/config.md#L13-L13), [docs/config.md#L15-L17](https://github.com/openinterpreter/openinterpreter/blob/860153a5318d54e91111af2699136540cf4fc610/docs/config.md#L15-L17) (`clm_ece22aadb879f8f6abcc37cab2e3011a63cfdaefd538b85ce0ab5b993ac69bdc`)
- [observation/documented] Custom OpenAI-compatible providers can be defined under `[model_providers.<id>]` with base_url, env_key, and wire_api (responses or chat), and credentials should come from environment variables or a credential store. -- evidence: [docs/config.md#L143-L148](https://github.com/openinterpreter/openinterpreter/blob/860153a5318d54e91111af2699136540cf4fc610/docs/config.md#L143-L148), [docs/config.md#L116-L117](https://github.com/openinterpreter/openinterpreter/blob/860153a5318d54e91111af2699136540cf4fc610/docs/config.md#L116-L117), [docs/config.md#L130-L131](https://github.com/openinterpreter/openinterpreter/blob/860153a5318d54e91111af2699136540cf4fc610/docs/config.md#L130-L131), [docs/config.md#L123-L128](https://github.com/openinterpreter/openinterpreter/blob/860153a5318d54e91111af2699136540cf4fc610/docs/config.md#L123-L128) (`clm_06a47d8b815a11a11d63da1f0fda96959422e1493a01fef878f0593124a05f8d`)

## limitations (1 claim(s))

- [observation/documented] The README notes this is the new Rust version of Open Interpreter; the original Python project continues as a community-maintained fork elsewhere. -- evidence: [README.md#L142-L143](https://github.com/openinterpreter/openinterpreter/blob/860153a5318d54e91111af2699136540cf4fc610/README.md#L142-L143) (`clm_9333519fc8b24b9e49e862e0364b9dad2f6b7221cace53cbffbd8f4db9c96b3f`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

