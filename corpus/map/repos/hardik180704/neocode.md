# hardik180704/neocode

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 0c016cadc012 @ 0d07d5515adf4028

## Summary (orientation draft, not independently verified)

Selected evidence records: NeoCode is described as an open-source, terminal-native coding agent with streaming AI responses, persistent sessions, PLAN and BUILD modes, local repository tools, NeoLens codebase intelligence, themes, and optional MCP integrations. The repository is a Bun monorepo with a terminal client (packages/cli), API server (packages/server), shared package, Prisma database package, and a Vite-powered landing page (packages/web).

## Source coverage

Source coverage (partial): 6 of 7 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 14 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

14 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] NeoCode is described as an open-source, terminal-native coding agent with streaming AI responses, persistent sessions, PLAN and BUILD modes, local repository tools, NeoLens codebase intelligence, themes, and optional MCP integrations. -- evidence: [README.md#L21-L24](https://github.com/Hardik180704/NeoCode/blob/0c016cadc0123825da87ec3f351c02ad10a316cc/README.md#L21-L24)
- components (2 claim(s)):
  - [observation/documented] The repository is a Bun monorepo with a terminal client (packages/cli), API server (packages/server), shared package, Prisma database package, and a Vite-powered landing page (packages/web). -- evidence: [README.md#L26-L27](https://github.com/Hardik180704/NeoCode/blob/0c016cadc0123825da87ec3f351c02ad10a316cc/README.md#L26-L27), [README.md#L218-L226](https://github.com/Hardik180704/NeoCode/blob/0c016cadc0123825da87ec3f351c02ad10a316cc/README.md#L218-L226)
  - [observation/documented] NeoLens is a local codebase explorer with three views: Graph (TypeScript dependency relationships), Workspace (read-only file previews and capped search), and Timeline (tool-activity replay with token, duration, and estimated cost summaries). -- evidence: [README.md#L160-L166](https://github.com/Hardik180704/NeoCode/blob/0c016cadc0123825da87ec3f351c02ad10a316cc/README.md#L160-L166), [README.md#L146-L150](https://github.com/Hardik180704/NeoCode/blob/0c016cadc0123825da87ec3f351c02ad10a316cc/README.md#L146-L150)
- design-choices (2 claim(s)):
  - [observation/documented] NeoCode has two agent modes: PLAN for read-only investigation and BUILD for implementation; the /agents command switches between the corresponding agents. -- evidence: [README.md#L127-L136](https://github.com/Hardik180704/NeoCode/blob/0c016cadc0123825da87ec3f351c02ad10a316cc/README.md#L127-L136), [README.md#L31-L40](https://github.com/Hardik180704/NeoCode/blob/0c016cadc0123825da87ec3f351c02ad10a316cc/README.md#L31-L40)
  - [observation/documented] NeoLens is project-scoped and keeps source local: it respects .gitignore rules, never follows symbolic links, hides credential files, rejects paths outside the project, and caps indexing/search/preview work; the Railway API receives session activity but not file contents. -- evidence: [README.md#L172-L178](https://github.com/Hardik180704/NeoCode/blob/0c016cadc0123825da87ec3f351c02ad10a316cc/README.md#L172-L178)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: contributors install Bun 1.3.13, run bun install --frozen-lockfile, start services with bun run dev:server/dev:cli/dev:web, and run bun test and bun run check before opening a pull request. -- evidence: [docs/DEVELOPMENT.md#L17-L20](https://github.com/Hardik180704/NeoCode/blob/0c016cadc0123825da87ec3f351c02ad10a316cc/docs/DEVELOPMENT.md#L17-L20), [docs/DEVELOPMENT.md#L77-L81](https://github.com/Hardik180704/NeoCode/blob/0c016cadc0123825da87ec3f351c02ad10a316cc/docs/DEVELOPMENT.md#L77-L81), [CONTRIBUTING.md#L45-L49](https://github.com/Hardik180704/NeoCode/blob/0c016cadc0123825da87ec3f351c02ad10a316cc/CONTRIBUTING.md#L45-L49), [CONTRIBUTING.md#L43-L43](https://github.com/Hardik180704/NeoCode/blob/0c016cadc0123825da87ec3f351c02ad10a316cc/CONTRIBUTING.md#L43-L43), [docs/DEVELOPMENT.md#L9-L12](https://github.com/Hardik180704/NeoCode/blob/0c016cadc0123825da87ec3f351c02ad10a316cc/docs/DEVELOPMENT.md#L9-L12)
  - [observation/documented] Repository development practice: the release workflow builds eight platform targets with archives, checksums, and GitHub provenance attestations, and opens an automated Homebrew formula update PR in the tap repository. -- evidence: [docs/RELEASING.md#L40-L43](https://github.com/Hardik180704/NeoCode/blob/0c016cadc0123825da87ec3f351c02ad10a316cc/docs/RELEASING.md#L40-L43)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The CLI exposes slash commands including /new, /agents, /models, /sessions, /lens, /mcp, /theme, and /login, and API_URL can point the CLI at a different NeoCode API. -- evidence: [README.md#L138-L138](https://github.com/Hardik180704/NeoCode/blob/0c016cadc0123825da87ec3f351c02ad10a316cc/README.md#L138-L138), [README.md#L127-L136](https://github.com/Hardik180704/NeoCode/blob/0c016cadc0123825da87ec3f351c02ad10a316cc/README.md#L127-L136), [README.md#L140-L142](https://github.com/Hardik180704/NeoCode/blob/0c016cadc0123825da87ec3f351c02ad10a316cc/README.md#L140-L142)
  - [observation/documented] Standalone binaries for macOS, Linux, and Windows are published via GitHub Releases and include the Bun runtime, so users need not install Bun or Node.js; Homebrew installation is also supported. -- evidence: [README.md#L68-L70](https://github.com/Hardik180704/NeoCode/blob/0c016cadc0123825da87ec3f351c02ad10a316cc/README.md#L68-L70), [README.md#L46-L48](https://github.com/Hardik180704/NeoCode/blob/0c016cadc0123825da87ec3f351c02ad10a316cc/README.md#L46-L48), [README.md#L31-L40](https://github.com/Hardik180704/NeoCode/blob/0c016cadc0123825da87ec3f351c02ad10a316cc/README.md#L31-L40)
More evidence: [full detail](neocode.detail.md)

Metadata and full claim list: [full detail](neocode.detail.md)
Human notes ([notes](neocode.notes.md), never overwritten by build)

[Back to map index](../../index.md)
