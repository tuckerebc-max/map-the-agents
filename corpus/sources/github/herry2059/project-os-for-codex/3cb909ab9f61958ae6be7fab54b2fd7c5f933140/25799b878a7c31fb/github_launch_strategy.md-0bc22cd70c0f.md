# GitHub Launch Strategy

This document is a publication checklist for maintainers. It is not marketing copy and must not be used to invent adoption, usage, customer, or performance claims.

## Repository identity

Recommended repository name:

`project-os-for-codex`

Project title:

`Project OS for Codex: Visible progress, durable context, and safe handoffs for AI-built projects`

GitHub About:

`Self-hosted project memory and handoff for Codex: MCP context, visible progress, Git evidence, and resumable AI work.`

The product should lead with Codex because the current vertical slice includes a working Codex MCP setup, project-context read, and idempotent progress write. Do not describe future tools as available today.

## Honest origin story

The strongest positioning is the real problem, not an inflated number:

> AI coding sessions can produce working code while leaving the next person without a reliable goal, acceptance criteria, decision trail, current status, or next step. Project OS for Codex turns those missing handoff signals into durable project context, visible progress, Git evidence, and a scoped MCP interface.

If the maintainer wants to discuss experience across many real projects, describe the recurring patterns and lessons that shaped the product. Publish a numeric project count only when it has a defined methodology and verifiable evidence. Personal Codex usage metrics may support the maintainer's experience, but they are not repository adoption, user, or quality metrics.

## Recommended topics

Use topics that match implemented behavior:

`codex`, `mcp`, `model-context-protocol`, `ai-agents`, `ai-coding`, `ai-project-management`, `agent-handoff`, `context-engineering`, `project-management`, `developer-tools`, `self-hosted`, `git`, `typescript`, `react`, `workflow-automation`

Do not add topics for storage adapters, hosted services, or agent capabilities that are only roadmap items.

## README first-screen structure

The first two screens should answer five questions without requiring product knowledge:

1. What breaks in an AI-assisted project?
2. What does this repository make visible and durable?
3. What can Codex do through MCP today?
4. What remains under human control?
5. How can a developer run it with the shortest safe path?

Recommended order:

1. title and one-sentence outcome;
2. real light and dark product screenshots containing only non-sensitive sample content;
3. a short problem-to-outcome comparison;
4. the current MCP tools and security boundary;
5. Docker quick start;
6. architecture and Git evidence flow;
7. detailed capabilities, limitations, deployment, security, roadmap, and contributing links.

Avoid an oversized badge wall, unsupported superlatives, fake testimonials, placeholder screenshots, and roadmap features written in present tense.

## Usage image rules

An anonymized Codex usage image can explain why the maintainer cares about durable context and handoffs. It must:

- use English text;
- omit the profile name, handle, email, avatar, account tier, organization, and account identifiers;
- exclude browser chrome, private tabs, notifications, file paths, and unrelated applications;
- show only accurate aggregate metrics the maintainer has chosen to make public;
- state clearly that the metrics describe maintainer experience, not repository adoption or benchmark results;
- avoid claims that usage volume proves product quality.

## Launch sequence

1. Complete the [Publication Security Checklist](./SECURITY_PUBLICATION_CHECKLIST.md).
2. Run `pnpm run check` and inspect the real UI in light and dark themes.
3. Verify the Codex MCP context-read and progress-write flow from a clean clone.
4. Open a focused release pull request so CI and the final diff are public and reviewable.
5. Merge only after the release candidate is accepted.
6. Create a signed or annotated release tag and publish accurate release notes.
7. Add the repository About text, topics, social preview, and documentation links.
8. Publish a short launch post that shows the problem, current working path, limitations, and invitation to contribute.
9. Respond to issues and document decisions; maintenance activity is more credible than promotional claims.

## Release notes and long-term maintenance

Every release should include:

- the user-visible result;
- the exact current Codex or MCP capability added;
- security or migration impact;
- verification performed;
- known limitations;
- rollback or compatibility notes when relevant;
- the next accepted vertical slice.

Use the roadmap to communicate direction without promising dates or calling incomplete work fully compatible. A truthful next milestone can say:

> Next: deepen Codex-native workflows with additional scoped, auditable tools, one reviewed vertical slice at a time.

Keep `CHANGELOG.md`, GitHub Releases, the roadmap, and the README current. Mark abandoned or superseded plans rather than leaving contradictory status claims.

## Metrics worth reporting

Report only measurements that can be checked:

- GitHub stars, forks, releases, contributors, issues, and pull requests as of a stated date;
- CI status and tested runtime versions;
- release cadence and time to respond to security reports;
- MCP acceptance-test results;
- documented third-party usage only with permission and evidence.

Never present maintainer token usage, private project counts, or unverified deployments as public adoption.

## Application and outreach integrity

When applying to an open-source program or contacting maintainers:

- use the public repository URL and the identity that controls it;
- state whether you are the primary or a core maintainer accurately;
- give dated GitHub metrics rather than rounded or projected numbers;
- describe only the released functionality;
- explain how any credits would support public maintenance workflows;
- disclose limitations directly;
- never submit confidential data or private credentials.

Trust is the growth strategy. A smaller accurate claim with reproducible evidence is more durable than a larger claim that reviewers cannot verify.
