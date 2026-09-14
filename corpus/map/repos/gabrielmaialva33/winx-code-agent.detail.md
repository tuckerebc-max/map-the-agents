# gabrielmaialva33/winx-code-agent -- full detail

[Back to orientation](winx-code-agent.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/gabrielmaialva33/winx-code-agent/a48e7a9f7e863f85750a98be7452e005c1486ec9/3dc3feafd9c47b9c.json](../../../wiki/dossiers/gabrielmaialva33/winx-code-agent/a48e7a9f7e863f85750a98be7452e005c1486ec9/3dc3feafd9c47b9c.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] On Unix, the MCP adapter is separated from PTY-owning processes: winxd manages the control plane and one winx-guardian per session keeps shells alive across disconnects and adapter upgrades. -- evidence: [README.md#L40-L44](https://github.com/gabrielmaialva33/winx-code-agent/blob/a48e7a9f7e863f85750a98be7452e005c1486ec9/README.md#L40-L44), [README.md#L325-L328](https://github.com/gabrielmaialva33/winx-code-agent/blob/a48e7a9f7e863f85750a98be7452e005c1486ec9/README.md#L325-L328) (`clm_6d461971413b29e13aa6de780592d6e79d453b1308a861ac4eacf1169117ac81`)

## design-choices (1 claim(s))

- [observation/documented] The SEARCH/REPLACE matcher tolerates model mistakes: indentation adjustment, smart-quote normalization, line-number stripping, neighbor-block disambiguation, and one retry on over-escaped quotes, while refusing heavily fuzzy matches. -- evidence: [README.md#L300-L314](https://github.com/gabrielmaialva33/winx-code-agent/blob/a48e7a9f7e863f85750a98be7452e005c1486ec9/README.md#L300-L314) (`clm_11ff99f9eb38a7e680c02a6444ea1f3dae14710abfec58990717c078d122ee6b`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] Winx is a remote-first MCP runtime exposing a Streamable HTTP endpoint at /mcp (default 127.0.0.1:8000) plus a stdio transport for local clients like Claude Code, Cursor, and VS Code. -- evidence: [README.md#L100-L103](https://github.com/gabrielmaialva33/winx-code-agent/blob/a48e7a9f7e863f85750a98be7452e005c1486ec9/README.md#L100-L103), [README.md#L35-L38](https://github.com/gabrielmaialva33/winx-code-agent/blob/a48e7a9f7e863f85750a98be7452e005c1486ec9/README.md#L35-L38), [README.md#L692-L693](https://github.com/gabrielmaialva33/winx-code-agent/blob/a48e7a9f7e863f85750a98be7452e005c1486ec9/README.md#L692-L693) (`clm_d90c1e8ff044aa2a9a6b34cbda42fc588922e04af9c4a8ec87dcddba1b1134a2`)
- [observation/documented] The single mutation tool EditFiles supports replace, SEARCH/REPLACE, revision-bound line patches, atomic batches, verification, and undo, with legacy edit names kept as hidden compatibility aliases. -- evidence: [README.md#L234-L239](https://github.com/gabrielmaialva33/winx-code-agent/blob/a48e7a9f7e863f85750a98be7452e005c1486ec9/README.md#L234-L239), [README.md#L195-L197](https://github.com/gabrielmaialva33/winx-code-agent/blob/a48e7a9f7e863f85750a98be7452e005c1486ec9/README.md#L195-L197), [README.md#L82-L96](https://github.com/gabrielmaialva33/winx-code-agent/blob/a48e7a9f7e863f85750a98be7452e005c1486ec9/README.md#L82-L96) (`clm_c76755fb1b3d5d067bce1993547f1583eb8a2554b909a991373d96dee48dbb01`)
- [observation/documented] Winx advertises MCP 2026-07-28; every tool publishes an outputSchema and returns a structuredContent envelope whose authoritative status field enumerates states like completed, conflict, needs_read, and denied. -- evidence: [README.md#L241-L266](https://github.com/gabrielmaialva33/winx-code-agent/blob/a48e7a9f7e863f85750a98be7452e005c1486ec9/README.md#L241-L266) (`clm_be9e773f1613dfe0ba8f4a425042b68bc83be5f11c0ae3fcba71ea2e1d0128ab`)

## memory-state (1 claim(s))

- [observation/documented] Durable sessions survive HTTP disconnects: guardians are capped at 32 by default with tiered idle retention (30 minutes never-used, 24 hours used), and active commands are never evicted. -- evidence: [README.md#L643-L647](https://github.com/gabrielmaialva33/winx-code-agent/blob/a48e7a9f7e863f85750a98be7452e005c1486ec9/README.md#L643-L647) (`clm_0c44421c9e3214370ff6ae51fa9e18ea24e9810789938d65cee3b1a07512b48d`)

## orchestration (1 claim(s))

- [observation/documented] MCP Tasks on BashCommand are capability-driven: adaptive promotes only after runtime state is running, until_complete creates a Task immediately, and return_early never does; cancellation is generation-bound with a fail-closed fallback. -- evidence: [README.md#L268-L280](https://github.com/gabrielmaialva33/winx-code-agent/blob/a48e7a9f7e863f85750a98be7452e005c1486ec9/README.md#L268-L280) (`clm_ca797917cdac719391d5d6289ae7a93bf16460945d5ba98c6eb1925691caa934`)

## tools-permissions (3 claim(s))

- [observation/documented] Workspaces have three modes: wcgw (full access), architect (read-only), and code_writer (command allowlist plus write globs), with the allowlist parsed via tree-sitter to check every command including pipelines and substitutions. -- evidence: [README.md#L137-L191](https://github.com/gabrielmaialva33/winx-code-agent/blob/a48e7a9f7e863f85750a98be7452e005c1486ec9/README.md#L137-L191) (`clm_c8e4d665c37d330a8a24ba66bf52949e3d865968f2595414dd4a8a11446a144e`)
- [observation/documented] Tool catalogs are profiled as terminal (2 tools), read-only (4), coding (5), and full (7), or an exact per-principal allowlist; policy is enforced at both discovery and dispatch. -- evidence: [README.md#L219-L220](https://github.com/gabrielmaialva33/winx-code-agent/blob/a48e7a9f7e863f85750a98be7452e005c1486ec9/README.md#L219-L220), [README.md#L204-L209](https://github.com/gabrielmaialva33/winx-code-agent/blob/a48e7a9f7e863f85750a98be7452e005c1486ec9/README.md#L204-L209), [README.md#L199-L202](https://github.com/gabrielmaialva33/winx-code-agent/blob/a48e7a9f7e863f85750a98be7452e005c1486ec9/README.md#L199-L202) (`clm_ed8671aa6e67eae8708539aaf717048ad72fa9b209551d701e557448b1f64aba`)
- [observation/documented] HTTP security defaults include loopback-only binding, 32-byte minimum bearer tokens, chmod-600 token files, DNS-rebinding host checks, 64 MiB body cap, 120 req/min per-IP rate limiting, and delayed invalid-auth responses. -- evidence: [README.md#L763-L776](https://github.com/gabrielmaialva33/winx-code-agent/blob/a48e7a9f7e863f85750a98be7452e005c1486ec9/README.md#L763-L776), [README.md#L82-L96](https://github.com/gabrielmaialva33/winx-code-agent/blob/a48e7a9f7e863f85750a98be7452e005c1486ec9/README.md#L82-L96) (`clm_13bd3a346b30c7b50bf5512510615d7a0bb26734cea32f4b292e980193f8b699`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Building requires Rust 1.88+ and bash; the durable daemon runtime is supported on Linux/macOS/WSL2, while native Windows uses an embedded runtime with sessions tied to the server process. -- evidence: [README.md#L330-L333](https://github.com/gabrielmaialva33/winx-code-agent/blob/a48e7a9f7e863f85750a98be7452e005c1486ec9/README.md#L330-L333) (`clm_dd2cba8dbd10a6a67da84f4938f0cda1e96b2ac009fe6ba4aba5a595464a10a8`)

## limitations (1 claim(s))

- [observation/documented] The README warns that a valid principal is equivalent to shell and file access as the OS user, and that BashCommand in wcgw mode is not workspace-confined. -- evidence: [README.md#L791-L795](https://github.com/gabrielmaialva33/winx-code-agent/blob/a48e7a9f7e863f85750a98be7452e005c1486ec9/README.md#L791-L795) (`clm_498d289ab333b26845e9bea1a7442bd09115936d7e574d82a70753ff9058492c`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

