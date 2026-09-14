# opendev-to/opendev -- full detail

[Back to orientation](opendev.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/opendev-to/opendev/d32c660e4eed1a8e988d1fd58da88e41ba641d08/6c2de2a3889db931.json](../../../wiki/dossiers/opendev-to/opendev/d32c660e4eed1a8e988d1fd58da88e41ba641d08/6c2de2a3889db931.json)

## specifications (3 claim(s))

- [observation/documented] OpenDev is described as an open-source, terminal-native coding agent built as a compound AI system of agents and workflows, each independently bound to a user-configured model. -- evidence: [README.md#L29-L29](https://github.com/opendev-to/opendev/blob/d32c660e4eed1a8e988d1fd58da88e41ba641d08/README.md#L29-L29) (`clm_f4ae9d69bbb3a124e5d977d19aab6973e9e30cd266f9137d3d007de153cf832d`)
- [observation/documented] Five workflow slots are defined: Normal (execution), Thinking (reasoning), Compact (context summarization), Critique (self-critique), and VLM (vision), each bindable to any configured LLM. -- evidence: [README.md#L224-L228](https://github.com/opendev-to/opendev/blob/d32c660e4eed1a8e988d1fd58da88e41ba641d08/README.md#L224-L228), [README.md#L33-L33](https://github.com/opendev-to/opendev/blob/d32c660e4eed1a8e988d1fd58da88e41ba641d08/README.md#L33-L33) (`clm_587ad963f0b29c88ef84f12dcef9d4ea5191f60cd22ff4e50b88e648d835bf9d`)
- [observation/documented] Workflow slots have documented fallback behavior: Thinking and Compact fall back to Normal, Critique falls back to Thinking, and VLM falls back to Normal when the model lacks vision. -- evidence: [README.md#L224-L228](https://github.com/opendev-to/opendev/blob/d32c660e4eed1a8e988d1fd58da88e41ba641d08/README.md#L224-L228) (`clm_a37a5639b9500601d35921738382ebbdd7c5d31c459de9de01bc5a720a5aa074`)

## components (3 claim(s))

- [observation/documented] The design doc specifies a TaskManager in opendev-runtime: a UI-agnostic task lifecycle state machine with idempotent transitions, a notified flag, 5-second eviction grace, and retain-to-block-eviction. -- evidence: [docs/agent-framework-adaptation.md#L44-L44](https://github.com/opendev-to/opendev/blob/d32c660e4eed1a8e988d1fd58da88e41ba641d08/docs/agent-framework-adaptation.md#L44-L44), [docs/agent-framework-adaptation.md#L48-L52](https://github.com/opendev-to/opendev/blob/d32c660e4eed1a8e988d1fd58da88e41ba641d08/docs/agent-framework-adaptation.md#L48-L52) (`clm_5311f4defdac0b9aa5585ce7580bda67b36fcaf7da683781a35d43a68074b1a6`)
- [observation/documented] A file-based mailbox system gives each agent an inbox with fd-lock protocol, corruption recovery via rename, a 1000-entry cap, and message types including Text, ShutdownRequest, ShutdownResponse, and Idle. -- evidence: [docs/agent-framework-adaptation.md#L156-L162](https://github.com/opendev-to/opendev/blob/d32c660e4eed1a8e988d1fd58da88e41ba641d08/docs/agent-framework-adaptation.md#L156-L162), [docs/agent-framework-adaptation.md#L152-L152](https://github.com/opendev-to/opendev/blob/d32c660e4eed1a8e988d1fd58da88e41ba641d08/docs/agent-framework-adaptation.md#L152-L152), [docs/agent-framework-adaptation.md#L164-L164](https://github.com/opendev-to/opendev/blob/d32c660e4eed1a8e988d1fd58da88e41ba641d08/docs/agent-framework-adaptation.md#L164-L164) (`clm_5ef3258e920f6d4f26c73241dd365762485d0daf361f457820279bbaa4b492f8`)
- [observation/documented] A WorktreeManager creates git worktrees per agent (branch `opendev/agent-{short_id}`), detects changes, and removes clean worktrees while preserving dirty ones for review. -- evidence: [docs/agent-framework-adaptation.md#L274-L278](https://github.com/opendev-to/opendev/blob/d32c660e4eed1a8e988d1fd58da88e41ba641d08/docs/agent-framework-adaptation.md#L274-L278), [docs/agent-framework-adaptation.md#L270-L270](https://github.com/opendev-to/opendev/blob/d32c660e4eed1a8e988d1fd58da88e41ba641d08/docs/agent-framework-adaptation.md#L270-L270) (`clm_4be6dda976e36c638f39a11f9cbb51907212a6cd5dbe269efe3e4f4de1989042`)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: contributors build with `cargo build --workspace`, run `cargo test --workspace`, and use cargo check, clippy, and fmt; the Web UI frontend is built with `npm ci && npm run build`. -- evidence: [README.md#L277-L279](https://github.com/opendev-to/opendev/blob/d32c660e4eed1a8e988d1fd58da88e41ba641d08/README.md#L277-L279), [README.md#L257-L262](https://github.com/opendev-to/opendev/blob/d32c660e4eed1a8e988d1fd58da88e41ba641d08/README.md#L257-L262), [README.md#L264-L269](https://github.com/opendev-to/opendev/blob/d32c660e4eed1a8e988d1fd58da88e41ba641d08/README.md#L264-L269) (`clm_e39232c09512d5721611cc3d38e7b02fe3cdee244f6f01f43e6aa9f586f84c0b`)
- [observation/documented] Repository development practice: contributors are asked to open an issue or submit a pull request, and a ROADMAP.md lists priorities for community contributions. -- evidence: [README.md#L285-L285](https://github.com/opendev-to/opendev/blob/d32c660e4eed1a8e988d1fd58da88e41ba641d08/README.md#L285-L285), [README.md#L283-L283](https://github.com/opendev-to/opendev/blob/d32c660e4eed1a8e988d1fd58da88e41ba641d08/README.md#L283-L283) (`clm_33d1cf01a6bfcad0d9c4df4ef23da1c6e7254a43a78d348bba914b5822ef67f0`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The CLI offers an interactive TUI (`opendev`), a Web UI (`opendev run ui`), single-prompt mode (`-p`), session resume (`--continue`), and an interactive `opendev config setup` for provider/model binding. -- evidence: [README.md#L210-L210](https://github.com/opendev-to/opendev/blob/d32c660e4eed1a8e988d1fd58da88e41ba641d08/README.md#L210-L210), [README.md#L198-L198](https://github.com/opendev-to/opendev/blob/d32c660e4eed1a8e988d1fd58da88e41ba641d08/README.md#L198-L198), [README.md#L204-L204](https://github.com/opendev-to/opendev/blob/d32c660e4eed1a8e988d1fd58da88e41ba641d08/README.md#L204-L204), [README.md#L207-L208](https://github.com/opendev-to/opendev/blob/d32c660e4eed1a8e988d1fd58da88e41ba641d08/README.md#L207-L208), [README.md#L201-L201](https://github.com/opendev-to/opendev/blob/d32c660e4eed1a8e988d1fd58da88e41ba641d08/README.md#L201-L201) (`clm_503fccdc1b8c9488d684ace2158f9b123df837d07cd7016bbd32d16ffbc7ad8b`)
- [observation/documented] MCP integration provides dynamic tool discovery with subcommands such as `opendev mcp list`, `mcp add`, and `mcp enable/disable`. -- evidence: [README.md#L249-L253](https://github.com/opendev-to/opendev/blob/d32c660e4eed1a8e988d1fd58da88e41ba641d08/README.md#L249-L253), [README.md#L247-L247](https://github.com/opendev-to/opendev/blob/d32c660e4eed1a8e988d1fd58da88e41ba641d08/README.md#L247-L247) (`clm_ccb040ffd3a9244a0ac84fa03356277cae4e88b35310173b5b6d1587cafca615`)
- [observation/documented] Workflow bindings are configured in `~/.opendev/settings.json` with keys like `model_provider`, `model`, `model_thinking_provider`, and `model_thinking`. -- evidence: [README.md#L232-L239](https://github.com/opendev-to/opendev/blob/d32c660e4eed1a8e988d1fd58da88e41ba641d08/README.md#L232-L239), [README.md#L230-L230](https://github.com/opendev-to/opendev/blob/d32c660e4eed1a8e988d1fd58da88e41ba641d08/README.md#L230-L230) (`clm_44effe643c218af7393a449baa3e734de40ff4ad2bbc1e8cba317ffc379566d0`)

## memory-state (1 claim(s))

- [observation/documented] Per-agent sidechain transcripts are stored as append-only JSONL at `~/.opendev/sessions/{session_id}/agents/{agent_id}.jsonl`, with readers that filter malformed lines and orphaned tool calls for resume. -- evidence: [docs/agent-framework-adaptation.md#L73-L73](https://github.com/opendev-to/opendev/blob/d32c660e4eed1a8e988d1fd58da88e41ba641d08/docs/agent-framework-adaptation.md#L73-L73), [docs/agent-framework-adaptation.md#L62-L62](https://github.com/opendev-to/opendev/blob/d32c660e4eed1a8e988d1fd58da88e41ba641d08/docs/agent-framework-adaptation.md#L62-L62), [docs/agent-framework-adaptation.md#L66-L71](https://github.com/opendev-to/opendev/blob/d32c660e4eed1a8e988d1fd58da88e41ba641d08/docs/agent-framework-adaptation.md#L66-L71) (`clm_4a036e3fd12f5f820c20bda1de179af88b26e18466b98ba789a5d1ca8f6622c2`)

## orchestration (2 claim(s))

- [observation/documented] An agent fleet can launch multiple sub-agents in parallel, each with its own LLM binding, context window, and tool access, aggregating results back into the session. -- evidence: [README.md#L75-L75](https://github.com/opendev-to/opendev/blob/d32c660e4eed1a8e988d1fd58da88e41ba641d08/README.md#L75-L75), [README.md#L87-L89](https://github.com/opendev-to/opendev/blob/d32c660e4eed1a8e988d1fd58da88e41ba641d08/README.md#L87-L89) (`clm_b679802c5a694a0347f7891060e029565b37b2bd707da0f957abf9949251ecab`)
- [observation/documented] A `run_in_background` parameter on `spawn_subagent` returns a task_id immediately, runs the agent in a detached tokio task, and injects results into the parent via a sentinel mechanism when idle. -- evidence: [docs/agent-framework-adaptation.md#L83-L83](https://github.com/opendev-to/opendev/blob/d32c660e4eed1a8e988d1fd58da88e41ba641d08/docs/agent-framework-adaptation.md#L83-L83), [docs/agent-framework-adaptation.md#L89-L107](https://github.com/opendev-to/opendev/blob/d32c660e4eed1a8e988d1fd58da88e41ba641d08/docs/agent-framework-adaptation.md#L89-L107) (`clm_69a59e544af4ec3feac0eff2c0f1723abb9883b424d2764fbce30d77686750c1`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (1 claim(s))

- [observation/documented] The README reports a benchmark comparing OpenDev 0.1.4 startup (4.3 ms), peak memory (9.4 MB), and install size (18 MB) against Codex, Claude Code, and OpenCode on macOS ARM64 using hyperfine and /usr/bin/time. -- evidence: [README.md#L39-L44](https://github.com/opendev-to/opendev/blob/d32c660e4eed1a8e988d1fd58da88e41ba641d08/README.md#L39-L44), [README.md#L46-L46](https://github.com/opendev-to/opendev/blob/d32c660e4eed1a8e988d1fd58da88e41ba641d08/README.md#L46-L46) (`clm_45f6186c1729a04a722d29291a00a6a37b21a80b82ea1f4b40ce4e9552b2e878`)

## dependencies (2 claim(s))

- [observation/documented] The agent supports nine LLM providers: OpenAI, Anthropic, Fireworks, Google, Groq, Mistral, DeepInfra, OpenRouter, and Azure OpenAI. -- evidence: [README.md#L220-L220](https://github.com/opendev-to/opendev/blob/d32c660e4eed1a8e988d1fd58da88e41ba641d08/README.md#L220-L220) (`clm_a7ea034be18177b69b9c1a56b4d0f55a061c21db4ad2a8403a5d5abee745b940`)
- [observation/documented] Building from source requires Rust 1.94 or later, and the runtime uses Tokio for async parallelism. -- evidence: [README.md#L137-L137](https://github.com/opendev-to/opendev/blob/d32c660e4eed1a8e988d1fd58da88e41ba641d08/README.md#L137-L137), [README.md#L87-L89](https://github.com/opendev-to/opendev/blob/d32c660e4eed1a8e988d1fd58da88e41ba641d08/README.md#L87-L89) (`clm_c03e2811bd10f1ede30152f87f4be947acc9fd89fca916623a976007e2ac1de8`)

## limitations (1 claim(s))

- [inference/documented] The adaptation document indicates that before this work OpenDev lacked background agents, inter-agent communication, teams, and worktree isolation, suggesting these multi-agent capabilities are recent additions whose shipped status should be verified against code. -- evidence: [docs/agent-framework-adaptation.md#L34-L34](https://github.com/opendev-to/opendev/blob/d32c660e4eed1a8e988d1fd58da88e41ba641d08/docs/agent-framework-adaptation.md#L34-L34), [docs/agent-framework-adaptation.md#L17-L30](https://github.com/opendev-to/opendev/blob/d32c660e4eed1a8e988d1fd58da88e41ba641d08/docs/agent-framework-adaptation.md#L17-L30) (`clm_2d92d54e1bfa222b4c19531557432f09070ab955ecaea84b3cded9bc16061d1e`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

