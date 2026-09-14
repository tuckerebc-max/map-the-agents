---
access: public
aliases: []
claim_ids:
- clm_b37db2c05958b89995ff627e90b4134fdc34bbf3ef42e193febae7a0e5c4e0f6
- clm_dcadf3e9c155c41dfc11e3fc4f6f6ff8dea9e498dc320b2ddde6913ca7f70091
maturity: draft
page_id: pg_fcd3e529a65256449b611c2b7a83f1b1
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_0a2043ae06255e78ade91b262b78c8f4
title: runvendo/vendo/TELEMETRY.md @ 4d149938d7d3
updated_at: '2026-09-14T02:37:55Z'
---

# runvendo/vendo/TELEMETRY.md @ 4d149938d7d3

<!-- rcw:begin owner=source:src_0a2043ae06255e78ade91b262b78c8f4 block=evidence -->
- Telemetry is anonymous and opt-out, build/dev-side only, never firing from a deployed production app; events carry only counts and enums, never source code, paths, prompts, keys, or raw error messages. [@claim:clm_b37db2c05958b89995ff627e90b4134fdc34bbf3ef42e193febae7a0e5c4e0f6]
- Telemetry identity is a random UUID stored in ~/.vendo/telemetry.json, and projectIdHash is a salted one-way SHA-256 of the git origin URL or package name, omitted when neither exists. [@claim:clm_dcadf3e9c155c41dfc11e3fc4f6f6ff8dea9e498dc320b2ddde6913ca7f70091]
<!-- rcw:end owner=source:src_0a2043ae06255e78ade91b262b78c8f4 block=evidence -->

## Researcher notes

