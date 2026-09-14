---
access: public
aliases: []
claim_ids:
- clm_5b760d4977d82ca2ac227b16909fbb9e1341fb7b80980924261609bed3f5b9f1
- clm_8150547612d9e2bf75eb8866f1b671801024ceccf12cf4fc9980a43cfd3cd6ed
maturity: draft
page_id: pg_53a1457ac98352b3ac618f29d638ecc2
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_109c906d1405539e941e767ff6c01186
title: solo-agent/solo/AGENTS.md @ 9d58e66769ed
updated_at: '2026-09-14T02:41:12Z'
---

# solo-agent/solo/AGENTS.md @ 9d58e66769ed

<!-- rcw:begin owner=source:src_109c906d1405539e941e767ff6c01186 block=evidence -->
- Repository development practice: agents may restart the frontend, API server, and daemon only via `make rebuild` from the repo root, and must never use launchctl, direct binaries, go run, npm run dev, nohup, or custom background commands. [@claim:clm_5b760d4977d82ca2ac227b16909fbb9e1341fb7b80980924261609bed3f5b9f1]
- Repository development practice: contributor rules require a complete architecture design before implementation, whole-project review of changes, and E2E validation using real frontend, API server, and PostgreSQL with no mocks for HTTP routes, services, or database behavior. [@claim:clm_8150547612d9e2bf75eb8866f1b671801024ceccf12cf4fc9980a43cfd3cd6ed]
<!-- rcw:end owner=source:src_109c906d1405539e941e767ff6c01186 block=evidence -->

## Researcher notes

