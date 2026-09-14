---
access: public
aliases: []
claim_ids:
- clm_76aaf847bf733c892162aade675cab31d8c0e6edc7873c64ec95b14ee3c8d206
- clm_94152b4b1bee22d28bb277eaf4cc2b6954eeecca1001e294cf3ad36d73464262
maturity: draft
page_id: pg_32d66fcfaeac501682d6131bbf52e1be
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_c9a609665f5a5c32be294059aa11ef70
title: aeonfun/aeon/CHANGELOG.md @ 95142d19705c
updated_at: '2026-09-14T01:29:55Z'
---

# aeonfun/aeon/CHANGELOG.md @ 95142d19705c

<!-- rcw:begin owner=source:src_c9a609665f5a5c32be294059aa11ef70 block=evidence -->
- The ./notify tool writes a structured JSON payload to a queue, and a post-run scripts/notify-deliver.sh is the only place channel tokens are consumed, rendering per channel (Telegram, Discord, Slack, Buzz) with per-send audit lines. [@claim:clm_76aaf847bf733c892162aade675cab31d8c0e6edc7873c64ec95b14ee3c8d206]
- Aeon dispatches to ten coding-agent CLIs via a run-harness contract, including Cursor, Hermes, GLM, and Vercel's fx, with credentials surfaced as dashboard Access Keys rows. [@claim:clm_94152b4b1bee22d28bb277eaf4cc2b6954eeecca1001e294cf3ad36d73464262]
<!-- rcw:end owner=source:src_c9a609665f5a5c32be294059aa11ef70 block=evidence -->

## Researcher notes

