---
access: public
aliases: []
claim_ids:
- clm_33d1cf01a6bfcad0d9c4df4ef23da1c6e7254a43a78d348bba914b5822ef67f0
- clm_44effe643c218af7393a449baa3e734de40ff4ad2bbc1e8cba317ffc379566d0
- clm_45f6186c1729a04a722d29291a00a6a37b21a80b82ea1f4b40ce4e9552b2e878
- clm_503fccdc1b8c9488d684ace2158f9b123df837d07cd7016bbd32d16ffbc7ad8b
- clm_587ad963f0b29c88ef84f12dcef9d4ea5191f60cd22ff4e50b88e648d835bf9d
- clm_a37a5639b9500601d35921738382ebbdd7c5d31c459de9de01bc5a720a5aa074
- clm_a7ea034be18177b69b9c1a56b4d0f55a061c21db4ad2a8403a5d5abee745b940
- clm_b679802c5a694a0347f7891060e029565b37b2bd707da0f957abf9949251ecab
- clm_c03e2811bd10f1ede30152f87f4be947acc9fd89fca916623a976007e2ac1de8
- clm_ccb040ffd3a9244a0ac84fa03356277cae4e88b35310173b5b6d1587cafca615
- clm_e39232c09512d5721611cc3d38e7b02fe3cdee244f6f01f43e6aa9f586f84c0b
- clm_f4ae9d69bbb3a124e5d977d19aab6973e9e30cd266f9137d3d007de153cf832d
maturity: draft
page_id: pg_21adcbb189f153bca255a3cf0a9cdd0b
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_533b5a956b54509da8dde81369676b2e
title: opendev-to/opendev/README.md @ d32c660e4eed
updated_at: '2026-09-14T02:27:10Z'
---

# opendev-to/opendev/README.md @ d32c660e4eed

<!-- rcw:begin owner=source:src_533b5a956b54509da8dde81369676b2e block=evidence -->
- Repository development practice: contributors are asked to open an issue or submit a pull request, and a ROADMAP.md lists priorities for community contributions. [@claim:clm_33d1cf01a6bfcad0d9c4df4ef23da1c6e7254a43a78d348bba914b5822ef67f0]
- Workflow bindings are configured in `~/.opendev/settings.json` with keys like `model_provider`, `model`, `model_thinking_provider`, and `model_thinking`. [@claim:clm_44effe643c218af7393a449baa3e734de40ff4ad2bbc1e8cba317ffc379566d0]
- The README reports a benchmark comparing OpenDev 0.1.4 startup (4.3 ms), peak memory (9.4 MB), and install size (18 MB) against Codex, Claude Code, and OpenCode on macOS ARM64 using hyperfine and /usr/bin/time. [@claim:clm_45f6186c1729a04a722d29291a00a6a37b21a80b82ea1f4b40ce4e9552b2e878]
- The CLI offers an interactive TUI (`opendev`), a Web UI (`opendev run ui`), single-prompt mode (`-p`), session resume (`--continue`), and an interactive `opendev config setup` for provider/model binding. [@claim:clm_503fccdc1b8c9488d684ace2158f9b123df837d07cd7016bbd32d16ffbc7ad8b]
- Five workflow slots are defined: Normal (execution), Thinking (reasoning), Compact (context summarization), Critique (self-critique), and VLM (vision), each bindable to any configured LLM. [@claim:clm_587ad963f0b29c88ef84f12dcef9d4ea5191f60cd22ff4e50b88e648d835bf9d]
- Workflow slots have documented fallback behavior: Thinking and Compact fall back to Normal, Critique falls back to Thinking, and VLM falls back to Normal when the model lacks vision. [@claim:clm_a37a5639b9500601d35921738382ebbdd7c5d31c459de9de01bc5a720a5aa074]
- The agent supports nine LLM providers: OpenAI, Anthropic, Fireworks, Google, Groq, Mistral, DeepInfra, OpenRouter, and Azure OpenAI. [@claim:clm_a7ea034be18177b69b9c1a56b4d0f55a061c21db4ad2a8403a5d5abee745b940]
- An agent fleet can launch multiple sub-agents in parallel, each with its own LLM binding, context window, and tool access, aggregating results back into the session. [@claim:clm_b679802c5a694a0347f7891060e029565b37b2bd707da0f957abf9949251ecab]
- Building from source requires Rust 1.94 or later, and the runtime uses Tokio for async parallelism. [@claim:clm_c03e2811bd10f1ede30152f87f4be947acc9fd89fca916623a976007e2ac1de8]
- MCP integration provides dynamic tool discovery with subcommands such as `opendev mcp list`, `mcp add`, and `mcp enable/disable`. [@claim:clm_ccb040ffd3a9244a0ac84fa03356277cae4e88b35310173b5b6d1587cafca615]
- Repository development practice: contributors build with `cargo build --workspace`, run `cargo test --workspace`, and use cargo check, clippy, and fmt; the Web UI frontend is built with `npm ci && npm run build`. [@claim:clm_e39232c09512d5721611cc3d38e7b02fe3cdee244f6f01f43e6aa9f586f84c0b]
- OpenDev is described as an open-source, terminal-native coding agent built as a compound AI system of agents and workflows, each independently bound to a user-configured model. [@claim:clm_f4ae9d69bbb3a124e5d977d19aab6973e9e30cd266f9137d3d007de153cf832d]
<!-- rcw:end owner=source:src_533b5a956b54509da8dde81369676b2e block=evidence -->

## Researcher notes

