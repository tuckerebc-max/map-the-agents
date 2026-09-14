---
access: public
aliases: []
claim_ids:
- clm_1d8854f3cfb6b107b191e949ef69ae37637537ac90099409d4f3b1e807311764
- clm_6556f5b9db4e6c95095816dab85a8d96a87549be7e70f98638033981995bdc1f
- clm_c64831fcb52d835985c3ea6dc918cde1504789919dd7175e259a5277700baa1c
maturity: draft
page_id: pg_d251cafb714f5cc9902b9aa3d47852b3
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_b0055e9124f0569ab0075d7395b4b5df
title: sourcegraph/cody-public-snapshot/ARCHITECTURE.md @ 8e20ac6c1460
updated_at: '2026-09-14T02:42:09Z'
---

# sourcegraph/cody-public-snapshot/ARCHITECTURE.md @ 8e20ac6c1460

<!-- rcw:begin owner=source:src_b0055e9124f0569ab0075d7395b4b5df block=evidence -->
- Repository development practice: telemetry rules require transcript data to go only in privateMetadata with a recordsPrivateMetadataTranscript flag, and only for DotCom (Free) users. [@claim:clm_1d8854f3cfb6b107b191e949ef69ae37637537ac90099409d4f3b1e807311764]
- Repository development practice: token-counting guidance says to express limits in tokens, apply limits after model selection, and count tokens after appending strings when possible. [@claim:clm_6556f5b9db4e6c95095816dab85a8d96a87549be7e70f98638033981995bdc1f]
- Repository development practice: ARCHITECTURE.md gives async-pattern guidance—Promises for single async results, Observables for changing values, and generators for demand-driven multiple values. [@claim:clm_c64831fcb52d835985c3ea6dc918cde1504789919dd7175e259a5277700baa1c]
<!-- rcw:end owner=source:src_b0055e9124f0569ab0075d7395b4b5df block=evidence -->

## Researcher notes

