---
access: public
aliases: []
claim_ids:
- clm_74652a3b62831b900d747c1d380e7ea37a89a2a8214fd7a361482d0593421807
maturity: draft
page_id: pg_19018a16d46b5459bc0a936174a8b6b1
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_c30d1eaf229a53b0909062233d684a85
title: shoyann/thrush-swe-agent/docs/adr/0004-use-auto-worker.md @ daef0a6d6a6d
updated_at: '2026-09-14T02:40:06Z'
---

# shoyann/thrush-swe-agent/docs/adr/0004-use-auto-worker.md @ daef0a6d6a6d

<!-- rcw:begin owner=source:src_c30d1eaf229a53b0909062233d684a85 block=evidence -->
- A local Auto Worker claims queued runs, manages mini-swe-agent processes, handles cancellation, and writes events and artifacts, keeping long-running jobs separate from request handling. [@claim:clm_74652a3b62831b900d747c1d380e7ea37a89a2a8214fd7a361482d0593421807]
<!-- rcw:end owner=source:src_c30d1eaf229a53b0909062233d684a85 block=evidence -->

## Researcher notes

