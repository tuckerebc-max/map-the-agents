# bytedance/trae-agent

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit e839e559ac61 @ aac655fead22ca30

## Summary (orientation draft, not independently verified)

Selected evidence records: Trae Agent provides a CLI (trae-cli) that accepts natural-language task instructions and runs software engineering workflows, with 'run' and 'interactive' subcommands. Interactive mode supports typed task descriptions plus commands: status, help, clear, and exit/quit.

## Source coverage

Source coverage (complete): 6 of 6 candidate file(s) selected; repository tree complete. Claims by basis: 15 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

15 claim(s) across 10 facet(s); 3 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] Trae Agent supports multiple LLM providers (OpenAI, Anthropic, Doubao, Azure, OpenRouter, Ollama, Google Gemini), and the trajectory docs reference a dedicated client module for each of these providers. -- evidence: [docs/TRAJECTORY_RECORDING.md#L86-L86](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/docs/TRAJECTORY_RECORDING.md#L86-L86), [docs/TRAJECTORY_RECORDING.md#L100-L100](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/docs/TRAJECTORY_RECORDING.md#L100-L100), [docs/TRAJECTORY_RECORDING.md#L30-L30](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/docs/TRAJECTORY_RECORDING.md#L30-L30), [docs/TRAJECTORY_RECORDING.md#L72-L72](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/docs/TRAJECTORY_RECORDING.md#L72-L72), [docs/TRAJECTORY_RECORDING.md#L58-L58](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/docs/TRAJECTORY_RECORDING.md#L58-L58), [docs/TRAJECTORY_RECORDING.md#L44-L44](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/docs/TRAJECTORY_RECORDING.md#L44-L44), [README.md#L19-L25](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/README.md#L19-L25), [docs/TRAJECTORY_RECORDING.md#L114-L114](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/docs/TRAJECTORY_RECORDING.md#L114-L114)
  - [observation/documented] The bash tool runs commands in a persistent shared session with a 120-second per-command timeout, session restart, and background process support. -- evidence: [docs/tools.md#L24-L28](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/docs/tools.md#L24-L28)
- design-choices (2 claim(s)):
  - [observation/documented] Configuration is YAML-based (JSON is deprecated legacy), with priority order: command-line arguments > config file > environment variables > defaults; base_url overrides are supported. -- evidence: [docs/legacy_config.md#L3-L3](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/docs/legacy_config.md#L3-L3), [README.md#L123-L123](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/README.md#L123-L123), [README.md#L84-L84](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/README.md#L84-L84), [docs/legacy_config.md#L30-L33](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/docs/legacy_config.md#L30-L33)
  - [observation/documented] The example YAML config enables Lakeview step summarization, sets max_steps (e.g. 200), and selects tools such as bash, str_replace_based_edit_tool, sequentialthinking, and task_done. -- evidence: [README.md#L53-L63](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/README.md#L53-L63)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: the repo runs pre-commit and unit-test GitHub Actions workflows, and contributors are directed to CONTRIBUTING.md and docs/roadmap.md. -- evidence: [README.md#L13-L13](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/README.md#L13-L13), [README.md#L240-L240](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/README.md#L240-L240), [README.md#L3-L7](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/README.md#L3-L7)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (4 claim(s)):
  - [observation/documented] Trae Agent provides a CLI (trae-cli) that accepts natural-language task instructions and runs software engineering workflows, with 'run' and 'interactive' subcommands. -- evidence: [README.md#L133-L133](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/README.md#L133-L133), [README.md#L9-L9](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/README.md#L9-L9), [README.md#L139-L140](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/README.md#L139-L140)
  - [observation/documented] Interactive mode supports typed task descriptions plus commands: status, help, clear, and exit/quit. -- evidence: [README.md#L208-L213](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/README.md#L208-L213)
- memory-state (1 claim(s)):
  - [observation/documented] Trajectory recording captures LLM interactions, agent steps, tool usage, and metadata into JSON files, saved continuously during execution with auto-generated or custom filenames. -- evidence: [docs/TRAJECTORY_RECORDING.md#L160-L161](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/docs/TRAJECTORY_RECORDING.md#L160-L161), [docs/TRAJECTORY_RECORDING.md#L320-L324](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/docs/TRAJECTORY_RECORDING.md#L320-L324), [docs/TRAJECTORY_RECORDING.md#L3-L3](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/docs/TRAJECTORY_RECORDING.md#L3-L3), [README.md#L234-L234](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/README.md#L234-L234), [docs/TRAJECTORY_RECORDING.md#L9-L11](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/docs/TRAJECTORY_RECORDING.md#L9-L11)
- orchestration (1 claim(s)):
  - [observation/documented] Tasks can execute inside Docker: via an image, an existing container ID, a Dockerfile path, or a local tar image file, with an option to keep or remove the container afterward; Docker must be configured in the environment. -- evidence: [README.md#L200-L200](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/README.md#L200-L200), [README.md#L183-L183](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/README.md#L183-L183), [README.md#L188-L188](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/README.md#L188-L188), [README.md#L197-L197](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/README.md#L197-L197), [README.md#L203-L204](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/README.md#L203-L204), [README.md#L194-L194](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/README.md#L194-L194)
- tools-permissions (1 claim(s)):
  - [observation/documented] Optional MCP services can be enabled via an mcp_servers config section, e.g. launching a Playwright MCP server through npx. -- evidence: [README.md#L113-L113](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/README.md#L113-L113), [README.md#L115-L121](https://github.com/bytedance/trae-agent/blob/e839e559ac61bdd0e057c375dd1dee391fee797d/README.md#L115-L121)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
More evidence: [full detail](trae-agent.detail.md)

Metadata and full claim list: [full detail](trae-agent.detail.md)
Human notes ([notes](trae-agent.notes.md), never overwritten by build)

[Back to map index](../../index.md)
