---
access: public
aliases: []
claim_ids:
- clm_21575bcd943e015a5692e0b3247855243cf04e1a986d2bda6ed4ea7103614b72
- clm_85dc8b1c6fe8d4e2b05fbfb52921da3814ef25bba8c39ff4dedcc4101760d8b1
maturity: draft
page_id: pg_22b5871a885450de9fe4a426af00f56d
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_c852aafddd21500bbbd91f2264cafb06
title: open-multi-agent/open-multi-agent/docs/adaptive-recovery.md @ eaeb420c4364
updated_at: '2026-09-14T02:26:17Z'
---

# open-multi-agent/open-multi-agent/docs/adaptive-recovery.md @ eaeb420c4364

<!-- rcw:begin owner=source:src_c852aafddd21500bbbd91f2264cafb06 block=evidence -->
- Patch operations are addTasks, retargetPending, and supersedePending; started or terminal tasks cannot be retargeted or superseded, and repairs are forward-only with no undo of external side effects. [@claim:clm_21575bcd943e015a5692e0b3247855243cf04e1a986d2bda6ed4ea7103614b72]
- Adaptive recovery is opt-in via recovery.mode 'repairable': a Replanner or onTaskOutcome callback proposes a PlanPatch, OMA validates it, an optional onPlanPatch gate approves it, and the patch is applied atomically before the triggering task completes. [@claim:clm_85dc8b1c6fe8d4e2b05fbfb52921da3814ef25bba8c39ff4dedcc4101760d8b1]
<!-- rcw:end owner=source:src_c852aafddd21500bbbd91f2264cafb06 block=evidence -->

## Researcher notes

