# AI contributor rules

These rules apply to Codex and every contributor working in this repository.

## Product truth

- This is a real open-source project, not a UI demo. Do not add fake success states, fake production data, or claims that are not implemented.
- Project OS for Codex makes AI-assisted projects visible, resumable, and handoff-ready through project context, Git evidence, next actions, and structured handoffs.
- Work one vertical slice at a time. Finish and verify one end-to-end path before widening the surface.

## Architecture and security

- Every persisted business record must belong to a `workspaceId`. Requests must derive the workspace from a verified session or AI credential, never from an untrusted body field.
- AI credentials must be short-lived, revocable, hashed at rest, scoped to the minimum project and actions, and covered by audit logs.
- Never put passwords, access tokens, provider keys, private endpoints, customer data, or production exports in source, logs, screenshots, prompts, issues, or commits.
- AI may read context and prepare drafts. Payment, deletion, role changes, credential management, publication, deployment, and rollback always require explicit human confirmation.
- Public error messages must not reveal private providers, internal routes, balances, or infrastructure details.

## Development workflow

- Read `README.md`, `docs/INTERFACES.md`, and the relevant source before changing behavior.
- Preserve user changes and keep commits focused on the requested slice.
- Use `pnpm` for dependency and build commands.
- Before committing, run `pnpm run check` and inspect the real affected UI in both light and dark themes.
- A change is complete only when the real path works end to end. A diff or a mocked response is not acceptance evidence.

## Agent integration contract

- Prefer MCP or documented API/CLI tools over browser automation.
- Never ask users to paste their website password into an AI conversation.
- Project event writes require `Idempotency-Key`, server-derived actor identity, input validation, workspace and project isolation, and an audit event.
- Keep dangerous tools out of the MCP surface until a human approval workflow exists.

## Codex session protocol

- When a Project OS MCP connection is configured, call `project_os_get_context` before planning or editing. If it fails, do not guess or claim the project is connected; run `pnpm codex:doctor` and report the blocker.
- Read the source checkout's local `AGENTS.md` as the code-change contract. Treat Project OS context as the project goal, recorded state, acceptance criteria, and next action. If they conflict or look stale, stop and ask for human direction.
- Complete and verify one vertical slice. Only then call `project_os_append_progress` with the checked result, plain-language result, reason, benefit, verification, and next action.
- Do not record plans, attempts, failed checks, or unverified output as completed progress.

## Deployment

- Do not deploy, restart production, change live permissions, delete data, or force-push without explicit human confirmation.
- Use staging, smoke tests, backup, and rollback for production changes. Do not use blind `rsync` overwrites.
