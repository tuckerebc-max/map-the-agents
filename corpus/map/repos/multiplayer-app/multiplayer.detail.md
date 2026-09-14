# multiplayer-app/multiplayer -- full detail

[Back to orientation](multiplayer.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/multiplayer-app/multiplayer/7ae811671d5a07b00afe4e7f67826fb7c82de5bf/f0cb7f49c8387c37.json](../../../wiki/dossiers/multiplayer-app/multiplayer/7ae811671d5a07b00afe4e7f67826fb7c82de5bf/f0cb7f49c8387c37.json)

## specifications (1 claim(s))

- [observation/documented] Multiplayer is described as an open-source debugging agent that connects a developer's coding agent to production to fix application bugs automatically. -- evidence: [README.md#L28-L32](https://github.com/multiplayer-app/multiplayer/blob/7ae811671d5a07b00afe4e7f67826fb7c82de5bf/README.md#L28-L32), [README.md#L46-L46](https://github.com/multiplayer-app/multiplayer/blob/7ae811671d5a07b00afe4e7f67826fb7c82de5bf/README.md#L46-L46) (`clm_9c1ad89c8f46e240336f2454221f6c2e9b7f05c775542c7ba11ec0be6d2e299e`)

## components (2 claim(s))

- [observation/documented] The repository contains a web app, backend services, data pipelines, storage integrations, and shared libraries powering the Multiplayer platform. -- evidence: [README.md#L52-L52](https://github.com/multiplayer-app/multiplayer/blob/7ae811671d5a07b00afe4e7f67826fb7c82de5bf/README.md#L52-L52) (`clm_930f73bee7cacaa0df000937dd0d2fcca5bd1078fb15da4608deb427225cc117`)
- [observation/documented] Repo layout includes clients/multiplayer-web-app, services/* for API, auth, git, collaboration, notifications, assets, versioning and radar workflows, plus libs/* and scripts/*. -- evidence: [README.md#L93-L97](https://github.com/multiplayer-app/multiplayer/blob/7ae811671d5a07b00afe4e7f67826fb7c82de5bf/README.md#L93-L97) (`clm_cdc51128f3e2d989feac77464b451f7a468884558dee427ff8def8a25a1bd43d`)

## design-choices (2 claim(s))

- [observation/documented] The agent runs locally alongside coding agents such as Claude Code (GA), Codex (private beta), and Copilot (private beta), and on error detection sends runtime session data to the coding agent, handling triage, prompting, PR creation and notification. -- evidence: [README.md#L48-L48](https://github.com/multiplayer-app/multiplayer/blob/7ae811671d5a07b00afe4e7f67826fb7c82de5bf/README.md#L48-L48) (`clm_8a6f5a46cb40e5d335dc9cfcff2e4a2d370d2c568c0f2dd2e252a0e13a45fdc7`)
- [observation/documented] Session data fed to coding agents is claimed to be full-stack, auto-correlated, unsampled, and to include request/response content and headers from all system components. -- evidence: [README.md#L50-L50](https://github.com/multiplayer-app/multiplayer/blob/7ae811671d5a07b00afe4e7f67826fb7c82de5bf/README.md#L50-L50) (`clm_a132356a7043d1fe2bb67761c055256c8e36a297a8035f74da8f8e0a869c3560`)

## workflows (4 claim(s))

- [observation/documented] Repository development practice: Docker Compose production deployment copies .env.example into docker/.env, fills credentials, then runs docker compose with docker-compose.prod.yml; services use health checks and start in dependency order. -- evidence: [README.md#L130-L130](https://github.com/multiplayer-app/multiplayer/blob/7ae811671d5a07b00afe4e7f67826fb7c82de5bf/README.md#L130-L130), [README.md#L118-L120](https://github.com/multiplayer-app/multiplayer/blob/7ae811671d5a07b00afe4e7f67826fb7c82de5bf/README.md#L118-L120), [README.md#L126-L128](https://github.com/multiplayer-app/multiplayer/blob/7ae811671d5a07b00afe4e7f67826fb7c82de5bf/README.md#L126-L128), [README.md#L122-L122](https://github.com/multiplayer-app/multiplayer/blob/7ae811671d5a07b00afe4e7f67826fb7c82de5bf/README.md#L122-L122), [README.md#L116-L116](https://github.com/multiplayer-app/multiplayer/blob/7ae811671d5a07b00afe4e7f67826fb7c82de5bf/README.md#L116-L116) (`clm_f0a4fee49a58a7a1147e950b7b8bb0568168e83c2514495f4833f5139beb1b9f`)
- [observation/documented] Repository development practice: local PM2 development requires pnpm install, .env setup, a dev compose file for infrastructure, then pnpm start:pm2, which builds libraries, runs migrations, seeds roles, and launches services. -- evidence: [README.md#L169-L169](https://github.com/multiplayer-app/multiplayer/blob/7ae811671d5a07b00afe4e7f67826fb7c82de5bf/README.md#L169-L169), [README.md#L159-L161](https://github.com/multiplayer-app/multiplayer/blob/7ae811671d5a07b00afe4e7f67826fb7c82de5bf/README.md#L159-L161), [README.md#L143-L145](https://github.com/multiplayer-app/multiplayer/blob/7ae811671d5a07b00afe4e7f67826fb7c82de5bf/README.md#L143-L145), [README.md#L149-L151](https://github.com/multiplayer-app/multiplayer/blob/7ae811671d5a07b00afe4e7f67826fb7c82de5bf/README.md#L149-L151), [README.md#L165-L167](https://github.com/multiplayer-app/multiplayer/blob/7ae811671d5a07b00afe4e7f67826fb7c82de5bf/README.md#L165-L167) (`clm_a8aa9953247d7209ec5414970a1b89df5303014d9f807c879b18eae2472f8549`)
- [observation/documented] Repository development practice: contributors branch from latest development (e.g. MP-1234), merge back into development, then development into main for release; conventional commits are enforced by a pre-commit hook. -- evidence: [CONTRIBUTING.md#L15-L15](https://github.com/multiplayer-app/multiplayer/blob/7ae811671d5a07b00afe4e7f67826fb7c82de5bf/CONTRIBUTING.md#L15-L15), [CONTRIBUTING.md#L5-L7](https://github.com/multiplayer-app/multiplayer/blob/7ae811671d5a07b00afe4e7f67826fb7c82de5bf/CONTRIBUTING.md#L5-L7), [CONTRIBUTING.md#L17-L18](https://github.com/multiplayer-app/multiplayer/blob/7ae811671d5a07b00afe4e7f67826fb7c82de5bf/CONTRIBUTING.md#L17-L18), [CONTRIBUTING.md#L11-L11](https://github.com/multiplayer-app/multiplayer/blob/7ae811671d5a07b00afe4e7f67826fb7c82de5bf/CONTRIBUTING.md#L11-L11) (`clm_aa49c2c89162bb49ebec5d575300f0da5a15ad24f6315c9989c665cc11d4a0ad`)
- [observation/documented] Repository development practice: AGENTS.md instructs contributing agents to act as a blunt senior/principal engineer giving direct, critical, unsweetened technical feedback. -- evidence: [AGENTS.md#L3-L13](https://github.com/multiplayer-app/multiplayer/blob/7ae811671d5a07b00afe4e7f67826fb7c82de5bf/AGENTS.md#L3-L13), [AGENTS.md#L1-L1](https://github.com/multiplayer-app/multiplayer/blob/7ae811671d5a07b00afe4e7f67826fb7c82de5bf/AGENTS.md#L1-L1) (`clm_4bb7a1da048c1eb7f1605b695731d2ede0d3962bad425ea99714177859583ed5`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] A separate Multiplayer CLI provides a terminal UI for working through sessions, inspecting context, asking an agent to debug, and turning fixes into branches or pull requests. -- evidence: [README.md#L71-L74](https://github.com/multiplayer-app/multiplayer/blob/7ae811671d5a07b00afe4e7f67826fb7c82de5bf/README.md#L71-L74), [README.md#L56-L61](https://github.com/multiplayer-app/multiplayer/blob/7ae811671d5a07b00afe4e7f67826fb7c82de5bf/README.md#L56-L61), [README.md#L65-L65](https://github.com/multiplayer-app/multiplayer/blob/7ae811671d5a07b00afe4e7f67826fb7c82de5bf/README.md#L65-L65) (`clm_120dc89be84fef5e91fcbe8bdcc567786ea1dcfa1a8bd6dfb231ca5b74590b81`)
- [observation/documented] A web dashboard offers a shared workspace to review agent conversations, session recordings, issues, replay user journeys, and annotate recordings with notes. -- evidence: [README.md#L84-L89](https://github.com/multiplayer-app/multiplayer/blob/7ae811671d5a07b00afe4e7f67826fb7c82de5bf/README.md#L84-L89), [README.md#L80-L80](https://github.com/multiplayer-app/multiplayer/blob/7ae811671d5a07b00afe4e7f67826fb7c82de5bf/README.md#L80-L80) (`clm_b4660a30e56ee461ecade86222990a9d734801c5161ebd189b054ef63e56abe0`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (3 claim(s))

- [observation/documented] The self-hostable stack uses Docker Compose, PM2, Turborepo, MongoDB, RabbitMQ, Redis, Kafka, ClickHouse, MinIO, OpenSearch, and OpenTelemetry. -- evidence: [README.md#L56-L61](https://github.com/multiplayer-app/multiplayer/blob/7ae811671d5a07b00afe4e7f67826fb7c82de5bf/README.md#L56-L61) (`clm_3736261d9eb3de1ca1ea8a2b456feb36d01698ed77cb6ed0ad280ff1ecb24c22`)
- [observation/documented] Requirements are Node.js v22+, pnpm v10+, Docker and Docker Compose, and PM2 with bunyan; Docker Compose deployment needs only Docker and Docker Compose. -- evidence: [README.md#L106-L106](https://github.com/multiplayer-app/multiplayer/blob/7ae811671d5a07b00afe4e7f67826fb7c82de5bf/README.md#L106-L106), [README.md#L108-L108](https://github.com/multiplayer-app/multiplayer/blob/7ae811671d5a07b00afe4e7f67826fb7c82de5bf/README.md#L108-L108), [README.md#L101-L104](https://github.com/multiplayer-app/multiplayer/blob/7ae811671d5a07b00afe4e7f67826fb7c82de5bf/README.md#L101-L104) (`clm_36ddd863f14c1d1f7858984073d9e33d58d0109ff79e1272d5379cd7909f44dc`)
- [observation/documented] Related projects include session recorder SDKs for JavaScript (browser, Node, React, React Native), Go, .NET, Python, Ruby, and Java, plus the multiplayer-cli repository. -- evidence: [README.md#L195-L204](https://github.com/multiplayer-app/multiplayer/blob/7ae811671d5a07b00afe4e7f67826fb7c82de5bf/README.md#L195-L204) (`clm_959619d7f9d17a4f440bccf33da3c1429dfa0a134b434f47c4520268c54de170`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

Superseded claim IDs (kept as history): clm_71c88d78e55f7bbe99bb3d61f6a30211910438bca77fa7399ad32e83cb63ed43

