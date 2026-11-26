# Changelog

## 0.3.0

### Added

- Fail-closed MCP startup preflight for credential validity, project binding, required scopes, and the exact released two-tool surface.
- A repository-local `pnpm codex:doctor` command that performs a real MCP handshake and context read against the current checkout without calling the progress-write tool; normal credential usage and audit metadata are recorded.
- A strict project-level Codex configuration with a required server and explicit tool allowlist.
- A Codex session protocol in both the repository rules and newly generated project `AGENTS.md` files.
- Regression coverage for MCP tool annotations, wrong-project setup, revoked credentials, doctor project-state zero-write plus audit behavior, and workspace role isolation.
- Release-guard checks that keep package, server, MCP, setup guide, and generated connection versions aligned.

### Changed

- Updated the public package metadata and release references to v0.3.0.
- Raised the supported runtime to maintained Node.js 22+ lines, expanded CI coverage to Node.js 22 and 24, and moved the container image to Node.js 24.
- Standardized contributor and server instructions on `pnpm`.
- Updated `nodemailer` to the audited 9.x line and added a high-severity production dependency audit to CI.
- Removed the direct maintainer profile screenshot from the v0.3.0 tree; the fully anonymized aggregate graphic remains with its non-adoption disclaimer.

### Security

- Workspace administration now depends only on the active workspace membership. A historical global account role can no longer elevate a member in another workspace.
- Default-workspace startup migration no longer guesses an owner from a global role or user order. Active owner memberships are authoritative; an explicit persisted owner is used only when the workspace has no membership history, and a freshly seeded identity is used only when no prior membership exists.
- Owner membership revocation now synchronizes the workspace owner pointer, so a removed or downgraded owner is not restored after restart. A protected first start after local no-auth evaluation is covered by an integration test.
- MCP errors map to safe connection categories instead of returning backend error strings.
- Local `.codex/config.toml`, `.codex/*.env`, and Codex logs are explicitly ignored.

## 0.2.0

### Added

- Short-lived AI credentials bound to one workspace and one project.
- Revocation, expiry, audit history, rate limiting, and server-derived agent identity.
- Idempotent Agent API progress writes with one matching Git commit.
- A stdio MCP server for Codex.
- Root `AGENTS.md` and an English Codex setup guide.
- Real dark/light product screenshots and Agent API + MCP acceptance tests.
- Plain-language progress fields for result, reason, benefit, stage, and next action.
- Owner approval for workspace join requests; invite codes no longer grant membership directly.
- An anonymized maintainer activity graphic with an explicit non-adoption disclaimer.

### Changed

- Production now fails closed when bootstrap password authentication is missing.
- Local Docker evaluation binds to `127.0.0.1` and enables no-auth mode explicitly.
- New integrations use short-lived MCP credentials; the persistent project key API is compatibility-only.
- README, package metadata, `llms.txt`, and public metadata now describe the verified Codex MCP integration.
- Renamed the public project to `Project OS for Codex` and the repository target to `project-os-for-codex` while keeping an explicit independent-project disclaimer.
- Replaced runtime variables with the neutral `PROJECT_OS_*` prefix.

### Security

- Agent writes validate progress, prevent rollback, require stable idempotency keys, and ignore body-supplied actor names.
- Cross-workspace and cross-project access is rejected from the credential's server-side ownership fields.
- Project deletion revokes all active AI credentials for that project.
- Provider keys and website passwords are excluded from the Agent API and MCP surface.
- Workspace joins require owner/admin review and reject cross-workspace request IDs.
- Browser progress actors are derived from the authenticated session rather than request bodies.
- Reaching 100% progress still requires a human to confirm project closure.
- Network metadata is excluded from AI audit records unless the operator explicitly opts in.

## 0.1.0-public-candidate

### Added

- Public README and deployment documentation.
- Deployment and interface documentation.
- Adapter boundary documentation for Git, AI provider, and knowledge storage.
- Curated public starter knowledge with no private customer data.
- Security publication checklist.

### Changed

- Removed deployment-specific provider implementation from the public candidate.
- Replaced internal business seed data with curated public starter knowledge.
- Project secrets are documented as header-only.

### Security

- Excluded production data, private deployment cards, and conversation logs from the public candidate.
- Added explicit guidance to keep provider secrets server-side only.
