# the-open-engine/zeroshot

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit b550c15279c9 @ 2ab85c8a6208f2d8

## Summary (orientation draft, not independently verified)

Zeroshot turns a software goal into an explicit multi-agent graph: one agent implements, independent agents review, failures route into bounded repair, and delivery happens only after the graph's checks pass. The built-in software-change graph gives the goal to a worker, runs acceptance and code review in parallel, routes rejections to a repair worker with repeated reviews, and delivers accepted changes through Git, CI, and merge, routing delivery conflicts back through repair.

## Source coverage

Source coverage (partial): 6 of 33 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 15 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

15 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] A run consists of three authored values: a graph defining control flow and typed state, a runtime plan binding each executable node to a harness, provider, model, and named connections, and caller-owned initial input validated against the graph before execution. -- evidence: [docs/index.md#L17-L21](https://github.com/the-open-engine/zeroshot/blob/b550c15279c9972a541f04c6d5925a5fa174363a/docs/index.md#L17-L21), [docs/index.md#L15-L15](https://github.com/the-open-engine/zeroshot/blob/b550c15279c9972a541f04c6d5925a5fa174363a/docs/index.md#L15-L15)
  - [observation/documented] Besides the software-change template, a single-worker template exists for work that does not need the review loop, and custom graphs follow the same protocol contracts. -- evidence: [docs/index.md#L40-L41](https://github.com/the-open-engine/zeroshot/blob/b550c15279c9972a541f04c6d5925a5fa174363a/docs/index.md#L40-L41)
- design-choices (3 claim(s)):
  - [observation/documented] Control flow is authored data rather than hidden in prompts: sequence, parallel review, retry paths, delivery, and exit conditions are explicit before a run starts, and no runtime agent chooses the next step. -- evidence: [README.md#L44-L46](https://github.com/the-open-engine/zeroshot/blob/b550c15279c9972a541f04c6d5925a5fa174363a/README.md#L44-L46), [README.md#L56-L57](https://github.com/the-open-engine/zeroshot/blob/b550c15279c9972a541f04c6d5925a5fa174363a/README.md#L56-L57)
  - [observation/documented] Three execution targets share the same graph and runtime plan: local mode in the current Git worktree reusing Codex or Claude Code logins, a self-hosted Docker target image bundling the engine plus pinned Codex and Claude harness CLIs, and a managed Zeroshot Cloud target. -- evidence: [README.md#L74-L74](https://github.com/the-open-engine/zeroshot/blob/b550c15279c9972a541f04c6d5925a5fa174363a/README.md#L74-L74), [docs/index.md#L63-L64](https://github.com/the-open-engine/zeroshot/blob/b550c15279c9972a541f04c6d5925a5fa174363a/docs/index.md#L63-L64), [README.md#L109-L110](https://github.com/the-open-engine/zeroshot/blob/b550c15279c9972a541f04c6d5925a5fa174363a/README.md#L109-L110), [README.md#L92-L93](https://github.com/the-open-engine/zeroshot/blob/b550c15279c9972a541f04c6d5925a5fa174363a/README.md#L92-L93), [README.md#L78-L79](https://github.com/the-open-engine/zeroshot/blob/b550c15279c9972a541f04c6d5925a5fa174363a/README.md#L78-L79)
- workflows (3 claim(s)):
  - [observation/documented] Repository development practice: contributors run `npm ci`, `npm run check`, and `cargo test --workspace`; Node.js is repository tooling and the npm delivery mechanism only. -- evidence: [README.md#L133-L137](https://github.com/the-open-engine/zeroshot/blob/b550c15279c9972a541f04c6d5925a5fa174363a/README.md#L133-L137), [README.md#L139-L140](https://github.com/the-open-engine/zeroshot/blob/b550c15279c9972a541f04c6d5925a5fa174363a/README.md#L139-L140)
  - [observation/documented] Repository development practice: releases publish one canonical version across GitHub tag, native archives, checksum manifest, npm package, target image, Python wheels, and versioned docs via a release workflow using GitHub OIDC trusted publishing, with no long-lived npm or PyPI tokens. -- evidence: [PUBLISHING.md#L10-L19](https://github.com/the-open-engine/zeroshot/blob/b550c15279c9972a541f04c6d5925a5fa174363a/PUBLISHING.md#L10-L19), [PUBLISHING.md#L37-L37](https://github.com/the-open-engine/zeroshot/blob/b550c15279c9972a541f04c6d5925a5fa174363a/PUBLISHING.md#L37-L37), [PUBLISHING.md#L3-L4](https://github.com/the-open-engine/zeroshot/blob/b550c15279c9972a541f04c6d5925a5fa174363a/PUBLISHING.md#L3-L4)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The product is a native `zeroshot` executable (v8 hard cutover, former Node.js runtime retired), installed via npm and providing commands like `zeroshot run`, `zeroshot version`, and `zeroshot template list/show`. -- evidence: [README.md#L29-L30](https://github.com/the-open-engine/zeroshot/blob/b550c15279c9972a541f04c6d5925a5fa174363a/README.md#L29-L30), [README.md#L81-L88](https://github.com/the-open-engine/zeroshot/blob/b550c15279c9972a541f04c6d5925a5fa174363a/README.md#L81-L88), [README.md#L67-L70](https://github.com/the-open-engine/zeroshot/blob/b550c15279c9972a541f04c6d5925a5fa174363a/README.md#L67-L70), [README.md#L34-L37](https://github.com/the-open-engine/zeroshot/blob/b550c15279c9972a541f04c6d5925a5fa174363a/README.md#L34-L37)
More evidence: [full detail](zeroshot.detail.md)

Metadata and full claim list: [full detail](zeroshot.detail.md)
Human notes ([notes](zeroshot.notes.md), never overwritten by build)

[Back to map index](../../index.md)
