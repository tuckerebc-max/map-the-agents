---
access: public
aliases: []
claim_ids:
- clm_15a63447d967a606bc5c76e6ef7b41bea5d357a74ec95e612d05a22addcd95d7
- clm_19d16fc3eed3a74fe5aa8ab417765ed6b55fdbddf11ea0c9477f2e3804b6d461
- clm_22913fc9380dc88e10656c0d72b8e2f98434dbe710ad9124bb58f5684c907b20
- clm_23e6a84256505495090b9aeae1b03c516f193e0bc1653cf4d3a688778e79214f
- clm_29e63738ba42a86cb835c97cc85c5529d371a68cb4e91697ee630f49eac035dc
- clm_75deef1acefc2a0832c6825d24a251d9f426b3839bf279e076183a8a6ed810ed
- clm_ac0e3569366ae30daaae55e550182ccc2f80b45025667969eca53471c260cc92
- clm_db87ddd91a25d7a744e6ba4bdb4aec304e6c0e477b75a2a1ff3d8cd328652708
- clm_e6afb2e8f6c0156b8d559c053f67c7e85152f398eb4d20a36c1ca85fddb43b4d
- clm_f75c028f5f61cf41f6187459b394feb7c3bf5006377793af43235cbb3a9aabfb
- clm_fd0693d501d68ee4c34de0a095b0e028adf606970f64c7503cca806342b66218
maturity: draft
page_id: pg_7141993ff3595c219cf2498e26522b58
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_f5aca28d20435bad9211aa6f4356a910
title: 2389-research/simmer/README.md @ 73089c6f2224
updated_at: '2026-09-14T03:29:51Z'
---

# 2389-research/simmer/README.md @ 73089c6f2224

<!-- rcw:begin owner=source:src_f5aca28d20435bad9211aa6f4356a910 block=evidence -->
- In workspace mode, each iteration is snapshotted as a git commit, enabling diffing and rollback via git checkout to the best iteration's commit; single-file mode instead writes iteration-N-candidate.md files. [@claim:clm_15a63447d967a606bc5c76e6ef7b41bea5d357a74ec95e612d05a22addcd95d7]
- Simmer auto-selects between a single judge and a multi-judge board based on complexity (e.g., ≤2 criteria vs. code or pipelines), and offers upgrading to the board mid-run if a single-judge run plateaus for 3 iterations. [@claim:clm_19d16fc3eed3a74fe5aa8ab417765ed6b55fdbddf11ea0c9477f2e3804b6d461]
- The reflect subskill tracks the best candidate seen so far; if an iteration regresses, the best-so-far is preserved and the final result.md contains the highest-scoring candidate rather than the latest one. [@claim:clm_22913fc9380dc88e10656c0d72b8e2f98434dbe710ad9124bb58f5684c907b20]
- Installation is via Claude Code plugin marketplace commands: adding the 2389-research/claude-plugins marketplace and installing simmer@2389-research. [@claim:clm_23e6a84256505495090b9aeae1b03c516f193e0bc1653cf4d3a688778e79214f]
- Each iteration targets one direction via ASI (Actionable Side Information), the single highest-leverage fix; for workspace targets this becomes one coherent multi-file direction rather than unrelated changes. [@claim:clm_29e63738ba42a86cb835c97cc85c5529d371a68cb4e91697ee630f49eac035dc]
- Default iteration count is 3 rounds per batch, after which the tool asks whether to continue; users can request a specific count or stop early at any prompt. [@claim:clm_75deef1acefc2a0832c6825d24a251d9f426b3839bf279e076183a8a6ed810ed]
- Three evaluation modes are supported: judge-only (default, for text artifacts), runnable (judge interprets a script's output), and hybrid (both). There is no format contract on evaluator output; the judge reads whatever the script produces. [@claim:clm_ac0e3569366ae30daaae55e550182ccc2f80b45025667969eca53471c260cc92]
- Context isolation is a stated design principle: the generator does not see scores and the judge does not see previous scores, so each role gets only the context it needs to avoid bias. [@claim:clm_db87ddd91a25d7a744e6ba4bdb4aec304e6c0e477b75a2a1ff3d8cd328652708]
- Simmer belongs to the test-kitchen skill family but is independently installable, alongside cookoff (parallel implementation competition) and omakase-off (parallel design exploration); simmer is the serial-iteration counterpart. [@claim:clm_e6afb2e8f6c0156b8d559c053f67c7e85152f398eb4d20a36c1ca85fddb43b4d]
- The skill is triggered by natural-language phrases such as 'simmer this', 'refine this', 'hone this', or 'polish this'; any request to iteratively improve an artifact starts the loop. [@claim:clm_f75c028f5f61cf41f6187459b394feb7c3bf5006377793af43235cbb3a9aabfb]
- The plugin ships one skill (simmer) with four subskills running the loop: Setup (identify artifact, elicit criteria), Generator (improve from ASI), Judge (score 1-10 per criterion, produce ASI), and Reflect (record trajectory, track best candidate). [@claim:clm_fd0693d501d68ee4c34de0a095b0e028adf606970f64c7503cca806342b66218]
<!-- rcw:end owner=source:src_f5aca28d20435bad9211aa6f4356a910 block=evidence -->

## Researcher notes

