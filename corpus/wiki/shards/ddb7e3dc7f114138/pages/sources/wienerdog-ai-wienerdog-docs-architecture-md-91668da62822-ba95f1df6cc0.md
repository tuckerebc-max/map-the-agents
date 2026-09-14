---
access: public
aliases: []
claim_ids:
- clm_08a95bc13672465450e1af9dc2e2077ece053a298f2d0fee5c4d0bce14218a94
- clm_24633907624715683fc04b6f82804512c790651f2cd5ffc5fd1ed56ad889640a
- clm_3b3c9776c318f3a63ad61fc96b1fb72d05df66813fa51ecd26475d0fd6c13ed3
- clm_5084cbc38fbf325c2c253449fe2129491a83eb5d8564e4e063c78cd081dd5538
- clm_6322c2e1d5d04d702f592aece3185e18c01908b2aaaff66f52f3b9d7ecb1e9a4
- clm_63cca3a57de5d309700d1ff247d0d31033b7b0badf369524eff9c42c4d45ef5f
- clm_688e4420a3e8bdb088dae1abc6c337a7b52584abfc71f3ef5fe3b4b9821638d4
- clm_c4663723fad34d1e0516557f27bb418697a7b97c024ec4a171dd13b92637cbc3
- clm_c4c09b1a3ea3f3c43ac6f9ce5dfc344b2e408628a25ec582ec23212e7c03168c
- clm_c614187fabbc61e893fa280980afd917e6d3a1ee9a3dbc42e0762f77a27e7378
- clm_feed64bc9c0751c31cc18715057ab3dda50d967c176a0cf4e0f4aa767835c7b9
maturity: draft
page_id: pg_ad454a080d4451a4bcb0ba95f1df6cc0
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_006c0cd9cbd35cd98e0ab4656a4191f3
title: wienerdog-ai/wienerdog/docs/ARCHITECTURE.md @ 91668da62822
updated_at: '2026-09-14T04:31:39Z'
---

# wienerdog-ai/wienerdog/docs/ARCHITECTURE.md @ 91668da62822

<!-- rcw:begin owner=source:src_006c0cd9cbd35cd98e0ab4656a4191f3 block=evidence -->
- The dream job (default 03:30 local via run-job dream) scans harness transcripts since per-harness watermarks, redacts secret-looking strings, then runs a dream skill headlessly with tool restrictions: read scratch and vault, write vault only, no Bash, no network. [@claim:clm_08a95bc13672465450e1af9dc2e2077ece053a298f2d0fee5c4d0bce14218a94]
- The architecture targets zero runtime dependencies except googleapis; the gws module is a thin ~600-LOC CLI over googleapis, with MCP, GAM, gcalcli, gmailctl, and the official Rust gws CLI evaluated and rejected for v1. [@claim:clm_24633907624715683fc04b6f82804512c790651f2cd5ffc5fd1ed56ad889640a]
- Vault notes carry mandatory frontmatter provenance fields on every auto-write, including id, type, origin, source_sessions, confidence, recurrence, and a derived_from_untrusted flag. [@claim:clm_3b3c9776c318f3a63ad61fc96b1fb72d05df66813fa51ecd26475d0fd6c13ed3]
- The system map shows a canonical core at ~/.wienerdog/ (config.yaml, skills, prompts, bin, state, secrets, logs, install manifest) plus Claude and Codex adapters that sync compiles into ~/.claude/ and ~/.codex/. [@claim:clm_5084cbc38fbf325c2c253449fe2129491a83eb5d8564e4e063c78cd081dd5538]
- Scheduled jobs use OS-native schedulers (launchd, systemd user timers, Task Scheduler) invoking short-lived run-job processes with watchdog timeout, rotated logging, catch-up, and fail-loud alerting; the design explicitly uses no daemon. [@claim:clm_6322c2e1d5d04d702f592aece3185e18c01908b2aaaff66f52f3b9d7ecb1e9a4]
- Wienerdog never owns the user's CLAUDE.md/AGENTS.md; it manages only a sentinel-delimited block, sync overwrites edits inside sentinels while leaving outside edits untouched, and uninstall removes exactly that region. [@claim:clm_63cca3a57de5d309700d1ff247d0d31033b7b0badf369524eff9c42c4d45ef5f]
- Memory promotion uses tiered quality gates: daily logs need score >= 0.5, atomic notes >= 0.75, and Tier 3 (identity, preferences, skills, digest-fed content) requires score >= 0.85, recurrence across 3+ distinct sessions, and derived_from_untrusted false. [@claim:clm_688e4420a3e8bdb088dae1abc6c337a7b52584abfc71f3ef5fe3b4b9821638d4]
- Outbound gws verbs such as gmail send execute only under a send grant: scoped routine-and-recipient-allowlist entries in config.yaml created only via an interactive typed-confirmation flow; ungranted sends degrade to a draft plus a notice. [@claim:clm_c4663723fad34d1e0516557f27bb418697a7b97c024ec4a171dd13b92637cbc3]
- The wienerdog CLI exposes subcommands install, sync, doctor, dream, schedule, run-job, gws, and uninstall per the architecture system map. [@claim:clm_c4c09b1a3ea3f3c43ac6f9ce5dfc344b2e408628a25ec582ec23212e7c03168c]
- The memory vault defaults to ~/wienerdog/ with PARA-style folders (00-Inbox through 07-Daily, reports, .git); machine state such as watermarks, queue, and score cache lives in ~/.wienerdog/state/, never in the vault. [@claim:clm_c614187fabbc61e893fa280980afd917e6d3a1ee9a3dbc42e0762f77a27e7378]
- The architecture describes the product as a compiler plus prompts, not an application: a thin CLI, short-lived hook scripts, and scheduled jobs whose brain is claude -p or codex exec, targeting under ~4k LOC of plain Node 18+ with no build step. [@claim:clm_feed64bc9c0751c31cc18715057ab3dda50d967c176a0cf4e0f4aa767835c7b9]
<!-- rcw:end owner=source:src_006c0cd9cbd35cd98e0ab4656a4191f3 block=evidence -->

## Researcher notes

