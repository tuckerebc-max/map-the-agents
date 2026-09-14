---
access: public
aliases: []
claim_ids:
- clm_189ea82591a4c70aa5ac4d2bb98dd27bc07f2d1cbe8232699c948eb48ea40743
- clm_3d70a2711a3754162d35e5e3dbea9673fa8b3cc6361f26cde522255b6fdbe3b3
- clm_4e24f56c08597b4e5bf19e6f1e352de6b37e6807b8d4e52986189f79bdb42944
- clm_86e231bb57bc19427e07677cd6dc9f5a0346474f1398cc99dfc7e1c43b6d1fef
- clm_fd6e4cbfe8bb6700351129167ddde7d053860c1add0dc82bb9d76e0d125fc569
maturity: draft
page_id: pg_3fa79d89e28556bc8e6849ec65d1facf
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_164b8ffe7141596bbe129d9cd9b84e42
title: superloglabs/superlog/docs/webhooks.md @ feffc9fd542a
updated_at: '2026-09-14T03:17:02Z'
---

# superloglabs/superlog/docs/webhooks.md @ feffc9fd542a

<!-- rcw:begin owner=source:src_164b8ffe7141596bbe129d9cd9b84e42 block=evidence -->
- A completed agent investigation can produce a root cause with confidence, estimated impact, severity, an opened pull request with patch and validation status, and Linear tickets, embedded in the agent_completed webhook payload. [@claim:clm_189ea82591a4c70aa5ac4d2bb98dd27bc07f2d1cbe8232699c948eb48ea40743]
- Outgoing webhooks use exactly two events, incident.created and incident.updated; resolve, reopen, merge, and agent start/finish/fail/await-input are all incident.updated distinguished by a change.kind field. [@claim:clm_3d70a2711a3754162d35e5e3dbea9673fa8b3cc6361f26cde522255b6fdbe3b3]
- Agent investigation runtimes are pluggable, with a default 'community' runner that records a local incident summary; webhook agentRun payloads show a runtime value of 'anthropic' and states including queued, running, awaiting_human, blocked_no_github, complete, and failed. [@claim:clm_4e24f56c08597b4e5bf19e6f1e352de6b37e6807b8d4e52986189f79bdb42944]
- Webhook delivery is a JSON POST with a 10-second timeout; failures are retried with backoff up to 8 attempts (~8h) before being marked failed, and retries reuse a stable Superlog-Delivery UUID as an idempotency key. [@claim:clm_86e231bb57bc19427e07677cd6dc9f5a0346474f1398cc99dfc7e1c43b6d1fef]
- Webhook deliveries carry a Stripe-style Superlog-Signature header (t=<unix-ts>,v1=<hex>) where the hex is HMAC-SHA256 over '<timestamp>.<raw body>'; verification must use the raw body before JSON parsing. [@claim:clm_fd6e4cbfe8bb6700351129167ddde7d053860c1add0dc82bb9d76e0d125fc569]
<!-- rcw:end owner=source:src_164b8ffe7141596bbe129d9cd9b84e42 block=evidence -->

## Researcher notes

