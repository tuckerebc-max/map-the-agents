---
access: public
aliases: []
claim_ids:
- clm_120dc89be84fef5e91fcbe8bdcc567786ea1dcfa1a8bd6dfb231ca5b74590b81
- clm_36ddd863f14c1d1f7858984073d9e33d58d0109ff79e1272d5379cd7909f44dc
- clm_3736261d9eb3de1ca1ea8a2b456feb36d01698ed77cb6ed0ad280ff1ecb24c22
- clm_8a6f5a46cb40e5d335dc9cfcff2e4a2d370d2c568c0f2dd2e252a0e13a45fdc7
- clm_930f73bee7cacaa0df000937dd0d2fcca5bd1078fb15da4608deb427225cc117
- clm_959619d7f9d17a4f440bccf33da3c1429dfa0a134b434f47c4520268c54de170
- clm_9c1ad89c8f46e240336f2454221f6c2e9b7f05c775542c7ba11ec0be6d2e299e
- clm_a132356a7043d1fe2bb67761c055256c8e36a297a8035f74da8f8e0a869c3560
- clm_a8aa9953247d7209ec5414970a1b89df5303014d9f807c879b18eae2472f8549
- clm_b4660a30e56ee461ecade86222990a9d734801c5161ebd189b054ef63e56abe0
- clm_cdc51128f3e2d989feac77464b451f7a468884558dee427ff8def8a25a1bd43d
- clm_f0a4fee49a58a7a1147e950b7b8bb0568168e83c2514495f4833f5139beb1b9f
maturity: draft
page_id: pg_5c095ad6e0dc5c04a7235e28b00c1855
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_0a7fc54499125e508b79fa82eee334ed
title: multiplayer-app/multiplayer/README.md @ 7ae811671d5a
updated_at: '2026-09-14T04:56:06Z'
---

# multiplayer-app/multiplayer/README.md @ 7ae811671d5a

<!-- rcw:begin owner=source:src_0a7fc54499125e508b79fa82eee334ed block=evidence -->
- A separate Multiplayer CLI provides a terminal UI for working through sessions, inspecting context, asking an agent to debug, and turning fixes into branches or pull requests. [@claim:clm_120dc89be84fef5e91fcbe8bdcc567786ea1dcfa1a8bd6dfb231ca5b74590b81]
- Requirements are Node.js v22+, pnpm v10+, Docker and Docker Compose, and PM2 with bunyan; Docker Compose deployment needs only Docker and Docker Compose. [@claim:clm_36ddd863f14c1d1f7858984073d9e33d58d0109ff79e1272d5379cd7909f44dc]
- The self-hostable stack uses Docker Compose, PM2, Turborepo, MongoDB, RabbitMQ, Redis, Kafka, ClickHouse, MinIO, OpenSearch, and OpenTelemetry. [@claim:clm_3736261d9eb3de1ca1ea8a2b456feb36d01698ed77cb6ed0ad280ff1ecb24c22]
- The agent runs locally alongside coding agents such as Claude Code (GA), Codex (private beta), and Copilot (private beta), and on error detection sends runtime session data to the coding agent, handling triage, prompting, PR creation and notification. [@claim:clm_8a6f5a46cb40e5d335dc9cfcff2e4a2d370d2c568c0f2dd2e252a0e13a45fdc7]
- The repository contains a web app, backend services, data pipelines, storage integrations, and shared libraries powering the Multiplayer platform. [@claim:clm_930f73bee7cacaa0df000937dd0d2fcca5bd1078fb15da4608deb427225cc117]
- Related projects include session recorder SDKs for JavaScript (browser, Node, React, React Native), Go, .NET, Python, Ruby, and Java, plus the multiplayer-cli repository. [@claim:clm_959619d7f9d17a4f440bccf33da3c1429dfa0a134b434f47c4520268c54de170]
- Multiplayer is described as an open-source debugging agent that connects a developer's coding agent to production to fix application bugs automatically. [@claim:clm_9c1ad89c8f46e240336f2454221f6c2e9b7f05c775542c7ba11ec0be6d2e299e]
- Session data fed to coding agents is claimed to be full-stack, auto-correlated, unsampled, and to include request/response content and headers from all system components. [@claim:clm_a132356a7043d1fe2bb67761c055256c8e36a297a8035f74da8f8e0a869c3560]
- Repository development practice: local PM2 development requires pnpm install, .env setup, a dev compose file for infrastructure, then pnpm start:pm2, which builds libraries, runs migrations, seeds roles, and launches services. [@claim:clm_a8aa9953247d7209ec5414970a1b89df5303014d9f807c879b18eae2472f8549]
- A web dashboard offers a shared workspace to review agent conversations, session recordings, issues, replay user journeys, and annotate recordings with notes. [@claim:clm_b4660a30e56ee461ecade86222990a9d734801c5161ebd189b054ef63e56abe0]
- Repo layout includes clients/multiplayer-web-app, services/* for API, auth, git, collaboration, notifications, assets, versioning and radar workflows, plus libs/* and scripts/*. [@claim:clm_cdc51128f3e2d989feac77464b451f7a468884558dee427ff8def8a25a1bd43d]
- Repository development practice: Docker Compose production deployment copies .env.example into docker/.env, fills credentials, then runs docker compose with docker-compose.prod.yml; services use health checks and start in dependency order. [@claim:clm_f0a4fee49a58a7a1147e950b7b8bb0568168e83c2514495f4833f5139beb1b9f]
<!-- rcw:end owner=source:src_0a7fc54499125e508b79fa82eee334ed block=evidence -->

## Researcher notes

