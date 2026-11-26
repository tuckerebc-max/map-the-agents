# Roadmap

## Released

- Git-backed project records
- Project kickoff cards
- Handoff package draft
- Knowledge capture
- Local JSON persistence
- Open-source adapter documentation for Git, AI provider, knowledge, and deployment
- Apache-2.0 license
- Docker Compose for local evaluation
- Short-lived, project-scoped AI credentials with revocation and audit history
- Idempotent AI progress events with server-derived agent identity
- Stdio MCP server for Codex
- CI build, syntax checks, and Agent API acceptance test
- Fail-closed Codex MCP capability preflight
- Project-state `codex:doctor` connection and context check with normal credential-use auditing
- Strict project-level Codex tool allowlist
- Workspace-membership-only administrator authorization regression test
- Fail-closed default-workspace owner bootstrap and migration regression tests

## Now

- Publish and validate the v0.3.0 Codex First-Run Contract
- Add a short end-to-end workflow GIF
- Finish remaining workspace and project permission regression tests
- Add a beginner onboarding path for the first project and first MCP connection
- Remove remaining legacy project-key and placeholder UI paths after migration
- Collect real issue and setup feedback without inventing adoption metrics

## Next — v0.4.0 guided Codex onboarding

- Import repository `AGENTS.md` rules and acceptance criteria into project context
- Add a real workspace-scoped onboarding status API and a Connect Codex checklist
- Record server-side evidence of a successful MCP context read before showing a connected state
- Add a clean-clone acceptance workflow for each supported Node.js version
- Keep merge, release, permission, deletion, deployment, and security decisions human-controlled

## Later

- Read-only dashboard and next-action tools
- Handoff-draft and knowledge-draft tools with human approval gates
- Optional PostgreSQL storage adapter
- Optional Gitea/GitLab/GitHub Enterprise Git adapter
- Remote Streamable HTTP MCP with OAuth and per-project approval gates
- Opt-in maintainer workflows for issue triage, PR review, CI diagnosis, and release-note drafts
- Provider adapter examples without private secrets
- Playwright visual regression checks
- Public plugin marketplace for project templates
- Timeline analytics
- Handoff quality scoring
- Multi-language docs
