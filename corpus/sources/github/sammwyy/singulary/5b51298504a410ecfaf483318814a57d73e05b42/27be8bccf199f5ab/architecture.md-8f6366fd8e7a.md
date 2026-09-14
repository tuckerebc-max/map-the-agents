# Singulary Architecture

Singulary is a monorepo containing a React frontend and an Express backend. The production container builds the frontend as static assets and serves them from the same Express process that exposes the API under `/api`.

## System Overview

```text
┌─────────────────────────────────────────────────────────┐
│                  Browser (React + Vite)                 │
│   editor · file tree · terminals · agent chat · admin   │
└──────────────┬────────────────┬─────────────────┬───────┘
               │ REST           │ SSE             │ WS
┌──────────────┴────────────────┴─────────────────┴───────┐
│                Express API · SQLite metadata            │
│ ─────────────────────────────────────────────────────── │
│  auth · groups · rules · workspaces · projects · env    │
│  agent loop · tool runtime · token accounting · audit   │
└──────────────┬─────────────────────────────────┬────────┘
               │                                 │
               ▼                                 ▼
        ┌─────────────┐                  ┌──────────────┐
        │   Docker    │                  │   Storage    │
        │   Engine    │                  │  workspaces/ │
        │             │                  │   projects/  │
        │  • project  │                  │   blobs/     │
        │    network  │                  └──────────────┘
        │  • runtime  │
        │  • shells   │
        │  • services │
        └─────────────┘
```

## Runtime & Environments

- **Production**:
  - `/` serves the Vite build from `apps/web/dist`.
  - `/api` serves the backend routes from `apps/server`.
  - SQLite stores instance metadata in `storage/singulary.sqlite` by default.
- **Development**: Uses Vite's proxy so frontend requests to `/api` reach the backend seamlessly.

## Backend Architecture

The backend (`apps/server`) is an Express application built on Node.js using TypeScript.
Key responsibilities include:
- **API Routing**: Exposes endpoints for UI clients to manage workspaces, projects, groups, rules, and providers.
- **Agent Loop & Tools**: Manages agent interactions, streams LLM responses via SSE, and securely executes agent tool calls inside isolated Docker containers.
- **Docker Orchestration**: Interacts with the Docker socket to spin up project runtimes, connect services (e.g., Postgres, Redis), and manage interactive shells (via WebSocket).
- **Metadata Storage**: Uses SQLite to keep track of user accounts, token limits, rules, and workspace topology.

## Frontend Architecture

The frontend (`apps/web`) is a React application powered by Vite and styled with Tailwind CSS. It is organized by responsibility:

```txt
src/
  components/
    ui/            Reusable primitives such as Button, Section, fields, stats
    layout/        App-level layout and navigation
    auth/          Auth-specific presentational components
    workspaces/    Workspace/project/service presentational components
    projects/      Project-specific presentational components
    settings/      Settings presentational components
    admin/         Admin presentational components
  hooks/           View-facing hooks that orchestrate services and stores
  services/        API clients; the only layer that calls fetch through services/api.ts
  stores/          Zustand stores for cached temporary frontend state
  utils/           Pure helpers
  views/           Route-level screens
```

### Data Flow

Views consume hooks. Hooks call services and write the result to stores. Stores keep temporary fetched data so repeated route visits do not refetch unless a hook decides it should.

```txt
View -> hook -> service -> API
          -> store
View <- hook <- store
```

Mutations call the service, then update the relevant store. A hook can also expose `refetch()` when a mutation or manual refresh should bypass cached data.

### Current Modules
- `useAuth` uses `authService` and `auth.store`.
- `useDashboard` uses `dashboardService` and `dashboard.store`.
- `useWorkspaces` uses `workspacesService` and `workspaces.store`.
- `useProviderKeys` uses `providerKeysService` and `provider-keys.store`.
- Admin views consume `adminService`.

## Data Model: Workspaces, Projects, and Services

- **Workspaces**: A high-level grouping representing a full product or system area. Workspaces own projects, shared environment variables, network spaces, and services.
- **Projects**: Codebases or runnable apps within a workspace. They keep runtime metadata such as `node`, `python`, `static`, or `custom_dockerfile`.
- **Services**: Shared infrastructure such as SQLite, PostgreSQL, MySQL, MongoDB, Redis, queues, object storage, search, or custom services. Services belong to the workspace and provide connection strings to all projects in that workspace.
