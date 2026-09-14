---
access: public
aliases: []
claim_ids:
- clm_173014819b1af3b4b441868ee2098845bf5b367c8e77a8cb4d24a31d65b0f2f6
- clm_1b27170cff80c1d0ab3195277abc8e6a772ee1e06f9ab06cdc70a865c8064b81
- clm_3681a4756ba766be2a278fad254b29188671aa3945b873d82a9ea4cc5bd01575
- clm_97400cbe362db73191667eb7250e8c6c723d8c7fa3dcab69c865899f447cd763
maturity: draft
page_id: pg_6396e1034e5a570d9f34ed76a7d8f904
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_51665feb7651590dad68b90b8932db8d
title: maxktz/hitch/README.md @ bcbfca260225
updated_at: '2026-09-14T04:09:11Z'
---

# maxktz/hitch/README.md @ bcbfca260225

<!-- rcw:begin owner=source:src_51665feb7651590dad68b90b8932db8d block=evidence -->
- Installation is via `npm install -g hitch-cli`; supported platforms are macOS and Linux on arm64 or x64. [@claim:clm_173014819b1af3b4b441868ee2098845bf5b367c8e77a8cb4d24a31d65b0f2f6]
- Hitch is not a terminal multiplexer UI like tmux; the terminal feels like a normal shell while Hitch proxies input/output, records context, and exposes agent-friendly commands. [@claim:clm_1b27170cff80c1d0ab3195277abc8e6a772ee1e06f9ab06cdc70a865c8064b81]
- Hitch is a CLI for sharing the user's real terminal with AI coding agents; running `hitch` gives agents terminal context, ability to send keys or commands, and inspect output. [@claim:clm_3681a4756ba766be2a278fad254b29188671aa3945b873d82a9ea4cc5bd01575]
- Human-facing usage is minimal: `hitch` starts sharing and `unhitch` or `hitch off` stops it; remaining commands are built for agents. [@claim:clm_97400cbe362db73191667eb7250e8c6c723d8c7fa3dcab69c865899f447cd763]
<!-- rcw:end owner=source:src_51665feb7651590dad68b90b8932db8d block=evidence -->

## Researcher notes

