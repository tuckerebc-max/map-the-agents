# build-with-groq/groq-code-cli

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit a303eb4be01a @ 8a579905cbff1efb

## Summary (orientation draft, not independently verified)

Groq Code CLI is a lightweight, customizable coding CLI powered by Groq models, with slash commands, AI-callable tools, proxy support, and a small codebase positioned as a hackable blueprint for developers. Evidence is README documentation only; no license text is cited.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] The codebase is organized into src/commands (slash command definitions), src/core (agent and CLI entry), src/tools (schemas, implementations, validators), src/ui (TUI components and hooks), and src/utils. -- evidence: [README.md#L189-L189](https://github.com/build-with-groq/groq-code-cli/blob/a303eb4be01a53aaf3fbf319636e2b608e80aeca/README.md#L189-L189), [README.md#L152-L187](https://github.com/build-with-groq/groq-code-cli/blob/a303eb4be01a53aaf3fbf319636e2b608e80aeca/README.md#L152-L187)
  - [observation/documented] Tools are AI-callable functions defined by schemas in tool-schemas.ts, implemented in tools.ts, and registered via a TOOL_REGISTRY and executeTool switch plus an ALL_TOOL_SCHEMAS array. -- evidence: [README.md#L225-L225](https://github.com/build-with-groq/groq-code-cli/blob/a303eb4be01a53aaf3fbf319636e2b608e80aeca/README.md#L225-L225), [README.md#L215-L221](https://github.com/build-with-groq/groq-code-cli/blob/a303eb4be01a53aaf3fbf319636e2b608e80aeca/README.md#L215-L221), [README.md#L223-L223](https://github.com/build-with-groq/groq-code-cli/blob/a303eb4be01a53aaf3fbf319636e2b608e80aeca/README.md#L223-L223), [README.md#L197-L213](https://github.com/build-with-groq/groq-code-cli/blob/a303eb4be01a53aaf3fbf319636e2b608e80aeca/README.md#L197-L213)
- design-choices (1 claim(s)):
  - [observation/documented] The project is intentionally positioned as a small, hackable blueprint for developers to customize and extend, contrasting itself with large feature-rich coding CLIs. -- evidence: [README.md#L34-L34](https://github.com/build-with-groq/groq-code-cli/blob/a303eb4be01a53aaf3fbf319636e2b608e80aeca/README.md#L34-L34), [README.md#L32-L32](https://github.com/build-with-groq/groq-code-cli/blob/a303eb4be01a53aaf3fbf319636e2b608e80aeca/README.md#L32-L32)
- workflows (3 claim(s)):
  - [observation/documented] Repository development practice: the recommended development setup is cloning the repo, running npm install, npm run build, and npm link, with npm run dev in the background to auto-apply source changes. -- evidence: [README.md#L57-L58](https://github.com/build-with-groq/groq-code-cli/blob/a303eb4be01a53aaf3fbf319636e2b608e80aeca/README.md#L57-L58), [README.md#L141-L142](https://github.com/build-with-groq/groq-code-cli/blob/a303eb4be01a53aaf3fbf319636e2b608e80aeca/README.md#L141-L142), [README.md#L47-L53](https://github.com/build-with-groq/groq-code-cli/blob/a303eb4be01a53aaf3fbf319636e2b608e80aeca/README.md#L47-L53)
  - [observation/documented] Repository development practice: contributors can add slash commands by creating a definition file in src/commands/definitions/ and registering it in the availableCommands array in src/commands/index.ts. -- evidence: [README.md#L231-L233](https://github.com/build-with-groq/groq-code-cli/blob/a303eb4be01a53aaf3fbf319636e2b608e80aeca/README.md#L231-L233), [README.md#L235-L246](https://github.com/build-with-groq/groq-code-cli/blob/a303eb4be01a53aaf3fbf319636e2b608e80aeca/README.md#L235-L246), [README.md#L248-L248](https://github.com/build-with-groq/groq-code-cli/blob/a303eb4be01a53aaf3fbf319636e2b608e80aeca/README.md#L248-L248)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The CLI is started with the `groq` command and supports options including temperature, custom system message, debug logging, proxy URL, help, and version. -- evidence: [README.md#L82-L89](https://github.com/build-with-groq/groq-code-cli/blob/a303eb4be01a53aaf3fbf319636e2b608e80aeca/README.md#L82-L89), [README.md#L79-L80](https://github.com/build-with-groq/groq-code-cli/blob/a303eb4be01a53aaf3fbf319636e2b608e80aeca/README.md#L79-L80)
  - [observation/documented] Slash commands include /help, /login, /model, /clear, /reasoning, and /stats for help, login, model selection, history clearing, reasoning display, and token usage stats. -- evidence: [README.md#L128-L133](https://github.com/build-with-groq/groq-code-cli/blob/a303eb4be01a53aaf3fbf319636e2b608e80aeca/README.md#L128-L133)
- memory-state (1 claim(s)):
  - [observation/documented] Authentication via /login stores the API key, default model selection, and other config in a .groq/ folder in the home directory; the key can alternatively be set per-directory via the GROQ_API_KEY environment variable. -- evidence: [README.md#L106-L109](https://github.com/build-with-groq/groq-code-cli/blob/a303eb4be01a53aaf3fbf319636e2b608e80aeca/README.md#L106-L109), [README.md#L104-L104](https://github.com/build-with-groq/groq-code-cli/blob/a303eb4be01a53aaf3fbf319636e2b608e80aeca/README.md#L104-L104)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
More evidence: [full detail](groq-code-cli.detail.md)

Metadata and full claim list: [full detail](groq-code-cli.detail.md)
Human notes ([notes](groq-code-cli.notes.md), never overwritten by build)

[Back to map index](../../index.md)
