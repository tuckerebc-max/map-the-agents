# openai/codex -- full detail

[Back to orientation](codex.md)

## Origins

- research-completed
- alltheagents.org-backing

## Projects

- navy-yard

Full evidence record (JSON): [wiki/dossiers/openai/codex/6f39a47bb3b04de4c804187bfbf55edc56939aab/3996e27a06a717c7.json](../../../wiki/dossiers/openai/codex/6f39a47bb3b04de4c804187bfbf55edc56939aab/3996e27a06a717c7.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [inference/code-inspected] The Rust core includes an AgentControl method that returns bounded root conversation and authorization state for MultiAgent V2 worker threads, skipping when the thread is the root itself or not V2. -- evidence: [codex-rs/core/src/agent/control/user_authorization.rs#L32-L46](https://github.com/openai/codex/blob/6f39a47bb3b04de4c804187bfbf55edc56939aab/codex-rs/core/src/agent/control/user_authorization.rs#L32-L46) (`clm_205c2433ea579e7fdd152e073ee906bd80488a22dae6f41e58df9f1ac39e20a9`)

## design-choices (1 claim(s))

- [observation/documented] Admins can set allow_managed_hooks_only=true in requirements.toml to ignore user, project, and session hook configs; the flag is only honored in requirements.toml, not config.toml. -- evidence: [docs/config.md#L11-L15](https://github.com/openai/codex/blob/6f39a47bb3b04de4c804187bfbf55edc56939aab/docs/config.md#L11-L15) (`clm_1c750b9b336d880065b98aed688d237d5809a58febc7c9f9727fed53b9e546d6`)

## workflows (2 claim(s))

- [observation/documented] On Mac/Linux the CLI installs via a curl-piped shell script, and on Windows via a PowerShell one-liner fetching install.ps1. -- evidence: [README.md#L16-L16](https://github.com/openai/codex/blob/6f39a47bb3b04de4c804187bfbf55edc56939aab/README.md#L16-L16), [README.md#L24-L26](https://github.com/openai/codex/blob/6f39a47bb3b04de4c804187bfbf55edc56939aab/README.md#L24-L26), [README.md#L22-L22](https://github.com/openai/codex/blob/6f39a47bb3b04de4c804187bfbf55edc56939aab/README.md#L22-L22), [README.md#L18-L20](https://github.com/openai/codex/blob/6f39a47bb3b04de4c804187bfbf55edc56939aab/README.md#L18-L20) (`clm_04115f1de140056c833e22ab498342411f9de61ca60aa63e2968b59a4ade8bd1`)
- [observation/documented] Standalone installers default to downloads from releases.openai.com/codex and fall back to GitHub Releases; setting CODEX_INSTALLER_USE_RELEASES_OPENAI_COM=false forces GitHub Releases. -- evidence: [README.md#L34-L36](https://github.com/openai/codex/blob/6f39a47bb3b04de4c804187bfbf55edc56939aab/README.md#L34-L36), [README.md#L28-L28](https://github.com/openai/codex/blob/6f39a47bb3b04de4c804187bfbf55edc56939aab/README.md#L28-L28), [README.md#L30-L32](https://github.com/openai/codex/blob/6f39a47bb3b04de4c804187bfbf55edc56939aab/README.md#L30-L32) (`clm_7a850c1df144fadce442e2744c5c922febb1dc34891c4f7f157a06cf82e766c2`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] Codex CLI is a local coding agent from OpenAI, started by running the `codex` command; a desktop app experience is available via `codex app`. -- evidence: [README.md#L50-L50](https://github.com/openai/codex/blob/6f39a47bb3b04de4c804187bfbf55edc56939aab/README.md#L50-L50), [README.md#L1-L8](https://github.com/openai/codex/blob/6f39a47bb3b04de4c804187bfbf55edc56939aab/README.md#L1-L8) (`clm_c0d9169e44929b3b0cf7c5e748c6caef777c8e51f27820ae3172a39da74730a2`)
- [observation/documented] Authentication supports signing in with a ChatGPT account (recommended for Plus/Pro/Business/Edu/Enterprise plans) or, with extra setup, an API key. -- evidence: [README.md#L70-L70](https://github.com/openai/codex/blob/6f39a47bb3b04de4c804187bfbf55edc56939aab/README.md#L70-L70), [README.md#L72-L72](https://github.com/openai/codex/blob/6f39a47bb3b04de4c804187bfbf55edc56939aab/README.md#L72-L72) (`clm_8dd0b86d8f1e4d8a4df8ee6f1e48a4dbc79b588753a1de38e54b0f0aa69ff945`)

## memory-state (1 claim(s))

- [inference/code-inspected] Root evidence projection filters the root thread's retained history, excluding summary messages and user messages starting with <user_action>, and caps root messages at 8. -- evidence: [codex-rs/core/src/agent/control/user_authorization.rs#L48-L230](https://github.com/openai/codex/blob/6f39a47bb3b04de4c804187bfbf55edc56939aab/codex-rs/core/src/agent/control/user_authorization.rs#L48-L230), [codex-rs/core/src/agent/control/user_authorization.rs#L30-L30](https://github.com/openai/codex/blob/6f39a47bb3b04de4c804187bfbf55edc56939aab/codex-rs/core/src/agent/control/user_authorization.rs#L30-L30) (`clm_920f6343a022061b8b5d9f07fe91db7fb124b9af002631696878221a63b251e4`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Codex CLI can also be installed through npm (@openai/codex) and Homebrew (brew install --cask codex), or by downloading platform binaries from GitHub Releases. -- evidence: [README.md#L42-L43](https://github.com/openai/codex/blob/6f39a47bb3b04de4c804187bfbf55edc56939aab/README.md#L42-L43), [README.md#L57-L62](https://github.com/openai/codex/blob/6f39a47bb3b04de4c804187bfbf55edc56939aab/README.md#L57-L62), [README.md#L38-L38](https://github.com/openai/codex/blob/6f39a47bb3b04de4c804187bfbf55edc56939aab/README.md#L38-L38), [README.md#L52-L53](https://github.com/openai/codex/blob/6f39a47bb3b04de4c804187bfbf55edc56939aab/README.md#L52-L53), [README.md#L47-L48](https://github.com/openai/codex/blob/6f39a47bb3b04de4c804187bfbf55edc56939aab/README.md#L47-L48) (`clm_1a4f339e0210a86bc4e23b93d223caaca7ad2520bcded444a04237244e5f46a5`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (1 claim(s))

- [observation/documented] The repository is Apache-2.0 licensed and links to external docs for configuration, sandboxing/approvals, execution policy, skills, and AGENTS.md. -- evidence: [docs/config.md#L3-L3](https://github.com/openai/codex/blob/6f39a47bb3b04de4c804187bfbf55edc56939aab/docs/config.md#L3-L3), [docs/sandbox.md#L3-L3](https://github.com/openai/codex/blob/6f39a47bb3b04de4c804187bfbf55edc56939aab/docs/sandbox.md#L3-L3), [docs/execpolicy.md#L3-L3](https://github.com/openai/codex/blob/6f39a47bb3b04de4c804187bfbf55edc56939aab/docs/execpolicy.md#L3-L3), [docs/config.md#L7-L7](https://github.com/openai/codex/blob/6f39a47bb3b04de4c804187bfbf55edc56939aab/docs/config.md#L7-L7), [README.md#L81-L81](https://github.com/openai/codex/blob/6f39a47bb3b04de4c804187bfbf55edc56939aab/README.md#L81-L81), [docs/skills.md#L3-L3](https://github.com/openai/codex/blob/6f39a47bb3b04de4c804187bfbf55edc56939aab/docs/skills.md#L3-L3), [docs/config.md#L5-L5](https://github.com/openai/codex/blob/6f39a47bb3b04de4c804187bfbf55edc56939aab/docs/config.md#L5-L5), [README.md#L76-L79](https://github.com/openai/codex/blob/6f39a47bb3b04de4c804187bfbf55edc56939aab/README.md#L76-L79) (`clm_b81ae7fa3f3152a9d6025f167edc84cdfad7f682e8498cea7be248faf9102608`)

