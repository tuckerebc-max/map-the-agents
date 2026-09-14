---
access: public
aliases: []
claim_ids:
- clm_10aa696aa08f7227c6c28225dced3c7ed40b84bcfbfbc7f935cdf032f2c008b0
- clm_151850951726e5b919a3bba97b8d0bbcc2ee7e654e666a2c109694cb2a52f81a
- clm_18aedf9b60a07a8dfecd3d4bb8198ed4979070f0f82189706ba445cbe11518e0
- clm_1b6c4432a08887fe775af4e489abe7784f67862803984f8619bb03f3cbb1d6a1
- clm_54f42e89394cfa61fd2e6f98dc5deffb1a467d9edd73c0a0124e57e391d39333
- clm_584ee797f3939285b5986aae939f25e1f2fdb047238c147329618fee438e7c7c
- clm_5d839887db4c8d4b2bb40284b08faddf7c32e5658f394de783d53eac5733efde
- clm_b8a7094ff45ebec4632a0dd0a5df899f48cb6f39f7255566681555aa18fd81fd
- clm_d4cfc6dea62942ca25475b8609e3485a6fb97daef9e1379fa1dc2d6d6118399a
- clm_dead6bf90aa07ecb23999bdcb3c7b6c3b293328c0ebd95424b1caad7bcd87a55
- clm_e13e8a900c50387938ff469bd2ae46ea7162b5227c5fef98936fdda51e8a31b0
maturity: draft
page_id: pg_918eb928645f523186ff85e9a40bedf5
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_98e6e24399395741aca7c37edb727bff
title: monkilabs/opencastle/README.md @ f297837635b1
updated_at: '2026-09-14T04:10:20Z'
---

# monkilabs/opencastle/README.md @ f297837635b1

<!-- rcw:begin owner=source:src_98e6e24399395741aca7c37edb727bff block=evidence -->
- The experimental convoy engine runs long tasks in dependency order across isolated git worktrees with SQLite persistence so crashes resume rather than restart. [@claim:clm_10aa696aa08f7227c6c28225dced3c7ed40b84bcfbfbc7f935cdf032f2c008b0]
- Convoy is invoked via 'opencastle convoy "<task>"', with bare convoy showing run state and 'convoy resume' continuing after interruption. [@claim:clm_151850951726e5b919a3bba97b8d0bbcc2ee7e654e666a2c109694cb2a52f81a]
- Running opencastle with no arguments reports installed targets, sync/drift state per assistant, and suggests the next command such as running sync. [@claim:clm_18aedf9b60a07a8dfecd3d4bb8198ed4979070f0f82189706ba445cbe11518e0]
- OpenCastle compiles to native formats for seven assistants including Claude Code (CLAUDE.md + .claude/), Cursor, Windsurf, Copilot, OpenCode, Codex CLI, and Antigravity. [@claim:clm_1b6c4432a08887fe775af4e489abe7784f67862803984f8619bb03f3cbb1d6a1]
- The convoy engine is explicitly labeled experimental and may change; the compiler does not depend on it. [@claim:clm_54f42e89394cfa61fd2e6f98dc5deffb1a467d9edd73c0a0124e57e391d39333]
- Agents declare capability tiers (premium, standard, economy) instead of pinned model names, letting the user's assistant choose the concrete model. [@claim:clm_584ee797f3939285b5986aae939f25e1f2fdb047238c147329618fee438e7c7c]
- The CLI exposes commands including bare status, sync (with --check for CI drift detection), add, and doctor, per the README's everyday-use examples. [@claim:clm_5d839887db4c8d4b2bb40284b08faddf7c32e5658f394de783d53eac5733efde]
- Repository development practice: contributors fork, branch as feat/ or fix/, ensure npm test and npx tsc --noEmit pass, then open a PR. [@claim:clm_b8a7094ff45ebec4632a0dd0a5df899f48cb6f39f7255566681555aa18fd81fd]
- The init command scans the repository for existing assistant config, framework, database, and test runner, then shows findings and asks a single confirmation. [@claim:clm_d4cfc6dea62942ca25475b8609e3485a6fb97daef9e1379fa1dc2d6d6118399a]
- Compiled content includes 13 role agent definitions, 31 domain skills plus 31 tool integrations loaded on demand, and 9 workflow templates. [@claim:clm_dead6bf90aa07ecb23999bdcb3c7b6c3b293328c0ebd95424b1caad7bcd87a55]
- Repository development practice: a CI workflow runs 'npx opencastle sync --check' on Node 22, and generated config is committed like a lockfile so the check has something to compare. [@claim:clm_e13e8a900c50387938ff469bd2ae46ea7162b5227c5fef98936fdda51e8a31b0]
<!-- rcw:end owner=source:src_98e6e24399395741aca7c37edb727bff block=evidence -->

## Researcher notes

