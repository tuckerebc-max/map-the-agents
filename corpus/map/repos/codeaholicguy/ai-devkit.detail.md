# codeaholicguy/ai-devkit -- full detail

[Back to orientation](ai-devkit.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/codeaholicguy/ai-devkit/1a3a0024eb3bfb389ed20c45e28b3ef0bf5360d1/fadc9f2153ecec7e.json](../../../wiki/dossiers/codeaholicguy/ai-devkit/1a3a0024eb3bfb389ed20c45e28b3ef0bf5360d1/fadc9f2153ecec7e.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The project comprises packages including cli, agent-manager, channel-connector, and memory, which were migrated from CommonJS to ES Modules with Vitest replacing Jest. -- evidence: [CHANGELOG.md#L292-L293](https://github.com/codeaholicguy/ai-devkit/blob/1a3a0024eb3bfb389ed20c45e28b3ef0bf5360d1/CHANGELOG.md#L292-L293) (`clm_c6471923b7153cc2abd6cbba3d0f8ae7c683d2d7cc2304bdcc2b81ae841daf51`)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributors clone the repo, run npm install and npm run build, and contributing guidance lives in CONTRIBUTING.md. -- evidence: [README.md#L240-L243](https://github.com/codeaholicguy/ai-devkit/blob/1a3a0024eb3bfb389ed20c45e28b3ef0bf5360d1/README.md#L240-L243), [README.md#L236-L238](https://github.com/codeaholicguy/ai-devkit/blob/1a3a0024eb3bfb389ed20c45e28b3ef0bf5360d1/README.md#L236-L238) (`clm_82ca6c942a0816f17fd9de53073b1412977e5a4a343dc7888014d785c6db15fc`)

## skills-patterns (2 claim(s))

- [observation/documented] Nine built-in skills are documented, anchored by dev-lifecycle, plus verify, tdd, structured-debug, memory, dev-commit, document-code, simplify-implementation, and technical-writer. -- evidence: [README.md#L176-L186](https://github.com/codeaholicguy/ai-devkit/blob/1a3a0024eb3bfb389ed20c45e28b3ef0bf5360d1/README.md#L176-L186), [README.md#L174-L174](https://github.com/codeaholicguy/ai-devkit/blob/1a3a0024eb3bfb389ed20c45e28b3ef0bf5360d1/README.md#L174-L174) (`clm_7b60b6b7cdda99d008059e9a9f24816afc8d1666b19fa3be8340a70024a4f61c`)
- [observation/documented] The verify skill blocks completion claims without fresh test or build evidence, and dev-commit checks diffs, stages explicit paths, validates, and reports the SHA/status. -- evidence: [README.md#L128-L132](https://github.com/codeaholicguy/ai-devkit/blob/1a3a0024eb3bfb389ed20c45e28b3ef0bf5360d1/README.md#L128-L132), [README.md#L176-L186](https://github.com/codeaholicguy/ai-devkit/blob/1a3a0024eb3bfb389ed20c45e28b3ef0bf5360d1/README.md#L176-L186) (`clm_d2535d283b54d38cbf9fe5aec52a1bdc128aeafca0a14b5e6e31ebec046e729d`)

## interfaces (4 claim(s))

- [observation/documented] The CLI exposes agent subcommands including agent list, agent detail, agent console, agent send, agent start, and agent rename; agent kill is documented as a console command with confirmation and tmux cleanup. -- evidence: [README.md#L86-L86](https://github.com/codeaholicguy/ai-devkit/blob/1a3a0024eb3bfb389ed20c45e28b3ef0bf5360d1/README.md#L86-L86), [README.md#L92-L92](https://github.com/codeaholicguy/ai-devkit/blob/1a3a0024eb3bfb389ed20c45e28b3ef0bf5360d1/README.md#L92-L92), [CHANGELOG.md#L271-L272](https://github.com/codeaholicguy/ai-devkit/blob/1a3a0024eb3bfb389ed20c45e28b3ef0bf5360d1/CHANGELOG.md#L271-L272), [CHANGELOG.md#L264-L265](https://github.com/codeaholicguy/ai-devkit/blob/1a3a0024eb3bfb389ed20c45e28b3ef0bf5360d1/CHANGELOG.md#L264-L265), [README.md#L21-L27](https://github.com/codeaholicguy/ai-devkit/blob/1a3a0024eb3bfb389ed20c45e28b3ef0bf5360d1/README.md#L21-L27), [README.md#L89-L89](https://github.com/codeaholicguy/ai-devkit/blob/1a3a0024eb3bfb389ed20c45e28b3ef0bf5360d1/README.md#L89-L89) (`clm_b8d8bdea9e2e7023abc49bdc9d9af76e740d6d08a8d8cca6d72fededf2a7dcb4`)
- [observation/documented] agent send supports --stdin for piped input, --wait to block until a response, --timeout in milliseconds, --json structured output, and --group for sending to saved agent groups. -- evidence: [README.md#L98-L98](https://github.com/codeaholicguy/ai-devkit/blob/1a3a0024eb3bfb389ed20c45e28b3ef0bf5360d1/README.md#L98-L98), [CHANGELOG.md#L335-L335](https://github.com/codeaholicguy/ai-devkit/blob/1a3a0024eb3bfb389ed20c45e28b3ef0bf5360d1/CHANGELOG.md#L335-L335), [CHANGELOG.md#L322-L325](https://github.com/codeaholicguy/ai-devkit/blob/1a3a0024eb3bfb389ed20c45e28b3ef0bf5360d1/CHANGELOG.md#L322-L325), [README.md#L95-L95](https://github.com/codeaholicguy/ai-devkit/blob/1a3a0024eb3bfb389ed20c45e28b3ef0bf5360d1/README.md#L95-L95) (`clm_0e00e645b8daf3e7c0235365253d43f81c750ac183df914a5e2d45b127b5df88`)
- [observation/documented] A channel command bridges running agent sessions to external channels such as Telegram and Slack, with named configs, daemon mode, stop/status commands, and authorization state reporting. -- evidence: [CHANGELOG.md#L316-L316](https://github.com/codeaholicguy/ai-devkit/blob/1a3a0024eb3bfb389ed20c45e28b3ef0bf5360d1/CHANGELOG.md#L316-L316), [README.md#L101-L102](https://github.com/codeaholicguy/ai-devkit/blob/1a3a0024eb3bfb389ed20c45e28b3ef0bf5360d1/README.md#L101-L102), [CHANGELOG.md#L132-L143](https://github.com/codeaholicguy/ai-devkit/blob/1a3a0024eb3bfb389ed20c45e28b3ef0bf5360d1/CHANGELOG.md#L132-L143), [CHANGELOG.md#L310-L312](https://github.com/codeaholicguy/ai-devkit/blob/1a3a0024eb3bfb389ed20c45e28b3ef0bf5360d1/CHANGELOG.md#L310-L312) (`clm_65f10b9848277131091a6d0d75cd9fbe28c47d48626832cfab51791beb87651f`)
- [observation/documented] A single .ai-devkit.json config reconciles setup across supported agents, and init writes per-agent directories, skills, MCP settings, and docs/ai phase folders. -- evidence: [README.md#L62-L62](https://github.com/codeaholicguy/ai-devkit/blob/1a3a0024eb3bfb389ed20c45e28b3ef0bf5360d1/README.md#L62-L62), [README.md#L192-L192](https://github.com/codeaholicguy/ai-devkit/blob/1a3a0024eb3bfb389ed20c45e28b3ef0bf5360d1/README.md#L192-L192), [README.md#L11-L15](https://github.com/codeaholicguy/ai-devkit/blob/1a3a0024eb3bfb389ed20c45e28b3ef0bf5360d1/README.md#L11-L15), [README.md#L66-L78](https://github.com/codeaholicguy/ai-devkit/blob/1a3a0024eb3bfb389ed20c45e28b3ef0bf5360d1/README.md#L66-L78) (`clm_627d829ba3f32cd5f2fb1ee8f98f3a4b50beeca60147ae46eb910dba740e38dc`)

## memory-state (1 claim(s))

- [observation/documented] Memory stores project decisions, conventions, and fixes in a local SQLite file, exposed through MCP and CLI, with store and search commands and opt-in hybrid semantic search. -- evidence: [README.md#L108-L108](https://github.com/codeaholicguy/ai-devkit/blob/1a3a0024eb3bfb389ed20c45e28b3ef0bf5360d1/README.md#L108-L108), [CHANGELOG.md#L41-L41](https://github.com/codeaholicguy/ai-devkit/blob/1a3a0024eb3bfb389ed20c45e28b3ef0bf5360d1/CHANGELOG.md#L41-L41), [README.md#L112-L116](https://github.com/codeaholicguy/ai-devkit/blob/1a3a0024eb3bfb389ed20c45e28b3ef0bf5360d1/README.md#L112-L116), [README.md#L11-L15](https://github.com/codeaholicguy/ai-devkit/blob/1a3a0024eb3bfb389ed20c45e28b3ef0bf5360d1/README.md#L11-L15), [README.md#L119-L120](https://github.com/codeaholicguy/ai-devkit/blob/1a3a0024eb3bfb389ed20c45e28b3ef0bf5360d1/README.md#L119-L120) (`clm_9a8f9904663487a5be3c373f07749e1507fc0fae6d7139369f45947f0a87980f`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (1 claim(s))

- [observation/documented] A changelog entry reports retrieval-quality metrics for hybrid semantic memory search tuning: judged irrelevant top-3 results fell from 4.7% to 2.5% while hit@3 stayed at 97%. -- evidence: [CHANGELOG.md#L30-L30](https://github.com/codeaholicguy/ai-devkit/blob/1a3a0024eb3bfb389ed20c45e28b3ef0bf5360d1/CHANGELOG.md#L30-L30) (`clm_5f3b05a24633a7f9491b659c0f6302dba0c461ee673989fbe075bee9c559005a`)

## dependencies (2 claim(s))

- [observation/documented] The changelog records a broken release: 0.62.0 pinned @ai-devkit/agent-manager 0.32.0 while importing 0.33.0 exports, was removed from npm, and 0.62.1 repinned to 0.33.0. -- evidence: [CHANGELOG.md#L10-L10](https://github.com/codeaholicguy/ai-devkit/blob/1a3a0024eb3bfb389ed20c45e28b3ef0bf5360d1/CHANGELOG.md#L10-L10) (`clm_115898b4e63993fc6ce3a3702d67de57cae817c78a20fbea32869a9468aab9c7`)
- [observation/documented] The changelog notes better-sqlite3 was updated to 12.11.1 and @ai-devkit/memory was pinned to 0.17.0 to include a database WAL concurrency fix. -- evidence: [CHANGELOG.md#L45-L45](https://github.com/codeaholicguy/ai-devkit/blob/1a3a0024eb3bfb389ed20c45e28b3ef0bf5360d1/CHANGELOG.md#L45-L45), [CHANGELOG.md#L147-L152](https://github.com/codeaholicguy/ai-devkit/blob/1a3a0024eb3bfb389ed20c45e28b3ef0bf5360d1/CHANGELOG.md#L147-L152) (`clm_2772c2c58d9336d95b5303a312b1fea886f9babe1f6c93158b661ad5cb0f5e08`)

## limitations (1 claim(s))

- [observation/documented] The README states the tool is not a smarter LLM, not a replacement for the coding agents it coordinates, and not a hosted service; it runs locally with no telemetry. -- evidence: [README.md#L229-L232](https://github.com/codeaholicguy/ai-devkit/blob/1a3a0024eb3bfb389ed20c45e28b3ef0bf5360d1/README.md#L229-L232) (`clm_fbce3145a3f79cf234902a7c2cb97925325c1fa916babc919920994f3e4fb541`)

## relevance (1 claim(s))

- [observation/documented] The tool targets developers running multiple AI coding agents who lack a shared control surface, maintain separate per-tool config files, and have no easy way to message running sessions. -- evidence: [README.md#L36-L36](https://github.com/codeaholicguy/ai-devkit/blob/1a3a0024eb3bfb389ed20c45e28b3ef0bf5360d1/README.md#L36-L36), [README.md#L38-L43](https://github.com/codeaholicguy/ai-devkit/blob/1a3a0024eb3bfb389ed20c45e28b3ef0bf5360d1/README.md#L38-L43) (`clm_e3e02f21aa765804791976a0bc11fa9767c2548d851540defd5921545cc77c9e`)

