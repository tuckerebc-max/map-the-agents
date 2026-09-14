# mayday-wpf/snow-cli -- full detail

[Back to orientation](snow-cli.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/mayday-wpf/snow-cli/063b72c5c0557204bf511f8541c92b2e9da85ce5/d502391872fd4362.json](../../../wiki/dossiers/mayday-wpf/snow-cli/063b72c5c0557204bf511f8541c92b2e9da85ce5/d502391872fd4362.json)

## specifications (1 claim(s))

- [observation/documented] Snow CLI is described as an agentic coding tool that runs in the terminal, distributed as the npm package snow-ai. -- evidence: [README.md#L20-L20](https://github.com/MayDay-wpf/snow-cli/blob/063b72c5c0557204bf511f8541c92b2e9da85ce5/README.md#L20-L20), [README.md#L88-L88](https://github.com/MayDay-wpf/snow-cli/blob/063b72c5c0557204bf511f8541c92b2e9da85ce5/README.md#L88-L88), [README.md#L90-L92](https://github.com/MayDay-wpf/snow-cli/blob/063b72c5c0557204bf511f8541c92b2e9da85ce5/README.md#L90-L92) (`clm_b39d06b41c7f4444d55910eb85e08566674ef242066dfb1499be60248b7e2818`)

## components (1 claim(s))

- [observation/documented] The documented source layout includes agents, LLM API adapters, React hooks for conversation, i18n, MCP, prompt templates, TypeScript types, Ink-based UI components, and utilities under source/. -- evidence: [README.md#L190-L200](https://github.com/MayDay-wpf/snow-cli/blob/063b72c5c0557204bf511f8541c92b2e9da85ce5/README.md#L190-L200) (`clm_b1206245df85850980fdc35cbe6f81934221c459a27379794ceb3819f660a43f`)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: building from source is done by cloning the repo, running npm install, then npm run link to build and globally link the snow command (npm run unlink to remove). -- evidence: [README.md#L168-L172](https://github.com/MayDay-wpf/snow-cli/blob/063b72c5c0557204bf511f8541c92b2e9da85ce5/README.md#L168-L172), [docs/usage/en/01.Installation Guide.md#L49-L55](https://github.com/MayDay-wpf/snow-cli/blob/063b72c5c0557204bf511f8541c92b2e9da85ce5/docs/usage/en/01.Installation%20Guide.md#L49-L55) (`clm_f0f20bfcda544932e59786454330b851154384fbef08913dffaf659ace9a5487`)

## skills-patterns (1 claim(s))

- [observation/documented] A recommended ROLE.md defines the assistant's behavior: plan every step using a Plan Agent, maintain a TODO list via todo-manage (get/add/update/delete), locate files before reading, and record risks with notebook-add. -- evidence: [docs/role/en/01.Snow CLI Plan Every Step.md#L19-L22](https://github.com/MayDay-wpf/snow-cli/blob/063b72c5c0557204bf511f8541c92b2e9da85ce5/docs/role/en/01.Snow%20CLI%20Plan%20Every%20Step.md#L19-L22), [docs/role/zh/01.Snow CLI 一步一规划.md#L37-L41](https://github.com/MayDay-wpf/snow-cli/blob/063b72c5c0557204bf511f8541c92b2e9da85ce5/docs/role/zh/01.Snow%20CLI%20%E4%B8%80%E6%AD%A5%E4%B8%80%E8%A7%84%E5%88%92.md#L37-L41), [README.md#L136-L138](https://github.com/MayDay-wpf/snow-cli/blob/063b72c5c0557204bf511f8541c92b2e9da85ce5/README.md#L136-L138), [docs/role/en/01.Snow CLI Plan Every Step.md#L36-L40](https://github.com/MayDay-wpf/snow-cli/blob/063b72c5c0557204bf511f8541c92b2e9da85ce5/docs/role/en/01.Snow%20CLI%20Plan%20Every%20Step.md#L36-L40), [docs/role/zh/01.Snow CLI 一步一规划.md#L16-L19](https://github.com/MayDay-wpf/snow-cli/blob/063b72c5c0557204bf511f8541c92b2e9da85ce5/docs/role/zh/01.Snow%20CLI%20%E4%B8%80%E6%AD%A5%E4%B8%80%E8%A7%84%E5%88%92.md#L16-L19) (`clm_9fab0fdea8402b7da855ddec0821340bcd7264964f11bd86085e3314dff9a79a`)

## interfaces (3 claim(s))

- [observation/documented] After installation the product is launched with the `snow` command, and installation can be verified with `snow --version` and `snow --help`. -- evidence: [README.md#L96-L98](https://github.com/MayDay-wpf/snow-cli/blob/063b72c5c0557204bf511f8541c92b2e9da85ce5/README.md#L96-L98), [docs/usage/en/01.Installation Guide.md#L59-L62](https://github.com/MayDay-wpf/snow-cli/blob/063b72c5c0557204bf511f8541c92b2e9da85ce5/docs/usage/en/01.Installation%20Guide.md#L59-L62) (`clm_4d3a07c029465e382278cad08c0bc65ad747cf9053a2336ef9192f4570abfd6b`)
- [observation/documented] Documentation describes IDE integrations: a VSCode extension (source in VSIX/, published as mufasa.snow-cli) and a JetBrains plugin (source in Jetbrains/), with configurable terminal, bell, git-blame, inline-completion, and next-edit settings. -- evidence: [docs/usage/en/01.Installation Guide.md#L79-L82](https://github.com/MayDay-wpf/snow-cli/blob/063b72c5c0557204bf511f8541c92b2e9da85ce5/docs/usage/en/01.Installation%20Guide.md#L79-L82), [docs/usage/en/01.Installation Guide.md#L99-L102](https://github.com/MayDay-wpf/snow-cli/blob/063b72c5c0557204bf511f8541c92b2e9da85ce5/docs/usage/en/01.Installation%20Guide.md#L99-L102), [README.md#L180-L181](https://github.com/MayDay-wpf/snow-cli/blob/063b72c5c0557204bf511f8541c92b2e9da85ce5/README.md#L180-L181), [docs/usage/en/01.Installation Guide.md#L110-L126](https://github.com/MayDay-wpf/snow-cli/blob/063b72c5c0557204bf511f8541c92b2e9da85ce5/docs/usage/en/01.Installation%20Guide.md#L110-L126), [docs/usage/en/01.Installation Guide.md#L86-L95](https://github.com/MayDay-wpf/snow-cli/blob/063b72c5c0557204bf511f8541c92b2e9da85ce5/docs/usage/en/01.Installation%20Guide.md#L86-L95), [README.md#L185-L186](https://github.com/MayDay-wpf/snow-cli/blob/063b72c5c0557204bf511f8541c92b2e9da85ce5/README.md#L185-L186), [docs/usage/en/01.Installation Guide.md#L130-L135](https://github.com/MayDay-wpf/snow-cli/blob/063b72c5c0557204bf511f8541c92b2e9da85ce5/docs/usage/en/01.Installation%20Guide.md#L130-L135) (`clm_39d397a37459b4d4c13ec7435c234880113f5df3066204af384673b4d63bec1c`)
- [observation/documented] Documented operating modes include headless mode for command-line conversations and script integration, command injection in messages with security mechanisms, a vulnerability hunting mode, and an SSE service mode exposing API endpoints. -- evidence: [docs/usage/en/0.Catalogue.md#L23-L40](https://github.com/MayDay-wpf/snow-cli/blob/063b72c5c0557204bf511f8541c92b2e9da85ce5/docs/usage/en/0.Catalogue.md#L23-L40), [README_zh.md#L118-L132](https://github.com/MayDay-wpf/snow-cli/blob/063b72c5c0557204bf511f8541c92b2e9da85ce5/README_zh.md#L118-L132), [README.md#L118-L132](https://github.com/MayDay-wpf/snow-cli/blob/063b72c5c0557204bf511f8541c92b2e9da85ce5/README.md#L118-L132) (`clm_6c8de81be64769c55bfa4963963099cc815faad911097084d75a67b86e4353da`)

## memory-state (1 claim(s))

- [observation/documented] Running snow creates a `~/.snow/` directory holding logs, configuration profiles, session history, async tasks, hooks, config.json for API settings, and settings.json including mcpServers. -- evidence: [README.md#L212-L212](https://github.com/MayDay-wpf/snow-cli/blob/063b72c5c0557204bf511f8541c92b2e9da85ce5/README.md#L212-L212), [README.md#L214-L224](https://github.com/MayDay-wpf/snow-cli/blob/063b72c5c0557204bf511f8541c92b2e9da85ce5/README.md#L214-L224) (`clm_35cfba37f73622135ae6e7fde0ede9d7dade02f39838d8b69a1a3c309a9a1f10`)

## orchestration (1 claim(s))

- [observation/documented] Feature docs cover sub-agent management and custom agents (including project Markdown agents), hooks for workflow automation, async background task management with sensitive-command approval, and a Team mode for multi-agent collaboration. -- evidence: [README.md#L108-L114](https://github.com/MayDay-wpf/snow-cli/blob/063b72c5c0557204bf511f8541c92b2e9da85ce5/README.md#L108-L114), [README_zh.md#L118-L132](https://github.com/MayDay-wpf/snow-cli/blob/063b72c5c0557204bf511f8541c92b2e9da85ce5/README_zh.md#L118-L132), [README.md#L118-L132](https://github.com/MayDay-wpf/snow-cli/blob/063b72c5c0557204bf511f8541c92b2e9da85ce5/README.md#L118-L132) (`clm_c8b6a1fce49c37e55ef7ff1a58253e86fe4e93592e6c252887024b28f9d2f424`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The documented runtime prerequisites are Node.js >= 18.x (ES2020 feature support) and npm >= 8.3.0. -- evidence: [docs/usage/en/01.Installation Guide.md#L13-L13](https://github.com/MayDay-wpf/snow-cli/blob/063b72c5c0557204bf511f8541c92b2e9da85ce5/docs/usage/en/01.Installation%20Guide.md#L13-L13), [docs/usage/en/01.Installation Guide.md#L11-L11](https://github.com/MayDay-wpf/snow-cli/blob/063b72c5c0557204bf511f8541c92b2e9da85ce5/docs/usage/en/01.Installation%20Guide.md#L11-L11), [README.md#L146-L147](https://github.com/MayDay-wpf/snow-cli/blob/063b72c5c0557204bf511f8541c92b2e9da85ce5/README.md#L146-L147) (`clm_a2ae32f2e35c2fb58f64d7fb3ed86804deacf3c40e56bc5525b5c573c0f707b9`)

## limitations (1 claim(s))

- [inference/documented] The English ROLE.md is noted as being maintained incrementally, with the Chinese version stated to be the more complete, primary version. -- evidence: [README_zh.md#L136-L138](https://github.com/MayDay-wpf/snow-cli/blob/063b72c5c0557204bf511f8541c92b2e9da85ce5/README_zh.md#L136-L138), [docs/role/en/01.Snow CLI Plan Every Step.md#L3-L4](https://github.com/MayDay-wpf/snow-cli/blob/063b72c5c0557204bf511f8541c92b2e9da85ce5/docs/role/en/01.Snow%20CLI%20Plan%20Every%20Step.md#L3-L4) (`clm_4f4bbc3c9c51b068aaa38923ec028e5b0f9e29583b887396402283b937d98536`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

