# cfal/garcon

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 42a5322794a9 @ 76fa39f541038aba

## Summary (orientation draft, not independently verified)

Garcon is a self-hosted browser workspace for running and coordinating multiple coding agents, with a CLI, agent skills package, ticket store, and Git/terminal integration. Evidence covers product features from README plus extensive contributor development rules in AGENTS.md. Evidence coverage: 132 of 144 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 3 of 13 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 15 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

15 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The repository is organized into a SvelteKit/Svelte 5 frontend (web/), a Bun server handling chat lifecycle, providers, Git, auth, and notifications (server/), agent-specific runtimes (server-agents/), shared contracts (common/), and black-box integration tests. -- evidence: [README.md#L190-L194](https://github.com/cfal/garcon/blob/42a5322794a9a755a9eee34f707aeb7e72ee6331/README.md#L190-L194)
- design-choices (1 claim(s)):
  - [observation/documented] Model names may carry a `[Nk]` suffix (100-1000, thousands of tokens) that sets a per-chat Claude auto-compaction window; the annotation overrides CLAUDE_CODE_AUTO_COMPACT_WINDOW for that child process only and requires Claude Code 2.1.238+. -- evidence: [README.md#L117-L117](https://github.com/cfal/garcon/blob/42a5322794a9a755a9eee34f707aeb7e72ee6331/README.md#L117-L117), [README.md#L119-L119](https://github.com/cfal/garcon/blob/42a5322794a9a755a9eee34f707aeb7e72ee6331/README.md#L119-L119)
- workflows (4 claim(s)):
  - [observation/documented] Repository development practice: AGENTS.md directs contributors to use bun instead of npm, run `bun run test` to validate changes, start new servers on different ports rather than killing running ones, and treat the git tree as read-only unless instructed. -- evidence: [AGENTS.md#L7-L37](https://github.com/cfal/garcon/blob/42a5322794a9a755a9eee34f707aeb7e72ee6331/AGENTS.md#L7-L37)
  - [observation/documented] Repository development practice: every WebSocket/API contract change requires updated type definitions, sender and receiver logic, tests, and a migration note in the PR description when behavior changes. -- evidence: [AGENTS.md#L56-L60](https://github.com/cfal/garcon/blob/42a5322794a9a755a9eee34f707aeb7e72ee6331/AGENTS.md#L56-L60), [AGENTS.md#L50-L52](https://github.com/cfal/garcon/blob/42a5322794a9a755a9eee34f707aeb7e72ee6331/AGENTS.md#L50-L52), [AGENTS.md#L54-L54](https://github.com/cfal/garcon/blob/42a5322794a9a755a9eee34f707aeb7e72ee6331/AGENTS.md#L54-L54)
- skills-patterns (1 claim(s)):
  - [observation/documented] A companion garcon-skills package exposes the control plane to skill-aware agents via skills like garcon-captain, garcon-agent, garcon-task, garcon-message, garcon-schedule, and garcon-amp, installed with a link.sh script. -- evidence: [README.md#L145-L147](https://github.com/cfal/garcon/blob/42a5322794a9a755a9eee34f707aeb7e72ee6331/README.md#L145-L147), [README.md#L155-L155](https://github.com/cfal/garcon/blob/42a5322794a9a755a9eee34f707aeb7e72ee6331/README.md#L155-L155), [README.md#L143-L143](https://github.com/cfal/garcon/blob/42a5322794a9a755a9eee34f707aeb7e72ee6331/README.md#L143-L143), [README.md#L149-L153](https://github.com/cfal/garcon/blob/42a5322794a9a755a9eee34f707aeb7e72ee6331/README.md#L149-L153)
- interfaces (3 claim(s)):
  - [observation/documented] A CLI drives visible Garcon chats through a running server, supporting catalog discovery, sync/detached starts and resumes, steering, status, transcript search and reads, export, handoff, and stop controls. -- evidence: [README.md#L123-L123](https://github.com/cfal/garcon/blob/42a5322794a9a755a9eee34f707aeb7e72ee6331/README.md#L123-L123)
  - [observation/documented] The web UI is served at http://127.0.0.1:8080 by default; first launch requires creating an account at /setup, and authentication is enabled by default. -- evidence: [README.md#L38-L38](https://github.com/cfal/garcon/blob/42a5322794a9a755a9eee34f707aeb7e72ee6331/README.md#L38-L38)
- memory-state (1 claim(s)):
  - [observation/documented] Tickets persist in the workspace's tickets.sqlite, independent of chats and transcripts; a damaged or unknown-schema store is left unavailable for explicit recovery rather than rebuilt from transcripts. -- evidence: [README.md#L165-L165](https://github.com/cfal/garcon/blob/42a5322794a9a755a9eee34f707aeb7e72ee6331/README.md#L165-L165)
- orchestration (1 claim(s)):
More evidence: [full detail](garcon.detail.md)

Metadata and full claim list: [full detail](garcon.detail.md)
Human notes ([notes](garcon.notes.md), never overwritten by build)

[Back to map index](../../index.md)
