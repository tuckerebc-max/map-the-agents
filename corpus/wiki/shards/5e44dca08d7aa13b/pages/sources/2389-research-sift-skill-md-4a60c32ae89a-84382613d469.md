---
access: public
aliases: []
claim_ids:
- clm_23fe5c519ee29bf9a4d40243a9484b3fe2e767d7fc500b4f633363e3289eb97f
- clm_3eeceb75514ba434b698440fe9745a1bce7c9f928d34ea4a98de9ff910718e33
- clm_63ec83bdfdb797ba408d25499af7f813938650c7f26b84813b7a9aeeae767557
- clm_672ed684d1d42f4acdea5078f9a206e1428e28eb9027c931a5525765208cf073
- clm_678631bbaee5510a888cde0e3c67ac144f37a2f4c54b4e5698884201f50a36fe
- clm_9d8948c4a9bf739ce506f1b87b484c784150d0ebab47cf51be7c93bf81c29968
- clm_a0140567ca2eaabdcdf25255aae7847d5de9846bf54257921eb1d92dff066bca
- clm_a9f535e83df9f6909619cbcbe0030271e168377c254352a0dee6c8c4c1f4465e
- clm_ba56cb7824b500b8344f953bd28b6e4f1bf2a511ff94bec1d1159803469b7545
- clm_ca41d79d8c4e400b86eef43d068cf09b79e665437eb1df28fd975bfb79b21214
- clm_cd82d40faf90a4ab4079744c1a6b24a13fdd8b6d64a8b48754a426e3cc83b3b4
maturity: draft
page_id: pg_0c8535cd2bc35f0191a384382613d469
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_b10170311bd75daf9367db0975dfd2ac
title: 2389-research/sift/SKILL.md @ 4a60c32ae89a
updated_at: '2026-09-14T03:29:36Z'
---

# 2389-research/sift/SKILL.md @ 4a60c32ae89a

<!-- rcw:begin owner=source:src_b10170311bd75daf9367db0975dfd2ac block=evidence -->
- Findings are bounded to at most two materially useful opportunities per subsystem, with an explicit skip recorded when nothing passes the materiality gate, and the skill rejects abstraction churn, stylistic changes, and complexity relocation. [@claim:clm_23fe5c519ee29bf9a4d40243a9484b3fe2e767d7fc500b4f633363e3289eb97f]
- The audit is read-only by design: the sole repository write is the final report, defaulting to docs/sift-audit-<date>.md, honoring a user-named path, or writing nothing when the user declines or the environment cannot write files. [@claim:clm_3eeceb75514ba434b698440fe9745a1bce7c9f928d34ea4a98de9ff910718e33]
- The operating contract forbids running tests, builds, formatters, code generators, migrations, package managers, or dev servers, permitting only read-only inspection commands such as cat, sed, head, tail, and git status/diff/log/show/ls-files. [@claim:clm_63ec83bdfdb797ba408d25499af7f813938650c7f26b84813b7a9aeeae767557]
- The skill requires read access to the repository plus ordinary file-search or shell inspection tools, write access only for the one report artifact, and no network access; if files cannot be written, the report is delivered in conversation. [@claim:clm_672ed684d1d42f4acdea5078f9a206e1428e28eb9027c931a5525765208cf073]
- If execution limits prevent full coverage, the audit must be labeled INCOMPLETE with every unreviewed or insufficiently verified row listed, and completion requires every subsystem reviewed with either an accepted finding or an explicit skip. [@claim:clm_678631bbaee5510a888cde0e3c67ac144f37a2f4c54b4e5698884201f50a36fe]
- The coordinator acts as an orchestrator that establishes complete coverage, delegates bounded reviews, independently validates every candidate finding against the repository, and runs a Phase 4 self-audit of coverage, duplication, materiality, schema completeness, and ranking. [@claim:clm_9d8948c4a9bf739ce506f1b87b484c784150d0ebab47cf51be7c93bf81c29968]
- The audit targets material simplifications in data structures, schemas, state representation, control flow, algorithms, lifecycle/concurrency, and module ownership boundaries. [@claim:clm_a0140567ca2eaabdcdf25255aae7847d5de9846bf54257921eb1d92dff066bca]
- Integrity is verified by capturing a repository-status baseline at start and comparing it at the end; if state changed the integrity check is labeled failed, and with no version control it is reported as not verifiable rather than verified. [@claim:clm_a9f535e83df9f6909619cbcbe0030271e168377c254352a0dee6c8c4c1f4465e]
- The skill is named sift-codebase-audit, version 1.2.1, MIT-licensed, and is described as a read-only whole-repository audit for simplification opportunities that recommends but never applies changes. [@claim:clm_ba56cb7824b500b8344f953bd28b6e4f1bf2a511ff94bec1d1159803469b7545]
- The skill is explicitly not intended for single-file, module, or diff-scoped reviews; those should use an ordinary focused code review instead. [@claim:clm_ca41d79d8c4e400b86eef43d068cf09b79e665437eb1df28fd975bfb79b21214]
- Phase 2 uses fresh read-only subagents when an agent-spawning tool exists, assigning each worker exactly one subsystem with a non-overlapping ownership boundary, batching review work, and closing workers after harvesting results; otherwise reviews run sequentially. [@claim:clm_cd82d40faf90a4ab4079744c1a6b24a13fdd8b6d64a8b48754a426e3cc83b3b4]
<!-- rcw:end owner=source:src_b10170311bd75daf9367db0975dfd2ac block=evidence -->

## Researcher notes

