---
access: public
aliases: []
claim_ids:
- clm_2a06be54291ad8e8f48a45d77c98c1e318aeb3d4daae34bf4cbe4d91e04c33c8
- clm_76494216b2d9638e21f750b10066da8acd7f6a890011b1feaa16f3cce557a0af
- clm_9580442f7fc4e840858ffa1cd5551b7f22ed7e7273464f6853da9283fae8ad03
- clm_ced4324c96d04c991d28f75a9df6b3e8cc81e9f67d46374b993bf22e9b2ef2d3
maturity: draft
page_id: pg_e2390c8a5b155eb29dc50bdd0e8c9f95
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_e6e3f52a46b35cb0993f81c369d14447
title: strands-agents/harness-sdk/strands-py/src/strands/agent/_agent_delegation.py
  @ 08ed4cfd3eb4
updated_at: '2026-09-14T04:23:42Z'
---

# strands-agents/harness-sdk/strands-py/src/strands/agent/_agent_delegation.py @ 08ed4cfd3eb4

<!-- rcw:begin owner=source:src_e6e3f52a46b35cb0993f81c369d14447 block=evidence -->
- Delegation enforces a single-call constraint (a delegation tool must be the only tool called in a turn, otherwise the call is cancelled or an error result is returned), and the agent loop exits via end_turn after a successful delegation whose content becomes the final assistant message. [@claim:clm_2a06be54291ad8e8f48a45d77c98c1e318aeb3d4daae34bf4cbe4d91e04c33c8]
- Delegation is incompatible with stateful models: initialization raises ValueError if a delegate=True tool is registered on a stateful model, and at execution time delegation is skipped and the tool runs normally, because early loop exit would leave unclosed function calls server-side. [@claim:clm_76494216b2d9638e21f750b10066da8acd7f6a890011b1feaa16f3cce557a0af]
- Delegation end_turn is skipped when the parent agent expects structured output or when the delegation tool result has no meaningful (blank) content. [@claim:clm_9580442f7fc4e840858ffa1cd5551b7f22ed7e7273464f6853da9283fae8ad03]
- The Python SDK includes an AgentDelegation plugin (auto-registered on every agent) that enforces delegation semantics for tools configured with delegate=True, acting as a no-op when no delegation tools fire. [@claim:clm_ced4324c96d04c991d28f75a9df6b3e8cc81e9f67d46374b993bf22e9b2ef2d3]
<!-- rcw:end owner=source:src_e6e3f52a46b35cb0993f81c369d14447 block=evidence -->

## Researcher notes

