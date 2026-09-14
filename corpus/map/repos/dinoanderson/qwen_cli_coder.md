# dinoanderson/qwen_cli_coder

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit dbf277291908 @ 6cb863d3cc58a3c7

## Summary (orientation draft, not independently verified)

Evidence consists of README and docs describing Qwen CLI, a community fork of Google's Gemini CLI adapted for Alibaba Cloud Qwen models, covering its features, configuration, architecture, and tooling. No code or eval results are present, so claims are documentation-based. Evidence coverage: 159 of 260 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 46 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 15 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

15 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (2 claim(s)):
  - [observation/documented] The project is a community-maintained fork of Google's Gemini CLI, modified to work with Qwen models from Alibaba Cloud, under Apache License 2.0. -- evidence: [README.md#L13-L13](https://github.com/dinoanderson/qwen_cli_coder/blob/dbf277291908dc45a1fee1c8b635ffe26e4f9d97/README.md#L13-L13), [README.md#L15-L17](https://github.com/dinoanderson/qwen_cli_coder/blob/dbf277291908dc45a1fee1c8b635ffe26e4f9d97/README.md#L15-L17), [README.md#L485-L488](https://github.com/dinoanderson/qwen_cli_coder/blob/dbf277291908dc45a1fee1c8b635ffe26e4f9d97/README.md#L485-L488), [README.md#L5-L5](https://github.com/dinoanderson/qwen_cli_coder/blob/dbf277291908dc45a1fee1c8b635ffe26e4f9d97/README.md#L5-L5)
  - [observation/documented] Supported models include qwen-turbo-latest (1M context), qwen3-235b-a22b (131k context), and qwen-vl-plus-latest (32k context, vision). -- evidence: [README.md#L134-L137](https://github.com/dinoanderson/qwen_cli_coder/blob/dbf277291908dc45a1fee1c8b635ffe26e4f9d97/README.md#L134-L137)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (1 claim(s)):
  - [observation/documented] Architecture splits a user-facing CLI package (packages/cli) from a backend core package (packages/core) that handles API calls, prompt construction, and tool execution. -- evidence: [docs/architecture.md#L9-L9](https://github.com/dinoanderson/qwen_cli_coder/blob/dbf277291908dc45a1fee1c8b635ffe26e4f9d97/docs/architecture.md#L9-L9), [docs/architecture.md#L21-L27](https://github.com/dinoanderson/qwen_cli_coder/blob/dbf277291908dc45a1fee1c8b635ffe26e4f9d97/docs/architecture.md#L21-L27), [docs/architecture.md#L29-L31](https://github.com/dinoanderson/qwen_cli_coder/blob/dbf277291908dc45a1fee1c8b635ffe26e4f9d97/docs/architecture.md#L29-L31)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributors are directed to CONTRIBUTING.md for guidelines specific to this community fork. -- evidence: [README.md#L494-L494](https://github.com/dinoanderson/qwen_cli_coder/blob/dbf277291908dc45a1fee1c8b635ffe26e4f9d97/README.md#L494-L494)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The CLI provides slash commands including /model for interactive model switching, /lang for English/Chinese localization, /theme, /auth, /mcp, and /tools. -- evidence: [README.md#L151-L155](https://github.com/dinoanderson/qwen_cli_coder/blob/dbf277291908dc45a1fee1c8b635ffe26e4f9d97/README.md#L151-L155), [README.md#L158-L162](https://github.com/dinoanderson/qwen_cli_coder/blob/dbf277291908dc45a1fee1c8b635ffe26e4f9d97/README.md#L158-L162), [README.md#L144-L148](https://github.com/dinoanderson/qwen_cli_coder/blob/dbf277291908dc45a1fee1c8b635ffe26e4f9d97/README.md#L144-L148), [README.md#L192-L195](https://github.com/dinoanderson/qwen_cli_coder/blob/dbf277291908dc45a1fee1c8b635ffe26e4f9d97/README.md#L192-L195)
  - [observation/documented] An Assistant Mode launched via 'node bundle/qwen.js --assistant' opens a browser chat interface with file upload, session-based storage, and dark mode detection. -- evidence: [README.md#L40-L41](https://github.com/dinoanderson/qwen_cli_coder/blob/dbf277291908dc45a1fee1c8b635ffe26e4f9d97/README.md#L40-L41), [README.md#L45-L51](https://github.com/dinoanderson/qwen_cli_coder/blob/dbf277291908dc45a1fee1c8b635ffe26e4f9d97/README.md#L45-L51)
- memory-state (2 claim(s)):
  - [observation/documented] Configuration uses ~/.qwen/settings.json (user) and .qwen/settings.json (project, overriding user), with a five-layer precedence ending in command-line arguments. -- evidence: [docs/cli/configuration.md#L9-L13](https://github.com/dinoanderson/qwen_cli_coder/blob/dbf277291908dc45a1fee1c8b635ffe26e4f9d97/docs/cli/configuration.md#L9-L13), [docs/cli/configuration.md#L19-L24](https://github.com/dinoanderson/qwen_cli_coder/blob/dbf277291908dc45a1fee1c8b635ffe26e4f9d97/docs/cli/configuration.md#L19-L24)
  - [observation/documented] A checkpointing feature (disabled by default) can save and restore conversation and file states, enabling a /restore command when enabled. -- evidence: [docs/cli/configuration.md#L153-L156](https://github.com/dinoanderson/qwen_cli_coder/blob/dbf277291908dc45a1fee1c8b635ffe26e4f9d97/docs/cli/configuration.md#L153-L156)
- orchestration (1 claim(s)):
  - [observation/documented] Multi-agent tools (spawn_sub_agent, delegate_task, aggregate_results) support up to 5 concurrent agents with priority-based scheduling and multiple aggregation formats. -- evidence: [README.md#L263-L266](https://github.com/dinoanderson/qwen_cli_coder/blob/dbf277291908dc45a1fee1c8b635ffe26e4f9d97/README.md#L263-L266), [README.md#L268-L272](https://github.com/dinoanderson/qwen_cli_coder/blob/dbf277291908dc45a1fee1c8b635ffe26e4f9d97/README.md#L268-L272)
- tools-permissions (3 claim(s)):
  - [observation/documented] Tools that modify the filesystem or run shell commands require user approval before execution; read-only operations may proceed without confirmation. -- evidence: [docs/architecture.md#L37-L50](https://github.com/dinoanderson/qwen_cli_coder/blob/dbf277291908dc45a1fee1c8b635ffe26e4f9d97/docs/architecture.md#L37-L50)
  - [observation/documented] Settings support coreTools and excludeTools lists to restrict which built-in tools the model can use, plus an autoAccept option to skip confirmation for safe tools. -- evidence: [docs/cli/configuration.md#L78-L80](https://github.com/dinoanderson/qwen_cli_coder/blob/dbf277291908dc45a1fee1c8b635ffe26e4f9d97/docs/cli/configuration.md#L78-L80), [docs/cli/configuration.md#L84-L86](https://github.com/dinoanderson/qwen_cli_coder/blob/dbf277291908dc45a1fee1c8b635ffe26e4f9d97/docs/cli/configuration.md#L84-L86), [docs/cli/configuration.md#L72-L74](https://github.com/dinoanderson/qwen_cli_coder/blob/dbf277291908dc45a1fee1c8b635ffe26e4f9d97/docs/cli/configuration.md#L72-L74)
- evaluation: unknown (no source-linked claim submitted for this facet)
More evidence: [full detail](qwen_cli_coder.detail.md)

Metadata and full claim list: [full detail](qwen_cli_coder.detail.md)
Human notes ([notes](qwen_cli_coder.notes.md), never overwritten by build)

[Back to map index](../../index.md)
