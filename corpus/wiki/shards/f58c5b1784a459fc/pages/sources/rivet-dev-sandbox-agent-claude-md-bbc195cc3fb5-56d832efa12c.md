---
access: public
aliases: []
claim_ids:
- clm_025330e06eb33b0b34663592c480e4a6c7d92c3a35699d0d490c734770ed3cbb
- clm_36c34769412bbc0fed30a69dfaa7fedeb057783af4401c71a9204f7cd1641014
- clm_e5e119691cee36d26dde10fbd579239fa8934c666b117b5ad2c45debfc442e0f
maturity: draft
page_id: pg_de06f1cbbbfb551a8dae56d832efa12c
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_e63aeda93bd55f609ba948651e015917
title: rivet-dev/sandbox-agent/CLAUDE.md @ bbc195cc3fb5
updated_at: '2026-09-14T02:36:10Z'
---

# rivet-dev/sandbox-agent/CLAUDE.md @ bbc195cc3fb5

<!-- rcw:begin owner=source:src_e63aeda93bd55f609ba948651e015917 block=evidence -->
- An experimental OpenCode compatibility layer lets OpenCode CLI, SDK, or web UI connect to control agents through OpenCode tooling; CLAUDE.md references an /opencode/* surface when enabled. [@claim:clm_025330e06eb33b0b34663592c480e4a6c7d92c3a35699d0d490c734770ed3cbb]
- Repository development practice: CLAUDE.md instructs contributors to keep CLI subcommands and HTTP endpoints in sync, update docs/cli.mdx on CLI changes, and regenerate docs/openapi.json when HTTP contracts change. [@claim:clm_36c34769412bbc0fed30a69dfaa7fedeb057783af4401c71a9204f7cd1641014]
- Repository development practice: contributors must keep three files in sync (common-software docs, a Dockerfile, and a Rust test file) and can verify with 'cargo test -p sandbox-agent --test common_software'. [@claim:clm_e5e119691cee36d26dde10fbd579239fa8934c666b117b5ad2c45debfc442e0f]
<!-- rcw:end owner=source:src_e63aeda93bd55f609ba948651e015917 block=evidence -->

## Researcher notes

