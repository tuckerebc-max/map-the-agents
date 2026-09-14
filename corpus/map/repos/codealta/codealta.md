# codealta/codealta

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 823f847297aa @ 00285a1be4caf16b

## Summary (orientation draft, not independently verified)

CodeAlta is a pre-release .NET terminal workspace for agentic coding, distributed as a dotnet global tool behind the `alta` command, with provider-neutral model setup, durable sessions, and a keyboard-first TUI. Contributor guidance in AGENTS.md/CLAUDE.md covers build, test, and coding conventions.

## Source coverage

Source coverage (partial): 3 of 17 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] Supported model providers include Codex, Copilot, xAI Grok, OpenAI/Azure OpenAI/Alibaba APIs, Anthropic, Gemini/Vertex, and custom endpoints. -- evidence: [readme.md#L26-L26](https://github.com/CodeAlta/CodeAlta/blob/823f847297aafb0662ee317c3434c96a755e32fa/readme.md#L26-L26)
- design-choices (2 claim(s)):
  - [observation/documented] On first launch the tool creates `~/.alta/config.toml` and leaves existing config untouched on later launches; if no provider is enabled, a Model Providers dialog opens. -- evidence: [readme.md#L26-L26](https://github.com/CodeAlta/CodeAlta/blob/823f847297aafb0662ee317c3434c96a755e32fa/readme.md#L26-L26)
  - [observation/documented] The UI is multilingual, offering Auto, English, Spanish, French, German, Japanese, or Simplified Chinese via Workspace Settings. -- evidence: [readme.md#L32-L38](https://github.com/CodeAlta/CodeAlta/blob/823f847297aafb0662ee317c3434c96a755e32fa/readme.md#L32-L38)
- workflows (3 claim(s)):
  - [observation/documented] Repository development practice: contributors build with `dotnet build -c Release` and test with `dotnet test -c Release` in src/, and must keep docs updated before submitting. -- evidence: [AGENTS.md#L21-L23](https://github.com/CodeAlta/CodeAlta/blob/823f847297aafb0662ee317c3434c96a755e32fa/AGENTS.md#L21-L23), [AGENTS.md#L30-L30](https://github.com/CodeAlta/CodeAlta/blob/823f847297aafb0662ee317c3434c96a755e32fa/AGENTS.md#L30-L30)
  - [observation/documented] Repository development practice: CLAUDE.md defers to AGENTS.md as the single source of truth, and AGENTS.md mandates tests for new behavior, XML docs on public APIs, and no static mutable data. -- evidence: [CLAUDE.md#L5-L5](https://github.com/CodeAlta/CodeAlta/blob/823f847297aafb0662ee317c3434c96a755e32fa/CLAUDE.md#L5-L5), [AGENTS.md#L34-L40](https://github.com/CodeAlta/CodeAlta/blob/823f847297aafb0662ee317c3434c96a755e32fa/AGENTS.md#L34-L40), [CLAUDE.md#L3-L3](https://github.com/CodeAlta/CodeAlta/blob/823f847297aafb0662ee317c3434c96a755e32fa/CLAUDE.md#L3-L3)
- skills-patterns (1 claim(s)):
  - [observation/documented] The repository includes a skills feature documented in doc/skills.md, referenced from the readme's documentation list. -- evidence: [readme.md#L59-L65](https://github.com/CodeAlta/CodeAlta/blob/823f847297aafb0662ee317c3434c96a755e32fa/readme.md#L59-L65)
- interfaces (2 claim(s)):
  - [observation/documented] CodeAlta runs as a terminal workspace invoked via the `alta` command, providing a keyboard-first TUI with tabs, prompt editor, project sidebar, and command discovery. -- evidence: [readme.md#L3-L3](https://github.com/CodeAlta/CodeAlta/blob/823f847297aafb0662ee317c3434c96a755e32fa/readme.md#L3-L3), [readme.md#L32-L38](https://github.com/CodeAlta/CodeAlta/blob/823f847297aafb0662ee317c3434c96a755e32fa/readme.md#L32-L38)
  - [observation/documented] The TUI exposes slash commands and shortcuts such as `/open` (Ctrl+O), `/prompt`, `/model_providers`, `/models`, `/logs`, and `/help`. -- evidence: [readme.md#L42-L55](https://github.com/CodeAlta/CodeAlta/blob/823f847297aafb0662ee317c3434c96a755e32fa/readme.md#L42-L55)
- memory-state (1 claim(s)):
  - [observation/documented] Agent sessions are durable and project-scoped, stored in CodeAlta-owned journals, and can be reopened independently of provider startup; prompts can be queued on busy sessions. -- evidence: [readme.md#L32-L38](https://github.com/CodeAlta/CodeAlta/blob/823f847297aafb0662ee317c3434c96a755e32fa/readme.md#L32-L38)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] Installation requires .NET 10 and is done via `dotnet tool install -g CodeAlta`, with updates via `dotnet tool update -g CodeAlta`. -- evidence: [readme.md#L22-L24](https://github.com/CodeAlta/CodeAlta/blob/823f847297aafb0662ee317c3434c96a755e32fa/readme.md#L22-L24), [readme.md#L13-L13](https://github.com/CodeAlta/CodeAlta/blob/823f847297aafb0662ee317c3434c96a755e32fa/readme.md#L13-L13), [readme.md#L15-L18](https://github.com/CodeAlta/CodeAlta/blob/823f847297aafb0662ee317c3434c96a755e32fa/readme.md#L15-L18)
- limitations (1 claim(s)):
  - [observation/documented] CodeAlta is pre-release software; configuration, screenshots, and extension APIs may change before version 1.0. -- evidence: [readme.md#L5-L5](https://github.com/CodeAlta/CodeAlta/blob/823f847297aafb0662ee317c3434c96a755e32fa/readme.md#L5-L5)
More evidence: [full detail](codealta.detail.md)

Metadata and full claim list: [full detail](codealta.detail.md)
Human notes ([notes](codealta.notes.md), never overwritten by build)

[Back to map index](../../index.md)
