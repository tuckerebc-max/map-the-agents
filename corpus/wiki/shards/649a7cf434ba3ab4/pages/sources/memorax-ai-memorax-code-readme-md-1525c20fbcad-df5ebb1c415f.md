---
access: public
aliases: []
claim_ids:
- clm_00ef1fa849729e7a115af31d85fd43cd1fb0031427e120f1f4efca65a9467d02
- clm_240adc51d6340123da53373e82062821f0b3eac1fd436951d486d551c7b93822
- clm_6a09ff5d063ad441a6116c83ff33e5750b49f3acfc6a16a9225f1e97e4c3b3e3
- clm_6e76580d4a2d5f02c2872490438c8d5dd3af395e3f83599b0b98ede8ba8bf69b
- clm_dedbb3ef52a30450ea7d4107a30759a1d7326e42ad2b0a8731b9af85351d99f2
- clm_dfdc7aa10d901b5177984db51d457bc54dda47d840c7823fcf94c64072fe85ea
- clm_e0814f36d299d52be5e1186498df052e916c8b65e0f2278c71a2e0600a0dbfa2
- clm_e496b6ef98a44ca543b57ba0e35e3d957a5960b25a0d668bc2bb8f7c576821f6
- clm_fc49aa3aba3966266d452b4e9afc40fb1dec4bea97059c7366292f6883a220ff
maturity: draft
page_id: pg_1cc56772532d58b6b82bdf5ebb1c415f
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_acab5a616cbc5342920196d674bce990
title: memorax-ai/memorax-code/README.md @ 1525c20fbcad
updated_at: '2026-09-14T04:09:28Z'
---

# memorax-ai/memorax-code/README.md @ 1525c20fbcad

<!-- rcw:begin owner=source:src_acab5a616cbc5342920196d674bce990 block=evidence -->
- Memory is divided into four categories: Coding Memory (engineering lessons), Repo Memory (repository knowledge), Personal Memory (user preferences), and Procedure Memory (reusable task steps). [@claim:clm_00ef1fa849729e7a115af31d85fd43cd1fb0031427e120f1f4efca65a9467d02]
- The product targets the problem that new coding-agent sessions start without prior architecture knowledge, failed attempts, repository rules, or working preferences, providing a shared memory layer across supported clients. [@claim:clm_240adc51d6340123da53373e82062821f0b3eac1fd436951d486d551c7b93822]
- Local trace capture is on by default for supported clients and retained traces under MEMORAX_CODE_HOME may include prompts, responses, recalled memory, reminder text, and local paths; it can be switched to metadata-only or disabled. [@claim:clm_6a09ff5d063ad441a6116c83ff33e5750b49f3acfc6a16a9225f1e97e4c3b3e3]
- Personal and Procedure Memory stay in the current repository under .repo_memory/; writes compare existing content so equivalent requests make no change and conflicts update or supersede entries. [@claim:clm_6e76580d4a2d5f02c2872490438c8d5dd3af395e3f83599b0b98ede8ba8bf69b]
- Repository development practice: contributors are directed to read CONTRIBUTING.md before making changes, and AGENTS.md defines working rules for coding agents, runtime/data invariants, and Git handoff requirements. [@claim:clm_dedbb3ef52a30450ea7d4107a30759a1d7326e42ad2b0a8731b9af85351d99f2]
- On Linux, guest credentials require /usr/bin/secret-tool from libsecret and an available Secret Service, and MemoraX search and writeback require network access. [@claim:clm_dfdc7aa10d901b5177984db51d457bc54dda47d840c7823fcf94c64072fe85ea]
- The package requires Node.js 20 or newer (Node 24 LTS recommended), and DeepSeek Harness releases require Node ^22.19.0 || >=24.0.0 with pnpm on PATH; MemoraX Code does not install or update DSH. [@claim:clm_e0814f36d299d52be5e1186498df052e916c8b65e0f2278c71a2e0600a0dbfa2]
- The MemoraX platform does not currently support attaching a Mark ID to an already-registered account, so guest users must obtain the Mark ID before registering to keep guest memory. [@claim:clm_e496b6ef98a44ca543b57ba0e35e3d957a5960b25a0d668bc2bb8f7c576821f6]
- Trae can use the Skill for Repo Memory but does not currently expose a headless worker for automatic Repo Memory maintenance, and automatic quota reminders are not listed for DeepSeek Harness. [@claim:clm_fc49aa3aba3966266d452b4e9afc40fb1dec4bea97059c7366292f6883a220ff]
<!-- rcw:end owner=source:src_acab5a616cbc5342920196d674bce990 block=evidence -->

## Researcher notes

