# build-with-groq/groq-code-cli -- full detail

[Back to orientation](groq-code-cli.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/build-with-groq/groq-code-cli/a303eb4be01a53aaf3fbf319636e2b608e80aeca/8a579905cbff1efb.json](../../../wiki/dossiers/build-with-groq/groq-code-cli/a303eb4be01a53aaf3fbf319636e2b608e80aeca/8a579905cbff1efb.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] The codebase is organized into src/commands (slash command definitions), src/core (agent and CLI entry), src/tools (schemas, implementations, validators), src/ui (TUI components and hooks), and src/utils. -- evidence: [README.md#L189-L189](https://github.com/build-with-groq/groq-code-cli/blob/a303eb4be01a53aaf3fbf319636e2b608e80aeca/README.md#L189-L189), [README.md#L152-L187](https://github.com/build-with-groq/groq-code-cli/blob/a303eb4be01a53aaf3fbf319636e2b608e80aeca/README.md#L152-L187) (`clm_30f6c22f3f42096bc07afc8c30350b66dbe41d1a1c2ed8fc85b4885ad5bbb0b4`)
- [observation/documented] Tools are AI-callable functions defined by schemas in tool-schemas.ts, implemented in tools.ts, and registered via a TOOL_REGISTRY and executeTool switch plus an ALL_TOOL_SCHEMAS array. -- evidence: [README.md#L225-L225](https://github.com/build-with-groq/groq-code-cli/blob/a303eb4be01a53aaf3fbf319636e2b608e80aeca/README.md#L225-L225), [README.md#L215-L221](https://github.com/build-with-groq/groq-code-cli/blob/a303eb4be01a53aaf3fbf319636e2b608e80aeca/README.md#L215-L221), [README.md#L223-L223](https://github.com/build-with-groq/groq-code-cli/blob/a303eb4be01a53aaf3fbf319636e2b608e80aeca/README.md#L223-L223), [README.md#L197-L213](https://github.com/build-with-groq/groq-code-cli/blob/a303eb4be01a53aaf3fbf319636e2b608e80aeca/README.md#L197-L213) (`clm_ca52f0aa2f558d5dfb91e0fb71531166e1a4b91f5dcc9dee569b0e8b20e967b9`)

## design-choices (1 claim(s))

- [observation/documented] The project is intentionally positioned as a small, hackable blueprint for developers to customize and extend, contrasting itself with large feature-rich coding CLIs. -- evidence: [README.md#L34-L34](https://github.com/build-with-groq/groq-code-cli/blob/a303eb4be01a53aaf3fbf319636e2b608e80aeca/README.md#L34-L34), [README.md#L32-L32](https://github.com/build-with-groq/groq-code-cli/blob/a303eb4be01a53aaf3fbf319636e2b608e80aeca/README.md#L32-L32) (`clm_516de3498966d3f5a6d2b8dc1e805279daa189b6323cabc0b20fb3f0729fc603`)

## workflows (3 claim(s))

- [observation/documented] Repository development practice: the recommended development setup is cloning the repo, running npm install, npm run build, and npm link, with npm run dev in the background to auto-apply source changes. -- evidence: [README.md#L57-L58](https://github.com/build-with-groq/groq-code-cli/blob/a303eb4be01a53aaf3fbf319636e2b608e80aeca/README.md#L57-L58), [README.md#L141-L142](https://github.com/build-with-groq/groq-code-cli/blob/a303eb4be01a53aaf3fbf319636e2b608e80aeca/README.md#L141-L142), [README.md#L47-L53](https://github.com/build-with-groq/groq-code-cli/blob/a303eb4be01a53aaf3fbf319636e2b608e80aeca/README.md#L47-L53) (`clm_a8dcb31bf3b72de9f3ac5117bbbdfa1edecf39e830226c54c22276874889364a`)
- [observation/documented] Repository development practice: contributors can add slash commands by creating a definition file in src/commands/definitions/ and registering it in the availableCommands array in src/commands/index.ts. -- evidence: [README.md#L231-L233](https://github.com/build-with-groq/groq-code-cli/blob/a303eb4be01a53aaf3fbf319636e2b608e80aeca/README.md#L231-L233), [README.md#L235-L246](https://github.com/build-with-groq/groq-code-cli/blob/a303eb4be01a53aaf3fbf319636e2b608e80aeca/README.md#L235-L246), [README.md#L248-L248](https://github.com/build-with-groq/groq-code-cli/blob/a303eb4be01a53aaf3fbf319636e2b608e80aeca/README.md#L248-L248) (`clm_cc8e7e16bac131c91e867af1ceab83a5f224db714df054cff249e686656afbdf`)
- [observation/documented] Repository development practice: the start command can be changed by editing the "bin" entry named "groq" in package.json, then re-running npm run build and npm link. -- evidence: [README.md#L253-L253](https://github.com/build-with-groq/groq-code-cli/blob/a303eb4be01a53aaf3fbf319636e2b608e80aeca/README.md#L253-L253), [README.md#L251-L251](https://github.com/build-with-groq/groq-code-cli/blob/a303eb4be01a53aaf3fbf319636e2b608e80aeca/README.md#L251-L251) (`clm_c720a9fea422335ba4160ba1e63d6fb9e709663de5bc12be37739ef49cc36559`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The CLI is started with the `groq` command and supports options including temperature, custom system message, debug logging, proxy URL, help, and version. -- evidence: [README.md#L82-L89](https://github.com/build-with-groq/groq-code-cli/blob/a303eb4be01a53aaf3fbf319636e2b608e80aeca/README.md#L82-L89), [README.md#L79-L80](https://github.com/build-with-groq/groq-code-cli/blob/a303eb4be01a53aaf3fbf319636e2b608e80aeca/README.md#L79-L80) (`clm_95a88068569a10ec3f95a94470eb3c9b021eb1c99c1453ae62e7913c0837c7d2`)
- [observation/documented] Slash commands include /help, /login, /model, /clear, /reasoning, and /stats for help, login, model selection, history clearing, reasoning display, and token usage stats. -- evidence: [README.md#L128-L133](https://github.com/build-with-groq/groq-code-cli/blob/a303eb4be01a53aaf3fbf319636e2b608e80aeca/README.md#L128-L133) (`clm_a9b0f52a6f4648e91c9998bde85b0503a71355b11db5589e9be44c6e30831055`)
- [observation/documented] Proxy support covers HTTP/HTTPS/SOCKS5 via a --proxy flag or HTTP_PROXY/HTTPS_PROXY environment variables, with the flag taking highest priority. -- evidence: [README.md#L121-L123](https://github.com/build-with-groq/groq-code-cli/blob/a303eb4be01a53aaf3fbf319636e2b608e80aeca/README.md#L121-L123), [README.md#L117-L118](https://github.com/build-with-groq/groq-code-cli/blob/a303eb4be01a53aaf3fbf319636e2b608e80aeca/README.md#L117-L118), [README.md#L113-L113](https://github.com/build-with-groq/groq-code-cli/blob/a303eb4be01a53aaf3fbf319636e2b608e80aeca/README.md#L113-L113), [README.md#L125-L125](https://github.com/build-with-groq/groq-code-cli/blob/a303eb4be01a53aaf3fbf319636e2b608e80aeca/README.md#L125-L125) (`clm_4961151b07767306a98461469a0149e8272974babb5ec77d60aaa36a45ab6cf9`)

## memory-state (1 claim(s))

- [observation/documented] Authentication via /login stores the API key, default model selection, and other config in a .groq/ folder in the home directory; the key can alternatively be set per-directory via the GROQ_API_KEY environment variable. -- evidence: [README.md#L106-L109](https://github.com/build-with-groq/groq-code-cli/blob/a303eb4be01a53aaf3fbf319636e2b608e80aeca/README.md#L106-L109), [README.md#L104-L104](https://github.com/build-with-groq/groq-code-cli/blob/a303eb4be01a53aaf3fbf319636e2b608e80aeca/README.md#L104-L104) (`clm_e06b14de38a364dd702d8fe942e46b4a4c0f73eab0ab459f54dacf6d62d91371`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The project is distributed as the npm package groq-code-cli, runnable via npx without installation or installable globally, and built with npm scripts (build, dev watch mode) from TypeScript to dist/. -- evidence: [README.md#L63-L64](https://github.com/build-with-groq/groq-code-cli/blob/a303eb4be01a53aaf3fbf319636e2b608e80aeca/README.md#L63-L64), [README.md#L67-L69](https://github.com/build-with-groq/groq-code-cli/blob/a303eb4be01a53aaf3fbf319636e2b608e80aeca/README.md#L67-L69), [README.md#L145-L148](https://github.com/build-with-groq/groq-code-cli/blob/a303eb4be01a53aaf3fbf319636e2b608e80aeca/README.md#L145-L148) (`clm_53c23ca581dc671a4d72325e0c55a28ce484fa6a97c7caf3ce849837105c76e7`)

## limitations (1 claim(s))

- [inference/documented] The CLI appears to depend on Groq-hosted models for its agent, with a /models command to list available models, suggesting it does not operate without Groq API access. -- evidence: [README.md#L34-L34](https://github.com/build-with-groq/groq-code-cli/blob/a303eb4be01a53aaf3fbf319636e2b608e80aeca/README.md#L34-L34) (`clm_436ba64c89ebd5bbcca22b988cdf3deecf6ceef037eb8a59c3c0ead154298a90`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

