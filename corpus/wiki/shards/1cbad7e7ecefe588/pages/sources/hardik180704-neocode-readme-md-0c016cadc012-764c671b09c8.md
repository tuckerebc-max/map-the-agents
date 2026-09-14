---
access: public
aliases: []
claim_ids:
- clm_13e5e051893240533e51ebb2502f38f355a54339443bbdd25a09fb4ce9587c85
- clm_162162155edf7705a8cc310d66c2f184e72f6ad2854ba7f58b4963cdd45b6b80
- clm_1eee16f9975100caa6166d463e3d38a33157f4c1bb4864bb0374014a7b549e94
- clm_323ade47fc038e67c2c4dfbd0a4782dd2eff5148c3ba4a04324f167b0cf43045
- clm_5d151589b03f9b636c914ca1968e237905f0c6e19ada82f07defa49b5e1cce45
- clm_73ea5333b41aa527c05395b2ed0b78103294390827b790fc15e6a02b1eb0766d
- clm_7fb1996554173ae15b989368b1be6b67ac6c85895709462db25ac44c0c5f574d
- clm_8d70bb43485fc8beab61b3f9d11c0beb0e7a34e4e40d18a3bbcad40bf6c2a2e6
- clm_bafc70538b01004da3a39bdb6fef4a2ee4bec2c2c710c21f9cfa63c2bcd23f00
- clm_d2542301208de71fffcc9f922d0b326a5ff6b351ec0ae3da5e865d79b1196310
- clm_eccbb2da05c806bd512b022bd56aee5c462c09a16f96340f2784fbad8f0b6fb8
- clm_f57bf841cc946245e85ff9f5be09f5d91a13908bdcdd933b86a1210ac93051f3
maturity: draft
page_id: pg_8dbd171347df59a69abc764c671b09c8
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_d4fb8f17ec345e5ca792bd7c211f3737
title: Hardik180704/NeoCode/README.md @ 0c016cadc012
updated_at: '2026-09-14T02:01:33Z'
---

# Hardik180704/NeoCode/README.md @ 0c016cadc012

<!-- rcw:begin owner=source:src_d4fb8f17ec345e5ca792bd7c211f3737 block=evidence -->
- Sessions are persistent and can be reopened via the /sessions command to browse previous conversations. [@claim:clm_13e5e051893240533e51ebb2502f38f355a54339443bbdd25a09fb4ce9587c85]
- NeoLens is a local codebase explorer with three views: Graph (TypeScript dependency relationships), Workspace (read-only file previews and capped search), and Timeline (tool-activity replay with token, duration, and estimated cost summaries). [@claim:clm_162162155edf7705a8cc310d66c2f184e72f6ad2854ba7f58b4963cdd45b6b80]
- MCP tools are denied by default and require an explicit policy: read tools are available in PLAN and BUILD, write tools only in BUILD, and disabled tools are never exposed to the model; a wildcard policy can classify unlisted tools. [@claim:clm_1eee16f9975100caa6166d463e3d38a33157f4c1bb4864bb0374014a7b549e94]
- NeoLens is project-scoped and keeps source local: it respects .gitignore rules, never follows symbolic links, hides credential files, rejects paths outside the project, and caps indexing/search/preview work; the Railway API receives session activity but not file contents. [@claim:clm_323ade47fc038e67c2c4dfbd0a4782dd2eff5148c3ba4a04324f167b0cf43045]
- Current release binaries are unsigned: macOS may require manual Privacy & Security approval and Windows may show a SmartScreen warning; SHA-256 checksums and GitHub attestations are published for verification. [@claim:clm_5d151589b03f9b636c914ca1968e237905f0c6e19ada82f07defa49b5e1cce45]
- The repository is a Bun monorepo with a terminal client (packages/cli), API server (packages/server), shared package, Prisma database package, and a Vite-powered landing page (packages/web). [@claim:clm_73ea5333b41aa527c05395b2ed0b78103294390827b790fc15e6a02b1eb0766d]
- MCP integration is optional and discovered from a project-local .neocode/mcp.json; without it, built-in local tools still work. Supported transports are stdio for local servers and Streamable HTTP for remote servers. [@claim:clm_7fb1996554173ae15b989368b1be6b67ac6c85895709462db25ac44c0c5f574d]
- NeoCode is described as an open-source, terminal-native coding agent with streaming AI responses, persistent sessions, PLAN and BUILD modes, local repository tools, NeoLens codebase intelligence, themes, and optional MCP integrations. [@claim:clm_8d70bb43485fc8beab61b3f9d11c0beb0e7a34e4e40d18a3bbcad40bf6c2a2e6]
- NeoCode has two agent modes: PLAN for read-only investigation and BUILD for implementation; the /agents command switches between the corresponding agents. [@claim:clm_bafc70538b01004da3a39bdb6fef4a2ee4bec2c2c710c21f9cfa63c2bcd23f00]
- The CLI exposes slash commands including /new, /agents, /models, /sessions, /lens, /mcp, /theme, and /login, and API_URL can point the CLI at a different NeoCode API. [@claim:clm_d2542301208de71fffcc9f922d0b326a5ff6b351ec0ae3da5e865d79b1196310]
- MCP secrets use environment references such as ${env:GITHUB_TOKEN}; resolved values stay in the server process and are not returned by the MCP inspection API, and local stdio servers inherit only a small safe set of variables plus their declared env block. [@claim:clm_eccbb2da05c806bd512b022bd56aee5c462c09a16f96340f2784fbad8f0b6fb8]
- Standalone binaries for macOS, Linux, and Windows are published via GitHub Releases and include the Bun runtime, so users need not install Bun or Node.js; Homebrew installation is also supported. [@claim:clm_f57bf841cc946245e85ff9f5be09f5d91a13908bdcdd933b86a1210ac93051f3]
<!-- rcw:end owner=source:src_d4fb8f17ec345e5ca792bd7c211f3737 block=evidence -->

## Researcher notes

