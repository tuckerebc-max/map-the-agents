---
access: public
aliases: []
claim_ids:
- clm_024b85fabc3ed6fdccecf18b94b19125e6b36492f5d3805ce8e9a348b818f0b3
- clm_1a357f8736b6cc0a08657b1756e8df4ef2f442266db5a604078341f7ba94e5cb
- clm_60cac2514d40779efa690ed3303a1b062c073b159d3ce90fa05c9dac8c721d35
- clm_b02eefd131eba01a9e345283241e7337ffbada4866c63f197ed1d6eca9f1b7ad
maturity: draft
page_id: pg_07c222292f1d5227873d933a52326170
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_85394d2d36eb50b9b042b63bb368925e
title: stacklok/brood-box/docs/ARCHITECTURE.md @ 5f27eeb76988
updated_at: '2026-09-14T02:42:31Z'
---

# stacklok/brood-box/docs/ARCHITECTURE.md @ 5f27eeb76988

<!-- rcw:begin owner=source:src_85394d2d36eb50b9b042b63bb368925e block=evidence -->
- The SandboxRunner lifecycle resolves the agent, merges config, collects forwarded env vars, creates a snapshot, starts the VM, runs an interactive SSH session, stops the VM, diffs, reviews per-file, flushes accepted changes, and cleans up. [@claim:clm_024b85fabc3ed6fdccecf18b94b19125e6b36492f5d3805ce8e9a348b818f0b3]
- The project follows a strict DDD layering: pure domain packages under pkg/domain, an application SandboxRunner in pkg/sandbox, infrastructure implementations in internal/infra, and a Cobra CLI composition root in cmd/bbox. [@claim:clm_1a357f8736b6cc0a08657b1756e8df4ef2f442266db5a604078341f7ba94e5cb]
- Brood Box depends on stacklok/go-microvm as a tagged module (e.g. v0.0.16); task build downloads pre-built go-microvm runtime artifacts and embeds them into a self-contained pure-Go bbox binary, while libkrunfw firmware is downloaded at runtime and cached. [@claim:clm_60cac2514d40779efa690ed3303a1b062c073b159d3ce90fa05c9dac8c721d35]
- The guest VM runs a custom Go init binary (bbox-init) as PID 1 that handles boot, networking, workspace mounting, and an embedded SSH server, with no shell scripts or external sshd. [@claim:clm_b02eefd131eba01a9e345283241e7337ffbada4866c63f197ed1d6eca9f1b7ad]
<!-- rcw:end owner=source:src_85394d2d36eb50b9b042b63bb368925e block=evidence -->

## Researcher notes

