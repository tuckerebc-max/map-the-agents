---
access: public
aliases: []
claim_ids:
- clm_268fa60143b4e9deb04a145622a3f2e61dde914be20d16d007fda4c47fa92cff
- clm_77710d899fdccae6207da39f19fbeb307462896b6b5aafb612a49c4a89ca939d
- clm_9be7ae9c62ec7cf80a116e03fa39b0691304a6c4bc55a753bf1885b8884afb39
- clm_9f47cfeb9ba25e69371a41a477e70c85c55351d62d75b01d9e20a4ae598d4126
- clm_a66169c6735c64d625bfcc66d3c2af4c6fc85dc313cbf2fc1eb94a82120524d6
- clm_af3e6a0b6e84ccc9de090eb958405c7395e59ddf0000400fdaf20281c5eb503e
- clm_b75a5618cf4e209f2bebc0f44ba8868fe6e714c40d1f93dd87cdcdf77e9fcb32
- clm_e9b9f7552a2ec2507f84366960cf6d977dbdfe73deb2dd863905f2b420dea60d
maturity: draft
page_id: pg_e46801d0cfd650ff858bc1e6bd8ce6de
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_429f822567d35259b1c6730bfe03ca2c
title: InsForge/InsForge/README.md @ fca20f318722
updated_at: '2026-09-14T03:58:31Z'
---

# InsForge/InsForge/README.md @ fca20f318722

<!-- rcw:begin owner=source:src_429f822567d35259b1c6730bfe03ca2c block=evidence -->
- The project is licensed under Apache License 2.0, while the public InsForge skills plugin is MIT-licensed. [@claim:clm_268fa60143b4e9deb04a145622a3f2e61dde914be20d16d007fda4c47fa92cff]
- Multiple isolated instances are supported by giving each project its own directory, COMPOSE_PROJECT_NAME, and ports; directories sharing a project name share containers, while distinct names yield separate containers, volumes, databases, and secrets. [@claim:clm_77710d899fdccae6207da39f19fbeb307462896b6b5aafb612a49c4a89ca939d]
- InsForge is described as an all-in-one, open-source backend platform for agentic coding, giving coding agents database, auth, storage, compute, hosting, and an AI gateway. [@claim:clm_9be7ae9c62ec7cf80a116e03fa39b0691304a6c4bc55a753bf1885b8884afb39]
- Storage defaults to the local filesystem; S3-compatible backing storage enables an S3 gateway at /storage/v1/s3, with bundled MinIO or RustFS compose overlays or bring-your-own S3 settings (S3_BUCKET, S3_REGION, keys, optional endpoint and presigned-URL mode). [@claim:clm_9f47cfeb9ba25e69371a41a477e70c85c55351d62d75b01d9e20a4ae598d4126]
- Core products include authentication, Postgres database, S3-compatible storage, an OpenAI-compatible model gateway, edge functions, compute (private preview), and site deployment. [@claim:clm_a66169c6735c64d625bfcc66d3c2af4c6fc85dc313cbf2fc1eb94a82120524d6]
- Through its interfaces agents can read backend context (docs, schemas, metadata such as deployed functions, bucket contents, auth config, and runtime logs) and configure primitives like edge functions, migrations, buckets, and auth providers. [@claim:clm_af3e6a0b6e84ccc9de090eb958405c7395e59ddf0000400fdaf20281c5eb503e]
- Coding agents interact with InsForge through two interfaces: an MCP server (self-hosted and cloud) exposing operations as tools, and a cloud-only CLI paired with Skills invoked from the terminal. [@claim:clm_b75a5618cf4e209f2bebc0f44ba8868fe6e714c40d1f93dd87cdcdf77e9fcb32]
- Self-hosting via Docker Compose requires Docker with Compose v2; a setup script generates secrets including JWT_SECRET, ENCRYPTION_KEY, POSTGRES_PASSWORD, ROOT_ADMIN_PASSWORD, and access keys into ~/insforge/.env (mode 600) without starting anything. [@claim:clm_e9b9f7552a2ec2507f84366960cf6d977dbdfe73deb2dd863905f2b420dea60d]
<!-- rcw:end owner=source:src_429f822567d35259b1c6730bfe03ca2c block=evidence -->

## Researcher notes

