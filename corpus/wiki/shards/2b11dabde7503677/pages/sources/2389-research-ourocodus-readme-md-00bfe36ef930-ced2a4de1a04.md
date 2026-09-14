---
access: public
aliases: []
claim_ids:
- clm_1b34a7debc1311954e67f6d350aa3217f5b96375723b93cfe74a8f3516d92fa1
- clm_3a6490b051ee68bd24de91a39b06e745905e262aa75aa0d5a1637348db93426d
- clm_5864c5808c2f2a626db14eb782ec691ab791a6fc411af0065903433a1c950661
- clm_623b889fee4087df44caf926c9d42cf08f0cd65157303b41bdab7db9cf23edbc
- clm_6ca9db23a40886b306ffcb0c64a36667da03806f4990a6f5a7d7dd9dfa96eb26
- clm_70e1749ccdeef560e19181e7a5c2f6ccede8259c96aac66937cc5b1a0b0de85b
- clm_750f941f7ad8c7803cba3d1d6a3997e3781df6d1a7567df52c47f03c262d9f08
- clm_796bcf743257a469b337f9591a1331a8b564054489e3dd088da95d749bebdeab
- clm_796d8b7b321878d6eff9da073d865a4e2f3aface18ad3d66cbc4b002edf31b95
- clm_8af410e0187b521fa235b3e804ce457539f72784d64ff2707cc4688db3699ed2
- clm_9939537d833031f7b1ea9333f9e711c4610755952b714cd6de4a250a36b4c2a7
- clm_c8ac75b6036b3b660bfcf3dc86967612a64469290afeb3ade3db91b39b914034
maturity: draft
page_id: pg_99c328c4da0056ddbe7cced2a4de1a04
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_5336c2953aa0548eb9f3e091a7b50930
title: 2389-research/ourocodus/README.md @ 00bfe36ef930
updated_at: '2026-09-14T01:28:48Z'
---

# 2389-research/ourocodus/README.md @ 00bfe36ef930

<!-- rcw:begin owner=source:src_5336c2953aa0548eb9f3e091a7b50930 block=evidence -->
- The API spec defines structured error responses with codes such as SESSION_NOT_FOUND, and the demo documentation distinguishes recoverable from non-recoverable errors. [@claim:clm_1b34a7debc1311954e67f6d350aa3217f5b96375723b93cfe74a8f3516d92fa1]
- Repository development practice: contributors are directed to install mise, run mise install, and work through GitHub issues ordered by dependency with acceptance criteria. [@claim:clm_3a6490b051ee68bd24de91a39b06e745905e262aa75aa0d5a1637348db93426d]
- The repository layout includes a relay WebSocket server, a CLI, an echo test agent under cmd/, shared packages in pkg/, and a PWA frontend in web/. [@claim:clm_5864c5808c2f2a626db14eb782ec691ab791a6fc411af0065903433a1c950661]
- Repository development practice: CI runs two GitHub Actions workflows on PRs and pushes to main, covering builds, go test, golangci-lint, gofmt, shellcheck, and smoke/integration tests; optional pre-commit hooks run gofumpt, go vet, and go mod tidy. [@claim:clm_623b889fee4087df44caf926c9d42cf08f0cd65157303b41bdab7db9cf23edbc]
- Documented dependencies include the Docker SDK for Go (Apache 2.0) for container lifecycle management and the NATS Go client, with the API built on Go's net/http stdlib. [@claim:clm_6ca9db23a40886b306ffcb0c64a36667da03806f4990a6f5a7d7dd9dfa96eb26]
- When NATS is enabled, the system auto-creates SESSION_EVENTS and WORK_RESULTS JetStream streams with 7-day retention and 100K message limits, using a documented topic naming convention. [@claim:clm_70e1749ccdeef560e19181e7a5c2f6ccede8259c96aac66937cc5b1a0b0de85b]
- The relay spawns multiple concurrent agents with user-chosen identifiers; agents can be spawned or terminated independently, and one agent's failure does not terminate the session. [@claim:clm_750f941f7ad8c7803cba3d1d6a3997e3781df6d1a7567df52c47f03c262d9f08]
- The project is at Phase 1 (foundation/proof of concept) focused on validating multi-agent communication and concurrent isolated work; the PWA client is planned while demos exist currently. [@claim:clm_796bcf743257a469b337f9591a1331a8b564054489e3dd088da95d749bebdeab]
- Container sessions validate workspace mount points to prevent directory traversal, ensuring workspace paths stay under the configured base directory when attaching to existing containers. [@claim:clm_796d8b7b321878d6eff9da073d865a4e2f3aface18ad3d66cbc4b002edf31b95]
- ACP processes can run as host processes via os/exec (default) or inside agent containers via docker exec, selected by the OUROCODUS_ACP_RUNTIME variable. [@claim:clm_8af410e0187b521fa235b3e804ce457539f72784d64ff2707cc4688db3699ed2]
- An interactive REPL demo supports session creation, agent spawning, messaging, and agent listing without requiring an API key by using an echo agent. [@claim:clm_9939537d833031f7b1ea9333f9e711c4610755952b714cd6de4a250a36b4c2a7]
- NATS with JetStream is optional for event logging; when NATS_URL is unset the relay logs events to stdout and works without it. [@claim:clm_c8ac75b6036b3b660bfcf3dc86967612a64469290afeb3ade3db91b39b914034]
<!-- rcw:end owner=source:src_5336c2953aa0548eb9f3e091a7b50930 block=evidence -->

## Researcher notes

