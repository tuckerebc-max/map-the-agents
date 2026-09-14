---
access: public
aliases: []
claim_ids:
- clm_533c81dd384a202572178406512950b400861323cee51997ca4c6a69a627fce7
- clm_b63bdd1252f44f770530105f49c0abbb4468ec8bede2531f73554ade123d25a2
- clm_cc0ca2b1acb13829948672687f021a4f5a2398436377757e0d766360e323ebc3
maturity: draft
page_id: pg_4a34626b043058229c0e62c897fb4447
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_523a9c1b71a3574b89f93a961d79cb7d
title: ultraworkers/claw-code/README.md @ 08106b0c3771
updated_at: '2026-09-14T03:20:41Z'
---

# ultraworkers/claw-code/README.md @ 08106b0c3771

<!-- rcw:begin owner=source:src_523a9c1b71a3574b89f93a961d79cb7d block=evidence -->
- The harness requires a provider API key (e.g. ANTHROPIC_API_KEY or OPENAI_API_KEY); Claude subscription login is not a supported auth path, and claw-analog selects providers by model and environment variables. [@claim:clm_533c81dd384a202572178406512950b400861323cee51997ca4c6a69a627fce7]
- Repository development practice: the README instructs building from source via `cargo build --workspace` in rust/, warns against `cargo install claw-code` (a deprecated stub), and says to run `cargo test --workspace` after verifying the binary. [@claim:clm_b63bdd1252f44f770530105f49c0abbb4468ec8bede2531f73554ade123d25a2]
- The README states claw-code does not yet ship an ACP/Zed daemon or JSON-RPC entrypoint; `claw acp serve` is only a discoverability alias returning status with exit code 0, with real ACP support tracked in the roadmap. [@claim:clm_cc0ca2b1acb13829948672687f021a4f5a2398436377757e0d766360e323ebc3]
<!-- rcw:end owner=source:src_523a9c1b71a3574b89f93a961d79cb7d block=evidence -->

## Researcher notes

