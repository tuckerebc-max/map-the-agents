---
access: public
aliases: []
claim_ids:
- clm_30f6c22f3f42096bc07afc8c30350b66dbe41d1a1c2ed8fc85b4885ad5bbb0b4
- clm_436ba64c89ebd5bbcca22b988cdf3deecf6ceef037eb8a59c3c0ead154298a90
- clm_4961151b07767306a98461469a0149e8272974babb5ec77d60aaa36a45ab6cf9
- clm_516de3498966d3f5a6d2b8dc1e805279daa189b6323cabc0b20fb3f0729fc603
- clm_53c23ca581dc671a4d72325e0c55a28ce484fa6a97c7caf3ce849837105c76e7
- clm_95a88068569a10ec3f95a94470eb3c9b021eb1c99c1453ae62e7913c0837c7d2
- clm_a8dcb31bf3b72de9f3ac5117bbbdfa1edecf39e830226c54c22276874889364a
- clm_a9b0f52a6f4648e91c9998bde85b0503a71355b11db5589e9be44c6e30831055
- clm_c720a9fea422335ba4160ba1e63d6fb9e709663de5bc12be37739ef49cc36559
- clm_ca52f0aa2f558d5dfb91e0fb71531166e1a4b91f5dcc9dee569b0e8b20e967b9
- clm_cc8e7e16bac131c91e867af1ceab83a5f224db714df054cff249e686656afbdf
- clm_e06b14de38a364dd702d8fe942e46b4a4c0f73eab0ab459f54dacf6d62d91371
maturity: draft
page_id: pg_5bc5f9460b9e543f82cce68a37380645
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_b191c32b198a52deb82ab1a1e85639cc
title: build-with-groq/groq-code-cli/README.md @ a303eb4be01a
updated_at: '2026-09-14T01:38:51Z'
---

# build-with-groq/groq-code-cli/README.md @ a303eb4be01a

<!-- rcw:begin owner=source:src_b191c32b198a52deb82ab1a1e85639cc block=evidence -->
- The codebase is organized into src/commands (slash command definitions), src/core (agent and CLI entry), src/tools (schemas, implementations, validators), src/ui (TUI components and hooks), and src/utils. [@claim:clm_30f6c22f3f42096bc07afc8c30350b66dbe41d1a1c2ed8fc85b4885ad5bbb0b4]
- The CLI appears to depend on Groq-hosted models for its agent, with a /models command to list available models, suggesting it does not operate without Groq API access. [@claim:clm_436ba64c89ebd5bbcca22b988cdf3deecf6ceef037eb8a59c3c0ead154298a90]
- Proxy support covers HTTP/HTTPS/SOCKS5 via a --proxy flag or HTTP_PROXY/HTTPS_PROXY environment variables, with the flag taking highest priority. [@claim:clm_4961151b07767306a98461469a0149e8272974babb5ec77d60aaa36a45ab6cf9]
- The project is intentionally positioned as a small, hackable blueprint for developers to customize and extend, contrasting itself with large feature-rich coding CLIs. [@claim:clm_516de3498966d3f5a6d2b8dc1e805279daa189b6323cabc0b20fb3f0729fc603]
- The project is distributed as the npm package groq-code-cli, runnable via npx without installation or installable globally, and built with npm scripts (build, dev watch mode) from TypeScript to dist/. [@claim:clm_53c23ca581dc671a4d72325e0c55a28ce484fa6a97c7caf3ce849837105c76e7]
- The CLI is started with the `groq` command and supports options including temperature, custom system message, debug logging, proxy URL, help, and version. [@claim:clm_95a88068569a10ec3f95a94470eb3c9b021eb1c99c1453ae62e7913c0837c7d2]
- Repository development practice: the recommended development setup is cloning the repo, running npm install, npm run build, and npm link, with npm run dev in the background to auto-apply source changes. [@claim:clm_a8dcb31bf3b72de9f3ac5117bbbdfa1edecf39e830226c54c22276874889364a]
- Slash commands include /help, /login, /model, /clear, /reasoning, and /stats for help, login, model selection, history clearing, reasoning display, and token usage stats. [@claim:clm_a9b0f52a6f4648e91c9998bde85b0503a71355b11db5589e9be44c6e30831055]
- Repository development practice: the start command can be changed by editing the "bin" entry named "groq" in package.json, then re-running npm run build and npm link. [@claim:clm_c720a9fea422335ba4160ba1e63d6fb9e709663de5bc12be37739ef49cc36559]
- Tools are AI-callable functions defined by schemas in tool-schemas.ts, implemented in tools.ts, and registered via a TOOL_REGISTRY and executeTool switch plus an ALL_TOOL_SCHEMAS array. [@claim:clm_ca52f0aa2f558d5dfb91e0fb71531166e1a4b91f5dcc9dee569b0e8b20e967b9]
- Repository development practice: contributors can add slash commands by creating a definition file in src/commands/definitions/ and registering it in the availableCommands array in src/commands/index.ts. [@claim:clm_cc8e7e16bac131c91e867af1ceab83a5f224db714df054cff249e686656afbdf]
- Authentication via /login stores the API key, default model selection, and other config in a .groq/ folder in the home directory; the key can alternatively be set per-directory via the GROQ_API_KEY environment variable. [@claim:clm_e06b14de38a364dd702d8fe942e46b4a4c0f73eab0ab459f54dacf6d62d91371]
<!-- rcw:end owner=source:src_b191c32b198a52deb82ab1a1e85639cc block=evidence -->

## Researcher notes

