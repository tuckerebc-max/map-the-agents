# Singulary Roadmap

This roadmap tracks implementation status one item at a time. Status values:

- `Done`: implemented in the current scaffold.
- `In progress`: partially implemented or structurally prepared.
- `Planned`: not implemented yet.

## 1. Monorepo Foundation

- `Done` Create pnpm workspace monorepo named `singulary`.
- `Done` Add shared TypeScript package for API/domain types.
- `Done` Add pnpm root scripts for development, build, start, typecheck, setup status, and admin creation.
- `Done` Add baseline documentation in `README.md` and `docs/architecture.md`.
- `Done` Add storage folder placeholder for local persistent data.

## 2. Local Database

- `Done` Use SQLite instead of PostgreSQL.
- `Done` Initialize SQLite automatically on backend startup.
- `Done` Create MVP tables for users, sessions, organizations, workspaces, projects, provider keys, agent sessions, snapshots, env vars, usage records, audit logs, and approvals.
- `Done` Add workspace services table for databases, cache, queues, object storage, search, and custom services.
- `Done` Add agent messages and agent tool calls tables for persistent chat history.
- `Planned` Add database migrations with version tracking.
- `Planned` Add seed fixtures for local development.

## 3. Backend API

- `Done` Build Express server with JSON parsing, cookies, CORS in development, and production static frontend serving.
- `Done` Expose `/api/health`.
- `Done` Expose `/api/setup/status`.
- `Done` Expose `/api/setup/complete` for first admin setup.
- `Done` Expose `/api/auth/login`, `/api/auth/logout`, and `/api/auth/me`.
- `Done` Expose workspace list and create endpoints.
- `Done` Expose project list and create endpoints.
- `Done` Expose project file explorer (list/read/write/create/rename/copy/delete).
- `Done` Expose project env var CRUD endpoints.
- `Done` Expose project runtime endpoints (status, actions, logs, shells).
- `Done` Expose project preview reverse proxy by port.
- `Done` Expose workspace service list, create, runtime, logs, and action endpoints.
- `Done` Expose service templates and project templates endpoints.
- `Done` Expose provider key list and create endpoints.
- `Done` Expose agent session, message, stream, and cancel endpoints.
- `Done` Expose dashboard summary endpoint.
- `Done` Expose admin APIs for platform summary, settings, users, groups, workspaces, global provider keys, token quotas, and permission policies.
- `Planned` Add update/delete endpoints with audit logging.
- `Planned` Add pagination and filtering for large local instances.

## 4. Authentication and Setup

- `Done` First setup asks for display name, username, email, and password.
- `Done` First setup creates the user as global `instance_admin`.
- `Done` First setup creates a default personal organization.
- `Done` Passwords are hashed with scrypt.
- `Done` Sessions use HTTP-only cookies.
- `Done` Short-lived WebSocket auth tokens for terminal and event streams.
- `Done` CLI script creates `admin:<random password>` when password is omitted.
- `Planned` Add password change flow.
- `Planned` Add multi-user invitation flow.

## 5. Provider Keys and Secrets

- `Done` Add provider key metadata model.
- `Done` Add admin provider configuration with OpenAI-compatible base URL and encrypted API key.
- `Done` Encrypt provider key values at rest with AES-GCM.
- `Done` Do not return secret values from API responses.
- `Done` Add admin-controlled BYOK toggle.
- `Done` Add admin-controlled global provider key toggle.
- `Done` Restrict global provider key creation to instance admins.
- `Done` Add provider model discovery through configured OpenAI-compatible `/models` endpoints.
- `Done` Add `/models/all` for unfiltered provider model discovery and `/models` for policy-filtered model access.
- `Planned` Add provider connection checks.
- `Planned` Add provider key scopes beyond basic metadata enforcement.
- `Planned` Add key rotation and deletion.

## 6. Frontend Shell

- `Done` Build Vite React app.
- `Done` Add Tailwind CSS.
- `Done` Add React Router routes.
- `Done` Add Zustand auth store.
- `Done` Refactor frontend into services, stores, hooks, views, utils, and component subfolders.
- `Done` Add service/store/hook data flow for auth, dashboard, workspaces, and provider keys.
- `Done` Add setup wizard.
- `Done` Add login page.
- `Done` Add authenticated app layout.
- `Done` Add dashboard page.
- `Done` Add workspace and project management page.
- `Done` Add workspace detail page.
- `Done` Add project detail page with code/preview/environment/settings tabs.
- `Done` Add Monaco editor + file tree with dirty/save flow.
- `Done` Add agent chat panel with model selector and tool call streaming.
- `Done` Add terminal/log panel and shell tabs.
- `Done` Add service detail page.
- `Done` Add provider keys page.
- `Done` Add runtime placeholder page.
- `Done` Add settings page.
- `Done` Add nested Admin Panel sidebar section.
- `Done` Add `/admin` views for overview, users, groups, workspaces, permissions, token quotas, global keys, and platform settings.
- `Planned` Add responsive mobile navigation.
- `Planned` Add toast notifications and field-level validation.

## 6.1 Admin Platform Controls

- `Done` Groups are the source of truth for permissions and limits.
- `Done` Every user gets an immutable personal group named Personal space.
- `Done` Group members support `group_admin` and `group_member` roles.
- `Done` Workspaces can be attached to groups for access control.
- `Done` Rules section can configure provider/model access, token quotas, workspace limits, project limits, and workspace access.
- `Done` Dashboard shows the current user's groups, Personal space, visible workspaces, and limits.
- `Done` Platform settings can enable or disable BYOK.
- `Done` Platform settings can enable or disable global provider keys.
- `Done` Platform settings can require approval for dangerous tools.
- `Done` Platform settings can define an optional default token quota.
- `Done` Admin users view can update global roles.
- `Done` Admin groups view can create groups and assign or remove members.
- `Done` Admin quotas view can create global, group, user, and workspace token quotas.
- `Done` Admin quotas can target all providers or a specific configured provider.
- `Done` Admin permissions view can create allow/deny policy records.
- `Done` Admin global keys view can create platform-level provider keys.
- `Done` Admin model access view supports provider policies in ALL, ALLOW, and DENY mode.
- `Done` Admin provider access policies can allow or deny providers by group, user, or globally.
- `Done` Admin Docker view configures socket or TCP connection settings.
- `Done` Admin Docker connection check inspects version + info, not just socket existence.
- `Done` Policy evaluation service enforces provider access, model access, and token quotas on every model call.
- `Done` Quota enforcement during model calls (user, group, workspace, global scopes; daily/weekly/monthly/lifetime windows).
- `Done` Provider connection test endpoint (`POST /api/admin/providers/:provider/test`).
- `Planned` Add group deletion and audit-safe user deactivation.

## 7. Development Workflow

- `Done` Root `npm run dev` starts frontend and backend concurrently.
- `Done` Vite development proxy routes `/api` to the backend.
- `Done` Root `npm run build` builds shared package, backend, and frontend.
- `Planned` Add linting and formatting scripts.
- `Planned` Add automated tests.

## 8. Production Container

- `Done` Add a single production Dockerfile.
- `Done` Add `docker-compose.yml` for one service.
- `Done` Serve frontend from `/`.
- `Done` Serve backend from `/api`.
- `Done` Persist SQLite data in a Docker volume.
- `Planned` Add healthcheck to Docker Compose.
- `Planned` Add non-default `SESSION_SECRET` validation in production.

## 9. Workspace Runtime

- `Done` Data model supports workspaces and projects.
- `Done` Workspace services model replaces project type for databases and shared infrastructure.
- `Done` Add Docker Engine connection settings.
- `Done` Add workspace network creation.
- `Done` Add project container lifecycle management (start, stop, restart, destroy).
- `Done` Add runtime logs endpoint with rolling buffer and live WebSocket stream.
- `Done` Add preview URL forwarding (path-based proxy by port).
- `Done` Add per-project environment injection from project env vars and workspace service connection URIs.
- `Done` Add idle auto-stop when no clients are connected.
- `Done` Add interactive shell containers attached to project workdir.
- `Planned` Add subdomain-based preview reverse proxy.
- `Planned` Add multiple preview sessions per project.

## 10. Filesystem and Snapshots

- `Done` Snapshot metadata table exists.
- `Done` Add materialized draft source storage under `storage/workspaces/...`.
- `Done` Add file explorer API (list/read/write/create/rename/copy/delete).
- `Done` Add file ignore + path-traversal safety.
- `Done` Content-addressed blob storage + tree objects (`storage/snapshots/blobs|trees`).
- `Done` Snapshot create / list / restore (whole + single file).
- `Done` Diff generation between two snapshots (added/removed/modified/unchanged).
- `Done` Automatic pre-write snapshot per agent turn (one layer per turn, host-keyed by sessionId).
- `Done` Restore creates a forward checkpoint so back/forward navigation is non-destructive.
- `Planned` Diff viewer UI.
- `Planned` Explicit branch entity (snapshots already form a parent-linked DAG).

## 11. AI Agent System

- `Done` Provider abstraction extracted to standalone `@singulary/inference` package (OpenAI-compatible across providers, streaming + tool calls + ALL-model listing).
- `Done` Tool-calling agent loop extracted to standalone `@singulary/agent` package.
- `Done` Agent config supports `_`-prefixed agent-only keys (`_maxLoops`, `_defaultTimeout`, `_llmTimeoutMs`); rest pass-through to LLM.
- `Done` Per-tool `_timeout` (seconds) honored by the loop with AbortController, default falls back to `_defaultTimeout`.
- `Done` Per-tool `_risk` (safe/medium/high/dangerous) emitted on events so the host can audit/gate.
- `Done` Per-tool `_preExecute` hook (used to take pre-write snapshots).
- `Done` Add agent sessions and messages API.
- `Done` Add per-session SSE event stream with cancellation.
- `Done` Add agent tool definitions (filesystem read/write/diff/list/delete/move/copy/find, shell open/read/wait/kill, project settings, service provisioning, container restart, create_snapshot, list_snapshots, restore_snapshot).
- `Done` Add agent .gitignore-aware file operations.
- `Done` Add streaming chat responses with token usage recording.
- `Done` Add automatic snapshots before AI writes (one per turn).
- `Done` Add approval requests for risky tools.
- `Planned` Add specialized agents (planner, reviewer, runtime).

## 12. Security and Audit

- `Done` Audit log table exists.
- `Done` Audit records are created for admin creation, login, workspace creation, project creation, service creation, provider key creation, and Docker config changes.
- `Done` Secret values are encrypted and hidden from API responses.
- `Done` Service credentials are encrypted and only revealed via the service detail endpoint to permitted users.
- `Done` Workspace/project routes verify group membership for every read/write action.
- `Done` Policy service enforces provider/model/quota at every model call.
- `Done` Audit risky agent tool calls (high/dangerous) including shell, service create, restart, file deletes, snapshot ops.
- `Done` Audit snapshot create/restore/file-restore actions.
- `Done` Add approval UI.
- `Planned` Add secret metadata-only access for AI context.
- `Planned` Add production security hardening checklist.

## 13. Usage and Quotas

- `Done` Usage records table exists.
- `Done` Token budget table and admin creation UI exist.
- `Done` Add token usage recording per chat completion (input/output/total tokens, cached tokens).
- `Done` Model cost metadata + per-call estimated cost stored in usage records.
- `Done` Token budgets enforced by user, group, workspace, and global scopes with daily/weekly/monthly/lifetime period windows.
- `Done` Hard limits enforced before model calls.
- `Planned` Soft warnings before hitting hard limits.

## 14. Workspace Services

- `Done` Service templates: PostgreSQL, MySQL, MariaDB, MongoDB, Redis, MinIO, RabbitMQ, Meilisearch.
- `Done` Generated credentials encrypted at rest, revealed via service detail endpoint to permitted users.
- `Done` Connection URIs rendered from templates and injected into project containers as env vars.
- `Done` TCP health probe on the internal port; healthy/healthMessage exposed in runtime info.
- `Done` Service lifecycle actions: start, stop, restart, destroy with explicit warnings.

## 15. Near-Term Implementation Order

1. Snapshot diff viewer UI + back/forward navigation affordance.
2. Workspace member/group access management UI.
3. Workspace-level env vars UI (API already exists).
4. Subdomain-based preview reverse proxy + multi-session preview.
5. Org/instance env inheritance levels.
6. Effective permissions viewer for users/groups.
7. Non-root container users + runtime policy gates.
8. Lint/format and automated test scaffolding.
9. Long-form docs: API reference, runtime architecture, snapshot store, agent tools, deployment.
