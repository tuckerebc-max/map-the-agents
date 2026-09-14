---
access: public
aliases: []
claim_ids:
- clm_0a6cdbcd4247e87899182199c11af1f69428675c9f61a12bcd6317259577f95a
- clm_3a547781567d5e5f8d33025c008f8a3f69e59de5abae6b6398fc7c1c9d93d0f6
- clm_59e67ac1078bfe3977e33549522ae908ba9cc9f48ac24f4303a6ad9ea8dbe296
- clm_7417f873c6180d1cb2ed9b5b5e9a0c9146fb0d0338b442f30a70cef61ab41dd6
- clm_815c1dc9ce9d65ec20562d19fa0acd65d53716dd8e58d41595efe81cf6f97c2c
- clm_b078dcab1d17214f58df8e8bf2fd5b882b441175fa19dabb4f67a830194f54a2
- clm_d73add54cd0a6bd30cc47dd6a09c250cbc0a73ecfd8719c5027999e90e5cb955
- clm_ddb7a23072693e7461594b65c4ba343c9e070098f80ed9b0cb8e1e3c51eb9b32
- clm_f7663ba5f01ce5b5896cdbd11c320dbee34d4dfc5d4db951277488eefbede05a
maturity: draft
page_id: pg_8979cadc2b2853a1a619995f90f4e80f
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_43bf6560eba85ead8b03c259c1eb56e5
title: onllm-dev/onUI/README.md @ d1a2d29677a4
updated_at: '2026-09-14T04:14:12Z'
---

# onllm-dev/onUI/README.md @ d1a2d29677a4

<!-- rcw:begin owner=source:src_43bf6560eba85ead8b03c259c1eb56e5 block=evidence -->
- The extension offers two capture flows: Annotate mode for element-level targeting (with Shift multi-select) and Draw mode for rectangle/ellipse region annotations. [@claim:clm_0a6cdbcd4247e87899182199c11af1f69428675c9f61a12bcd6317259577f95a]
- Installer-based MCP setup uses a prebuilt release bundle and requires Node 20+; development prerequisites include Node.js 20+, pnpm 8+, and Chrome, Edge, or Firefox. [@claim:clm_3a547781567d5e5f8d33025c008f8a3f69e59de5abae6b6398fc7c1c9d93d0f6]
- onUI ships as a lightweight browser extension for Chrome, Edge, and Firefox plus a local MCP bridge for annotation-first UI pair programming. [@claim:clm_59e67ac1078bfe3977e33549522ae908ba9cc9f48ac24f4303a6ad9ea8dbe296]
- Exports come in four output levels (compact, standard, detailed, forensic); region annotations include shape and geometry fields in report output at detailed and forensic levels. [@claim:clm_7417f873c6180d1cb2ed9b5b5e9a0c9146fb0d0338b442f30a70cef61ab41dd6]
- Repository development practice: contributors run pnpm install, pnpm check, and pnpm test:coverage; docs/development.md also documents pnpm test:all and loading unpacked builds from packages/extension/dist. [@claim:clm_815c1dc9ce9d65ec20562d19fa0acd65d53716dd8e58d41595efe81cf6f97c2c]
- The MCP server is registered as 'onui-local' and runs via node on the onui-cli.js entrypoint; setup auto-registers it for Claude Code and Codex when those CLIs are installed. [@claim:clm_b078dcab1d17214f58df8e8bf2fd5b882b441175fa19dabb4f67a830194f54a2]
- The repository has three packages: core (shared annotation/report types and formatters), extension (background/content/popup runtime), and mcp-server (local MCP server plus native bridge setup/doctor tooling). [@claim:clm_d73add54cd0a6bd30cc47dd6a09c250cbc0a73ecfd8719c5027999e90e5cb955]
- The extension uses Shadow DOM isolation for stable styling and per-tab ON/OFF control that is off by default; new tabs start with onUI off. [@claim:clm_ddb7a23072693e7461594b65c4ba343c9e070098f80ed9b0cb8e1e3c51eb9b32]
- Repository development practice: releases run locally via app.sh with no CI/CD dependency; --release gates on a clean tree, main branch, and gh auth, then bumps, tags, and publishes a GitHub release. [@claim:clm_f7663ba5f01ce5b5896cdbd11c320dbee34d4dfc5d4db951277488eefbede05a]
<!-- rcw:end owner=source:src_43bf6560eba85ead8b03c259c1eb56e5 block=evidence -->

## Researcher notes

