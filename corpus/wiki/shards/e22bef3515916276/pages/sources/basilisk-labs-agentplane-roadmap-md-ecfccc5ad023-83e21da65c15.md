---
access: public
aliases: []
claim_ids:
- clm_1bc37a795fdb42e459d031a010e8591c0e5fcc568564d3fbb14ec4854b2c558e
- clm_2e7b18cde13b2fde3c6870dc745e92a447b192908aed443020cbfa52828f22b2
- clm_f7f8893373dca19d9be87d75299a84cd36526429ab714c7958e071998e306cea
maturity: draft
page_id: pg_997a3cf91ba35d59941583e21da65c15
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_642751c5f70755e28ae153c6abbd51e2
title: basilisk-labs/agentplane/ROADMAP.md @ ecfccc5ad023
updated_at: '2026-09-14T01:36:43Z'
---

# basilisk-labs/agentplane/ROADMAP.md @ ecfccc5ad023

<!-- rcw:begin owner=source:src_642751c5f70755e28ae153c6abbd51e2 block=evidence -->
- A supervisor model prepares a bounded AgentWorkOrder, enforces state and authority preconditions, invokes one specialized semantic role, and records an independent ExecutionReceipt; state fingerprints reject stale results. [@claim:clm_1bc37a795fdb42e459d031a010e8591c0e5fcc568564d3fbb14ec4854b2c558e]
- The product exposes a CLI (npm package 'agentplane', short alias 'ap') with commands such as init, quickstart, task create/active/advance/run, and evaluator list/show/execute. [@claim:clm_2e7b18cde13b2fde3c6870dc745e92a447b192908aed443020cbfa52828f22b2]
- Projects can store prompt modules under .agentplane/evaluators and run a read-only evaluation episode via 'agentplane evaluator execute <task-id>'; the roadmap plans comparative evaluation and quality gates in a later horizon. [@claim:clm_f7f8893373dca19d9be87d75299a84cd36526429ab714c7958e071998e306cea]
<!-- rcw:end owner=source:src_642751c5f70755e28ae153c6abbd51e2 block=evidence -->

## Researcher notes

