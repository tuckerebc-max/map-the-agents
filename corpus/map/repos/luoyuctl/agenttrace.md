# luoyuctl/agenttrace

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 6848aa10df9d @ 786a6feb4df14021

## Summary (orientation draft, not independently verified)

AgentTrace is a local-first Rust CLI/TUI tool that parses AI coding-agent session logs to report cost, token, and time usage and diagnose slow or regressed runs, emitting JSON/Markdown/HTML reports. Evidence is documentation-only (README, PRIVACY, ROADMAP, archived migration docs); no runtime source code is included in the slices.

## Source coverage

Source coverage (partial): 6 of 21 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The Rust codebase is split into agenttrace-core (data model, detection, parsers, analysis, pricing, reports, cache, SQLite), agenttrace-cli (clap-based CLI), and agenttrace-tui (ratatui/crossterm). -- evidence: [docs/archive/rust-migration-compatibility-v0.6.md#L64-L66](https://github.com/luoyuctl/agenttrace/blob/6848aa10df9dae7034a7bfeaf9f51a7d55424862/docs/archive/rust-migration-compatibility-v0.6.md#L64-L66)
- design-choices (3 claim(s)):
  - [observation/documented] The tool is local-first: it reads session logs from chosen paths, computes metrics on the machine, and does not upload prompts, code, logs, reports, or telemetry to any hosted service. -- evidence: [PRIVACY.md#L3-L3](https://github.com/luoyuctl/agenttrace/blob/6848aa10df9dae7034a7bfeaf9f51a7d55424862/PRIVACY.md#L3-L3)
  - [observation/documented] Each session is labeled Detailed, Aggregate, or Limited so missing event-level evidence is never presented as a complete trace. -- evidence: [README.md#L137-L149](https://github.com/luoyuctl/agenttrace/blob/6848aa10df9dae7034a7bfeaf9f51a7d55424862/README.md#L137-L149), [ROADMAP.md#L34-L40](https://github.com/luoyuctl/agenttrace/blob/6848aa10df9dae7034a7bfeaf9f51a7d55424862/ROADMAP.md#L34-L40)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: parser PRs should include a redacted fixture, format detection in crates/agenttrace-core/src/parser.rs, field extraction, and tests; contributors run cargo test, a release build, and --doctor before sending a PR. -- evidence: [README.md#L175-L175](https://github.com/luoyuctl/agenttrace/blob/6848aa10df9dae7034a7bfeaf9f51a7d55424862/README.md#L175-L175), [README.md#L170-L173](https://github.com/luoyuctl/agenttrace/blob/6848aa10df9dae7034a7bfeaf9f51a7d55424862/README.md#L170-L173), [README.md#L168-L168](https://github.com/luoyuctl/agenttrace/blob/6848aa10df9dae7034a7bfeaf9f51a7d55424862/README.md#L168-L168), [README.md#L177-L181](https://github.com/luoyuctl/agenttrace/blob/6848aa10df9dae7034a7bfeaf9f51a7d55424862/README.md#L177-L181)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (4 claim(s)):
  - [observation/documented] A single agenttrace binary provides both interfaces: run without a report action to open the TUI, or pass flags such as --sessions and --overview for CLI output. -- evidence: [README.md#L33-L33](https://github.com/luoyuctl/agenttrace/blob/6848aa10df9dae7034a7bfeaf9f51a7d55424862/README.md#L33-L33)
  - [observation/documented] The CLI exposes governance report actions including --audit, --recommend, --mcp-governance, --context-trends, and --delivery-evidence, each shown with --range and -f options. -- evidence: [README.md#L104-L104](https://github.com/luoyuctl/agenttrace/blob/6848aa10df9dae7034a7bfeaf9f51a7d55424862/README.md#L104-L104), [README.md#L120-L121](https://github.com/luoyuctl/agenttrace/blob/6848aa10df9dae7034a7bfeaf9f51a7d55424862/README.md#L120-L121), [README.md#L110-L110](https://github.com/luoyuctl/agenttrace/blob/6848aa10df9dae7034a7bfeaf9f51a7d55424862/README.md#L110-L110), [README.md#L114-L114](https://github.com/luoyuctl/agenttrace/blob/6848aa10df9dae7034a7bfeaf9f51a7d55424862/README.md#L114-L114), [README.md#L117-L117](https://github.com/luoyuctl/agenttrace/blob/6848aa10df9dae7034a7bfeaf9f51a7d55424862/README.md#L117-L117)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] The --update-pricing command downloads public model pricing metadata from the LiteLLM community pricing source and does not send local session logs. -- evidence: [PRIVACY.md#L7-L7](https://github.com/luoyuctl/agenttrace/blob/6848aa10df9dae7034a7bfeaf9f51a7d55424862/PRIVACY.md#L7-L7)
- limitations (2 claim(s)):
  - [observation/documented] Stated non-goals include hosted prompt storage, billing-grade invoice reconciliation, replacing agent chat UIs, live tracing during streaming, and security enforcement. -- evidence: [ROADMAP.md#L44-L46](https://github.com/luoyuctl/agenttrace/blob/6848aa10df9dae7034a7bfeaf9f51a7d55424862/ROADMAP.md#L44-L46)
  - [observation/documented] All cost and delivery fields are explicitly estimates or heuristics, not provider billing or proof that a commit reached main. -- evidence: [README.md#L129-L133](https://github.com/luoyuctl/agenttrace/blob/6848aa10df9dae7034a7bfeaf9f51a7d55424862/README.md#L129-L133)
- relevance: unknown (no source-linked claim submitted for this facet)
More evidence: [full detail](agenttrace.detail.md)

Metadata and full claim list: [full detail](agenttrace.detail.md)
Human notes ([notes](agenttrace.notes.md), never overwritten by build)

[Back to map index](../../index.md)
