---
access: public
aliases: []
claim_ids:
- clm_2c98d456627272e3e128f2df6d724ee230d45bbae284c9036c1f36e71276d13d
- clm_3fb7485119e0352cb1f6ee6406d436717ccabe1e2f97fb79f4b3baefd729929e
- clm_db18ff26dbe334f9fd3cdb06e19553e9325018cf2c89471aef795a9702b2cad7
maturity: draft
page_id: pg_ce21c53e7c535c3086129e52c4435962
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_2f5dfa42b3005ce0b474c44c84ed9f6c
title: solo-agent/solo/CHANGELOG.md @ 9d58e66769ed
updated_at: '2026-09-14T02:41:12Z'
---

# solo-agent/solo/CHANGELOG.md @ 9d58e66769ed

<!-- rcw:begin owner=source:src_2f5dfa42b3005ce0b474c44c84ed9f6c block=evidence -->
- Repository development practice: the changelog reports real end-to-end test coverage for workspaces, multi-daemon execution, automations, token accounting, remote uploads, governance, wake coalescing, and runtime capability detection. [@claim:clm_2c98d456627272e3e128f2df6d724ee230d45bbae284c9036c1f36e71276d13d]
- Solo supports remote deployment: the web app, API, PostgreSQL, attachments, and artifacts can run on a remote server while agent runtimes and credentials stay local, with one-time pairing tokens and a `solo` CLI for daemon management. [@claim:clm_3fb7485119e0352cb1f6ee6406d436717ccabe1e2f97fb79f4b3baefd729929e]
- The changelog documents deterministic agent wake-up routing with idempotency, acknowledgements, durable offline recovery, send-time freshness checks, and wake coalescing for busy agents while preserving distinct messages. [@claim:clm_db18ff26dbe334f9fd3cdb06e19553e9325018cf2c89471aef795a9702b2cad7]
<!-- rcw:end owner=source:src_2f5dfa42b3005ce0b474c44c84ed9f6c block=evidence -->

## Researcher notes

