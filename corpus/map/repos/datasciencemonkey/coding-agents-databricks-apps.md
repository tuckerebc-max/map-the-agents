# datasciencemonkey/coding-agents-databricks-apps

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit e4a4b216e439 @ d20a4ad5ff34cf66

## Summary (orientation draft, not independently verified)

A Databricks Apps template that runs five coding-agent CLIs (Claude Code, Codex, Gemini CLI, Hermes Agent, OpenCode) in a browser terminal wired to a Databricks workspace, with bundled skills, MCP servers, MLflow tracing, and PAT-based auth; the project has moved to Databricks Labs. Evidence coverage: 143 of 177 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 18 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 19 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

19 claim(s) across 11 facet(s); 2 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] The project lets users run Claude Code, Codex, Gemini CLI, Hermes Agent, and OpenCode in a browser, connected to their Databricks workspace with no local setup. -- evidence: [README.md#L11-L11](https://github.com/datasciencemonkey/coding-agents-databricks-apps/blob/e4a4b216e43998f7243d922e1b6e3d4e85efc18e/README.md#L11-L11)
- components (3 claim(s)):
  - [observation/documented] The repo bundles five agents: Claude Code (with 39 Databricks skills and 2 MCP servers), Codex, Gemini CLI, Hermes Agent, and OpenCode, each installed at boot. -- evidence: [README.md#L35-L35](https://github.com/datasciencemonkey/coding-agents-databricks-apps/blob/e4a4b216e43998f7243d922e1b6e3d4e85efc18e/README.md#L35-L35), [README.md#L33-L33](https://github.com/datasciencemonkey/coding-agents-databricks-apps/blob/e4a4b216e43998f7243d922e1b6e3d4e85efc18e/README.md#L33-L33), [README.md#L27-L27](https://github.com/datasciencemonkey/coding-agents-databricks-apps/blob/e4a4b216e43998f7243d922e1b6e3d4e85efc18e/README.md#L27-L27), [README.md#L25-L25](https://github.com/datasciencemonkey/coding-agents-databricks-apps/blob/e4a4b216e43998f7243d922e1b6e3d4e85efc18e/README.md#L25-L25), [README.md#L29-L29](https://github.com/datasciencemonkey/coding-agents-databricks-apps/blob/e4a4b216e43998f7243d922e1b6e3d4e85efc18e/README.md#L29-L29), [README.md#L31-L31](https://github.com/datasciencemonkey/coding-agents-databricks-apps/blob/e4a4b216e43998f7243d922e1b6e3d4e85efc18e/README.md#L31-L31)
  - [observation/documented] Two MCP servers are included: DeepWiki for AI-powered questions about GitHub repos, and Exa for web search and code context retrieval. -- evidence: [README.md#L206-L209](https://github.com/datasciencemonkey/coding-agents-databricks-apps/blob/e4a4b216e43998f7243d922e1b6e3d4e85efc18e/README.md#L206-L209)
- design-choices (4 claim(s)):
  - [observation/documented] On first terminal session the user pastes a short-lived PAT that configures all CLIs; tokens auto-rotate every 10 minutes and are not persisted across restarts by design. -- evidence: [README.md#L35-L35](https://github.com/datasciencemonkey/coding-agents-databricks-apps/blob/e4a4b216e43998f7243d922e1b6e3d4e85efc18e/README.md#L35-L35), [README.md#L372-L372](https://github.com/datasciencemonkey/coding-agents-databricks-apps/blob/e4a4b216e43998f7243d922e1b6e3d4e85efc18e/README.md#L372-L372)
  - [observation/documented] An approved design doc records bundling skills into the image rather than downloading at startup, citing faster startup, no network dependency, and predictability as reasons. -- evidence: [docs/plans/2025-02-03-bundled-skills-design.md#L3-L4](https://github.com/datasciencemonkey/coding-agents-databricks-apps/blob/e4a4b216e43998f7243d922e1b6e3d4e85efc18e/docs/plans/2025-02-03-bundled-skills-design.md#L3-L4), [docs/plans/2025-02-03-bundled-skills-design.md#L164-L170](https://github.com/datasciencemonkey/coding-agents-databricks-apps/blob/e4a4b216e43998f7243d922e1b6e3d4e85efc18e/docs/plans/2025-02-03-bundled-skills-design.md#L164-L170)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns (1 claim(s)):
  - [observation/documented] The app bundles 39 skills: 25 Databricks skills from ai-dev-kit (agent-bricks, genie, mlflow-eval, unity-catalog, etc.) and 14 superpowers skills (TDD, debugging, review, git-worktrees, etc.). -- evidence: [README.md#L180-L188](https://github.com/datasciencemonkey/coding-agents-databricks-apps/blob/e4a4b216e43998f7243d922e1b6e3d4e85efc18e/README.md#L180-L188), [README.md#L192-L199](https://github.com/datasciencemonkey/coding-agents-databricks-apps/blob/e4a4b216e43998f7243d922e1b6e3d4e85efc18e/README.md#L192-L199), [README.md#L25-L25](https://github.com/datasciencemonkey/coding-agents-databricks-apps/blob/e4a4b216e43998f7243d922e1b6e3d4e85efc18e/README.md#L25-L25)
- interfaces (3 claim(s)):
  - [observation/documented] The app exposes HTTP endpoints including /health, /api/session, /api/input, /api/output, /api/output-batch, /api/heartbeat, /api/resize, /api/upload, and /api/session/close. -- evidence: [README.md#L325-L338](https://github.com/datasciencemonkey/coding-agents-databricks-apps/blob/e4a4b216e43998f7243d922e1b6e3d4e85efc18e/README.md#L325-L338)
  - [observation/documented] Socket.IO events include join_session, terminal_input, terminal_resize, heartbeat (client-to-server) and terminal_output, session_exited, session_closed, shutting_down (server-to-client). -- evidence: [README.md#L342-L352](https://github.com/datasciencemonkey/coding-agents-databricks-apps/blob/e4a4b216e43998f7243d922e1b6e3d4e85efc18e/README.md#L342-L352)
- memory-state (1 claim(s)):
  - [observation/documented] A state_sync.py process persists Claude Code auto-memory and bash history to /Workspace/Users/{email}/.state/ every 5 minutes, since only /Workspace files survive container restarts. -- evidence: [docs/2026-03-08-tmux-evaluation.md#L40-L42](https://github.com/datasciencemonkey/coding-agents-databricks-apps/blob/e4a4b216e43998f7243d922e1b6e3d4e85efc18e/docs/2026-03-08-tmux-evaluation.md#L40-L42), [docs/2026-03-08-tmux-evaluation.md#L22-L25](https://github.com/datasciencemonkey/coding-agents-databricks-apps/blob/e4a4b216e43998f7243d922e1b6e3d4e85efc18e/docs/2026-03-08-tmux-evaluation.md#L22-L25)
- orchestration (1 claim(s)):
  - [observation/documented] At startup, Gunicorn calls initialize_app(), then a background thread runs 5 sequential setup steps followed by 6 agent setups in parallel via ThreadPoolExecutor, with progress reported through /api/setup-status. -- evidence: [README.md#L317-L321](https://github.com/datasciencemonkey/coding-agents-databricks-apps/blob/e4a4b216e43998f7243d922e1b6e3d4e85efc18e/README.md#L317-L321)
- tools-permissions (1 claim(s)):
More evidence: [full detail](coding-agents-databricks-apps.detail.md)

Metadata and full claim list: [full detail](coding-agents-databricks-apps.detail.md)
Human notes ([notes](coding-agents-databricks-apps.notes.md), never overwritten by build)

[Back to map index](../../index.md)
