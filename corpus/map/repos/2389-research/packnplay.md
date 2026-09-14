# 2389-research/packnplay

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-site-pages - Projects: Observatory
Latest snapshot: commit 5abeea291783 @ 233c35e9bb5fb7ff

## Summary (orientation draft, not independently verified)

The evidence is a single implementation plan document (docs/plans/2025-10-23-cage-implementation.md) describing the planned packnplay CLI: a Go tool to run commands in isolated Docker containers with git worktree and devcontainer management. All content is planned/documented design, not verified shipped behavior. Evidence coverage: 203 of 400 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 11 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] The plan's stated goal is to build packnplay, a CLI tool that launches commands such as Claude Code inside isolated Docker containers with automated worktree and dev container management. -- evidence: [docs/plans/2025-10-23-cage-implementation.md#L5-L5](https://github.com/2389-research/packnplay/blob/5abeea29178330dec7ba09c035934fa9416e2945/docs/plans/2025-10-23-cage-implementation.md#L5-L5)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (5 claim(s)):
  - [observation/documented] The planned architecture is a single Go binary using cobra for the CLI that shells out to docker and git commands, uses idmap mounts for UID translation, and tracks container state via session-based Docker labels. -- evidence: [docs/plans/2025-10-23-cage-implementation.md#L7-L7](https://github.com/2389-research/packnplay/blob/5abeea29178330dec7ba09c035934fa9416e2945/docs/plans/2025-10-23-cage-implementation.md#L7-L7)
  - [observation/documented] The planned Docker client detects the container CLI by honoring a DOCKER_CMD environment variable override, then falling back to docker and then podman in PATH. -- evidence: [docs/plans/2025-10-23-cage-implementation.md#L438-L439](https://github.com/2389-research/packnplay/blob/5abeea29178330dec7ba09c035934fa9416e2945/docs/plans/2025-10-23-cage-implementation.md#L438-L439), [docs/plans/2025-10-23-cage-implementation.md#L418-L426](https://github.com/2389-research/packnplay/blob/5abeea29178330dec7ba09c035934fa9416e2945/docs/plans/2025-10-23-cage-implementation.md#L418-L426), [docs/plans/2025-10-23-cage-implementation.md#L433-L436](https://github.com/2389-research/packnplay/blob/5abeea29178330dec7ba09c035934fa9416e2945/docs/plans/2025-10-23-cage-implementation.md#L433-L436), [docs/plans/2025-10-23-cage-implementation.md#L428-L431](https://github.com/2389-research/packnplay/blob/5abeea29178330dec7ba09c035934fa9416e2945/docs/plans/2025-10-23-cage-implementation.md#L428-L431)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: the plan document instructs the implementing agent to use the superpowers:executing-plans sub-skill to implement the plan task-by-task. -- evidence: [docs/plans/2025-10-23-cage-implementation.md#L3-L3](https://github.com/2389-research/packnplay/blob/5abeea29178330dec7ba09c035934fa9416e2945/docs/plans/2025-10-23-cage-implementation.md#L3-L3)
  - [observation/documented] Repository development practice: the plan follows a test-first workflow per task — write a failing test, implement, re-run go test to verify it passes, then commit. -- evidence: [docs/plans/2025-10-23-cage-implementation.md#L383-L383](https://github.com/2389-research/packnplay/blob/5abeea29178330dec7ba09c035934fa9416e2945/docs/plans/2025-10-23-cage-implementation.md#L383-L383), [docs/plans/2025-10-23-cage-implementation.md#L459-L459](https://github.com/2389-research/packnplay/blob/5abeea29178330dec7ba09c035934fa9416e2945/docs/plans/2025-10-23-cage-implementation.md#L459-L459), [docs/plans/2025-10-23-cage-implementation.md#L465-L465](https://github.com/2389-research/packnplay/blob/5abeea29178330dec7ba09c035934fa9416e2945/docs/plans/2025-10-23-cage-implementation.md#L465-L465), [docs/plans/2025-10-23-cage-implementation.md#L387-L387](https://github.com/2389-research/packnplay/blob/5abeea29178330dec7ba09c035934fa9416e2945/docs/plans/2025-10-23-cage-implementation.md#L387-L387), [docs/plans/2025-10-23-cage-implementation.md#L463-L463](https://github.com/2389-research/packnplay/blob/5abeea29178330dec7ba09c035934fa9416e2945/docs/plans/2025-10-23-cage-implementation.md#L463-L463), [docs/plans/2025-10-23-cage-implementation.md#L328-L328](https://github.com/2389-research/packnplay/blob/5abeea29178330dec7ba09c035934fa9416e2945/docs/plans/2025-10-23-cage-implementation.md#L328-L328)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] The planned CLI exposes four subcommands: run (with path, worktree, no-worktree, env, and verbose flags), attach, stop, and list, with attach and stop accepting path and worktree flags. -- evidence: [docs/plans/2025-10-23-cage-implementation.md#L263-L271](https://github.com/2389-research/packnplay/blob/5abeea29178330dec7ba09c035934fa9416e2945/docs/plans/2025-10-23-cage-implementation.md#L263-L271), [docs/plans/2025-10-23-cage-implementation.md#L179-L185](https://github.com/2389-research/packnplay/blob/5abeea29178330dec7ba09c035934fa9416e2945/docs/plans/2025-10-23-cage-implementation.md#L179-L185), [docs/plans/2025-10-23-cage-implementation.md#L101-L108](https://github.com/2389-research/packnplay/blob/5abeea29178330dec7ba09c035934fa9416e2945/docs/plans/2025-10-23-cage-implementation.md#L101-L108), [docs/plans/2025-10-23-cage-implementation.md#L215-L218](https://github.com/2389-research/packnplay/blob/5abeea29178330dec7ba09c035934fa9416e2945/docs/plans/2025-10-23-cage-implementation.md#L215-L218), [docs/plans/2025-10-23-cage-implementation.md#L248-L251](https://github.com/2389-research/packnplay/blob/5abeea29178330dec7ba09c035934fa9416e2945/docs/plans/2025-10-23-cage-implementation.md#L248-L251)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] The planned tech stack is Go 1.21+, the cobra CLI framework, and the Docker and git CLIs invoked via shell. -- evidence: [docs/plans/2025-10-23-cage-implementation.md#L9-L9](https://github.com/2389-research/packnplay/blob/5abeea29178330dec7ba09c035934fa9416e2945/docs/plans/2025-10-23-cage-implementation.md#L9-L9)
- limitations (1 claim(s)):
More evidence: [full detail](packnplay.detail.md)

Metadata and full claim list: [full detail](packnplay.detail.md)
Human notes ([notes](packnplay.notes.md), never overwritten by build)

[Back to map index](../../index.md)
