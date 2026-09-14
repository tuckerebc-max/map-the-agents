# aattaran/deepclaude -- full detail

[Back to orientation](deepclaude.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/aattaran/deepclaude/70518b6cdcf3cc488e62e817b86da4b550dd7dfa/5d655440a2eb307f.json](../../../wiki/dossiers/aattaran/deepclaude/70518b6cdcf3cc488e62e817b86da4b550dd7dfa/5d655440a2eb307f.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The product consists of platform launcher scripts (deepclaude.ps1 for Windows, deepclaude.sh for macOS/Linux) plus a Node-based local proxy component. -- evidence: [README.md#L51-L55](https://github.com/aattaran/deepclaude/blob/70518b6cdcf3cc488e62e817b86da4b550dd7dfa/README.md#L51-L55), [README.md#L318-L320](https://github.com/aattaran/deepclaude/blob/70518b6cdcf3cc488e62e817b86da4b550dd7dfa/README.md#L318-L320), [README.md#L45-L45](https://github.com/aattaran/deepclaude/blob/70518b6cdcf3cc488e62e817b86da4b550dd7dfa/README.md#L45-L45), [README.md#L322-L322](https://github.com/aattaran/deepclaude/blob/70518b6cdcf3cc488e62e817b86da4b550dd7dfa/README.md#L322-L322) (`clm_e284560b6b4f2f3799eb14e8284c132c293700e3108fc22161292077c6e0308e`)

## design-choices (3 claim(s))

- [observation/documented] The tool sets Claude Code environment variables (e.g. ANTHROPIC_BASE_URL, ANTHROPIC_AUTH_TOKEN, model-tier variables) per session and restores original settings on exit rather than persisting them. -- evidence: [README.md#L74-L81](https://github.com/aattaran/deepclaude/blob/70518b6cdcf3cc488e62e817b86da4b550dd7dfa/README.md#L74-L81), [README.md#L72-L72](https://github.com/aattaran/deepclaude/blob/70518b6cdcf3cc488e62e817b86da4b550dd7dfa/README.md#L72-L72), [README.md#L83-L83](https://github.com/aattaran/deepclaude/blob/70518b6cdcf3cc488e62e817b86da4b550dd7dfa/README.md#L83-L83) (`clm_b8c3083374e2a38acf7ea39d2f836aad77e8e441cb78b9fc1ba52d741eff5f93`)
- [observation/documented] Backend switching works mid-session without restart via slash commands, a CLI --switch flag, or VS Code tasks that POST to the proxy's mode endpoint. -- evidence: [README.md#L150-L150](https://github.com/aattaran/deepclaude/blob/70518b6cdcf3cc488e62e817b86da4b550dd7dfa/README.md#L150-L150), [README.md#L204-L207](https://github.com/aattaran/deepclaude/blob/70518b6cdcf3cc488e62e817b86da4b550dd7dfa/README.md#L204-L207), [README.md#L177-L177](https://github.com/aattaran/deepclaude/blob/70518b6cdcf3cc488e62e817b86da4b550dd7dfa/README.md#L177-L177), [README.md#L200-L200](https://github.com/aattaran/deepclaude/blob/70518b6cdcf3cc488e62e817b86da4b550dd7dfa/README.md#L200-L200), [README.md#L211-L232](https://github.com/aattaran/deepclaude/blob/70518b6cdcf3cc488e62e817b86da4b550dd7dfa/README.md#L211-L232) (`clm_79365cc07170d0ad05b9891ea3960ae2b545b6d2da3ccd81455e5bd514b5a2a9`)
- [inference/documented] The proxy appears to pass through non-/v1/messages traffic to Anthropic unchanged, so only model API calls are rerouted. -- evidence: [README.md#L164-L173](https://github.com/aattaran/deepclaude/blob/70518b6cdcf3cc488e62e817b86da4b550dd7dfa/README.md#L164-L173), [README.md#L309-L315](https://github.com/aattaran/deepclaude/blob/70518b6cdcf3cc488e62e817b86da4b550dd7dfa/README.md#L309-L315) (`clm_e6d8ebc3451893026b5439c68d442fd320654961279eca38fefba7340977d4e8`)

## workflows (1 claim(s))

- [observation/documented] Setup involves obtaining a DeepSeek API key, setting DEEPSEEK_API_KEY via setx or shell profile, and installing the script on PATH by copy or symlink. -- evidence: [README.md#L51-L55](https://github.com/aattaran/deepclaude/blob/70518b6cdcf3cc488e62e817b86da4b550dd7dfa/README.md#L51-L55), [README.md#L45-L45](https://github.com/aattaran/deepclaude/blob/70518b6cdcf3cc488e62e817b86da4b550dd7dfa/README.md#L45-L45), [README.md#L25-L25](https://github.com/aattaran/deepclaude/blob/70518b6cdcf3cc488e62e817b86da4b550dd7dfa/README.md#L25-L25), [README.md#L29-L32](https://github.com/aattaran/deepclaude/blob/70518b6cdcf3cc488e62e817b86da4b550dd7dfa/README.md#L29-L32), [README.md#L34-L38](https://github.com/aattaran/deepclaude/blob/70518b6cdcf3cc488e62e817b86da4b550dd7dfa/README.md#L34-L38) (`clm_6f7da39702c1469dbdc0ad7fcd32088c414bb9e2c039a57a1c5f896117ebd39f`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (4 claim(s))

- [observation/documented] The CLI supports flags including --status, --backend (ds/or/fw/anthropic), --cost, --benchmark, --switch, and --remote, per the usage examples. -- evidence: [README.md#L204-L207](https://github.com/aattaran/deepclaude/blob/70518b6cdcf3cc488e62e817b86da4b550dd7dfa/README.md#L204-L207), [README.md#L297-L301](https://github.com/aattaran/deepclaude/blob/70518b6cdcf3cc488e62e817b86da4b550dd7dfa/README.md#L297-L301), [README.md#L59-L68](https://github.com/aattaran/deepclaude/blob/70518b6cdcf3cc488e62e817b86da4b550dd7dfa/README.md#L59-L68) (`clm_ad24844036b5d2e52a06e5d6e4292615aae35b03d8d091eca0810e17cdba1980`)
- [observation/documented] A local proxy on localhost:3200 exposes control endpoints: POST /_proxy/mode to switch backends, GET /_proxy/status, and GET /_proxy/cost, forwarding /v1/messages to the active backend. -- evidence: [README.md#L162-L162](https://github.com/aattaran/deepclaude/blob/70518b6cdcf3cc488e62e817b86da4b550dd7dfa/README.md#L162-L162), [README.md#L164-L173](https://github.com/aattaran/deepclaude/blob/70518b6cdcf3cc488e62e817b86da4b550dd7dfa/README.md#L164-L173) (`clm_87d0e4d80cd9787e07a75fb6e29a853bec628cb3afdb7c8200502c51a3e291d5`)
- [observation/documented] The --cost endpoint returns per-backend token counts, request counts, cost, an anthropic_equivalent figure, and total savings as JSON. -- evidence: [README.md#L244-L246](https://github.com/aattaran/deepclaude/blob/70518b6cdcf3cc488e62e817b86da4b550dd7dfa/README.md#L244-L246), [README.md#L248-L264](https://github.com/aattaran/deepclaude/blob/70518b6cdcf3cc488e62e817b86da4b550dd7dfa/README.md#L248-L264) (`clm_10f056634a8ba8b8c19d9a383d353e5e14f763387c0d820f7213d2807bd6f8fb`)
- [observation/documented] Remote control mode prints a claude.ai/code session URL usable from a browser, keeping the WebSocket bridge on Anthropic while model calls route through the local proxy. -- evidence: [README.md#L295-L295](https://github.com/aattaran/deepclaude/blob/70518b6cdcf3cc488e62e817b86da4b550dd7dfa/README.md#L295-L295), [README.md#L307-L307](https://github.com/aattaran/deepclaude/blob/70518b6cdcf3cc488e62e817b86da4b550dd7dfa/README.md#L307-L307), [README.md#L303-L303](https://github.com/aattaran/deepclaude/blob/70518b6cdcf3cc488e62e817b86da4b550dd7dfa/README.md#L303-L303), [README.md#L309-L315](https://github.com/aattaran/deepclaude/blob/70518b6cdcf3cc488e62e817b86da4b550dd7dfa/README.md#L309-L315) (`clm_886d0c6a2de6f7863af35c2fce74e9e8327895e56bc9413e142f40377f86b15c`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Prerequisites are a logged-in Claude Code install, a claude.ai subscription (the remote bridge is Anthropic infrastructure), Node.js 18+ for the proxy, and backend API keys such as DEEPSEEK_API_KEY. -- evidence: [README.md#L318-L320](https://github.com/aattaran/deepclaude/blob/70518b6cdcf3cc488e62e817b86da4b550dd7dfa/README.md#L318-L320), [README.md#L96-L100](https://github.com/aattaran/deepclaude/blob/70518b6cdcf3cc488e62e817b86da4b550dd7dfa/README.md#L96-L100), [README.md#L108-L112](https://github.com/aattaran/deepclaude/blob/70518b6cdcf3cc488e62e817b86da4b550dd7dfa/README.md#L108-L112), [README.md#L102-L106](https://github.com/aattaran/deepclaude/blob/70518b6cdcf3cc488e62e817b86da4b550dd7dfa/README.md#L102-L106) (`clm_55127b79e3a893c302f1682bde7603b03b196c7e3f8c500e5d3d9d7e654ed110`)

## limitations (2 claim(s))

- [observation/documented] Documented degraded features: no image/vision input through DeepSeek's endpoint, no MCP server tools via the compatibility layer, sequential tool calls by default, and Anthropic cache_control ignored. -- evidence: [README.md#L137-L142](https://github.com/aattaran/deepclaude/blob/70518b6cdcf3cc488e62e817b86da4b550dd7dfa/README.md#L137-L142) (`clm_df2f2873b71a5ce3656a5c44182210eb57e4b68cb432980097b6ee757d0f748b`)
- [observation/documented] The README states Claude Opus is stronger on complex reasoning, recommending --backend anthropic for hard problems while DeepSeek is comparable on routine tasks. -- evidence: [README.md#L145-L146](https://github.com/aattaran/deepclaude/blob/70518b6cdcf3cc488e62e817b86da4b550dd7dfa/README.md#L145-L146) (`clm_77f453c6f5fa5bce0b17f3791f04517206cbe88926f87ee483b34de3ca5e2540`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

