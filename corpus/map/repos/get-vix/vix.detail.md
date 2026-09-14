# get-vix/vix -- full detail

[Back to orientation](vix.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/get-vix/vix/8e4262d6d1a80ff8600e2fe7554a8dcc36367ed3/5bb529b55446d470.json](../../../wiki/dossiers/get-vix/vix/8e4262d6d1a80ff8600e2fe7554a8dcc36367ed3/5bb529b55446d470.json)

## specifications (1 claim(s))

- [observation/documented] Vix is described as a fast, token-efficient AI coding agent whose stem agents maximize prompt-cache reuse across phases and whose Tree-sitter virtual filesystem lets it read and edit minified code, claimed to cut tokens 20-50%. -- evidence: [README.md#L5-L5](https://github.com/get-vix/vix/blob/8e4262d6d1a80ff8600e2fe7554a8dcc36367ed3/README.md#L5-L5), [README.md#L23-L23](https://github.com/get-vix/vix/blob/8e4262d6d1a80ff8600e2fe7554a8dcc36367ed3/README.md#L23-L23) (`clm_6aa395684bce4bc756bb56e6d7a535a88804a7a56c6b15f67ba6af213c1fdaae`)

## components (1 claim(s))

- [observation/documented] The product consists of a daemon (vixd) and a client (vix); the daemon is started first, and multiple isolated vix instances can then be run. -- evidence: [README.md#L96-L96](https://github.com/get-vix/vix/blob/8e4262d6d1a80ff8600e2fe7554a8dcc36367ed3/README.md#L96-L96), [README.md#L92-L94](https://github.com/get-vix/vix/blob/8e4262d6d1a80ff8600e2fe7554a8dcc36367ed3/README.md#L92-L94), [README.md#L90-L90](https://github.com/get-vix/vix/blob/8e4262d6d1a80ff8600e2fe7554a8dcc36367ed3/README.md#L90-L90), [README.md#L98-L100](https://github.com/get-vix/vix/blob/8e4262d6d1a80ff8600e2fe7554a8dcc36367ed3/README.md#L98-L100) (`clm_3545dc45d9b7ad479e2c620228964c63671d24e94377e6814db097a6c512f092`)

## design-choices (2 claim(s))

- [observation/documented] The stem-agent design uses a generic system prompt with per-phase instructions delivered as user messages, so the explore-phase history stays cached when the LLM is told to act as a planner. -- evidence: [README.md#L133-L133](https://github.com/get-vix/vix/blob/8e4262d6d1a80ff8600e2fe7554a8dcc36367ed3/README.md#L133-L133), [README.md#L135-L135](https://github.com/get-vix/vix/blob/8e4262d6d1a80ff8600e2fe7554a8dcc36367ed3/README.md#L135-L135), [README.md#L129-L129](https://github.com/get-vix/vix/blob/8e4262d6d1a80ff8600e2fe7554a8dcc36367ed3/README.md#L129-L129) (`clm_9eb24386eb08953c860267c104b348ed50e7cdcc328b18c4d47e2c62583b44f9`)
- [observation/documented] Rather than limiting exploration, vix strips whitespace characters from file content via a virtual filesystem so the LLM works on minified code, reportedly reducing tokens by 20-50%. -- evidence: [README.md#L143-L143](https://github.com/get-vix/vix/blob/8e4262d6d1a80ff8600e2fe7554a8dcc36367ed3/README.md#L143-L143), [README.md#L145-L145](https://github.com/get-vix/vix/blob/8e4262d6d1a80ff8600e2fe7554a8dcc36367ed3/README.md#L145-L145) (`clm_16ad7ac3f1bb1bc1b0eee0e21bd983a2faa14e55e5129d60c20e2fb8c8e0e9ab`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (1 claim(s))

- [observation/documented] Vix advertises standard agent capabilities including skills, MCP servers, subagents, LSP-backed code intelligence, sandboxed execution, and multiple providers. -- evidence: [README.md#L29-L29](https://github.com/get-vix/vix/blob/8e4262d6d1a80ff8600e2fe7554a8dcc36367ed3/README.md#L29-L29) (`clm_a5cf3e5c13cf84d1175817479e9b17a39f8dd35f9f3e5c88d179a86fe9697aa8`)

## interfaces (6 claim(s))

- [observation/documented] Both vixd and vix expose a pprof HTTP server via --pprof-port (default ports 6060 and 6061, overridable by VIX_PPROF_PORT), serving goroutine, heap, allocs, and CPU profiles. -- evidence: [DEBUG.md#L29-L31](https://github.com/get-vix/vix/blob/8e4262d6d1a80ff8600e2fe7554a8dcc36367ed3/DEBUG.md#L29-L31), [DEBUG.md#L52-L59](https://github.com/get-vix/vix/blob/8e4262d6d1a80ff8600e2fe7554a8dcc36367ed3/DEBUG.md#L52-L59), [DEBUG.md#L6-L9](https://github.com/get-vix/vix/blob/8e4262d6d1a80ff8600e2fe7554a8dcc36367ed3/DEBUG.md#L6-L9), [DEBUG.md#L3-L4](https://github.com/get-vix/vix/blob/8e4262d6d1a80ff8600e2fe7554a8dcc36367ed3/DEBUG.md#L3-L4), [DEBUG.md#L38-L40](https://github.com/get-vix/vix/blob/8e4262d6d1a80ff8600e2fe7554a8dcc36367ed3/DEBUG.md#L38-L40) (`clm_abb732c45493367b0f6915840bdd8cca6f6627623c11943bb9e173bbb96afbb1`)
- [observation/documented] Providers are configured via a providers.json overlay in ~/.vix/ or ./.vix/ merged over an embedded base: same-id entries are field-patched, new ids appended, and models/credential_methods arrays replace wholesale. -- evidence: [PROVIDERS.md#L12-L13](https://github.com/get-vix/vix/blob/8e4262d6d1a80ff8600e2fe7554a8dcc36367ed3/PROVIDERS.md#L12-L13), [README.md#L110-L112](https://github.com/get-vix/vix/blob/8e4262d6d1a80ff8600e2fe7554a8dcc36367ed3/README.md#L110-L112), [PROVIDERS.md#L15-L16](https://github.com/get-vix/vix/blob/8e4262d6d1a80ff8600e2fe7554a8dcc36367ed3/PROVIDERS.md#L15-L16), [PROVIDERS.md#L18-L23](https://github.com/get-vix/vix/blob/8e4262d6d1a80ff8600e2fe7554a8dcc36367ed3/PROVIDERS.md#L18-L23) (`clm_ebfe153201e4121ed4c396c411725a8a6b69e32bf6b230a052ec0bb5ce5c779b`)
- [observation/documented] The wire_format field selects among a closed set of compiled HTTP adapters: chat_completions (OpenAI-compatible), messages (Anthropic), and responses (OpenAI Responses API); other values are rejected at load. -- evidence: [PROVIDERS.md#L108-L112](https://github.com/get-vix/vix/blob/8e4262d6d1a80ff8600e2fe7554a8dcc36367ed3/PROVIDERS.md#L108-L112), [PROVIDERS.md#L106-L106](https://github.com/get-vix/vix/blob/8e4262d6d1a80ff8600e2fe7554a8dcc36367ed3/PROVIDERS.md#L106-L106) (`clm_8624316264fceb42feac30c1bf13c2dbf6cf44166f2e8aa07bb2dbb17b6f4ded`)
- [observation/documented] Credential methods are tried in order and the first to resolve wins; kinds include api_key (env var or keyring), none, and OAuth flows (oauth_token, oauth_mint_key) referencing auth_logins entries by login_id. -- evidence: [PROVIDERS.md#L194-L197](https://github.com/get-vix/vix/blob/8e4262d6d1a80ff8600e2fe7554a8dcc36367ed3/PROVIDERS.md#L194-L197), [PROVIDERS.md#L147-L148](https://github.com/get-vix/vix/blob/8e4262d6d1a80ff8600e2fe7554a8dcc36367ed3/PROVIDERS.md#L147-L148), [PROVIDERS.md#L152-L154](https://github.com/get-vix/vix/blob/8e4262d6d1a80ff8600e2fe7554a8dcc36367ed3/PROVIDERS.md#L152-L154), [PROVIDERS.md#L169-L171](https://github.com/get-vix/vix/blob/8e4262d6d1a80ff8600e2fe7554a8dcc36367ed3/PROVIDERS.md#L169-L171), [PROVIDERS.md#L187-L188](https://github.com/get-vix/vix/blob/8e4262d6d1a80ff8600e2fe7554a8dcc36367ed3/PROVIDERS.md#L187-L188) (`clm_b8e46ecd9b155effeb248f4b2382de30c9607eab80d846fc35e3c0cdf2efbb9c`)
- [observation/documented] With local:true, the model list is fetched live from an OpenAI-compatible GET /models endpoint (cached 5 seconds), with Ollama- and llama.cpp-specific probes for loaded models and context lengths; unreachable servers show as offline after a 1.5s timeout. -- evidence: [PROVIDERS.md#L237-L240](https://github.com/get-vix/vix/blob/8e4262d6d1a80ff8600e2fe7554a8dcc36367ed3/PROVIDERS.md#L237-L240), [PROVIDERS.md#L231-L233](https://github.com/get-vix/vix/blob/8e4262d6d1a80ff8600e2fe7554a8dcc36367ed3/PROVIDERS.md#L231-L233), [PROVIDERS.md#L242-L243](https://github.com/get-vix/vix/blob/8e4262d6d1a80ff8600e2fe7554a8dcc36367ed3/PROVIDERS.md#L242-L243) (`clm_11d79d5e65c091396041c791d76df936842330d482f6b1e55b4d294a3a17f1e6`)
- [observation/documented] Installation is via a curl-piped install script or Homebrew tap (get-vix/vix), and requires ANTHROPIC_API_KEY to be set in the environment. -- evidence: [README.md#L83-L83](https://github.com/get-vix/vix/blob/8e4262d6d1a80ff8600e2fe7554a8dcc36367ed3/README.md#L83-L83), [README.md#L79-L81](https://github.com/get-vix/vix/blob/8e4262d6d1a80ff8600e2fe7554a8dcc36367ed3/README.md#L79-L81), [README.md#L85-L88](https://github.com/get-vix/vix/blob/8e4262d6d1a80ff8600e2fe7554a8dcc36367ed3/README.md#L85-L88) (`clm_beb97569d494bc062e86ddd6ffe7a1bd7b1d273af53365716936762caac39830`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (1 claim(s))

- [observation/documented] Users can define multi-phase agent pipelines in JSON with agent, bash, and tool steps, including templating, branching, parallelism, and history forking; custom workflows are configured in settings.json. -- evidence: [README.md#L25-L25](https://github.com/get-vix/vix/blob/8e4262d6d1a80ff8600e2fe7554a8dcc36367ed3/README.md#L25-L25), [README.md#L159-L159](https://github.com/get-vix/vix/blob/8e4262d6d1a80ff8600e2fe7554a8dcc36367ed3/README.md#L159-L159) (`clm_77520a9f5f9f5181495cb44caca0365d9a205b40aa0f34d2ddbdac3e0bda989a`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (1 claim(s))

- [observation/documented] The README reports a self-described non-scientific benchmark of vix plan mode against Claude Code on 7 real coding scenarios with the same prompt, measuring time and cost, with reproducible transcripts in a separate vix-eval repo; vix was faster and cheaper on almost all tasks. -- evidence: [README.md#L68-L68](https://github.com/get-vix/vix/blob/8e4262d6d1a80ff8600e2fe7554a8dcc36367ed3/README.md#L68-L68), [README.md#L51-L60](https://github.com/get-vix/vix/blob/8e4262d6d1a80ff8600e2fe7554a8dcc36367ed3/README.md#L51-L60), [README.md#L64-L64](https://github.com/get-vix/vix/blob/8e4262d6d1a80ff8600e2fe7554a8dcc36367ed3/README.md#L64-L64), [README.md#L45-L45](https://github.com/get-vix/vix/blob/8e4262d6d1a80ff8600e2fe7554a8dcc36367ed3/README.md#L45-L45), [README.md#L43-L43](https://github.com/get-vix/vix/blob/8e4262d6d1a80ff8600e2fe7554a8dcc36367ed3/README.md#L43-L43) (`clm_c173eb70a76e93de12a84d0fb32d7f022d42b77c8f5facbfe3596e47887ddd20`)

## dependencies (1 claim(s))

- [observation/documented] Vix ships built-in provider support for Anthropic, OpenAI, OpenRouter, OrcaRouter, AWS Bedrock, Ollama, llama.cpp, and Lemonade, among others. -- evidence: [README.md#L108-L108](https://github.com/get-vix/vix/blob/8e4262d6d1a80ff8600e2fe7554a8dcc36367ed3/README.md#L108-L108), [PROVIDERS.md#L285-L288](https://github.com/get-vix/vix/blob/8e4262d6d1a80ff8600e2fe7554a8dcc36367ed3/PROVIDERS.md#L285-L288), [PROVIDERS.md#L3-L6](https://github.com/get-vix/vix/blob/8e4262d6d1a80ff8600e2fe7554a8dcc36367ed3/PROVIDERS.md#L3-L6) (`clm_020a496a591bcacc57dc87e0a3dcf7401640c6e3e1128853ba970b17fb82ebe7`)

## limitations (2 claim(s))

- [observation/documented] The README warns that vix currently works only on macOS and Linux. -- evidence: [README.md#L76-L77](https://github.com/get-vix/vix/blob/8e4262d6d1a80ff8600e2fe7554a8dcc36367ed3/README.md#L76-L77) (`clm_ebaacd428ce48ed5c86ba840771f868324e5ee616cb4c0486337f474da618095`)
- [observation/documented] The benchmark summary notes vix lost on one task involving a 3,000+ line file, because minification only helped during exploration while execution fell back to regular read/edit tools. -- evidence: [README.md#L64-L64](https://github.com/get-vix/vix/blob/8e4262d6d1a80ff8600e2fe7554a8dcc36367ed3/README.md#L64-L64) (`clm_daf1e6e7c86ca43435b0d4dea6aeef9eb60326b604f33b1f7698510de294f8e4`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

