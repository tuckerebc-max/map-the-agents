# Deployment Guide

This guide covers local evaluation and a small self-hosted installation. It does not replace your organization's infrastructure review, backup policy, or access controls.

## 1. Fast local evaluation with Docker

```bash
docker compose up --build
```

Open <http://localhost:8790>. The included Compose configuration binds to `127.0.0.1`, uses an isolated Docker volume, and enables the local development authentication bypass. Do not expose this configuration to the public internet.

## 2. Local development

Requirements:

- Node.js 22 or newer on a currently supported LTS line;
- Git;
- pnpm.

Install dependencies and create the initial local data:

```bash
pnpm install --frozen-lockfile
pnpm --dir server seed
```

Start the API in one terminal:

```bash
PROJECT_OS_DEV_NO_AUTH=true pnpm --dir server start
```

Start Vite in another terminal:

```bash
pnpm dev
```

The API listens on <http://localhost:8790> by default. Vite prints the frontend URL. Local persisted data and project Git repositories are stored under `server/data` unless `PROJECT_OS_DATA_DIR` is set.

`PROJECT_OS_DEV_NO_AUTH=true` is accepted only outside production. The server refuses to start in production unless both `PROJECT_OS_AUTH_USER` and `PROJECT_OS_AUTH_PASSWORD` are configured.

## 3. Small single-host deployment

A simple directory layout is:

```text
/opt/project-os-for-codex
/var/lib/project-os-for-codex/data
/var/backups/project-os-for-codex
```

Prepare a release in a staging directory first:

```bash
git clone <public-repository-url> /opt/project-os-for-codex
cd /opt/project-os-for-codex
cp .env.example .env
cp server/.env.example server/.env
pnpm install --frozen-lockfile
pnpm run check
```

Seed a new persistent data directory once:

```bash
NODE_ENV=production \
PROJECT_OS_AUTH_USER='replace-with-admin-account' \
PROJECT_OS_AUTH_PASSWORD='replace-with-a-long-random-password' \
PROJECT_OS_DATA_DIR=/var/lib/project-os-for-codex/data \
pnpm --dir server seed
```

Start the server with secrets supplied by the service manager or a secret manager, not by a committed file:

```bash
NODE_ENV=production \
PROJECT_OS_AUTH_USER='replace-with-admin-account' \
PROJECT_OS_AUTH_PASSWORD='replace-with-a-long-random-password' \
PROJECT_OS_DATA_DIR=/var/lib/project-os-for-codex/data \
PROJECT_OS_PUBLIC_BASE=https://project-os.example.com \
pnpm --dir server start
```

The Node.js server serves both `/api` and the built frontend when `dist` exists. Run it under `systemd`, a container platform, or another supervised service. Test a staged release, take a backup, and keep the previous release available for rollback before changing live traffic.

## 4. Nginx reverse proxy

This example serves the built frontend directly and sends API traffic to the Node.js process:

```nginx
server {
  server_name project-os.example.com;

  root /opt/project-os-for-codex/dist;
  index index.html;

  location /api/ {
    proxy_pass http://127.0.0.1:8790/api/;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme;
  }

  location / {
    try_files $uri $uri/ /index.html;
  }
}
```

For a subpath deployment, keep these values aligned before building and starting the service:

```bash
VITE_BASE=/your-subpath/
PROJECT_OS_COOKIE_PATH=/your-subpath
PROJECT_OS_PUBLIC_BASE=https://example.com/your-subpath
```

Verify subpath routing, cookies, generated MCP connection URLs, and static assets in staging before release.

## 5. Persistent data and backups

Back up the complete `PROJECT_OS_DATA_DIR`, including:

- all JSON records;
- the `repos` directory containing project Git repositories;
- the bare mirror directory when `GIT_PUBLIC_DIR` points outside the data directory.

A minimal filesystem backup is:

```bash
tar -czf /var/backups/project-os-for-codex/backup-$(date +%Y%m%d-%H%M%S).tgz \
  /var/lib/project-os-for-codex/data
```

Use a consistent snapshot or briefly stop writes while taking a filesystem archive. Test restoration in staging. Restore the complete data directory rather than a single JSON file, because the records and Git history must remain consistent.

## 6. Connect an AI service

The optional draft and knowledge helpers use an OpenAI-compatible server-side API. Configure it only in the server environment:

```bash
PROJECT_OS_AI_BASE=https://your-ai-service.example/v1
PROJECT_OS_AI_KEY=replace-with-a-server-side-secret
PROJECT_OS_AI_MODEL=replace-with-a-supported-chat-model
PROJECT_OS_EMBEDDING_MODEL=replace-with-a-supported-embedding-model
```

The configured service must support:

- `POST /chat/completions`;
- `POST /embeddings`;
- bearer authorization.

Keep real credentials out of documentation, screenshots, issues, logs, commits, and frontend bundles. Public errors must remain generic and must not reveal service details, balances, or infrastructure.

## 7. Git storage

The default implementation stores one local Git repository per project. Optional public clone URLs and bare mirrors are controlled by:

```bash
GIT_PUBLIC_BASE=https://git.example.com/project-os
GIT_PUBLIC_DIR=/data/git-bare
```

These variables do not configure authentication for an external Git host. If you integrate Gitea, GitLab, GitHub Enterprise, or another service, keep write credentials on the server and preserve workspace and project isolation in the adapter.

## 8. Knowledge storage

The included knowledge store uses JSON. `PROJECT_OS_KB_DIR` can point to an exported document directory for the included import workflow. PostgreSQL, vector search, and third-party knowledge systems are extension directions, not bundled storage adapters in this release. See [Interfaces and Extension Points](./INTERFACES.md) for the current API and proposed adapter boundaries.

## 9. Release gate

Before exposing a release to users:

1. run `pnpm run check`;
2. verify `GET /api/health` returns `200` and reports protected authentication;
3. confirm the release data directory contains no customer exports, production credentials, or unrelated repositories;
4. scan the tracked files and Git history for tokens, private keys, personal information, private hostnames, and internal endpoints;
5. inspect every affected page in both light and dark themes;
6. exercise the Codex MCP context-read and progress-write path against staging;
7. test backup and rollback commands;
8. obtain human approval for the repository, license, permissions, deployment, and traffic switch.
