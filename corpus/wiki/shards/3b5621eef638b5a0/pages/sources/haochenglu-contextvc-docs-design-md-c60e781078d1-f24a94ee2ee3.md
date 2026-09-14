---
access: public
aliases: []
claim_ids:
- clm_34ac5a4ebbea9767098180f3b5b5d5267d892535fbbe7c4125737889e539af5e
- clm_5e521869161dc13625bf816ea26b81e2b6410670ef84525194e245f8f7e542b1
- clm_5e7bbbc3233201d4d77bd5e3239f1cc9b1d0082727047670b460e0537cc7263c
- clm_66e6dab94ec315fc9d5187e5029bd541a3b627779f9d0b8935d4e0fc982b3599
- clm_b31ce64076e65640909b5a5a3639881a24fa13f41cff33d8d89e5bb119911d53
- clm_db53d87a4bcbdfedcd0106e608eb2c975a47e4458e2d566e0302fff2d3e4418f
- clm_ee4626da2fc8af0cad27bf5361e019b2f29d487a5c09e00b8936b640bb88ca57
maturity: draft
page_id: pg_6c67153fa8ec5dc4a505f24a94ee2ee3
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_6f4388e4333c502fb97b7d23987f329c
title: HaochengLu/contextvc/docs/design.md @ c60e781078d1
updated_at: '2026-09-14T03:56:04Z'
---

# HaochengLu/contextvc/docs/design.md @ c60e781078d1

<!-- rcw:begin owner=source:src_6f4388e4333c502fb97b7d23987f329c block=evidence -->
- Generated hook adapters inject a brief at session start, run precheck before tool execution, log failures, distill proposals at stop, and add context before compaction. [@claim:clm_34ac5a4ebbea9767098180f3b5b5d5267d892535fbbe7c4125737889e539af5e]
- Knowledge objects are Markdown files with YAML frontmatter (id, type, scope, status, trust, confidence, evidence, bindings) stored under `.context/objects/` in six type directories. [@claim:clm_5e521869161dc13625bf816ea26b81e2b6410670ef84525194e245f8f7e542b1]
- RepeatBench is a benchmark checking that known repeat failures are caught by the gate while safe actions pass; the committed summary reports 1 scenario, 1 gate hit, 0 misses, and 0.0 repeat failure rate, runnable via `ctx repeatbench --json`. [@claim:clm_5e7bbbc3233201d4d77bd5e3239f1cc9b1d0082727047670b460e0537cc7263c]
- `ctx serve-mcp` runs a local stdio MCP server exposing tools: context_brief, context_search, context_precheck, context_log, context_propose, and context_status. [@claim:clm_66e6dab94ec315fc9d5187e5029bd541a3b627779f9d0b8935d4e0fc982b3599]
- Events are append-only JSONL with secret redaction and git context; proposals are candidate knowledge activated into objects only via `ctx review accept`, with rejects recorded as tombstones to avoid re-distillation. [@claim:clm_b31ce64076e65640909b5a5a3639881a24fa13f41cff33d8d89e5bb119911d53]
- Design principles include Git-native versioning, local-first operation with no API key or hosted service, deterministic gates independent of model output, and human review before runtime learnings become formal objects. [@claim:clm_db53d87a4bcbdfedcd0106e608eb2c975a47e4458e2d566e0302fff2d3e4418f]
- The precheck gate returns warn, ask, or block verdicts before risky actions, based on scope globs, bindings, failure history, stale hints, and snooze events; command matching is token-aware rather than substring-based. [@claim:clm_ee4626da2fc8af0cad27bf5361e019b2f29d487a5c09e00b8936b640bb88ca57]
<!-- rcw:end owner=source:src_6f4388e4333c502fb97b7d23987f329c block=evidence -->

## Researcher notes

