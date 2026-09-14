---
access: public
aliases: []
claim_ids:
- clm_19c20ba1c908846385fa0b12122781533e156a23300f497c9bb8a046300a45bf
- clm_566f79842b0096c0e360c3a6e5a49fc17ac9911db93c1d27b585f4916483cb45
- clm_7375a5afe5e3c460771b3fd74b0e571b033b13bcffc2a523fb5097cd4ac5d9db
maturity: draft
page_id: pg_9c93c21222f55f01a16f92da97a3af30
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_fbc4e6918b155fc1ad9b2ebbf18cdfb8
title: patrickdappollonio/dux/CLAUDE.md @ 14e044d616d2
updated_at: '2026-09-14T02:30:06Z'
---

# patrickdappollonio/dux/CLAUDE.md @ 14e044d616d2

<!-- rcw:begin owner=source:src_fbc4e6918b155fc1ad9b2ebbf18cdfb8 block=evidence -->
- Repository development practice: contributors verify changes with cargo fmt, cargo clippy --all-targets --all-features -- -D warnings (a CI gate on every PR), and cargo test, and every change should include unit tests. [@claim:clm_19c20ba1c908846385fa0b12122781533e156a23300f497c9bb8a046300a45bf]
- Repository development practice: the src/app/ TUI is split into focused submodules (mod.rs, input.rs, render.rs, sessions.rs, workers.rs), and changes should stay scoped to the relevant submodule. [@claim:clm_566f79842b0096c0e360c3a6e5a49fc17ac9911db93c1d27b585f4916483cb45]
- Session state persists in sessions.sqlite3 alongside the config, and logs go to dux.log in the config directory with a configurable level and path. [@claim:clm_7375a5afe5e3c460771b3fd74b0e571b033b13bcffc2a523fb5097cd4ac5d9db]
<!-- rcw:end owner=source:src_fbc4e6918b155fc1ad9b2ebbf18cdfb8 block=evidence -->

## Researcher notes

