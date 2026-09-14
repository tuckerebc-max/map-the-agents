---
access: public
aliases: []
claim_ids:
- clm_1acd9739e57a064b485bd19f156b5419178846af13464452495d41b9c85f9c08
- clm_1c0982328557c797273d1738618266d07074dd42a3e37ed058b3b50e31e6d8fd
- clm_3cb98631c03fcb2b1556c1b93a2bedd6f431f8d5d2155750a63a3c55fd15c637
- clm_3fc58f555374c73ba3593a36b58c429093665a06e18105fa687d178ea654f010
- clm_7c06879da3b4891c713f59e5490bae36fe4aab8287854faf5f9d42bf25c35d9e
- clm_82581b1582d7667b196012cb16fa81d864344db38de083cb8979b582a32eb87b
- clm_9c2e691b4bd5850923f0c27528ee0e6aa4d0b68ee9419075ca225fba2a3dfcbf
- clm_a3ba2c513f47868d14f2b6b4eff747d2036179598cf9abee9c673560a6068fa8
- clm_a9cf62070de819442d116355e30a898ccbb653a3c9347fc4334913a7de2f37b0
- clm_b4e41cdc9b7c5ad3fc9cd74329ca984b9a373e5a4e8289930c5c3be5ef864de0
- clm_f9e3d7d8905aedd84a24c98a4568e3545b84f73a5ec20252c1965974e3aeb891
maturity: draft
page_id: pg_f2709c074fb55f8fa50f1f761100a75e
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_1a8628246ced568db74fc033ad223936
title: FailproofAI/failproofai/README.md @ 86f80fc59ee1
updated_at: '2026-09-14T03:50:03Z'
---

# FailproofAI/failproofai/README.md @ 86f80fc59ee1

<!-- rcw:begin owner=source:src_1a8628246ced568db74fc033ad223936 block=evidence -->
- Repository development practice: contributors must run 'bun install && bun run build' before starting, because the repo runs failproofai's own hooks on itself and they resolve the import against the compiled dist/ bundle. [@claim:clm_1acd9739e57a064b485bd19f156b5419178846af13464452495d41b9c85f9c08]
- Custom policies are JS files dropped into .failproofai/policies/ that load automatically without flags, and can be committed so the whole team receives them on pull. [@claim:clm_1c0982328557c797273d1738618266d07074dd42a3e37ed058b3b50e31e6d8fd]
- Agents outside supported harnesses can report via a Python SDK providing tracing, sessions and audits; enforcement there requires a hook in the user's own runtime. [@claim:clm_3cb98631c03fcb2b1556c1b93a2bedd6f431f8d5d2155750a63a3c55fd15c637]
- A hosted observability product offers fleet-wide runs, execution graphs with parallel sub-agent lanes, latency percentiles, per-model cost tracking, SQL over traces, scheduled audits, and Slack/email/webhook alerts; self-hosting is Enterprise-only. [@claim:clm_3fc58f555374c73ba3593a36b58c429093665a06e18105fa687d178ea654f010]
- The package is distributed via npm as failproofai and installed globally with npm install -g; the project is written in TypeScript per its Trendshift badge. [@claim:clm_7c06879da3b4891c713f59e5490bae36fe4aab8287854faf5f9d42bf25c35d9e]
- 39 built-in policies ship with the tool and activate immediately on install; examples include blocking .env reads, sudo, rm -rf, force pushes, destructive SQL, and unreviewed terraform/kubectl changes. [@claim:clm_82581b1582d7667b196012cb16fa81d864344db38de083cb8979b582a32eb87b]
- The tool is licensed under MIT plus the Commons Clause: free for internal and personal use, but commercial resale of failproofai itself requires a separate agreement. [@claim:clm_9c2e691b4bd5850923f0c27528ee0e6aa4d0b68ee9419075ca225fba2a3dfcbf]
- The product hooks into 12 agent harnesses in two classes: ten coding CLIs (e.g. Claude Code, Codex) and two chat/assistant gateways (Hermes, OpenClaw), with the same events and policies across them. [@claim:clm_a3ba2c513f47868d14f2b6b4eff747d2036179598cf9abee9c673560a6068fa8]
- Running failproofai with no arguments serves a local dashboard on localhost:8020 reading existing run history with no account or data leaving the machine; an audit command scans history for risky patterns and suggests policies. [@claim:clm_a9cf62070de819442d116355e30a898ccbb653a3c9347fc4334913a7de2f37b0]
- Policies return one of three decisions: allow() permits the operation, deny(message) blocks it and returns the message to the agent, and instruct(message) lets it pass while adding context to the agent's next prompt. [@claim:clm_b4e41cdc9b7c5ad3fc9cd74329ca984b9a373e5a4e8289930c5c3be5ef864de0]
- Custom policies are registered via a customPolicies.add() API from the failproofai package, matching events such as PreToolUse and receiving a context with tool input. [@claim:clm_f9e3d7d8905aedd84a24c98a4568e3545b84f73a5ec20252c1965974e3aeb891]
<!-- rcw:end owner=source:src_1a8628246ced568db74fc033ad223936 block=evidence -->

## Researcher notes

