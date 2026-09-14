# bhouston/mycoder

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 774e068e5dae @ 3e0884f69cea3872

## Summary (orientation draft, not independently verified)

Evidence consists of README and docs describing MyCoder, a CLI AI coding agent with configurable providers, browser automation, MCP support, sub-agents, and context compaction, plus contributor workflow instructions.

## Source coverage

Source coverage (partial): 6 of 18 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The repository is a monorepo with packages for the CLI (mycoder), the agent module (mycoder-agent), and a documentation website (mycoder-docs). -- evidence: [README.md#L181-L183](https://github.com/bhouston/mycoder/blob/774e068e5daefab9c18bac898521d238dd12c794/README.md#L181-L183)
- design-choices (1 claim(s)):
  - [observation/documented] A system browser detection feature lets MyCoder use installed Chrome, Edge, Firefox and other browsers on Windows, macOS, and Linux, falling back to Playwright's bundled browsers when none is found. -- evidence: [README.md#L230-L233](https://github.com/bhouston/mycoder/blob/774e068e5daefab9c18bac898521d238dd12c794/README.md#L230-L233), [README.md#L226-L226](https://github.com/bhouston/mycoder/blob/774e068e5daefab9c18bac898521d238dd12c794/README.md#L226-L226)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributors clone the repo, run pnpm install/build/test/commit, and releases follow Conventional Commits with an automated CI/CD pipeline that versions, generates a changelog, creates a GitHub Release, tags, and publishes to NPM after PR review and merge to main. -- evidence: [README.md#L207-L207](https://github.com/bhouston/mycoder/blob/774e068e5daefab9c18bac898521d238dd12c794/README.md#L207-L207), [README.md#L199-L199](https://github.com/bhouston/mycoder/blob/774e068e5daefab9c18bac898521d238dd12c794/README.md#L199-L199), [README.md#L196-L196](https://github.com/bhouston/mycoder/blob/774e068e5daefab9c18bac898521d238dd12c794/README.md#L196-L196), [README.md#L209-L216](https://github.com/bhouston/mycoder/blob/774e068e5daefab9c18bac898521d238dd12c794/README.md#L209-L216), [README.md#L189-L190](https://github.com/bhouston/mycoder/blob/774e068e5daefab9c18bac898521d238dd12c794/README.md#L189-L190), [README.md#L193-L193](https://github.com/bhouston/mycoder/blob/774e068e5daefab9c18bac898521d238dd12c794/README.md#L193-L193), [README.md#L202-L203](https://github.com/bhouston/mycoder/blob/774e068e5daefab9c18bac898521d238dd12c794/README.md#L202-L203)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (6 claim(s)):
  - [observation/documented] MyCoder is a command-line interface for AI-powered coding tasks, installable globally via npm. -- evidence: [README.md#L3-L3](https://github.com/bhouston/mycoder/blob/774e068e5daefab9c18bac898521d238dd12c794/README.md#L3-L3), [README.md#L21-L23](https://github.com/bhouston/mycoder/blob/774e068e5daefab9c18bac898521d238dd12c794/README.md#L21-L23)
  - [observation/documented] The CLI supports interactive mode (-i), prompt arguments, prompt files (-f), an --interactive correction mode, and flags like --userPrompt false and --upgradeCheck false for automated runs. -- evidence: [README.md#L37-L37](https://github.com/bhouston/mycoder/blob/774e068e5daefab9c18bac898521d238dd12c794/README.md#L37-L37), [README.md#L34-L34](https://github.com/bhouston/mycoder/blob/774e068e5daefab9c18bac898521d238dd12c794/README.md#L34-L34), [README.md#L43-L43](https://github.com/bhouston/mycoder/blob/774e068e5daefab9c18bac898521d238dd12c794/README.md#L43-L43), [README.md#L31-L31](https://github.com/bhouston/mycoder/blob/774e068e5daefab9c18bac898521d238dd12c794/README.md#L31-L31), [README.md#L46-L47](https://github.com/bhouston/mycoder/blob/774e068e5daefab9c18bac898521d238dd12c794/README.md#L46-L47), [README.md#L40-L40](https://github.com/bhouston/mycoder/blob/774e068e5daefab9c18bac898521d238dd12c794/README.md#L40-L40)
- memory-state (1 claim(s)):
  - [observation/documented] Status updates are sent every 5 interactions and when token usage exceeds 50%, and above 70% usage the agent is reminded to use the compactHistory tool, which summarizes all but a configurable number of recent messages. -- evidence: [example-status-update.md#L36-L36](https://github.com/bhouston/mycoder/blob/774e068e5daefab9c18bac898521d238dd12c794/example-status-update.md#L36-L36), [example-status-update.md#L50-L50](https://github.com/bhouston/mycoder/blob/774e068e5daefab9c18bac898521d238dd12c794/example-status-update.md#L50-L50), [example-status-update.md#L42-L48](https://github.com/bhouston/mycoder/blob/774e068e5daefab9c18bac898521d238dd12c794/example-status-update.md#L42-L48), [example-status-update.md#L28-L28](https://github.com/bhouston/mycoder/blob/774e068e5daefab9c18bac898521d238dd12c794/example-status-update.md#L28-L28)
- orchestration (1 claim(s)):
  - [observation/documented] MyCoder can spawn sub-agents for concurrent task processing, and status updates report active sub-agents, shell processes, and browser sessions. -- evidence: [example-status-update.md#L30-L34](https://github.com/bhouston/mycoder/blob/774e068e5daefab9c18bac898521d238dd12c794/example-status-update.md#L30-L34), [README.md#L7-L15](https://github.com/bhouston/mycoder/blob/774e068e5daefab9c18bac898521d238dd12c794/README.md#L7-L15), [example-status-update.md#L10-L12](https://github.com/bhouston/mycoder/blob/774e068e5daefab9c18bac898521d238dd12c794/example-status-update.md#L10-L12), [example-status-update.md#L19-L20](https://github.com/bhouston/mycoder/blob/774e068e5daefab9c18bac898521d238dd12c794/example-status-update.md#L19-L20), [example-status-update.md#L14-L17](https://github.com/bhouston/mycoder/blob/774e068e5daefab9c18bac898521d238dd12c794/example-status-update.md#L14-L17)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] The agent leverages Anthropic's Claude, OpenAI models, and Ollama, and uses Playwright for browser automation, which normally requires separate browser installation. -- evidence: [README.md#L7-L15](https://github.com/bhouston/mycoder/blob/774e068e5daefab9c18bac898521d238dd12c794/README.md#L7-L15), [README.md#L222-L222](https://github.com/bhouston/mycoder/blob/774e068e5daefab9c18bac898521d238dd12c794/README.md#L222-L222)
- limitations: unknown (no source-linked claim submitted for this facet)
- relevance: unknown (no source-linked claim submitted for this facet)

(4 additional claim(s) omitted for length; see [full detail](mycoder.detail.md) for every claim.)

Metadata and full claim list: [full detail](mycoder.detail.md)
Human notes ([notes](mycoder.notes.md), never overwritten by build)

[Back to map index](../../index.md)
