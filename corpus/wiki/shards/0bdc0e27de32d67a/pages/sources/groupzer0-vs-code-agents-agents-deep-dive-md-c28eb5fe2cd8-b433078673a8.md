---
access: public
aliases: []
claim_ids:
- clm_2ce1f21009b619978b1eddf0fb0832d36923ccddc3b7966336c69d5a5ae89177
- clm_3dcf52e09a293b8a48971a00354ec04249984a3828ce5ba846db54352935535e
- clm_678bd2ab1b9bc91e0548d625a3db570020da99d2200002d7c1043bbf8ffb8f00
- clm_7d0a4d51754cffb43ef8242451bbea844e0f8ee13d0c0263675dd5b84fe91387
- clm_9e4410ad90882b3d6192781296375d23fbf410dc5b0200c8dbaa57a4f53ac63c
- clm_d80b7a6681aa592db734a8270c04c10e9c38de0218351736265dd54ad01d815e
- clm_e18849a789eb2578ecce0e8b4b3f79970a93aedf86f24f3afaca745cf57e63c5
- clm_f535595cd8fc0e62b71d6a72a3d7aff31963dd92152389a291227802bd52296f
maturity: draft
page_id: pg_eb3633d269f65c62ae47b433078673a8
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_908e994eb4a857149d9f66544266cfe8
title: groupzer0/vs-code-agents/AGENTS-DEEP-DIVE.md @ c28eb5fe2cd8
updated_at: '2026-09-14T03:54:59Z'
---

# groupzer0/vs-code-agents/AGENTS-DEEP-DIVE.md @ c28eb5fe2cd8

<!-- rcw:begin owner=source:src_908e994eb4a857149d9f66544266cfe8 block=evidence -->
- Flowbaby exposes agent tools #flowbabyStoreSummary and #flowbabyRetrieveMemory, used with structured JSON payloads carrying query, decisions, rationale, and artifact metadata. [@claim:clm_2ce1f21009b619978b1eddf0fb0832d36923ccddc3b7966336c69d5a5ae89177]
- Quality gates are built in: Critic reviews plans, Code Reviewer gates code before QA and can reject, Security audits at any phase, and DevOps releases only with explicit user approval. [@claim:clm_3dcf52e09a293b8a48971a00354ec04249984a3828ce5ba846db54352935535e]
- All agents load a memory-contract skill governing Flowbaby usage: retrieve before decisions, store at value boundaries (including every 5 turns), use specific hypothesis-driven queries, and acknowledge retrieved memory. [@claim:clm_678bd2ab1b9bc91e0548d625a3db570020da99d2200002d7c1043bbf8ffb8f00]
- Agents carry explicit constraints, e.g. Planner plans without writing code, Implementer follows plans without redesigning, and Security produces findings without implementing remediations. [@claim:clm_7d0a4d51754cffb43ef8242451bbea844e0f8ee13d0c0263675dd5b84fe91387]
- The workflow is document-driven: agents write Markdown artifacts into agent-output/ subfolders (planning, analysis, security, qa, etc.) with sequential NNN naming, status fields, and closure into closed/ subfolders. [@claim:clm_9e4410ad90882b3d6192781296375d23fbf410dc5b0200c8dbaa57a4f53ac63c]
- Flowbaby provides workspace-scoped long-term memory in a local knowledge graph with hybrid graph-vector search; the README states agents fall back to stateless behavior without it. [@claim:clm_d80b7a6681aa592db734a8270c04c10e9c38de0218351736265dd54ad01d815e]
- Agents hand off via a structured template (source agent, artifact path, status, key context, recommended action), and Planner, Implementer, QA, Analyst, and Security document invoking each other as scoped subagents. [@claim:clm_e18849a789eb2578ecce0e8b4b3f79970a93aedf86f24f3afaca745cf57e63c5]
- A typical pipeline runs Roadmap → Planner → Analyst/Architect/Security/Critic → Implementer → Code Reviewer → QA → UAT → DevOps, with documented patterns including an investigation branch and a security gate. [@claim:clm_f535595cd8fc0e62b71d6a72a3d7aff31963dd92152389a291227802bd52296f]
<!-- rcw:end owner=source:src_908e994eb4a857149d9f66544266cfe8 block=evidence -->

## Researcher notes

