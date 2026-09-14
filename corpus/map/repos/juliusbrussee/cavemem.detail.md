# juliusbrussee/cavemem -- full detail

[Back to orientation](cavemem.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/juliusbrussee/cavemem/166078dd7c463b8e3006da28b2401fb063303f88/f87f7425c04f96c8.json](../../../wiki/dossiers/juliusbrussee/cavemem/166078dd7c463b8e3006da28b2401fb063303f88/f87f7425c04f96c8.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (2 claim(s))

- [observation/documented] Compression is deterministic and offline, never invoking a model; technical tokens (code, URLs, paths, commands, versions, dates, numbers, identifiers) are preserved byte-for-byte and prose is lossy only on filler/hedging words. -- evidence: [docs/compression.md#L5-L7](https://github.com/JuliusBrussee/cavemem/blob/166078dd7c463b8e3006da28b2401fb063303f88/docs/compression.md#L5-L7), [docs/compression.md#L3-L3](https://github.com/JuliusBrussee/cavemem/blob/166078dd7c463b8e3006da28b2401fb063303f88/docs/compression.md#L3-L3) (`clm_79544db9a6dd960cbb0764a47337b6d8b58bb0b46c5b87effbfbcfc206148890`)
- [observation/documented] Search is hybrid: SQLite FTS5 BM25 keyword matching blended with a local vector index, weighted by the tunable search.alpha setting (default 0.5). -- evidence: [docs/mcp.md#L26-L26](https://github.com/JuliusBrussee/cavemem/blob/166078dd7c463b8e3006da28b2401fb063303f88/docs/mcp.md#L26-L26), [README.md#L165-L178](https://github.com/JuliusBrussee/cavemem/blob/166078dd7c463b8e3006da28b2401fb063303f88/README.md#L165-L178), [README.md#L28-L35](https://github.com/JuliusBrussee/cavemem/blob/166078dd7c463b8e3006da28b2401fb063303f88/README.md#L28-L35) (`clm_480027dceffab8387cd4e6f137c4e4000d2e01c942ca21d43dfd440fac4d33fb`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: contributors must pass four gates (pnpm typecheck, lint, test, build) before merging, add changesets for package changes, use Conventional Commits, and get one review on PRs. -- evidence: [CLAUDE.md#L52-L60](https://github.com/JuliusBrussee/cavemem/blob/166078dd7c463b8e3006da28b2401fb063303f88/CLAUDE.md#L52-L60), [docs/development.md#L42-L42](https://github.com/JuliusBrussee/cavemem/blob/166078dd7c463b8e3006da28b2401fb063303f88/docs/development.md#L42-L42), [CLAUDE.md#L89-L90](https://github.com/JuliusBrussee/cavemem/blob/166078dd7c463b8e3006da28b2401fb063303f88/CLAUDE.md#L89-L90), [docs/development.md#L35-L40](https://github.com/JuliusBrussee/cavemem/blob/166078dd7c463b8e3006da28b2401fb063303f88/docs/development.md#L35-L40) (`clm_2a2353bea03c8280a40b04662eb0a4d0823fb74a0e0d1cda4460d532d3c3faff`)
- [observation/documented] Repository development practice: an end-to-end publish script (scripts/e2e-publish.sh) must pass in CI before changeset publish, driving real hook events, FTS search, and the MCP server in an isolated install prefix. -- evidence: [CLAUDE.md#L66-L69](https://github.com/JuliusBrussee/cavemem/blob/166078dd7c463b8e3006da28b2401fb063303f88/CLAUDE.md#L66-L69) (`clm_0c12ac598840de1d240853f7894df7c1af5156a02b57b7dc602dc169e4ad271c`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The CLI offers commands including install/uninstall per IDE, status, config show/get/set/open, viewer, doctor, search, compress, reindex, export/import JSONL, and an stdio MCP server. -- evidence: [README.md#L114-L128](https://github.com/JuliusBrussee/cavemem/blob/166078dd7c463b8e3006da28b2401fb063303f88/README.md#L114-L128) (`clm_709d3de502f98f815dd6192a06d792030c4c8233931a2f2d64d83755f34a14af`)
- [observation/documented] The MCP server exposes search, timeline, get_observations, and list_sessions, plus an opt-in enrich tool; search and timeline return compact results while get_observations fetches full bodies. -- evidence: [README.md#L138-L144](https://github.com/JuliusBrussee/cavemem/blob/166078dd7c463b8e3006da28b2401fb063303f88/README.md#L138-L144), [README.md#L136-L136](https://github.com/JuliusBrussee/cavemem/blob/166078dd7c463b8e3006da28b2401fb063303f88/README.md#L136-L136), [docs/mcp.md#L3-L3](https://github.com/JuliusBrussee/cavemem/blob/166078dd7c463b8e3006da28b2401fb063303f88/docs/mcp.md#L3-L3) (`clm_678ba0783d1b892060edc42a069e4f41b9b62d173e8bcbc803e80e3812eb98f6`)

## memory-state (1 claim(s))

- [observation/documented] Memory persists in a local SQLite database with FTS5 updated via triggers; embeddings are computed out-of-band by a background worker that auto-spawns on the first hook and self-exits when idle. -- evidence: [docs/architecture.md#L21-L26](https://github.com/JuliusBrussee/cavemem/blob/166078dd7c463b8e3006da28b2401fb063303f88/docs/architecture.md#L21-L26), [README.md#L49-L49](https://github.com/JuliusBrussee/cavemem/blob/166078dd7c463b8e3006da28b2401fb063303f88/README.md#L49-L49) (`clm_3a40fa0208bb18e5513f35db0e9746a1e7c454a6c705c37c1d65d401f8d9120c`)

## orchestration (1 claim(s))

- [observation/documented] Per-IDE installers wire hooks and MCP: Claude Code, OpenCode, Codex, Copilot, and Augment capture observations, while Cursor, Gemini CLI, Antigravity, and IBM Bob are query-only over memory captured elsewhere. -- evidence: [README.md#L55-L65](https://github.com/JuliusBrussee/cavemem/blob/166078dd7c463b8e3006da28b2401fb063303f88/README.md#L55-L65), [README.md#L26-L26](https://github.com/JuliusBrussee/cavemem/blob/166078dd7c463b8e3006da28b2401fb063303f88/README.md#L26-L26) (`clm_5876598e81e58c868cf404f2baa200a4126ea147b0101e82383e4a359dcaa183`)

## tools-permissions (2 claim(s))

- [observation/documented] The viewer worker binds to 127.0.0.1 only, checks Host/Origin headers, and requires a local bearer token (mode 0600) on /api/* endpoints. -- evidence: [README.md#L180-L180](https://github.com/JuliusBrussee/cavemem/blob/166078dd7c463b8e3006da28b2401fb063303f88/README.md#L180-L180) (`clm_2dc40f3f1621f08f7f134df1cf8eb2329213d80b85017dd08d9224d6d3095f15`)
- [observation/documented] The enrich tool is off by default and unregistered when disabled, so no network call occurs; when enabled it enforces SSRF protections, rejecting private, loopback, link-local, and unique-local targets including obfuscated numeric forms. -- evidence: [docs/mcp.md#L84-L84](https://github.com/JuliusBrussee/cavemem/blob/166078dd7c463b8e3006da28b2401fb063303f88/docs/mcp.md#L84-L84), [README.md#L146-L146](https://github.com/JuliusBrussee/cavemem/blob/166078dd7c463b8e3006da28b2401fb063303f88/README.md#L146-L146) (`clm_88e327d845e8cf0a9d80c8b1987b52295573e0bbd7f024ed555958ff70fda8a3`)

## evaluation (1 claim(s))

- [observation/documented] An evals/ harness measures compression performance: fixtures verify determinism and technical-token round-trip, and the benchmark corpus requires at least 30% average token reduction (targets of 40% at full and 55% at ultra intensity). -- evidence: [docs/compression.md#L50-L52](https://github.com/JuliusBrussee/cavemem/blob/166078dd7c463b8e3006da28b2401fb063303f88/docs/compression.md#L50-L52), [CLAUDE.md#L33-L48](https://github.com/JuliusBrussee/cavemem/blob/166078dd7c463b8e3006da28b2401fb063303f88/CLAUDE.md#L33-L48) (`clm_bcab83a0d9115abec8ffdc6c784f16baca14f9faa4ad507429688007dac9c093`)

## dependencies (1 claim(s))

- [observation/documented] The npm package cavemem installs globally via npm; the default embedding provider is local (Transformers.js per CLAUDE.md), with ollama and openai as opt-in remote providers. -- evidence: [README.md#L41-L47](https://github.com/JuliusBrussee/cavemem/blob/166078dd7c463b8e3006da28b2401fb063303f88/README.md#L41-L47), [README.md#L165-L178](https://github.com/JuliusBrussee/cavemem/blob/166078dd7c463b8e3006da28b2401fb063303f88/README.md#L165-L178), [README.md#L9-L9](https://github.com/JuliusBrussee/cavemem/blob/166078dd7c463b8e3006da28b2401fb063303f88/README.md#L9-L9), [CLAUDE.md#L13-L21](https://github.com/JuliusBrussee/cavemem/blob/166078dd7c463b8e3006da28b2401fb063303f88/CLAUDE.md#L13-L21) (`clm_351188e71d23d66b0f6244052fa9c8a7e615a26f9a71c7801bdce4688162ab51`)

## limitations (1 claim(s))

- [observation/documented] The project is frozen as of August 2026: no new features or fixes are expected, and development continues in the related caveman repository. -- evidence: [README.md#L15-L20](https://github.com/JuliusBrussee/cavemem/blob/166078dd7c463b8e3006da28b2401fb063303f88/README.md#L15-L20) (`clm_18acbaf207d45397b5f47addc0e5747760c7e681967331a2aa39d8d00550abb7`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

