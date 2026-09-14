---
access: public
aliases: []
claim_ids:
- clm_0f3694a87625c36771cfceaadfaf1ba3d1713f1d4be7e64722c86df75de43ff9
- clm_22ae115ba65a74d9e0ac789e8cc3cfbdc75330c0ccf98faa010c486d6eb06529
- clm_3184e7b87fbfef61d605b31fe4c05dd591697492696f715f93da57427a2f711e
maturity: draft
page_id: pg_b314eadf370f54e2a4e0dfaed6463c01
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_a58a33b63d115fd888085894e6ba17a5
title: dagger/dagger/RELEASING.md @ 7c35e6274737
updated_at: '2026-09-14T05:10:24Z'
---

# dagger/dagger/RELEASING.md @ 7c35e6274737

<!-- rcw:begin owner=source:src_a58a33b63d115fd888085894e6ba17a5 block=evidence -->
- Repository development practice: pushing a version tag triggers the publish.yml workflow, and patch releases may be cut from release branches with a separate catch-up PR to main. [@claim:clm_0f3694a87625c36771cfceaadfaf1ba3d1713f1d4be7e64722c86df75de43ff9]
- Repository development practice: RELEASING.md says backwards compatibility between mismatched CLI and engine versions is attempted where possible, with minimum versions bumped in engine/version.go when protocol or feature changes require it. [@claim:clm_22ae115ba65a74d9e0ac789e8cc3cfbdc75330c0ccf98faa010c486d6eb06529]
- Repository development practice: RELEASING.md prescribes a release process using changie for release notes, the gh CLI, and a prep PR; internal/version/VERSION is the single source of truth propagated by `dagger generate`. [@claim:clm_3184e7b87fbfef61d605b31fe4c05dd591697492696f715f93da57427a2f711e]
<!-- rcw:end owner=source:src_a58a33b63d115fd888085894e6ba17a5 block=evidence -->

## Researcher notes

