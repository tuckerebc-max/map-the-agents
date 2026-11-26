# Connect Codex

Project OS for Codex gives Codex explicit project tools. It does not ask Codex to sign in as a human and click through the whole website.

The first production-oriented vertical slice lets an agent:

1. read one project's goal, acceptance criteria, rules, progress, Git trail, handoff, and next step;
2. append one structured progress event with an agent-reported verification note;
3. create exactly one matching project-record Git commit, even when a network retry repeats the request;
4. make the result immediately visible in the web timeline.

## Requirements

- Node.js 22 or newer on a currently supported LTS line, `npx`, and Git on the machine that runs the stdio MCP server;
- Codex CLI, the Codex IDE extension, or another Codex host that supports MCP;
- a running Project OS server reachable over HTTPS outside local evaluation;
- one short-lived project credential created by a human project owner or workspace administrator.

Codex does not provide a system Node.js runtime for arbitrary local MCP packages. If `node --version` or `npx --version` fails, install Node.js before continuing.

## Why the agent should not receive your website password

A website account can usually manage projects, users, credentials, deletion, and settings. A password pasted into a model conversation can enter chat history, logs, screenshots, or a third-party service, and you cannot revoke access for just one agent.

The system uses a short-lived AI credential instead:

- bound to one `workspaceId` and one `projectId`;
- fixed scopes: `project.context.read` and `project.events.append`;
- expires after 24 hours or 7 days;
- independently revocable;
- returned in plaintext once and stored by the server only as a hash;
- server-derived agent identity rather than an actor supplied in the request body;
- audit records for reads, writes, rejected requests, idempotent replays, rate limits, and revocation.

## 1. Start the app

For local evaluation:

```bash
docker compose up --build
```

Open <http://localhost:8790>. The included Compose file listens on `127.0.0.1` only.

## 2. Create the connection

1. Create a project and define its acceptance criteria and next step.
2. Open the project and select **Connect**.
3. Under **Connect Codex**, name the connection and choose 24 hours or 7 days.
4. Select **Create AI credential**.
5. Run the generated command directly in your own terminal.

Do not paste the generated command or credential into a model chat, issue, screenshot, log, or repository.

## 3. Connect Codex

The page generates a command with real values. Its shape is:

```bash
codex mcp add project-os-<project-id> \
  --env PROJECT_OS_BASE_URL='https://your-domain.example' \
  --env PROJECT_OS_AGENT_TOKEN='pos_...' \
  --env PROJECT_OS_PROJECT_ID='<project-id>' \
  -- npx -y github:herry2059/project-os-for-codex#v0.3.0
```

Check the connection:

```bash
codex mcp list
```

`codex mcp list` proves that Codex parsed the configuration. It does not prove that the service, credential, project binding, scopes, tools, and context read all work.

Version 0.3.0 performs a fail-closed capability check before the MCP server accepts a Codex session. For an explicit project-state check from this repository, expose the same three `PROJECT_OS_*` values through your local shell or secret manager and run:

```bash
pnpm install --frozen-lockfile
pnpm codex:doctor
```

A successful check prints the project name, current progress, next step, and `MCP tools: 2/2 available`. The doctor never calls the progress-write tool, so project progress and Git history stay unchanged. The server still records normal credential usage and the two read audit events (`capabilities.read` and `project.context.read`). This command exercises the MCP server in the current checkout; it does not prove that Codex loaded a saved client configuration or that the pinned Git tag can launch. Use `codex mcp list` for entries added through the CLI and Codex's `/mcp` view for project-scoped configuration.

Then ask Codex:

```text
Read the Project OS context first. Summarize the goal, acceptance criteria, risks, and next step. Complete and verify the next slice, then append one progress event.
```

[Official Codex MCP documentation](https://developers.openai.com/codex/mcp/)

## Current tools

### `project_os_get_context`

Project-state read-only. Returns the kickoff card, acceptance criteria, `AGENTS.md`, handoff package, progress, recent Git trail, and next step without changing project progress or Git history. A successful request still updates the credential's last-used timestamp and appends a read audit event.

### `project_os_append_progress`

A low-risk write tool with the following input:

- `message`: a concise technical statement of the checked result;
- `plainMessage`: the same result in language a non-technical project owner can understand;
- `why`: why this vertical slice was completed now;
- `benefit`: the concrete benefit for the user or next maintainer;
- `verification`: the concrete check performed, such as a command and result, inspected URL, screenshot, or artifact; this is agent-reported evidence for human review;
- `stageIndex`: optional project stage number from 1 to 99;
- `progressTo`: optional percentage from 0 to 100; it cannot move backward;
- `nextStep`: the required next concrete action; when progress reaches 100, it must state that human closure approval is pending;
- `idempotencyKey`: optional stable retry key; the MCP bridge derives one from the MCP request when omitted.

The server records the credential label as the actor. A request cannot claim a different identity in its body.

If the same idempotency key and payload are retried, the server returns the existing result and does not create a second event or Git commit. Reusing that key with a different payload returns `409`.

## Codex-focused behavior

The MCP server is shaped around Codex's documented capabilities:

- its initialization instructions tell Codex to read context first, follow `PROJECT.md` and `AGENTS.md`, complete one checked slice, include a verification note, and stop for human approval on high-risk actions;
- initialization verifies the short-lived credential, configured project binding, required scopes, and exact released tool surface before Codex can use the server;
- `project_os_get_context` is marked project-state read-only and idempotent; successful requests still persist normal credential-use and audit metadata;
- `project_os_append_progress` is marked non-destructive and idempotent, but it remains an explicit write tool;
- the root `AGENTS.md` gives Codex durable repository rules before work starts;
- the generated command follows the official `codex mcp add ... -- <stdio command>` shape.

The checked-in configuration is intentionally strict: `required = true` fails the Codex startup path when project context is unavailable, and `enabled_tools` allowlists only the two tools released in v0.3.0. The write tool remains subject to the `writes` approval mode.

Codex stores MCP settings in its configuration. The short-lived token is therefore present on the client until you remove the entry. Use HTTPS in production, choose the shortest practical lifetime, revoke the credential after the task, and remove the local entry:

```bash
codex mcp remove project-os-<project-id>
```

For a project-scoped setup that forwards local environment variables instead of committing values, first inspect the checkout, its root `AGENTS.md`, and [`.codex/config.toml.example`](../.codex/config.toml.example). Copy the example to `.codex/config.toml` only when you trust that repository content, expose the three `PROJECT_OS_*` variables through your local shell or secret manager, and restart Codex. The repository ignores `.codex/config.toml`, `.codex/*.env`, and `.codex-log/`, but you should still inspect `git status` before every commit.

From the repository root, ask the installed Codex CLI to load that project configuration and report missing local runtimes or unresolved MCP commands:

```bash
codex -C "$PWD" doctor --all
```

This diagnoses the Codex client and its saved configuration. It complements `pnpm codex:doctor`, which checks the Project OS credential, binding, capability surface, and context read against the current checkout.

The example allows 90 seconds for the first MCP startup because a cold `npx` run may need to fetch the pinned Git release and its dependencies. Later cached starts should be faster.

The Git tag in the example is a release reference, not a software supply-chain guarantee. Until a provenance-backed package is published, review the release commit before allowing the MCP process to receive a credential and upgrade intentionally.

## AI access by module

The current MCP surface is intentionally smaller than the web application. This table describes what is available now and the boundary planned for future vertical slices. Planned actions are not implemented MCP tools yet.

| Area | Available to an agent now | Human-only boundary |
| --- | --- | --- |
| Project overview | Read the current project context and next step | No direct edit tool |
| Project timeline | Append a scoped, auditable progress event | Change ownership, edit the kickoff record, delete, or restore |
| Handoff | Read the handoff material returned with project context | Approve a formal handoff or change access |
| Project files | Read `HANDOFF.md`, `PROJECT.md`, `AGENTS.md`, and `PROGRESS.md` returned with context | Edit protected source or approve formal delivery |
| Team and access | No MCP tool | Invite, change role, suspend, or remove a member |
| AI credentials | No MCP tool | Create, reveal, rotate, or revoke credentials in the web application |
| Deployment | No MCP tool | Change configuration, deploy, roll back, or change domains and permissions |

Future tools must reuse the same controls: verified `workspaceId` isolation, minimum scopes, short expiration, idempotency, audit records, and explicit human approval for high-risk actions. The project will not bypass these controls by giving an agent an administrator password and asking it to click through the website.

## What remains human-only

Deleting or restoring projects, changing owners or roles, managing credentials, publishing knowledge, payments, deployment, and rollback are not exposed as MCP tools. Future modules will use draft and approval workflows rather than giving an agent unrestricted browser access.

## Remove or revoke access

Revoke the credential immediately from the project's **Connect** tab. You can also remove the local MCP entry:

```bash
codex mcp remove project-os-<project-id>
```

## Errors

- `401`: credential is invalid, expired, or revoked.
- `403`: credential lacks the required scope.
- `404`: credential does not belong to this project, or the project is deleted.
- `409`: the same idempotency key was reused for different content.
- `429`: too many writes in one minute.

Never solve a connection problem by disabling production authentication.

In production, the server refuses to start when the required bootstrap authentication variables are missing. `PROJECT_OS_DEV_NO_AUTH=true` is restricted to non-production local development.
