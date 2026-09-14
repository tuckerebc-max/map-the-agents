# haochenglu/contextvc -- full detail

[Back to orientation](contextvc.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/haochenglu/contextvc/c60e781078d1028dcb01908ad5719a1288f77ab0/090e0236068cbedc.json](../../../wiki/dossiers/haochenglu/contextvc/c60e781078d1028dcb01908ad5719a1288f77ab0/090e0236068cbedc.json)

## specifications (1 claim(s))

- [observation/documented] ContextVC is described as a Git-native context control plane for AI coding agents, storing rules, decisions, failure memory, how-tos, preferences, and code maps in `.context/`. -- evidence: [README.md#L5-L5](https://github.com/HaochengLu/contextvc/blob/c60e781078d1028dcb01908ad5719a1288f77ab0/README.md#L5-L5), [README.md#L3-L3](https://github.com/HaochengLu/contextvc/blob/c60e781078d1028dcb01908ad5719a1288f77ab0/README.md#L3-L3) (`clm_fa75b0955a3f9dd7497ed68e01f42381b0c65412340385a7cf8c76fb7d0ab8c9`)

## components (1 claim(s))

- [observation/documented] Knowledge objects are Markdown files with YAML frontmatter (id, type, scope, status, trust, confidence, evidence, bindings) stored under `.context/objects/` in six type directories. -- evidence: [docs/ocl-v0.md#L37-L52](https://github.com/HaochengLu/contextvc/blob/c60e781078d1028dcb01908ad5719a1288f77ab0/docs/ocl-v0.md#L37-L52), [docs/design.md#L37-L44](https://github.com/HaochengLu/contextvc/blob/c60e781078d1028dcb01908ad5719a1288f77ab0/docs/design.md#L37-L44), [docs/ocl-v0.md#L35-L35](https://github.com/HaochengLu/contextvc/blob/c60e781078d1028dcb01908ad5719a1288f77ab0/docs/ocl-v0.md#L35-L35), [docs/design.md#L17-L31](https://github.com/HaochengLu/contextvc/blob/c60e781078d1028dcb01908ad5719a1288f77ab0/docs/design.md#L17-L31), [README.md#L263-L263](https://github.com/HaochengLu/contextvc/blob/c60e781078d1028dcb01908ad5719a1288f77ab0/README.md#L263-L263) (`clm_5e521869161dc13625bf816ea26b81e2b6410670ef84525194e245f8f7e542b1`)

## design-choices (2 claim(s))

- [observation/documented] Design principles include Git-native versioning, local-first operation with no API key or hosted service, deterministic gates independent of model output, and human review before runtime learnings become formal objects. -- evidence: [docs/design.md#L7-L13](https://github.com/HaochengLu/contextvc/blob/c60e781078d1028dcb01908ad5719a1288f77ab0/docs/design.md#L7-L13), [docs/design.md#L137-L141](https://github.com/HaochengLu/contextvc/blob/c60e781078d1028dcb01908ad5719a1288f77ab0/docs/design.md#L137-L141), [docs/design.md#L135-L135](https://github.com/HaochengLu/contextvc/blob/c60e781078d1028dcb01908ad5719a1288f77ab0/docs/design.md#L135-L135), [README.md#L74-L78](https://github.com/HaochengLu/contextvc/blob/c60e781078d1028dcb01908ad5719a1288f77ab0/README.md#L74-L78) (`clm_db53d87a4bcbdfedcd0106e608eb2c975a47e4458e2d566e0302fff2d3e4418f`)
- [observation/documented] Projection files use managed `ctx:begin`/`ctx:end` blocks; `ctx render` regenerates only managed blocks and preserves human-written text outside them. -- evidence: [docs/ocl-v0.md#L88-L89](https://github.com/HaochengLu/contextvc/blob/c60e781078d1028dcb01908ad5719a1288f77ab0/docs/ocl-v0.md#L88-L89), [README.md#L274-L274](https://github.com/HaochengLu/contextvc/blob/c60e781078d1028dcb01908ad5719a1288f77ab0/README.md#L274-L274) (`clm_1d70e544fb855bd596e99adaa10cee0d3f13410a4c66313a12f9e4c85ae9751c`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: the included GitHub Actions workflow runs cargo fmt check, cargo test, release build, repeatbench, and git diff --check; local development uses the same commands. -- evidence: [README.md#L287-L293](https://github.com/HaochengLu/contextvc/blob/c60e781078d1028dcb01908ad5719a1288f77ab0/README.md#L287-L293), [README.md#L243-L249](https://github.com/HaochengLu/contextvc/blob/c60e781078d1028dcb01908ad5719a1288f77ab0/README.md#L243-L249), [README.md#L241-L241](https://github.com/HaochengLu/contextvc/blob/c60e781078d1028dcb01908ad5719a1288f77ab0/README.md#L241-L241) (`clm_70aa09977987b4a1a68b582a3197afb777d519a34440cf941365ec6b1c723322`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The product exposes a `ctx` CLI with subcommands including init, adopt, render, check, precheck, review, merge, verify, log-event, serve-mcp, and repeatbench. -- evidence: [README.md#L228-L231](https://github.com/HaochengLu/contextvc/blob/c60e781078d1028dcb01908ad5719a1288f77ab0/README.md#L228-L231), [README.md#L99-L118](https://github.com/HaochengLu/contextvc/blob/c60e781078d1028dcb01908ad5719a1288f77ab0/README.md#L99-L118) (`clm_e33f2a629f100f7d2ba5148153a6ab2ede0842178471e7253b3eb11fa8991ce9`)
- [observation/documented] `ctx serve-mcp` runs a local stdio MCP server exposing tools: context_brief, context_search, context_precheck, context_log, context_propose, and context_status. -- evidence: [docs/design.md#L81-L86](https://github.com/HaochengLu/contextvc/blob/c60e781078d1028dcb01908ad5719a1288f77ab0/docs/design.md#L81-L86), [docs/design.md#L79-L79](https://github.com/HaochengLu/contextvc/blob/c60e781078d1028dcb01908ad5719a1288f77ab0/docs/design.md#L79-L79), [README.md#L74-L78](https://github.com/HaochengLu/contextvc/blob/c60e781078d1028dcb01908ad5719a1288f77ab0/README.md#L74-L78) (`clm_66e6dab94ec315fc9d5187e5029bd541a3b627779f9d0b8935d4e0fc982b3599`)

## memory-state (1 claim(s))

- [observation/documented] Events are append-only JSONL with secret redaction and git context; proposals are candidate knowledge activated into objects only via `ctx review accept`, with rejects recorded as tombstones to avoid re-distillation. -- evidence: [docs/design.md#L137-L141](https://github.com/HaochengLu/contextvc/blob/c60e781078d1028dcb01908ad5719a1288f77ab0/docs/design.md#L137-L141), [docs/design.md#L48-L48](https://github.com/HaochengLu/contextvc/blob/c60e781078d1028dcb01908ad5719a1288f77ab0/docs/design.md#L48-L48), [docs/design.md#L52-L52](https://github.com/HaochengLu/contextvc/blob/c60e781078d1028dcb01908ad5719a1288f77ab0/docs/design.md#L52-L52) (`clm_b31ce64076e65640909b5a5a3639881a24fa13f41cff33d8d89e5bb119911d53`)

## orchestration (1 claim(s))

- [observation/documented] Generated hook adapters inject a brief at session start, run precheck before tool execution, log failures, distill proposals at stop, and add context before compaction. -- evidence: [docs/design.md#L94-L98](https://github.com/HaochengLu/contextvc/blob/c60e781078d1028dcb01908ad5719a1288f77ab0/docs/design.md#L94-L98), [docs/design.md#L92-L92](https://github.com/HaochengLu/contextvc/blob/c60e781078d1028dcb01908ad5719a1288f77ab0/docs/design.md#L92-L92) (`clm_34ac5a4ebbea9767098180f3b5b5d5267d892535fbbe7c4125737889e539af5e`)

## tools-permissions (1 claim(s))

- [observation/documented] The precheck gate returns warn, ask, or block verdicts before risky actions, based on scope globs, bindings, failure history, stale hints, and snooze events; command matching is token-aware rather than substring-based. -- evidence: [docs/design.md#L120-L125](https://github.com/HaochengLu/contextvc/blob/c60e781078d1028dcb01908ad5719a1288f77ab0/docs/design.md#L120-L125), [README.md#L84-L95](https://github.com/HaochengLu/contextvc/blob/c60e781078d1028dcb01908ad5719a1288f77ab0/README.md#L84-L95), [docs/design.md#L127-L127](https://github.com/HaochengLu/contextvc/blob/c60e781078d1028dcb01908ad5719a1288f77ab0/docs/design.md#L127-L127) (`clm_ee4626da2fc8af0cad27bf5361e019b2f29d487a5c09e00b8936b640bb88ca57`)

## evaluation (1 claim(s))

- [observation/documented] RepeatBench is a benchmark checking that known repeat failures are caught by the gate while safe actions pass; the committed summary reports 1 scenario, 1 gate hit, 0 misses, and 0.0 repeat failure rate, runnable via `ctx repeatbench --json`. -- evidence: [README.md#L211-L211](https://github.com/HaochengLu/contextvc/blob/c60e781078d1028dcb01908ad5719a1288f77ab0/README.md#L211-L211), [docs/design.md#L176-L176](https://github.com/HaochengLu/contextvc/blob/c60e781078d1028dcb01908ad5719a1288f77ab0/docs/design.md#L176-L176), [README.md#L215-L222](https://github.com/HaochengLu/contextvc/blob/c60e781078d1028dcb01908ad5719a1288f77ab0/README.md#L215-L222), [README.md#L228-L231](https://github.com/HaochengLu/contextvc/blob/c60e781078d1028dcb01908ad5719a1288f77ab0/README.md#L228-L231) (`clm_5e7bbbc3233201d4d77bd5e3239f1cc9b1d0082727047670b460e0537cc7263c`)

## dependencies (1 claim(s))

- [observation/documented] The tool is written in Rust and installed via cargo; the stable Rust toolchain is required, and installation uses `cargo install --locked` from a tagged GitHub release or source. -- evidence: [README.md#L38-L43](https://github.com/HaochengLu/contextvc/blob/c60e781078d1028dcb01908ad5719a1288f77ab0/README.md#L38-L43), [README.md#L45-L45](https://github.com/HaochengLu/contextvc/blob/c60e781078d1028dcb01908ad5719a1288f77ab0/README.md#L45-L45), [README.md#L31-L34](https://github.com/HaochengLu/contextvc/blob/c60e781078d1028dcb01908ad5719a1288f77ab0/README.md#L31-L34) (`clm_c26d3d26536a409bfd310cd3182a94f0f34c08e7624d42fc77659bf54073c2e4`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

