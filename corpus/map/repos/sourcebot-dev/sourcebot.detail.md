# sourcebot-dev/sourcebot -- full detail

[Back to orientation](sourcebot.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/sourcebot-dev/sourcebot/c0d0df91a6b962234263dac6a6b3ebc500ae7fb0/cedbf25d27012bb1.json](../../../wiki/dossiers/sourcebot-dev/sourcebot/c0d0df91a6b962234263dac6a6b3ebc500ae7fb0/cedbf25d27012bb1.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (3 claim(s))

- [observation/documented] Sourcebot ships as a single Docker container running multiple services under supervisord, including a Next.js web server, a Node.js backend worker, Zoekt, Postgres, and a Redis job queue used with BullMQ. -- evidence: [docs/docs/misc/architecture.mdx#L11-L17](https://github.com/sourcebot-dev/sourcebot/blob/c0d0df91a6b962234263dac6a6b3ebc500ae7fb0/docs/docs/misc/architecture.mdx#L11-L17), [docs/docs/misc/architecture.mdx#L5-L5](https://github.com/sourcebot-dev/sourcebot/blob/c0d0df91a6b962234263dac6a6b3ebc500ae7fb0/docs/docs/misc/architecture.mdx#L5-L5) (`clm_ba17d2a74b1da070ec8360db1bc4fd0f4148d9f60c613f9e82a33e72cafbf119`)
- [observation/documented] The backend worker incrementally syncs with code hosts such as GitHub and GitLab and asynchronously indexes configured repositories; Zoekt is the trigram indexing search engine powering Sourcebot. -- evidence: [docs/docs/misc/architecture.mdx#L11-L17](https://github.com/sourcebot-dev/sourcebot/blob/c0d0df91a6b962234263dac6a6b3ebc500ae7fb0/docs/docs/misc/architecture.mdx#L11-L17) (`clm_635fbf9564f50329643ec3cd0a2e82da528441ed8ad4ab924b9d327b263a0a5e`)
- [observation/documented] A `.sourcebot/` file-system cache stores persistent data, and managed Redis/Postgres can run outside the container via the REDIS_URL and DATABASE_URL environment variables. -- evidence: [docs/docs/misc/architecture.mdx#L11-L17](https://github.com/sourcebot-dev/sourcebot/blob/c0d0df91a6b962234263dac6a6b3ebc500ae7fb0/docs/docs/misc/architecture.mdx#L11-L17), [docs/docs/misc/architecture.mdx#L19-L19](https://github.com/sourcebot-dev/sourcebot/blob/c0d0df91a6b962234263dac6a6b3ebc500ae7fb0/docs/docs/misc/architecture.mdx#L19-L19) (`clm_e1e152ff8b87012459d303f8a81c321258a9c8460fcba834bf2c892fe78477d9`)

## design-choices (2 claim(s))

- [observation/documented] Sourcebot collects anonymous usage data by default; this can be disabled by setting the SOURCEBOT_TELEMETRY_DISABLED environment variable to true. -- evidence: [README.md#L110-L112](https://github.com/sourcebot-dev/sourcebot/blob/c0d0df91a6b962234263dac6a6b3ebc500ae7fb0/README.md#L110-L112) (`clm_a2d889e660e5a8c3d6d03fb2de84ebeeb6de7b6bc654467b3225f0b7d0536ae2`)
- [observation/documented] Paid subscriptions activate by default via an Activation Code requiring periodic service pings; deployments failing to ping for 7 days downgrade to the free plan, and offline License Key activation is available on request via SOURCEBOT_EE_LICENSE_KEY. -- evidence: [docs/docs/activating-a-subscription.mdx#L24-L24](https://github.com/sourcebot-dev/sourcebot/blob/c0d0df91a6b962234263dac6a6b3ebc500ae7fb0/docs/docs/activating-a-subscription.mdx#L24-L24), [docs/docs/activating-a-subscription.mdx#L22-L22](https://github.com/sourcebot-dev/sourcebot/blob/c0d0df91a6b962234263dac6a6b3ebc500ae7fb0/docs/docs/activating-a-subscription.mdx#L22-L22), [docs/docs/activating-a-subscription.mdx#L10-L10](https://github.com/sourcebot-dev/sourcebot/blob/c0d0df91a6b962234263dac6a6b3ebc500ae7fb0/docs/docs/activating-a-subscription.mdx#L10-L10), [docs/docs/activating-a-subscription.mdx#L12-L13](https://github.com/sourcebot-dev/sourcebot/blob/c0d0df91a6b962234263dac6a6b3ebc500ae7fb0/docs/docs/activating-a-subscription.mdx#L12-L13) (`clm_b56f1a275c7b156c416a124e6cf338aceec4ede0b834559e0da6f60c94f22511`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: docs previewing uses the Mintlify CLI (npm i -g mintlify, then mintlify dev in the folder containing docs.json), and building Sourcebot from source for contribution is described in CONTRIBUTING.md. -- evidence: [docs/README.md#L31-L32](https://github.com/sourcebot-dev/sourcebot/blob/c0d0df91a6b962234263dac6a6b3ebc500ae7fb0/docs/README.md#L31-L32), [README.md#L115-L116](https://github.com/sourcebot-dev/sourcebot/blob/c0d0df91a6b962234263dac6a6b3ebc500ae7fb0/README.md#L115-L116), [docs/README.md#L21-L23](https://github.com/sourcebot-dev/sourcebot/blob/c0d0df91a6b962234263dac6a6b3ebc500ae7fb0/docs/README.md#L21-L23), [docs/README.md#L15-L17](https://github.com/sourcebot-dev/sourcebot/blob/c0d0df91a6b962234263dac6a6b3ebc500ae7fb0/docs/README.md#L15-L17), [docs/README.md#L13-L13](https://github.com/sourcebot-dev/sourcebot/blob/c0d0df91a6b962234263dac6a6b3ebc500ae7fb0/docs/README.md#L13-L13), [README.md#L118-L118](https://github.com/sourcebot-dev/sourcebot/blob/c0d0df91a6b962234263dac6a6b3ebc500ae7fb0/README.md#L118-L118) (`clm_c251b59b2e9868eefd9ac0888864c2634c58d6c866e2c7d0773b5472255c10d3`)

## skills-patterns (3 claim(s))

- [observation/documented] Skills are reusable context for Ask Sourcebot with four fields (name, command, description, instructions), invoked via slash commands like /deep-research, and can be personal or shared within a workspace. -- evidence: [docs/docs/features/ask/skills.mdx#L59-L60](https://github.com/sourcebot-dev/sourcebot/blob/c0d0df91a6b962234263dac6a6b3ebc500ae7fb0/docs/docs/features/ask/skills.mdx#L59-L60), [docs/docs/features/ask/skills.mdx#L57-L57](https://github.com/sourcebot-dev/sourcebot/blob/c0d0df91a6b962234263dac6a6b3ebc500ae7fb0/docs/docs/features/ask/skills.mdx#L57-L57), [docs/docs/features/ask/skills.mdx#L5-L6](https://github.com/sourcebot-dev/sourcebot/blob/c0d0df91a6b962234263dac6a6b3ebc500ae7fb0/docs/docs/features/ask/skills.mdx#L5-L6), [docs/docs/features/ask/skills.mdx#L24-L27](https://github.com/sourcebot-dev/sourcebot/blob/c0d0df91a6b962234263dac6a6b3ebc500ae7fb0/docs/docs/features/ask/skills.mdx#L24-L27) (`clm_cd3e569a8fef081afb7aa44f7e2d2ac9e95656dd5b9ebc95947aed1cc397c2c5`)
- [observation/documented] Skills can be created directly, imported from local .md/.markdown files (front matter prefills name, command, description), or imported from an indexed repository and kept synced to that file. -- evidence: [docs/docs/features/ask/skills.mdx#L74-L74](https://github.com/sourcebot-dev/sourcebot/blob/c0d0df91a6b962234263dac6a6b3ebc500ae7fb0/docs/docs/features/ask/skills.mdx#L74-L74), [docs/docs/features/ask/skills.mdx#L92-L92](https://github.com/sourcebot-dev/sourcebot/blob/c0d0df91a6b962234263dac6a6b3ebc500ae7fb0/docs/docs/features/ask/skills.mdx#L92-L92), [docs/docs/features/ask/skills.mdx#L18-L20](https://github.com/sourcebot-dev/sourcebot/blob/c0d0df91a6b962234263dac6a6b3ebc500ae7fb0/docs/docs/features/ask/skills.mdx#L18-L20) (`clm_ec2ee541c08154080dd6a44af122f3f84eaac9525ef27e16ad7e8b8607aa83c6`)
- [observation/documented] Synced skills are shown only to users who can access the source repository, and sharing one warns before publishing when repository permission syncing is enabled. -- evidence: [docs/docs/features/ask/skills.mdx#L109-L109](https://github.com/sourcebot-dev/sourcebot/blob/c0d0df91a6b962234263dac6a6b3ebc500ae7fb0/docs/docs/features/ask/skills.mdx#L109-L109), [docs/docs/features/ask/skills.mdx#L111-L111](https://github.com/sourcebot-dev/sourcebot/blob/c0d0df91a6b962234263dac6a6b3ebc500ae7fb0/docs/docs/features/ask/skills.mdx#L111-L111) (`clm_682f0cb823cf1f791bfffd2e73a5318e9ef3867784ea8b14556697d1fbe7659f`)

## interfaces (2 claim(s))

- [observation/documented] Sourcebot is configured through a JSON config file (with a schema and comment support) that defines connections, which repositories to index, language model providers, and auth providers. -- evidence: [README.md#L82-L98](https://github.com/sourcebot-dev/sourcebot/blob/c0d0df91a6b962234263dac6a6b3ebc500ae7fb0/README.md#L82-L98) (`clm_68698d2f00d264be4b7298b62bd4d4005fba6438a841674a17cb9afa965c8fc3`)
- [observation/documented] After deployment via docker compose, the product is accessed at http://localhost:3000. -- evidence: [README.md#L100-L103](https://github.com/sourcebot-dev/sourcebot/blob/c0d0df91a6b962234263dac6a6b3ebc500ae7fb0/README.md#L100-L103), [README.md#L105-L106](https://github.com/sourcebot-dev/sourcebot/blob/c0d0df91a6b962234263dac6a6b3ebc500ae7fb0/README.md#L105-L106) (`clm_93320c74f21cb81d44c89b1cb83313b63b7278409e5c59b429ee5bd76705c92b`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The product depends on Zoekt (Sourcegraph's open-source trigram search engine), Postgres, Redis with BullMQ, and supervisord within its container. -- evidence: [docs/docs/misc/architecture.mdx#L11-L17](https://github.com/sourcebot-dev/sourcebot/blob/c0d0df91a6b962234263dac6a6b3ebc500ae7fb0/docs/docs/misc/architecture.mdx#L11-L17), [docs/docs/misc/architecture.mdx#L5-L5](https://github.com/sourcebot-dev/sourcebot/blob/c0d0df91a6b962234263dac6a6b3ebc500ae7fb0/docs/docs/misc/architecture.mdx#L5-L5) (`clm_48f97af79ce101c738b634bb6bf4cf59c00ffe056ed237866765fd8cca45eb82`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

