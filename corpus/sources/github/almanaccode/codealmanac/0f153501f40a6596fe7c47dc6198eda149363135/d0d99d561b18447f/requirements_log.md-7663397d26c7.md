# Requirements Log

Working agreement log for the hosted Almanac GitHub App direction. This file should record settled requirements only; unresolved ideas stay out until we decide them.

## Product Name And Language

- Use "Almanac" and "Update the Almanac" language in product UX.
- Avoid the word "memory" in user-facing GitHub App copy.

## Core GitHub App Flow

- The hosted product starts as an Almanac GitHub App, not a generic connector platform.
- The App runs on pull requests and proposes Almanac changes when the PR contains project knowledge that belongs in the repo Almanac.
- For same-repository PRs, the PR UI should offer three actions: "Update this PR", "Skip this PR", and "Always update in this repo".
- "Update this PR" is ongoing approval for the current PR: Almanac may rerun as commits, comments, or review discussion change until the PR is merged, closed, or skipped.
- "Always update in this repo" promotes the behavior to a repository default for future same-repository PRs.
- For v1, the first PR prompt is permission-first: it asks whether Almanac should update the PR, but does not need to show a generated diff before the user opts in.
- "Update this PR" commits Almanac changes to the current PR branch.
- "Skip this PR" leaves the branch unchanged and stops future prompts/runs for that PR unless the user re-enables Almanac.
- A PR should have one Almanac check/comment thread that updates in place rather than a new bot comment on every push.
- A PR may have many Almanac runs as the branch evolves. The app should track current head SHA, last prompted head SHA, last run head SHA, last Almanac commit SHA, and status.
- Draft PRs should wait until `ready_for_review` before the first Almanac prompt.
- Same-repository PRs can be updated by committing Almanac changes to the PR branch.
- Fork PRs should use post-merge Almanac updates by default: after the PR merges, Almanac can open a follow-up PR against the upstream repository.
- Fork PR copy should avoid negative permission framing. Preferred prompt: "Update the Almanac after merge? After this PR merges, Almanac can open a follow-up PR with any Almanac updates."
- Fork PR actions should be "Update after merge", "Skip this PR", and "Always do this for fork PRs".

## Repo-Owned Almanac

- The repo remains the canonical source of truth for Almanac pages.
- Almanac updates are written as Git changes, not hidden hosted-only records.
- The Almanac root/path must be configurable by the repository.
- App-authored commits for "Update this PR" must only change files under the repository's configured Almanac root, such as `.almanac/**` or `docs/almanac/**`.

## Settings

- Decision: GitHub App settings live in the hosted dashboard/database for v1, not in repo configuration.
- Reason: repo-based settings add unnecessary write/review complexity before the GitHub App loop is proven.
- New repositories default to asking on future same-repository PRs after installation.
- The GitHub App should not backfill existing open PRs immediately after installation.
- Existing open PRs may enter the flow only after a future trigger such as `ready_for_review` or a new supported PR event.
- The first settings surface should stay simple: ask, auto-update, or disabled.
- Same-repository PR behavior has exactly three v1 modes: `ask`, `auto`, and `disabled`.
- Changing a repository to `auto` is forward-looking only. It affects future PR triggers, not existing PRs that were already prompted or skipped unless the user explicitly runs Almanac on those PRs.

## Hosted Product Boundary

- `codealmanac` remains the open-source/local engine and prompt stack.
- `usealmanac` is the natural home for the hosted website, onboarding, GitHub App installation flow, dashboard, and settings UI.
- The hosted service coordinates GitHub events, runs, checks, and App-authored commits, but the durable Almanac content lives in the repo.
- Hosted backend and worker orchestration may be Python if that makes the product easier to build and maintain, while reusing CodeAlmanac's operation prompts and repository-writing behavior where practical.

## Hosted Worker Model

- The hosted worker should feel like a coding agent dropped into a real codebase environment with additional Almanac instructions.
- The worker gets a repository checkout, the configured Almanac root, GitHub source access for the triggering PR, and instructions to update only the Almanac root.
- GitHub PR context should not be pre-injected as a fixed context bundle by default. The agent should receive additional instructions that it must inspect the relevant PR source material through available tools, then decide what to read and what matters.
- The run should reuse CodeAlmanac's existing operation prompts and judgment model instead of replacing them with a deterministic hosted pipeline.
- The web/API service should not run long agent jobs directly; it should receive GitHub events, enqueue jobs, and return quickly.
- The v1 async execution path should evaluate Modal as both the fire-and-forget job runner and the sandbox substrate, because Modal supports async function spawning and secure sandboxes.
- Daytona and E2B remain fallback sandbox options if Modal Sandbox cannot support the repo-agent workflow cleanly.
- "Update only the Almanac root" means the publisher should only push/commit changes under the repository's configured Almanac path; the agent may still read the whole checkout and inspect GitHub PR context through tools.
- The hosted run needs an isolated sandbox/codebase environment that can clone and check out a PR branch, inject secrets and tool configuration, run an AI coding-agent harness or CodeAlmanac operation, collect the resulting diff, validate write scope, and clean up after the run.

## GitHub App Permissions

- The GitHub App can request read/write permissions for repository contents, pull requests, issues, and checks.
- Metadata permission is read-only.

## GitHub Access Model

- GitHub appears in two roles: the GitHub App handles installation, permissions, webhook triggers, checks, and bot-authored writes; GitHub source access lets the agent inspect PRs, reviews, comments, diffs, commits, issues, and linked context during an Almanac operation.
- GitHub source access is tool access, not prompt stuffing. The hosted operation should tell the agent which PR triggered the run and require it to inspect the source tools as part of the task.
- Hosted automation is owned by Almanac: webhook handling, queuing, worker orchestration, sandbox setup, and publishing back to GitHub are part of the hosted product surface.
- GitHub source access should evaluate the official GitHub MCP server as the preferred tool transport if it works cleanly with GitHub App installation tokens.
- The likely MCP path is running the official local/Docker GitHub MCP server inside the Modal sandbox/job with the installation token, `GITHUB_READ_ONLY=true`, and toolsets such as `pull_requests,repos,issues,actions`.
- Official remote GitHub MCP remains less attractive for v1 because installation-token support is not the primary documented path and local deployment gives better control.
- Octokit-backed native tools remain the fallback if official GitHub MCP does not work cleanly in the hosted worker.
- GitHub App auth and GitHub source tooling are separate concerns: the App creates/scopes access and receives events; the source tooling can be native API wrappers, an MCP server, or another adapter that runs under that scoped access.

## Secrets

- Use Doppler for hosted product secret management where possible.
- Secrets likely include GitHub App private key, GitHub webhook secret, model provider keys, Modal tokens, database credentials, and any MCP/source-tool credentials.
- GitHub App installation tokens are short-lived runtime credentials minted per job; they should not be stored as durable secrets.

## Backend And API Questions To Design Next

- GitHub App installation callback and repository onboarding.
- GitHub webhook verification and event ingestion.
- Repository settings API for Almanac root and PR behavior mode.
- Check/button handling for "Update this PR", "Ignore", and "Always update automatically".
- Run/job records for PR-triggered Almanac update attempts.
- Modal job invocation and result/status reporting.
- Hosted wiki browsing API for repo Almanac pages.

## Platform Direction

- V1 should evaluate a Modal-only hosted execution path: usealmanac API receives GitHub events and starts Modal async jobs; Modal Sandbox provides the isolated repo workspace for the agent run.
- Daytona and E2B are fallback sandbox options if Modal Sandbox cannot support the repo-agent workflow.
- The first runtime spike should test GitHub App installation-token access through raw REST, remote GitHub MCP, and local/Docker GitHub MCP before committing to the source-tool implementation.

## Proposal Lifecycle

- Current v1 direction is permission-first rather than proposal-storage-first.
- The first check/comment asks whether to run Almanac without storing a proposed diff.
- After the user clicks "Update this PR", the full job runs and commits any resulting Almanac changes directly to the PR branch.
- GitHub becomes the review surface for the actual diff after Almanac commits to the PR branch.
- This avoids proposal storage, custom diff rendering, and apply-later patch handling in the first version.

## Update Delivery

- Decision: "how an Almanac update is delivered" is a first-class abstraction, separate from trigger handling, source access, and agent judgment.
- The initial delivery methods are same-PR branch commit for same-repository PRs and post-merge follow-up PR for fork PRs.
- Future delivery methods may include comment-only, hosted proposal, separate Almanac branch, external Almanac repo, or batched post-merge PRs, but those should share one delivery interface rather than becoming separate operation flows.
- Delivery code owns GitHub writes: updating comments/checks, committing to branches, opening follow-up PRs, and recording publisher actions.
- Operation/agent code owns judgment: whether an Almanac update belongs and what Almanac files should change.
