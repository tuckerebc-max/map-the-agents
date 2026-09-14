# mayday-wpf/snow-cli

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 063b72c5c055 @ d502391872fd4362

## Summary (orientation draft, not independently verified)

Evidence consists of README files and usage/role documentation for Snow CLI (npm package snow-ai), a terminal-based agentic coding tool with IDE extensions, MCP support, sub-agents, hooks, headless/SSE modes, and a ~/.snow configuration directory. No source code slices are present, so claims are documentation-based. Evidence coverage: 157 of 160 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 78 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Snow CLI is described as an agentic coding tool that runs in the terminal, distributed as the npm package snow-ai. -- evidence: [README.md#L20-L20](https://github.com/MayDay-wpf/snow-cli/blob/063b72c5c0557204bf511f8541c92b2e9da85ce5/README.md#L20-L20), [README.md#L88-L88](https://github.com/MayDay-wpf/snow-cli/blob/063b72c5c0557204bf511f8541c92b2e9da85ce5/README.md#L88-L88), [README.md#L90-L92](https://github.com/MayDay-wpf/snow-cli/blob/063b72c5c0557204bf511f8541c92b2e9da85ce5/README.md#L90-L92)
- components (1 claim(s)):
  - [observation/documented] The documented source layout includes agents, LLM API adapters, React hooks for conversation, i18n, MCP, prompt templates, TypeScript types, Ink-based UI components, and utilities under source/. -- evidence: [README.md#L190-L200](https://github.com/MayDay-wpf/snow-cli/blob/063b72c5c0557204bf511f8541c92b2e9da85ce5/README.md#L190-L200)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: building from source is done by cloning the repo, running npm install, then npm run link to build and globally link the snow command (npm run unlink to remove). -- evidence: [README.md#L168-L172](https://github.com/MayDay-wpf/snow-cli/blob/063b72c5c0557204bf511f8541c92b2e9da85ce5/README.md#L168-L172), [docs/usage/en/01.Installation Guide.md#L49-L55](https://github.com/MayDay-wpf/snow-cli/blob/063b72c5c0557204bf511f8541c92b2e9da85ce5/docs/usage/en/01.Installation%20Guide.md#L49-L55)
- skills-patterns (1 claim(s)):
  - [observation/documented] A recommended ROLE.md defines the assistant's behavior: plan every step using a Plan Agent, maintain a TODO list via todo-manage (get/add/update/delete), locate files before reading, and record risks with notebook-add. -- evidence: [docs/role/en/01.Snow CLI Plan Every Step.md#L19-L22](https://github.com/MayDay-wpf/snow-cli/blob/063b72c5c0557204bf511f8541c92b2e9da85ce5/docs/role/en/01.Snow%20CLI%20Plan%20Every%20Step.md#L19-L22), [docs/role/zh/01.Snow CLI 一步一规划.md#L37-L41](https://github.com/MayDay-wpf/snow-cli/blob/063b72c5c0557204bf511f8541c92b2e9da85ce5/docs/role/zh/01.Snow%20CLI%20%E4%B8%80%E6%AD%A5%E4%B8%80%E8%A7%84%E5%88%92.md#L37-L41), [README.md#L136-L138](https://github.com/MayDay-wpf/snow-cli/blob/063b72c5c0557204bf511f8541c92b2e9da85ce5/README.md#L136-L138), [docs/role/en/01.Snow CLI Plan Every Step.md#L36-L40](https://github.com/MayDay-wpf/snow-cli/blob/063b72c5c0557204bf511f8541c92b2e9da85ce5/docs/role/en/01.Snow%20CLI%20Plan%20Every%20Step.md#L36-L40), [docs/role/zh/01.Snow CLI 一步一规划.md#L16-L19](https://github.com/MayDay-wpf/snow-cli/blob/063b72c5c0557204bf511f8541c92b2e9da85ce5/docs/role/zh/01.Snow%20CLI%20%E4%B8%80%E6%AD%A5%E4%B8%80%E8%A7%84%E5%88%92.md#L16-L19)
- interfaces (3 claim(s)):
  - [observation/documented] After installation the product is launched with the `snow` command, and installation can be verified with `snow --version` and `snow --help`. -- evidence: [README.md#L96-L98](https://github.com/MayDay-wpf/snow-cli/blob/063b72c5c0557204bf511f8541c92b2e9da85ce5/README.md#L96-L98), [docs/usage/en/01.Installation Guide.md#L59-L62](https://github.com/MayDay-wpf/snow-cli/blob/063b72c5c0557204bf511f8541c92b2e9da85ce5/docs/usage/en/01.Installation%20Guide.md#L59-L62)
  - [observation/documented] Documentation describes IDE integrations: a VSCode extension (source in VSIX/, published as mufasa.snow-cli) and a JetBrains plugin (source in Jetbrains/), with configurable terminal, bell, git-blame, inline-completion, and next-edit settings. -- evidence: [docs/usage/en/01.Installation Guide.md#L79-L82](https://github.com/MayDay-wpf/snow-cli/blob/063b72c5c0557204bf511f8541c92b2e9da85ce5/docs/usage/en/01.Installation%20Guide.md#L79-L82), [docs/usage/en/01.Installation Guide.md#L99-L102](https://github.com/MayDay-wpf/snow-cli/blob/063b72c5c0557204bf511f8541c92b2e9da85ce5/docs/usage/en/01.Installation%20Guide.md#L99-L102), [README.md#L180-L181](https://github.com/MayDay-wpf/snow-cli/blob/063b72c5c0557204bf511f8541c92b2e9da85ce5/README.md#L180-L181), [docs/usage/en/01.Installation Guide.md#L110-L126](https://github.com/MayDay-wpf/snow-cli/blob/063b72c5c0557204bf511f8541c92b2e9da85ce5/docs/usage/en/01.Installation%20Guide.md#L110-L126), [docs/usage/en/01.Installation Guide.md#L86-L95](https://github.com/MayDay-wpf/snow-cli/blob/063b72c5c0557204bf511f8541c92b2e9da85ce5/docs/usage/en/01.Installation%20Guide.md#L86-L95), [README.md#L185-L186](https://github.com/MayDay-wpf/snow-cli/blob/063b72c5c0557204bf511f8541c92b2e9da85ce5/README.md#L185-L186), [docs/usage/en/01.Installation Guide.md#L130-L135](https://github.com/MayDay-wpf/snow-cli/blob/063b72c5c0557204bf511f8541c92b2e9da85ce5/docs/usage/en/01.Installation%20Guide.md#L130-L135)
- memory-state (1 claim(s)):
  - [observation/documented] Running snow creates a `~/.snow/` directory holding logs, configuration profiles, session history, async tasks, hooks, config.json for API settings, and settings.json including mcpServers. -- evidence: [README.md#L212-L212](https://github.com/MayDay-wpf/snow-cli/blob/063b72c5c0557204bf511f8541c92b2e9da85ce5/README.md#L212-L212), [README.md#L214-L224](https://github.com/MayDay-wpf/snow-cli/blob/063b72c5c0557204bf511f8541c92b2e9da85ce5/README.md#L214-L224)
- orchestration (1 claim(s)):
  - [observation/documented] Feature docs cover sub-agent management and custom agents (including project Markdown agents), hooks for workflow automation, async background task management with sensitive-command approval, and a Team mode for multi-agent collaboration. -- evidence: [README.md#L108-L114](https://github.com/MayDay-wpf/snow-cli/blob/063b72c5c0557204bf511f8541c92b2e9da85ce5/README.md#L108-L114), [README_zh.md#L118-L132](https://github.com/MayDay-wpf/snow-cli/blob/063b72c5c0557204bf511f8541c92b2e9da85ce5/README_zh.md#L118-L132), [README.md#L118-L132](https://github.com/MayDay-wpf/snow-cli/blob/063b72c5c0557204bf511f8541c92b2e9da85ce5/README.md#L118-L132)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
More evidence: [full detail](snow-cli.detail.md)

Metadata and full claim list: [full detail](snow-cli.detail.md)
Human notes ([notes](snow-cli.notes.md), never overwritten by build)

[Back to map index](../../index.md)
