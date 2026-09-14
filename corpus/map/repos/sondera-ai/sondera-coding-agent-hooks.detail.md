# sondera-ai/sondera-coding-agent-hooks -- full detail

[Back to orientation](sondera-coding-agent-hooks.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/sondera-ai/sondera-coding-agent-hooks/9efefedd249ee23c48608070978dd1a08a3be1ff/5bba1d792787685d.json](../../../wiki/dossiers/sondera-ai/sondera-coding-agent-hooks/9efefedd249ee23c48608070978dd1a08a3be1ff/5bba1d792787685d.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] The harness coordinates three guardrail subsystems: a YARA-X signature engine (always on and the only deterministic one), an optional LLM secure-code policy classifier, and optional LLM information-flow sensitivity labeling. -- evidence: [docs/architecture.md#L10-L17](https://github.com/sondera-ai/sondera-coding-agent-hooks/blob/9efefedd249ee23c48608070978dd1a08a3be1ff/docs/architecture.md#L10-L17) (`clm_2e75df0423716b7eb4c091eb3655c1c73464b5c8c6790a97c2d6d57a61e9f4d5`)
- [observation/documented] The Cedar policy engine combines guardrail signals with entity state from a Turso (SQLite) local store and returns Allow, Deny, or Escalate adjudications back through the hook adapter. -- evidence: [docs/architecture.md#L25-L29](https://github.com/sondera-ai/sondera-coding-agent-hooks/blob/9efefedd249ee23c48608070978dd1a08a3be1ff/docs/architecture.md#L25-L29) (`clm_8767f500c0ffa2ddd79be00717321c6c9125448995e9b94ae40097ee222889ef`)

## design-choices (4 claim(s))

- [observation/documented] Agent-specific tool names normalize to shared event types (Claude's Bash, Cursor's shell hook, Copilot's and Gemini's bash all become ShellCommand), so one Cedar rule set governs every supported agent. -- evidence: [docs/architecture.md#L45-L51](https://github.com/sondera-ai/sondera-coding-agent-hooks/blob/9efefedd249ee23c48608070978dd1a08a3be1ff/docs/architecture.md#L45-L51) (`clm_88ed8a71d007983c82e9c01c87da37e888b9248facff52d23c5abc89708dd93d`)
- [observation/documented] Agent execution is modeled as a trajectory of typed events in four categories: Action (pre-execution), Observation (post-execution), Control (lifecycle), and State (environment snapshots). -- evidence: [docs/architecture.md#L38-L43](https://github.com/sondera-ai/sondera-coding-agent-hooks/blob/9efefedd249ee23c48608070978dd1a08a3be1ff/docs/architecture.md#L38-L43), [docs/architecture.md#L35-L36](https://github.com/sondera-ai/sondera-coding-agent-hooks/blob/9efefedd249ee23c48608070978dd1a08a3be1ff/docs/architecture.md#L35-L36) (`clm_7783327bc069eb34f4f2ce168fe6716dc241982bfa659502336eedb6607d1c86`)
- [observation/documented] Enforcement hooks fail closed: a hook that cannot reach the harness denies preventive events and never proceeds unadjudicated, so losing the server blocks the agent rather than ungoverning it. -- evidence: [README.md#L29-L32](https://github.com/sondera-ai/sondera-coding-agent-hooks/blob/9efefedd249ee23c48608070978dd1a08a3be1ff/README.md#L29-L32), [docs/deployment.md#L20-L22](https://github.com/sondera-ai/sondera-coding-agent-hooks/blob/9efefedd249ee23c48608070978dd1a08a3be1ff/docs/deployment.md#L20-L22) (`clm_7a57cadd1c414fb6b86affaf23659e238323b1f38ce4fc1872cd33a8db67904e`)
- [observation/documented] The optional LLM classifiers fail open when disabled, erroring, or slower than the adjudication budget — to compliant with no violations and to Public — so Cedar and the deterministic policies still decide. -- evidence: [docs/configuration.md#L89-L92](https://github.com/sondera-ai/sondera-coding-agent-hooks/blob/9efefedd249ee23c48608070978dd1a08a3be1ff/docs/configuration.md#L89-L92), [docs/architecture.md#L19-L23](https://github.com/sondera-ai/sondera-coding-agent-hooks/blob/9efefedd249ee23c48608070978dd1a08a3be1ff/docs/architecture.md#L19-L23) (`clm_3a741e09d77fec14ba60d2e5a9ae0b274fa33b27303aa30df5d27b2d97db7b71`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: CI runs cargo fmt --check, clippy with -D warnings, cargo doc, cargo test --locked --workspace, cargo deny check, and buf lint/format from crates/schema/proto; working conventions live in AGENTS.md. -- evidence: [docs/development.md#L20-L21](https://github.com/sondera-ai/sondera-coding-agent-hooks/blob/9efefedd249ee23c48608070978dd1a08a3be1ff/docs/development.md#L20-L21), [docs/development.md#L9-L11](https://github.com/sondera-ai/sondera-coding-agent-hooks/blob/9efefedd249ee23c48608070978dd1a08a3be1ff/docs/development.md#L9-L11), [docs/development.md#L14-L14](https://github.com/sondera-ai/sondera-coding-agent-hooks/blob/9efefedd249ee23c48608070978dd1a08a3be1ff/docs/development.md#L14-L14), [docs/development.md#L17-L18](https://github.com/sondera-ai/sondera-coding-agent-hooks/blob/9efefedd249ee23c48608070978dd1a08a3be1ff/docs/development.md#L17-L18), [docs/development.md#L56-L58](https://github.com/sondera-ai/sondera-coding-agent-hooks/blob/9efefedd249ee23c48608070978dd1a08a3be1ff/docs/development.md#L56-L58) (`clm_27d771a4615fbcfb0f831dc6ebc3d807780d2876177289fb5125954e43a0c26f`)
- [observation/documented] Repository development practice: integration tests needing a reachable model provider are #[ignore]d by default and run explicitly with `cargo test -- --ignored` once the configured provider is up. -- evidence: [docs/development.md#L23-L25](https://github.com/sondera-ai/sondera-coding-agent-hooks/blob/9efefedd249ee23c48608070978dd1a08a3be1ff/docs/development.md#L23-L25) (`clm_151be13f17087c676c76c50fa013810f91a0db8e8fd85e1e01d7c53462f871c4`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] Hook adapters speak stdin/stdout JSON with each agent, normalize the payload, and forward it over gRPC to `sondera serve` on loopback TCP, 127.0.0.1:50051 by default. -- evidence: [docs/architecture.md#L5-L8](https://github.com/sondera-ai/sondera-coding-agent-hooks/blob/9efefedd249ee23c48608070978dd1a08a3be1ff/docs/architecture.md#L5-L8) (`clm_bf8497c681173ea7473cce5d7575717ec448844610374f088825240865108883`)
- [observation/documented] `sondera serve` runs two gRPC surfaces on one address: `sondera.harness.v1` for Cedar-backed adjudication and `sondera.console.v1` for agent and trajectory reads over the same store. -- evidence: [docs/getting-started.md#L40-L43](https://github.com/sondera-ai/sondera-coding-agent-hooks/blob/9efefedd249ee23c48608070978dd1a08a3be1ff/docs/getting-started.md#L40-L43), [docs/getting-started.md#L38-L38](https://github.com/sondera-ai/sondera-coding-agent-hooks/blob/9efefedd249ee23c48608070978dd1a08a3be1ff/docs/getting-started.md#L38-L38) (`clm_7f7b6605c571d369fa524101d1df8ae9f1b2a6d10f929c62895d4780b44a69ef`)

## memory-state (1 claim(s))

- [observation/documented] Trajectories persist in a Turso (SQLite) store defaulting to ~/.sondera/trajectories/trajectories.db, overridable via --db; the console reads agents and trajectories from the same store. -- evidence: [docs/configuration.md#L32-L37](https://github.com/sondera-ai/sondera-coding-agent-hooks/blob/9efefedd249ee23c48608070978dd1a08a3be1ff/docs/configuration.md#L32-L37), [docs/development.md#L29-L47](https://github.com/sondera-ai/sondera-coding-agent-hooks/blob/9efefedd249ee23c48608070978dd1a08a3be1ff/docs/development.md#L29-L47), [docs/getting-started.md#L49-L54](https://github.com/sondera-ai/sondera-coding-agent-hooks/blob/9efefedd249ee23c48608070978dd1a08a3be1ff/docs/getting-started.md#L49-L54), [docs/getting-started.md#L40-L43](https://github.com/sondera-ai/sondera-coding-agent-hooks/blob/9efefedd249ee23c48608070978dd1a08a3be1ff/docs/getting-started.md#L40-L43) (`clm_0e4251a539d939fbb92dc47c02dc4634ab606aba944ff261b394f5dd12078a26`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] Adapters can act on decisions as block (deny, fail-closed), ask (escalate to the host approval UI), steer (inject context), redact (replace tool output), terminate (stop the loop), or observe only, with capability varying per adapter and hook group. -- evidence: [README.md#L36-L39](https://github.com/sondera-ai/sondera-coding-agent-hooks/blob/9efefedd249ee23c48608070978dd1a08a3be1ff/README.md#L36-L39), [README.md#L41-L52](https://github.com/sondera-ai/sondera-coding-agent-hooks/blob/9efefedd249ee23c48608070978dd1a08a3be1ff/README.md#L41-L52) (`clm_f550331e2cdc019645cd24aa3e4dbd228fbc6d345391de39c7ca3e2ae8054b5e`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] The signature engine and Cedar policies run with no external dependencies or API keys; the optional LLM classifiers support Ollama (the default when enabled), OpenAI-compatible servers, Anthropic, Gemini, and Vertex AI via Application Default Credentials. -- evidence: [docs/configuration.md#L57-L60](https://github.com/sondera-ai/sondera-coding-agent-hooks/blob/9efefedd249ee23c48608070978dd1a08a3be1ff/docs/configuration.md#L57-L60), [docs/configuration.md#L74-L76](https://github.com/sondera-ai/sondera-coding-agent-hooks/blob/9efefedd249ee23c48608070978dd1a08a3be1ff/docs/configuration.md#L74-L76), [docs/configuration.md#L62-L63](https://github.com/sondera-ai/sondera-coding-agent-hooks/blob/9efefedd249ee23c48608070978dd1a08a3be1ff/docs/configuration.md#L62-L63), [README.md#L75-L77](https://github.com/sondera-ai/sondera-coding-agent-hooks/blob/9efefedd249ee23c48608070978dd1a08a3be1ff/README.md#L75-L77) (`clm_62c117de4ded26410eb724f0fcc8271166c43e9219430589de5e69647fb51b55`)
- [observation/documented] Every hook adapter depends on the harness crate as sondera-harness-client with default-features off and only the client feature, linking the gRPC client but not the policy engine. -- evidence: [docs/development.md#L49-L52](https://github.com/sondera-ai/sondera-coding-agent-hooks/blob/9efefedd249ee23c48608070978dd1a08a3be1ff/docs/development.md#L49-L52) (`clm_58dec173115ed2b423be7154e433283dda251967e8fda2d4f71ff19d60f81761`)

## limitations (2 claim(s))

- [observation/documented] Neither gRPC surface authenticates its caller: adjudication is plain HTTP/2 gRPC and the console returns the whole local store and exposes agent deletion, so the bind address should stay on loopback or behind an authenticating proxy. -- evidence: [docs/deployment.md#L11-L13](https://github.com/sondera-ai/sondera-coding-agent-hooks/blob/9efefedd249ee23c48608070978dd1a08a3be1ff/docs/deployment.md#L11-L13), [docs/deployment.md#L5-L9](https://github.com/sondera-ai/sondera-coding-agent-hooks/blob/9efefedd249ee23c48608070978dd1a08a3be1ff/docs/deployment.md#L5-L9) (`clm_b681d68111c5abe390647f360132cd7da05640b2c7eb469edf57a106aa232433`)
- [observation/documented] Enabling the LLM classifiers adds latency to every decision they touch, and with guardrails enabled event content is sent to the configured provider. -- evidence: [docs/deployment.md#L26-L28](https://github.com/sondera-ai/sondera-coding-agent-hooks/blob/9efefedd249ee23c48608070978dd1a08a3be1ff/docs/deployment.md#L26-L28), [docs/configuration.md#L89-L92](https://github.com/sondera-ai/sondera-coding-agent-hooks/blob/9efefedd249ee23c48608070978dd1a08a3be1ff/docs/configuration.md#L89-L92) (`clm_282c65fb898dbc36c04ca741468f17d4fe306b35cfe25c16f96733339b435d11`)

## relevance (1 claim(s))

- [observation/documented] The project targets AI coding agents — Claude Code, Cursor, GitHub Copilot, and Gemini CLI, plus adapters for Antigravity, Codex, Hermes, OpenCode, OpenHands, and VS Code — intercepting shell commands, file operations, and web requests. -- evidence: [README.md#L12-L18](https://github.com/sondera-ai/sondera-coding-agent-hooks/blob/9efefedd249ee23c48608070978dd1a08a3be1ff/README.md#L12-L18), [README.md#L20-L25](https://github.com/sondera-ai/sondera-coding-agent-hooks/blob/9efefedd249ee23c48608070978dd1a08a3be1ff/README.md#L20-L25) (`clm_9199d2916301eb69ee465747887bbc77c211d10431e79444f9d89588f0caa566`)

