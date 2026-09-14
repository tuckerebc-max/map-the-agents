---
access: public
aliases: []
claim_ids:
- clm_5855780a08a556bc688828aede3928d6f15a08f883136c5a65ae70a930b743c7
- clm_696ec7009591b47894ea23641fa212728108c394d8591a951cd5577bb9b4d94f
- clm_b0a523d224d1f0301fe4f80e762249ae4fd312b0ead739e6a0823bc6c4748a1e
- clm_d2632504b040d72f23f04e041f855f5477bf8eed918ad7e89a6e6547a53325dd
- clm_ece923b61180a4ba6cddd106e87561664de24b4fde9a97fa055feb261cae51cf
maturity: draft
page_id: pg_8a5d7b58117c5781b67253e9cf5853ac
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_19ebf01509515fb5a05b0f4c1882fdde
title: itwanger/PaiAgent/docs/agent-plan-harness-integration-plan.md @ 05297308189f
updated_at: '2026-09-14T03:59:38Z'
---

# itwanger/PaiAgent/docs/agent-plan-harness-integration-plan.md @ 05297308189f

<!-- rcw:begin owner=source:src_19ebf01509515fb5a05b0f4c1882fdde block=evidence -->
- Repository development practice: the integration plan's test plan calls for backend unit tests (./mvnw test), frontend npm run build verification, and mock-based integration acceptance of a web content production workflow. [@claim:clm_5855780a08a556bc688828aede3928d6f15a08f883136c5a65ae70a930b743c7]
- A plan document proposes memory nodes (memory_write/memory_retrieve) backed by local agent_memory tables and Doubao-embedding-vision embeddings, with workflow/user/global scopes and explicit (not automatic) memory writes. [@claim:clm_696ec7009591b47894ea23641fa212728108c394d8591a951cd5577bb9b4d94f]
- MinIO is listed as an optional object storage dependency; the Agent Plan plan proposes transferring generated images and videos to MinIO to avoid reliance on vendor temporary URLs. [@claim:clm_b0a523d224d1f0301fe4f80e762249ae4fd312b0ead739e6a0823bc6c4748a1e]
- The plan adds a volcengine_agent_plan provider with global config fields for embedding, image, video, and TTS models plus webSearchEnabled and memoryEnabled toggles, normalizing provider aliases like 'ark' and '火山方舟'. [@claim:clm_d2632504b040d72f23f04e041f855f5477bf8eed918ad7e89a6e6547a53325dd]
- The Agent Plan integration plan specifies new node types: web_search/web_fetch, memory_write/memory_retrieve, image_generate/video_generate/vision_analyze, and knowledge_upsert/knowledge_retrieve, also registrable as ReAct Agent tools. [@claim:clm_ece923b61180a4ba6cddd106e87561664de24b4fde9a97fa055feb261cae51cf]
<!-- rcw:end owner=source:src_19ebf01509515fb5a05b0f4c1882fdde block=evidence -->

## Researcher notes

