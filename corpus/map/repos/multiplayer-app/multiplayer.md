# multiplayer-app/multiplayer

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 7ae811671d5a @ f0cb7f49c8387c37

## Summary (orientation draft, not independently verified)

The snapshot is the README/CONTRIBUTING/AGENTS documentation of the Multiplayer self-hostable debugging agent platform, describing its components, deployment options, and contributor workflow. No source code is included in the evidence.

## Source coverage

Source coverage (complete): 3 of 3 candidate file(s) selected; repository tree complete. Claims by basis: 14 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

14 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Multiplayer is described as an open-source debugging agent that connects a developer's coding agent to production to fix application bugs automatically. -- evidence: [README.md#L28-L32](https://github.com/multiplayer-app/multiplayer/blob/7ae811671d5a07b00afe4e7f67826fb7c82de5bf/README.md#L28-L32), [README.md#L46-L46](https://github.com/multiplayer-app/multiplayer/blob/7ae811671d5a07b00afe4e7f67826fb7c82de5bf/README.md#L46-L46)
- components (2 claim(s)):
  - [observation/documented] The repository contains a web app, backend services, data pipelines, storage integrations, and shared libraries powering the Multiplayer platform. -- evidence: [README.md#L52-L52](https://github.com/multiplayer-app/multiplayer/blob/7ae811671d5a07b00afe4e7f67826fb7c82de5bf/README.md#L52-L52)
  - [observation/documented] Repo layout includes clients/multiplayer-web-app, services/* for API, auth, git, collaboration, notifications, assets, versioning and radar workflows, plus libs/* and scripts/*. -- evidence: [README.md#L93-L97](https://github.com/multiplayer-app/multiplayer/blob/7ae811671d5a07b00afe4e7f67826fb7c82de5bf/README.md#L93-L97)
- design-choices (2 claim(s)):
  - [observation/documented] The agent runs locally alongside coding agents such as Claude Code (GA), Codex (private beta), and Copilot (private beta), and on error detection sends runtime session data to the coding agent, handling triage, prompting, PR creation and notification. -- evidence: [README.md#L48-L48](https://github.com/multiplayer-app/multiplayer/blob/7ae811671d5a07b00afe4e7f67826fb7c82de5bf/README.md#L48-L48)
  - [observation/documented] Session data fed to coding agents is claimed to be full-stack, auto-correlated, unsampled, and to include request/response content and headers from all system components. -- evidence: [README.md#L50-L50](https://github.com/multiplayer-app/multiplayer/blob/7ae811671d5a07b00afe4e7f67826fb7c82de5bf/README.md#L50-L50)
- workflows (4 claim(s)):
  - [observation/documented] Repository development practice: Docker Compose production deployment copies .env.example into docker/.env, fills credentials, then runs docker compose with docker-compose.prod.yml; services use health checks and start in dependency order. -- evidence: [README.md#L130-L130](https://github.com/multiplayer-app/multiplayer/blob/7ae811671d5a07b00afe4e7f67826fb7c82de5bf/README.md#L130-L130), [README.md#L118-L120](https://github.com/multiplayer-app/multiplayer/blob/7ae811671d5a07b00afe4e7f67826fb7c82de5bf/README.md#L118-L120), [README.md#L126-L128](https://github.com/multiplayer-app/multiplayer/blob/7ae811671d5a07b00afe4e7f67826fb7c82de5bf/README.md#L126-L128), [README.md#L122-L122](https://github.com/multiplayer-app/multiplayer/blob/7ae811671d5a07b00afe4e7f67826fb7c82de5bf/README.md#L122-L122), [README.md#L116-L116](https://github.com/multiplayer-app/multiplayer/blob/7ae811671d5a07b00afe4e7f67826fb7c82de5bf/README.md#L116-L116)
  - [observation/documented] Repository development practice: local PM2 development requires pnpm install, .env setup, a dev compose file for infrastructure, then pnpm start:pm2, which builds libraries, runs migrations, seeds roles, and launches services. -- evidence: [README.md#L169-L169](https://github.com/multiplayer-app/multiplayer/blob/7ae811671d5a07b00afe4e7f67826fb7c82de5bf/README.md#L169-L169), [README.md#L159-L161](https://github.com/multiplayer-app/multiplayer/blob/7ae811671d5a07b00afe4e7f67826fb7c82de5bf/README.md#L159-L161), [README.md#L143-L145](https://github.com/multiplayer-app/multiplayer/blob/7ae811671d5a07b00afe4e7f67826fb7c82de5bf/README.md#L143-L145), [README.md#L149-L151](https://github.com/multiplayer-app/multiplayer/blob/7ae811671d5a07b00afe4e7f67826fb7c82de5bf/README.md#L149-L151), [README.md#L165-L167](https://github.com/multiplayer-app/multiplayer/blob/7ae811671d5a07b00afe4e7f67826fb7c82de5bf/README.md#L165-L167)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] A separate Multiplayer CLI provides a terminal UI for working through sessions, inspecting context, asking an agent to debug, and turning fixes into branches or pull requests. -- evidence: [README.md#L71-L74](https://github.com/multiplayer-app/multiplayer/blob/7ae811671d5a07b00afe4e7f67826fb7c82de5bf/README.md#L71-L74), [README.md#L56-L61](https://github.com/multiplayer-app/multiplayer/blob/7ae811671d5a07b00afe4e7f67826fb7c82de5bf/README.md#L56-L61), [README.md#L65-L65](https://github.com/multiplayer-app/multiplayer/blob/7ae811671d5a07b00afe4e7f67826fb7c82de5bf/README.md#L65-L65)
  - [observation/documented] A web dashboard offers a shared workspace to review agent conversations, session recordings, issues, replay user journeys, and annotate recordings with notes. -- evidence: [README.md#L84-L89](https://github.com/multiplayer-app/multiplayer/blob/7ae811671d5a07b00afe4e7f67826fb7c82de5bf/README.md#L84-L89), [README.md#L80-L80](https://github.com/multiplayer-app/multiplayer/blob/7ae811671d5a07b00afe4e7f67826fb7c82de5bf/README.md#L80-L80)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (3 claim(s)):
More evidence: [full detail](multiplayer.detail.md)

Metadata and full claim list: [full detail](multiplayer.detail.md)
Human notes ([notes](multiplayer.notes.md), never overwritten by build)

[Back to map index](../../index.md)
