---
access: public
aliases: []
claim_ids:
- clm_44b21d610b4018b6fae8bddca5dd0133d207f337af491549d90b463683bc0987
- clm_7cd739cb3940f7caa6e602600f903871cc4e0e8d575b893474173211fe41fdc2
maturity: draft
page_id: pg_5efeb15dc96452fba504f81a5ad179fa
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_af4b9237e0ad510db44ff75978805333
title: truefoundry/trueforge/docs/ui-sdk/concepts/architecture.mdx @ 4bf9ce063019
updated_at: '2026-09-14T03:19:56Z'
---

# truefoundry/trueforge/docs/ui-sdk/concepts/architecture.mdx @ 4bf9ce063019

<!-- rcw:begin owner=source:src_af4b9237e0ad510db44ff75978805333 block=evidence -->
- The UI SDK offers three levels of control: using the TrueForgeUI component directly, supplying a custom layout, or mounting providers manually; it exports runtime-connected containers (ThreadContainer, ComposerContainer, ThreadListContainer) and presentational atoms replaceable via an overrides mechanism. [@claim:clm_44b21d610b4018b6fae8bddca5dd0133d207f337af491549d90b463683bc0987]
- The UI SDK exposes stable styling hooks (.aui-root, .aui-markdown, .aui-monaco, data-slot attributes), though some slot values like avatar and tool-call-card lack the aui_ prefix, so users should inspect elements rather than assume the prefix. [@claim:clm_7cd739cb3940f7caa6e602600f903871cc4e0e8d575b893474173211fe41fdc2]
<!-- rcw:end owner=source:src_af4b9237e0ad510db44ff75978805333 block=evidence -->

## Researcher notes

