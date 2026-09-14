---
access: public
aliases: []
claim_ids:
- clm_3d14e3506855e00df38745874bb293139acd35244e80b9d9cd799a9989e41e92
- clm_cea5a85715c07cf110ae0802d469ae9def4b93a50072fecbff71061f0a73329d
maturity: draft
page_id: pg_7bc79bf676b1543cbde8a969dcec4c1a
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_ce204fca4bac564f9617609bffd201db
title: sinameraji/kimiflare/CAMOUFLAGE_MIGRATION.md @ efe84a2e65dc
updated_at: '2026-09-14T02:40:52Z'
---

# sinameraji/kimiflare/CAMOUFLAGE_MIGRATION.md @ efe84a2e65dc

<!-- rcw:begin owner=source:src_ce204fca4bac564f9617609bffd201db block=evidence -->
- In Camouflage UI mode, every inbound event is persisted to a SQLite WAL database (~/.config/kimiflare/camouflage-sessions.db), making sessions replayable via a --replay flag. [@claim:clm_3d14e3506855e00df38745874bb293139acd35244e80b9d9cd799a9989e41e92]
- The experimental Camouflage renderer is an external package (camouflage-tui, e.g. 2.1.0-beta.1 as an optionalDependency) whose upstream capabilities gate some features like renderer-side mouse events. [@claim:clm_cea5a85715c07cf110ae0802d469ae9def4b93a50072fecbff71061f0a73329d]
<!-- rcw:end owner=source:src_ce204fca4bac564f9617609bffd201db block=evidence -->

## Researcher notes

