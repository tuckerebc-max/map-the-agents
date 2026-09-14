---
access: public
aliases: []
claim_ids:
- clm_86e8f2900261b629e153cd1dde98953fa87e3276d94a1f53b2e2d80915c0a5ee
- clm_8796e11e418c56d54480904700c96f54ff83e4ae1f8771d328fe3dccfdd2f116
maturity: draft
page_id: pg_d189c5003f3e5985ba7489c9c8fa40c0
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_17a4b3dc3e095a57be519fce98198a62
title: andrefetch/postal/docs/approvals.md @ 240622b0c2dc
updated_at: '2026-09-14T01:33:24Z'
---

# andrefetch/postal/docs/approvals.md @ 240622b0c2dc

<!-- rcw:begin owner=source:src_17a4b3dc3e095a57be519fce98198a62 block=evidence -->
- Six approval policies govern mutating actions: on_request (default), auto_edit, auto, on_fail (currently identical to auto), never (read-only), and yolo; read-only tools never prompt. [@claim:clm_86e8f2900261b629e153cd1dde98953fa87e3276d94a1f53b2e2d80915c0a5ee]
- Two rules override any policy except yolo: dangerous commands (e.g. rm -rf /, mkfs, curl piped to bash) are rejected, and anything touching paths outside the working directory requires confirmation (or is rejected under never). [@claim:clm_8796e11e418c56d54480904700c96f54ff83e4ae1f8771d328fe3dccfdd2f116]
<!-- rcw:end owner=source:src_17a4b3dc3e095a57be519fce98198a62 block=evidence -->

## Researcher notes

