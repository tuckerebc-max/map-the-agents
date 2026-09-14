# 2389-research/simmer -- full detail

[Back to orientation](simmer.md)

## Origins

- alltheagents.org-site-pages

## Projects

- Observatory

Full evidence record (JSON): [wiki/dossiers/2389-research/simmer/73089c6f2224b2379ceb177ee511eca7c4c4ef79/0c3030b83e9b2b41.json](../../../wiki/dossiers/2389-research/simmer/73089c6f2224b2379ceb177ee511eca7c4c4ef79/0c3030b83e9b2b41.json)

## specifications (1 claim(s))

- [observation/documented] The v2 design spec extends the refinement loop with pluggable evaluation, multi-file workspace targets, expanded ASI, and background constraints; all additions are opt-in and default behavior matches v1. -- evidence: [docs/specs/2026-03-16-simmer-v2-design.md#L5-L5](https://github.com/2389-research/simmer/blob/73089c6f2224b2379ceb177ee511eca7c4c4ef79/docs/specs/2026-03-16-simmer-v2-design.md#L5-L5) (`clm_f293ce370837c3c5494befae45ffd49835a60461c28f0d1c9134fff2e0662213`)

## components (1 claim(s))

- [observation/documented] The plugin ships one skill (simmer) with four subskills running the loop: Setup (identify artifact, elicit criteria), Generator (improve from ASI), Judge (score 1-10 per criterion, produce ASI), and Reflect (record trajectory, track best candidate). -- evidence: [README.md#L20-L23](https://github.com/2389-research/simmer/blob/73089c6f2224b2379ceb177ee511eca7c4c4ef79/README.md#L20-L23), [README.md#L18-L18](https://github.com/2389-research/simmer/blob/73089c6f2224b2379ceb177ee511eca7c4c4ef79/README.md#L18-L18) (`clm_fd0693d501d68ee4c34de0a095b0e028adf606970f64c7503cca806342b66218`)

## design-choices (3 claim(s))

- [observation/documented] Context isolation is a stated design principle: the generator does not see scores and the judge does not see previous scores, so each role gets only the context it needs to avoid bias. -- evidence: [README.md#L178-L180](https://github.com/2389-research/simmer/blob/73089c6f2224b2379ceb177ee511eca7c4c4ef79/README.md#L178-L180) (`clm_db87ddd91a25d7a744e6ba4bdb4aec304e6c0e477b75a2a1ff3d8cd328652708`)
- [observation/documented] Each iteration targets one direction via ASI (Actionable Side Information), the single highest-leverage fix; for workspace targets this becomes one coherent multi-file direction rather than unrelated changes. -- evidence: [README.md#L20-L23](https://github.com/2389-research/simmer/blob/73089c6f2224b2379ceb177ee511eca7c4c4ef79/README.md#L20-L23), [docs/specs/2026-03-16-simmer-v2-design.md#L55-L55](https://github.com/2389-research/simmer/blob/73089c6f2224b2379ceb177ee511eca7c4c4ef79/docs/specs/2026-03-16-simmer-v2-design.md#L55-L55), [docs/specs/2026-03-16-simmer-v2-design.md#L49-L53](https://github.com/2389-research/simmer/blob/73089c6f2224b2379ceb177ee511eca7c4c4ef79/docs/specs/2026-03-16-simmer-v2-design.md#L49-L53) (`clm_29e63738ba42a86cb835c97cc85c5529d371a68cb4e91697ee630f49eac035dc`)
- [observation/documented] Default iteration count is 3 rounds per batch, after which the tool asks whether to continue; users can request a specific count or stop early at any prompt. -- evidence: [README.md#L135-L135](https://github.com/2389-research/simmer/blob/73089c6f2224b2379ceb177ee511eca7c4c4ef79/README.md#L135-L135) (`clm_75deef1acefc2a0832c6825d24a251d9f426b3839bf279e076183a8a6ed810ed`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] Installation is via Claude Code plugin marketplace commands: adding the 2389-research/claude-plugins marketplace and installing simmer@2389-research. -- evidence: [README.md#L11-L14](https://github.com/2389-research/simmer/blob/73089c6f2224b2379ceb177ee511eca7c4c4ef79/README.md#L11-L14) (`clm_23e6a84256505495090b9aeae1b03c516f193e0bc1653cf4d3a688778e79214f`)
- [observation/documented] The skill is triggered by natural-language phrases such as 'simmer this', 'refine this', 'hone this', or 'polish this'; any request to iteratively improve an artifact starts the loop. -- evidence: [README.md#L29-L29](https://github.com/2389-research/simmer/blob/73089c6f2224b2379ceb177ee511eca7c4c4ef79/README.md#L29-L29), [README.md#L31-L31](https://github.com/2389-research/simmer/blob/73089c6f2224b2379ceb177ee511eca7c4c4ef79/README.md#L31-L31) (`clm_f75c028f5f61cf41f6187459b394feb7c3bf5006377793af43235cbb3a9aabfb`)

## memory-state (2 claim(s))

- [observation/documented] The reflect subskill tracks the best candidate seen so far; if an iteration regresses, the best-so-far is preserved and the final result.md contains the highest-scoring candidate rather than the latest one. -- evidence: [README.md#L137-L137](https://github.com/2389-research/simmer/blob/73089c6f2224b2379ceb177ee511eca7c4c4ef79/README.md#L137-L137) (`clm_22913fc9380dc88e10656c0d72b8e2f98434dbe710ad9124bb58f5684c907b20`)
- [observation/documented] In workspace mode, each iteration is snapshotted as a git commit, enabling diffing and rollback via git checkout to the best iteration's commit; single-file mode instead writes iteration-N-candidate.md files. -- evidence: [README.md#L141-L148](https://github.com/2389-research/simmer/blob/73089c6f2224b2379ceb177ee511eca7c4c4ef79/README.md#L141-L148), [docs/specs/2026-03-16-simmer-v2-design.md#L65-L65](https://github.com/2389-research/simmer/blob/73089c6f2224b2379ceb177ee511eca7c4c4ef79/docs/specs/2026-03-16-simmer-v2-design.md#L65-L65), [README.md#L174-L174](https://github.com/2389-research/simmer/blob/73089c6f2224b2379ceb177ee511eca7c4c4ef79/README.md#L174-L174), [docs/specs/2026-03-16-simmer-v2-design.md#L59-L63](https://github.com/2389-research/simmer/blob/73089c6f2224b2379ceb177ee511eca7c4c4ef79/docs/specs/2026-03-16-simmer-v2-design.md#L59-L63) (`clm_15a63447d967a606bc5c76e6ef7b41bea5d357a74ec95e612d05a22addcd95d7`)

## orchestration (1 claim(s))

- [observation/documented] Simmer auto-selects between a single judge and a multi-judge board based on complexity (e.g., ≤2 criteria vs. code or pipelines), and offers upgrading to the board mid-run if a single-judge run plateaus for 3 iterations. -- evidence: [README.md#L121-L121](https://github.com/2389-research/simmer/blob/73089c6f2224b2379ceb177ee511eca7c4c4ef79/README.md#L121-L121), [README.md#L130-L130](https://github.com/2389-research/simmer/blob/73089c6f2224b2379ceb177ee511eca7c4c4ef79/README.md#L130-L130), [README.md#L123-L124](https://github.com/2389-research/simmer/blob/73089c6f2224b2379ceb177ee511eca7c4c4ef79/README.md#L123-L124) (`clm_19d16fc3eed3a74fe5aa8ab417765ed6b55fdbddf11ea0c9477f2e3804b6d461`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (1 claim(s))

- [observation/documented] Three evaluation modes are supported: judge-only (default, for text artifacts), runnable (judge interprets a script's output), and hybrid (both). There is no format contract on evaluator output; the judge reads whatever the script produces. -- evidence: [docs/specs/2026-03-16-simmer-v2-design.md#L45-L45](https://github.com/2389-research/simmer/blob/73089c6f2224b2379ceb177ee511eca7c4c4ef79/docs/specs/2026-03-16-simmer-v2-design.md#L45-L45), [docs/specs/2026-03-16-simmer-v2-design.md#L39-L43](https://github.com/2389-research/simmer/blob/73089c6f2224b2379ceb177ee511eca7c4c4ef79/docs/specs/2026-03-16-simmer-v2-design.md#L39-L43), [README.md#L111-L115](https://github.com/2389-research/simmer/blob/73089c6f2224b2379ceb177ee511eca7c4c4ef79/README.md#L111-L115), [README.md#L117-L117](https://github.com/2389-research/simmer/blob/73089c6f2224b2379ceb177ee511eca7c4c4ef79/README.md#L117-L117) (`clm_ac0e3569366ae30daaae55e550182ccc2f80b45025667969eca53471c260cc92`)

## dependencies (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (1 claim(s))

- [observation/documented] Simmer belongs to the test-kitchen skill family but is independently installable, alongside cookoff (parallel implementation competition) and omakase-off (parallel design exploration); simmer is the serial-iteration counterpart. -- evidence: [README.md#L186-L189](https://github.com/2389-research/simmer/blob/73089c6f2224b2379ceb177ee511eca7c4c4ef79/README.md#L186-L189), [README.md#L41-L41](https://github.com/2389-research/simmer/blob/73089c6f2224b2379ceb177ee511eca7c4c4ef79/README.md#L41-L41), [README.md#L35-L39](https://github.com/2389-research/simmer/blob/73089c6f2224b2379ceb177ee511eca7c4c4ef79/README.md#L35-L39) (`clm_e6afb2e8f6c0156b8d559c053f67c7e85152f398eb4d20a36c1ca85fddb43b4d`)

