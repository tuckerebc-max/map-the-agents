# fy0/codekanban

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 921b2512aeb0 @ 6bf09518330b3b17

## Summary (orientation draft, not independently verified)

Selected evidence records: The project is a Go backend paired with a Vue 3.5 / TypeScript 5.8 frontend, per README badges. The product is runnable via `npx codekanban` or a global npm install of the codekanban package.

## Source coverage

Source coverage (partial): 3 of 9 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] The project is a Go backend paired with a Vue 3.5 / TypeScript 5.8 frontend, per README badges. -- evidence: [README.md#L11-L14](https://github.com/fy0/CodeKanban/blob/921b2512aeb00ca37b27a8f711ca6479c0d8b9e0/README.md#L11-L14)
  - [observation/documented] The build produces a single-file executable: frontend artifacts from ui/dist are copied to static/ and embedded into the Go binary. -- evidence: [README.md#L135-L137](https://github.com/fy0/CodeKanban/blob/921b2512aeb00ca37b27a8f711ca6479c0d8b9e0/README.md#L135-L137)
- design-choices (1 claim(s)):
  - [observation/documented] Worktree management uses a hybrid Git engine: go-git for fast in-process reads (status, diff, line stats) and system Git preferred for commits and mutations to preserve hooks, signing, filters, and user config; read and write engines are independently selectable in Settings. -- evidence: [README.md#L43-L46](https://github.com/fy0/CodeKanban/blob/921b2512aeb00ca37b27a8f711ca6479c0d8b9e0/README.md#L43-L46)
- workflows (3 claim(s)):
  - [observation/documented] Repository development practice: AGENTS.md instructs contributors to run `go test ./...` (optionally with -race), regenerate SQLC before committing schema changes, and run `go vet ./...` during review. -- evidence: [AGENTS.md#L7-L11](https://github.com/fy0/CodeKanban/blob/921b2512aeb00ca37b27a8f711ca6479c0d8b9e0/AGENTS.md#L7-L11)
  - [observation/documented] Repository development practice: contributors must format with gofmt, group imports with goimports, use PascalCase/camelCase naming, and write structured zap log fields instead of printf-style strings. -- evidence: [AGENTS.md#L14-L14](https://github.com/fy0/CodeKanban/blob/921b2512aeb00ca37b27a8f711ca6479c0d8b9e0/AGENTS.md#L14-L14)
- skills-patterns (1 claim(s)):
  - [observation/documented] The repo ships an installable Codex skill bundle built around a single public CLI, codekanban-cli, with the skill source at packages/codekanban-cli/skills/codekanban-cli. -- evidence: [README.md#L54-L55](https://github.com/fy0/CodeKanban/blob/921b2512aeb00ca37b27a8f711ca6479c0d8b9e0/README.md#L54-L55), [README.md#L59-L61](https://github.com/fy0/CodeKanban/blob/921b2512aeb00ca37b27a8f711ca6479c0d8b9e0/README.md#L59-L61)
- interfaces (4 claim(s)):
  - [observation/documented] The product is runnable via `npx codekanban` or a global npm install of the codekanban package. -- evidence: [README.md#L22-L23](https://github.com/fy0/CodeKanban/blob/921b2512aeb00ca37b27a8f711ca6479c0d8b9e0/README.md#L22-L23), [README.md#L25-L27](https://github.com/fy0/CodeKanban/blob/921b2512aeb00ca37b27a8f711ca6479c0d8b9e0/README.md#L25-L27)
  - [observation/documented] The backend exposes an OpenAPI docs page at /docs and a health check at /api/v1/health in development. -- evidence: [README.md#L102-L108](https://github.com/fy0/CodeKanban/blob/921b2512aeb00ca37b27a8f711ca6479c0d8b9e0/README.md#L102-L108)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] Development requires Node.js v20.19.0+ or v22.12.0+, Go 1.25+, and pnpm 9.15.9. -- evidence: [README.md#L76-L78](https://github.com/fy0/CodeKanban/blob/921b2512aeb00ca37b27a8f711ca6479c0d8b9e0/README.md#L76-L78)
- limitations: unknown (no source-linked claim submitted for this facet)
- relevance: unknown (no source-linked claim submitted for this facet)

(3 additional claim(s) omitted for length; see [full detail](codekanban.detail.md) for every claim.)

Metadata and full claim list: [full detail](codekanban.detail.md)
Human notes ([notes](codekanban.notes.md), never overwritten by build)

[Back to map index](../../index.md)
