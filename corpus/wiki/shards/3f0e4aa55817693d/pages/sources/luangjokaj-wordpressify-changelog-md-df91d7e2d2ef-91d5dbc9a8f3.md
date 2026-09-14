---
access: public
aliases: []
claim_ids:
- clm_398dbdeb907696681c5fe42f9a941d2b7e79942a8736bffcba7e59f6936e60b4
- clm_54cad9df560a82e52ec55eda90207e0f3230d8b55e174cf543457812dd19a6bd
- clm_81d60215c751a5fef171b8b929b7218da4077ffcbbfe379ce31173947c70359a
- clm_86a965440a8e19cc0b591a9ac34c05b6d625821e65174176018259cb68f1c3cd
- clm_9327d227a8f18ce7996c9f88a6b6adda6004d11dfe17a73662a2d3a093a5ffa0
- clm_bc69155ee6e94bd774b0d13ecdc7d014dfd111f75b6824d4c3ed6f0c05e321d5
maturity: draft
page_id: pg_f4d0ba0d24b752baa73f91d5dbc9a8f3
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_c550ca26f60f5f42b305e06392d8e0b1
title: luangjokaj/wordpressify/CHANGELOG.md @ df91d7e2d2ef
updated_at: '2026-09-14T04:06:58Z'
---

# luangjokaj/wordpressify/CHANGELOG.md @ df91d7e2d2ef

<!-- rcw:begin owner=source:src_c550ca26f60f5f42b305e06392d8e0b1 block=evidence -->
- Since v0.4.0, NodeJS is no longer a global dependency; Docker is the only main dependency, enabling cross-platform runs. [@claim:clm_398dbdeb907696681c5fe42f9a941d2b7e79942a8736bffcba7e59f6936e60b4]
- Export and export:backup scripts auto-stop Docker containers when the stack was not already running, and a healthcheck was added to the WordPress service to fix a chmod race condition. [@claim:clm_54cad9df560a82e52ec55eda90207e0f3230d8b55e174cf543457812dd19a6bd]
- v0.4.0 replaced older npm tasks with commands such as npm run start, npm run export, npm run export:backup, npm run lintcss, and docker compose equivalents. [@claim:clm_81d60215c751a5fef171b8b929b7218da4077ffcbbfe379ce31173947c70359a]
- The default theme was rewritten as a modern block-based theme using HTML markup instead of PHP templates (v0.5.0). [@claim:clm_86a965440a8e19cc0b591a9ac34c05b6d625821e65174176018259cb68f1c3cd]
- The v0.6.3 installer adds an update subcommand that upgrades existing projects without overwriting theme source files. [@claim:clm_9327d227a8f18ce7996c9f88a6b6adda6004d11dfe17a73662a2d3a093a5ffa0]
- v0.6.0 replaced chalk and prompts with native ANSI codes and Node's readline, cutting installer dependencies from over 100 to 18 packages. [@claim:clm_bc69155ee6e94bd774b0d13ecdc7d014dfd111f75b6824d4c3ed6f0c05e321d5]
<!-- rcw:end owner=source:src_c550ca26f60f5f42b305e06392d8e0b1 block=evidence -->

## Researcher notes

