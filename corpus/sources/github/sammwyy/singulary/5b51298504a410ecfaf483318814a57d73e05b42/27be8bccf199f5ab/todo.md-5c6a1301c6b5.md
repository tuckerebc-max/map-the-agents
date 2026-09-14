# Singulary MVP TODO

This file tracks the remaining work needed to turn the current platform foundation into the intended MVP.

## Status Legend

- `[x]` Done
- `[~]` Partial
- `[ ]` Not started

## 1. Platform Foundation

- `[x]` Monorepo with pnpm workspaces.
- `[x]` Express API and Vite React frontend in one production container.
- `[x]` SQLite metadata database.
- `[x]` First setup creates global instance admin.
- `[x]` Login/logout/session cookies.
- `[x]` Admin panel shell.
- `[x]` Groups as the permission source of truth.
- `[x]` Immutable personal group per user.
- `[x]` Group member roles: `group_admin`, `group_member`.
- `[x]` Workspace access through groups.
- `[x]` Rules admin section.
- `[x]` Provider configs with OpenAI-compatible `/models`.
- `[x]` Docker connection config metadata.
- `[x]` Inference + Agent extracted to standalone packages (`@singulary/inference`, `@singulary/agent`).

## 2. Workspace and Project UX

- `[x]` Users can create workspaces.
- `[x]` Users can create projects in workspaces.
- `[x]` Users can create workspace services as metadata.
- `[x]` Create workspace into a selected group (defaults to Personal space).
- `[ ]` Show clear create permissions and limits before submit.
- `[x]` Workspace detail page.
- `[x]` Project detail page.
- `[x]` Service detail page.
- `[ ]` Workspace member/group access management from workspace UI.

## 3. Source Storage

- `[x]` Define storage layout under `storage/workspaces/{workspaceId}/projects/{projectId}`.
- `[x]` Initialize project source from real template scaffolds.
- `[x]` Store source as a materialized working tree.
- `[ ]` Add zip import/export for project source.
- `[x]` Add content-addressed blob store for snapshot files.
- `[x]` Add ignore rules for `node_modules`, build outputs, secrets, and large generated files.
- `[x]` Add filesystem safety checks to prevent path traversal.

## 4. File Explorer and Editor

- `[x]` API: list directory tree.
- `[x]` API: read file.
- `[x]` API: write file.
- `[x]` API: create file/folder.
- `[x]` API: rename file/folder.
- `[x]` API: delete file/folder with approval/risk marker.
- `[x]` Frontend file tree.
- `[x]` Monaco editor integration.
- `[x]` Dirty state and save flow.
- `[x]` Binary/large file handling.

## 5. Snapshots and Branches

- `[x]` Create manual snapshot.
- `[x]` Create automatic snapshot before AI writes (one layer per turn).
- `[x]` Store snapshot metadata.
- `[x]` Store snapshot file tree and blobs (content-addressed).
- `[x]` List snapshots.
- `[x]` Restore whole snapshot (creates a forward checkpoint so nothing is discarded).
- `[x]` Restore single file from snapshot.
- `[x]` Compare snapshots (diff API with added/removed/modified/unchanged).
- `[ ]` Diff viewer (UI panel).
- `[ ]` Branch model (snapshot graph is parent-linked but no explicit branch entity).
- `[ ]` Create branch from snapshot.
- `[ ]` Switch active branch.
- `[~]` Forward/back navigation through snapshot history (checkpoints exist; UI affordance pending).

## 6. Docker Runtime

- `[x]` Docker connection settings exist.
- `[x]` Docker connection check inspects version/info (not only socket/ping).
- `[x]` Create isolated Docker network per workspace.
- `[x]` Start project container from runtime template.
- `[x]` Stop/restart project container.
- `[x]` Stream runtime logs.
- `[x]` Run project commands inside container.
- `[x]` Install dependencies inside container.
- `[x]` Persist runtime metadata.
- `[ ]` Non-root container user where possible.
- `[ ]` Runtime policy checks before privileged actions.

## 7. Workspace Services

- `[x]` Workspace services metadata exists.
- `[x]` Create real PostgreSQL service container.
- `[x]` Create real MySQL service container.
- `[x]` Create real Redis service container.
- `[x]` Create real MongoDB service container.
- `[x]` Generate random service usernames/passwords.
- `[x]` Encrypt service credentials.
- `[x]` Allow permitted users to reveal service credentials.
- `[x]` Generate connection URIs.
- `[x]` Inject connection URIs into selected projects.
- `[x]` Keep DB services internal to workspace network by default.
- `[x]` Service health checks (TCP probe on internal port surfaced in runtime info).
- `[x]` Service logs.
- `[x]` Service delete/recreate flow with explicit warnings.

## 8. Environment Variables and Secrets

- `[x]` Env var table exists.
- `[x]` API for workspace env vars.
- `[x]` API for project env vars.
- `[x]` Secret encryption for env values.
- `[ ]` Secret metadata-only mode for AI context.
- `[x]` Env inheritance: service URIs → workspace env → project env (instance/org levels still pending).
- `[x]` Runtime env injection into project containers.
- `[ ]` Secret reveal permissions.
- `[ ]` Secret rotation.

## 9. Preview and Reverse Proxy

- `[~]` Internal reverse proxy by host header (currently path-based proxy under `/api/projects/:id/preview/:port`).
- `[ ]` Preview host format: `<project-session-id>.<custom-hostname>`.
- `[ ]` Configurable base preview hostname.
- `[ ]` Static domain assignment per workspace/project.
- `[ ]` Ownership/permission checks before assigning a domain.
- `[x]` Route preview traffic to the correct project container.
- `[ ]` Support multiple preview sessions per project.
- `[x]` Preview status in UI.
- `[~]` Preview logs/errors (runtime logs stream exists, dedicated preview errors do not).

## 10. AI Provider Runtime

- `[x]` Provider config metadata exists.
- `[x]` OpenAI-compatible `/models` discovery via backend endpoint.
- `[x]` Model access policy modes: `ALL`, `ALLOW`, `DENY`.
- `[x]` Provider chat completion adapter (in `@singulary/inference`).
- `[x]` Streaming responses.
- `[x]` Token accounting.
- `[x]` Cost estimation (per-model pricing table, persisted on usage records).
- `[x]` Enforce provider access rules at model-call time.
- `[x]` Enforce model access rules at model-call time.
- `[x]` Enforce token quotas per user/group/workspace/global with period windows.
- `[x]` Provider connection test endpoint (`POST /api/admin/providers/:provider/test`).

## 11. Agent Sessions

- `[x]` Agent session table exists.
- `[x]` Agent session API.
- `[x]` Agent messages table/API.
- `[x]` Chat UI in project detail.
- `[x]` Tool call persistence.
- `[x]` Agent status: idle/running/waiting/failed/completed/cancelled.
- `[x]` Cancel running session.
- `[x]` Resume session.
- `[x]` Attach session to workspace/project/branch.

## 12. Agent Tools

- `[x]` Tool registry (`@singulary/agent` `Agent.registerTool` with name/description/parameters/handler).
- `[x]` Risk levels: safe, medium, high, dangerous (via `_risk`).
- `[~]` Permission checks before tool execution (host can inspect `_risk` in events).
- `[x]` Approval checks before risky tools.
- `[x]` `filesystem.list_files`.
- `[x]` `filesystem.read_file`.
- `[x]` `filesystem.write_file`.
- `[x]` `filesystem.apply_patch` (`write_diff`).
- `[x]` `filesystem.create_snapshot` (`create_snapshot`).
- `[x]` `filesystem.restore_snapshot` (`restore_snapshot`).
- `[x]` `shell.run` inside project container (`shell_open`).
- `[x]` `runtime.start` (auto-start + `container_restart`).
- `[~]` `runtime.stop` (lifecycle stops on idle, no explicit tool).
- `[~]` `runtime.logs` (HTTP/WS streams + buffered fetch, no agent tool yet).
- `[ ]` `provider.chat`.
- `[x]` Tool output streaming to UI.
- `[x]` Per-tool `_timeout` and global `_defaultTimeout` honored by the agent loop.

## 13. Approvals and Audit

- `[x]` Audit log table exists.
- `[x]` Admin events are audited (settings, users, groups, providers, quotas, Docker config).
- `[x]` Approval request table usage.
- `[x]` Approval UI.
- `[x]` Approve/reject actions.
- `[ ]` Modify approval actions.
- `[x]` Show risk level, reason, command/diff, and impact.
- `[x]` Audit every high-risk file delete + agent shell + service creation + container restart + snapshot operation.
- `[x]` Audit every shell command (logged as `agent.tool_called.high`).
- `[ ]` Audit every secret reveal.
- `[x]` Audit every service/container action (workspace_service.* + agent tool audit).

## 14. Rules and Permissions

- `[x]` Group rules table exists.
- `[x]` Rules admin UI exists.
- `[x]` Policy evaluation service (`modules/policy/policy-service.ts`).
- `[x]` Enforce provider access rules.
- `[x]` Enforce model access rules.
- `[x]` Enforce token quota rules.
- `[x]` Enforce workspace access rules everywhere (project/workspace/service/snapshot routes check group membership).
- `[x]` Enforce workspace creation limits by group.
- `[x]` Enforce project creation limits by group.
- `[ ]` Prevent confusing duplicate/conflicting rules or show effective policy.
- `[ ]` Effective permissions viewer for a user/group.

## 15. Templates

- `[x]` React + Vite template (full scaffold: package.json, vite.config, App.jsx).
- `[x]` Express API template (full scaffold: package.json, index.js).
- `[x]` Static site template.
- `[x]` Worker template (Node loop scaffold).
- `[x]` Custom Dockerfile template (Ubuntu base for now).
- `[x]` Template metadata: commands, ports, env, healthcheck.
- `[x]` Template selection in UI.

## 16. Tests and Quality

- `[ ]` API tests for setup/auth.
- `[ ]` API tests for groups/rules.
- `[ ]` API tests for workspaces/projects/services.
- `[ ]` API tests for provider configs/model filtering.
- `[ ]` API tests for limits enforcement.
- `[ ]` File storage tests.
- `[ ]` Snapshot tests.
- `[ ]` Runtime service tests.
- `[ ]` Frontend smoke tests.
- `[ ]` Docker build test.
- `[ ]` Add lint/format scripts.

## 17. Documentation

- `[x]` Architecture overview.
- `[x]` Permissions and rules document.
- `[x]` Roadmap.
- `[x]` MVP TODO.
- `[ ]` API reference.
- `[ ]` Runtime architecture document.
- `[ ]` Snapshot storage document.
- `[ ]` Agent tool document.
- `[ ]` Local development guide.
- `[ ]` Production/self-hosting guide.

## Recommended Next Implementation Order

1. Snapshot diff viewer UI + back/forward navigation affordance.
2. Workspace member/group access management UI.
3. Workspace-level env vars UI (API already exists).
4. Subdomain-based preview reverse proxy + multi-session preview.
5. Org/instance env inheritance levels.
6. Effective permissions viewer for users/groups.
7. Non-root container users + runtime policy gates.
8. Lint/format and automated test scaffolding.
9. Long-form docs: API reference, runtime architecture, snapshot store, agent tools.
