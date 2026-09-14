# dcouple/pane

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit df04c767aa66 @ 8a95ecdbaaeaa09d

## Summary (orientation draft, not independently verified)

Selected evidence records: Pane ships a runpane CLI intended for agent use, including agent-context, repos add/list, and panes create for registering repositories and opening panes with prompts. runpane agent-context is token-efficient by default, printing only command names, arguments, and usage notes, with per-command detail available via --command and --json.

## Source coverage

Source coverage (partial): 3 of 34 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 14 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

14 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] Pane is organized around two primitives, panes and tabs: each pane maps to one git worktree and contains tabs for agents, diff viewer, file explorer, git tree, logs, and terminals, with state persisting across restarts. -- evidence: [README.md#L238-L238](https://github.com/dcouple/Pane/blob/df04c767aa669d953f9624a6f0a66782582522f4/README.md#L238-L238)
- design-choices (2 claim(s)):
  - [observation/documented] Pane is agent-agnostic: any CLI tool that runs in a terminal runs in Pane with no plugins or SDK, and the terminal serves as the integration layer rather than Pane re-implementing agent integrations. -- evidence: [README.md#L96-L96](https://github.com/dcouple/Pane/blob/df04c767aa669d953f9624a6f0a66782582522f4/README.md#L96-L96), [README.md#L244-L244](https://github.com/dcouple/Pane/blob/df04c767aa669d953f9624a6f0a66782582522f4/README.md#L244-L244), [README.md#L240-L240](https://github.com/dcouple/Pane/blob/df04c767aa669d953f9624a6f0a66782582522f4/README.md#L240-L240)
  - [observation/documented] Each pane gets its own worktree, port range, and copy of secrets so parallel agents run in isolated workspaces without conflicts, and worktrees are created and torn down automatically with panes. -- evidence: [README.md#L408-L409](https://github.com/dcouple/Pane/blob/df04c767aa669d953f9624a6f0a66782582522f4/README.md#L408-L409), [README.md#L405-L406](https://github.com/dcouple/Pane/blob/df04c767aa669d953f9624a6f0a66782582522f4/README.md#L405-L406)
- workflows (3 claim(s)):
  - [observation/documented] Repository development practice: the repo is a pnpm workspace with main (Electron main process), frontend (React+Vite), shared types, and Playwright E2E tests; dev runs via pnpm dev and builds via pnpm build with per-platform build scripts. -- evidence: [AGENTS.md#L4-L8](https://github.com/dcouple/Pane/blob/df04c767aa669d953f9624a6f0a66782582522f4/AGENTS.md#L4-L8), [README.md#L430-L435](https://github.com/dcouple/Pane/blob/df04c767aa669d953f9624a6f0a66782582522f4/README.md#L430-L435), [AGENTS.md#L11-L19](https://github.com/dcouple/Pane/blob/df04c767aa669d953f9624a6f0a66782582522f4/AGENTS.md#L11-L19)
  - [observation/documented] Repository development practice: contributors use TypeScript with 2-space indentation, no explicit any (ESLint error level), kebab-case filenames, and must run pnpm lint and pnpm typecheck before sending PRs. -- evidence: [AGENTS.md#L22-L26](https://github.com/dcouple/Pane/blob/df04c767aa669d953f9624a6f0a66782582522f4/AGENTS.md#L22-L26)
- skills-patterns (1 claim(s)):
  - [observation/documented] Pane Chat writes local orchestrator skills in Codex, Claude, and Cursor formats (e.g. .codex/skills/pane-orchestrator/SKILL.md) and caches workflow skills including discussion, plan, implement, implementation-reviewer, prepare-pr, investigate, and commit from a skills repository. -- evidence: [README.md#L209-L209](https://github.com/dcouple/Pane/blob/df04c767aa669d953f9624a6f0a66782582522f4/README.md#L209-L209), [README.md#L203-L207](https://github.com/dcouple/Pane/blob/df04c767aa669d953f9624a6f0a66782582522f4/README.md#L203-L207)
- interfaces (4 claim(s)):
  - [observation/documented] Pane ships a runpane CLI intended for agent use, including agent-context, repos add/list, and panes create for registering repositories and opening panes with prompts. -- evidence: [README.md#L221-L226](https://github.com/dcouple/Pane/blob/df04c767aa669d953f9624a6f0a66782582522f4/README.md#L221-L226), [README.md#L118-L133](https://github.com/dcouple/Pane/blob/df04c767aa669d953f9624a6f0a66782582522f4/README.md#L118-L133)
  - [observation/documented] runpane agent-context is token-efficient by default, printing only command names, arguments, and usage notes, with per-command detail available via --command and --json. -- evidence: [README.md#L228-L228](https://github.com/dcouple/Pane/blob/df04c767aa669d953f9624a6f0a66782582522f4/README.md#L228-L228)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
More evidence: [full detail](pane.detail.md)

Metadata and full claim list: [full detail](pane.detail.md)
Human notes ([notes](pane.notes.md), never overwritten by build)

[Back to map index](../../index.md)
