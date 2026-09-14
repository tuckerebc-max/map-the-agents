---
access: public
aliases: []
claim_ids:
- clm_0e5d29b6dedc005b653821275afa67ebd02afd880a6eb405e5eb7a196615fc8c
- clm_105014d924b25e519cecc21d417b0d2de15a7cdb764de15ab0c6e84752a8697f
- clm_3d6a7d0597e6ca15591c35cdbf4113cdb7106ddda2212e97034005af8fda2239
- clm_51bb064a0be450abf3833e9edcf1095eeac19fcfd26d96861f34fe203ab43cfe
- clm_6e0cee3d0ef9fb48d2a64af69932471fa3a2d75b324d2a606248af898c4b840f
- clm_9de5bb01170e5a33f41495cc23c00132ee1f87e71bca99c5775edf62c83a7fa6
- clm_aad8c4d7e94fad5ffbc9d4e4979621a34a4ed639df0fb167335c949fc0a86df1
- clm_ae96de8fd332dcf0913d4e9163301ad6f790682478413c91bb7fb89f6c980274
- clm_baf49f898612c0d1607a2c499df6a0570704e54eef91703f124b0acef7b75aee
- clm_d8d4ea05c10b8183558cf2b2dc435321fb6e914764821698ba41093323fa6efb
maturity: draft
page_id: pg_de1e3c14fbec53f88544956c01c38b78
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_9a5c51749a775bd7908166914ee6d87e
title: jigjoy-ai/baro/docs/collective-experiment.md @ f9a610774532
updated_at: '2026-09-14T02:06:52Z'
---

# jigjoy-ai/baro/docs/collective-experiment.md @ f9a610774532

<!-- rcw:begin owner=source:src_9a5c51749a775bd7908166914ee6d87e block=evidence -->
- Repository development practice: the experiment guide instructs preparing a clean git repo with an unexecuted prd.json whose stories have concrete acceptance criteria and test commands, and installing workspace dependencies with npm install before running trials. [@claim:clm_0e5d29b6dedc005b653821275afa67ebd02afd880a6eb405e5eb7a196615fc8c]
- `--local-only` disables pushes and PRs but is explicitly not an OS or network sandbox, since story agents can execute arbitrary shell commands; a hard no-push boundary requires removing git remotes. [@claim:clm_105014d924b25e519cecc21d417b0d2de15a7cdb764de15ab0c6e84752a8697f]
- Codex, OpenCode, and Pi workers are one-shot CLI processes that cannot consume corrective messages after exit; failed verdicts for those backends require a separate recovery execution rather than in-process revision. [@claim:clm_3d6a7d0597e6ca15591c35cdbf4113cdb7106ddda2212e97034005af8fda2239]
- Collective coordination is the CLI default; a legacy Conductor mode (one owner of DAG levels, retries, completion) can be selected with `--coordination legacy` for A/B comparison. [@claim:clm_51bb064a0be450abf3833e9edcf1095eeac19fcfd26d96861f34fe203ab43cfe]
- Runtime replan proposals carry run/story/lease/generation and a graphVersion; invalid, stale, cyclic, unauthorized, over-budget or non-durable candidates get a correlated rejection and are never shown as applied just because a model requested them. [@claim:clm_6e0cee3d0ef9fb48d2a64af69932471fa3a2d75b324d2a606248af898c4b840f]
- The public CLI does not yet expose process-level run resumption: a restart creates a new run identity, keeps the graph version as baseline, resets the discovery budget, and does not expose the old decision ledger. [@claim:clm_9de5bb01170e5a33f41495cc23c00132ee1f87e71bca99c5775edf62c83a7fa6]
- A paired A/B harness (ab-run.ts) compares legacy vs collective coordination on identical PRD bytes across isolated clones, alternating arm order, hashing verify inputs, and producing per-trial artifacts including diff.patch, metrics.json, and audit logs. [@claim:clm_aad8c4d7e94fad5ffbc9d4e4979621a34a4ed639df0fb167335c949fc0a86df1]
- In collective mode, workers publish credential-free capabilities and bids, a broker grants a correlated lease to a deterministic winner, and with the Critic enabled a story passes only after the acceptance verdict plus StoryMerged, not merely when the model process exits. [@claim:clm_ae96de8fd332dcf0913d4e9163301ad6f790682478413c91bb7fb89f6c980274]
- Proposal IDs act as idempotency keys: exact re-delivery returns the remembered decision without reapplying, reuse with different content is rejected, and applied decisions can be restored from the PRD's runtimeGraph metadata when a host resumes the same runId. [@claim:clm_baf49f898612c0d1607a2c499df6a0570704e54eef91703f124b0acef7b75aee]
- The DialogueAgent is text-only with no codebase tools; it may send a bounded targeted message and one add-only delegation proposal of at most two stories, with no authority over removal, rewiring, priority, retries, model, route, lease, or merging. [@claim:clm_d8d4ea05c10b8183558cf2b2dc435321fb6e914764821698ba41093323fa6efb]
<!-- rcw:end owner=source:src_9a5c51749a775bd7908166914ee6d87e block=evidence -->

## Researcher notes

