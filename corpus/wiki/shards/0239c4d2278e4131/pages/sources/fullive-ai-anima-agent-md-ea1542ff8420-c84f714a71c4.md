---
access: public
aliases: []
claim_ids:
- clm_247e5c7fedb850fedcfd3756826acdf3774a04afad92b0cd48c6470bd61e3a78
- clm_78b9daea3331e0375dc183432c508859db32ba23556679864b75aa73a34b9cfd
- clm_9f7cebc7de082417d4e66dbf9851a0ded38ceeb64b50e8d3bc6fe47c09d7a1a9
- clm_e0d994ab5624ad8f9917691c96dba6bb59b93eb5e075f052efd887ed929297db
maturity: draft
page_id: pg_3ed8abf924d6571392bac84f714a71c4
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_b387f6512ee75993a72b3b3dcb570c73
title: Fullive-AI/Anima/AGENT.md @ ea1542ff8420
updated_at: '2026-09-14T03:51:44Z'
---

# Fullive-AI/Anima/AGENT.md @ ea1542ff8420

<!-- rcw:begin owner=source:src_b387f6512ee75993a72b3b3dcb570c73 block=evidence -->
- Repository development practice: AGENT.md and ARCHITECTURE_GUARDRAILS.md target coding agents contributing to the repo, defining module ownership boundaries, change heuristics, and testing expectations such as running tests under tests/ before considering work complete. [@claim:clm_247e5c7fedb850fedcfd3756826acdf3774a04afad92b0cd48c6470bd61e3a78]
- Per AGENT.md, MQTT is not the main production event path, the dashboard is polling-based rather than realtime, room modeling is weak, and chat is narrow task routing rather than a full assistant. [@claim:clm_78b9daea3331e0375dc183432c508859db32ba23556679864b75aa73a34b9cfd]
- The runtime comprises a Brain decision layer, device Skills, a layered Memory system, hardware Adapters, a FastAPI backend, and a React dashboard; core/main.py is the composition root and startup entrypoint. [@claim:clm_9f7cebc7de082417d4e66dbf9851a0ded38ceeb64b50e8d3bc6fe47c09d7a1a9]
- Per AGENT.md, the implemented system is a single-process Python backend under core/ with file-based memory in data/memory and a polling-based frontend refresh. [@claim:clm_e0d994ab5624ad8f9917691c96dba6bb59b93eb5e075f052efd887ed929297db]
<!-- rcw:end owner=source:src_b387f6512ee75993a72b3b3dcb570c73 block=evidence -->

## Researcher notes

