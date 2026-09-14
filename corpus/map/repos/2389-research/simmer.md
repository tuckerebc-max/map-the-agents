# 2389-research/simmer

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-site-pages - Projects: Observatory
Latest snapshot: commit 73089c6f2224 @ 0c3030b83e9b2b41

## Summary (orientation draft, not independently verified)

Simmer is a Claude Code plugin providing an iterative, criteria-driven artifact refinement skill with four subskills (Setup, Generator, Judge, Reflect), three evaluation modes, single-file and workspace modes, and judge-board auto-selection. Evidence is documentation (README and a v2 design spec); no source code slices are present.

## Source coverage

Source coverage (complete): 3 of 3 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] The v2 design spec extends the refinement loop with pluggable evaluation, multi-file workspace targets, expanded ASI, and background constraints; all additions are opt-in and default behavior matches v1. -- evidence: [docs/specs/2026-03-16-simmer-v2-design.md#L5-L5](https://github.com/2389-research/simmer/blob/73089c6f2224b2379ceb177ee511eca7c4c4ef79/docs/specs/2026-03-16-simmer-v2-design.md#L5-L5)
- components (1 claim(s)):
  - [observation/documented] The plugin ships one skill (simmer) with four subskills running the loop: Setup (identify artifact, elicit criteria), Generator (improve from ASI), Judge (score 1-10 per criterion, produce ASI), and Reflect (record trajectory, track best candidate). -- evidence: [README.md#L20-L23](https://github.com/2389-research/simmer/blob/73089c6f2224b2379ceb177ee511eca7c4c4ef79/README.md#L20-L23), [README.md#L18-L18](https://github.com/2389-research/simmer/blob/73089c6f2224b2379ceb177ee511eca7c4c4ef79/README.md#L18-L18)
- design-choices (3 claim(s)):
  - [observation/documented] Context isolation is a stated design principle: the generator does not see scores and the judge does not see previous scores, so each role gets only the context it needs to avoid bias. -- evidence: [README.md#L178-L180](https://github.com/2389-research/simmer/blob/73089c6f2224b2379ceb177ee511eca7c4c4ef79/README.md#L178-L180)
  - [observation/documented] Each iteration targets one direction via ASI (Actionable Side Information), the single highest-leverage fix; for workspace targets this becomes one coherent multi-file direction rather than unrelated changes. -- evidence: [README.md#L20-L23](https://github.com/2389-research/simmer/blob/73089c6f2224b2379ceb177ee511eca7c4c4ef79/README.md#L20-L23), [docs/specs/2026-03-16-simmer-v2-design.md#L55-L55](https://github.com/2389-research/simmer/blob/73089c6f2224b2379ceb177ee511eca7c4c4ef79/docs/specs/2026-03-16-simmer-v2-design.md#L55-L55), [docs/specs/2026-03-16-simmer-v2-design.md#L49-L53](https://github.com/2389-research/simmer/blob/73089c6f2224b2379ceb177ee511eca7c4c4ef79/docs/specs/2026-03-16-simmer-v2-design.md#L49-L53)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] Installation is via Claude Code plugin marketplace commands: adding the 2389-research/claude-plugins marketplace and installing simmer@2389-research. -- evidence: [README.md#L11-L14](https://github.com/2389-research/simmer/blob/73089c6f2224b2379ceb177ee511eca7c4c4ef79/README.md#L11-L14)
  - [observation/documented] The skill is triggered by natural-language phrases such as 'simmer this', 'refine this', 'hone this', or 'polish this'; any request to iteratively improve an artifact starts the loop. -- evidence: [README.md#L29-L29](https://github.com/2389-research/simmer/blob/73089c6f2224b2379ceb177ee511eca7c4c4ef79/README.md#L29-L29), [README.md#L31-L31](https://github.com/2389-research/simmer/blob/73089c6f2224b2379ceb177ee511eca7c4c4ef79/README.md#L31-L31)
- memory-state (2 claim(s)):
  - [observation/documented] The reflect subskill tracks the best candidate seen so far; if an iteration regresses, the best-so-far is preserved and the final result.md contains the highest-scoring candidate rather than the latest one. -- evidence: [README.md#L137-L137](https://github.com/2389-research/simmer/blob/73089c6f2224b2379ceb177ee511eca7c4c4ef79/README.md#L137-L137)
  - [observation/documented] In workspace mode, each iteration is snapshotted as a git commit, enabling diffing and rollback via git checkout to the best iteration's commit; single-file mode instead writes iteration-N-candidate.md files. -- evidence: [README.md#L141-L148](https://github.com/2389-research/simmer/blob/73089c6f2224b2379ceb177ee511eca7c4c4ef79/README.md#L141-L148), [docs/specs/2026-03-16-simmer-v2-design.md#L65-L65](https://github.com/2389-research/simmer/blob/73089c6f2224b2379ceb177ee511eca7c4c4ef79/docs/specs/2026-03-16-simmer-v2-design.md#L65-L65), [README.md#L174-L174](https://github.com/2389-research/simmer/blob/73089c6f2224b2379ceb177ee511eca7c4c4ef79/README.md#L174-L174), [docs/specs/2026-03-16-simmer-v2-design.md#L59-L63](https://github.com/2389-research/simmer/blob/73089c6f2224b2379ceb177ee511eca7c4c4ef79/docs/specs/2026-03-16-simmer-v2-design.md#L59-L63)
- orchestration (1 claim(s)):
  - [observation/documented] Simmer auto-selects between a single judge and a multi-judge board based on complexity (e.g., ≤2 criteria vs. code or pipelines), and offers upgrading to the board mid-run if a single-judge run plateaus for 3 iterations. -- evidence: [README.md#L121-L121](https://github.com/2389-research/simmer/blob/73089c6f2224b2379ceb177ee511eca7c4c4ef79/README.md#L121-L121), [README.md#L130-L130](https://github.com/2389-research/simmer/blob/73089c6f2224b2379ceb177ee511eca7c4c4ef79/README.md#L130-L130), [README.md#L123-L124](https://github.com/2389-research/simmer/blob/73089c6f2224b2379ceb177ee511eca7c4c4ef79/README.md#L123-L124)
More evidence: [full detail](simmer.detail.md)

Metadata and full claim list: [full detail](simmer.detail.md)
Human notes ([notes](simmer.notes.md), never overwritten by build)

[Back to map index](../../index.md)
