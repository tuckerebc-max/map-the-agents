# generalaction/emdash

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit fccf35084709 @ a2795a7f46ba37a1

## Summary (orientation draft, not independently verified)

Emdash is an Electron desktop app for running AI coding agents in parallel, each isolated in a Git worktree, with local and SSH remote support, issue-tracker integrations, and diff/PR review. Most evidence is README product description plus AGENTS.md contributor guidance (workflows only).

## Source coverage

Source coverage (partial): 3 of 14 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Emdash is a desktop app for running AI coding agents in parallel, with each task isolated in its own Git worktree so multiple fixes or features can be explored, reviewed, and merged. -- evidence: [README.md#L21-L23](https://github.com/generalaction/emdash/blob/fccf350847097c8f9d9de3e7e5c98b0d292a4554/README.md#L21-L23)
- components (3 claim(s)):
  - [observation/documented] Features include running multiple agents without juggling terminals, per-agent worktree/branch isolation, sending issues from trackers like Linear, GitHub, Jira, and GitLab into agents, and reviewing diffs, creating PRs, inspecting CI checks, and merging from one place. -- evidence: [README.md#L32-L37](https://github.com/generalaction/emdash/blob/fccf350847097c8f9d9de3e7e5c98b0d292a4554/README.md#L32-L37)
  - [observation/documented] For agents with lifecycle-hook support, Emdash installs marker-tagged hook entries in the agent's user-level config to track status, notifications, and resumable sessions, and the hooks do nothing when the agent runs outside Emdash. -- evidence: [README.md#L57-L59](https://github.com/generalaction/emdash/blob/fccf350847097c8f9d9de3e7e5c98b0d292a4554/README.md#L57-L59)
- design-choices (2 claim(s)):
  - [observation/documented] The app is local-first: app state lives in a local SQLite database, and Emdash does not send the user's code or chats to Emdash servers, though agent CLIs may send data to their own providers. -- evidence: [README.md#L77-L78](https://github.com/generalaction/emdash/blob/fccf350847097c8f9d9de3e7e5c98b0d292a4554/README.md#L77-L78), [README.md#L74-L75](https://github.com/generalaction/emdash/blob/fccf350847097c8f9d9de3e7e5c98b0d292a4554/README.md#L74-L75)
  - [observation/documented] Telemetry is optional and can be disabled in Settings or by launching with TELEMETRY_ENABLED=false. -- evidence: [README.md#L82-L84](https://github.com/generalaction/emdash/blob/fccf350847097c8f9d9de3e7e5c98b0d292a4554/README.md#L82-L84), [README.md#L80-L80](https://github.com/generalaction/emdash/blob/fccf350847097c8f9d9de3e7e5c98b0d292a4554/README.md#L80-L80)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: the merge gate is four root commands (format, lint, typecheck, test) run via pnpm/Nx, with CI running a code-consistency workflow using nx affected on touched projects and dependents, and browser Vitest projects skipped in CI. -- evidence: [AGENTS.md#L213-L228](https://github.com/generalaction/emdash/blob/fccf350847097c8f9d9de3e7e5c98b0d292a4554/AGENTS.md#L213-L228), [AGENTS.md#L60-L66](https://github.com/generalaction/emdash/blob/fccf350847097c8f9d9de3e7e5c98b0d292a4554/AGENTS.md#L60-L66)
  - [observation/documented] Repository development practice: the repo is a pnpm workspace monorepo; only pnpm on PATH is needed since package.json pins pnpm 10.28.2 and Node 24.14.0 with onFail download, so the toolchain self-provisions. -- evidence: [AGENTS.md#L49-L54](https://github.com/generalaction/emdash/blob/fccf350847097c8f9d9de3e7e5c98b0d292a4554/AGENTS.md#L49-L54), [AGENTS.md#L10-L14](https://github.com/generalaction/emdash/blob/fccf350847097c8f9d9de3e7e5c98b0d292a4554/AGENTS.md#L10-L14)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The product works with local projects and remote machines over SSH, and drives CLI agents the user already has, such as Claude Code, Codex, OpenCode, and Amp. -- evidence: [README.md#L25-L26](https://github.com/generalaction/emdash/blob/fccf350847097c8f9d9de3e7e5c98b0d292a4554/README.md#L25-L26)
  - [observation/documented] Emdash automatically detects installed provider CLIs and supports agents including Claude Code, Codex, Cursor, OpenCode, Amp, Devin, Qwen Code, Droid, and GitHub Copilot. -- evidence: [README.md#L53-L55](https://github.com/generalaction/emdash/blob/fccf350847097c8f9d9de3e7e5c98b0d292a4554/README.md#L53-L55)
- memory-state: unknown (no source-linked claim submitted for this facet)
More evidence: [full detail](emdash.detail.md)

Metadata and full claim list: [full detail](emdash.detail.md)
Human notes ([notes](emdash.notes.md), never overwritten by build)

[Back to map index](../../index.md)
