# hardik180704/neocode -- full detail

[Back to orientation](neocode.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/hardik180704/neocode/0c016cadc0123825da87ec3f351c02ad10a316cc/0d07d5515adf4028.json](../../../wiki/dossiers/hardik180704/neocode/0c016cadc0123825da87ec3f351c02ad10a316cc/0d07d5515adf4028.json)

## specifications (1 claim(s))

- [observation/documented] NeoCode is described as an open-source, terminal-native coding agent with streaming AI responses, persistent sessions, PLAN and BUILD modes, local repository tools, NeoLens codebase intelligence, themes, and optional MCP integrations. -- evidence: [README.md#L21-L24](https://github.com/Hardik180704/NeoCode/blob/0c016cadc0123825da87ec3f351c02ad10a316cc/README.md#L21-L24) (`clm_8d70bb43485fc8beab61b3f9d11c0beb0e7a34e4e40d18a3bbcad40bf6c2a2e6`)

## components (2 claim(s))

- [observation/documented] The repository is a Bun monorepo with a terminal client (packages/cli), API server (packages/server), shared package, Prisma database package, and a Vite-powered landing page (packages/web). -- evidence: [README.md#L26-L27](https://github.com/Hardik180704/NeoCode/blob/0c016cadc0123825da87ec3f351c02ad10a316cc/README.md#L26-L27), [README.md#L218-L226](https://github.com/Hardik180704/NeoCode/blob/0c016cadc0123825da87ec3f351c02ad10a316cc/README.md#L218-L226) (`clm_73ea5333b41aa527c05395b2ed0b78103294390827b790fc15e6a02b1eb0766d`)
- [observation/documented] NeoLens is a local codebase explorer with three views: Graph (TypeScript dependency relationships), Workspace (read-only file previews and capped search), and Timeline (tool-activity replay with token, duration, and estimated cost summaries). -- evidence: [README.md#L160-L166](https://github.com/Hardik180704/NeoCode/blob/0c016cadc0123825da87ec3f351c02ad10a316cc/README.md#L160-L166), [README.md#L146-L150](https://github.com/Hardik180704/NeoCode/blob/0c016cadc0123825da87ec3f351c02ad10a316cc/README.md#L146-L150) (`clm_162162155edf7705a8cc310d66c2f184e72f6ad2854ba7f58b4963cdd45b6b80`)

## design-choices (2 claim(s))

- [observation/documented] NeoCode has two agent modes: PLAN for read-only investigation and BUILD for implementation; the /agents command switches between the corresponding agents. -- evidence: [README.md#L127-L136](https://github.com/Hardik180704/NeoCode/blob/0c016cadc0123825da87ec3f351c02ad10a316cc/README.md#L127-L136), [README.md#L31-L40](https://github.com/Hardik180704/NeoCode/blob/0c016cadc0123825da87ec3f351c02ad10a316cc/README.md#L31-L40) (`clm_bafc70538b01004da3a39bdb6fef4a2ee4bec2c2c710c21f9cfa63c2bcd23f00`)
- [observation/documented] NeoLens is project-scoped and keeps source local: it respects .gitignore rules, never follows symbolic links, hides credential files, rejects paths outside the project, and caps indexing/search/preview work; the Railway API receives session activity but not file contents. -- evidence: [README.md#L172-L178](https://github.com/Hardik180704/NeoCode/blob/0c016cadc0123825da87ec3f351c02ad10a316cc/README.md#L172-L178) (`clm_323ade47fc038e67c2c4dfbd0a4782dd2eff5148c3ba4a04324f167b0cf43045`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: contributors install Bun 1.3.13, run bun install --frozen-lockfile, start services with bun run dev:server/dev:cli/dev:web, and run bun test and bun run check before opening a pull request. -- evidence: [docs/DEVELOPMENT.md#L17-L20](https://github.com/Hardik180704/NeoCode/blob/0c016cadc0123825da87ec3f351c02ad10a316cc/docs/DEVELOPMENT.md#L17-L20), [docs/DEVELOPMENT.md#L77-L81](https://github.com/Hardik180704/NeoCode/blob/0c016cadc0123825da87ec3f351c02ad10a316cc/docs/DEVELOPMENT.md#L77-L81), [CONTRIBUTING.md#L45-L49](https://github.com/Hardik180704/NeoCode/blob/0c016cadc0123825da87ec3f351c02ad10a316cc/CONTRIBUTING.md#L45-L49), [CONTRIBUTING.md#L43-L43](https://github.com/Hardik180704/NeoCode/blob/0c016cadc0123825da87ec3f351c02ad10a316cc/CONTRIBUTING.md#L43-L43), [docs/DEVELOPMENT.md#L9-L12](https://github.com/Hardik180704/NeoCode/blob/0c016cadc0123825da87ec3f351c02ad10a316cc/docs/DEVELOPMENT.md#L9-L12) (`clm_7d5405b5257200d29167261f08ad98f8930ff5aa85970a6233fade5954887c97`)
- [observation/documented] Repository development practice: the release workflow builds eight platform targets with archives, checksums, and GitHub provenance attestations, and opens an automated Homebrew formula update PR in the tap repository. -- evidence: [docs/RELEASING.md#L40-L43](https://github.com/Hardik180704/NeoCode/blob/0c016cadc0123825da87ec3f351c02ad10a316cc/docs/RELEASING.md#L40-L43) (`clm_332f193b0c60efb991549341250f20e35988fae4862b82d24623c8ca2e2b2fa5`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The CLI exposes slash commands including /new, /agents, /models, /sessions, /lens, /mcp, /theme, and /login, and API_URL can point the CLI at a different NeoCode API. -- evidence: [README.md#L138-L138](https://github.com/Hardik180704/NeoCode/blob/0c016cadc0123825da87ec3f351c02ad10a316cc/README.md#L138-L138), [README.md#L127-L136](https://github.com/Hardik180704/NeoCode/blob/0c016cadc0123825da87ec3f351c02ad10a316cc/README.md#L127-L136), [README.md#L140-L142](https://github.com/Hardik180704/NeoCode/blob/0c016cadc0123825da87ec3f351c02ad10a316cc/README.md#L140-L142) (`clm_d2542301208de71fffcc9f922d0b326a5ff6b351ec0ae3da5e865d79b1196310`)
- [observation/documented] Standalone binaries for macOS, Linux, and Windows are published via GitHub Releases and include the Bun runtime, so users need not install Bun or Node.js; Homebrew installation is also supported. -- evidence: [README.md#L68-L70](https://github.com/Hardik180704/NeoCode/blob/0c016cadc0123825da87ec3f351c02ad10a316cc/README.md#L68-L70), [README.md#L46-L48](https://github.com/Hardik180704/NeoCode/blob/0c016cadc0123825da87ec3f351c02ad10a316cc/README.md#L46-L48), [README.md#L31-L40](https://github.com/Hardik180704/NeoCode/blob/0c016cadc0123825da87ec3f351c02ad10a316cc/README.md#L31-L40) (`clm_f57bf841cc946245e85ff9f5be09f5d91a13908bdcdd933b86a1210ac93051f3`)

## memory-state (1 claim(s))

- [observation/documented] Sessions are persistent and can be reopened via the /sessions command to browse previous conversations. -- evidence: [README.md#L127-L136](https://github.com/Hardik180704/NeoCode/blob/0c016cadc0123825da87ec3f351c02ad10a316cc/README.md#L127-L136), [README.md#L31-L40](https://github.com/Hardik180704/NeoCode/blob/0c016cadc0123825da87ec3f351c02ad10a316cc/README.md#L31-L40) (`clm_13e5e051893240533e51ebb2502f38f355a54339443bbdd25a09fb4ce9587c85`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (2 claim(s))

- [observation/documented] MCP tools are denied by default and require an explicit policy: read tools are available in PLAN and BUILD, write tools only in BUILD, and disabled tools are never exposed to the model; a wildcard policy can classify unlisted tools. -- evidence: [README.md#L192-L192](https://github.com/Hardik180704/NeoCode/blob/0c016cadc0123825da87ec3f351c02ad10a316cc/README.md#L192-L192), [README.md#L194-L198](https://github.com/Hardik180704/NeoCode/blob/0c016cadc0123825da87ec3f351c02ad10a316cc/README.md#L194-L198), [README.md#L200-L201](https://github.com/Hardik180704/NeoCode/blob/0c016cadc0123825da87ec3f351c02ad10a316cc/README.md#L200-L201) (`clm_1eee16f9975100caa6166d463e3d38a33157f4c1bb4864bb0374014a7b549e94`)
- [observation/documented] MCP secrets use environment references such as ${env:GITHUB_TOKEN}; resolved values stay in the server process and are not returned by the MCP inspection API, and local stdio servers inherit only a small safe set of variables plus their declared env block. -- evidence: [README.md#L203-L206](https://github.com/Hardik180704/NeoCode/blob/0c016cadc0123825da87ec3f351c02ad10a316cc/README.md#L203-L206) (`clm_eccbb2da05c806bd512b022bd56aee5c462c09a16f96340f2784fbad8f0b6fb8`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] MCP integration is optional and discovered from a project-local .neocode/mcp.json; without it, built-in local tools still work. Supported transports are stdio for local servers and Streamable HTTP for remote servers. -- evidence: [README.md#L182-L183](https://github.com/Hardik180704/NeoCode/blob/0c016cadc0123825da87ec3f351c02ad10a316cc/README.md#L182-L183), [README.md#L210-L211](https://github.com/Hardik180704/NeoCode/blob/0c016cadc0123825da87ec3f351c02ad10a316cc/README.md#L210-L211) (`clm_7fb1996554173ae15b989368b1be6b67ac6c85895709462db25ac44c0c5f574d`)

## limitations (1 claim(s))

- [observation/documented] Current release binaries are unsigned: macOS may require manual Privacy & Security approval and Windows may show a SmartScreen warning; SHA-256 checksums and GitHub attestations are published for verification. -- evidence: [docs/RELEASING.md#L72-L78](https://github.com/Hardik180704/NeoCode/blob/0c016cadc0123825da87ec3f351c02ad10a316cc/docs/RELEASING.md#L72-L78), [README.md#L72-L75](https://github.com/Hardik180704/NeoCode/blob/0c016cadc0123825da87ec3f351c02ad10a316cc/README.md#L72-L75) (`clm_5d151589b03f9b636c914ca1968e237905f0c6e19ada82f07defa49b5e1cce45`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

