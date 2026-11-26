# Interfaces and Extension Points

This document describes the interfaces that exist in the open-source release and the boundaries intended for deployment-specific adapters. The included implementation runs with local JSON records and local Git repositories. External Git, AI, and knowledge systems require deployment-specific integration; they are not bundled as completed adapters.

## 1. Codex through MCP

MCP is the recommended agent interface. It uses short-lived project credentials instead of website passwords or login cookies. The current MCP package exposes two tools:

- `project_os_get_context` reads the current project context;
- `project_os_append_progress` appends a scoped progress event.

See [Connect Codex](./CODEX_SETUP.md) for the terminal command and security model.

The MCP bridge calls the following agent API.

### Read capabilities

```http
GET /api/agent/v1/capabilities
Authorization: Bearer <short-lived-agent-token>
```

### Read project context

```http
GET /api/agent/v1/projects/:id/context
Authorization: Bearer <short-lived-agent-token>
```

### Append project progress

```http
POST /api/agent/v1/projects/:id/events
Authorization: Bearer <short-lived-agent-token>
Idempotency-Key: <stable-retry-key>
Content-Type: application/json
```

```json
{
  "message": "Completed the scoped change and verified the acceptance path.",
  "plainMessage": "The current stage now works on the real path and is ready for review.",
  "why": "This was the next accepted vertical slice.",
  "benefit": "The next maintainer can continue from a recorded check instead of reconstructing context.",
  "verification": "pnpm run check passed and the changed page was inspected in light and dark themes.",
  "stageIndex": 2,
  "progressTo": 55,
  "nextStep": "Run the next staged acceptance check."
}
```

Current controls:

- each credential is bound to one verified `workspaceId` and one `projectId`;
- scopes are limited to `project.context.read` and `project.events.append`;
- expiration is restricted to 24 hours or 7 days;
- the plaintext token is returned once and only its SHA-256 hash is persisted;
- the actor is derived from the credential label, not the request body;
- `progressTo` must be between 0 and 100 and cannot move backward;
- the same idempotency key and payload create only one event and one project-record Git commit;
- reusing an idempotency key with different content returns `409`;
- reads, writes, rejected requests, replays, rate limits, and revocation are audited in the credential's workspace.

## 2. Legacy project-key API

The following endpoints remain for earlier scripts. New integrations should use the short-lived agent credential and MCP path above.

### Read context

```http
GET /api/projects/:id/context
X-Project-Key: <project-secret>
```

### Append progress

```http
POST /api/projects/:id/events
X-Project-Key: <project-secret>
Idempotency-Key: <stable-retry-key>
Content-Type: application/json
```

```json
{
  "message": "Checked the current vertical slice.",
  "plainMessage": "The current stage has passed its acceptance check.",
  "why": "The project plan identifies this as the current slice.",
  "benefit": "The handoff now records a checked result and a clear continuation point.",
  "verification": "The staged handoff URL loaded and the acceptance checklist was reviewed.",
  "stageIndex": 2,
  "progressTo": 55,
  "nextStep": "Review the staged handoff."
}
```

The secret belongs in `X-Project-Key`, never in a URL or request body. Do not put it in documentation, screenshots, issues, logs, or commits. Writes require a stable `Idempotency-Key`, and the server derives the actor rather than accepting an identity claimed by the caller.

## 3. Git storage

The included Git implementation:

- creates one repository for each project;
- persists project events in application records and writes a corresponding Git commit;
- reads project files and recent Git history when building project context.

Relevant environment variables are:

```bash
PROJECT_OS_DATA_DIR=/data/project-os
GIT_PUBLIC_BASE=https://git.example.com/project-os
GIT_PUBLIC_DIR=/data/git-bare
```

`GIT_PUBLIC_BASE` controls generated clone URLs. `GIT_PUBLIC_DIR` enables bare mirrors. Neither variable supplies external-host authentication.

If a deployment replaces local Git, the adapter must preserve workspace and project isolation, deterministic event writes, and recoverable handoff history. The following is an illustrative contract, not an exported TypeScript interface in this release:

```ts
interface GitStoreAdapter {
  createProjectRepo(
    projectId: string,
    files: Record<string, string>,
  ): Promise<{ repoPath: string; cloneUrl?: string }>;
  appendEvent(projectId: string, event: ProjectEvent): Promise<void>;
  readContext(projectId: string): Promise<ProjectContext>;
  buildHandoff(projectId: string): Promise<string>;
}
```

## 4. AI service integration

The optional server-side AI helpers use an OpenAI-compatible API. The public repository contains the generic HTTP integration only; it does not contain deployment credentials or organization-specific infrastructure.

```bash
PROJECT_OS_AI_BASE=https://your-ai-service.example/v1
PROJECT_OS_AI_KEY=replace-with-a-server-side-secret
PROJECT_OS_AI_MODEL=replace-with-a-supported-chat-model
PROJECT_OS_EMBEDDING_MODEL=replace-with-a-supported-embedding-model
```

The current implementation calls:

- `POST {PROJECT_OS_AI_BASE}/chat/completions`;
- `POST {PROJECT_OS_AI_BASE}/embeddings`;
- bearer authorization with `PROJECT_OS_AI_KEY`.

Keep the credential in a server environment or secret manager. Never return it to the frontend. User-facing failures should remain generic and must not reveal service details, balances, configured models, or private infrastructure.

For deployments that need a different implementation, this illustrative boundary keeps service-specific logic outside project behavior:

```ts
interface AiServiceAdapter {
  chat(
    messages: Array<{ role: string; content: string }>,
    options?: { temperature?: number },
  ): Promise<{ content: string; usage?: unknown }>;
  embed(text: string): Promise<number[]>;
  health(): Promise<{ ok: boolean }>;
}
```

This contract is a design direction, not a completed adapter registry in this release.

## 5. Knowledge API

The knowledge system stores project lessons, operating rules, methods, and handoff material as structured records. The included store is JSON-based.

### Create an item

```http
POST /api/w/:workspace-public-id/kb/v1/items
Authorization: Bearer <knowledge-token>
Content-Type: application/json
```

```json
{
  "type": "method",
  "title": "Run acceptance checks before handoff",
  "body": "Record the verification steps, evidence, and known risks.",
  "businessLine": "project execution",
  "tags": ["handoff", "verification"],
  "visibility": "internal"
}
```

### Search items

```http
POST /api/w/:workspace-public-id/kb/v1/search
Authorization: Bearer <knowledge-token>
Content-Type: application/json
```

```json
{
  "q": "handoff acceptance checks",
  "limit": 10
}
```

The namespace in the URL and the verified knowledge credential determine the workspace. A client must not be allowed to select a different workspace through a request body field.

PostgreSQL, vector search, and third-party knowledge systems are possible extension directions, but their storage adapters are not included in this release. An implementation should preserve workspace ownership, visibility, audit behavior, and exportability. An illustrative boundary is:

```ts
interface KnowledgeStoreAdapter {
  upsert(item: KnowledgeItem): Promise<KnowledgeItem>;
  search(query: {
    q?: string;
    tags?: string[];
    limit?: number;
  }): Promise<KnowledgeItem[]>;
  export(projectId?: string): Promise<KnowledgeItem[]>;
}
```

## 6. Deployment boundary

A small production installation normally contains:

- a built web frontend served by the Node.js process or a static web server;
- the Node.js API under a supervised service;
- a durable `PROJECT_OS_DATA_DIR` volume;
- local Git repositories or a deployment-specific Git integration;
- complete backups of JSON records and repositories;
- a reverse proxy that sends `/api` to the backend.

Never publish `.env` files, `server/data`, private repositories, real project records, AI credentials, website passwords, or raw AI-agent conversations. Follow the [Deployment Guide](./DEPLOYMENT.md) and [Publication Security Checklist](./SECURITY_PUBLICATION_CHECKLIST.md) before release.
