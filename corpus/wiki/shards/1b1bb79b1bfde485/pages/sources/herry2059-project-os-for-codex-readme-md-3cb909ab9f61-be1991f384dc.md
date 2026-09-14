---
access: public
aliases: []
claim_ids:
- clm_0bf96c9f545e21013613668df7059b1be652419401bc2439d188c07d4db841d2
- clm_0e614fceb948b9c17a8db38686ffd89d1975719960b9002ebb55fff992091592
- clm_10ff73852c2d3d163a52758640ad407003784c72df654bb915656190d8a43136
- clm_3d9f3f90adfad3d749fcc33d51447b9f783542095e435499bc12986616b5c9db
- clm_505d5baa55fb3ede538bd2052b62e1e06fd6fb18d838d148cb4a6cf6ae650743
- clm_82308b18879b1cb426a3bb84259dfdebd0e9dc5a54e8009b41466598cf90cd2e
- clm_875b5289194917f8ebaa709322274ff9972ab45318e387a1a2d1f5436d3cdc14
- clm_9af94a8357694dc42a69c58861d1d1e0fd2701f6da0d837477594db662c1fa36
- clm_bdb1c7199cce60d79e28e986dc1158d3715f255a802840c364e77a0a05701a67
- clm_d5ee7eba328c2168569c7a435e4c6b2e8c81109864dc019699b222a873cbe029
maturity: draft
page_id: pg_fdc318f372cf5a1cb680be1991f384dc
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_59e7420d879c56ec92e7ff5630094eef
title: herry2059/project-os-for-codex/README.md @ 3cb909ab9f61
updated_at: '2026-09-14T02:03:21Z'
---

# herry2059/project-os-for-codex/README.md @ 3cb909ab9f61

<!-- rcw:begin owner=source:src_59e7420d879c56ec92e7ff5630094eef block=evidence -->
- Verification notes are agent-reported and validated for structure, identity, scope, idempotency, and progress rules, but the server does not independently prove source code or deployments passed. [@claim:clm_0bf96c9f545e21013613668df7059b1be652419401bc2439d188c07d4db841d2]
- The released MCP surface contains exactly two tools: project_os_get_context for scoped context reads and project_os_append_progress for validated, idempotent progress appends. [@claim:clm_0e614fceb948b9c17a8db38686ffd89d1975719960b9002ebb55fff992091592]
- The open-source design keeps private infrastructure behind replaceable adapter boundaries for Git, AI provider, knowledge base, and deployment/reverse proxy, with local JSON persistence for simple evaluation. [@claim:clm_10ff73852c2d3d163a52758640ad407003784c72df654bb915656190d8a43136]
- An Agent API endpoint accepts progress events via POST with X-Project-Key and Idempotency-Key headers, including verification notes, progress percentage, and next step. [@claim:clm_3d9f3f90adfad3d749fcc33d51447b9f783542095e435499bc12986616b5c9db]
- Version 0.3.0 adds a fail-closed first-run contract: the MCP process verifies credential, project binding, scopes, and the exact two-tool surface before Codex uses it, with a project-level config allowlisting only released tools. [@claim:clm_505d5baa55fb3ede538bd2052b62e1e06fd6fb18d838d148cb4a6cf6ae650743]
- The stack is React, Vite, TypeScript, and Tailwind CSS on the frontend with Node.js and Express on the backend, persisting to local JSON files by default under an Apache-2.0 license. [@claim:clm_82308b18879b1cb426a3bb84259dfdebd0e9dc5a54e8009b41466598cf90cd2e]
- The server creates a local Git-backed project record for kickoff, progress, issues, and handoff files, with important progress linked to Git commits as the durable record. [@claim:clm_875b5289194917f8ebaa709322274ff9972ab45318e387a1a2d1f5436d3cdc14]
- AI credentials are short-lived (24 hours or 7 days), revocable independently, stored only as hashes, and cannot access members, keys, deletion, publication, or deployment. [@claim:clm_9af94a8357694dc42a69c58861d1d1e0fd2701f6da0d837477594db662c1fa36]
- The product does not run Codex, monitor sessions automatically, control a Codex account, or modify an existing source repository; its Git commits belong to the local Project OS record repository. [@claim:clm_bdb1c7199cce60d79e28e986dc1158d3715f255a802840c364e77a0a05701a67]
- High-risk actions such as payment, deletion, role changes, publication, deployment, and rollback stay outside the MCP surface and require explicit human confirmation. [@claim:clm_d5ee7eba328c2168569c7a435e4c6b2e8c81109864dc019699b222a873cbe029]
<!-- rcw:end owner=source:src_59e7420d879c56ec92e7ff5630094eef block=evidence -->

## Researcher notes

