# codealta/codealta -- full detail

[Back to orientation](codealta.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/codealta/codealta/823f847297aafb0662ee317c3434c96a755e32fa/00285a1be4caf16b.json](../../../wiki/dossiers/codealta/codealta/823f847297aafb0662ee317c3434c96a755e32fa/00285a1be4caf16b.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] Supported model providers include Codex, Copilot, xAI Grok, OpenAI/Azure OpenAI/Alibaba APIs, Anthropic, Gemini/Vertex, and custom endpoints. -- evidence: [readme.md#L26-L26](https://github.com/CodeAlta/CodeAlta/blob/823f847297aafb0662ee317c3434c96a755e32fa/readme.md#L26-L26) (`clm_62191ab58edb1d8e18a05f804eb2d7c56fd76345433ab2fc9e12d483cb5efd15`)

## design-choices (2 claim(s))

- [observation/documented] On first launch the tool creates `~/.alta/config.toml` and leaves existing config untouched on later launches; if no provider is enabled, a Model Providers dialog opens. -- evidence: [readme.md#L26-L26](https://github.com/CodeAlta/CodeAlta/blob/823f847297aafb0662ee317c3434c96a755e32fa/readme.md#L26-L26) (`clm_e3bb666a49f4d38533de7f03f341fa0088bd15e61e8ef1b96eb805698534ad2a`)
- [observation/documented] The UI is multilingual, offering Auto, English, Spanish, French, German, Japanese, or Simplified Chinese via Workspace Settings. -- evidence: [readme.md#L32-L38](https://github.com/CodeAlta/CodeAlta/blob/823f847297aafb0662ee317c3434c96a755e32fa/readme.md#L32-L38) (`clm_8201ed11d6397eaa2f3160e11324088928bc29f08b89602208ac1b51ce4b46b5`)

## workflows (3 claim(s))

- [observation/documented] Repository development practice: contributors build with `dotnet build -c Release` and test with `dotnet test -c Release` in src/, and must keep docs updated before submitting. -- evidence: [AGENTS.md#L21-L23](https://github.com/CodeAlta/CodeAlta/blob/823f847297aafb0662ee317c3434c96a755e32fa/AGENTS.md#L21-L23), [AGENTS.md#L30-L30](https://github.com/CodeAlta/CodeAlta/blob/823f847297aafb0662ee317c3434c96a755e32fa/AGENTS.md#L30-L30) (`clm_8f659276043daaf1bf8644326e1eb6ea257309ea72531249d32ff90761bbc2e2`)
- [observation/documented] Repository development practice: CLAUDE.md defers to AGENTS.md as the single source of truth, and AGENTS.md mandates tests for new behavior, XML docs on public APIs, and no static mutable data. -- evidence: [CLAUDE.md#L5-L5](https://github.com/CodeAlta/CodeAlta/blob/823f847297aafb0662ee317c3434c96a755e32fa/CLAUDE.md#L5-L5), [AGENTS.md#L34-L40](https://github.com/CodeAlta/CodeAlta/blob/823f847297aafb0662ee317c3434c96a755e32fa/AGENTS.md#L34-L40), [CLAUDE.md#L3-L3](https://github.com/CodeAlta/CodeAlta/blob/823f847297aafb0662ee317c3434c96a755e32fa/CLAUDE.md#L3-L3) (`clm_721c9da5f83fdf93d7e210689ba21400c6c993409b1814c47fac3c1e4bea6e92`)
- [observation/documented] Repository development practice: commit subjects must use dotnet-releaser autolabel prefixes such as `Breaking Change`, `Add`, `Fix`, or `Enhance`, with issue references in parentheses. -- evidence: [AGENTS.md#L64-L66](https://github.com/CodeAlta/CodeAlta/blob/823f847297aafb0662ee317c3434c96a755e32fa/AGENTS.md#L64-L66) (`clm_1ed53038245916a41b9aa6eb2958fbdca79352232ec8edef3206eab4cd9fb2d7`)

## skills-patterns (1 claim(s))

- [observation/documented] The repository includes a skills feature documented in doc/skills.md, referenced from the readme's documentation list. -- evidence: [readme.md#L59-L65](https://github.com/CodeAlta/CodeAlta/blob/823f847297aafb0662ee317c3434c96a755e32fa/readme.md#L59-L65) (`clm_d5f8c94c30368f21bcb1cc4dfa11db134a0ebca986a73af09807f5ed7ed65e8e`)

## interfaces (2 claim(s))

- [observation/documented] CodeAlta runs as a terminal workspace invoked via the `alta` command, providing a keyboard-first TUI with tabs, prompt editor, project sidebar, and command discovery. -- evidence: [readme.md#L3-L3](https://github.com/CodeAlta/CodeAlta/blob/823f847297aafb0662ee317c3434c96a755e32fa/readme.md#L3-L3), [readme.md#L32-L38](https://github.com/CodeAlta/CodeAlta/blob/823f847297aafb0662ee317c3434c96a755e32fa/readme.md#L32-L38) (`clm_4fb51b45446c4fc50320e764c9919189090f247ee1ec419d6bd76b3d4ac5d757`)
- [observation/documented] The TUI exposes slash commands and shortcuts such as `/open` (Ctrl+O), `/prompt`, `/model_providers`, `/models`, `/logs`, and `/help`. -- evidence: [readme.md#L42-L55](https://github.com/CodeAlta/CodeAlta/blob/823f847297aafb0662ee317c3434c96a755e32fa/readme.md#L42-L55) (`clm_0eec30d1d88beb8ad7c5cc5969a19787270def7e5ad0dc07c71fbd47ec6426ec`)

## memory-state (1 claim(s))

- [observation/documented] Agent sessions are durable and project-scoped, stored in CodeAlta-owned journals, and can be reopened independently of provider startup; prompts can be queued on busy sessions. -- evidence: [readme.md#L32-L38](https://github.com/CodeAlta/CodeAlta/blob/823f847297aafb0662ee317c3434c96a755e32fa/readme.md#L32-L38) (`clm_9cd83eb66198470021588e31e602ed326a8c85d86c7c02c8d0358f2fb170c627`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Installation requires .NET 10 and is done via `dotnet tool install -g CodeAlta`, with updates via `dotnet tool update -g CodeAlta`. -- evidence: [readme.md#L22-L24](https://github.com/CodeAlta/CodeAlta/blob/823f847297aafb0662ee317c3434c96a755e32fa/readme.md#L22-L24), [readme.md#L13-L13](https://github.com/CodeAlta/CodeAlta/blob/823f847297aafb0662ee317c3434c96a755e32fa/readme.md#L13-L13), [readme.md#L15-L18](https://github.com/CodeAlta/CodeAlta/blob/823f847297aafb0662ee317c3434c96a755e32fa/readme.md#L15-L18) (`clm_273f1f6d380f8126f781489b3deefb03ed1cda43de79b591b6863f366295d712`)

## limitations (1 claim(s))

- [observation/documented] CodeAlta is pre-release software; configuration, screenshots, and extension APIs may change before version 1.0. -- evidence: [readme.md#L5-L5](https://github.com/CodeAlta/CodeAlta/blob/823f847297aafb0662ee317c3434c96a755e32fa/readme.md#L5-L5) (`clm_7e22fe5742cbcec9f00ea2005a4d13769f868f5bbf4282445ccf9b03d6775bf3`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

