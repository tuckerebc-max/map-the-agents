---
access: public
aliases: []
claim_ids:
- clm_de140b026f067271a1bd6f289483b8df06eeb143283bd457a434d70ef9d8cd3f
- clm_f00e8ae3612d8aa5a1a2b876acebaffb678d3d7555eebab2d1f42f17e721c561
- clm_fe4c06c7a894921ed836f7a3277d0f9fdf2ed5f085856d9589d34abb63afa4ad
maturity: draft
page_id: pg_dc0dd9de4b8e57d093c5e546187c99fc
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_7c6541943b72585ca3b2360a06c7564b
title: urbint/cortex/History.md @ b2897306c6cd
updated_at: '2026-09-14T04:29:07Z'
---

# urbint/cortex/History.md @ b2897306c6cd

<!-- rcw:begin owner=source:src_7c6541943b72585ca3b2360a06c7564b block=evidence -->
- Repository development practice: the project uses CircleCI for CI (badge plus changelog entries about adding CircleCI config and installing inotify-tools in CI), and changelog entries mention Credo and Dialyzer checks. [@claim:clm_de140b026f067271a1bd6f289483b8df06eeb143283bd457a434d70ef9d8cd3f]
- File watching appears to rely on the file_system package, based on a changelog entry stating the file watcher was updated to use the new file_system API. [@claim:clm_f00e8ae3612d8aa5a1a2b876acebaffb678d3d7555eebab2d1f42f17e721c561]
- Version 0.6.0 added file throttling to prevent files being compiled multiple times in quick succession and tests being run multiple times from a single change. [@claim:clm_fe4c06c7a894921ed836f7a3277d0f9fdf2ed5f085856d9589d34abb63afa4ad]
<!-- rcw:end owner=source:src_7c6541943b72585ca3b2360a06c7564b block=evidence -->

## Researcher notes

