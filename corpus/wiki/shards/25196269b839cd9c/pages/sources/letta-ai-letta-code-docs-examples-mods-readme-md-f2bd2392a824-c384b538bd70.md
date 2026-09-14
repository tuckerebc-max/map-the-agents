---
access: public
aliases: []
claim_ids:
- clm_620c8ca987a08b92188ef8ac08e403edde0b3af25f50a365292b8282f0657b16
- clm_ba1bf2a9771b6650f3912fdcc2dbfb5ac4a52bf4f56f82ec7c51dea906a1bfb4
- clm_d338eb607bc396e4231717c3d02b0f41570d497fda647f9a6755aa95951af61e
maturity: draft
page_id: pg_01aefb49e79053c7b5e3c384b538bd70
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_a1638063f650540daf5a1f1887067ac7
title: letta-ai/letta-code/docs/examples/mods/README.md @ f2bd2392a824
updated_at: '2026-09-14T02:12:21Z'
---

# letta-ai/letta-code/docs/examples/mods/README.md @ f2bd2392a824

<!-- rcw:begin owner=source:src_a1638063f650540daf5a1f1887067ac7 block=evidence -->
- The example memory-citations mod is intentionally conservative: it observes memory paths passed to tools at tool_start (before execution), not successful reads, and marks shell-command matches as medium confidence. [@claim:clm_620c8ca987a08b92188ef8ac08e403edde0b3af25f50a365292b8282f0657b16]
- A mod-learning harness (scripts/mod-learning/learn-mod.ts) runs a headless agent to generate a candidate mod, then a second headless eval with LETTA_MODS_DIR pointed at it, saving prompts, output, and a pass/fail report under .letta/mod-learning-runs/. [@claim:clm_ba1bf2a9771b6650f3912fdcc2dbfb5ac4a52bf4f56f82ec7c51dea906a1bfb4]
- The /mods learn TUI command never auto-installs learned mods; users must review the generated candidate before copying it into their mod directory and running /reload. [@claim:clm_d338eb607bc396e4231717c3d02b0f41570d497fda647f9a6755aa95951af61e]
<!-- rcw:end owner=source:src_a1638063f650540daf5a1f1887067ac7 block=evidence -->

## Researcher notes

