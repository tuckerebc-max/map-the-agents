# 2389-research/ourocodus

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-site-pages - Projects: Observatory
Latest snapshot: commit 00bfe36ef930 @ fbb642909c8dc3bb

## Summary (orientation draft, not independently verified)

Ourocodus is a Phase 1 multi-agent coding system where a Go WebSocket relay orchestrates ACP-compatible agents (e.g., Claude Code) in isolated git worktrees and Docker containers, with an optional NATS event bus and a documented REST control-plane spec. Evidence is documentation-based; CI, linting, and contributor setup are development practice, not product behavior. Evidence coverage: 197 of 391 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 123 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 18 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

18 claim(s) across 11 facet(s); 2 facet(s) unknown.

- specifications (2 claim(s)):
  - [observation/documented] The PRD specifies an HTTP control plane providing REST endpoints for session management, agent lifecycle, event log access, health checks, and serving static web UI files. -- evidence: [docs/prd/api.md#L9-L13](https://github.com/2389-research/ourocodus/blob/00bfe36ef93024f4e3ff8c85f68b4b0ca3a243bc/docs/prd/api.md#L9-L13), [docs/prd/api.md#L5-L5](https://github.com/2389-research/ourocodus/blob/00bfe36ef93024f4e3ff8c85f68b4b0ca3a243bc/docs/prd/api.md#L5-L5)
  - [observation/documented] The PRD specifies Session, Agent, and Event data models with JSON fields including status, container_id, chunks_completed, and payload. -- evidence: [docs/prd/api.md#L215-L226](https://github.com/2389-research/ourocodus/blob/00bfe36ef93024f4e3ff8c85f68b4b0ca3a243bc/docs/prd/api.md#L215-L226), [docs/prd/api.md#L244-L253](https://github.com/2389-research/ourocodus/blob/00bfe36ef93024f4e3ff8c85f68b4b0ca3a243bc/docs/prd/api.md#L244-L253), [docs/prd/api.md#L230-L240](https://github.com/2389-research/ourocodus/blob/00bfe36ef93024f4e3ff8c85f68b4b0ca3a243bc/docs/prd/api.md#L230-L240)
- components (1 claim(s)):
  - [observation/documented] The repository layout includes a relay WebSocket server, a CLI, an echo test agent under cmd/, shared packages in pkg/, and a PWA frontend in web/. -- evidence: [README.md#L185-L195](https://github.com/2389-research/ourocodus/blob/00bfe36ef93024f4e3ff8c85f68b4b0ca3a243bc/README.md#L185-L195)
- design-choices (3 claim(s)):
  - [observation/documented] Each AgentSession has three isolation layers (git worktree, read-only credentials, Docker container) orchestrated by an AgentContainerLauncher. -- evidence: [docs/architecture/ARCHITECTURE.md#L13-L17](https://github.com/2389-research/ourocodus/blob/00bfe36ef93024f4e3ff8c85f68b4b0ca3a243bc/docs/architecture/ARCHITECTURE.md#L13-L17), [docs/architecture/ARCHITECTURE.md#L44-L44](https://github.com/2389-research/ourocodus/blob/00bfe36ef93024f4e3ff8c85f68b4b0ca3a243bc/docs/architecture/ARCHITECTURE.md#L44-L44), [docs/architecture/ARCHITECTURE.md#L46-L46](https://github.com/2389-research/ourocodus/blob/00bfe36ef93024f4e3ff8c85f68b4b0ca3a243bc/docs/architecture/ARCHITECTURE.md#L46-L46)
  - [observation/documented] ACP processes can run as host processes via os/exec (default) or inside agent containers via docker exec, selected by the OUROCODUS_ACP_RUNTIME variable. -- evidence: [README.md#L44-L49](https://github.com/2389-research/ourocodus/blob/00bfe36ef93024f4e3ff8c85f68b4b0ca3a243bc/README.md#L44-L49)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: CI runs two GitHub Actions workflows on PRs and pushes to main, covering builds, go test, golangci-lint, gofmt, shellcheck, and smoke/integration tests; optional pre-commit hooks run gofumpt, go vet, and go mod tidy. -- evidence: [README.md#L216-L218](https://github.com/2389-research/ourocodus/blob/00bfe36ef93024f4e3ff8c85f68b4b0ca3a243bc/README.md#L216-L218), [README.md#L258-L262](https://github.com/2389-research/ourocodus/blob/00bfe36ef93024f4e3ff8c85f68b4b0ca3a243bc/README.md#L258-L262), [README.md#L243-L243](https://github.com/2389-research/ourocodus/blob/00bfe36ef93024f4e3ff8c85f68b4b0ca3a243bc/README.md#L243-L243), [README.md#L203-L203](https://github.com/2389-research/ourocodus/blob/00bfe36ef93024f4e3ff8c85f68b4b0ca3a243bc/README.md#L203-L203), [README.md#L207-L212](https://github.com/2389-research/ourocodus/blob/00bfe36ef93024f4e3ff8c85f68b4b0ca3a243bc/README.md#L207-L212)
  - [observation/documented] Repository development practice: contributors are directed to install mise, run mise install, and work through GitHub issues ordered by dependency with acceptance criteria. -- evidence: [README.md#L475-L479](https://github.com/2389-research/ourocodus/blob/00bfe36ef93024f4e3ff8c85f68b4b0ca3a243bc/README.md#L475-L479), [README.md#L471-L471](https://github.com/2389-research/ourocodus/blob/00bfe36ef93024f4e3ff8c85f68b4b0ca3a243bc/README.md#L471-L471)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The documented REST API includes POST/GET/DELETE /api/sessions, GET /api/agents, event tailing and SSE streaming at /api/events, plus /health and /api/info endpoints. -- evidence: [docs/prd/api.md#L55-L56](https://github.com/2389-research/ourocodus/blob/00bfe36ef93024f4e3ff8c85f68b4b0ca3a243bc/docs/prd/api.md#L55-L56), [docs/prd/api.md#L179-L180](https://github.com/2389-research/ourocodus/blob/00bfe36ef93024f4e3ff8c85f68b4b0ca3a243bc/docs/prd/api.md#L179-L180), [docs/prd/api.md#L35-L37](https://github.com/2389-research/ourocodus/blob/00bfe36ef93024f4e3ff8c85f68b4b0ca3a243bc/docs/prd/api.md#L35-L37), [docs/prd/api.md#L167-L169](https://github.com/2389-research/ourocodus/blob/00bfe36ef93024f4e3ff8c85f68b4b0ca3a243bc/docs/prd/api.md#L167-L169), [docs/prd/api.md#L90-L91](https://github.com/2389-research/ourocodus/blob/00bfe36ef93024f4e3ff8c85f68b4b0ca3a243bc/docs/prd/api.md#L90-L91), [docs/prd/api.md#L147-L148](https://github.com/2389-research/ourocodus/blob/00bfe36ef93024f4e3ff8c85f68b4b0ca3a243bc/docs/prd/api.md#L147-L148), [docs/prd/api.md#L100-L101](https://github.com/2389-research/ourocodus/blob/00bfe36ef93024f4e3ff8c85f68b4b0ca3a243bc/docs/prd/api.md#L100-L101), [docs/prd/api.md#L192-L193](https://github.com/2389-research/ourocodus/blob/00bfe36ef93024f4e3ff8c85f68b4b0ca3a243bc/docs/prd/api.md#L192-L193)
  - [observation/documented] The API spec defines structured error responses with codes such as SESSION_NOT_FOUND, and the demo documentation distinguishes recoverable from non-recoverable errors. -- evidence: [docs/prd/api.md#L310-L316](https://github.com/2389-research/ourocodus/blob/00bfe36ef93024f4e3ff8c85f68b4b0ca3a243bc/docs/prd/api.md#L310-L316), [README.md#L444-L447](https://github.com/2389-research/ourocodus/blob/00bfe36ef93024f4e3ff8c85f68b4b0ca3a243bc/README.md#L444-L447), [README.md#L442-L442](https://github.com/2389-research/ourocodus/blob/00bfe36ef93024f4e3ff8c85f68b4b0ca3a243bc/README.md#L442-L442)
- memory-state (1 claim(s)):
More evidence: [full detail](ourocodus.detail.md)

Metadata and full claim list: [full detail](ourocodus.detail.md)
Human notes ([notes](ourocodus.notes.md), never overwritten by build)

[Back to map index](../../index.md)
