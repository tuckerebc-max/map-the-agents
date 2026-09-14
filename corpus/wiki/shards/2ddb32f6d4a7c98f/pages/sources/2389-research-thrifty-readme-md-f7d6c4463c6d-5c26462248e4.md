---
access: public
aliases: []
claim_ids:
- clm_0d22e1cd0e03a3b3282d9198349a59975552e708ee2572550818b6fcc61dfcb4
- clm_2fa35724d27f405e600481dd18aba87b7d22d3dd7a71fdee8f0f3388eb7276f3
- clm_353a15c273003ed6bc0a8531189294e598af3e99fcbf787ea1f93b8e3f89fd42
- clm_4349eb8d1acccfe0c7179cb1c8621b8d95d1f9e7d898265ae010d3784090668b
- clm_441ddfefd9d678ec632cecefb19d0bdd3d4a10b7e62941a46fdfe822f107309e
- clm_a73ec95d2b9d973887323b5336ef2386d1e438db2e70bb4b9e78586ef777305a
- clm_b05e8fba92a522a56957765172c6940fe881ae06f72005244ff21dc9f8937dc4
- clm_bb231c1945669950152dff2457d2d71bcdaa111c96580a71c641b19715aa051e
- clm_c04fb626212fc5561db71551095cc61f7d00e9dfc1c46c10ca80a05eea2e1ef1
- clm_caf64bb1bd518bd5a1f8b37466930885ef5d245def9480aded31afd14c68f62f
- clm_e0377273fce875b241edf866eda8db47085bb257dfd98e63c08377265771c865
- clm_eab430e721c1e70b7353787f380ef995830f7e9dda9d353e5140bece88198282
- clm_eb606ce0c67baaba579e2f6b08ab5a7af068859f2896bc960eb946f2543953f7
- clm_fa26fbe7781addc61ab981fb7fb788e36ad508049d1e02f83191a2f786e3c1f7
maturity: draft
page_id: pg_608afa1e4c6659b8b8345c26462248e4
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_f818c182c7b35646840aad704c826852
title: 2389-research/thrifty/README.md @ f7d6c4463c6d
updated_at: '2026-09-14T03:29:52Z'
---

# 2389-research/thrifty/README.md @ f7d6c4463c6d

<!-- rcw:begin owner=source:src_f818c182c7b35646840aad704c826852 block=evidence -->
- On trivial builds the planning overhead makes thrifty cost more than a single capable agent, so there is a crossover below which one strong model should be used directly. [@claim:clm_0d22e1cd0e03a3b3282d9198349a59975552e708ee2572550818b6fcc61dfcb4]
- The lean dispatch flow uses dispatch.py to run bare claude -p calls that hard-pin every codegen sprint to Haiku regardless of the plan's tier, writing outputs to disk while the orchestrator reads only a tiny manifest. [@claim:clm_2fa35724d27f405e600481dd18aba87b7d22d3dd7a71fdee8f0f3388eb7276f3]
- The README reports the dispatch flow is about 64% cheaper than Opus building the same spec at equal gate quality, benchmarked across 7 tasks spanning JS, Python, Go, and prose, with results in eval/RESULTS.md and scripts in experiments/. [@claim:clm_353a15c273003ed6bc0a8531189294e598af3e99fcbf787ea1f93b8e3f89fd42]
- Repository development practice: contributors can hack locally by symlinking the skills directories into ~/.claude/skills/ instead of installing the plugin. [@claim:clm_4349eb8d1acccfe0c7179cb1c8621b8d95d1f9e7d898265ae010d3784090668b]
- Core philosophy: concentrate planning in a strong model and push execution to a cheap one, with a gate (tests/checklist) re-run independently rather than self-reported as the trust contract. [@claim:clm_441ddfefd9d678ec632cecefb19d0bdd3d4a10b7e62941a46fdfe822f107309e]
- Verification is adaptive: runnable criteria are checked by re-running the gate at no model cost; Sonnet checkers are spent only on gate failures or assertional criteria such as prose and design quality. [@claim:clm_a73ec95d2b9d973887323b5336ef2386d1e438db2e70bb4b9e78586ef777305a]
- In the subagent flow the executor model cannot be forced in code; a runtime may silently ignore the requested Haiku model, self-reported model is a weak signal, and observed cost/usage is the authoritative check. [@claim:clm_b05e8fba92a522a56957765172c6940fe881ae06f72005244ff21dc9f8937dc4]
- The planner (Sonnet) writes a contract plus sprints.jsonl with one self-contained unit of work per sprint, pinning cross-sprint and genuinely ambiguous decisions so the executor never invents system-level choices. [@claim:clm_bb231c1945669950152dff2457d2d71bcdaa111c96580a71c641b19715aa051e]
- The fix loop is bounded: up to 2 surgical Sonnet fixes, 1 executor redo with fresh Haiku, 1 architect replan, then escalation to the human; a regression guard rolls back fixes that break previously-passing criteria. [@claim:clm_c04fb626212fc5561db71551095cc61f7d00e9dfc1c46c10ca80a05eea2e1ef1]
- thrifty installs as a Claude Code plugin via /plugin marketplace add 2389-research/thrifty and /plugin install thrifty@thrifty, triggered by phrases like 'thrifty', 'delegate this', or 'tiered build'. [@claim:clm_caf64bb1bd518bd5a1f8b37466930885ef5d245def9480aded31afd14c68f62f]
- The plugin bundles six skills: thrifty and thrifty-dispatch (orchestrators), thrifty-plan (Sonnet), thrifty-brief (Sonnet, split tier), thrifty-execute (Haiku), and thrifty-check (Sonnet), with orchestrators running in-session. [@claim:clm_e0377273fce875b241edf866eda8db47085bb257dfd98e63c08377265771c865]
- The architect picks a decomposition mode by artifact cohesion: partition (parallel separate regions), relay (sequential shared artifact), or layered (sequential role-specialized passes). [@claim:clm_eab430e721c1e70b7353787f380ef995830f7e9dda9d353e5140bece88198282]
- Run artifacts (CONTRACT.md, briefs/, LEDGER.md) are written under docs/thrifty/<task-slug>/ so a run is auditable and resumable. [@claim:clm_eb606ce0c67baaba579e2f6b08ab5a7af068859f2896bc960eb946f2543953f7]
- The subagent-based skills need no external runtime, but the lean thrifty-dispatch flow shells out to dispatch.py and additionally requires Python 3 on PATH. [@claim:clm_fa26fbe7781addc61ab981fb7fb788e36ad508049d1e02f83191a2f786e3c1f7]
<!-- rcw:end owner=source:src_f818c182c7b35646840aad704c826852 block=evidence -->

## Researcher notes

