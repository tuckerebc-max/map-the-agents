---
access: public
aliases: []
claim_ids:
- clm_60ebe396ad28e37aa93ef174f0bba34f73b811a6640bf67dcb65ec9ffea16e7d
- clm_716a94ee2df9d2cc27e347a3f74868aa61fd6730ad2735e8c8ad8f5e50a48d48
- clm_77b3f5647a2ab4bd0aaa53a815091dae89240b4e37ccfafdc325e74c3e92244f
- clm_b4658a6f8b56d4e4b54e99bb5ba3269473613d12a0c19b50af2133d76c572ac0
- clm_f5f5e5080557dcf8eaafc9876e1c021ef7fe57bbfe765dec709a531877b301db
maturity: draft
page_id: pg_6b0706b73c0b5c1bba71a87587e12420
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_c471c5a913f858139dd45ad896f316e4
title: NeuralInverse/neuralinverse/NEURALINVERSE_CODEBASE_GUIDE.md @ 2d68ded2f2b7
updated_at: '2026-09-14T02:21:25Z'
---

# NeuralInverse/neuralinverse/NEURALINVERSE_CODEBASE_GUIDE.md @ 2d68ded2f2b7

<!-- rcw:begin owner=source:src_c471c5a913f858139dd45ad896f316e4 block=evidence -->
- Apply has two modes: Fast Apply prompts the LLM for Search/Replace blocks for quick edits on large files, while Slow Apply rewrites the whole file; edits render as red/green DiffZones. [@claim:clm_60ebe396ad28e37aa93ef174f0bba34f73b811a6640bf67dcb65ec9ffea16e7d]
- Code changes are written to a text model identified only by the file's URI via voidModelService, without requiring the file to be loaded or saved. [@claim:clm_716a94ee2df9d2cc27e347a3f74868aa61fd6730ad2735e8c8ad8f5e50a48d48]
- CE-specific code is organized under src/vs/workbench/contrib/ in modules for AI chat (void/), Power Mode, Agent Manager (neuralInverse/), firmware, and modernisation. [@claim:clm_77b3f5647a2ab4bd0aaa53a815091dae89240b4e37ccfafdc325e74c3e92244f]
- LLM messages are sent from the Electron main process, which the guide says avoids CSP issues with local providers and allows use of node_modules. [@claim:clm_b4658a6f8b56d4e4b54e99bb5ba3269473613d12a0c19b50af2133d76c572ac0]
- voidSettingsService stores all settings including providers, models, and global preferences, and is an implicit dependency of core services; chat modes include normal, gather, and agent. [@claim:clm_f5f5e5080557dcf8eaafc9876e1c021ef7fe57bbfe765dec709a531877b301db]
<!-- rcw:end owner=source:src_c471c5a913f858139dd45ad896f316e4 block=evidence -->

## Researcher notes

