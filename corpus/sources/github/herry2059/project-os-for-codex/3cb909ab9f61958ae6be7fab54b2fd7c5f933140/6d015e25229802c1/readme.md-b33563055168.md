<h1 align="center">🚦 Project OS for Codex</h1>

<p align="center"><strong>The open-source control plane for Codex projects: visible progress, resumable context, safe handoffs, and reusable knowledge.</strong></p>

<p align="center"><strong>Independent open-source project. Not affiliated with or endorsed by OpenAI.</strong></p>

<p align="center">
  Built for Codex. Connect through MCP, keep project truth in Git, and make every handoff resumable.
</p>

<p align="center">
  <a href="https://github.com/herry2059/project-os-for-codex/actions/workflows/ci.yml"><img src="https://img.shields.io/github/actions/workflow/status/herry2059/project-os-for-codex/ci.yml?branch=main&style=for-the-badge&label=CI" alt="CI Status"></a>
  <a href="https://github.com/herry2059/project-os-for-codex/releases/latest"><img src="https://img.shields.io/github/v/release/herry2059/project-os-for-codex?style=for-the-badge" alt="Latest Release"></a>
  <a href="https://github.com/herry2059/project-os-for-codex/stargazers"><img src="https://img.shields.io/github/stars/herry2059/project-os-for-codex?style=for-the-badge" alt="GitHub Stars"></a>
  <a href="https://github.com/herry2059/project-os-for-codex/forks"><img src="https://img.shields.io/github/forks/herry2059/project-os-for-codex?style=for-the-badge" alt="GitHub Forks"></a>
  <a href="https://github.com/herry2059/project-os-for-codex/graphs/contributors"><img src="https://img.shields.io/github/contributors/herry2059/project-os-for-codex?style=for-the-badge" alt="Contributors"></a>
  <a href="LICENSE"><img src="https://img.shields.io/github/license/herry2059/project-os-for-codex?style=for-the-badge" alt="Apache-2.0 License"></a>
  <a href="https://github.com/herry2059/project-os-for-codex/commits/main"><img src="https://img.shields.io/github/last-commit/herry2059/project-os-for-codex?style=for-the-badge" alt="Last Commit"></a>
</p>

<p align="center">
  <a href="#quick-start">🚀 Quick Start</a> ·
  <a href="docs/CODEX_SETUP.md">🤖 Connect Codex</a> ·
  <a href="#key-features">🧭 Features</a> ·
  <a href="docs/DEPLOYMENT.md">📦 Deployment</a> ·
  <a href="docs/INTERFACES.md">🔌 Interfaces</a>
</p>

Project OS for Codex is for the moment when a team asks: **What is the AI doing? Where should the next session start? How can another person or AI take over without rereading every chat?**

It is not another AI chat window. It is the control plane around the work: kickoff card, acceptance criteria, current progress, Git evidence, next action, reusable knowledge, and a handoff package that both humans and agents can read.

![Project OS for Codex working project cockpit in an isolated local workspace](docs/assets/product-dashboard-dark.png)

## 💡 Why Does This Exist?

AI can generate code quickly, but real projects still fail in very ordinary ways:

- The project progress is hidden inside chat history.
- The next AI session does not know where to start.
- Humans cannot tell which tasks are done, blocked, risky, or waiting for review.
- Handoffs become painful because context is scattered across prompts, screenshots, commits, and private notes.
- Teams lose trust because there is no visible project trail.

Project OS for Codex turns those scattered pieces into one workspace: project goals, acceptance criteria, Git records, progress events, risks, next steps, knowledge, and handoff packages.

### Built from repeated real delivery work

This is not a weekend concept built from imagined agent problems. It was distilled from recurring problems seen across many real internal and client projects, then refined through sustained Codex use: context loss, invisible progress, unclear acceptance, difficult handoffs, and knowledge that disappears after delivery.

The anonymized July 2026 maintainer snapshot below shows **14,570 Codex tasks, 8.8B lifetime tokens, a 23-day streak, and 743 skill uses**. These numbers are evidence of maintainer practice—not repository users, downloads, adoption, or 14,570 separate projects.

![Anonymized maintainer Codex activity: 14,570 tasks and 8.8B lifetime tokens](docs/assets/anonymized-codex-usage.svg)

## Explain It Like I Am New

Think of this system as a project cockpit for AI-assisted development.

When an AI helps you build a project, it should not only write code. It should also leave behind:

- what it changed;
- why it changed it;
- what still needs to be done;
- what risks remain;
- what the next human or AI should read first.

This repository provides the structure for that cockpit. It helps a project become something another person or AI can continue, instead of a one-time chat transcript.

## Connect Codex

Do **not** give an AI your website username and password. From a project page, create a short-lived AI credential that is bound to one workspace and one project, then run the generated MCP command in your own terminal.

The first production-oriented slice exposes two real MCP tools:

- `project_os_get_context` — reads the kickoff card, acceptance criteria, AGENTS rules, handoff package, progress, Git trail, and next step;
- `project_os_append_progress` — appends one validated, audited, idempotent progress event, an agent-reported verification note, and one matching project-record Git commit.

Credentials expire after 24 hours or 7 days, can be revoked independently, are stored only as hashes, and cannot access members, keys, deletion, publication, or deployment.

Version 0.3.0 adds a fail-closed first-run contract:

- the MCP process verifies the credential, project binding, scopes, and exact two-tool surface before Codex starts using it;
- the project-level configuration requires the server and allowlists only the released tools;
- from a checked-out and installed repository, `pnpm codex:doctor` exercises that checkout's MCP server and backend without calling the progress-write tool; normal credential usage and audit metadata are still recorded, and this local check does not prove that Codex loaded a saved client configuration or the pinned Git tag;
- root and generated `AGENTS.md` files tell Codex to read context first, verify one vertical slice, and only then write progress back.

[Follow the Codex setup guide →](docs/CODEX_SETUP.md)

### Designed around Codex's real extension points

- Codex reads the repository's root [`AGENTS.md`](AGENTS.md) before work starts.
- The stdio MCP server returns concise workflow instructions during initialization.
- Tool annotations distinguish the project-state read context tool from the scoped progress-write tool; successful reads still update credential-use and audit metadata.
- [`.codex/config.toml.example`](.codex/config.toml.example) shows a project-scoped configuration that forwards local environment variables without committing secret values.
- The same MCP configuration can be used by Codex CLI, the Codex IDE extension, and the ChatGPT desktop app on the same Codex host.
- High-risk actions stay outside the MCP surface and require a human.

See OpenAI's official [MCP](https://developers.openai.com/codex/mcp/) and [`AGENTS.md`](https://developers.openai.com/codex/guides/agents-md/) documentation. This repository extends Codex with project context and progress records; it is not a fork or replacement for Codex.

## Core Loop

![Git-backed project loop](docs/assets/git-loop.svg)

1. Create a project with a kickoff card.
2. Define the goal, acceptance criteria, non-goals, owner, and next step.
3. The server creates a local Git-backed project record for the kickoff, progress, issues, and handoff files.
4. Humans or AI agents post progress events.
5. Important progress becomes a project record and can be linked to Git commits.
6. The dashboard shows status, health, progress, and the recorded next action.
7. A handoff package lets the next AI or human resume without rereading the whole history.
8. Retrospectives and project notes become reusable knowledge for the next project.

## Key Features

### Project kickoff cards

Start every project with a clear brief:

- project goal;
- expected result;
- acceptance criteria;
- non-goals;
- current owner;
- next step.

### Visible AI progress

Track project state with progress events instead of guessing from chat logs:

- active / paused / done project states;
- progress percentage;
- owner;
- next action;
- green / yellow / red project health.

### Git-backed evidence

The system is designed around Git as the durable project record:

- project workspace records;
- Git file tracking;
- commit-friendly progress notes;
- audit trail for what changed and why.

### Handoff packages

Generate context that another AI or human can use immediately:

- project summary;
- current state;
- important files;
- recent decisions;
- blocked items;
- next step;
- acceptance checklist.

### Knowledge base and retrospectives

Turn finished project experience into reusable knowledge:

- project lessons;
- delivery patterns;
- reusable prompts and checklists;
- project review notes;
- future improvement ideas.

### Adapter-friendly open-source design

The open-source version keeps private infrastructure behind replaceable boundaries:

- Git database / Git service adapter;
- AI provider adapter;
- knowledge-base adapter;
- deployment and reverse-proxy boundary;
- local JSON persistence for simple evaluation.

No private API keys, production provider addresses, customer data, or internal deployment secrets are included.

### AI-native access instead of password sharing

- one short-lived credential per AI and project;
- workspace and project isolation enforced on the server;
- explicit read/append scopes;
- idempotent writes and Git request IDs;
- revocation and audit history;
- one focused MCP integration for Codex.

### Current scope and honest limits

The current release is a focused project-record layer around Codex, not a replacement agent runtime.

- It does not run Codex, monitor Codex sessions automatically, or control a Codex account.
- It does not connect to or modify an existing source repository. Its Git commits belong to the local Project OS record repository.
- A verification note is reported by Codex and stored for review; the server validates structure, identity, scope, idempotency, and progress rules, but it does not independently prove that source code or a deployment passed.
- The released MCP surface contains exactly two tools: scoped context read and scoped progress append.
- Existing source-repository integration, richer evidence, handoff drafts, knowledge drafts, remote MCP, and OAuth remain roadmap work.

## Open-Source Surface

This repository is the focused **OSS Project OS surface**. It exposes the project cockpit, kickoff cards, Git-backed progress, handoff packages, team spaces, knowledge base, and retrospectives.

Commercial SaaS modules such as sales back-office pages, paid-plan operations, platform administration, announcement systems, and payment infrastructure have been removed from the public runtime and source tree. A fresh local run starts as a normal project workspace, not as a hosted commercial admin console.

This repository does not include a hosted commercial service, private provider credentials, production customer data, payment infrastructure, or internal deployment secrets.

## Who Is This For?

This project is useful if you are:

- building projects with AI coding agents;
- managing multiple AI-assisted software projects;
- using Codex for real, multi-session software delivery;
- trying to make AI work visible to teammates, stakeholders, or future maintainers;
- tired of losing project context between chat sessions;
- building an internal AI project management platform;
- exploring context engineering, agent handoff, and Git-based AI workflows.

## Common Use Cases

- AI project management dashboard
- AI coding agent progress tracker
- Agent handoff and context package generator
- Git-backed project execution system
- Internal project operating system for AI teams
- Knowledge base for repeated AI delivery work
- Customer-facing project progress visibility
- Multi-project AI workflow control center

## Screenshots and Diagrams

### Working project cockpit

![Project OS for Codex local acceptance workspace in dark mode](docs/assets/product-dashboard-dark.png)

### Connect Codex

![Create a short-lived project credential for Codex](docs/assets/product-connect-ai-dark.png)

<details>
<summary>Light mode</summary>

![Codex project connection in light mode](docs/assets/product-connect-ai-light.png)

</details>

> Screenshots use an isolated local workspace with non-sensitive sample content. No customer account, production endpoint, or private credential is shown.

### Workflow diagram

![Workflow](docs/assets/workflow.svg)

### Git loop diagram

![Git-backed project loop](docs/assets/git-loop.svg)

### Architecture diagram

![Architecture](docs/assets/architecture.svg)

## Tech Stack

- Frontend: React, Vite, TypeScript, Tailwind CSS
- Backend: Node.js, Express
- Persistence: local JSON files by default
- Project record model: Git-oriented project workspace
- License: Apache-2.0

## Quick Start

Requirements:

- Node.js 22+ (a currently supported LTS line)
- pnpm 9+
- Git

The fastest local-only start is Docker Compose:

```bash
docker compose up --build
```

Open <http://localhost:8790>. The included Compose file binds to `127.0.0.1` and enables password-free access only for local evaluation.

For a manual development start, install frontend dependencies:

```bash
pnpm install
```

Start the backend:

```bash
pnpm --dir server run seed
PROJECT_OS_DEV_NO_AUTH=true pnpm --dir server start
```

Start the frontend in another terminal:

```bash
pnpm dev
```

Open the Vite URL shown in your terminal. The API listens on:

```text
http://localhost:8790
```

Production refuses to start without `PROJECT_OS_AUTH_USER` and `PROJECT_OS_AUTH_PASSWORD`.

For local, server, reverse-proxy, storage, backup, Git, AI provider, and knowledge-base setup, see:

- [Deployment Guide](docs/DEPLOYMENT.md)
- [Interface and Adapter Contracts](docs/INTERFACES.md)
- [Codex MCP Setup](docs/CODEX_SETUP.md)
- [Publication Security Checklist](docs/SECURITY_PUBLICATION_CHECKLIST.md)

## Agent Event Example

Project secrets must be sent in the `X-Project-Key` header. Do not put secrets in URLs.

```bash
curl -X POST http://localhost:8790/api/projects/<project-id>/events \
  -H 'Content-Type: application/json' \
  -H 'X-Project-Key: <project-secret>' \
  -H 'Idempotency-Key: progress-step-001' \
  -d '{"message":"Add handoff checklist","verification":"The checklist page loaded and each acceptance item was reviewed.","progressTo":55,"nextStep":"Run acceptance smoke test"}'
```

## Repository Keywords

People may find this project while searching for:

- AI project management
- Codex project management
- Codex delivery workflow
- MCP server
- Model Context Protocol
- AI coding agent dashboard
- agent handoff
- context engineering
- Git-based project management
- AI workflow automation
- project progress tracker
- knowledge base for AI teams
- developer tools for AI-assisted software delivery

## Current Status

This repository is an early public open-source release.

Version 0.3.0 closes the audited global-role/workspace-role escalation path, prevents startup migration from guessing or restoring a revoked default-workspace owner, and adds regression coverage for those boundaries. It also adds a reproducible repository-local MCP/backend connection doctor. The MCP surface remains exactly two scoped tools.

Before production use, review the release gate:

- multi-tenant permission audit;
- no production tokens, private domains, private docs, or customer data;
- `pnpm run check` passes;
- Agent API + MCP acceptance tests pass;
- light and dark UI screenshots reviewed;
- clear deployment, backup, and rollback plan.

## Roadmap

- Stronger project role model
- Remote OAuth-protected MCP transport
- More scoped tools for handoff drafts and knowledge drafts
- Better visual progress timeline
- Provider adapter examples without shipping private keys
- Playwright smoke tests
- A short end-to-end workflow GIF and more guided examples
- More beginner-friendly setup recipes

## Independent Project

Codex is a trademark of OpenAI. This independent open-source project is not affiliated with or endorsed by OpenAI.

## Long-term Maintenance

This repository is intended to be maintained in public. Every release will document verified additions, security changes, known limits, and the next milestone in [CHANGELOG.md](CHANGELOG.md) and [ROADMAP.md](ROADMAP.md).

The latest release is **v0.3.0: Codex First-Run Contract**—fail-closed MCP preflight, a project-state connection doctor, strict tool allowlisting, clearer `AGENTS.md` execution rules, and workspace-role security regression tests.

The next milestone is **v0.4.0: guided Codex onboarding**. Remote MCP, OAuth, source-repository synchronization, and maintainer automation remain planned work and are not presented as released functionality.

## Contributing

Issues, ideas, and pull requests are welcome. Good contributions include:

- clearer documentation;
- adapter examples;
- deployment recipes;
- UI improvements;
- security hardening;
- real-world AI project workflow cases.

If this project helps you, starring the repository makes it easier for more AI builders and project teams to discover it.
