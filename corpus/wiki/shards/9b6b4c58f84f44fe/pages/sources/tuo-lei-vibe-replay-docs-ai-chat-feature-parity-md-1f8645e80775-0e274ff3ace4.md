---
access: public
aliases: []
claim_ids:
- clm_d29a9a19c3f403e6dbdb850a7db353ec9e33bf75158d4c4daffbe28386069613
- clm_f24a361e3953ef8183d1714ac85a48a3dcc82d45033041cce148e0c60a4d081d
maturity: draft
page_id: pg_68635029fbbe58989ed00e274ff3ace4
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_03f1411c3de55579a7c04ce1bd6c34f1
title: tuo-lei/vibe-replay/docs/ai-chat-feature-parity.md @ 1f8645e80775
updated_at: '2026-09-14T04:27:41Z'
---

# tuo-lei/vibe-replay/docs/ai-chat-feature-parity.md @ 1f8645e80775

<!-- rcw:begin owner=source:src_03f1411c3de55579a7c04ce1bd6c34f1 block=evidence -->
- Ask Replay is documented as a read-only assistant: it can inspect data and navigate the editor but never edits files, publishes, or mutates state; requested mutations are returned to the user as handoff data for review. [@claim:clm_d29a9a19c3f403e6dbdb850a7db353ec9e33bf75158d4c4daffbe28386069613]
- Ask Replay exposes bounded read-only server tools such as search_sessions, get_session_summary, get_session_content, get_scene, get_session_annotations, get_session_overlays, and get_insights with time ranges like 7d/30d/90d/all. [@claim:clm_f24a361e3953ef8183d1714ac85a48a3dcc82d45033041cce148e0c60a4d081d]
<!-- rcw:end owner=source:src_03f1411c3de55579a7c04ce1bd6c34f1 block=evidence -->

## Researcher notes

