---
access: public
aliases: []
claim_ids:
- clm_68698d2f00d264be4b7298b62bd4d4005fba6438a841674a17cb9afa965c8fc3
- clm_93320c74f21cb81d44c89b1cb83313b63b7278409e5c59b429ee5bd76705c92b
- clm_a2d889e660e5a8c3d6d03fb2de84ebeeb6de7b6bc654467b3225f0b7d0536ae2
- clm_c251b59b2e9868eefd9ac0888864c2634c58d6c866e2c7d0773b5472255c10d3
maturity: draft
page_id: pg_b55d8fc626d95601844239edc5fe0ec3
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_b1ba5a60f15356159224f7475798e335
title: sourcebot-dev/sourcebot/README.md @ c0d0df91a6b9
updated_at: '2026-09-14T04:23:33Z'
---

# sourcebot-dev/sourcebot/README.md @ c0d0df91a6b9

<!-- rcw:begin owner=source:src_b1ba5a60f15356159224f7475798e335 block=evidence -->
- Sourcebot is configured through a JSON config file (with a schema and comment support) that defines connections, which repositories to index, language model providers, and auth providers. [@claim:clm_68698d2f00d264be4b7298b62bd4d4005fba6438a841674a17cb9afa965c8fc3]
- After deployment via docker compose, the product is accessed at http://localhost:3000. [@claim:clm_93320c74f21cb81d44c89b1cb83313b63b7278409e5c59b429ee5bd76705c92b]
- Sourcebot collects anonymous usage data by default; this can be disabled by setting the SOURCEBOT_TELEMETRY_DISABLED environment variable to true. [@claim:clm_a2d889e660e5a8c3d6d03fb2de84ebeeb6de7b6bc654467b3225f0b7d0536ae2]
- Repository development practice: docs previewing uses the Mintlify CLI (npm i -g mintlify, then mintlify dev in the folder containing docs.json), and building Sourcebot from source for contribution is described in CONTRIBUTING.md. [@claim:clm_c251b59b2e9868eefd9ac0888864c2634c58d6c866e2c7d0773b5472255c10d3]
<!-- rcw:end owner=source:src_b1ba5a60f15356159224f7475798e335 block=evidence -->

## Researcher notes

