---
access: public
aliases: []
claim_ids:
- clm_25d17b3503f0f70a56d4c6627e8e455ba961183096a27edd4b96b0a7361731a3
- clm_2bcdede85999f98704e486b2e01b4b012e209c4775e97bf6cadf86b2677d8a9c
- clm_399fd78d899ec5c4ed40d88a8b8b3c35dc125f17f407dac2d37be4572cee4fcc
- clm_6625bc64d16e48f8af6e5b54bb1562114f2e3ba70e923db60df8dd0be8c99ad1
- clm_f5df0aa09e45f5d96eff0a0af29b76683bb3c80fff5af2b8ff2ee961bc47c5dd
maturity: draft
page_id: pg_182778a45de15d4ca0119c8d5877736d
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_a424580216455819bbd547e1c5094ab0
title: nimbalyst/nimbalyst/CLAUDE.md @ d6e1d008d9ee
updated_at: '2026-09-14T03:10:36Z'
---

# nimbalyst/nimbalyst/CLAUDE.md @ d6e1d008d9ee

<!-- rcw:begin owner=source:src_a424580216455819bbd547e1c5094ab0 block=evidence -->
- The repository is a TypeScript/Electron npm-workspaces monorepo with packages for the Electron desktop app, a native SwiftUI iOS app, cross-platform runtime services (AI, sync, Lexical editor), a collab-protocol wire-format package, an extension SDK, and built-in extensions. [@claim:clm_25d17b3503f0f70a56d4c6627e8e455ba961183096a27edd4b96b0a7361731a3]
- Repository development practice: CLAUDE.md instructs AI contributors that any runtime-behavior change ships with a unit test and that the pre-push gate (npm run typecheck && npm run test:prepush) must be run locally, with failures recorded to .vitest/last-run.log readable via npm run test:last. [@claim:clm_2bcdede85999f98704e486b2e01b4b012e209c4775e97bf6cadf86b2677d8a9c]
- Repository development practice: API keys must never be read from process.env as a fallback for provider authentication; keys may come only from explicitly configured settings, after a past incident where an env var silently billed a user's personal Anthropic account. [@claim:clm_399fd78d899ec5c4ed40d88a8b8b3c35dc125f17f407dac2d37be4572cee4fcc]
- Repository development practice: contributors must not open database files directly from a second process (risking corruption via PID-based or exclusive locking) and should instead use the mcp__nimbalyst-extension-dev__database_query tool. [@claim:clm_6625bc64d16e48f8af6e5b54bb1562114f2e3ba70e923db60df8dd0be8c99ad1]
- Repository development practice: parallel work slices must declare disjoint file sets (including CHANGELOG.md and package.json), slices never run the full gate themselves, and CHANGELOG entries are written only when a commit is requested, one bullet per feature with no internal scaffolding. [@claim:clm_f5df0aa09e45f5d96eff0a0af29b76683bb3c80fff5af2b8ff2ee961bc47c5dd]
<!-- rcw:end owner=source:src_a424580216455819bbd547e1c5094ab0 block=evidence -->

## Researcher notes

