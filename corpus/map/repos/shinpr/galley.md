# shinpr/galley

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit b542bd7adb37 @ b672269c9deea4f0

## Summary (orientation draft, not independently verified)

Galley is a local runtime for supervised, multi-model AI coding that queues task YAML, runs executors in isolated git worktrees, and gates results through an independently selected supervisor. Evidence is mostly README/SECURITY/CONTRIBUTING documentation; no source code slices are present.

## Source coverage

Source coverage (partial): 3 of 11 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 14 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

14 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (2 claim(s)):
  - [observation/documented] Task YAML is trusted local input describing goal, acceptance criteria, scope, executor overrides, verification, and worktree, with a documented reference at docs/task-yaml.md. -- evidence: [README.md#L168-L174](https://github.com/shinpr/galley/blob/b542bd7adb37039a5bc69393f199d8e9c7937679/README.md#L168-L174)
  - [observation/documented] Repositories are configured via two profile types: a quality profile (required checks, review dimensions, evidence, pass criteria) and an environment profile (commands, executor CLI/model/effort, constraints, PR behavior, cleanup). -- evidence: [README.md#L168-L174](https://github.com/shinpr/galley/blob/b542bd7adb37039a5bc69393f199d8e9c7937679/README.md#L168-L174)
- components (1 claim(s)):
  - [observation/documented] The system comprises a galley CLI, a background daemon that claims queued tasks, executor backends that implement tasks, and supervisor backends that act as the acceptance gate. -- evidence: [README.md#L168-L174](https://github.com/shinpr/galley/blob/b542bd7adb37039a5bc69393f199d8e9c7937679/README.md#L168-L174), [README.md#L144-L164](https://github.com/shinpr/galley/blob/b542bd7adb37039a5bc69393f199d8e9c7937679/README.md#L144-L164)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: contributors run gofmt, go test ./..., go build ./cmd/galley, and scripts/smoke-local.sh before opening a PR, and validate examples and plugin metadata when changing schemas or plugin files. -- evidence: [CONTRIBUTING.md#L14-L14](https://github.com/shinpr/galley/blob/b542bd7adb37039a5bc69393f199d8e9c7937679/CONTRIBUTING.md#L14-L14), [CONTRIBUTING.md#L16-L21](https://github.com/shinpr/galley/blob/b542bd7adb37039a5bc69393f199d8e9c7937679/CONTRIBUTING.md#L16-L21), [CONTRIBUTING.md#L38-L38](https://github.com/shinpr/galley/blob/b542bd7adb37039a5bc69393f199d8e9c7937679/CONTRIBUTING.md#L38-L38), [CONTRIBUTING.md#L40-L43](https://github.com/shinpr/galley/blob/b542bd7adb37039a5bc69393f199d8e9c7937679/CONTRIBUTING.md#L40-L43), [CONTRIBUTING.md#L25-L29](https://github.com/shinpr/galley/blob/b542bd7adb37039a5bc69393f199d8e9c7937679/CONTRIBUTING.md#L25-L29), [CONTRIBUTING.md#L23-L23](https://github.com/shinpr/galley/blob/b542bd7adb37039a5bc69393f199d8e9c7937679/CONTRIBUTING.md#L23-L23)
  - [observation/documented] Repository development practice: releases are created from the GitHub UI, triggering a GoReleaser workflow that attaches macOS, Linux, and Windows archives; contributors add CHANGELOG.md entries for user-visible changes. -- evidence: [CONTRIBUTING.md#L68-L68](https://github.com/shinpr/galley/blob/b542bd7adb37039a5bc69393f199d8e9c7937679/CONTRIBUTING.md#L68-L68), [CONTRIBUTING.md#L72-L72](https://github.com/shinpr/galley/blob/b542bd7adb37039a5bc69393f199d8e9c7937679/CONTRIBUTING.md#L72-L72)
- skills-patterns (1 claim(s)):
  - [observation/documented] The plugin packages one Agent Skill for Claude Code, Codex, and Grok Build covering setup, CLI checks, task YAML drafting/validation, profile authoring, approval-gated queueing, and failed-run diagnosis; skills-compatible clients can symlink plugins/galley/skills/galley/. -- evidence: [README.md#L136-L138](https://github.com/shinpr/galley/blob/b542bd7adb37039a5bc69393f199d8e9c7937679/README.md#L136-L138), [README.md#L134-L134](https://github.com/shinpr/galley/blob/b542bd7adb37039a5bc69393f199d8e9c7937679/README.md#L134-L134), [README.md#L126-L126](https://github.com/shinpr/galley/blob/b542bd7adb37039a5bc69393f199d8e9c7937679/README.md#L126-L126), [README.md#L128-L132](https://github.com/shinpr/galley/blob/b542bd7adb37039a5bc69393f199d8e9c7937679/README.md#L128-L132)
- interfaces (2 claim(s)):
  - [observation/documented] The CLI exposes commands including daemon config init, daemon start, daemon status --output json, daemon run --once, task validate, profile validate, and schema generate/check. -- evidence: [CONTRIBUTING.md#L33-L36](https://github.com/shinpr/galley/blob/b542bd7adb37039a5bc69393f199d8e9c7937679/CONTRIBUTING.md#L33-L36), [README.md#L217-L222](https://github.com/shinpr/galley/blob/b542bd7adb37039a5bc69393f199d8e9c7937679/README.md#L217-L222), [README.md#L50-L52](https://github.com/shinpr/galley/blob/b542bd7adb37039a5bc69393f199d8e9c7937679/README.md#L50-L52), [CONTRIBUTING.md#L25-L29](https://github.com/shinpr/galley/blob/b542bd7adb37039a5bc69393f199d8e9c7937679/CONTRIBUTING.md#L25-L29)
  - [observation/documented] Executor and supervisor model fields resolve from the task, then the environment profile; only the executor cli has a built-in default (claude), and empty model/effort values defer to the provider CLI's defaults. -- evidence: [README.md#L168-L174](https://github.com/shinpr/galley/blob/b542bd7adb37039a5bc69393f199d8e9c7937679/README.md#L168-L174)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (2 claim(s)):
  - [observation/documented] The pipeline flows from task YAML plus repository policy through queueing, daemon claim, isolated git worktree execution, supervisor review, then acceptance (PR or local completion), retry within budget, or failure for human review. -- evidence: [README.md#L144-L164](https://github.com/shinpr/galley/blob/b542bd7adb37039a5bc69393f199d8e9c7937679/README.md#L144-L164)
More evidence: [full detail](galley.detail.md)

Metadata and full claim list: [full detail](galley.detail.md)
Human notes ([notes](galley.notes.md), never overwritten by build)

[Back to map index](../../index.md)
