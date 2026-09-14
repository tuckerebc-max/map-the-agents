---
access: public
aliases: []
claim_ids:
- clm_8caff6869983a9e3fd3980a4682fa21d6e645241026f6cf66f1b4ac7a3915e89
- clm_b0fe7b41816f8a9c7d3200b12342185ac681511119188f6b6e47a9f4f48b67af
- clm_fff2bab0bada154ab9d84941d3f32689b1f2a8663038bef381b1d6caa791448c
maturity: draft
page_id: pg_cf1a322cad8855fa9d874d652e59f4a1
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_71fc3729ed1258809e0018f9b6f9e632
title: GoogleCloudPlatform/race-condition/GEMINI.md @ 26efc1b46743
updated_at: '2026-09-14T03:55:12Z'
---

# GoogleCloudPlatform/race-condition/GEMINI.md @ 26efc1b46743

<!-- rcw:begin owner=source:src_71fc3729ed1258809e0018f9b6f9e632 block=evidence -->
- Agents expose agent cards at /.well-known/agent-card.json; the gateway fetches these cards at startup and routes messages to agents based on their declared skills. [@claim:clm_8caff6869983a9e3fd3980a4682fa21d6e645241026f6cf66f1b4ac7a3915e89]
- Repository development practice: the repo ships an AGENTS.md plus four skill files under .claude/skills/ (getting-started, exploring-the-codebase, deploying, contributing) that AI coding assistants are directed to read for setup, architecture, deployment, and contribution tasks. [@claim:clm_b0fe7b41816f8a9c7d3200b12342185ac681511119188f6b6e47a9f4f48b67af]
- Repository development practice: contributors use make targets for tests (Go, Python, web), linting, formatting, and coverage; Python tests run offline because a root conftest.py mocks google.auth.default credentials, and Go integration tests need Redis via docker compose. [@claim:clm_fff2bab0bada154ab9d84941d3f32689b1f2a8663038bef381b1d6caa791448c]
<!-- rcw:end owner=source:src_71fc3729ed1258809e0018f9b6f9e632 block=evidence -->

## Researcher notes

