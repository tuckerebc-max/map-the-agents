---
access: public
aliases: []
claim_ids:
- clm_0475b89f5bfe31899de4be72b7abcd8e06ae41d2b69a02a99397caa4c687dd30
- clm_0a0059637d9c2dec44469c8016c9b5119cd0c3a6ab73b65419c60346199c2b79
- clm_4eb19095b825e1dce149eb592b543a2c3cba59be0d3a5c9fb358d80f6e477c5b
- clm_4f40ab06dac6a094c5ae2d85ccbce7383fd4bf12378cf8e15c31da7f1b715339
- clm_5480a7cfb79f0be9eca4f737d770f3f02b949d0938504601eca8059b1034edeb
- clm_68a747fa5b84177e8c72b23a834b71d99e8911595d41008d634785c50377b4e3
- clm_8c713e5de00cf36e36dd5dfd45cb26a4f8f315e617623a16d7f0b359c62d2ce5
- clm_8eca49103057ef62c2b73cadf2d63d29a3a6e5e650e4cfb8bb845a331e910a2b
- clm_bc85f846cbe4371da7a7bd63cc0021c9ad8192e27c22f0bda0ef2d785f126c18
- clm_ca335db59b0fc1a02d2aa7e0aab28c0b93ebbacc0497fa0ec913c85923b58b23
- clm_d0c198c3e506aef2728817f79cdfde75acb6d1e4a78863dc95863926a278aae1
- clm_d549687835c904fd64a719ee9a77bac891c203766fbffd0bcf89da3dc365c8d4
- clm_e34bea2087838fa9d13c24274906cc14a3bd5e1ad2244be65a23e893b7116c5a
- clm_eb8b142d8da726cb48de1fafc9894d79902ea0afa680698d00408866a3f0640b
- clm_ef3c31899f024447ae41c0d8abe2737080c85cd26bcdee574b7d18a6f50075f5
maturity: draft
page_id: pg_5f7c07d8d9be58ce9358a0ecbed36360
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_018b66cb8fbc5c9c9d7a86fd29d372ee
title: with-geun/alive-analysis/README.md @ e9f8d8209ff2
updated_at: '2026-09-14T04:32:58Z'
---

# with-geun/alive-analysis/README.md @ e9f8d8209ff2

<!-- rcw:begin owner=source:src_018b66cb8fbc5c9c9d7a86fd29d372ee block=evidence -->
- Education mode scores learner work against rubrics with three progressive hint levels and a graduation path (70%+ on two Beginner scenarios unlocks Intermediate; 75%+ there is deemed production-ready). [@claim:clm_0475b89f5bfe31899de4be72b7abcd8e06ae41d2b69a02a99397caa4c687dd30]
- Experiment-type analyses adapt the loop to DESIGN, VALIDATE, ANALYZE, DECIDE, LEARN with enforcements including a pre-registration lock, automatic SRM detection, guardrail metrics, and multiple-comparison correction. [@claim:clm_0a0059637d9c2dec44469c8016c9b5119cd0c3a6ab73b65419c60346199c2b79]
- Agents can be disabled per-project via a .analysis/agents.yml configuration file. [@claim:clm_4eb19095b825e1dce149eb592b543a2c3cba59be0d3a5c9fb358d80f6e477c5b]
- The README states the product is not a BI tool, does not connect to databases or run queries automatically, and is tool-agnostic about the user's data stack (SQL, Python, R, notebooks, spreadsheets). [@claim:clm_4f40ab06dac6a094c5ae2d85ccbce7383fd4bf12378cf8e15c31da7f1b715339]
- The team dashboard is a single-file HTML5 force-directed node graph (D3.js v7) where node size encodes stage progress, color encodes analysis type, and edges show follow-up or shared-tag connections; data comes from a bash export script emitting JSON. [@claim:clm_5480a7cfb79f0be9eca4f737d770f3f02b949d0938504601eca8059b1034edeb]
- Three analysis modes exist: Full (five per-stage files, ~40-item checklists), Quick (single file, compressed checklist, promotable to Full via /analysis-promote), and Learn (guided scenarios with rubric-based scoring). [@claim:clm_68a747fa5b84177e8c72b23a834b71d99e8911595d41008d634785c50377b4e3]
- Analyses follow a five-stage ALIVE loop (ASK, LOOK, INVESTIGATE, VOICE, EVOLVE); each stage produces a markdown file and has a checklist plus a quality gate before advancing. [@claim:clm_8c713e5de00cf36e36dd5dfd45cb26a4f8f315e617623a16d7f0b359c62d2ce5]
- The product is a structured analysis workflow for AI coding agents, versioned 1.4.0 and MIT-licensed, with its MCP server distributed on npm as alive-analysis-mcp. [@claim:clm_8eca49103057ef62c2b73cadf2d63d29a3a6e5e650e4cfb8bb845a331e910a2b]
- The tool targets teams doing product/metric analysis with AI agents, aiming to preserve reasoning, data checks, and audit trails across sessions instead of losing them in chat history. [@claim:clm_bc85f846cbe4371da7a7bd63cc0021c9ad8192e27c22f0bda0ef2d785f126c18]
- The analyses/ folder doubles as an Obsidian vault; wiki-links like [[F-2026-0305-001]] are picked up by Obsidian's graph view. [@claim:clm_ca335db59b0fc1a02d2aa7e0aab28c0b93ebbacc0497fa0ec913c85923b58b23]
- A routing engine reads analysis context and recommends specialists from a pool of 31 agents, presenting the top 3 with explanations; four gate agents (scope-guard, data-quality-sentinel, ethics-guard, reproducibility-keeper) auto-run when their trigger conditions are met. [@claim:clm_d0c198c3e506aef2728817f79cdfde75acb6d1e4a78863dc95863926a278aae1]
- The product exposes slash commands including /analysis-init, /analysis-new, /analysis-next, /analysis-status, /analysis-archive, /analysis-list, /analysis-promote, /analysis-search, /analysis-retro, /analysis-dashboard, /analysis-dr, and /analysis-wiki. [@claim:clm_d549687835c904fd64a719ee9a77bac891c203766fbffd0bcf89da3dc365c8d4]
- Repository development practice: the README's Contributing section says issues and PRs are welcome and points contributors to CONTRIBUTING.md. [@claim:clm_e34bea2087838fa9d13c24274906cc14a3bd5e1ad2244be65a23e893b7116c5a]
- The MCP server (alive-analysis-mcp) exposes four tools — alive_list, alive_get, alive_search, alive_dashboard_export — configured for Claude Desktop via an --analyses-dir argument or for Claude Code via an ALIVE_ANALYSES_DIR environment variable. [@claim:clm_eb8b142d8da726cb48de1fafc9894d79902ea0afa680698d00408866a3f0640b]
- Platform support is documented for Claude Code and Cursor 2.4+, with Cursor using a batch interaction model that presents all required inputs at once. [@claim:clm_ef3c31899f024447ae41c0d8abe2737080c85cd26bcdee574b7d18a6f50075f5]
<!-- rcw:end owner=source:src_018b66cb8fbc5c9c9d7a86fd29d372ee block=evidence -->

## Researcher notes

