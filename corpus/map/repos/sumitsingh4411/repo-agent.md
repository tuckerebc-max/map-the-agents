# sumitsingh4411/repo-agent

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 703c1afdf6f3 @ ff5baa40eebdbcd5

## Summary (orientation draft, not independently verified)

Evidence consists of README and docs/PLUGINS.md describing 'Free Repo Agent', a VS Code extension (SUMITKUMARSINGH.free-repo-agent) offering repo-aware chat, an autonomous self-verifying agent, a terminal CLI, MCP plugins, project memory, and code review, with BYO-key DeepSeek/OpenAI-compatible model access. All prior product claims were supported by cited slices; the license label was dropped as uncited.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (4 claim(s)):
  - [observation/documented] An autonomous agent mode reads files, edits across many files with inline Keep/Undo review, and runs terminal commands with user approval, tracked by a live checklist that can be stopped. -- evidence: [README.md#L190-L194](https://github.com/sumitsingh4411/repo-agent/blob/703c1afdf6f3f6d291e828852af9db361bcb3cc9/README.md#L190-L194), [README.md#L98-L98](https://github.com/sumitsingh4411/repo-agent/blob/703c1afdf6f3f6d291e828852af9db361bcb3cc9/README.md#L98-L98)
  - [observation/documented] After editing, the agent reportedly runs the project's typecheck/build, reads errors, and fixes them before declaring a task done (self-verification). -- evidence: [README.md#L190-L194](https://github.com/sumitsingh4411/repo-agent/blob/703c1afdf6f3f6d291e828852af9db361bcb3cc9/README.md#L190-L194), [README.md#L106-L106](https://github.com/sumitsingh4411/repo-agent/blob/703c1afdf6f3f6d291e828852af9db361bcb3cc9/README.md#L106-L106), [README.md#L404-L408](https://github.com/sumitsingh4411/repo-agent/blob/703c1afdf6f3f6d291e828852af9db361bcb3cc9/README.md#L404-L408)
- design-choices (1 claim(s)):
  - [observation/documented] API keys and plugin tokens are stored in VS Code SecretStorage rather than settings or repo files; the CLI keeps its own key store (~/.repo-agent.json, chmod 600, opt-in) since it cannot read VS Code SecretStorage. -- evidence: [docs/PLUGINS.md#L89-L90](https://github.com/sumitsingh4411/repo-agent/blob/703c1afdf6f3f6d291e828852af9db361bcb3cc9/docs/PLUGINS.md#L89-L90), [README.md#L376-L385](https://github.com/sumitsingh4411/repo-agent/blob/703c1afdf6f3f6d291e828852af9db361bcb3cc9/README.md#L376-L385), [README.md#L235-L237](https://github.com/sumitsingh4411/repo-agent/blob/703c1afdf6f3f6d291e828852af9db361bcb3cc9/README.md#L235-L237)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The product ships as a VS Code extension ('free-repo-agent' on the Marketplace) with a chat panel opened via Cmd/Ctrl+Shift+A or a docked icon, plus 'Agent:' commands in the command palette. -- evidence: [README.md#L339-L350](https://github.com/sumitsingh4411/repo-agent/blob/703c1afdf6f3f6d291e828852af9db361bcb3cc9/README.md#L339-L350), [README.md#L180-L180](https://github.com/sumitsingh4411/repo-agent/blob/703c1afdf6f3f6d291e828852af9db361bcb3cc9/README.md#L180-L180), [README.md#L22-L26](https://github.com/sumitsingh4411/repo-agent/blob/703c1afdf6f3f6d291e828852af9db361bcb3cc9/README.md#L22-L26), [README.md#L337-L337](https://github.com/sumitsingh4411/repo-agent/blob/703c1afdf6f3f6d291e828852af9db361bcb3cc9/README.md#L337-L337), [README.md#L9-L9](https://github.com/sumitsingh4411/repo-agent/blob/703c1afdf6f3f6d291e828852af9db361bcb3cc9/README.md#L9-L9)
  - [observation/documented] A terminal CLI ships inside the extension (v0.10.0+), runnable via an alias to dist/cli.js, with flags like --model, --effort, --cwd, --base-url, --yes, and in-session commands such as /model, /effort, /login. -- evidence: [README.md#L229-L233](https://github.com/sumitsingh4411/repo-agent/blob/703c1afdf6f3f6d291e828852af9db361bcb3cc9/README.md#L229-L233), [README.md#L215-L215](https://github.com/sumitsingh4411/repo-agent/blob/703c1afdf6f3f6d291e828852af9db361bcb3cc9/README.md#L215-L215), [README.md#L219-L220](https://github.com/sumitsingh4411/repo-agent/blob/703c1afdf6f3f6d291e828852af9db361bcb3cc9/README.md#L219-L220)
- memory-state (2 claim(s)):
  - [observation/documented] The agent indexes the repository (symbols, structure, optional AI per-file summaries) into a local .agent-cache/ cache and injects the most relevant files (default 8 via repoAgent.retrieval.maxFiles) into each prompt. -- evidence: [README.md#L333-L333](https://github.com/sumitsingh4411/repo-agent/blob/703c1afdf6f3f6d291e828852af9db361bcb3cc9/README.md#L333-L333), [README.md#L357-L370](https://github.com/sumitsingh4411/repo-agent/blob/703c1afdf6f3f6d291e828852af9db361bcb3cc9/README.md#L357-L370)
  - [observation/documented] A 'Learn this codebase' command writes a knowledge brief to .repo-agent/knowledge.md injected into every prompt, and a memory.md (or .agent.md/.claude.md) at the repo root supplies always-on user rules. -- evidence: [README.md#L254-L254](https://github.com/sumitsingh4411/repo-agent/blob/703c1afdf6f3f6d291e828852af9db361bcb3cc9/README.md#L254-L254), [README.md#L311-L311](https://github.com/sumitsingh4411/repo-agent/blob/703c1afdf6f3f6d291e828852af9db361bcb3cc9/README.md#L311-L311), [README.md#L297-L297](https://github.com/sumitsingh4411/repo-agent/blob/703c1afdf6f3f6d291e828852af9db361bcb3cc9/README.md#L297-L297)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
  - [observation/documented] Plugin tools run without a confirmation prompt by default (repoAgent.plugins.autoRun = true); turning it off yields a Run/Reject prompt per external tool call. File edits are blocked from absolute paths and '..' traversal per the README. -- evidence: [README.md#L376-L385](https://github.com/sumitsingh4411/repo-agent/blob/703c1afdf6f3f6d291e828852af9db361bcb3cc9/README.md#L376-L385), [docs/PLUGINS.md#L74-L75](https://github.com/sumitsingh4411/repo-agent/blob/703c1afdf6f3f6d291e828852af9db361bcb3cc9/docs/PLUGINS.md#L74-L75), [README.md#L357-L370](https://github.com/sumitsingh4411/repo-agent/blob/703c1afdf6f3f6d291e828852af9db361bcb3cc9/README.md#L357-L370)
More evidence: [full detail](repo-agent.detail.md)

Metadata and full claim list: [full detail](repo-agent.detail.md)
Human notes ([notes](repo-agent.notes.md), never overwritten by build)

[Back to map index](../../index.md)
