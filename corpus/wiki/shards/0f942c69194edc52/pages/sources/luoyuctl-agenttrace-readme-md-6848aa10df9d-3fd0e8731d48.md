---
access: public
aliases: []
claim_ids:
- clm_1f393ee8300cf185ad5297db015d11aa7258ddf6e968da0bb6ca5657fa923ca3
- clm_78017a72603b060f7411a215370a03a6622c87588c89a66846efcc4ab07d7159
- clm_7df72fada2c196a0008c89b0d59c77b0d113dde7e4ca05b9df7427e924b857b6
- clm_8cca191f05de49aecd28f93acccac33a6070e19e4e6150c1d498c800a62746c8
- clm_9fb13a17b870bafabcf22c747d163185884bd1548f21420c8c240cd4d2cb9c45
- clm_bc12580d644454d6a98bbfbcbf628d52d9824ffe74613d94c60287709a6c890e
- clm_e49ff145f630a73bbf1dc2a4df722fcd7b17a03109148fe1dbdb0d4df94064a6
- clm_f302dfad9b8c653e33a9ddbaa82677024134a73f35fb37e028a1e52c79c793ef
maturity: draft
page_id: pg_cde52303227e57928a3b3fd0e8731d48
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_5f5d952017aa551ab4fbaa83c780fa63
title: luoyuctl/agenttrace/README.md @ 6848aa10df9d
updated_at: '2026-09-14T04:08:28Z'
---

# luoyuctl/agenttrace/README.md @ 6848aa10df9d

<!-- rcw:begin owner=source:src_5f5d952017aa551ab4fbaa83c780fa63 block=evidence -->
- Repository development practice: parser PRs should include a redacted fixture, format detection in crates/agenttrace-core/src/parser.rs, field extraction, and tests; contributors run cargo test, a release build, and --doctor before sending a PR. [@claim:clm_1f393ee8300cf185ad5297db015d11aa7258ddf6e968da0bb6ca5657fa923ca3]
- Each session is labeled Detailed, Aggregate, or Limited so missing event-level evidence is never presented as a complete trace. [@claim:clm_78017a72603b060f7411a215370a03a6622c87588c89a66846efcc4ab07d7159]
- Tool steps retain only timing/status metadata; no prompt, response, result, or tool-argument body is stored in steps. [@claim:clm_7df72fada2c196a0008c89b0d59c77b0d113dde7e4ca05b9df7427e924b857b6]
- A single agenttrace binary provides both interfaces: run without a report action to open the TUI, or pass flags such as --sessions and --overview for CLI output. [@claim:clm_8cca191f05de49aecd28f93acccac33a6070e19e4e6150c1d498c800a62746c8]
- Reports can be emitted as JSON, Markdown, and self-contained HTML; --overview includes scope, parse/pricing confidence, cost audit, recommendations, MCP governance, context trends, and delivery signals. [@claim:clm_9fb13a17b870bafabcf22c747d163185884bd1548f21420c8c240cd4d2cb9c45]
- All cost and delivery fields are explicitly estimates or heuristics, not provider billing or proof that a commit reached main. [@claim:clm_bc12580d644454d6a98bbfbcbf628d52d9824ffe74613d94c60287709a6c890e]
- Pricing overrides via AGENTTRACE_PRICING_FILE accept model aliases plus per-million-token prices for input, output, cache write, and cache read. [@claim:clm_e49ff145f630a73bbf1dc2a4df722fcd7b17a03109148fe1dbdb0d4df94064a6]
- The CLI exposes governance report actions including --audit, --recommend, --mcp-governance, --context-trends, and --delivery-evidence, each shown with --range and -f options. [@claim:clm_f302dfad9b8c653e33a9ddbaa82677024134a73f35fb37e028a1e52c79c793ef]
<!-- rcw:end owner=source:src_5f5d952017aa551ab4fbaa83c780fa63 block=evidence -->

## Researcher notes

