---
access: public
aliases: []
claim_ids:
- clm_2977149c896d390d85dc7b688e24d0de53cc006e0462a859791ae8181d201d77
- clm_356548984db3b70dec0dac9254b93e3319b3637b92c1356fdc4205836dc4903d
- clm_3c496fa181c347d4d2bc5d1d713272a867683522e9293cbe867f2d628f5edf49
- clm_51f805147a670437263e2ea05c5038d3e55dae7996da0334828ae8a95a7e926e
- clm_628012f55f1759ff16b6fdc0a848a6034952fe44437ec4da5938bf74d3466e08
- clm_8c7894a7fa7f85c096726b8d440f1909f6aad5fd0aa7fb372d1edd8beffe0310
- clm_9a37a215454350cff077b7be60a3ad65d016ecccda6d8b76a32553e61d876430
- clm_a563bc20230ea2696cfc480d8afcdee4f3ffd70199fb71282981b6de00cb24bd
- clm_b156661f134fe4a626a4c5ef6cab80740e13d404de73f21a6b965a6c9ab242b3
- clm_d312c51a35551142730fe5916cd76a6658ca102cc1958b87ea57f9e26cb6ef3a
- clm_d8e825009f4e4be073c8dc8c811ddef411ea6948c8737fe98e5c9f03f46fe9a1
- clm_f1216dbd966231217d4dea2f9e592660ca95c677ee81d60d67548fbea74aee7c
maturity: draft
page_id: pg_fbbc3f69e06958d4887ad72bb23d312c
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_07acea46c7545d4084ff9872d0c06910
title: AlmanacCode/codealmanac/README.md @ 0f153501f40a
updated_at: '2026-09-14T03:34:14Z'
---

# AlmanacCode/codealmanac/README.md @ 0f153501f40a

<!-- rcw:begin owner=source:src_07acea46c7545d4084ff9872d0c06910 block=evidence -->
- The product is local-only: no hosted login, connect, or upload commands, no public SDK or MCP package, and no alternate wiki roots beyond almanac/. [@claim:clm_2977149c896d390d85dc7b688e24d0de53cc006e0462a859791ae8181d201d77]
- Lifecycle agents run with broad, non-interactive filesystem permissions; the almanac/ boundary is described as an instruction and commit policy rather than an OS sandbox. [@claim:clm_356548984db3b70dec0dac9254b93e3319b3637b92c1356fdc4205836dc4903d]
- The serve command opens a read-only local web viewer rendering pages, search, topics, backlinks, and file-reference navigation, with --no-open and --wiki options. [@claim:clm_3c496fa181c347d4d2bc5d1d713272a867683522e9293cbe867f2d628f5edf49]
- The tool requires Python 3.12+, is distributed via PyPI (the npm package is retired), and uses almanac-yoke as its single provider boundary for Codex and Claude runners. [@claim:clm_51f805147a670437263e2ea05c5038d3e55dae7996da0334828ae8a95a7e926e]
- Sync scans local Codex and Claude transcript stores and queues conversations from registered repositories as ingest jobs, possibly deciding a conversation holds no durable knowledge. [@claim:clm_628012f55f1759ff16b6fdc0a848a6034952fe44437ec4da5938bf74d3466e08]
- Lifecycle commands (init, ingest, garden) queue runs and start a local worker; jobs can be listed, shown, logged, attached to, or cancelled, and records persist after the starting terminal closes. [@claim:clm_8c7894a7fa7f85c096726b8d440f1909f6aad5fd0aa7fb372d1edd8beffe0310]
- Setup installs three macOS launchd jobs: Sync every 5 hours scanning agent conversations, Garden every 24 hours reviewing wikis, and Update every 24 hours installing safe CLI updates. [@claim:clm_9a37a215454350cff077b7be60a3ad65d016ecccda6d8b76a32553e61d876430]
- Optional anonymous telemetry sends command/lifecycle outcomes and sanitized crashes under a random install UUID, never code, paths, prompts, or credentials; it can be disabled via setup flag, config, or DO_NOT_TRACK=1. [@claim:clm_a563bc20230ea2696cfc480d8afcdee4f3ffd70199fb71282981b6de00cb24bd]
- The wiki is plain markdown stored in the repo under almanac/, indexed locally and reviewed in Git like other code changes; a repo counts as a wiki when almanac/topics.yaml and almanac/README.md exist. [@claim:clm_b156661f134fe4a626a4c5ef6cab80740e13d404de73f21a6b965a6c9ab242b3]
- Read commands accept --wiki <name> to target another registered local wiki; by default they target the exact current directory when it is a registered repository root. [@claim:clm_d312c51a35551142730fe5916cd76a6658ca102cc1958b87ea57f9e26cb6ef3a]
- Derived local state lives under ~/.codealmanac/, including a main database recording repositories, runs, run events, worker locks, and sync state, plus per-repo index databases. [@claim:clm_d8e825009f4e4be073c8dc8c811ddef411ea6948c8737fe98e5c9f03f46fe9a1]
- Support is currently limited to macOS with Codex or Claude Code, and the rewrite is described as local-only for now, with hosted integration possible later but not in this release surface. [@claim:clm_f1216dbd966231217d4dea2f9e592660ca95c677ee81d60d67548fbea74aee7c]
<!-- rcw:end owner=source:src_07acea46c7545d4084ff9872d0c06910 block=evidence -->

## Researcher notes

