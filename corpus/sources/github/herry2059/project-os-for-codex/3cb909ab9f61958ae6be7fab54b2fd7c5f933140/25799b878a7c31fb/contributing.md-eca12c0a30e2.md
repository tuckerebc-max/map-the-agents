# Contributing

Thanks for helping improve Project OS for Codex.

## What We Value

- Real project evidence over vague claims.
- Small vertical slices over large unreviewable rewrites.
- Clear handoff notes for every meaningful change.
- Security boundaries that are boring, explicit, and easy to audit.

## Local Setup

```bash
pnpm install
cd server
pnpm run seed
PROJECT_OS_DEV_NO_AUTH=true pnpm start
```

In another terminal:

```bash
pnpm run dev
```

## Pull Requests

Before opening a PR:

- Run `pnpm run check`.
- Review the affected real page in both light and dark themes.
- Keep private provider keys and production data out of the branch.
- Update docs when changing interfaces or deployment behavior.

## Security

Do not open a public issue for secrets, auth bypasses, cross-workspace access, or data deletion bugs. Use `SECURITY.md`.
