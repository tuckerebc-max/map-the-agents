# Security Policy

## Supported Versions

The current supported line is `0.2.x`. This remains an early open-source release. Do not host sensitive customer data until you have completed the publication checklist, backup, tenant-isolation regression tests, and your own deployment review.

## Report a Vulnerability

Please do not disclose security issues in public issues.

Include:

- affected version or commit
- reproduction steps
- expected and actual behavior
- impact scope
- whether credentials, workspace data, or project secrets are exposed

## Sensitive Data Rules

Never commit:

- `.env`
- API keys or provider tokens
- private AI provider or billing integration code
- production domain internals
- customer data
- `server/data`
- Codex or other raw AI conversation logs

## Required Checks Before Public Hosting

- No project secret in URLs.
- Workspace isolation verified.
- AI credentials are short-lived, revocable, scoped, hashed at rest, and audited.
- Agent writes are validated and idempotent.
- Project deletion recoverable or explicitly confirmed.
- Provider credentials server-side only.
- Production password authentication configured; `PROJECT_OS_DEV_NO_AUTH` disabled.
- Backup and rollback tested.
