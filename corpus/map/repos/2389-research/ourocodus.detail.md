# 2389-research/ourocodus -- full detail

[Back to orientation](ourocodus.md)

## Origins

- alltheagents.org-site-pages

## Projects

- Observatory

Full evidence record (JSON): [wiki/dossiers/2389-research/ourocodus/00bfe36ef93024f4e3ff8c85f68b4b0ca3a243bc/fbb642909c8dc3bb.json](../../../wiki/dossiers/2389-research/ourocodus/00bfe36ef93024f4e3ff8c85f68b4b0ca3a243bc/fbb642909c8dc3bb.json)

## specifications (2 claim(s))

- [observation/documented] The PRD specifies an HTTP control plane providing REST endpoints for session management, agent lifecycle, event log access, health checks, and serving static web UI files. -- evidence: [docs/prd/api.md#L9-L13](https://github.com/2389-research/ourocodus/blob/00bfe36ef93024f4e3ff8c85f68b4b0ca3a243bc/docs/prd/api.md#L9-L13), [docs/prd/api.md#L5-L5](https://github.com/2389-research/ourocodus/blob/00bfe36ef93024f4e3ff8c85f68b4b0ca3a243bc/docs/prd/api.md#L5-L5) (`clm_24df3fd603b4e4051167965eea00be03f2d866c6725924ce96854268bffb6d79`)
- [observation/documented] The PRD specifies Session, Agent, and Event data models with JSON fields including status, container_id, chunks_completed, and payload. -- evidence: [docs/prd/api.md#L215-L226](https://github.com/2389-research/ourocodus/blob/00bfe36ef93024f4e3ff8c85f68b4b0ca3a243bc/docs/prd/api.md#L215-L226), [docs/prd/api.md#L244-L253](https://github.com/2389-research/ourocodus/blob/00bfe36ef93024f4e3ff8c85f68b4b0ca3a243bc/docs/prd/api.md#L244-L253), [docs/prd/api.md#L230-L240](https://github.com/2389-research/ourocodus/blob/00bfe36ef93024f4e3ff8c85f68b4b0ca3a243bc/docs/prd/api.md#L230-L240) (`clm_bcaae0760238d545f6457ef2dcbd0ea9967782595481669884629ec568cf9b16`)

## components (1 claim(s))

- [observation/documented] The repository layout includes a relay WebSocket server, a CLI, an echo test agent under cmd/, shared packages in pkg/, and a PWA frontend in web/. -- evidence: [README.md#L185-L195](https://github.com/2389-research/ourocodus/blob/00bfe36ef93024f4e3ff8c85f68b4b0ca3a243bc/README.md#L185-L195) (`clm_5864c5808c2f2a626db14eb782ec691ab791a6fc411af0065903433a1c950661`)

## design-choices (3 claim(s))

- [observation/documented] Each AgentSession has three isolation layers (git worktree, read-only credentials, Docker container) orchestrated by an AgentContainerLauncher. -- evidence: [docs/architecture/ARCHITECTURE.md#L13-L17](https://github.com/2389-research/ourocodus/blob/00bfe36ef93024f4e3ff8c85f68b4b0ca3a243bc/docs/architecture/ARCHITECTURE.md#L13-L17), [docs/architecture/ARCHITECTURE.md#L44-L44](https://github.com/2389-research/ourocodus/blob/00bfe36ef93024f4e3ff8c85f68b4b0ca3a243bc/docs/architecture/ARCHITECTURE.md#L44-L44), [docs/architecture/ARCHITECTURE.md#L46-L46](https://github.com/2389-research/ourocodus/blob/00bfe36ef93024f4e3ff8c85f68b4b0ca3a243bc/docs/architecture/ARCHITECTURE.md#L46-L46) (`clm_0480c25b52d33b5fbdda40c1ef3b3a383e561a89b9eefffbf46288b2e3978741`)
- [observation/documented] ACP processes can run as host processes via os/exec (default) or inside agent containers via docker exec, selected by the OUROCODUS_ACP_RUNTIME variable. -- evidence: [README.md#L44-L49](https://github.com/2389-research/ourocodus/blob/00bfe36ef93024f4e3ff8c85f68b4b0ca3a243bc/README.md#L44-L49) (`clm_8af410e0187b521fa235b3e804ce457539f72784d64ff2707cc4688db3699ed2`)
- [observation/documented] When NATS is enabled, the system auto-creates SESSION_EVENTS and WORK_RESULTS JetStream streams with 7-day retention and 100K message limits, using a documented topic naming convention. -- evidence: [README.md#L324-L326](https://github.com/2389-research/ourocodus/blob/00bfe36ef93024f4e3ff8c85f68b4b0ca3a243bc/README.md#L324-L326), [README.md#L320-L322](https://github.com/2389-research/ourocodus/blob/00bfe36ef93024f4e3ff8c85f68b4b0ca3a243bc/README.md#L320-L322), [README.md#L318-L318](https://github.com/2389-research/ourocodus/blob/00bfe36ef93024f4e3ff8c85f68b4b0ca3a243bc/README.md#L318-L318), [README.md#L330-L333](https://github.com/2389-research/ourocodus/blob/00bfe36ef93024f4e3ff8c85f68b4b0ca3a243bc/README.md#L330-L333) (`clm_70e1749ccdeef560e19181e7a5c2f6ccede8259c96aac66937cc5b1a0b0de85b`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: CI runs two GitHub Actions workflows on PRs and pushes to main, covering builds, go test, golangci-lint, gofmt, shellcheck, and smoke/integration tests; optional pre-commit hooks run gofumpt, go vet, and go mod tidy. -- evidence: [README.md#L216-L218](https://github.com/2389-research/ourocodus/blob/00bfe36ef93024f4e3ff8c85f68b4b0ca3a243bc/README.md#L216-L218), [README.md#L258-L262](https://github.com/2389-research/ourocodus/blob/00bfe36ef93024f4e3ff8c85f68b4b0ca3a243bc/README.md#L258-L262), [README.md#L243-L243](https://github.com/2389-research/ourocodus/blob/00bfe36ef93024f4e3ff8c85f68b4b0ca3a243bc/README.md#L243-L243), [README.md#L203-L203](https://github.com/2389-research/ourocodus/blob/00bfe36ef93024f4e3ff8c85f68b4b0ca3a243bc/README.md#L203-L203), [README.md#L207-L212](https://github.com/2389-research/ourocodus/blob/00bfe36ef93024f4e3ff8c85f68b4b0ca3a243bc/README.md#L207-L212) (`clm_623b889fee4087df44caf926c9d42cf08f0cd65157303b41bdab7db9cf23edbc`)
- [observation/documented] Repository development practice: contributors are directed to install mise, run mise install, and work through GitHub issues ordered by dependency with acceptance criteria. -- evidence: [README.md#L475-L479](https://github.com/2389-research/ourocodus/blob/00bfe36ef93024f4e3ff8c85f68b4b0ca3a243bc/README.md#L475-L479), [README.md#L471-L471](https://github.com/2389-research/ourocodus/blob/00bfe36ef93024f4e3ff8c85f68b4b0ca3a243bc/README.md#L471-L471) (`clm_3a6490b051ee68bd24de91a39b06e745905e262aa75aa0d5a1637348db93426d`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The documented REST API includes POST/GET/DELETE /api/sessions, GET /api/agents, event tailing and SSE streaming at /api/events, plus /health and /api/info endpoints. -- evidence: [docs/prd/api.md#L55-L56](https://github.com/2389-research/ourocodus/blob/00bfe36ef93024f4e3ff8c85f68b4b0ca3a243bc/docs/prd/api.md#L55-L56), [docs/prd/api.md#L179-L180](https://github.com/2389-research/ourocodus/blob/00bfe36ef93024f4e3ff8c85f68b4b0ca3a243bc/docs/prd/api.md#L179-L180), [docs/prd/api.md#L35-L37](https://github.com/2389-research/ourocodus/blob/00bfe36ef93024f4e3ff8c85f68b4b0ca3a243bc/docs/prd/api.md#L35-L37), [docs/prd/api.md#L167-L169](https://github.com/2389-research/ourocodus/blob/00bfe36ef93024f4e3ff8c85f68b4b0ca3a243bc/docs/prd/api.md#L167-L169), [docs/prd/api.md#L90-L91](https://github.com/2389-research/ourocodus/blob/00bfe36ef93024f4e3ff8c85f68b4b0ca3a243bc/docs/prd/api.md#L90-L91), [docs/prd/api.md#L147-L148](https://github.com/2389-research/ourocodus/blob/00bfe36ef93024f4e3ff8c85f68b4b0ca3a243bc/docs/prd/api.md#L147-L148), [docs/prd/api.md#L100-L101](https://github.com/2389-research/ourocodus/blob/00bfe36ef93024f4e3ff8c85f68b4b0ca3a243bc/docs/prd/api.md#L100-L101), [docs/prd/api.md#L192-L193](https://github.com/2389-research/ourocodus/blob/00bfe36ef93024f4e3ff8c85f68b4b0ca3a243bc/docs/prd/api.md#L192-L193) (`clm_44433d7a980c1e24c96eff57ece50b171a39671aceae7ac5290c69099536242e`)
- [observation/documented] The API spec defines structured error responses with codes such as SESSION_NOT_FOUND, and the demo documentation distinguishes recoverable from non-recoverable errors. -- evidence: [docs/prd/api.md#L310-L316](https://github.com/2389-research/ourocodus/blob/00bfe36ef93024f4e3ff8c85f68b4b0ca3a243bc/docs/prd/api.md#L310-L316), [README.md#L444-L447](https://github.com/2389-research/ourocodus/blob/00bfe36ef93024f4e3ff8c85f68b4b0ca3a243bc/README.md#L444-L447), [README.md#L442-L442](https://github.com/2389-research/ourocodus/blob/00bfe36ef93024f4e3ff8c85f68b4b0ca3a243bc/README.md#L442-L442) (`clm_1b34a7debc1311954e67f6d350aa3217f5b96375723b93cfe74a8f3516d92fa1`)
- [observation/documented] An interactive REPL demo supports session creation, agent spawning, messaging, and agent listing without requiring an API key by using an echo agent. -- evidence: [README.md#L362-L367](https://github.com/2389-research/ourocodus/blob/00bfe36ef93024f4e3ff8c85f68b4b0ca3a243bc/README.md#L362-L367), [README.md#L345-L346](https://github.com/2389-research/ourocodus/blob/00bfe36ef93024f4e3ff8c85f68b4b0ca3a243bc/README.md#L345-L346), [README.md#L341-L341](https://github.com/2389-research/ourocodus/blob/00bfe36ef93024f4e3ff8c85f68b4b0ca3a243bc/README.md#L341-L341) (`clm_9939537d833031f7b1ea9333f9e711c4610755952b714cd6de4a250a36b4c2a7`)

## memory-state (1 claim(s))

- [observation/documented] The API server uses in-memory state with reconstruction from an event log at startup, reconnecting to NATS and Docker and querying running agent containers. -- evidence: [docs/prd/api.md#L270-L274](https://github.com/2389-research/ourocodus/blob/00bfe36ef93024f4e3ff8c85f68b4b0ca3a243bc/docs/prd/api.md#L270-L274), [docs/prd/api.md#L257-L257](https://github.com/2389-research/ourocodus/blob/00bfe36ef93024f4e3ff8c85f68b4b0ca3a243bc/docs/prd/api.md#L257-L257) (`clm_b7ca3efcea9d777902b74df8b5c7e0ce56435235d244deacd8b9eb72189eddd2`)

## orchestration (1 claim(s))

- [observation/documented] The relay spawns multiple concurrent agents with user-chosen identifiers; agents can be spawned or terminated independently, and one agent's failure does not terminate the session. -- evidence: [docs/architecture/ARCHITECTURE.md#L35-L36](https://github.com/2389-research/ourocodus/blob/00bfe36ef93024f4e3ff8c85f68b4b0ca3a243bc/docs/architecture/ARCHITECTURE.md#L35-L36), [docs/architecture/ARCHITECTURE.md#L38-L42](https://github.com/2389-research/ourocodus/blob/00bfe36ef93024f4e3ff8c85f68b4b0ca3a243bc/docs/architecture/ARCHITECTURE.md#L38-L42), [README.md#L69-L69](https://github.com/2389-research/ourocodus/blob/00bfe36ef93024f4e3ff8c85f68b4b0ca3a243bc/README.md#L69-L69) (`clm_750f941f7ad8c7803cba3d1d6a3997e3781df6d1a7567df52c47f03c262d9f08`)

## tools-permissions (1 claim(s))

- [observation/documented] Container sessions validate workspace mount points to prevent directory traversal, ensuring workspace paths stay under the configured base directory when attaching to existing containers. -- evidence: [README.md#L73-L73](https://github.com/2389-research/ourocodus/blob/00bfe36ef93024f4e3ff8c85f68b4b0ca3a243bc/README.md#L73-L73) (`clm_796d8b7b321878d6eff9da073d865a4e2f3aface18ad3d66cbc4b002edf31b95`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] Documented dependencies include the Docker SDK for Go (Apache 2.0) for container lifecycle management and the NATS Go client, with the API built on Go's net/http stdlib. -- evidence: [docs/prd/api.md#L24-L27](https://github.com/2389-research/ourocodus/blob/00bfe36ef93024f4e3ff8c85f68b4b0ca3a243bc/docs/prd/api.md#L24-L27), [docs/prd/api.md#L358-L362](https://github.com/2389-research/ourocodus/blob/00bfe36ef93024f4e3ff8c85f68b4b0ca3a243bc/docs/prd/api.md#L358-L362), [README.md#L81-L84](https://github.com/2389-research/ourocodus/blob/00bfe36ef93024f4e3ff8c85f68b4b0ca3a243bc/README.md#L81-L84) (`clm_6ca9db23a40886b306ffcb0c64a36667da03806f4990a6f5a7d7dd9dfa96eb26`)
- [observation/documented] NATS with JetStream is optional for event logging; when NATS_URL is unset the relay logs events to stdout and works without it. -- evidence: [README.md#L51-L55](https://github.com/2389-research/ourocodus/blob/00bfe36ef93024f4e3ff8c85f68b4b0ca3a243bc/README.md#L51-L55), [README.md#L282-L282](https://github.com/2389-research/ourocodus/blob/00bfe36ef93024f4e3ff8c85f68b4b0ca3a243bc/README.md#L282-L282) (`clm_c8ac75b6036b3b660bfcf3dc86967612a64469290afeb3ade3db91b39b914034`)

## limitations (1 claim(s))

- [observation/documented] The API spec states the POC has no authentication, is localhost-only, and allows all CORS origins, with API keys, CORS config, and rate limiting deferred to post-POC. -- evidence: [docs/prd/api.md#L351-L354](https://github.com/2389-research/ourocodus/blob/00bfe36ef93024f4e3ff8c85f68b4b0ca3a243bc/docs/prd/api.md#L351-L354), [docs/prd/api.md#L320-L321](https://github.com/2389-research/ourocodus/blob/00bfe36ef93024f4e3ff8c85f68b4b0ca3a243bc/docs/prd/api.md#L320-L321) (`clm_e3e9ce81b66270048c886d8b46679c1d102e1292668bf76c906b2a06877121af`)

## relevance (1 claim(s))

- [observation/documented] The project is at Phase 1 (foundation/proof of concept) focused on validating multi-agent communication and concurrent isolated work; the PWA client is planned while demos exist currently. -- evidence: [README.md#L101-L101](https://github.com/2389-research/ourocodus/blob/00bfe36ef93024f4e3ff8c85f68b4b0ca3a243bc/README.md#L101-L101), [docs/architecture/ARCHITECTURE.md#L7-L11](https://github.com/2389-research/ourocodus/blob/00bfe36ef93024f4e3ff8c85f68b4b0ca3a243bc/docs/architecture/ARCHITECTURE.md#L7-L11), [docs/architecture/ARCHITECTURE.md#L5-L5](https://github.com/2389-research/ourocodus/blob/00bfe36ef93024f4e3ff8c85f68b4b0ca3a243bc/docs/architecture/ARCHITECTURE.md#L5-L5) (`clm_796bcf743257a469b337f9591a1331a8b564054489e3dd088da95d749bebdeab`)

