---
access: public
aliases: []
claim_ids:
- clm_025330e06eb33b0b34663592c480e4a6c7d92c3a35699d0d490c734770ed3cbb
- clm_15175ee4db2049a588eb0d4805f15d96e35df34aa512a6026abbc6f404c93dc8
- clm_16d113dec9f7509298c8c01a10bc131339d728df168ce9376f23ad98867540d9
- clm_3b99eb62e5f03b235d5b8f0a137a788a2fc0444bb7b473a4c6f7336adaee8f05
- clm_5699c7bdc6e84a2368dff746f65401fe9b415f28da3374d59a37474bf3293576
- clm_78cd62e388ca61b9205ba5caa1357221fd1591520093c04db81b49dab1015226
- clm_941e2d550bd396066cd667c7725808f6aedd6502c061458f50d88467876322b8
- clm_a9e4a25e4a74a1fa96bc095f1a7408e6a1dc215e99ebffb61a659b79bd0eb7af
- clm_bd54df6b2cc9905d7aa78b3796af6cc63e894512520caad0bb1888cfa90fd357
- clm_be02c656aaba0703376e1247050b6fa12502604b784adc5b15d8e56c68bbe487
- clm_fd20928cf36dd687d6c27a895a787fd780ad987e842f5004264589b6d33cbced
maturity: draft
page_id: pg_6af918a183ed56b18c5eeb705f42e4b2
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_d2070ba8873159f2bba6a794213032c0
title: rivet-dev/sandbox-agent/README.md @ bbc195cc3fb5
updated_at: '2026-09-14T02:36:10Z'
---

# rivet-dev/sandbox-agent/README.md @ bbc195cc3fb5

<!-- rcw:begin owner=source:src_d2070ba8873159f2bba6a794213032c0 block=evidence -->
- An experimental OpenCode compatibility layer lets OpenCode CLI, SDK, or web UI connect to control agents through OpenCode tooling; CLAUDE.md references an /opencode/* surface when enabled. [@claim:clm_025330e06eb33b0b34663592c480e4a6c7d92c3a35699d0d490c734770ed3cbb]
- The product exposes a single HTTP API with SSE streaming that normalizes different coding agents' proprietary APIs, so integrations can swap agents via configuration rather than code changes. [@claim:clm_15175ee4db2049a588eb0d4805f15d96e35df34aa512a6026abbc6f404c93dc8]
- A skill for the product can be installed via 'npx skills add rivet-dev/skills -s sandbox-agent' or the bunx equivalent. [@claim:clm_16d113dec9f7509298c8c01a10bc131339d728df168ce9376f23ad98867540d9]
- The TypeScript SDK supports embedded mode via SandboxAgent.start() and remote server mode via SandboxAgent.connect() with a baseUrl and token, and offers methods like listAgents, createSession, postMessage, and streamEvents. [@claim:clm_3b99eb62e5f03b235d5b8f0a137a788a2fc0444bb7b473a4c6f7336adaee8f05]
- The server is implemented as a single static Rust binary, chosen for fast startup and predictable memory usage so it can run in sandboxes or CI without a Node.js runtime. [@claim:clm_5699c7bdc6e84a2368dff746f65401fe9b415f28da3374d59a37474bf3293576]
- The SDK does not persist session data itself; events stream in a universal JSON schema that consumers are expected to store externally, e.g. in Postgres, ClickHouse, or Rivet. [@claim:clm_78cd62e388ca61b9205ba5caa1357221fd1591520093c04db81b49dab1015226]
- Agent binaries are installed lazily on first use by default, with an optional 'sandbox-agent install-agent --all' command to preinstall them. [@claim:clm_941e2d550bd396066cd667c7725808f6aedd6502c061458f50d88467876322b8]
- The server is started with a token for auth (e.g. 'sandbox-agent server --token ... --host 127.0.0.1 --port 2468'), and a --no-token flag exists to disable auth locally. [@claim:clm_a9e4a25e4a74a1fa96bc095f1a7408e6a1dc215e99ebffb61a659b79bd0eb7af]
- The project comprises a Rust daemon ('sandbox-agent server') exposing HTTP+SSE, a TypeScript SDK with embedded and server modes, a built-in Inspector UI, and a CLI mirroring the HTTP endpoints. [@claim:clm_bd54df6b2cc9905d7aa78b3796af6cc63e894512520caad0bb1888cfa90fd357]
- The README explicitly lists out-of-scope areas: on-disk session storage, direct LLM wrappers, git repo management, and a sandbox-provider API abstraction layer. [@claim:clm_be02c656aaba0703376e1247050b6fa12502604b784adc5b15d8e56c68bbe487]
- A built-in Inspector UI for debugging sessions and events is served at a path like http://localhost:2468/ui/. [@claim:clm_fd20928cf36dd687d6c27a895a787fd780ad987e842f5004264589b6d33cbced]
<!-- rcw:end owner=source:src_d2070ba8873159f2bba6a794213032c0 block=evidence -->

## Researcher notes

