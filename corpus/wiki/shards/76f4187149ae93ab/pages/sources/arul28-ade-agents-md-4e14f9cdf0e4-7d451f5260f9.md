---
access: public
aliases: []
claim_ids:
- clm_26a3cb98ff4cdd901a66252b198b2a330bcb13341a0b6ee95eb9e61acc711143
- clm_371dbe999fffc43586ceb731c6e0f7127169cd9a15471601d1c40e20a4fbe90c
- clm_43718c723c662d9363f9bac9c02387d673d9097229f989d4643de9a45f1c205d
- clm_86c97dce700ad06af87539ba3420dc4f7ce2ceae3803f6ed57a648725d74f707
- clm_e2d3c884f44e5bd60f5b2f4685dc485d194085cb4c761bfabb917e00970e6a09
maturity: draft
page_id: pg_202c4a88b241500b8ae67d451f5260f9
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_8fbff41946485f0a956bf1043fcdf893
title: arul28/ADE/AGENTS.md @ 4e14f9cdf0e4
updated_at: '2026-09-14T01:34:36Z'
---

# arul28/ADE/AGENTS.md @ 4e14f9cdf0e4

<!-- rcw:begin owner=source:src_8fbff41946485f0a956bf1043fcdf893 block=evidence -->
- Repository development practice: PRs require conventional-commit titles, a Problem/Cause/Change/Verification body, before/after images for UI changes, and one concern per PR. [@claim:clm_26a3cb98ff4cdd901a66252b198b2a330bcb13341a0b6ee95eb9e61acc711143]
- Repository development practice: AGENTS.md defines a five-stage dev loop (/context, /quality, /test, /ship plus utilities) implemented as agent skills under .agents/skills/, with /ship wrapping an autonomous PR-to-merge playbook. [@claim:clm_371dbe999fffc43586ceb731c6e0f7127169cd9a15471601d1c40e20a4fbe90c]
- Repository development practice: Node.js 22.x is required because node:sqlite is the primary database engine, and each app under apps/ has independent node_modules with no npm workspaces. [@claim:clm_43718c723c662d9363f9bac9c02387d673d9097229f989d4643de9a45f1c205d]
- Repository development practice: releases are cut by tagging main with vX.Y.Z, triggering a workflow that publishes a draft GitHub Release; Windows builds are gated behind the ADE_WINDOWS_PUBLIC_RELEASE_ENABLED variable. [@claim:clm_86c97dce700ad06af87539ba3420dc4f7ce2ceae3803f6ed57a648725d74f707]
- Repository development practice: validation uses desktop and CLI typecheck/test/build commands, with the large desktop suite sharded and the smallest relevant subset run first. [@claim:clm_e2d3c884f44e5bd60f5b2f4685dc485d194085cb4c761bfabb917e00970e6a09]
<!-- rcw:end owner=source:src_8fbff41946485f0a956bf1043fcdf893 block=evidence -->

## Researcher notes

