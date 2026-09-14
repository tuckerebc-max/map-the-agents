# renaissance-innovation-labs/jacob-ai

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit bd0e26461466 @ b95445b127d3ee29

## Summary (orientation draft, not independently verified)

The evidence is README-only documentation for JACoB, an open-source AI coding bot that integrates with GitHub and Figma to convert designs into code and open PRs. It covers product description, self-hosted setup steps, privacy details, and stated limitations, but no source code.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 10 facet(s); 3 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] JACoB (Just Another Coding Bot) is an open-source AI tool that automates coding tasks, converts Figma designs into deployable code, and integrates into existing developer workflows. -- evidence: [README.md#L27-L27](https://github.com/Renaissance-Innovation-Labs/jacob-ai/blob/bd0e26461466991aee873f74896f4902387b9f47/README.md#L27-L27)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (1 claim(s)):
  - [observation/documented] Per-project behavior is configured via a jacob.config file generated with 'npx jacob-setup create', specifying project details and build environment variables. -- evidence: [README.md#L163-L165](https://github.com/Renaissance-Innovation-Labs/jacob-ai/blob/bd0e26461466991aee873f74896f4902387b9f47/README.md#L163-L165)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: local setup involves creating .env from .env.example, running docker compose, npm install, npm run db create/migrate, verifying with npm test, and launching with npm run dev. -- evidence: [README.md#L176-L185](https://github.com/Renaissance-Innovation-Labs/jacob-ai/blob/bd0e26461466991aee873f74896f4902387b9f47/README.md#L176-L185), [README.md#L189-L189](https://github.com/Renaissance-Innovation-Labs/jacob-ai/blob/bd0e26461466991aee873f74896f4902387b9f47/README.md#L189-L189), [README.md#L199-L201](https://github.com/Renaissance-Innovation-Labs/jacob-ai/blob/bd0e26461466991aee873f74896f4902387b9f47/README.md#L199-L201), [README.md#L193-L193](https://github.com/Renaissance-Innovation-Labs/jacob-ai/blob/bd0e26461466991aee873f74896f4902387b9f47/README.md#L193-L193), [README.md#L197-L197](https://github.com/Renaissance-Innovation-Labs/jacob-ai/blob/bd0e26461466991aee873f74896f4902387b9f47/README.md#L197-L197)
  - [observation/documented] Repository development practice: the README describes using GitHub's webhook redeliver feature to replay events against the local instance for debugging and iteration. -- evidence: [README.md#L223-L223](https://github.com/Renaissance-Innovation-Labs/jacob-ai/blob/bd0e26461466991aee873f74896f4902387b9f47/README.md#L223-L223), [README.md#L229-L229](https://github.com/Renaissance-Innovation-Labs/jacob-ai/blob/bd0e26461466991aee873f74896f4902387b9f47/README.md#L229-L229)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] The product is delivered as a custom GitHub app, a Figma plugin, and a command-line tool for setting configuration options. -- evidence: [README.md#L115-L115](https://github.com/Renaissance-Innovation-Labs/jacob-ai/blob/bd0e26461466991aee873f74896f4902387b9f47/README.md#L115-L115)
- memory-state (1 claim(s)):
  - [observation/documented] The local version does not store the codebase; hosted logs with code snippets are retained 14 days, GitHub app tokens expire after 8 hours and are not saved in the database. -- evidence: [README.md#L111-L111](https://github.com/Renaissance-Innovation-Labs/jacob-ai/blob/bd0e26461466991aee873f74896f4902387b9f47/README.md#L111-L111)
- orchestration (1 claim(s)):
  - [observation/documented] Local infrastructure runs RabbitMQ and Postgres via Docker Compose, and GitHub webhooks are proxied to the local server through smee.io. -- evidence: [README.md#L189-L189](https://github.com/Renaissance-Innovation-Labs/jacob-ai/blob/bd0e26461466991aee873f74896f4902387b9f47/README.md#L189-L189), [README.md#L159-L159](https://github.com/Renaissance-Innovation-Labs/jacob-ai/blob/bd0e26461466991aee873f74896f4902387b9f47/README.md#L159-L159)
- tools-permissions (1 claim(s)):
  - [observation/documented] The GitHub app is configured with read/write permissions for issues, pull requests, and contents, and subscribes to issue, comment, and pull-request webhook events. -- evidence: [README.md#L137-L155](https://github.com/Renaissance-Innovation-Labs/jacob-ai/blob/bd0e26461466991aee873f74896f4902387b9f47/README.md#L137-L155)
- evaluation (1 claim(s)):
  - [observation/documented] The team evaluated JACoB via the JACoB Arena, where developers compared it against top design-to-code tools and human benchmarks, reportedly outperforming seven such tools. -- evidence: [README.md#L72-L72](https://github.com/Renaissance-Innovation-Labs/jacob-ai/blob/bd0e26461466991aee873f74896f4902387b9f47/README.md#L72-L72)
- dependencies (2 claim(s)):
  - [observation/documented] The codebase is built with Next.js, NextAuth.js, Tailwind CSS, tRPC, and Orchid ORM. -- evidence: [README.md#L119-L123](https://github.com/Renaissance-Innovation-Labs/jacob-ai/blob/bd0e26461466991aee873f74896f4902387b9f47/README.md#L119-L123)
  - [observation/documented] Self-hosting requires GitHub and Figma accounts, Node.js, Docker and Docker Compose, an OpenAI account, and a PortKey account. -- evidence: [README.md#L127-L131](https://github.com/Renaissance-Innovation-Labs/jacob-ai/blob/bd0e26461466991aee873f74896f4902387b9f47/README.md#L127-L131)
More evidence: [full detail](jacob-ai.detail.md)

Metadata and full claim list: [full detail](jacob-ai.detail.md)
Human notes ([notes](jacob-ai.notes.md), never overwritten by build)

[Back to map index](../../index.md)
