---
access: public
aliases: []
claim_ids:
- clm_7e6464333ecf12589fc953d9d751453083ee9243650e60a1f3ab0b41c14c0a89
maturity: draft
page_id: pg_2f89243b5dad50df858f884fddf7ea3b
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_c0b0146fd12c539e8c23340f4af53345
title: shoyann/thrush-swe-agent/docs/adr/0003-bundle-mini-swe-agent.md @ daef0a6d6a6d
updated_at: '2026-09-14T02:40:06Z'
---

# shoyann/thrush-swe-agent/docs/adr/0003-bundle-mini-swe-agent.md @ daef0a6d6a6d

<!-- rcw:begin owner=source:src_c0b0146fd12c539e8c23340f4af53345 block=evidence -->
- Auto Mode is backed by a bundled mini-swe-agent checkout in vendor/mini-swe-agent with a non-interactive runner at scripts/mini-auto-run.py; an ADR states the bundled copy should be managed as a Git submodule or clearly tracked vendored dependency. [@claim:clm_7e6464333ecf12589fc953d9d751453083ee9243650e60a1f3ab0b41c14c0a89]
<!-- rcw:end owner=source:src_c0b0146fd12c539e8c23340f4af53345 block=evidence -->

## Researcher notes

