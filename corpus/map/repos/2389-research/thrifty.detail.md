# 2389-research/thrifty -- full detail

[Back to orientation](thrifty.md)

## Origins

- alltheagents.org-site-pages

## Projects

- Observatory

Full evidence record (JSON): [wiki/dossiers/2389-research/thrifty/f7d6c4463c6de7fc63933e3d23775f917e2f7865/e5c1fe9c72e06cb4.json](../../../wiki/dossiers/2389-research/thrifty/f7d6c4463c6de7fc63933e3d23775f917e2f7865/e5c1fe9c72e06cb4.json)

## specifications (1 claim(s))

- [observation/documented] The planner (Sonnet) writes a contract plus sprints.jsonl with one self-contained unit of work per sprint, pinning cross-sprint and genuinely ambiguous decisions so the executor never invents system-level choices. -- evidence: [README.md#L22-L32](https://github.com/2389-research/thrifty/blob/f7d6c4463c6de7fc63933e3d23775f917e2f7865/README.md#L22-L32), [README.md#L34-L41](https://github.com/2389-research/thrifty/blob/f7d6c4463c6de7fc63933e3d23775f917e2f7865/README.md#L34-L41) (`clm_bb231c1945669950152dff2457d2d71bcdaa111c96580a71c641b19715aa051e`)

## components (2 claim(s))

- [observation/documented] The plugin bundles six skills: thrifty and thrifty-dispatch (orchestrators), thrifty-plan (Sonnet), thrifty-brief (Sonnet, split tier), thrifty-execute (Haiku), and thrifty-check (Sonnet), with orchestrators running in-session. -- evidence: [README.md#L45-L45](https://github.com/2389-research/thrifty/blob/f7d6c4463c6de7fc63933e3d23775f917e2f7865/README.md#L45-L45), [README.md#L86-L93](https://github.com/2389-research/thrifty/blob/f7d6c4463c6de7fc63933e3d23775f917e2f7865/README.md#L86-L93) (`clm_e0377273fce875b241edf866eda8db47085bb257dfd98e63c08377265771c865`)
- [observation/documented] The lean dispatch flow uses dispatch.py to run bare claude -p calls that hard-pin every codegen sprint to Haiku regardless of the plan's tier, writing outputs to disk while the orchestrator reads only a tiny manifest. -- evidence: [README.md#L186-L193](https://github.com/2389-research/thrifty/blob/f7d6c4463c6de7fc63933e3d23775f917e2f7865/README.md#L186-L193) (`clm_2fa35724d27f405e600481dd18aba87b7d22d3dd7a71fdee8f0f3388eb7276f3`)

## design-choices (1 claim(s))

- [observation/documented] Core philosophy: concentrate planning in a strong model and push execution to a cheap one, with a gate (tests/checklist) re-run independently rather than self-reported as the trust contract. -- evidence: [README.md#L11-L14](https://github.com/2389-research/thrifty/blob/f7d6c4463c6de7fc63933e3d23775f917e2f7865/README.md#L11-L14) (`clm_441ddfefd9d678ec632cecefb19d0bdd3d4a10b7e62941a46fdfe822f107309e`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: the project follows SemVer with the version in .claude-plugin/plugin.json as source of truth, and every release bumps it so /plugin installs pick up changes cleanly. -- evidence: [CHANGELOG.md#L3-L5](https://github.com/2389-research/thrifty/blob/f7d6c4463c6de7fc63933e3d23775f917e2f7865/CHANGELOG.md#L3-L5) (`clm_23fdabe6257e0e5116c77c4805a98c88db5786313a6c22d9927b086755fcdf02`)
- [observation/documented] Repository development practice: contributors can hack locally by symlinking the skills directories into ~/.claude/skills/ instead of installing the plugin. -- evidence: [README.md#L59-L59](https://github.com/2389-research/thrifty/blob/f7d6c4463c6de7fc63933e3d23775f917e2f7865/README.md#L59-L59), [README.md#L61-L63](https://github.com/2389-research/thrifty/blob/f7d6c4463c6de7fc63933e3d23775f917e2f7865/README.md#L61-L63) (`clm_4349eb8d1acccfe0c7179cb1c8621b8d95d1f9e7d898265ae010d3784090668b`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] thrifty installs as a Claude Code plugin via /plugin marketplace add 2389-research/thrifty and /plugin install thrifty@thrifty, triggered by phrases like 'thrifty', 'delegate this', or 'tiered build'. -- evidence: [README.md#L52-L52](https://github.com/2389-research/thrifty/blob/f7d6c4463c6de7fc63933e3d23775f917e2f7865/README.md#L52-L52), [README.md#L47-L50](https://github.com/2389-research/thrifty/blob/f7d6c4463c6de7fc63933e3d23775f917e2f7865/README.md#L47-L50) (`clm_caf64bb1bd518bd5a1f8b37466930885ef5d245def9480aded31afd14c68f62f`)

## memory-state (1 claim(s))

- [observation/documented] Run artifacts (CONTRACT.md, briefs/, LEDGER.md) are written under docs/thrifty/<task-slug>/ so a run is auditable and resumable. -- evidence: [README.md#L143-L144](https://github.com/2389-research/thrifty/blob/f7d6c4463c6de7fc63933e3d23775f917e2f7865/README.md#L143-L144) (`clm_eb606ce0c67baaba579e2f6b08ab5a7af068859f2896bc960eb946f2543953f7`)

## orchestration (3 claim(s))

- [observation/documented] Verification is adaptive: runnable criteria are checked by re-running the gate at no model cost; Sonnet checkers are spent only on gate failures or assertional criteria such as prose and design quality. -- evidence: [README.md#L140-L141](https://github.com/2389-research/thrifty/blob/f7d6c4463c6de7fc63933e3d23775f917e2f7865/README.md#L140-L141), [README.md#L133-L138](https://github.com/2389-research/thrifty/blob/f7d6c4463c6de7fc63933e3d23775f917e2f7865/README.md#L133-L138) (`clm_a73ec95d2b9d973887323b5336ef2386d1e438db2e70bb4b9e78586ef777305a`)
- [observation/documented] The fix loop is bounded: up to 2 surgical Sonnet fixes, 1 executor redo with fresh Haiku, 1 architect replan, then escalation to the human; a regression guard rolls back fixes that break previously-passing criteria. -- evidence: [README.md#L166-L169](https://github.com/2389-research/thrifty/blob/f7d6c4463c6de7fc63933e3d23775f917e2f7865/README.md#L166-L169), [README.md#L163-L164](https://github.com/2389-research/thrifty/blob/f7d6c4463c6de7fc63933e3d23775f917e2f7865/README.md#L163-L164), [README.md#L171-L171](https://github.com/2389-research/thrifty/blob/f7d6c4463c6de7fc63933e3d23775f917e2f7865/README.md#L171-L171) (`clm_c04fb626212fc5561db71551095cc61f7d00e9dfc1c46c10ca80a05eea2e1ef1`)
- [observation/documented] The architect picks a decomposition mode by artifact cohesion: partition (parallel separate regions), relay (sequential shared artifact), or layered (sequential role-specialized passes). -- evidence: [README.md#L151-L156](https://github.com/2389-research/thrifty/blob/f7d6c4463c6de7fc63933e3d23775f917e2f7865/README.md#L151-L156), [README.md#L148-L149](https://github.com/2389-research/thrifty/blob/f7d6c4463c6de7fc63933e3d23775f917e2f7865/README.md#L148-L149) (`clm_eab430e721c1e70b7353787f380ef995830f7e9dda9d353e5140bece88198282`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (1 claim(s))

- [observation/documented] The README reports the dispatch flow is about 64% cheaper than Opus building the same spec at equal gate quality, benchmarked across 7 tasks spanning JS, Python, Go, and prose, with results in eval/RESULTS.md and scripts in experiments/. -- evidence: [README.md#L3-L5](https://github.com/2389-research/thrifty/blob/f7d6c4463c6de7fc63933e3d23775f917e2f7865/README.md#L3-L5), [README.md#L210-L213](https://github.com/2389-research/thrifty/blob/f7d6c4463c6de7fc63933e3d23775f917e2f7865/README.md#L210-L213), [README.md#L18-L20](https://github.com/2389-research/thrifty/blob/f7d6c4463c6de7fc63933e3d23775f917e2f7865/README.md#L18-L20) (`clm_353a15c273003ed6bc0a8531189294e598af3e99fcbf787ea1f93b8e3f89fd42`)

## dependencies (1 claim(s))

- [observation/documented] The subagent-based skills need no external runtime, but the lean thrifty-dispatch flow shells out to dispatch.py and additionally requires Python 3 on PATH. -- evidence: [README.md#L54-L57](https://github.com/2389-research/thrifty/blob/f7d6c4463c6de7fc63933e3d23775f917e2f7865/README.md#L54-L57) (`clm_fa26fbe7781addc61ab981fb7fb788e36ad508049d1e02f83191a2f786e3c1f7`)

## limitations (2 claim(s))

- [observation/documented] On trivial builds the planning overhead makes thrifty cost more than a single capable agent, so there is a crossover below which one strong model should be used directly. -- evidence: [README.md#L34-L41](https://github.com/2389-research/thrifty/blob/f7d6c4463c6de7fc63933e3d23775f917e2f7865/README.md#L34-L41), [README.md#L116-L122](https://github.com/2389-research/thrifty/blob/f7d6c4463c6de7fc63933e3d23775f917e2f7865/README.md#L116-L122) (`clm_0d22e1cd0e03a3b3282d9198349a59975552e708ee2572550818b6fcc61dfcb4`)
- [observation/documented] In the subagent flow the executor model cannot be forced in code; a runtime may silently ignore the requested Haiku model, self-reported model is a weak signal, and observed cost/usage is the authoritative check. -- evidence: [README.md#L200-L206](https://github.com/2389-research/thrifty/blob/f7d6c4463c6de7fc63933e3d23775f917e2f7865/README.md#L200-L206) (`clm_b05e8fba92a522a56957765172c6940fe881ae06f72005244ff21dc9f8937dc4`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

