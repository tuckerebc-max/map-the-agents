# stagewise-io/stagewise

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 18ac8a27b18c @ 389bf292978597bd

## Summary (orientation draft, not independently verified)

Stagewise is an open-source agentic IDE (Electron browser app) with a built-in coding agent, BYOK model providers, and AGPLv3 licensing; the snapshot is mostly README, versioning, and contributor-guidance documentation with no runtime source code.

## Source coverage

Source coverage (partial): 6 of 9 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications (2 claim(s)):
  - [observation/documented] Stagewise is described as an open-source agentic IDE for developers with a coding agent built in. -- evidence: [README.md#L41-L41](https://github.com/stagewise-io/stagewise/blob/18ac8a27b18c5de4e2d76d03b515cf10186631ca/README.md#L41-L41)
  - [observation/documented] A stagewise Account offers Free, Pro ($20/mo), and Ultra ($200/mo) plans with differing model access and usage limits. -- evidence: [README.md#L82-L86](https://github.com/stagewise-io/stagewise/blob/18ac8a27b18c5de4e2d76d03b515cf10186631ca/README.md#L82-L86)
- components (2 claim(s)):
  - [observation/documented] Recent release notes list features such as provider usage-limit display, external coding agent integrations, Codex worktree support, chat archiving, and isolated dev instances. -- evidence: [.release-notes.md#L5-L13](https://github.com/stagewise-io/stagewise/blob/18ac8a27b18c5de4e2d76d03b515cf10186631ca/.release-notes.md#L5-L13)
  - [observation/documented] Release notes mention ACP session, lifecycle, and approval handling fixes, suggesting the product integrates agents over the ACP protocol. -- evidence: [.release-notes.md#L17-L39](https://github.com/stagewise-io/stagewise/blob/18ac8a27b18c5de4e2d76d03b515cf10186631ca/.release-notes.md#L17-L39)
- design-choices (1 claim(s)):
  - [observation/documented] The product supports bring-your-own-key for all AI providers, including registering fully custom providers such as local inference and defining custom models. -- evidence: [README.md#L43-L48](https://github.com/stagewise-io/stagewise/blob/18ac8a27b18c5de4e2d76d03b515cf10186631ca/README.md#L43-L48), [README.md#L56-L56](https://github.com/stagewise-io/stagewise/blob/18ac8a27b18c5de4e2d76d03b515cf10186631ca/README.md#L56-L56)
- workflows (3 claim(s)):
  - [observation/documented] Repository development practice: AGENTS.md instructs AI coding agents on pnpm/Turborepo commands, Biome linting, Vitest tests, Electron app scripts, and pre-commit hooks (Lefthook, commitlint). -- evidence: [AGENTS.md#L23-L24](https://github.com/stagewise-io/stagewise/blob/18ac8a27b18c5de4e2d76d03b515cf10186631ca/AGENTS.md#L23-L24), [AGENTS.md#L8-L9](https://github.com/stagewise-io/stagewise/blob/18ac8a27b18c5de4e2d76d03b515cf10186631ca/AGENTS.md#L8-L9), [AGENTS.md#L131-L135](https://github.com/stagewise-io/stagewise/blob/18ac8a27b18c5de4e2d76d03b515cf10186631ca/AGENTS.md#L131-L135), [AGENTS.md#L27-L33](https://github.com/stagewise-io/stagewise/blob/18ac8a27b18c5de4e2d76d03b515cf10186631ca/AGENTS.md#L27-L33), [AGENTS.md#L17-L20](https://github.com/stagewise-io/stagewise/blob/18ac8a27b18c5de4e2d76d03b515cf10186631ca/AGENTS.md#L17-L20)
  - [observation/documented] Repository development practice: commits must follow Conventional Commits with a mandatory workspace-package scope, and releases run via a two-step GitHub Actions workflow with nightly builds separate. -- evidence: [VERSIONING.md#L151-L151](https://github.com/stagewise-io/stagewise/blob/18ac8a27b18c5de4e2d76d03b515cf10186631ca/VERSIONING.md#L151-L151), [VERSIONING.md#L7-L7](https://github.com/stagewise-io/stagewise/blob/18ac8a27b18c5de4e2d76d03b515cf10186631ca/VERSIONING.md#L7-L7), [VERSIONING.md#L140-L140](https://github.com/stagewise-io/stagewise/blob/18ac8a27b18c5de4e2d76d03b515cf10186631ca/VERSIONING.md#L140-L140), [VERSIONING.md#L149-L149](https://github.com/stagewise-io/stagewise/blob/18ac8a27b18c5de4e2d76d03b515cf10186631ca/VERSIONING.md#L149-L149), [VERSIONING.md#L142-L145](https://github.com/stagewise-io/stagewise/blob/18ac8a27b18c5de4e2d76d03b515cf10186631ca/VERSIONING.md#L142-L145)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] The product lets users work with a coding agent that has access to the browser tab's console and debugger, and supports IDE integration to view and apply code changes. -- evidence: [README.md#L43-L48](https://github.com/stagewise-io/stagewise/blob/18ac8a27b18c5de4e2d76d03b515cf10186631ca/README.md#L43-L48)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
  - [observation/documented] Documented provider integrations include Moonshot Kimi, Alibaba Qwen, MiniMax, Xiaomi MiMo, Mistral, and OpenRouter access to 345+ models via one API key. -- evidence: [README.md#L72-L72](https://github.com/stagewise-io/stagewise/blob/18ac8a27b18c5de4e2d76d03b515cf10186631ca/README.md#L72-L72), [README.md#L62-L68](https://github.com/stagewise-io/stagewise/blob/18ac8a27b18c5de4e2d76d03b515cf10186631ca/README.md#L62-L68)
  - [observation/documented] The account plans include open-weight models (Kimi, Qwen, DeepSeek, GLM, MiniMax, MiMo, Mistral) and proprietary models from Anthropic, OpenAI, Google, and xAI. -- evidence: [README.md#L102-L105](https://github.com/stagewise-io/stagewise/blob/18ac8a27b18c5de4e2d76d03b515cf10186631ca/README.md#L102-L105), [README.md#L92-L98](https://github.com/stagewise-io/stagewise/blob/18ac8a27b18c5de4e2d76d03b515cf10186631ca/README.md#L92-L98)
- limitations (1 claim(s)):
More evidence: [full detail](stagewise.detail.md)

Metadata and full claim list: [full detail](stagewise.detail.md)
Human notes ([notes](stagewise.notes.md), never overwritten by build)

[Back to map index](../../index.md)
