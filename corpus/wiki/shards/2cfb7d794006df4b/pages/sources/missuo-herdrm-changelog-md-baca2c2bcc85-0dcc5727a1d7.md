---
access: public
aliases: []
claim_ids:
- clm_2f4c402a8e5c1923d93bf74efbacb495153f337be0f3c7b8de1b19a7117f2df1
- clm_2fff585020710d7406ed760f7c86cc9007800753b22df2a23012ad968405703e
- clm_36b1573bbb5562055b08b47ec95ed140bef84db21623a3eb4a1daec021d3b13f
- clm_669f94fde187ef1bfc843da0287eb170cb4f28f90ac137a3808b729ab4933e44
- clm_6af4d840972683d52c763ad52341452a3af85f677e3d54088169363b1486bad3
- clm_d6368bdbca0fed50f8b2df2b2b17415c11f40750c5b762409516802cb8841933
maturity: draft
page_id: pg_3229fcd6064d57ab99550dcc5727a1d7
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_995910bf91035ed59f4e158c7a110976
title: missuo/herdrm/CHANGELOG.md @ baca2c2bcc85
updated_at: '2026-09-14T02:20:03Z'
---

# missuo/herdrm/CHANGELOG.md @ baca2c2bcc85

<!-- rcw:begin owner=source:src_995910bf91035ed59f4e158c7a110976 block=evidence -->
- Remote pastes stream over SSH into a self-pruning cache with 7-day retention and a 50 MB cap, pasting the remote path into the agent. [@claim:clm_2f4c402a8e5c1923d93bf74efbacb495153f337be0f3c7b8de1b19a7117f2df1]
- Repository development practice: pushing a v* tag triggers release automation that builds, notarizes, Sparkle-signs, and publishes a release, and CI fails if CHANGELOG.md lacks a matching version section. [@claim:clm_2fff585020710d7406ed760f7c86cc9007800753b22df2a23012ad968405703e]
- Tailcat devices pay a roughly 1-2 second tunnel handshake per operation, and standalone shells and the Files workspace still require SSH rather than the tunnel. [@claim:clm_36b1573bbb5562055b08b47ec95ed140bef84db21623a3eb4a1daec021d3b13f]
- A two-pane file manager browses local and SSH files side by side with transfers supporting progress, cancellation, and Replace/Keep Both conflict handling. [@claim:clm_669f94fde187ef1bfc843da0287eb170cb4f28f90ac137a3808b729ab4933e44]
- The embedded terminal renders via libghostty (Metal) rather than SwiftTerm, with herdrm layering light-mode color adaptation, readline chords, and agent-aware paste on top. [@claim:clm_6af4d840972683d52c763ad52341452a3af85f677e3d54088169363b1486bad3]
- On the iOS/iPadOS client, tailcat devices carry herdr's control plane (spaces, agents, prompting) but not a live terminal, which remains SSH-only. [@claim:clm_d6368bdbca0fed50f8b2df2b2b17415c11f40750c5b762409516802cb8841933]
<!-- rcw:end owner=source:src_995910bf91035ed59f4e158c7a110976 block=evidence -->

## Researcher notes

