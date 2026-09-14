# Releasing

`package.json` is the release source of truth for `denchclaw`.

## Main flow

1. Bump the root package version in `package.json`.
2. Push or merge that commit to `main`.
3. GitHub Actions runs `.github/workflows/release.yml`.
4. If that version is not already on npm, the workflow runs the same `deploy.sh` test and build checks in validation mode.
5. Only after those checks pass does the workflow publish `denchclaw` to npm.
6. The workflow creates a matching GitHub release named `v<version>`.

If the npm package already exists, the workflow skips publishing. If the GitHub release already exists, the workflow skips creating it. This makes reruns safe.

## Local commands

- `pnpm run deploy`
- `pnpm run deploy:check`
- `pnpm run deploy:patch`
- `pnpm run deploy:minor`
- `pnpm run deploy:major`
- `pnpm run github:sync-secrets`

The deploy commands load `.env` automatically when it exists.

Examples:

```bash
pnpm run deploy:check
pnpm run deploy
pnpm run deploy -- --dry-run --version 2.3.15
pnpm run deploy:patch
```

## GitHub Actions secrets

The release workflow expects:

- `POSTHOG_KEY`
- `NPM_TOKEN`

To sync the current local `.env` values into GitHub repository secrets:

```bash
pnpm run github:sync-secrets
```

## Better long-term option

The workflow supports `NPM_TOKEN` today because that matches the current local deploy process. For better security, configure npm trusted publishing for `.github/workflows/release.yml` and then remove `NPM_TOKEN`. The deploy script already supports GitHub Actions OIDC when no `NPM_TOKEN` is present.
