---
name: sift-codebase-audit
description: Use when asked to run SIFT (Structural Inspection for Technical Simplification), audit a codebase for simplification or refactoring opportunities, review structural complexity or tech debt, find invalid-state representations, or produce a prioritized simplification plan. A read-only, whole-repository audit covering data structures, state representation, control flow, algorithms, schemas, lifecycle/concurrency, and ownership boundaries. Not for single-file or diff-scoped reviews; recommends but never applies changes.
license: MIT
compatibility: Requires read access to the repository and ordinary file-search or shell inspection tools, plus write access for the one report artifact; when files cannot be written, the report is delivered in conversation. No network access needed.
metadata:
  version: "1.2.1"
---

# SIFT Codebase Audit

**SIFT = Structural Inspection for Technical Simplification.**

## Mission

Audit the complete codebase for **materially useful simplifications** in:

- data structures and schemas;
- state representation and invalid-state prevention;
- control flow and duplicated branching;
- algorithms, scans, transformations, and lookup strategies;
- lifecycle, concurrency, and asynchronous state;
- module boundaries, authority, and ownership.

This is an **audit-only** exercise. Act as the coordinator: establish complete coverage, delegate bounded reviews when possible, independently validate every candidate, audit the audit, and return a prioritized report.

## When not to use this skill

- A single file, module, or diff review does not need SIFT; use an ordinary focused code review instead.
- SIFT recommends and never implements. When the user also wants fixes applied, finish and deliver the audit first, then treat implementation as separate follow-up work outside this skill.

## Non-negotiable operating contract

1. **Keep the repository unchanged.**
   - Do not edit, create, delete, rename, or reformat repository files.
   - Do not implement recommendations.
   - Do not commit, push, stage, stash, checkout, reset, or alter branches.
   - Do not write a scratchpad inside the repository. Use internal notes or a temporary path outside the repository, and remove temporary files when finished.
   - The one exception is the final report artifact defined in Final output, written only after the final integrity comparison has been captured.

2. **Do not execute mutating or potentially mutating workflows.**
   - Do not run tests, builds, formatters, linters with autofix, code generators, migrations, package managers, dependency installers, or development servers.
   - Avoid commands that may create caches, lockfiles, generated output, or metadata in the repository.
   - Read-only inspection commands are allowed: file listing, search, `cat`, `sed`, `head`, `tail`, `git status`, `git diff`, `git log`, `git show`, `git ls-files`, and equivalent read operations.

3. **Use repository evidence as the authority.**
   - Inspect implementation, public interfaces, major call sites, existing tests, schemas, and relevant documentation.
   - Do not justify findings primarily from generic best practices or external sources.
   - Cite exact file paths and line ranges for every accepted finding.

4. **Prefer material simplification over abstraction churn.**
   - Do not force an abstraction. Prefer boring local code when it is already clear.
   - Do not recommend changes solely for stylistic consistency, hypothetical extensibility, minor line-count reduction, naming taste, or moving existing branching behind a new type.
   - Do not merely relocate complexity.

5. **Bound findings.**
   - Return at most two materially useful opportunities per subsystem.
   - If nothing clearly passes the materiality gate, record an explicit `skip`.

6. **Do not claim completion without coverage.**
   - Continue until every identifiable subsystem has been reviewed and the final audit has been validated.
   - If execution limits prevent completion, label the audit `INCOMPLETE` and list every unreviewed or insufficiently verified row. Never imply full coverage.

## Initialize the audit

Before reviewing code:

1. Determine the repository root and the user-requested scope. Default to the current repository and the whole application when no narrower scope is stated.
2. Record a baseline:
   - repository root;
   - current revision and branch, when available;
   - complete `git status --porcelain=v1 --untracked-files=all`, when this is a Git repository;
   - when no version control is available, record that no baseline fingerprint exists and report the integrity check as `not verifiable` rather than claiming verified integrity.
3. Read local operating guidance such as `CLAUDE.md`, `AGENTS.md`, `CONTRIBUTING`, architecture notes, and top-level READMEs when present.
4. Record explicit user exclusions and obvious non-source categories such as vendored dependencies, binary assets, generated artifacts, snapshots, and build output. Do not silently exclude them; assign an explicit skip decision or identify the authoritative source that should be audited instead.
5. Maintain one canonical coverage ledger and one canonical finding set. Do not allow parallel workers to keep separate authoritative inventories.

## Phase 1: Establish the coverage contract

Inspect the repository and inventory every identifiable subsystem. The inventory is the coverage contract.

Give each subsystem:

- a stable ID and descriptive name;
- an exact, non-overlapping ownership boundary;
- key implementation files or directories;
- relevant public interfaces, major call sites, schemas, and tests;
- dependencies or adjacent subsystem boundaries that matter to the review;
- a status: `queued`, `in-review`, `recommend`, or `skip`;
- an explicit skip reason when applicable.

Include, where materially relevant:

- frontend surfaces and client state;
- backend services and domain logic;
- shared libraries and infrastructure;
- persistence models, schemas, migrations, and generated-contract ownership;
- platform bridges, adapters, queues, workers, and external integration boundaries;
- lifecycle and concurrency infrastructure;
- test harnesses, fixtures, build tooling, and developer tooling.

Rules for the inventory:

- Do not use broad catch-all rows as proof of coverage.
- Split a row when separate authorities, schemas, lifecycles, or call graphs require independent review.
- Keep boundaries exact enough that two workers cannot reasonably audit the same implementation as their primary scope.
- For generated code, identify and audit the generator, schema, or source-of-truth owner; record generated output as a skip unless it contains hand-maintained behavior.
- For vendored code, record a skip unless the repository owns modifications or behavioral integration that requires review.

## Phase 2: Run bounded subsystem reviews

Use fresh, read-only subagents when the environment provides an agent-spawning or task-dispatch tool. Otherwise perform the same reviews sequentially.

### Review standard

`references/worker-brief.md` is the single authority for the per-subsystem review: the required inspection targets, the simplification checklist, the materiality gate, and the return format. Read it before starting Phase 2 and apply it identically whether delegating or reviewing sequentially yourself. Do not restate its rules elsewhere; when they need adjusting, change the brief.

### Delegation protocol

- Workers do not share your context, so provide each worker the full text of `references/worker-brief.md` plus the subsystem-specific assignment, not a summary or a file path.
- Prefer read-only subagent types when the environment offers them; the brief's constraints are instructions, not enforcement.
- Assign each worker exactly one subsystem ID with an exact ownership boundary and explicit exclusions.
- Never give two active workers overlapping primary ownership.
- Keep concurrency bounded to the number of lanes you can actively coordinate.
- Open review work in batches; use one consolidated wait or collection step for each batch.
- Do not interrupt productive workers merely because they are slow.
- Close completed workers after harvesting their results.

## Phase 3: Validate and synthesize

The coordinator must independently verify every candidate against the current repository before accepting it.

For each candidate:

1. Re-open the cited implementation and line ranges.
2. Trace representative producers, consumers, and call sites.
3. Inspect tests or other evidence of intended semantics.
4. Confirm the proposed representation removes complexity rather than moving it.
5. Confirm the implementation scope is credible and bounded.
6. Check for overlap with every accepted or pending finding.
7. Assign the finding to one authoritative subsystem.
8. Reject, narrow, merge, or lower confidence when the evidence does not support the original claim.

Record skips as completed coverage. Keep a concise audit log of rejected, merged, superseded, and demoted findings so the final synthesis is explainable.

Use the exact finding fields in `references/finding-schema.md`.

## Phase 4: Audit the audit

Before finishing, run fresh independent passes for:

1. **Coverage:** missing subsystems, hidden ownership boundaries, unreviewed schemas, or broad catch-all rows.
2. **Duplication and authority:** overlapping findings, duplicate abstractions, and recommendations assigned to the wrong subsystem.
3. **Materiality:** weak findings, stylistic cleanup, speculative abstractions, or complexity relocation.
4. **Schema completeness:** missing evidence, scope, risk, migration, validation, or confidence fields.
5. **Dependency-aware ranking:** impact, confidence, effort, blast radius, prerequisites, and sequencing.

Use fresh subagents or clean review contexts when available.

If the coverage pass finds a real omission, add an explicit subsystem row and audit it. Do not conceal the omission by broadening a previously completed row.

## Completion criteria

The audit is complete only when:

- every identifiable subsystem has been reviewed;
- every subsystem has either an accepted recommendation or an explicit skip;
- every accepted finding has complete evidence, scope, risk, migration, validation, and confidence fields;
- duplicates, weak findings, and abstraction churn have been removed;
- priorities and dependencies are internally consistent;
- the final repository state matches the recorded baseline, or the integrity check is explicitly reported as `not verifiable` because no baseline existed.

At the end, capture the same repository-status command used at baseline and compare the results. If the state changed, do not claim the repository remained unchanged; identify the difference and label the integrity check failed. When no baseline fingerprint was available, report the integrity check as `not verifiable`.

## Final output

Read `references/report-template.md` and produce one canonical report following that structure.

Write the full report to a file and summarize it in the conversation response with the executive summary, the ranking table, and the artifact path. The file is the audit's only repository write and happens only after the final repository-integrity comparison has been captured:

- When the user named a report path, write to exactly that path.
- When the user declined a file, deliver the full report in the conversation instead and write nothing.
- When the environment cannot write files, deliver the full report in the conversation instead.
- Otherwise write to `docs/sift-audit-<YYYY-MM-DD>.md` under the repository root, creating `docs/` when it does not exist.

Record the artifact path in the report's integrity section as the sole post-audit write.

The report must:

- state `COMPLETE` or `INCOMPLETE` prominently;
- summarize the highest-value structural themes;
- show the full subsystem coverage ledger, including explicit skips;
- provide no more than two accepted findings per subsystem;
- include exact evidence for every finding;
- rank recommendations by concrete impact, confidence, implementation effort, blast radius, and prerequisites;
- identify the smallest credible first implementation slices;
- include rejected, merged, or superseded candidates when they materially explain the result;
- include the final repository-integrity comparison.
