# haochenglu/contextvc

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit c60e781078d1 @ 090e0236068cbedc

## Summary (orientation draft, not independently verified)

ContextVC is a Rust CLI (`ctx`) that stores agent memory as Markdown objects in `.context/` and renders them into native files for multiple coding agents, with a deterministic precheck gate, MCP server, hooks, and a RepeatBench benchmark. Evidence is mostly README and design docs describing the shipped product.

## Source coverage

Source coverage (complete): 3 of 3 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 10 facet(s); 3 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] ContextVC is described as a Git-native context control plane for AI coding agents, storing rules, decisions, failure memory, how-tos, preferences, and code maps in `.context/`. -- evidence: [README.md#L5-L5](https://github.com/HaochengLu/contextvc/blob/c60e781078d1028dcb01908ad5719a1288f77ab0/README.md#L5-L5), [README.md#L3-L3](https://github.com/HaochengLu/contextvc/blob/c60e781078d1028dcb01908ad5719a1288f77ab0/README.md#L3-L3)
- components (1 claim(s)):
  - [observation/documented] Knowledge objects are Markdown files with YAML frontmatter (id, type, scope, status, trust, confidence, evidence, bindings) stored under `.context/objects/` in six type directories. -- evidence: [docs/ocl-v0.md#L37-L52](https://github.com/HaochengLu/contextvc/blob/c60e781078d1028dcb01908ad5719a1288f77ab0/docs/ocl-v0.md#L37-L52), [docs/design.md#L37-L44](https://github.com/HaochengLu/contextvc/blob/c60e781078d1028dcb01908ad5719a1288f77ab0/docs/design.md#L37-L44), [docs/ocl-v0.md#L35-L35](https://github.com/HaochengLu/contextvc/blob/c60e781078d1028dcb01908ad5719a1288f77ab0/docs/ocl-v0.md#L35-L35), [docs/design.md#L17-L31](https://github.com/HaochengLu/contextvc/blob/c60e781078d1028dcb01908ad5719a1288f77ab0/docs/design.md#L17-L31), [README.md#L263-L263](https://github.com/HaochengLu/contextvc/blob/c60e781078d1028dcb01908ad5719a1288f77ab0/README.md#L263-L263)
- design-choices (2 claim(s)):
  - [observation/documented] Design principles include Git-native versioning, local-first operation with no API key or hosted service, deterministic gates independent of model output, and human review before runtime learnings become formal objects. -- evidence: [docs/design.md#L7-L13](https://github.com/HaochengLu/contextvc/blob/c60e781078d1028dcb01908ad5719a1288f77ab0/docs/design.md#L7-L13), [docs/design.md#L137-L141](https://github.com/HaochengLu/contextvc/blob/c60e781078d1028dcb01908ad5719a1288f77ab0/docs/design.md#L137-L141), [docs/design.md#L135-L135](https://github.com/HaochengLu/contextvc/blob/c60e781078d1028dcb01908ad5719a1288f77ab0/docs/design.md#L135-L135), [README.md#L74-L78](https://github.com/HaochengLu/contextvc/blob/c60e781078d1028dcb01908ad5719a1288f77ab0/README.md#L74-L78)
  - [observation/documented] Projection files use managed `ctx:begin`/`ctx:end` blocks; `ctx render` regenerates only managed blocks and preserves human-written text outside them. -- evidence: [docs/ocl-v0.md#L88-L89](https://github.com/HaochengLu/contextvc/blob/c60e781078d1028dcb01908ad5719a1288f77ab0/docs/ocl-v0.md#L88-L89), [README.md#L274-L274](https://github.com/HaochengLu/contextvc/blob/c60e781078d1028dcb01908ad5719a1288f77ab0/README.md#L274-L274)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: the included GitHub Actions workflow runs cargo fmt check, cargo test, release build, repeatbench, and git diff --check; local development uses the same commands. -- evidence: [README.md#L287-L293](https://github.com/HaochengLu/contextvc/blob/c60e781078d1028dcb01908ad5719a1288f77ab0/README.md#L287-L293), [README.md#L243-L249](https://github.com/HaochengLu/contextvc/blob/c60e781078d1028dcb01908ad5719a1288f77ab0/README.md#L243-L249), [README.md#L241-L241](https://github.com/HaochengLu/contextvc/blob/c60e781078d1028dcb01908ad5719a1288f77ab0/README.md#L241-L241)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The product exposes a `ctx` CLI with subcommands including init, adopt, render, check, precheck, review, merge, verify, log-event, serve-mcp, and repeatbench. -- evidence: [README.md#L228-L231](https://github.com/HaochengLu/contextvc/blob/c60e781078d1028dcb01908ad5719a1288f77ab0/README.md#L228-L231), [README.md#L99-L118](https://github.com/HaochengLu/contextvc/blob/c60e781078d1028dcb01908ad5719a1288f77ab0/README.md#L99-L118)
  - [observation/documented] `ctx serve-mcp` runs a local stdio MCP server exposing tools: context_brief, context_search, context_precheck, context_log, context_propose, and context_status. -- evidence: [docs/design.md#L81-L86](https://github.com/HaochengLu/contextvc/blob/c60e781078d1028dcb01908ad5719a1288f77ab0/docs/design.md#L81-L86), [docs/design.md#L79-L79](https://github.com/HaochengLu/contextvc/blob/c60e781078d1028dcb01908ad5719a1288f77ab0/docs/design.md#L79-L79), [README.md#L74-L78](https://github.com/HaochengLu/contextvc/blob/c60e781078d1028dcb01908ad5719a1288f77ab0/README.md#L74-L78)
- memory-state (1 claim(s)):
  - [observation/documented] Events are append-only JSONL with secret redaction and git context; proposals are candidate knowledge activated into objects only via `ctx review accept`, with rejects recorded as tombstones to avoid re-distillation. -- evidence: [docs/design.md#L137-L141](https://github.com/HaochengLu/contextvc/blob/c60e781078d1028dcb01908ad5719a1288f77ab0/docs/design.md#L137-L141), [docs/design.md#L48-L48](https://github.com/HaochengLu/contextvc/blob/c60e781078d1028dcb01908ad5719a1288f77ab0/docs/design.md#L48-L48), [docs/design.md#L52-L52](https://github.com/HaochengLu/contextvc/blob/c60e781078d1028dcb01908ad5719a1288f77ab0/docs/design.md#L52-L52)
- orchestration (1 claim(s)):
  - [observation/documented] Generated hook adapters inject a brief at session start, run precheck before tool execution, log failures, distill proposals at stop, and add context before compaction. -- evidence: [docs/design.md#L94-L98](https://github.com/HaochengLu/contextvc/blob/c60e781078d1028dcb01908ad5719a1288f77ab0/docs/design.md#L94-L98), [docs/design.md#L92-L92](https://github.com/HaochengLu/contextvc/blob/c60e781078d1028dcb01908ad5719a1288f77ab0/docs/design.md#L92-L92)
- tools-permissions (1 claim(s)):
  - [observation/documented] The precheck gate returns warn, ask, or block verdicts before risky actions, based on scope globs, bindings, failure history, stale hints, and snooze events; command matching is token-aware rather than substring-based. -- evidence: [docs/design.md#L120-L125](https://github.com/HaochengLu/contextvc/blob/c60e781078d1028dcb01908ad5719a1288f77ab0/docs/design.md#L120-L125), [README.md#L84-L95](https://github.com/HaochengLu/contextvc/blob/c60e781078d1028dcb01908ad5719a1288f77ab0/README.md#L84-L95), [docs/design.md#L127-L127](https://github.com/HaochengLu/contextvc/blob/c60e781078d1028dcb01908ad5719a1288f77ab0/docs/design.md#L127-L127)
More evidence: [full detail](contextvc.detail.md)

Metadata and full claim list: [full detail](contextvc.detail.md)
Human notes ([notes](contextvc.notes.md), never overwritten by build)

[Back to map index](../../index.md)
