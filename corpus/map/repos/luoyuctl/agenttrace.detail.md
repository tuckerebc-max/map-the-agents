# luoyuctl/agenttrace -- full detail

[Back to orientation](agenttrace.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/luoyuctl/agenttrace/6848aa10df9dae7034a7bfeaf9f51a7d55424862/786a6feb4df14021.json](../../../wiki/dossiers/luoyuctl/agenttrace/6848aa10df9dae7034a7bfeaf9f51a7d55424862/786a6feb4df14021.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The Rust codebase is split into agenttrace-core (data model, detection, parsers, analysis, pricing, reports, cache, SQLite), agenttrace-cli (clap-based CLI), and agenttrace-tui (ratatui/crossterm). -- evidence: [docs/archive/rust-migration-compatibility-v0.6.md#L64-L66](https://github.com/luoyuctl/agenttrace/blob/6848aa10df9dae7034a7bfeaf9f51a7d55424862/docs/archive/rust-migration-compatibility-v0.6.md#L64-L66) (`clm_119d1915758b44602d53903ba9b17c5ddc3cf83874f2f26abde8f38ad87ce074`)

## design-choices (3 claim(s))

- [observation/documented] The tool is local-first: it reads session logs from chosen paths, computes metrics on the machine, and does not upload prompts, code, logs, reports, or telemetry to any hosted service. -- evidence: [PRIVACY.md#L3-L3](https://github.com/luoyuctl/agenttrace/blob/6848aa10df9dae7034a7bfeaf9f51a7d55424862/PRIVACY.md#L3-L3) (`clm_bb92fd35b762993b69e746e99276ecb81aec79c4b5583565dfc3313b2c6a4fc4`)
- [observation/documented] Each session is labeled Detailed, Aggregate, or Limited so missing event-level evidence is never presented as a complete trace. -- evidence: [README.md#L137-L149](https://github.com/luoyuctl/agenttrace/blob/6848aa10df9dae7034a7bfeaf9f51a7d55424862/README.md#L137-L149), [ROADMAP.md#L34-L40](https://github.com/luoyuctl/agenttrace/blob/6848aa10df9dae7034a7bfeaf9f51a7d55424862/ROADMAP.md#L34-L40) (`clm_78017a72603b060f7411a215370a03a6622c87588c89a66846efcc4ab07d7159`)
- [observation/documented] Tool steps retain only timing/status metadata; no prompt, response, result, or tool-argument body is stored in steps. -- evidence: [README.md#L137-L149](https://github.com/luoyuctl/agenttrace/blob/6848aa10df9dae7034a7bfeaf9f51a7d55424862/README.md#L137-L149), [ROADMAP.md#L34-L40](https://github.com/luoyuctl/agenttrace/blob/6848aa10df9dae7034a7bfeaf9f51a7d55424862/ROADMAP.md#L34-L40) (`clm_7df72fada2c196a0008c89b0d59c77b0d113dde7e4ca05b9df7427e924b857b6`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: parser PRs should include a redacted fixture, format detection in crates/agenttrace-core/src/parser.rs, field extraction, and tests; contributors run cargo test, a release build, and --doctor before sending a PR. -- evidence: [README.md#L175-L175](https://github.com/luoyuctl/agenttrace/blob/6848aa10df9dae7034a7bfeaf9f51a7d55424862/README.md#L175-L175), [README.md#L170-L173](https://github.com/luoyuctl/agenttrace/blob/6848aa10df9dae7034a7bfeaf9f51a7d55424862/README.md#L170-L173), [README.md#L168-L168](https://github.com/luoyuctl/agenttrace/blob/6848aa10df9dae7034a7bfeaf9f51a7d55424862/README.md#L168-L168), [README.md#L177-L181](https://github.com/luoyuctl/agenttrace/blob/6848aa10df9dae7034a7bfeaf9f51a7d55424862/README.md#L177-L181) (`clm_1f393ee8300cf185ad5297db015d11aa7258ddf6e968da0bb6ca5657fa923ca3`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (4 claim(s))

- [observation/documented] A single agenttrace binary provides both interfaces: run without a report action to open the TUI, or pass flags such as --sessions and --overview for CLI output. -- evidence: [README.md#L33-L33](https://github.com/luoyuctl/agenttrace/blob/6848aa10df9dae7034a7bfeaf9f51a7d55424862/README.md#L33-L33) (`clm_8cca191f05de49aecd28f93acccac33a6070e19e4e6150c1d498c800a62746c8`)
- [observation/documented] The CLI exposes governance report actions including --audit, --recommend, --mcp-governance, --context-trends, and --delivery-evidence, each shown with --range and -f options. -- evidence: [README.md#L104-L104](https://github.com/luoyuctl/agenttrace/blob/6848aa10df9dae7034a7bfeaf9f51a7d55424862/README.md#L104-L104), [README.md#L120-L121](https://github.com/luoyuctl/agenttrace/blob/6848aa10df9dae7034a7bfeaf9f51a7d55424862/README.md#L120-L121), [README.md#L110-L110](https://github.com/luoyuctl/agenttrace/blob/6848aa10df9dae7034a7bfeaf9f51a7d55424862/README.md#L110-L110), [README.md#L114-L114](https://github.com/luoyuctl/agenttrace/blob/6848aa10df9dae7034a7bfeaf9f51a7d55424862/README.md#L114-L114), [README.md#L117-L117](https://github.com/luoyuctl/agenttrace/blob/6848aa10df9dae7034a7bfeaf9f51a7d55424862/README.md#L117-L117) (`clm_f302dfad9b8c653e33a9ddbaa82677024134a73f35fb37e028a1e52c79c793ef`)
- [observation/documented] Reports can be emitted as JSON, Markdown, and self-contained HTML; --overview includes scope, parse/pricing confidence, cost audit, recommendations, MCP governance, context trends, and delivery signals. -- evidence: [README.md#L129-L133](https://github.com/luoyuctl/agenttrace/blob/6848aa10df9dae7034a7bfeaf9f51a7d55424862/README.md#L129-L133), [README.md#L137-L149](https://github.com/luoyuctl/agenttrace/blob/6848aa10df9dae7034a7bfeaf9f51a7d55424862/README.md#L137-L149) (`clm_9fb13a17b870bafabcf22c747d163185884bd1548f21420c8c240cd4d2cb9c45`)
- [observation/documented] Pricing overrides via AGENTTRACE_PRICING_FILE accept model aliases plus per-million-token prices for input, output, cache write, and cache read. -- evidence: [README.md#L123-L123](https://github.com/luoyuctl/agenttrace/blob/6848aa10df9dae7034a7bfeaf9f51a7d55424862/README.md#L123-L123), [README.md#L125-L127](https://github.com/luoyuctl/agenttrace/blob/6848aa10df9dae7034a7bfeaf9f51a7d55424862/README.md#L125-L127), [README.md#L107-L107](https://github.com/luoyuctl/agenttrace/blob/6848aa10df9dae7034a7bfeaf9f51a7d55424862/README.md#L107-L107) (`clm_e49ff145f630a73bbf1dc2a4df722fcd7b17a03109148fe1dbdb0d4df94064a6`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The --update-pricing command downloads public model pricing metadata from the LiteLLM community pricing source and does not send local session logs. -- evidence: [PRIVACY.md#L7-L7](https://github.com/luoyuctl/agenttrace/blob/6848aa10df9dae7034a7bfeaf9f51a7d55424862/PRIVACY.md#L7-L7) (`clm_7ffefc1127f33a96e79b2e95b9e9b4a06a7aa83e9a6a69f19a15a7f3a40fa347`)

## limitations (2 claim(s))

- [observation/documented] Stated non-goals include hosted prompt storage, billing-grade invoice reconciliation, replacing agent chat UIs, live tracing during streaming, and security enforcement. -- evidence: [ROADMAP.md#L44-L46](https://github.com/luoyuctl/agenttrace/blob/6848aa10df9dae7034a7bfeaf9f51a7d55424862/ROADMAP.md#L44-L46) (`clm_16c197f31379c6840fdd0fe7c4a5dc5f428179f8d080f90e3d93420c87f1c71c`)
- [observation/documented] All cost and delivery fields are explicitly estimates or heuristics, not provider billing or proof that a commit reached main. -- evidence: [README.md#L129-L133](https://github.com/luoyuctl/agenttrace/blob/6848aa10df9dae7034a7bfeaf9f51a7d55424862/README.md#L129-L133) (`clm_bc12580d644454d6a98bbfbcbf628d52d9824ffe74613d94c60287709a6c890e`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

