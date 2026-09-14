---
access: public
aliases: []
claim_ids:
- clm_0347fc06cd25320cbcfff0e1a47b120b65f0d1a7e260f64fb9b4fcf72826693d
- clm_2983288e6f8844552e4040f302925ec47a6bce3b5b90f6dbaf1b4984126eee0c
- clm_3e682aabc706c0737272b81f88722d17e5bd166111b55b7246566d6e4cca40fc
- clm_7451d006a5619d5533b960dffee79cf6d97616c0c27a6a6636d9e3ebe58f24ab
maturity: draft
page_id: pg_3026c2c5856750be9cf21d6cd7725b71
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_5dd42030269053d5a055ea365763dfca
title: aws/amazon-q-developer-cli/README.md @ 15cc8f3cd18c
updated_at: '2026-09-14T01:59:48Z'
---

# aws/amazon-q-developer-cli/README.md @ 15cc8f3cd18c

<!-- rcw:begin owner=source:src_5dd42030269053d5a055ea365763dfca block=evidence -->
- The main component is the chat_cli crate, the `q` CLI for interfacing with Amazon Q Developer from the command line; the repo also contains crates, scripts, and docs directories. [@claim:clm_0347fc06cd25320cbcfff0e1a47b120b65f0d1a7e260f64fb9b4fcf72826693d]
- The README states this open-source project is no longer actively maintained and will only receive critical security fixes; Amazon Q Developer CLI continues as the closed-source Kiro CLI. [@claim:clm_2983288e6f8844552e4040f302925ec47a6bce3b5b90f6dbaf1b4984126eee0c]
- Repository development practice: contributors need macOS with Xcode 13+ and Brew, install the Rust toolchain via rustup (stable plus nightly) and typos-cli, then build with cargo run --bin chat_cli, test with cargo test, lint with cargo clippy, and format with cargo +nightly fmt. [@claim:clm_3e682aabc706c0737272b81f88722d17e5bd166111b55b7246566d6e4cca40fc]
- The project is written in Rust; contributor setup instructions require installing the Rust toolchain via rustup with stable as default plus the nightly toolchain. [@claim:clm_7451d006a5619d5533b960dffee79cf6d97616c0c27a6a6636d9e3ebe58f24ab]
<!-- rcw:end owner=source:src_5dd42030269053d5a055ea365763dfca block=evidence -->

## Researcher notes

