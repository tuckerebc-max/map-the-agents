---
access: public
aliases: []
claim_ids:
- clm_69af78d568cd66eb1f537fb2a366e29418d664e650884e8f65a376f75006dd9e
- clm_f069076df183e2ab68d9b97fc2917f08965a96a0352ad530fd72183259b7e4b8
- clm_f8648b5e8f4a3a2d7049619d0cfd930f059906763b7b456e9f51caf753cab9ac
maturity: draft
page_id: pg_c950d4bd32fc522a9931fdf7175b677d
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_37b4747e250d5b10b2b4b9569d0a9793
title: MoonshotAI/kimi-cli/docs/en/faq.md @ 86f136422a0a
updated_at: '2026-09-14T04:48:37Z'
---

# MoonshotAI/kimi-cli/docs/en/faq.md @ 86f136422a0a

<!-- rcw:begin owner=source:src_37b4747e250d5b10b2b4b9569d0a9793 block=evidence -->
- Documentation states that if the working directory becomes inaccessible mid-session, Kimi Code CLI detects this, shows a crash report with the session ID and path, exits cleanly, and lets the session be resumed from the correct directory. [@claim:clm_69af78d568cd66eb1f537fb2a366e29418d664e650884e8f65a376f75006dd9e]
- Documentation states a detected newer version shows a blocking update prompt before the shell loads, letting the user upgrade immediately, skip once, or skip and suppress future reminders for that version; this whole update check can be disabled with an environment variable. [@claim:clm_f069076df183e2ab68d9b97fc2917f08965a96a0352ad530fd72183259b7e4b8]
- Documentation states running cd in shell command mode does not change Kimi Code CLI's own working directory, because each shell command runs in an independent subprocess whose directory changes do not persist. [@claim:clm_f8648b5e8f4a3a2d7049619d0cfd930f059906763b7b456e9f51caf753cab9ac]
<!-- rcw:end owner=source:src_37b4747e250d5b10b2b4b9569d0a9793 block=evidence -->

## Researcher notes

