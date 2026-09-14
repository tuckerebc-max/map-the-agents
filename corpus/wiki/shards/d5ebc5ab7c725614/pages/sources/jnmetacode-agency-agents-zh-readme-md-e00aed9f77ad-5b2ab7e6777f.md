---
access: public
aliases: []
claim_ids:
- clm_14bb3e1857ffec42bfcf844ec466bebe395f206e4ecaa20934df028c45417c1f
- clm_1e2410e7fe1861549402f5ae860ff494140969ca0dae080ccaf8f8a3b0ee2295
- clm_2479f15a3e5f3e6965af299b4c81781d0d95ce44994224f8c75f9a44ebbdf190
- clm_2b9869990c85a5a6b7fcb0f722bf21a673a984c192899d3b35ff06fe37009f52
- clm_4d14819594770e366ba9ceb2ebee5e76edf180d7aadf90c7d4218eeed74dd00b
- clm_67696439575e9d300774ec8c37395d0110d2a6a80a5c27d1fbe49051d4ec997b
- clm_6ab1265b6d672ee3ca4bdf1d714974f2d5952c0cf48f7ebe3475956bd896e154
- clm_6d498467d9e307e7d8ed024a0ac4cb60fa20d989951646fa6c43ea34b39d2cc0
- clm_6deee4ba7d5408dc6ce513239a852fc55083404a2f299579a48805c9b0b3e4a1
- clm_7a6fc5cf9dff19f165a155191f2fa5d6d24609c01523bcbcf8324adbb967ddee
- clm_8a354c62f1fdb66bca7c5ebbc3c247034a7068c64858e56beac62b106473d221
maturity: draft
page_id: pg_f0e7f98ba81152f995dc5b2ab7e6777f
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_ef3421de316a5ad88d08fe492fc289b9
title: jnMetaCode/agency-agents-zh/README.md @ e00aed9f77ad
updated_at: '2026-09-14T04:43:34Z'
---

# jnMetaCode/agency-agents-zh/README.md @ e00aed9f77ad

<!-- rcw:begin owner=source:src_ef3421de316a5ad88d08fe492fc289b9 block=evidence -->
- A per-tool install-location table maps each of the 20 tools to target paths, e.g. ~/.claude/agents/ for Claude Code, .cursor/rules/ for Cursor, and ~/.gemini/extensions/agency-agents/ for Gemini CLI. [@claim:clm_14bb3e1857ffec42bfcf844ec466bebe395f206e4ecaa20934df028c45417c1f]
- A companion tool, Agency Orchestrator (npm install -g agency-orchestrator), composes multiple expert agents into teams with a 'ao compose ... --run' command, advertising DAG parallel execution and resume-from-checkpoint. [@claim:clm_1e2410e7fe1861549402f5ae860ff494140969ca0dae080ccaf8f8a3b0ee2295]
- Repository development practice: the README documents a usage workflow of converting formats (convert.sh), installing to a tool (install.sh), and linting agent files (lint-agents.sh), with OpenClaw requiring a gateway restart after install. [@claim:clm_2479f15a3e5f3e6965af299b4c81781d0d95ce44994224f8c75f9a44ebbdf190]
- Claude Code and GitHub Copilot agents can be copied directly without conversion; other tools require running convert.sh first to transform the format. [@claim:clm_2b9869990c85a5a6b7fcb0f722bf21a673a984c192899d3b35ff06fe37009f52]
- The library advertises 277 AI expert agents spanning 20 departments, of which 213 are translations of the English upstream and 64 are original China-market additions. [@claim:clm_4d14819594770e366ba9ceb2ebee5e76edf180d7aadf90c7d4218eeed74dd00b]
- The collection targets users of AI coding assistants who want role-specialized prompts rather than generic templates; agents are also usable by copying/adapting the prompt text directly. [@claim:clm_67696439575e9d300774ec8c37395d0110d2a6a80a5c27d1fbe49051d4ec997b]
- Original China-market agents cover platforms and verticals such as Xiaohongshu, Douyin, WeChat, Bilibili, Feishu/DingTalk operations, cross-border e-commerce, government ToG, medical compliance, Qt industrial host software, and mechanical design. [@claim:clm_6ab1265b6d672ee3ca4bdf1d714974f2d5952c0cf48f7ebe3475956bd896e154]
- The project is a Chinese community fork of msitarzewski/agency-agents, published as the npm package agency-agents-zh under an MIT license. [@claim:clm_6d498467d9e307e7d8ed024a0ac4cb60fa20d989951646fa6c43ea34b39d2cc0]
- The repo ships shell scripts for format conversion and one-click installation: install.sh (with --tool flags for 20 named tools), convert.sh, and lint-agents.sh for checking agent file format. [@claim:clm_6deee4ba7d5408dc6ce513239a852fc55083404a2f299579a48805c9b0b3e4a1]
- Each agent is defined as a persona with an identity, key rules, workflow, and deliverables, activated by natural language after installation into an AI coding tool. [@claim:clm_7a6fc5cf9dff19f165a155191f2fa5d6d24609c01523bcbcf8324adbb967ddee]
- For OpenClaw, each agent is split into three files — SOUL.md (identity/persona), AGENTS.md (capabilities and workflow), and IDENTITY.md (name and intro) — installed under ~/.openclaw/agency-agents/. [@claim:clm_8a354c62f1fdb66bca7c5ebbc3c247034a7068c64858e56beac62b106473d221]
<!-- rcw:end owner=source:src_ef3421de316a5ad88d08fe492fc289b9 block=evidence -->

## Researcher notes

