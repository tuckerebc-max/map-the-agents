---
access: public
aliases: []
claim_ids:
- clm_1d70e544fb855bd596e99adaa10cee0d3f13410a4c66313a12f9e4c85ae9751c
- clm_5e521869161dc13625bf816ea26b81e2b6410670ef84525194e245f8f7e542b1
- clm_5e7bbbc3233201d4d77bd5e3239f1cc9b1d0082727047670b460e0537cc7263c
- clm_66e6dab94ec315fc9d5187e5029bd541a3b627779f9d0b8935d4e0fc982b3599
- clm_70aa09977987b4a1a68b582a3197afb777d519a34440cf941365ec6b1c723322
- clm_c26d3d26536a409bfd310cd3182a94f0f34c08e7624d42fc77659bf54073c2e4
- clm_db53d87a4bcbdfedcd0106e608eb2c975a47e4458e2d566e0302fff2d3e4418f
- clm_e33f2a629f100f7d2ba5148153a6ab2ede0842178471e7253b3eb11fa8991ce9
- clm_ee4626da2fc8af0cad27bf5361e019b2f29d487a5c09e00b8936b640bb88ca57
- clm_fa75b0955a3f9dd7497ed68e01f42381b0c65412340385a7cf8c76fb7d0ab8c9
maturity: draft
page_id: pg_b466e92b060359d78e862efdc5210896
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_7212447f2a285dd9a6bbcbc45b2dda6d
title: HaochengLu/contextvc/README.md @ c60e781078d1
updated_at: '2026-09-14T03:56:04Z'
---

# HaochengLu/contextvc/README.md @ c60e781078d1

<!-- rcw:begin owner=source:src_7212447f2a285dd9a6bbcbc45b2dda6d block=evidence -->
- Projection files use managed `ctx:begin`/`ctx:end` blocks; `ctx render` regenerates only managed blocks and preserves human-written text outside them. [@claim:clm_1d70e544fb855bd596e99adaa10cee0d3f13410a4c66313a12f9e4c85ae9751c]
- Knowledge objects are Markdown files with YAML frontmatter (id, type, scope, status, trust, confidence, evidence, bindings) stored under `.context/objects/` in six type directories. [@claim:clm_5e521869161dc13625bf816ea26b81e2b6410670ef84525194e245f8f7e542b1]
- RepeatBench is a benchmark checking that known repeat failures are caught by the gate while safe actions pass; the committed summary reports 1 scenario, 1 gate hit, 0 misses, and 0.0 repeat failure rate, runnable via `ctx repeatbench --json`. [@claim:clm_5e7bbbc3233201d4d77bd5e3239f1cc9b1d0082727047670b460e0537cc7263c]
- `ctx serve-mcp` runs a local stdio MCP server exposing tools: context_brief, context_search, context_precheck, context_log, context_propose, and context_status. [@claim:clm_66e6dab94ec315fc9d5187e5029bd541a3b627779f9d0b8935d4e0fc982b3599]
- Repository development practice: the included GitHub Actions workflow runs cargo fmt check, cargo test, release build, repeatbench, and git diff --check; local development uses the same commands. [@claim:clm_70aa09977987b4a1a68b582a3197afb777d519a34440cf941365ec6b1c723322]
- The tool is written in Rust and installed via cargo; the stable Rust toolchain is required, and installation uses `cargo install --locked` from a tagged GitHub release or source. [@claim:clm_c26d3d26536a409bfd310cd3182a94f0f34c08e7624d42fc77659bf54073c2e4]
- Design principles include Git-native versioning, local-first operation with no API key or hosted service, deterministic gates independent of model output, and human review before runtime learnings become formal objects. [@claim:clm_db53d87a4bcbdfedcd0106e608eb2c975a47e4458e2d566e0302fff2d3e4418f]
- The product exposes a `ctx` CLI with subcommands including init, adopt, render, check, precheck, review, merge, verify, log-event, serve-mcp, and repeatbench. [@claim:clm_e33f2a629f100f7d2ba5148153a6ab2ede0842178471e7253b3eb11fa8991ce9]
- The precheck gate returns warn, ask, or block verdicts before risky actions, based on scope globs, bindings, failure history, stale hints, and snooze events; command matching is token-aware rather than substring-based. [@claim:clm_ee4626da2fc8af0cad27bf5361e019b2f29d487a5c09e00b8936b640bb88ca57]
- ContextVC is described as a Git-native context control plane for AI coding agents, storing rules, decisions, failure memory, how-tos, preferences, and code maps in `.context/`. [@claim:clm_fa75b0955a3f9dd7497ed68e01f42381b0c65412340385a7cf8c76fb7d0ab8c9]
<!-- rcw:end owner=source:src_7212447f2a285dd9a6bbcbc45b2dda6d block=evidence -->

## Researcher notes

