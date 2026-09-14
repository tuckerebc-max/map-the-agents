# github/copilot-cli

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit b49df25cafe8 @ bb11b5b4363508e2

## Summary (orientation draft, not independently verified)

The snapshot is README and license documentation for GitHub Copilot CLI, a terminal-based AI coding agent with GitHub integration, MCP extensibility, LSP support, and multiple install/auth paths. No source code or development-practice files are present in the evidence.

## Source coverage

Source coverage (partial): 2 of 3 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 5 facet(s); 8 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] The agent ships with GitHub's MCP server by default and supports adding custom MCP servers to extend its capabilities. -- evidence: [README.md#L16-L20](https://github.com/github/copilot-cli/blob/b49df25cafe802d2012876c8703332064237c7e3/README.md#L16-L20)
  - [observation/documented] It uses the same agentic harness as GitHub's Copilot coding agent, working locally and synchronously in the terminal. -- evidence: [README.md#L14-L14](https://github.com/github/copilot-cli/blob/b49df25cafe802d2012876c8703332064237c7e3/README.md#L14-L14), [README.md#L5-L5](https://github.com/github/copilot-cli/blob/b49df25cafe802d2012876c8703332064237c7e3/README.md#L5-L5)
- design-choices (2 claim(s)):
  - [observation/documented] The CLI previews every action before execution and requires explicit user approval, so nothing runs without consent. -- evidence: [README.md#L16-L20](https://github.com/github/copilot-cli/blob/b49df25cafe802d2012876c8703332064237c7e3/README.md#L16-L20)
  - [observation/documented] An experimental mode, enabled via the `--experimental` flag or `/experimental` command and persisted in config, unlocks in-development features like Autopilot mode cycled with Shift+Tab. -- evidence: [README.md#L126-L126](https://github.com/github/copilot-cli/blob/b49df25cafe802d2012876c8703332064237c7e3/README.md#L126-L126), [README.md#L135-L135](https://github.com/github/copilot-cli/blob/b49df25cafe802d2012876c8703332064237c7e3/README.md#L135-L135), [README.md#L128-L129](https://github.com/github/copilot-cli/blob/b49df25cafe802d2012876c8703332064237c7e3/README.md#L128-L129), [README.md#L131-L131](https://github.com/github/copilot-cli/blob/b49df25cafe802d2012876c8703332064237c7e3/README.md#L131-L131)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (4 claim(s)):
  - [observation/documented] Copilot CLI is a terminal application launched with the `copilot` command, offering natural-language conversations to build, debug, and understand code. -- evidence: [README.md#L101-L103](https://github.com/github/copilot-cli/blob/b49df25cafe802d2012876c8703332064237c7e3/README.md#L101-L103), [README.md#L120-L120](https://github.com/github/copilot-cli/blob/b49df25cafe802d2012876c8703332064237c7e3/README.md#L120-L120), [README.md#L3-L3](https://github.com/github/copilot-cli/blob/b49df25cafe802d2012876c8703332064237c7e3/README.md#L3-L3), [README.md#L5-L5](https://github.com/github/copilot-cli/blob/b49df25cafe802d2012876c8703332064237c7e3/README.md#L5-L5)
  - [observation/documented] Slash commands include `/login` for authentication, `/model` for model selection, `/experimental`, `/lsp` for LSP status, and `/feedback` for a confidential survey. -- evidence: [README.md#L194-L194](https://github.com/github/copilot-cli/blob/b49df25cafe802d2012876c8703332064237c7e3/README.md#L194-L194), [README.md#L107-L107](https://github.com/github/copilot-cli/blob/b49df25cafe802d2012876c8703332064237c7e3/README.md#L107-L107), [README.md#L128-L129](https://github.com/github/copilot-cli/blob/b49df25cafe802d2012876c8703332064237c7e3/README.md#L128-L129), [README.md#L184-L184](https://github.com/github/copilot-cli/blob/b49df25cafe802d2012876c8703332064237c7e3/README.md#L184-L184), [README.md#L122-L122](https://github.com/github/copilot-cli/blob/b49df25cafe802d2012876c8703332064237c7e3/README.md#L122-L122)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
  - [observation/documented] By default the CLI uses Claude Sonnet 4.5, with other models such as Claude Sonnet 4 and GPT-5 selectable via `/model`. -- evidence: [README.md#L122-L122](https://github.com/github/copilot-cli/blob/b49df25cafe802d2012876c8703332064237c7e3/README.md#L122-L122)
  - [observation/documented] Each submitted prompt reduces the user's monthly premium-requests quota by one, requiring an active Copilot subscription. -- evidence: [README.md#L137-L137](https://github.com/github/copilot-cli/blob/b49df25cafe802d2012876c8703332064237c7e3/README.md#L137-L137), [README.md#L34-L35](https://github.com/github/copilot-cli/blob/b49df25cafe802d2012876c8703332064237c7e3/README.md#L34-L35)
- limitations (2 claim(s)):
  - [observation/documented] The CLI does not bundle LSP servers; users must install language servers such as typescript-language-server separately. -- evidence: [README.md#L147-L147](https://github.com/github/copilot-cli/blob/b49df25cafe802d2012876c8703332064237c7e3/README.md#L147-L147), [README.md#L149-L151](https://github.com/github/copilot-cli/blob/b49df25cafe802d2012876c8703332064237c7e3/README.md#L149-L151)
  - [observation/documented] Organization or enterprise administrators can disable Copilot CLI access for their members via policy settings. -- evidence: [README.md#L37-L37](https://github.com/github/copilot-cli/blob/b49df25cafe802d2012876c8703332064237c7e3/README.md#L37-L37)
- relevance: unknown (no source-linked claim submitted for this facet)

(2 additional claim(s) omitted for length; see [full detail](copilot-cli.detail.md) for every claim.)

Metadata and full claim list: [full detail](copilot-cli.detail.md)
Human notes ([notes](copilot-cli.notes.md), never overwritten by build)

[Back to map index](../../index.md)
