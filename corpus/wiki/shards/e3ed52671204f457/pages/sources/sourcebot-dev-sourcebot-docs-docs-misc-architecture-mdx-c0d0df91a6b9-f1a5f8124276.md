---
access: public
aliases: []
claim_ids:
- clm_48f97af79ce101c738b634bb6bf4cf59c00ffe056ed237866765fd8cca45eb82
- clm_635fbf9564f50329643ec3cd0a2e82da528441ed8ad4ab924b9d327b263a0a5e
- clm_ba17d2a74b1da070ec8360db1bc4fd0f4148d9f60c613f9e82a33e72cafbf119
- clm_e1e152ff8b87012459d303f8a81c321258a9c8460fcba834bf2c892fe78477d9
maturity: draft
page_id: pg_a845e739fce25ebf8244f1a5f8124276
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_ee14423fd26d57ccb6f5ccebaf40064b
title: sourcebot-dev/sourcebot/docs/docs/misc/architecture.mdx @ c0d0df91a6b9
updated_at: '2026-09-14T04:23:33Z'
---

# sourcebot-dev/sourcebot/docs/docs/misc/architecture.mdx @ c0d0df91a6b9

<!-- rcw:begin owner=source:src_ee14423fd26d57ccb6f5ccebaf40064b block=evidence -->
- The product depends on Zoekt (Sourcegraph's open-source trigram search engine), Postgres, Redis with BullMQ, and supervisord within its container. [@claim:clm_48f97af79ce101c738b634bb6bf4cf59c00ffe056ed237866765fd8cca45eb82]
- The backend worker incrementally syncs with code hosts such as GitHub and GitLab and asynchronously indexes configured repositories; Zoekt is the trigram indexing search engine powering Sourcebot. [@claim:clm_635fbf9564f50329643ec3cd0a2e82da528441ed8ad4ab924b9d327b263a0a5e]
- Sourcebot ships as a single Docker container running multiple services under supervisord, including a Next.js web server, a Node.js backend worker, Zoekt, Postgres, and a Redis job queue used with BullMQ. [@claim:clm_ba17d2a74b1da070ec8360db1bc4fd0f4148d9f60c613f9e82a33e72cafbf119]
- A `.sourcebot/` file-system cache stores persistent data, and managed Redis/Postgres can run outside the container via the REDIS_URL and DATABASE_URL environment variables. [@claim:clm_e1e152ff8b87012459d303f8a81c321258a9c8460fcba834bf2c892fe78477d9]
<!-- rcw:end owner=source:src_ee14423fd26d57ccb6f5ccebaf40064b block=evidence -->

## Researcher notes

