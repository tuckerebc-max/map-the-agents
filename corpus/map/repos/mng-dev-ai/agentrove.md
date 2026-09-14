# mng-dev-ai/agentrove

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 53ef8fc0dea3 @ 7ceeacd8ec0fc1b5

## Summary (orientation draft, not independently verified)

README-only evidence for Agentrove, a self-hosted workspace that orchestrates multiple coding agents via ACP adapters and a bundled MCP server, shipped as Docker web app, macOS desktop, and iOS client. No code inspected; claims are documentation-based.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] Agents are run through ACP adapters, and each workspace gets its own Docker or host sandbox. -- evidence: [README.md#L14-L22](https://github.com/Mng-dev-ai/agentrove/blob/53ef8fc0dea3a29005d341ad1031014aa07e56b8/README.md#L14-L22)
  - [observation/documented] The stack is React 19, TypeScript, Vite, Tailwind, Monaco, and xterm.js on the frontend; FastAPI, SQLAlchemy, SQLite, and Redis on the backend; ACP with Docker or host sandboxes at runtime. -- evidence: [README.md#L158-L160](https://github.com/Mng-dev-ai/agentrove/blob/53ef8fc0dea3a29005d341ad1031014aa07e56b8/README.md#L158-L160)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: building the iOS app from source requires macOS with Xcode, Rust iOS targets via rustup, and CocoaPods; a helper script (npm run ios:install) builds, signs, exports, and installs using APPLE_DEVELOPMENT_TEAM. -- evidence: [README.md#L118-L121](https://github.com/Mng-dev-ai/agentrove/blob/53ef8fc0dea3a29005d341ad1031014aa07e56b8/README.md#L118-L121), [README.md#L123-L127](https://github.com/Mng-dev-ai/agentrove/blob/53ef8fc0dea3a29005d341ad1031014aa07e56b8/README.md#L123-L127), [README.md#L88-L89](https://github.com/Mng-dev-ai/agentrove/blob/53ef8fc0dea3a29005d341ad1031014aa07e56b8/README.md#L88-L89)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] Agentrove is a self-hosted AI coding workspace that runs and orchestrates Antigravity, Claude Code, Codex, Copilot, Cursor, Grok, and OpenCode agents from one interface. -- evidence: [README.md#L3-L3](https://github.com/Mng-dev-ai/agentrove/blob/53ef8fc0dea3a29005d341ad1031014aa07e56b8/README.md#L3-L3)
  - [observation/documented] The workspace combines chat, code editor, terminal, file tree, diffs, secrets, and git tools, and streams agent sessions with cancellation, permission prompts, queued follow-ups, file mentions, slash commands, and attachments. -- evidence: [README.md#L14-L22](https://github.com/Mng-dev-ai/agentrove/blob/53ef8fc0dea3a29005d341ad1031014aa07e56b8/README.md#L14-L22)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (4 claim(s)):
  - [observation/documented] A bundled MCP server exposes the instance as tools such as send_message, get_messages, list_models, and list_personas, letting any chat's agent act as an orchestrator that decomposes work and reviews results. -- evidence: [README.md#L26-L26](https://github.com/Mng-dev-ai/agentrove/blob/53ef8fc0dea3a29005d341ad1031014aa07e56b8/README.md#L26-L26)
  - [observation/documented] Sub-threads created via send_message(parent_chat_id=...) are worker chats grouped under the lead in the same workspace and branch, and stay flat with no nesting. -- evidence: [README.md#L30-L34](https://github.com/Mng-dev-ai/agentrove/blob/53ef8fc0dea3a29005d341ad1031014aa07e56b8/README.md#L30-L34)
- tools-permissions (1 claim(s)):
  - [observation/documented] Orchestrated turns run in the agent's full-execution mode, so workers finish without permission prompts. -- evidence: [README.md#L30-L34](https://github.com/Mng-dev-ai/agentrove/blob/53ef8fc0dea3a29005d341ad1031014aa07e56b8/README.md#L30-L34)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] Quick start requires Docker and Docker Compose, cloning the repo, copying .env.example to .env, and setting SECRET_KEY before docker compose up -d; the app is served at localhost:3000. -- evidence: [README.md#L51-L51](https://github.com/Mng-dev-ai/agentrove/blob/53ef8fc0dea3a29005d341ad1031014aa07e56b8/README.md#L51-L51), [README.md#L45-L49](https://github.com/Mng-dev-ai/agentrove/blob/53ef8fc0dea3a29005d341ad1031014aa07e56b8/README.md#L45-L49), [README.md#L59-L61](https://github.com/Mng-dev-ai/agentrove/blob/53ef8fc0dea3a29005d341ad1031014aa07e56b8/README.md#L59-L61), [README.md#L63-L63](https://github.com/Mng-dev-ai/agentrove/blob/53ef8fc0dea3a29005d341ad1031014aa07e56b8/README.md#L63-L63), [README.md#L42-L43](https://github.com/Mng-dev-ai/agentrove/blob/53ef8fc0dea3a29005d341ad1031014aa07e56b8/README.md#L42-L43)
- limitations: unknown (no source-linked claim submitted for this facet)
More evidence: [full detail](agentrove.detail.md)

Metadata and full claim list: [full detail](agentrove.detail.md)
Human notes ([notes](agentrove.notes.md), never overwritten by build)

[Back to map index](../../index.md)
