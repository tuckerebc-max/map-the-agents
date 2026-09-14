---
access: public
aliases: []
claim_ids:
- clm_01e71e4702e758b7dd80fe6444df948dfd3328bdbedb69d063be5ce806e68f0f
- clm_2538c1f14f81963df1c6c74aff14b0b6a90b2f10dc8d72062f97a4d27f77b3c1
- clm_2bc710bfd8367bb2936d2771ddc6cdce02d4d7a3cefbb4a8b731d51b42aaec53
- clm_2c27258808a9bf7e8a25448ed04c259033351a8e07f1d5c350ca42ae17e05d91
- clm_3c90c5c84ce8c5f8eef9495f403e41791993ecae8ea3521ce0f9610ae4052814
- clm_599bedf9da939d82beae33cb7158bdb8e6372a56abf5a30df5bda5f52a81afbb
- clm_612d0227e64f675cf51e48639a2ea475fada7ea45e3571d15ed8ab995fac05bb
- clm_75b2cac5faae10fe7601fc8c391ac8ea9a2934aee8b4693462ca61ae78e18e7a
- clm_903824559fd500c4aed7b7b4502c7ffbaf489ba004242c7225686ef040c5d4dd
- clm_cde2a48ea961707f7a249875a300d97a161baa13e8039a78159ab983653e3966
- clm_d2e035e901de65d314f66e3326889be2e9d24599a5816b1d786de0ade2291daf
- clm_e5c3e82993e4837617736ee602b7eb73de200f7bd51d6931972ca1e57571bd8f
maturity: draft
page_id: pg_a26c0a577d025a8eb70e31e492cdcd85
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_1d8d43e93e3851a2a268e9d1d76356b3
title: Renaissance-Innovation-Labs/jacob-ai/README.md @ bd0e26461466
updated_at: '2026-09-14T02:35:03Z'
---

# Renaissance-Innovation-Labs/jacob-ai/README.md @ bd0e26461466

<!-- rcw:begin owner=source:src_1d8d43e93e3851a2a268e9d1d76356b3 block=evidence -->
- JACoB (Just Another Coding Bot) is an open-source AI tool that automates coding tasks, converts Figma designs into deployable code, and integrates into existing developer workflows. [@claim:clm_01e71e4702e758b7dd80fe6444df948dfd3328bdbedb69d063be5ce806e68f0f]
- The product is delivered as a custom GitHub app, a Figma plugin, and a command-line tool for setting configuration options. [@claim:clm_2538c1f14f81963df1c6c74aff14b0b6a90b2f10dc8d72062f97a4d27f77b3c1]
- The codebase is built with Next.js, NextAuth.js, Tailwind CSS, tRPC, and Orchid ORM. [@claim:clm_2bc710bfd8367bb2936d2771ddc6cdce02d4d7a3cefbb4a8b731d51b42aaec53]
- The local version does not store the codebase; hosted logs with code snippets are retained 14 days, GitHub app tokens expire after 8 hours and are not saved in the database. [@claim:clm_2c27258808a9bf7e8a25448ed04c259033351a8e07f1d5c350ca42ae17e05d91]
- Repository development practice: local setup involves creating .env from .env.example, running docker compose, npm install, npm run db create/migrate, verifying with npm test, and launching with npm run dev. [@claim:clm_3c90c5c84ce8c5f8eef9495f403e41791993ecae8ea3521ce0f9610ae4052814]
- Per-project behavior is configured via a jacob.config file generated with 'npx jacob-setup create', specifying project details and build environment variables. [@claim:clm_599bedf9da939d82beae33cb7158bdb8e6372a56abf5a30df5bda5f52a81afbb]
- Local infrastructure runs RabbitMQ and Postgres via Docker Compose, and GitHub webhooks are proxied to the local server through smee.io. [@claim:clm_612d0227e64f675cf51e48639a2ea475fada7ea45e3571d15ed8ab995fac05bb]
- The team evaluated JACoB via the JACoB Arena, where developers compared it against top design-to-code tools and human benchmarks, reportedly outperforming seven such tools. [@claim:clm_75b2cac5faae10fe7601fc8c391ac8ea9a2934aee8b4693462ca61ae78e18e7a]
- Self-hosting requires GitHub and Figma accounts, Node.js, Docker and Docker Compose, an OpenAI account, and a PortKey account. [@claim:clm_903824559fd500c4aed7b7b4502c7ffbaf489ba004242c7225686ef040c5d4dd]
- Due to context window and model constraints, JACoB targets smaller tasks and currently works best with TypeScript/JavaScript, Next.js, Tailwind, and Figma designs. [@claim:clm_cde2a48ea961707f7a249875a300d97a161baa13e8039a78159ab983653e3966]
- The GitHub app is configured with read/write permissions for issues, pull requests, and contents, and subscribes to issue, comment, and pull-request webhook events. [@claim:clm_d2e035e901de65d314f66e3326889be2e9d24599a5816b1d786de0ade2291daf]
- Repository development practice: the README describes using GitHub's webhook redeliver feature to replay events against the local instance for debugging and iteration. [@claim:clm_e5c3e82993e4837617736ee602b7eb73de200f7bd51d6931972ca1e57571bd8f]
<!-- rcw:end owner=source:src_1d8d43e93e3851a2a268e9d1d76356b3 block=evidence -->

## Researcher notes

