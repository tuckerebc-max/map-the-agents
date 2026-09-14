# hyperaiteam/clitrigger

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit d9dabe2c719d @ 2cd220238205759b

## Summary (orientation draft, not independently verified)

CLITrigger is a README-documented web/desktop IDE for AI CLI agents built around a five-stage pipeline (Docs, Plan, Terminal, Autonomous Tasks, Version Control) with parallel git-worktree execution, scheduling, an MCP server, and a built-in Git client. All evidence is documentation; no code-level or benchmark evidence is present. Evidence coverage: 162 of 218 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 3 of 143 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 13 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

13 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] CLITrigger is described as an IDE for AI CLI agents, unifying docs, plans, terminals, autonomous agents, and git into one workspace instead of five scattered tools. -- evidence: [README.md#L9-L9](https://github.com/HyperAITeam/CLITrigger/blob/d9dabe2c719d7e04c8e2e784305d6553334cc6e2/README.md#L9-L9), [README.md#L11-L11](https://github.com/HyperAITeam/CLITrigger/blob/d9dabe2c719d7e04c8e2e784305d6553334cc6e2/README.md#L11-L11)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (1 claim(s)):
  - [observation/documented] The product is organized around a five-stage pipeline — Docs, Plan, Terminal, Autonomous Tasks, Version Control — where each stage consumes the previous stage's context, with lessons feeding back into docs. -- evidence: [README.md#L73-L73](https://github.com/HyperAITeam/CLITrigger/blob/d9dabe2c719d7e04c8e2e784305d6553334cc6e2/README.md#L73-L73), [README.md#L45-L51](https://github.com/HyperAITeam/CLITrigger/blob/d9dabe2c719d7e04c8e2e784305d6553334cc6e2/README.md#L45-L51), [README.md#L53-L60](https://github.com/HyperAITeam/CLITrigger/blob/d9dabe2c719d7e04c8e2e784305d6553334cc6e2/README.md#L53-L60)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: running from source involves cloning, npm install in root and src/client, copying .env.example to .env, and `npm run dev` with the dev server at localhost:5173; tests run via `npm test` or scripts/test.bat. -- evidence: [README.md#L280-L285](https://github.com/HyperAITeam/CLITrigger/blob/d9dabe2c719d7e04c8e2e784305d6553334cc6e2/README.md#L280-L285), [README.md#L258-L259](https://github.com/HyperAITeam/CLITrigger/blob/d9dabe2c719d7e04c8e2e784305d6553334cc6e2/README.md#L258-L259), [README.md#L247-L250](https://github.com/HyperAITeam/CLITrigger/blob/d9dabe2c719d7e04c8e2e784305d6553334cc6e2/README.md#L247-L250), [README.md#L253-L253](https://github.com/HyperAITeam/CLITrigger/blob/d9dabe2c719d7e04c8e2e784305d6553334cc6e2/README.md#L253-L253), [README.md#L261-L261](https://github.com/HyperAITeam/CLITrigger/blob/d9dabe2c719d7e04c8e2e784305d6553334cc6e2/README.md#L261-L261), [README.md#L267-L274](https://github.com/HyperAITeam/CLITrigger/blob/d9dabe2c719d7e04c8e2e784305d6553334cc6e2/README.md#L267-L274)
  - [observation/documented] Repository development practice: contributors are invited to file issues, open PRs (starting with 'good first issue' labels), and share workflows in Discussions; docs include CICD.md for GitHub Actions CI/CD and TESTING.md. -- evidence: [README.md#L334-L336](https://github.com/HyperAITeam/CLITrigger/blob/d9dabe2c719d7e04c8e2e784305d6553334cc6e2/README.md#L334-L336), [README.md#L318-L324](https://github.com/HyperAITeam/CLITrigger/blob/d9dabe2c719d7e04c8e2e784305d6553334cc6e2/README.md#L318-L324)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] An MCP server exposes CLITrigger over HTTP so MCP clients like Claude Desktop or Claude Code can list projects, create and run tasks, and check status; config (URL + token) is copied from Settings. -- evidence: [README.md#L183-L183](https://github.com/HyperAITeam/CLITrigger/blob/d9dabe2c719d7e04c8e2e784305d6553334cc6e2/README.md#L183-L183)
  - [observation/documented] The CLI supports configuration commands such as `clitrigger config port 8080` to change the port and `clitrigger config tunnel on` to enable Cloudflare tunnel sharing. -- evidence: [README.md#L231-L233](https://github.com/HyperAITeam/CLITrigger/blob/d9dabe2c719d7e04c8e2e784305d6553334cc6e2/README.md#L231-L233)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (3 claim(s)):
  - [observation/documented] Each TODO runs in its own isolated git worktree, with Claude, Antigravity, and Codex executing in parallel, plus dependency chains and merge control. -- evidence: [README.md#L77-L80](https://github.com/HyperAITeam/CLITrigger/blob/d9dabe2c719d7e04c8e2e784305d6553334cc6e2/README.md#L77-L80), [README.md#L129-L129](https://github.com/HyperAITeam/CLITrigger/blob/d9dabe2c719d7e04c8e2e784305d6553334cc6e2/README.md#L129-L129)
  - [observation/documented] A multi-agent discussion feature has architect, developer, and reviewer agents debate before implementation, then commit code or send action items to the planner. -- evidence: [README.md#L132-L132](https://github.com/HyperAITeam/CLITrigger/blob/d9dabe2c719d7e04c8e2e784305d6553334cc6e2/README.md#L132-L132), [README.md#L77-L80](https://github.com/HyperAITeam/CLITrigger/blob/d9dabe2c719d7e04c8e2e784305d6553334cc6e2/README.md#L77-L80)
- tools-permissions (1 claim(s)):
More evidence: [full detail](clitrigger.detail.md)

Metadata and full claim list: [full detail](clitrigger.detail.md)
Human notes ([notes](clitrigger.notes.md), never overwritten by build)

[Back to map index](../../index.md)
