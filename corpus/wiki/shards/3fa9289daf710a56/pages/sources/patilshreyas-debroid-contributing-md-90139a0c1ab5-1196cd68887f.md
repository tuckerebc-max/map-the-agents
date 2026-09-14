---
access: public
aliases: []
claim_ids:
- clm_9271ae6cd91a98ffb73c4b60cafeec033cdc6413914839cf1a1869f1210356dd
- clm_99542f5b662d255ad217bcd9c6cf245fcd7179b5accf9d3b9aa7efd5258e1e98
maturity: draft
page_id: pg_1632586236285c24ae361196cd68887f
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_6426cfc9c9f35f0b8c4c06672371ac9a
title: PatilShreyas/debroid/CONTRIBUTING.md @ 90139a0c1ab5
updated_at: '2026-09-14T04:15:05Z'
---

# PatilShreyas/debroid/CONTRIBUTING.md @ 90139a0c1ab5

<!-- rcw:begin owner=source:src_6426cfc9c9f35f0b8c4c06672371ac9a block=evidence -->
- Repository development practice: contributors must run ./gradlew detekt test :cli:build for fast verification and ./gradlew build before final commits, and must never use raw println in the CLI layer—only serialized JSON via kotlinx.serialization. [@claim:clm_9271ae6cd91a98ffb73c4b60cafeec033cdc6413914839cf1a1869f1210356dd]
- Repository development practice: CLI JSON response models are guarded by golden schema tests in JsonSchemaGoldenTest; contributors update schemas with ./gradlew test -DupdateGoldenSchemas=true and must keep SKILL.md, README command reference, and CHANGELOG.md in sync with any command or output change. [@claim:clm_99542f5b662d255ad217bcd9c6cf245fcd7179b5accf9d3b9aa7efd5258e1e98]
<!-- rcw:end owner=source:src_6426cfc9c9f35f0b8c4c06672371ac9a block=evidence -->

## Researcher notes

