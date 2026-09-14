# Open Source Self-Hosted Vibecoding Platform

## 1. Vision

An open source, self-hostable alternative to tools like v0, Lovable, Bolt, Replit Agent, or Cursor-style project agents, focused on **local-first development**, **BYOK model access**, **Docker-based execution**, **multi-project workspaces**, and **auditable AI-driven code changes**.

The platform should let a user install an instance locally or on a private server, configure API keys, connect Docker, create workspaces, and start building real software through an AI coding interface.

The core promise:

> “Self-host your own AI app builder. Bring your keys, run everything in isolated Docker environments, snapshot every change, and let the agent safely build, edit, run, debug, and connect projects.”

It should support both:

* **Single-user mode**: first user is admin and owns everything.
* **Multi-user organization mode**: teams, organizations, workspaces, project permissions, shared keys, quotas, and scoped environments.

---

## 2. Core Principles

### 2.1 Self-host first

The platform must work locally without requiring a hosted SaaS backend.

The user should be able to run:

```bash
docker compose up
```

Then open the web UI, create the first admin user, configure Docker access, add model providers, and start generating projects.

### 2.2 Bring Your Own Keys

The platform should not force a specific AI provider. Users should be able to connect:

* OpenAI
* Anthropic Claude
* OpenRouter
* Google Gemini
* Mistral
* Groq
* Ollama/local models
* Custom OpenAI-compatible endpoints

Keys may be:

* Personal user keys
* Workspace keys
* Organization keys
* Global admin-managed keys

### 2.3 Security-first execution

The AI should not directly modify host files or execute arbitrary commands on the host.

All execution must happen through isolated project containers, controlled mounts, scoped permissions, and audited tool calls.

### 2.4 Snapshot-based filesystem

Every AI change should be reversible.

The platform should store project history as snapshots/diffs, allowing the user to:

* Inspect what changed
* Revert one file
* Revert a whole step
* Branch from a previous snapshot
* Compare generated versions
* Replay agent sessions

### 2.5 Workspace as a full system

A workspace is not just one codebase. It is a group of related projects and services.

Example:

```txt
Organization: My Team
Workspace: My App
Projects:
  - frontend
  - backend
  - postgres
  - redis
  - worker
  - docs
```

The AI should understand that these projects belong together and can communicate through workspace-level networking, environment variables, service discovery, and shared context.

---

## 3. Product Modes

## 3.1 Single-user mode

Single-user mode is the default local setup.

The first registered user becomes the instance admin and gets immediate access to:

* All projects
* All workspaces
* Global settings
* Docker configuration
* Provider keys
* Quotas
* Logs
* System diagnostics

This mode should feel like a private local development tool.

## 3.2 Multi-user organization mode

Multi-user mode allows teams to self-host one shared instance.

It should support:

* Organizations
* Members
* Roles
* Groups
* Workspace permissions
* Shared provider keys
* Token budgets
* Audit logs
* Project-level permissions
* Environment variable scopes
* Admin-only Docker/runtime settings

This mode should feel closer to a private internal development platform.

---

## 4. Main Entities

## 4.1 User

A user is an account inside the self-hosted instance.

Fields:

```txt
id
email
username
display_name
avatar_url
role
created_at
updated_at
```

Possible global roles:

* `instance_admin`
* `user`
* `readonly`

In single-user mode, the first user is automatically `instance_admin`.

---

## 4.2 Organization

An organization groups users, workspaces, billing-like limits, shared provider keys, and policies.

Fields:

```txt
id
name
slug
owner_user_id
created_at
updated_at
```

Organization roles:

* `owner`
* `admin`
* `developer`
* `viewer`

---

## 4.3 Group

Groups allow permissions and token limits to be applied to sets of users.

Examples:

* Frontend Team
* Backend Team
* Contractors
* Read-only Reviewers
* AI Power Users

Fields:

```txt
id
organization_id
name
description
created_at
updated_at
```

---

## 4.4 Workspace

A workspace is a full product/system area.

Example:

```txt
Workspace: SaaS Analytics Platform
Projects:
  - web
  - api
  - worker
  - postgres
  - redis
```

Fields:

```txt
id
organization_id
name
slug
description
created_by
created_at
updated_at
```

Workspace owns:

* Projects
* Shared environment variables
* Docker network
* Workspace secrets
* Shared context documents
* Runtime policies
* Agent sessions
* Snapshots

---

## 4.5 Project

A project is a runnable unit inside a workspace.

Examples:

* React frontend
* Elysia backend
* PostgreSQL database
* Redis service
* Worker
* Documentation site
* CLI package

Fields:

```txt
id
workspace_id
name
slug
type
runtime_kind
source_path
created_at
updated_at
```

Project types:

```txt
app_frontend
app_backend
service_worker
database
cache
queue
static_site
library
cli
docs
custom
```

Runtime kinds:

```txt
node
bun
deno
python
go
rust
php
static
database_postgres
database_mysql
database_mongo
redis
custom_dockerfile
custom_compose
```

---

## 4.6 Agent Session

An agent session represents one conversation or task execution against a workspace/project.

Fields:

```txt
id
workspace_id
project_id nullable
user_id
status
model_provider
model_name
created_at
updated_at
```

Session status:

```txt
idle
running
waiting_for_approval
failed
completed
cancelled
```

Agent sessions should store:

* User prompts
* AI responses
* Tool calls
* File diffs
* Command outputs
* Runtime logs
* Errors
* Snapshots created during the session

---

## 4.7 Snapshot

A snapshot represents a recoverable point in project/workspace state.

Fields:

```txt
id
workspace_id
project_id nullable
parent_snapshot_id nullable
created_by_session_id nullable
created_by_user_id
message
kind
created_at
```

Snapshot kinds:

```txt
manual
agent_step
agent_batch
before_command
before_apply
before_dependency_install
checkpoint
rollback
branch_base
```

Snapshots should support:

* Full snapshot storage for small projects
* Content-addressed blob storage for files
* Git-like tree objects
* File-level diffs
* Branching
* Reverting
* Comparing
* Restoring

---

## 4.8 Provider Key

Provider keys are API credentials used to access LLMs.

Scopes:

```txt
user
workspace
organization
global
```

Fields:

```txt
id
scope_type
scope_id
provider
label
encrypted_key
created_by
created_at
updated_at
```

Supported providers:

```txt
openai
anthropic
openrouter
gemini
mistral
groq
ollama
custom_openai_compatible
```

Important: keys must be encrypted at rest.

---

## 4.9 Token Budget

Token budgets limit usage for users, groups, workspaces, or organizations.

Fields:

```txt
id
scope_type
scope_id
provider_key_id nullable
limit_tokens
limit_usd nullable
period
created_at
updated_at
```

Periods:

```txt
daily
weekly
monthly
lifetime
custom
```

Budgets should support:

* Hard limits
* Soft warnings
* Per-provider limits
* Per-model limits
* Group limits
* User overrides
* Workspace limits

---

## 4.10 Environment Variable

Environment variables can exist at different scopes.

Scopes:

```txt
instance
organization
workspace
project
runtime_session
```

Fields:

```txt
id
scope_type
scope_id
key
encrypted_value
is_secret
created_by
created_at
updated_at
```

The platform should support inheritance:

```txt
instance env
  -> organization env
    -> workspace env
      -> project env
        -> runtime session env
```

Project env overrides workspace env.
Workspace env overrides organization env.

---

## 5. AI Agent System

## 5.1 Agent responsibilities

The agent should be able to:

* Read files
* Search files
* Edit files
* Create files
* Delete files with approval when necessary
* Run commands in containers
* Install dependencies
* Start dev servers
* Inspect logs
* Debug errors
* Generate migrations
* Create Docker services
* Modify env variables with approval
* Create snapshots
* Explain diffs
* Suggest architecture changes
* Work across multiple projects in a workspace

---

## 5.2 Tool system

The agent should never have raw unrestricted access.

Tools should be explicit and permissioned:

```txt
filesystem.read
filesystem.write
filesystem.diff
filesystem.snapshot
filesystem.restore
shell.run
docker.create_container
docker.start_container
docker.stop_container
docker.logs
docker.exec
workspace.create_project
workspace.connect_service
env.read
env.write_secret
package.install
database.create
database.migrate
network.create
```

Each tool should define:

```txt
name
description
input_schema
output_schema
required_permissions
risk_level
requires_approval
```

Risk levels:

```txt
safe
medium
high
dangerous
```

Examples:

```txt
filesystem.read        -> safe
filesystem.write       -> medium
shell.run npm install  -> medium
shell.run rm -rf       -> dangerous
docker mount host path -> dangerous
env.write_secret       -> high
```

---

## 5.3 Agent permission profiles

Useful profiles:

### Read-only

Can inspect project but cannot modify files or run commands.

### Safe edit

Can edit files and create snapshots, but cannot run arbitrary shell commands.

### Developer

Can edit files, run package scripts, install dependencies, and inspect logs.

### Full workspace agent

Can create projects, containers, databases, networks, and environment variables.

### Admin agent

Can modify instance-level configuration, global provider keys, Docker socket settings, and runtime policies.

---

## 5.4 Approval system

The platform should support human approval for risky actions.

Approval examples:

* Install dependency
* Delete many files
* Modify Dockerfile
* Modify docker-compose.yml
* Expose port publicly
* Add environment secret
* Run command with network access
* Create database
* Reset database
* Run migration on persistent database
* Use global provider key

Approval prompt should show:

```txt
Action
Reason
Risk level
Affected project
Command or diff
Estimated impact
Approve / Reject / Modify
```

---

## 5.5 Planning mode

Before editing, the agent can produce a plan:

```txt
1. Inspect current project structure
2. Identify framework and package manager
3. Create snapshot
4. Add auth entities
5. Add API routes
6. Update frontend forms
7. Run tests
8. Show diff summary
```

The user may approve the whole plan or individual steps.

---

## 5.6 Multi-agent architecture

Possible specialized agents:

### Planner Agent

Breaks the request into steps.

### Code Agent

Writes and modifies code.

### Runtime Agent

Runs commands, reads logs, debugs runtime errors.

### UI Agent

Focuses on frontend layout, components, styling, responsive behavior.

### Database Agent

Handles schemas, migrations, seeders, indexes, and data consistency.

### DevOps Agent

Handles Dockerfiles, compose files, envs, service networking, deployments.

### Reviewer Agent

Reviews diffs, detects bugs, security issues, missing tests, and bad architecture.

MVP can start with one general agent and evolve into specialized agents later.

---

## 6. Filesystem and Snapshot System

## 6.1 Draft source vs stored history

Each project should have a current working tree called the **draft source**.

The draft source is the current editable version mounted into the runtime container.

Behind it, the platform stores:

* Snapshots
* Diffs
* File blobs
* Metadata
* Agent session history

The draft source is not the only source of truth. It is the active materialized state.

---

## 6.2 Snapshot model

A good internal model:

```txt
Blob: content-addressed file content
Tree: directory structure pointing to blobs
Snapshot: pointer to tree + metadata + parent
Diff: changes between snapshots
```

This is similar to Git internally, but controlled by the platform.

Benefits:

* Efficient storage
* Deduplication
* Fast rollback
* File-level history
* Workspace-level history
* Branching support

---

## 6.3 Snapshot operations

Required operations:

```txt
create_snapshot(project_id, message)
list_snapshots(project_id)
compare_snapshots(a, b)
restore_snapshot(snapshot_id)
restore_file(snapshot_id, path)
create_branch_from_snapshot(snapshot_id)
compact_history(project_id)
```

---

## 6.4 Diff viewer

The UI should include a strong diff viewer.

Features:

* File tree of changed files
* Added/modified/deleted markers
* Inline diff
* Side-by-side diff
* Accept/reject file changes
* Restore file from previous snapshot
* “Explain this diff” with AI
* “Regenerate this file” action

---

## 6.5 Branching

Branching is useful for AI experiments.

Example:

```txt
main
  ├─ auth-system-v1
  ├─ auth-system-with-clerk
  └─ auth-system-custom-jwt
```

The user can ask the AI to try multiple implementations and compare them.

---

## 7. Docker Runtime

## 7.1 Docker access

The instance should allow the admin to configure Docker access:

Options:

```txt
unix socket: /var/run/docker.sock
remote docker host: tcp://host:2375
rootless docker socket
podman-compatible socket
```

For security, Docker access should be treated as highly privileged.

---

## 7.2 Runtime architecture

Each workspace gets its own private Docker network:

```txt
workspace_my_app_network
```

Each project runs as one or more containers:

```txt
my_app_frontend
my_app_backend
my_app_postgres
my_app_redis
```

Services communicate using internal DNS:

```txt
http://backend:3000
postgres://postgres:5432
redis://redis:6379
```

---

## 7.3 Source mounting

The platform should mount the current draft source into the container.

Example:

```txt
host/platform/storage/workspaces/ws_123/projects/frontend/current
  -> /workspace
```

The container should run as a non-root user when possible.

---

## 7.4 Runtime templates

Project templates should define:

```txt
name
image
ports
volumes
commands
env
healthcheck
dev_command
build_command
test_command
```

Examples:

### Bun React app

```yaml
image: oven/bun:latest
workdir: /workspace
install: bun install
dev: bun run dev --host 0.0.0.0
port: 5173
```

### Node API

```yaml
image: node:22-bookworm
workdir: /workspace
install: npm install
dev: npm run dev
port: 3000
```

### PostgreSQL

```yaml
image: postgres:16
port: 5432
volume: postgres_data
env:
  POSTGRES_USER: app
  POSTGRES_PASSWORD: generated_secret
  POSTGRES_DB: app
```

---

## 7.5 Database on demand

The user or AI should be able to create services like:

* PostgreSQL
* MySQL
* MariaDB
* MongoDB
* Redis
* RabbitMQ
* MinIO
* Meilisearch
* Typesense

The platform should generate:

* Container
* Volume
* Internal network alias
* Environment variables
* Connection string
* Project bindings

Example:

```txt
DATABASE_URL=postgres://app:secret@postgres:5432/app
REDIS_URL=redis://redis:6379
```

---

## 7.6 Auto env key creation

When a service is created, the platform should be able to automatically create scoped env keys.

Example:

If the AI creates a PostgreSQL service for the backend project:

```txt
workspace env:
  POSTGRES_HOST=postgres
  POSTGRES_PORT=5432

backend project env:
  DATABASE_URL=postgres://app:secret@postgres:5432/app
```

Secrets should be encrypted and only injected at runtime.

---

## 8. Environment Management

## 8.1 Env scopes

Supported scopes:

```txt
Instance
Organization
Workspace
Project
Runtime session
```

Example:

```txt
Organization:
  OPENAI_API_KEY

Workspace:
  APP_NAME
  PUBLIC_API_URL

Backend project:
  DATABASE_URL
  JWT_SECRET

Frontend project:
  VITE_API_URL
```

---

## 8.2 Secret permissions

Secrets should support access policies:

```txt
read_metadata
read_value
write_value
inject_runtime
rotate
remove
```

Most users should not be able to read secret values after creation.

They may only know that a secret exists.

---

## 8.3 AI access to envs

The AI should not automatically see secret values.

It should see metadata like:

```txt
DATABASE_URL exists and is injected into backend runtime.
JWT_SECRET exists and is injected into backend runtime.
```

The AI can request new secrets or modifications, but risky actions should require approval.

---

## 9. Key Management and Token Limits

## 9.1 BYOK model

Users can add their own keys.

A user key can be used only by that user unless shared.

Organization admins can configure shared keys for teams.

Instance admins can configure global keys for all users.

---

## 9.2 Key resolution order

When an agent needs a model, resolve keys in this order:

```txt
1. Explicit session-selected key
2. User key
3. Workspace key
4. Organization key
5. Global key
```

Admins can change this policy.

---

## 9.3 Token accounting

Every model call should record:

```txt
user_id
organization_id
workspace_id
project_id
provider
model
input_tokens
output_tokens
cached_tokens
total_tokens
estimated_cost
created_at
```

---

## 9.4 Limits

Limits can be applied to:

* User
* Group
* Workspace
* Organization
* Provider key
* Model

Examples:

```txt
User Valentina: 2M tokens/month
Frontend Team: 20M tokens/month
Workspace My App: $30/month
Global OpenRouter key: 100M tokens/month
Claude Sonnet: $10/day
```

---

## 10. Workspace Networking

Each workspace should get an isolated private network.

Example:

```txt
workspace_my_app_default
```

Project services can expose:

* Internal ports
* Localhost forwarded ports
* Public tunnel ports if enabled

Default should be private/local only.

The platform should show a service map:

```txt
frontend -> backend -> postgres
frontend -> backend -> redis
worker -> postgres
worker -> redis
```

The AI should be able to understand this map.

---

## 11. UI/UX

## 11.1 Main layout

Suggested UI sections:

```txt
Dashboard
Organizations
Workspaces
Projects
Agent Sessions
Runtime
Snapshots
Secrets
Provider Keys
Usage
Settings
```

---

## 11.2 Workspace view

Workspace page should show:

* Project list
* Running services
* Docker network status
* Env variables
* Recent snapshots
* Recent agent sessions
* Token usage
* Warnings/errors
* Service graph

---

## 11.3 Project view

Project page should show:

* File explorer
* Code editor
* Preview iframe/webview
* Terminal output
* Runtime logs
* Dev server status
* Snapshot timeline
* Diff panel
* Chat/agent panel

Recommended layout:

```txt
Left: files + project tree
Center: editor / diff / preview
Right: agent chat + plan + actions
Bottom: terminal/logs/problems
```

---

## 11.4 Agent UX

The agent chat should support:

* Ask mode
* Edit mode
* Plan mode
* Debug mode
* Review mode
* Multi-project mode

The user should be able to say:

```txt
Create a landing page in frontend and connect it to the backend health endpoint.
```

The agent should know it may need to edit both `frontend` and `backend`.

---

## 11.5 Preview system

For web projects, the platform should provide live preview.

Features:

* Auto-detect dev server port
* Show preview iframe
* Restart dev server
* Show build errors
* Show browser console logs if possible
* Screenshot preview for agent vision later

---

## 12. Project Creation

## 12.1 Templates

Built-in templates:

```txt
React + Vite + Tailwind
Next.js
SvelteKit
Vue + Vite
Elysia + Bun API
Express API
Fastify API
Hono API
NestJS API
Rust Axum API
Go Fiber API
Python FastAPI
PostgreSQL
Redis
Worker service
Static docs
```

---

## 12.2 AI-generated projects

The user can also ask:

```txt
Create a SaaS app with React frontend, Bun backend, PostgreSQL, Redis, auth, billing-ready structure, and Docker dev environment.
```

The platform should create:

```txt
Workspace: SaaS App
Projects:
  - frontend
  - backend
  - postgres
  - redis
```

Then generate:

* Source files
* Docker runtime config
* Env variables
* Service bindings
* Initial snapshots
* README
* Development instructions

---

## 13. Context System

## 13.1 Workspace context

The agent needs durable context about the workspace.

Examples:

```txt
This workspace is a SaaS analytics platform.
Frontend uses React, Zustand, Tailwind.
Backend uses Bun, Elysia, Drizzle, PostgreSQL.
Auth is JWT-based.
Database schema lives in backend/src/db/schema.ts.
```

---

## 13.2 Project context

Each project should have its own context file.

Example:

```txt
.project/context.md
```

Or internally stored as metadata.

It should contain:

* Stack
* Commands
* Architecture rules
* Known conventions
* Important files
* Coding style
* Testing strategy
* Runtime details

---

## 13.3 Agent memory

Useful memory types:

```txt
workspace_facts
project_facts
user_preferences
architecture_decisions
known_errors
resolved_errors
```

Architecture decisions should be explicit.

Example:

```txt
ADR-0001: Use Bun + Elysia for backend instead of Express.
ADR-0002: Use Drizzle ORM instead of Prisma.
ADR-0003: Use workspace-level PostgreSQL shared by backend and worker.
```

---

## 14. Security Model

## 14.1 Threat model

Main risks:

* AI executes dangerous commands
* AI leaks secrets
* AI modifies host files
* Malicious package install
* Dependency supply-chain compromise
* Container escape
* User abuses shared global API keys
* Prompt injection through project files
* Prompt injection through logs or package output
* Workspace data leak between organizations
* Accidental deletion of project files

---

## 14.2 Isolation

Minimum security rules:

* Run commands only inside containers
* Mount only project/workspace directories
* No host root mount
* Use non-root users inside containers when possible
* Separate Docker networks per workspace
* Separate volumes per workspace/project
* Encrypt secrets at rest
* Do not expose secrets to AI context by default
* Audit every tool call
* Snapshot before risky writes

---

## 14.3 Prompt injection defense

The agent must treat project files, logs, terminal output, dependency README files, and external content as untrusted.

Rules:

* Files cannot override system policy
* Logs cannot instruct the agent to reveal secrets
* README instructions cannot bypass permissions
* Package output cannot request tool calls
* AI should never expose secret values

---

## 14.4 Audit logs

Audit log events:

```txt
user.login
provider_key.created
provider_key.used
agent.session_started
agent.tool_called
agent.command_executed
agent.file_modified
snapshot.created
snapshot.restored
env.secret_created
env.secret_injected
docker.container_created
docker.container_started
docker.network_created
quota.exceeded
approval.requested
approval.accepted
approval.rejected
```

---

## 15. Suggested Tech Stack

## 15.1 Backend

Recommended:

```txt
TypeScript
Bun
Elysia or Hono
PostgreSQL
Drizzle ORM
Redis optional for queues/cache
Docker Engine API
WebSockets/SSE for live updates
```

Why:

* Fast development
* Good fit for AI/tool orchestration
* Strong type safety
* Easy Docker API integration
* Good enough performance for self-hosted instances

Alternative more systems-level backend:

```txt
Rust
Axum
PostgreSQL
SQLx
Tokio
Bollard Docker client
```

This is more robust but slower to build.

Best practical recommendation:

* Start with TypeScript/Bun backend.
* Keep runtime/tool execution abstractions clean.
* Later move critical sandbox/runtime pieces to Rust if needed.

---

## 15.2 Frontend

Recommended:

```txt
React
Vite
TailwindCSS
Zustand
TanStack Query
Monaco Editor
Xterm.js
React Flow for service graph
```

---

## 15.3 Database

Use PostgreSQL for platform metadata:

* Users
* Organizations
* Workspaces
* Projects
* Sessions
* Snapshots
* Provider keys
* Usage records
* Permissions
* Audit logs

Use local filesystem or object storage for blobs:

* File snapshots
* Large logs
* Generated artifacts
* Project archives

For local self-host:

```txt
/storage/blobs
/storage/workspaces
/storage/logs
```

For server self-host:

```txt
S3-compatible storage optional
```

---

## 15.4 Real-time updates

Use WebSockets or SSE for:

* Agent streaming responses
* Tool call updates
* Command output
* Runtime logs
* Snapshot creation
* Preview status
* Container status

SSE is simpler for one-way streams.
WebSockets are better if terminal input is needed.

Recommended:

* SSE for agent/model streaming
* WebSocket for terminal/runtime sessions

---

## 16. Backend Modules

Suggested backend structure:

```txt
apps/server/src/
  main.ts
  config/
  db/
  modules/
    auth/
    users/
    organizations/
    groups/
    workspaces/
    projects/
    permissions/
    provider-keys/
    usage/
    agents/
    tools/
    snapshots/
    filesystem/
    docker/
    runtime/
    env/
    approvals/
    audit/
    templates/
    realtime/
  shared/
    errors/
    crypto/
    logger/
    ids/
    validation/
```

---

## 17. Monorepo Structure

Recommended repository:

```txt
platform/
  apps/
    web/
      src/
      package.json
    server/
      src/
      package.json
    worker/
      src/
      package.json
  packages/
    shared/
      src/
    ai-core/
      src/
    docker-runtime/
      src/
    snapshot-store/
      src/
    permissions/
      src/
    templates/
      src/
    sdk/
      src/
  storage/
    .gitkeep
  docker/
    Dockerfile.server
    Dockerfile.web
    compose.dev.yml
    compose.prod.yml
  docs/
    architecture.md
    security.md
    runtime.md
    agent-tools.md
  scripts/
  package.json
  README.md
```

---

## 18. AI Provider Abstraction

Provider interface:

```ts
interface LLMProvider {
  id: string;
  listModels(): Promise<ModelInfo[]>;
  streamChat(input: ChatInput): AsyncIterable<ChatChunk>;
  complete(input: ChatInput): Promise<ChatResult>;
  countTokens?(input: TokenCountInput): Promise<TokenCountResult>;
}
```

Supported provider adapters:

```txt
OpenAIProvider
AnthropicProvider
OpenRouterProvider
GeminiProvider
OllamaProvider
CustomOpenAIProvider
```

Model capabilities should be tracked:

```txt
supports_tool_calling
supports_vision
supports_json_mode
supports_caching
context_window
max_output_tokens
input_cost
output_cost
```

---

## 19. Tool Calling Runtime

Tool execution should follow this flow:

```txt
AI requests tool call
  -> validate schema
  -> check permissions
  -> check risk level
  -> request approval if needed
  -> create snapshot if required
  -> execute tool
  -> store output
  -> stream result to UI
  -> append result to session context
```

Tool calls should be fully persisted.

---

## 20. MVP Scope

A realistic MVP should avoid trying to build everything at once.

## 20.1 MVP goals

The MVP should support:

* Single-user local mode
* Login / first admin setup
* Provider key setup
* One organization implicitly owned by admin
* Workspaces
* Projects
* Docker-backed runtime
* File explorer/editor
* AI chat with tool calling
* Read/write files
* Run commands in container
* Create snapshots before AI edits
* Restore snapshots
* Basic preview for web apps
* Usage tracking

---

## 20.2 MVP project types

Start with:

```txt
React + Vite frontend
Bun/Node backend
PostgreSQL service
Redis service
Custom Dockerfile project
```

Avoid supporting every stack at first.

---

## 20.3 MVP agent tools

Start with:

```txt
filesystem.read_file
filesystem.list_files
filesystem.write_file
filesystem.apply_patch
filesystem.create_snapshot
filesystem.restore_snapshot
shell.run
runtime.start
runtime.stop
runtime.logs
provider.chat
```

---

## 20.4 MVP screens

Required screens:

```txt
Setup Wizard
Provider Keys
Dashboard
Workspace Detail
Project Detail
Editor
Agent Chat
Snapshots
Runtime Logs
Settings
```

---

## 20.5 MVP non-goals

Do not start with:

* Full multi-tenant billing
* Marketplace
* Cloud deploys
* Kubernetes
* Complex RBAC
* Browser automation
* Visual drag-and-drop builder
* Mobile support
* Full Git replacement
* Plugin marketplace
* Enterprise SSO

These can come later.

---

## 21. Roadmap

## Phase 1: Local single-user prototype

* Docker Compose setup
* First admin user
* Provider key setup
* Create workspace/project
* File tree/editor
* Docker runtime
* Basic AI chat
* File edits
* Shell execution
* Manual snapshots
* Restore snapshot

## Phase 2: Agentic project building

* Tool calling loop
* Apply patches
* Run commands
* Read logs
* Debug errors
* Auto snapshots
* Web preview
* Project templates
* Usage tracking

## Phase 3: Multi-project workspaces

* Workspace Docker networks
* Multiple projects per workspace
* Service discovery
* PostgreSQL/Redis on demand
* Env binding generation
* Workspace-level context
* Service graph UI

## Phase 4: Teams and organizations

* Multi-user auth
* Organizations
* Groups
* Roles
* Shared provider keys
* Token budgets
* Audit logs
* Approval flows

## Phase 5: Advanced AI workflows

* Planner/reviewer agents
* Branching experiments
* Diff explanations
* Architecture memory
* ADR generation
* Prompt-injection hardening
* Visual screenshot feedback
* Test generation

## Phase 6: Deployment integrations

* Docker Compose export
* GitHub repo export
* Coolify integration
* Dokploy integration
* Railway/Fly.io/Render optional
* SSH deploy agent
* Environment promotion: dev -> staging -> prod

---

## 22. Differentiators

This platform should differentiate itself from closed-source tools by being:

### Fully self-hosted

Users control their projects, keys, snapshots, and runtime.

### BYOK-first

No forced provider. No hidden markup. No vendor lock-in.

### Docker-native

Real projects run inside real containers, not fake sandboxes.

### Multi-project aware

A workspace can contain frontend, backend, database, worker, cache, and docs.

### Snapshot-native

Every AI edit can be reviewed, reverted, branched, and replayed.

### Security-conscious

Scoped tools, approval gates, secret isolation, audit logs, and runtime isolation are first-class concepts.

### Open-source and hackable

Users can extend providers, tools, templates, and runtime adapters.

---

## 23. Extra Features Worth Adding Later

## 23.1 Git integration

* Import GitHub repo
* Commit snapshots to Git
* Create branch from AI session
* Open pull request
* Compare AI snapshots with Git commits

## 23.2 Template marketplace

Self-hosted template registry for:

* App starters
* Docker services
* Agent tools
* Runtime images
* Workspace blueprints

## 23.3 Plugin system

Allow plugins for:

* Providers
* Tools
* Project templates
* Runtime adapters
* Deploy targets
* UI panels

## 23.4 Local model support

Support Ollama/LM Studio/custom OpenAI-compatible servers.

Useful for:

* Cheap local autocomplete
* Small refactors
* Offline coding
* Private code inspection

## 23.5 Browser automation

Optional Playwright container for:

* Screenshot testing
* UI validation
* Console error detection
* Accessibility checks
* Visual feedback loops

## 23.6 Test intelligence

AI can:

* Detect test command
* Generate tests
* Run tests
* Explain failing tests
* Propose fixes

## 23.7 Dependency security

Supply-chain features:

* Lockfile diff warnings
* Package risk scoring
* Detect install scripts
* Warn on typosquatting
* Warn on abandoned packages
* Dependency allowlist/denylist
* Approval required for new dependencies

## 23.8 Cost simulator

Before running a long task, estimate:

* Model cost
* Token usage
* Runtime impact
* Disk usage

## 23.9 Workspace blueprints

Blueprint example:

```txt
Fullstack SaaS:
  - React frontend
  - Bun backend
  - PostgreSQL
  - Redis
  - Worker
  - Admin panel
```

## 23.10 Dev container export

Export project as:

* docker-compose.yml
* devcontainer.json
* .env.example
* README.md

---

## 24. Biggest Technical Challenges

### 24.1 Safe Docker access

Mounting Docker socket into a container is effectively root-level access to the host.

This must be documented clearly.

Possible mitigations:

* Support rootless Docker
* Support remote Docker host
* Run platform outside Docker in local mode
* Use a minimal privileged runtime daemon
* Add policy restrictions at platform level

---

### 24.2 Snapshot performance

Large projects can make naive snapshots expensive.

Avoid copying the whole folder every time.

Use:

* Content-addressed blobs
* File hashing
* Incremental snapshots
* Ignore rules
* Snapshot compaction

---

### 24.3 Agent reliability

The AI will make bad edits.

Mitigations:

* Small patches
* Snapshot before changes
* Run tests
* Show diffs
* Require approval for risky edits
* Reviewer agent
* Project conventions/context

---

### 24.4 Secret leakage

The AI must not see secret values by default.

Expose only metadata.

Inject secrets into runtime containers, not into prompts.

---

### 24.5 Multi-project context size

Large workspaces can exceed context windows.

Need:

* File search
* Symbol search
* Context packs
* Project summaries
* Architecture memory
* Relevant file selection

---

## 25. Recommended MVP Architecture

```txt
Browser UI
  -> Web Server API
    -> Auth / Users / Workspaces / Projects
    -> Provider Key Manager
    -> Agent Orchestrator
    -> Tool Runtime
    -> Snapshot Store
    -> Docker Runtime Manager
    -> Env Manager
    -> Usage Tracker
    -> Audit Logger

Docker Runtime Manager
  -> Docker Engine
    -> Project Containers
    -> Database Containers
    -> Workspace Networks
    -> Volumes

Snapshot Store
  -> PostgreSQL metadata
  -> Blob storage on disk
  -> Materialized draft source folders
```

---

## 26. Suggested Initial Stack

Use this for the first serious implementation:

```txt
Monorepo: pnpm or bun workspaces
Frontend: React + Vite + Tailwind + Zustand + TanStack Query
Editor: Monaco Editor
Terminal: xterm.js
Backend: Bun + Elysia
Database: PostgreSQL
ORM: Drizzle
Realtime: WebSocket + SSE
Runtime: Docker Engine API
Snapshots: custom content-addressed store
AI: provider abstraction over OpenAI/OpenRouter/Anthropic/Gemini/Ollama
Auth: local email/password first, OAuth later
Secrets: AES-GCM encryption with instance master key
```

---

## 27. First Implementation Milestones

### Milestone 1: Instance setup

* Install with Docker Compose
* First admin user
* Instance settings
* Docker connection check
* Provider key setup

### Milestone 2: Workspace/project basics

* Create workspace
* Create project
* File explorer
* Editor
* Save files
* Manual snapshots
* Restore snapshots

### Milestone 3: Runtime

* Start project container
* Install dependencies
* Run dev command
* Stream logs
* Preview web app

### Milestone 4: AI agent

* Chat UI
* Provider abstraction
* File read/list tools
* Patch/write tools
* Shell run tool
* Auto snapshot before edits
* Diff summary

### Milestone 5: Multi-project workspace

* Add PostgreSQL service
* Add Redis service
* Generate env variables
* Workspace Docker network
* Internal service names

### Milestone 6: Permissions and quotas

* Usage tracking
* Token limits
* Key scopes
* Basic approval gates
* Audit logs

---

## 28. Minimal Database Tables

MVP tables:

```txt
users
organizations
organization_members
workspaces
workspace_members
projects
provider_keys
agent_sessions
agent_messages
agent_tool_calls
snapshots
snapshot_files
file_blobs
env_vars
usage_records
audit_logs
approvals
```

Later:

```txt
groups
group_members
permission_policies
workspace_networks
runtime_containers
project_services
deployment_targets
plugins
templates
architecture_decisions
```

---

## 29. Final Product Positioning

Possible positioning:

> Open-source self-hosted AI app builder for real Docker-based projects.

Alternative:

> A local-first AI development platform where agents can build, run, debug, snapshot, and connect full-stack applications inside isolated Docker workspaces.

Alternative:

> Lovable/v0-style AI coding, but open source, BYOK, Docker-native, reversible, and self-hosted.

---

## 30. Final Opinion

The idea is strong because it combines several things developers actually want:

* AI-assisted app creation
* Self-hosting
* BYOK
* Docker-native execution
* Real full-stack projects
* Snapshot rollback
* Team support
* Cost control
* Security boundaries

The most important thing is to not start too broad.

The MVP should focus on this loop:

```txt
Create workspace
Create project
Run project in Docker
Chat with AI
AI edits files
Snapshot every change
Run command
Read logs
Fix error
Preview result
Rollback if needed
```

Once that loop feels excellent, organizations, quotas, multi-project orchestration, and advanced permissions can be layered on top.
