# Publication Security Checklist

Use this checklist before every public release, not only the first one. A clean working tree is insufficient: review tracked files, generated assets, build output, Git history, release archives, and the repository settings that will become public.

## 1. Content that must never enter the public repository

- `.env` files, access tokens, API credentials, cookies, private keys, recovery codes, or generated agent credentials;
- production hostnames, IP addresses, filesystem paths, infrastructure inventories, or deployment runbooks that reveal private systems;
- customer, employee, contractor, or contact records;
- personal phone numbers, personal email addresses, account identifiers, avatars, and unapproved real names;
- raw Codex or other AI conversations, prompts containing private context, terminal history, or diagnostic archives;
- real project repositories, production exports, database snapshots, or populated `server/data` directories;
- private AI service integration code, billing logic, metering records, or service credentials;
- screenshots that show accounts, usage identity, private paths, browser tabs, notifications, credentials, or customer information.

## 2. Public-build security model

- Persisted records belong to a `workspaceId`.
- A request derives its workspace from a verified session or credential, not from an untrusted request body field.
- Workspace administration is derived only from the active workspace membership; a global account role never grants authority in another workspace.
- Startup migration never guesses a default-workspace owner from a global role or user order. Active owner memberships are authoritative; persisted ownership may create the first membership only when no membership history exists, and a freshly seeded identity is accepted only when no prior membership exists.
- New Codex connections use short-lived, project-scoped credentials rather than website passwords.
- Agent credentials are sent in `Authorization: Bearer`, returned in plaintext once, and stored only as hashes.
- The legacy compatibility secret is accepted only in `X-Project-Key`.
- Project event writes require a stable `Idempotency-Key` and an audit record.
- Credential creation, role changes, deletion, publication, deployment, and rollback remain human-approved actions.
- Public errors do not reveal private service details, balances, configured models, or infrastructure.

## 3. Source and history review

Before publishing:

1. inspect `git status` and every staged diff;
2. scan all tracked text for secret patterns, personal information, private domains, private IP addresses, internal product names, and absolute paths;
3. inspect Git history and all refs that may be pushed, not only the current files;
4. verify `.gitignore` excludes local data, environment files, credentials, logs, and generated archives;
5. inspect release archives and Docker build context separately;
6. verify the push command targets only the intended branch and tags; never use `--mirror` or `--all` from a repository that contains private backup refs.

If a credential ever entered Git history, revoke or rotate it first. History rewriting is not a substitute for rotation. Back up the repository, obtain explicit approval, rewrite all public refs, verify the new history, and coordinate any required force push with collaborators.

## 4. Screenshot and media review

Use purpose-built sample content, not blurred production screenshots. Blurring can be reversible or can leave readable metadata and surrounding context.

For every image:

- use English UI text for the default public presentation;
- remove names, email addresses, phone numbers, handles, avatars, organization names, project names, usage identity, and account badges;
- remove browser chrome, tabs, desktop notifications, terminal prompts, file paths, and hidden panels that are not part of the product;
- confirm no credential or private URL appears at full resolution;
- strip unnecessary metadata;
- open the committed image from a clean clone and inspect it at 100 percent zoom.

An anonymized usage image may show aggregate, non-identifying metrics only when the values are accurate and the image does not imply that those metrics are repository adoption statistics.

## 5. Functional and security release gate

The release may proceed only after all of the following are true:

- P0 workspace-isolation and permission findings are closed;
- production authentication fails closed when required variables are missing;
- agent credentials are workspace-bound, project-bound, scoped, expiring, revocable, hashed at rest, and audited;
- cross-workspace context reads and writes are rejected by automated tests;
- a global administrator account with only member access in the current workspace is rejected by workspace-administrator endpoints;
- existing workspace ownership survives restart without granting the first user or a global administrator a new default-workspace membership;
- removing or downgrading one of multiple owners updates the workspace owner pointer and does not restore that owner after restart;
- idempotent retries produce one event and one Git commit;
- `pnpm run check` succeeds;
- affected UI paths are inspected in both light and dark themes;
- staging smoke tests cover login, project creation, context read, progress write, credential revocation, backup, and rollback;
- the public data directory contains only intentional seed content;
- the repository name, visibility, Apache-2.0 license, topics, release notes, and account identity have human approval.

## 6. Final human confirmation

Publication, deployment, permission changes, history rewriting, and traffic switching are high-risk actions. Record the exact branch, commit, tag, repository URL, backup location, rollback command, and approver before execution.
