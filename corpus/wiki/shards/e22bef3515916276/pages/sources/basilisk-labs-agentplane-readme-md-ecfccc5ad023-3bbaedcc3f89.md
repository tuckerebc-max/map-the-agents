---
access: public
aliases: []
claim_ids:
- clm_035f0bd1efc93eee97aeeab1f56f08edf6ff5659ec94791467cf1b5fc0792f3a
- clm_1bc37a795fdb42e459d031a010e8591c0e5fcc568564d3fbb14ec4854b2c558e
- clm_2d81e167ba8b55b621418b0ab80a5e452879911a5620eb747ea870975dbf4868
- clm_2e7b18cde13b2fde3c6870dc745e92a447b192908aed443020cbfa52828f22b2
- clm_7e749beadf11d612b477abadf9e8156314497a0196fb978369c541a111167363
- clm_c30a8292f1ebd0534402d3ba77dfd8feeed6a1c60a2492117dd278910b868a7f
- clm_c9e78f670e1e03a49b6aaccc5330333d99c279eadb1e28ff93b53edee1d0e804
- clm_cba1e5b9e301549e54c200b5037d3ff21a08c5bdc889d15715e3c106dc809cec
- clm_d3d6ce3cf3d725e39bc0b89f8f8251a33f4156c463e4909a150d6f99fbb3ffc9
- clm_fbfa6dec6f4134450cc76d2ea796618168bf82593401f626aeb2f955f69afedb
maturity: draft
page_id: pg_e8b51585d5355d8bbee73bbaedcc3f89
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_ff75843e7d71552d85972d208b1065ae
title: basilisk-labs/agentplane/README.md @ ecfccc5ad023
updated_at: '2026-09-14T01:36:43Z'
---

# basilisk-labs/agentplane/README.md @ ecfccc5ad023

<!-- rcw:begin owner=source:src_ff75843e7d71552d85972d208b1065ae block=evidence -->
- Operating state lives in the repository: AGENTS.md/CLAUDE.md as policy gateway, .agentplane/WORKFLOW.md, per-task README and acr.json (Agent Change Record), and pr/ artifacts; an optional Local Context layer adds source-backed repository knowledge. [@claim:clm_035f0bd1efc93eee97aeeab1f56f08edf6ff5659ec94791467cf1b5fc0792f3a]
- A supervisor model prepares a bounded AgentWorkOrder, enforces state and authority preconditions, invokes one specialized semantic role, and records an independent ExecutionReceipt; state fingerprints reject stale results. [@claim:clm_1bc37a795fdb42e459d031a010e8591c0e5fcc568564d3fbb14ec4854b2c558e]
- task advance returns a bounded episode packet containing the objective, writable scope, context, result schema, an exchange.result_path, and an exact exchange.resume_argv command for returning the typed result. [@claim:clm_2d81e167ba8b55b621418b0ab80a5e452879911a5620eb747ea870975dbf4868]
- The product exposes a CLI (npm package 'agentplane', short alias 'ap') with commands such as init, quickstart, task create/active/advance/run, and evaluator list/show/execute. [@claim:clm_2e7b18cde13b2fde3c6870dc745e92a447b192908aed443020cbfa52828f22b2]
- Writable roots and allowed effects for each episode are carried in that episode's WorkOrder, and semantic episodes cannot perform or claim formal lifecycle transitions. [@claim:clm_7e749beadf11d612b477abadf9e8156314497a0196fb978369c541a111167363]
- The project is pre-1.0 and under active development; the README advises pinning the CLI version in automation and reviewing release notes when upgrading. [@claim:clm_c30a8292f1ebd0534402d3ba77dfd8feeed6a1c60a2492117dd278910b868a7f]
- The CLI requires Node.js 24+ and Git, is distributed via npm, and is MIT licensed. [@claim:clm_c9e78f670e1e03a49b6aaccc5330333d99c279eadb1e28ff93b53edee1d0e804]
- The control loop issues a bounded semantic episode, the agent returns a semantic result, and the CLI observes facts, runs the formal route, records evidence, and stops at approval, recovery, or verified completion. [@claim:clm_cba1e5b9e301549e54c200b5037d3ff21a08c5bdc889d15715e3c106dc809cec]
- Two workflow modes are offered: 'direct' for lighter local routes and 'branch_pr' for worktrees, branches, PR artifacts, and hosted checks; the agent declares a preferred mode but Agentplane can strengthen the route based on observed work. [@claim:clm_d3d6ce3cf3d725e39bc0b89f8f8251a33f4156c463e4909a150d6f99fbb3ffc9]
- The design separates semantic judgment (agents) from mechanically authoritative workflow mechanics (CLI), with the CLI resolving authority, transitions, routing, schemas, and stop conditions in code rather than by model guesses. [@claim:clm_fbfa6dec6f4134450cc76d2ea796618168bf82593401f626aeb2f955f69afedb]
<!-- rcw:end owner=source:src_ff75843e7d71552d85972d208b1065ae block=evidence -->

## Researcher notes

