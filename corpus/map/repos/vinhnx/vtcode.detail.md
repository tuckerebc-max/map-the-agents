# vinhnx/vtcode -- full detail

[Back to orientation](vtcode.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/vinhnx/vtcode/18f7d26c76e28ab83e3de4bec4874f5fc9264190/d83edd9c49fa70e2.json](../../../wiki/dossiers/vinhnx/vtcode/18f7d26c76e28ab83e3de4bec4874f5fc9264190/d83edd9c49fa70e2.json)

## specifications (1 claim(s))

- [observation/documented] VT Code is described as a secure, open-source terminal coding agent written in Rust, shipped as a single static binary for interactive and long-running autonomous work. -- evidence: [README.md#L7-L7](https://github.com/vinhnx/VTCode/blob/18f7d26c76e28ab83e3de4bec4874f5fc9264190/README.md#L7-L7), [README.md#L62-L62](https://github.com/vinhnx/VTCode/blob/18f7d26c76e28ab83e3de4bec4874f5fc9264190/README.md#L62-L62) (`clm_16010ea108571dcb7a1d265fd945fe8ae46bc81d8f684e5b1dc761a0613afeb9`)

## components (1 claim(s))

- [observation/documented] ThreadEvent (vtcode-exec-events) is the authoritative runtime event contract feeding replay, checkpoints, memory, and trajectory export; follow-up inputs queue and inject one at a time at idle boundaries. -- evidence: [README.md#L91-L97](https://github.com/vinhnx/VTCode/blob/18f7d26c76e28ab83e3de4bec4874f5fc9264190/README.md#L91-L97), [docs/ARCHITECTURE.md#L44-L44](https://github.com/vinhnx/VTCode/blob/18f7d26c76e28ab83e3de4bec4874f5fc9264190/docs/ARCHITECTURE.md#L44-L44) (`clm_48a6b59da80c47ab9878bd8c7835334964a4fd640576244c5919012c21f24dc0`)

## design-choices (1 claim(s))

- [observation/documented] The architecture separates the model (reasoning) from the harness (runtime supplying tools, context, sandboxing, state, and verification), organized as seven reinforcing subsystems. -- evidence: [docs/ARCHITECTURE.md#L26-L30](https://github.com/vinhnx/VTCode/blob/18f7d26c76e28ab83e3de4bec4874f5fc9264190/docs/ARCHITECTURE.md#L26-L30), [README.md#L64-L64](https://github.com/vinhnx/VTCode/blob/18f7d26c76e28ab83e3de4bec4874f5fc9264190/README.md#L64-L64) (`clm_6e5dbab108180acb00e3375600d1ea7b54fd606a3842be6720d12cccf0297428`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (4 claim(s))

- [observation/documented] The CLI separates data on stdout from diagnostics on stderr, uses clap for argument parsing, isolates subcommands (ask, exec, chat) in dedicated modules, and handles SIGINT/SIGTERM gracefully. -- evidence: [docs/ARCHITECTURE.md#L108-L111](https://github.com/vinhnx/VTCode/blob/18f7d26c76e28ab83e3de4bec4874f5fc9264190/docs/ARCHITECTURE.md#L108-L111) (`clm_6ef343e7928a4cf6ae926150393063eea497ee91f908e4d7e43fef9a518d0da1`)
- [observation/documented] Default public tool surface includes exec_command (shell via policy/sandbox/approvals), write_stdin for live-session continuation, and apply_patch with workspace-boundary checks. -- evidence: [docs/ARCHITECTURE.md#L196-L198](https://github.com/vinhnx/VTCode/blob/18f7d26c76e28ab83e3de4bec4874f5fc9264190/docs/ARCHITECTURE.md#L196-L198) (`clm_1e3bec124a4f73f70cdf323253c0b20a1b3e5515deefecf78676e391cf00e36a`)
- [observation/documented] Configuration uses vtcode.toml at workspace or platform config-directory layers, with environment-variable overrides and a legacy $VTCODE_HOME path kept as a migration source. -- evidence: [docs/config/config.md#L31-L34](https://github.com/vinhnx/VTCode/blob/18f7d26c76e28ab83e3de4bec4874f5fc9264190/docs/config/config.md#L31-L34), [docs/config/config.md#L5-L5](https://github.com/vinhnx/VTCode/blob/18f7d26c76e28ab83e3de4bec4874f5fc9264190/docs/config/config.md#L5-L5) (`clm_663bfe81efe3364e76cb4773e59ac35b9d050340db2ddc8ec8612fe76ca3cd33`)
- [observation/documented] Interactive sessions live-reload watched config changes with debouncing; safe settings apply without restart, and malformed edits keep the last valid configuration with a warning. -- evidence: [docs/config/config.md#L75-L81](https://github.com/vinhnx/VTCode/blob/18f7d26c76e28ab83e3de4bec4874f5fc9264190/docs/config/config.md#L75-L81), [docs/config/config.md#L83-L86](https://github.com/vinhnx/VTCode/blob/18f7d26c76e28ab83e3de4bec4874f5fc9264190/docs/config/config.md#L83-L86) (`clm_162178fbb2ce931ce2e8e56772ac5136101131a67ab3b9465378587ac3b73c5c`)

## memory-state (1 claim(s))

- [observation/documented] A persisted SessionMemoryEnvelope summarizes objective, constraints, touched files, grounded facts, verification status, and delegated findings for resume and summarized-fork handoff. -- evidence: [docs/ARCHITECTURE.md#L34-L42](https://github.com/vinhnx/VTCode/blob/18f7d26c76e28ab83e3de4bec4874f5fc9264190/docs/ARCHITECTURE.md#L34-L42), [docs/ARCHITECTURE.md#L89-L93](https://github.com/vinhnx/VTCode/blob/18f7d26c76e28ab83e3de4bec4874f5fc9264190/docs/ARCHITECTURE.md#L89-L93) (`clm_7f3c0cc587b459a327597326855b28aedbc7c126ef8e0074808864109c192089`)

## orchestration (2 claim(s))

- [observation/documented] With agent.harness.orchestration_mode = plan_build_evaluate, a planner writes spec/contract artifacts, the generator runs on the main session, and an evaluator performs a skeptical post-build pass; failed evaluation triggers bounded revision rounds. -- evidence: [docs/ARCHITECTURE.md#L74-L75](https://github.com/vinhnx/VTCode/blob/18f7d26c76e28ab83e3de4bec4874f5fc9264190/docs/ARCHITECTURE.md#L74-L75), [docs/ARCHITECTURE.md#L77-L80](https://github.com/vinhnx/VTCode/blob/18f7d26c76e28ab83e3de4bec4874f5fc9264190/docs/ARCHITECTURE.md#L77-L80) (`clm_a30db75e4cf6eaa56af6b0f0b2b3580641747e16e5690c7ce11bacaf859a410a`)
- [observation/documented] Delegation is modeled as explicit thread spawning: child agents do bounded sidecar work, their output is advisory until the parent validates and merges it into the SessionMemoryEnvelope at turn boundaries. -- evidence: [docs/ARCHITECTURE.md#L89-L93](https://github.com/vinhnx/VTCode/blob/18f7d26c76e28ab83e3de4bec4874f5fc9264190/docs/ARCHITECTURE.md#L89-L93), [docs/ARCHITECTURE.md#L87-L87](https://github.com/vinhnx/VTCode/blob/18f7d26c76e28ab83e3de4bec4874f5fc9264190/docs/ARCHITECTURE.md#L87-L87) (`clm_60046b34315663cfb147fe9d6b65a77b114c523287e08877ed52c61fda45c7d6`)

## tools-permissions (1 claim(s))

- [observation/documented] Feature flags include human_in_the_loop (tool approval prompts, default true) and mcp_enabled (default false), toggled via the [features] table in vtcode.toml. -- evidence: [docs/config/config.md#L106-L112](https://github.com/vinhnx/VTCode/blob/18f7d26c76e28ab83e3de4bec4874f5fc9264190/docs/config/config.md#L106-L112), [docs/config/config.md#L96-L102](https://github.com/vinhnx/VTCode/blob/18f7d26c76e28ab83e3de4bec4874f5fc9264190/docs/config/config.md#L96-L102) (`clm_0318e6798c363c9641107dd48e241fd62305b43e7c61e6e9182808db47b777ef`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The agent.provider setting supports many providers including openai, anthropic, google, deepseek, ollama, lmstudio, and others, with per-provider base_url and API-key environment variables configurable. -- evidence: [docs/config/config.md#L120-L124](https://github.com/vinhnx/VTCode/blob/18f7d26c76e28ab83e3de4bec4874f5fc9264190/docs/config/config.md#L120-L124), [docs/config/config.md#L132-L136](https://github.com/vinhnx/VTCode/blob/18f7d26c76e28ab83e3de4bec4874f5fc9264190/docs/config/config.md#L132-L136) (`clm_caa9a1ab5e14a82f06aaa03c7761877c88dbc28176966cac348494764dcc4a4a`)

## limitations (1 claim(s))

- [observation/documented] The README states the project is in active development and that local inference and some automation flows are experimental and may change between releases. -- evidence: [README.md#L66-L68](https://github.com/vinhnx/VTCode/blob/18f7d26c76e28ab83e3de4bec4874f5fc9264190/README.md#L66-L68) (`clm_8273e1126f3d9d7e38cf1b03c1ba2438054b74ed3c5244b458a991fc86deda54`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

