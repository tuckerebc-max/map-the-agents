# agentsmesh/agentsmesh -- full detail

[Back to orientation](agentsmesh.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/agentsmesh/agentsmesh/1f90b14194d03c353df4f281a05442afe93cae34/d9e238fa0886609c.json](../../../wiki/dossiers/agentsmesh/agentsmesh/1f90b14194d03c353df4f281a05442afe93cae34/d9e238fa0886609c.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] Server side comprises a Go backend (Gin+GORM) handling auth, pod lifecycle, tickets, billing and runner-cert PKI; a WebSocket Relay for terminal data; and a self-hosted Go runner daemon that spawns PTY pods. -- evidence: [README.md#L84-L88](https://github.com/AgentsMesh/AgentsMesh/blob/1f90b14194d03c353df4f281a05442afe93cae34/README.md#L84-L88) (`clm_ea545419cf54b28aff3267fb6248324edbe84867533bc99c44bde783790620b3`)
- [observation/documented] Client side includes a Rust core of 10 crates compiled to WASM for web/desktop and exposed to iOS via UniFFI, plus Next.js web, Electron desktop, SwiftUI/TCA iOS, and a web-admin console. -- evidence: [README.md#L92-L98](https://github.com/AgentsMesh/AgentsMesh/blob/1f90b14194d03c353df4f281a05442afe93cae34/README.md#L92-L98) (`clm_2bc41b0538b7a6939c35d3dbd5362414a141ee6c9e27f65af498680de8231727`)

## design-choices (1 claim(s))

- [observation/documented] The architecture splits control plane from data plane: orchestration travels over gRPC with mTLS while terminal I/O streams through a stateless Relay cluster, so the backend never handles PTY bytes. -- evidence: [README.md#L76-L76](https://github.com/AgentsMesh/AgentsMesh/blob/1f90b14194d03c353df4f281a05442afe93cae34/README.md#L76-L76), [README.md#L63-L63](https://github.com/AgentsMesh/AgentsMesh/blob/1f90b14194d03c353df4f281a05442afe93cae34/README.md#L63-L63) (`clm_998a48c72462952db8470c2aa4302aa850458369df5533595b1fcb1adacd86af`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The runner CLI exposes login (with --headless and --server options), run, and service install/start subcommands. -- evidence: [README.md#L116-L118](https://github.com/AgentsMesh/AgentsMesh/blob/1f90b14194d03c353df4f281a05442afe93cae34/README.md#L116-L118), [README.md#L134-L136](https://github.com/AgentsMesh/AgentsMesh/blob/1f90b14194d03c353df4f281a05442afe93cae34/README.md#L134-L136), [README.md#L128-L130](https://github.com/AgentsMesh/AgentsMesh/blob/1f90b14194d03c353df4f281a05442afe93cae34/README.md#L128-L130), [README.md#L140-L143](https://github.com/AgentsMesh/AgentsMesh/blob/1f90b14194d03c353df4f281a05442afe93cae34/README.md#L140-L143), [README.md#L122-L124](https://github.com/AgentsMesh/AgentsMesh/blob/1f90b14194d03c353df4f281a05442afe93cae34/README.md#L122-L124) (`clm_0d106f000c296b554e29110ea7382c6b5d7bb5bc5e00d2b915d588278142bde6`)
- [observation/documented] Pods communicate over channels with @mentions within a bound mesh topology, and tickets on a Kanban board can be bound to pods with progress and MR/PR tracking. -- evidence: [README.md#L67-L72](https://github.com/AgentsMesh/AgentsMesh/blob/1f90b14194d03c353df4f281a05442afe93cae34/README.md#L67-L72) (`clm_3073488140587ba1b71883fa442aec6c133706190547b3711df2c24474d3665f`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (2 claim(s))

- [observation/documented] Runners advertise capacity (max_concurrent_pods) and pods are scheduled onto a chosen runner or an available one from the pool; each pod gets an isolated Git worktree sandbox, private credentials, and its own branch. -- evidence: [README.md#L55-L61](https://github.com/AgentsMesh/AgentsMesh/blob/1f90b14194d03c353df4f281a05442afe93cae34/README.md#L55-L61) (`clm_544297cb7fd13bf91d01e3b1292e917184328be5a05b2c4de84c8fc6e2bbf06d`)
- [observation/documented] An Autopilot control agent watches a pod, sends the next instruction when it goes idle, enforces iteration caps, keeps decision history, and supports human takeover and handback. -- evidence: [README.md#L55-L61](https://github.com/AgentsMesh/AgentsMesh/blob/1f90b14194d03c353df4f281a05442afe93cae34/README.md#L55-L61), [README.md#L67-L72](https://github.com/AgentsMesh/AgentsMesh/blob/1f90b14194d03c353df4f281a05442afe93cae34/README.md#L67-L72) (`clm_a5a3ccb0fec004a5312a032d70a8370e130b81a2f0f4c8a523f1b52b7bae37d3`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] The stack uses PostgreSQL and Redis, MinIO for S3-compatible storage, Traefik as reverse proxy, JWT for web auth and mTLS for runner connections. -- evidence: [README.md#L231-L242](https://github.com/AgentsMesh/AgentsMesh/blob/1f90b14194d03c353df4f281a05442afe93cae34/README.md#L231-L242) (`clm_cf2a54ee6f4230ba40aa9f35c9c1979e36c325585884fee5ded7b00276fe16f6`)
- [observation/documented] Any terminal-based agent can run; built-in support is documented for Claude Code, Codex CLI, Gemini CLI, Aider, and OpenCode. -- evidence: [README.md#L220-L227](https://github.com/AgentsMesh/AgentsMesh/blob/1f90b14194d03c353df4f281a05442afe93cae34/README.md#L220-L227), [README.md#L218-L218](https://github.com/AgentsMesh/AgentsMesh/blob/1f90b14194d03c353df4f281a05442afe93cae34/README.md#L218-L218) (`clm_e207fcc2a48dcd22c6f07ea244a08c1a60ce2d472de05dc95c581712d7856e99`)

## limitations (1 claim(s))

- [observation/documented] The code is licensed under BSL-1.1: non-production use, copying and modification are allowed, but production use requires a commercial license until the 2030-02-28 change date, after which it becomes GPL-2.0-or-later. -- evidence: [README.md#L273-L273](https://github.com/AgentsMesh/AgentsMesh/blob/1f90b14194d03c353df4f281a05442afe93cae34/README.md#L273-L273), [README.md#L275-L276](https://github.com/AgentsMesh/AgentsMesh/blob/1f90b14194d03c353df4f281a05442afe93cae34/README.md#L275-L276), [README.md#L278-L278](https://github.com/AgentsMesh/AgentsMesh/blob/1f90b14194d03c353df4f281a05442afe93cae34/README.md#L278-L278) (`clm_a97aef40fa55433c2789ee1dde5d931170bf0e3dcb9d6210bf1998323132ab07`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

