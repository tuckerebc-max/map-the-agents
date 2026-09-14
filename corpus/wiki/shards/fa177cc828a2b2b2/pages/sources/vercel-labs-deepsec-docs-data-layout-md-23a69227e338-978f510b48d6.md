---
access: public
aliases: []
claim_ids:
- clm_464516511c0919624e784e1287d95cab321c0ff3b445638529795cef84d4a7c6
- clm_b6bed49895eecebc40b35a02a6ad4fc03946a9346b3a4d1fc1919a1ddbba76ec
- clm_c1cb44e3925745ed552930bc70b4e219fd30ee62dabc58da7de0d9bf2bfb1b0a
maturity: draft
page_id: pg_09b5e53d52bc5e9495a0978f510b48d6
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_3eab186a3a045b25a3505f1bdfd3ed8d
title: vercel-labs/deepsec/docs/data-layout.md @ 23a69227e338
updated_at: '2026-09-14T04:30:26Z'
---

# vercel-labs/deepsec/docs/data-layout.md @ 23a69227e338

<!-- rcw:begin owner=source:src_3eab186a3a045b25a3505f1bdfd3ed8d block=evidence -->
- Each FileRecord tracks candidates, findings, an append-only analysisHistory, gitInfo, a lifecycle status (pending/processing/analyzed/error), and a lockedByRunId field used for atomic file claiming. [@claim:clm_464516511c0919624e784e1287d95cab321c0ff3b445638529795cef84d4a7c6]
- Only the name of the environment variable holding the model key is stored, never the key value itself; setup-state evidence likewise contains no credential values. [@claim:clm_b6bed49895eecebc40b35a02a6ad4fc03946a9346b3a4d1fc1919a1ddbba76ec]
- On-disk state is append-only: re-scans merge new candidates, re-processing appends to analysisHistory and merges findings, and revalidation annotates findings with verdicts without overwriting or deleting anything. [@claim:clm_c1cb44e3925745ed552930bc70b4e219fd30ee62dabc58da7de0d9bf2bfb1b0a]
<!-- rcw:end owner=source:src_3eab186a3a045b25a3505f1bdfd3ed8d block=evidence -->

## Researcher notes

