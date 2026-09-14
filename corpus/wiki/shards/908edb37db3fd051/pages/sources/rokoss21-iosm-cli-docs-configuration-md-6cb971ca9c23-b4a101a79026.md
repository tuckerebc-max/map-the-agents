---
access: public
aliases: []
claim_ids:
- clm_681652bc83cda90b4f779bd6c102b5f44ae1b049b6f42ecc42ed186913c08dd3
- clm_87cae113a1c3c5204a6909af3016baaaf4afc920614b36a75d5cfc75677876e9
- clm_c1edaa8f67958d6ec4f988e69f8d9fd8b156d9a720a67484bc02df5c1fca6a46
- clm_feda1eb8196f0b2bae19da4afe24bd56939ec1b9d03740ef44cc854177f653fe
maturity: draft
page_id: pg_c58fe52152625070b599b4a101a79026
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_a29e183fd7d4575b8389d2b4a90806a4
title: rokoss21/iosm-cli/docs/configuration.md @ 6cb971ca9c23
updated_at: '2026-09-14T03:12:36Z'
---

# rokoss21/iosm-cli/docs/configuration.md @ 6cb971ca9c23

<!-- rcw:begin owner=source:src_a29e183fd7d4575b8389d2b4a90806a4 block=evidence -->
- Extension tools can declare permission tiers (read-only, workspace-write, danger-full-access); with permissions.extensionToolEnforcement=true, read-only extension tools run automatically in auto mode and tools lacking requiredPermission metadata are blocked there. [@claim:clm_681652bc83cda90b4f779bd6c102b5f44ae1b049b6f42ecc42ed186913c08dd3]
- Settings merge later-wins: global ~/.iosm/agent/settings.json lowest priority, then project .iosm/settings.json, then CLI flags at highest priority. [@claim:clm_87cae113a1c3c5204a6909af3016baaaf4afc920614b36a75d5cfc75677876e9]
- Profiles control behavior and available tools: full grants all built-ins, plan is a read-only bundle, iosm adds IOSM cycle context, and meta is orchestration-first for multi-agent delegation; db_run is enabled only in write-capable profiles (full, meta, iosm). [@claim:clm_c1edaa8f67958d6ec4f988e69f8d9fd8b156d9a720a67484bc02df5c1fca6a46]
- Sessions persist under ~/.iosm/agent/sessions with JSONL trace files in session-traces; semantic search indexes are cached per project hash under ~/.iosm/agent/semantic/indexes containing meta.json, chunks.jsonl, and vectors.jsonl. [@claim:clm_feda1eb8196f0b2bae19da4afe24bd56939ec1b9d03740ef44cc854177f653fe]
<!-- rcw:end owner=source:src_a29e183fd7d4575b8389d2b4a90806a4 block=evidence -->

## Researcher notes

