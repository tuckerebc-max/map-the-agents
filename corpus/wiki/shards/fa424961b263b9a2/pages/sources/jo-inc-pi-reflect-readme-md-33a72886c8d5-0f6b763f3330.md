---
access: public
aliases: []
claim_ids:
- clm_4286e5dbb05ae508648e60708481a621fb154404b62193e9bf1b711eda0b97b0
- clm_519cca9eab04a2918c1d6c6249b735d83f59394dc4e7ad4c9ce1f0ad174862c7
- clm_5679f1f801687ba24152b92060c54285863babeb737a4b685412abbfd6a69dc0
- clm_59cd8c99132308fb69a143c65e8df55b7633b23d4f6518f5301d4a7d055a78dd
- clm_59ee74960cb8cd751211cc325a4b2d0d245ea6016a1934228c96e6771de1d39c
- clm_5f6696be287d7d7516ac1b6e4e96e716a9d98b685831bac69a75b56a0665a16d
- clm_a734af846c931536b749636279cbd6b5950be5008c9e46eb41601dee1d4d4e85
- clm_b568b027e7c0c42f5c87b51c19cf3eb0de0cad9b78da654dfde01559551955bb
- clm_d122522e3727471b8d69bbae0879a838ed5e8a5014d0640ff18a4dfb3ac593cb
- clm_eb1d07658535882fa2790a812ca4b999ffafe927de0715dc34f5d12c636d0af8
maturity: draft
page_id: pg_e82af46705a45909afd40f6b763f3330
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_be34794af01652e58dc76e23f38e1cd4
title: jo-inc/pi-reflect/README.md @ 33a72886c8d5
updated_at: '2026-09-14T04:01:14Z'
---

# jo-inc/pi-reflect/README.md @ 33a72886c8d5

<!-- rcw:begin owner=source:src_be34794af01652e58dc76e23f38e1cd4 block=evidence -->
- Data sources support three types (files with glob patterns, shell commands capturing stdout, and HTTP URLs), all with {lookbackDays} interpolation and per-source maxBytes caps; file sources are date-pruned by filename. [@claim:clm_4286e5dbb05ae508648e60708481a621fb154404b62193e9bf1b711eda0b97b0]
- The product exposes slash commands: /reflect (optionally with a file path), /reflect-config, /reflect-history, /reflect-stats, and /reflect-backfill. [@claim:clm_519cca9eab04a2918c1d6c6249b735d83f59394dc4e7ad4c9ce1f0ad174862c7]
- Each run collects evidence from transcripts, daily logs, and reference files, sends evidence plus the target file and a prompt to an LLM, then applies the LLM's proposed edits with safety checks. [@claim:clm_5679f1f801687ba24152b92060c54285863babeb737a4b685412abbfd6a69dc0]
- pi-reflect provides iterative self-improvement for pi coding agents: it reads recent conversations and reference material, compares actual behavior against a defined target, and edits the target file to close the gap. [@claim:clm_59cd8c99132308fb69a143c65e8df55b7633b23d4f6518f5301d4a7d055a78dd]
- The tool requires pi with an LLM API key configured; each run makes one LLM call, estimated at roughly $0.05–0.15 with Sonnet, and models are specified as provider/model-id strings. [@claim:clm_59ee74960cb8cd751211cc325a4b2d0d245ea6016a1934228c96e6771de1d39c]
- Edit safety measures include backing up the original, skipping ambiguous matches, rejecting suspiciously large deletions, and auto-committing to git when the target is in a repository. [@claim:clm_5f6696be287d7d7516ac1b6e4e96e716a9d98b685831bac69a75b56a0665a16d]
- Configuration lives in ~/.pi/agent/reflect.json with a targets array; each target requires a path and model, and supports lookbackDays, maxSessionBytes, transcripts, transcriptSource, context, prompt, and backupDir fields. [@claim:clm_a734af846c931536b749636279cbd6b5950be5008c9e46eb41601dee1d4d4e85]
- Repository development practice: contributors clone the repo, run npm install and npm test (137 tests), and can test locally with pi -e ./extensions/index.ts without installing. [@claim:clm_b568b027e7c0c42f5c87b51c19cf3eb0de0cad9b78da654dfde01559551955bb]
- Targets are any markdown file, e.g. AGENTS.md for behavioral rules, MEMORY.md for long-term memory, or SOUL.md for personality; the prompt determines whether reflect strengthens rules, extracts durable facts, or sharpens identity. [@claim:clm_d122522e3727471b8d69bbae0879a838ed5e8a5014d0640ff18a4dfb3ac593cb]
- /reflect-stats tracks reflection impact via a correction-rate trend (corrections per session over time) and rule recidivism (sections edited repeatedly); /reflect-backfill bootstraps stats from historical sessions in dry-run mode without editing files. [@claim:clm_eb1d07658535882fa2790a812ca4b999ffafe927de0715dc34f5d12c636d0af8]
<!-- rcw:end owner=source:src_be34794af01652e58dc76e23f38e1cd4 block=evidence -->

## Researcher notes

