---
access: public
aliases: []
claim_ids:
- clm_28e7e2ff579406ca590719fb772e6a38e10886e2c37e3205bfc4ede6ec77bcd3
- clm_42f4ad5dacb79504f42de84f269a6a34fca034edcf82b5d2820131447546e83b
- clm_59ee74960cb8cd751211cc325a4b2d0d245ea6016a1934228c96e6771de1d39c
maturity: draft
page_id: pg_b6e1e50755905478a5e84a02cadbc2f2
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_d502c9fcc43755b3a8a64eeded33742e
title: jo-inc/pi-reflect/SETUP.md @ 33a72886c8d5
updated_at: '2026-09-14T04:01:14Z'
---

# jo-inc/pi-reflect/SETUP.md @ 33a72886c8d5

<!-- rcw:begin owner=source:src_d502c9fcc43755b3a8a64eeded33742e block=evidence -->
- Repository development practice: SETUP.md is an instruction guide addressed to the coding agent for installing, locating a target file, running a first /reflect, and scheduling daily runs via launchd or cron. [@claim:clm_28e7e2ff579406ca590719fb772e6a38e10886e2c37e3205bfc4ede6ec77bcd3]
- Documented runtime constraints: sessions with fewer than 3 exchanges are not considered substantive, and the target file must be at least 100 bytes; skipped edits are logged with reasons such as ambiguous match or text not found. [@claim:clm_42f4ad5dacb79504f42de84f269a6a34fca034edcf82b5d2820131447546e83b]
- The tool requires pi with an LLM API key configured; each run makes one LLM call, estimated at roughly $0.05–0.15 with Sonnet, and models are specified as provider/model-id strings. [@claim:clm_59ee74960cb8cd751211cc325a4b2d0d245ea6016a1934228c96e6771de1d39c]
<!-- rcw:end owner=source:src_d502c9fcc43755b3a8a64eeded33742e block=evidence -->

## Researcher notes

