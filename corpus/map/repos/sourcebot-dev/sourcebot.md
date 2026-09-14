# sourcebot-dev/sourcebot

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit c0d0df91a6b9 @ cedbf25d27012bb1

## Summary (orientation draft, not independently verified)

Evidence shows Sourcebot is a self-hosted code-understanding tool (README) shipped as a single Docker container running a Next.js web server, Node.js backend worker, Zoekt, Postgres, and a Redis/BullMQ job queue under supervisord, with a JSON config file, skills for Ask Sourcebot, telemetry, and subscription licensing; docs preview uses the Mintlify CLI.

## Source coverage

Source coverage (partial): 6 of 87 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (3 claim(s)):
  - [observation/documented] Sourcebot ships as a single Docker container running multiple services under supervisord, including a Next.js web server, a Node.js backend worker, Zoekt, Postgres, and a Redis job queue used with BullMQ. -- evidence: [docs/docs/misc/architecture.mdx#L11-L17](https://github.com/sourcebot-dev/sourcebot/blob/c0d0df91a6b962234263dac6a6b3ebc500ae7fb0/docs/docs/misc/architecture.mdx#L11-L17), [docs/docs/misc/architecture.mdx#L5-L5](https://github.com/sourcebot-dev/sourcebot/blob/c0d0df91a6b962234263dac6a6b3ebc500ae7fb0/docs/docs/misc/architecture.mdx#L5-L5)
  - [observation/documented] The backend worker incrementally syncs with code hosts such as GitHub and GitLab and asynchronously indexes configured repositories; Zoekt is the trigram indexing search engine powering Sourcebot. -- evidence: [docs/docs/misc/architecture.mdx#L11-L17](https://github.com/sourcebot-dev/sourcebot/blob/c0d0df91a6b962234263dac6a6b3ebc500ae7fb0/docs/docs/misc/architecture.mdx#L11-L17)
- design-choices (2 claim(s)):
  - [observation/documented] Sourcebot collects anonymous usage data by default; this can be disabled by setting the SOURCEBOT_TELEMETRY_DISABLED environment variable to true. -- evidence: [README.md#L110-L112](https://github.com/sourcebot-dev/sourcebot/blob/c0d0df91a6b962234263dac6a6b3ebc500ae7fb0/README.md#L110-L112)
  - [observation/documented] Paid subscriptions activate by default via an Activation Code requiring periodic service pings; deployments failing to ping for 7 days downgrade to the free plan, and offline License Key activation is available on request via SOURCEBOT_EE_LICENSE_KEY. -- evidence: [docs/docs/activating-a-subscription.mdx#L24-L24](https://github.com/sourcebot-dev/sourcebot/blob/c0d0df91a6b962234263dac6a6b3ebc500ae7fb0/docs/docs/activating-a-subscription.mdx#L24-L24), [docs/docs/activating-a-subscription.mdx#L22-L22](https://github.com/sourcebot-dev/sourcebot/blob/c0d0df91a6b962234263dac6a6b3ebc500ae7fb0/docs/docs/activating-a-subscription.mdx#L22-L22), [docs/docs/activating-a-subscription.mdx#L10-L10](https://github.com/sourcebot-dev/sourcebot/blob/c0d0df91a6b962234263dac6a6b3ebc500ae7fb0/docs/docs/activating-a-subscription.mdx#L10-L10), [docs/docs/activating-a-subscription.mdx#L12-L13](https://github.com/sourcebot-dev/sourcebot/blob/c0d0df91a6b962234263dac6a6b3ebc500ae7fb0/docs/docs/activating-a-subscription.mdx#L12-L13)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: docs previewing uses the Mintlify CLI (npm i -g mintlify, then mintlify dev in the folder containing docs.json), and building Sourcebot from source for contribution is described in CONTRIBUTING.md. -- evidence: [docs/README.md#L31-L32](https://github.com/sourcebot-dev/sourcebot/blob/c0d0df91a6b962234263dac6a6b3ebc500ae7fb0/docs/README.md#L31-L32), [README.md#L115-L116](https://github.com/sourcebot-dev/sourcebot/blob/c0d0df91a6b962234263dac6a6b3ebc500ae7fb0/README.md#L115-L116), [docs/README.md#L21-L23](https://github.com/sourcebot-dev/sourcebot/blob/c0d0df91a6b962234263dac6a6b3ebc500ae7fb0/docs/README.md#L21-L23), [docs/README.md#L15-L17](https://github.com/sourcebot-dev/sourcebot/blob/c0d0df91a6b962234263dac6a6b3ebc500ae7fb0/docs/README.md#L15-L17), [docs/README.md#L13-L13](https://github.com/sourcebot-dev/sourcebot/blob/c0d0df91a6b962234263dac6a6b3ebc500ae7fb0/docs/README.md#L13-L13), [README.md#L118-L118](https://github.com/sourcebot-dev/sourcebot/blob/c0d0df91a6b962234263dac6a6b3ebc500ae7fb0/README.md#L118-L118)
- skills-patterns (3 claim(s)):
  - [observation/documented] Skills are reusable context for Ask Sourcebot with four fields (name, command, description, instructions), invoked via slash commands like /deep-research, and can be personal or shared within a workspace. -- evidence: [docs/docs/features/ask/skills.mdx#L59-L60](https://github.com/sourcebot-dev/sourcebot/blob/c0d0df91a6b962234263dac6a6b3ebc500ae7fb0/docs/docs/features/ask/skills.mdx#L59-L60), [docs/docs/features/ask/skills.mdx#L57-L57](https://github.com/sourcebot-dev/sourcebot/blob/c0d0df91a6b962234263dac6a6b3ebc500ae7fb0/docs/docs/features/ask/skills.mdx#L57-L57), [docs/docs/features/ask/skills.mdx#L5-L6](https://github.com/sourcebot-dev/sourcebot/blob/c0d0df91a6b962234263dac6a6b3ebc500ae7fb0/docs/docs/features/ask/skills.mdx#L5-L6), [docs/docs/features/ask/skills.mdx#L24-L27](https://github.com/sourcebot-dev/sourcebot/blob/c0d0df91a6b962234263dac6a6b3ebc500ae7fb0/docs/docs/features/ask/skills.mdx#L24-L27)
  - [observation/documented] Skills can be created directly, imported from local .md/.markdown files (front matter prefills name, command, description), or imported from an indexed repository and kept synced to that file. -- evidence: [docs/docs/features/ask/skills.mdx#L74-L74](https://github.com/sourcebot-dev/sourcebot/blob/c0d0df91a6b962234263dac6a6b3ebc500ae7fb0/docs/docs/features/ask/skills.mdx#L74-L74), [docs/docs/features/ask/skills.mdx#L92-L92](https://github.com/sourcebot-dev/sourcebot/blob/c0d0df91a6b962234263dac6a6b3ebc500ae7fb0/docs/docs/features/ask/skills.mdx#L92-L92), [docs/docs/features/ask/skills.mdx#L18-L20](https://github.com/sourcebot-dev/sourcebot/blob/c0d0df91a6b962234263dac6a6b3ebc500ae7fb0/docs/docs/features/ask/skills.mdx#L18-L20)
- interfaces (2 claim(s)):
  - [observation/documented] Sourcebot is configured through a JSON config file (with a schema and comment support) that defines connections, which repositories to index, language model providers, and auth providers. -- evidence: [README.md#L82-L98](https://github.com/sourcebot-dev/sourcebot/blob/c0d0df91a6b962234263dac6a6b3ebc500ae7fb0/README.md#L82-L98)
  - [observation/documented] After deployment via docker compose, the product is accessed at http://localhost:3000. -- evidence: [README.md#L100-L103](https://github.com/sourcebot-dev/sourcebot/blob/c0d0df91a6b962234263dac6a6b3ebc500ae7fb0/README.md#L100-L103), [README.md#L105-L106](https://github.com/sourcebot-dev/sourcebot/blob/c0d0df91a6b962234263dac6a6b3ebc500ae7fb0/README.md#L105-L106)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
More evidence: [full detail](sourcebot.detail.md)

Metadata and full claim list: [full detail](sourcebot.detail.md)
Human notes ([notes](sourcebot.notes.md), never overwritten by build)

[Back to map index](../../index.md)
