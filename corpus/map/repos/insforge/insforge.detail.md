# insforge/insforge -- full detail

[Back to orientation](insforge.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/insforge/insforge/fca20f318722c1fa89371e94878ba08b114c73b7/4305e1ce136d7730.json](../../../wiki/dossiers/insforge/insforge/fca20f318722c1fa89371e94878ba08b114c73b7/4305e1ce136d7730.json)

## specifications (1 claim(s))

- [observation/documented] InsForge is described as an all-in-one, open-source backend platform for agentic coding, giving coding agents database, auth, storage, compute, hosting, and an AI gateway. -- evidence: [README.md#L42-L42](https://github.com/InsForge/InsForge/blob/fca20f318722c1fa89371e94878ba08b114c73b7/README.md#L42-L42) (`clm_9be7ae9c62ec7cf80a116e03fa39b0691304a6c4bc55a753bf1885b8884afb39`)

## components (1 claim(s))

- [observation/documented] Core products include authentication, Postgres database, S3-compatible storage, an OpenAI-compatible model gateway, edge functions, compute (private preview), and site deployment. -- evidence: [README.md#L92-L98](https://github.com/InsForge/InsForge/blob/fca20f318722c1fa89371e94878ba08b114c73b7/README.md#L92-L98) (`clm_a66169c6735c64d625bfcc66d3c2af4c6fc85dc313cbf2fc1eb94a82120524d6`)

## design-choices (2 claim(s))

- [observation/documented] The MCP server and CLI expose infrastructure as structured, machine-readable context so AI coding agents can plan and execute operations autonomously within scoped permissions. -- evidence: [docs/alternatives.mdx#L11-L15](https://github.com/InsForge/InsForge/blob/fca20f318722c1fa89371e94878ba08b114c73b7/docs/alternatives.mdx#L11-L15) (`clm_a5874fc9623ba53d553a62dcd8cf353b45dc57071eb322eb85f75e1978c7a36f`)
- [observation/documented] Storage defaults to the local filesystem; S3-compatible backing storage enables an S3 gateway at /storage/v1/s3, with bundled MinIO or RustFS compose overlays or bring-your-own S3 settings (S3_BUCKET, S3_REGION, keys, optional endpoint and presigned-URL mode). -- evidence: [README.md#L240-L240](https://github.com/InsForge/InsForge/blob/fca20f318722c1fa89371e94878ba08b114c73b7/README.md#L240-L240), [README.md#L233-L234](https://github.com/InsForge/InsForge/blob/fca20f318722c1fa89371e94878ba08b114c73b7/README.md#L233-L234), [README.md#L251-L251](https://github.com/InsForge/InsForge/blob/fca20f318722c1fa89371e94878ba08b114c73b7/README.md#L251-L251), [README.md#L231-L231](https://github.com/InsForge/InsForge/blob/fca20f318722c1fa89371e94878ba08b114c73b7/README.md#L231-L231) (`clm_9f47cfeb9ba25e69371a41a477e70c85c55351d62d75b01d9e20a4ae598d4126`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: docs/asset-guidelines.md instructs contributors to review and optimize documentation media before committing, with a PR checklist and recommended tools (FFmpeg, pngquant, jpegoptim, SVGO). -- evidence: [docs/asset-guidelines.md#L77-L80](https://github.com/InsForge/InsForge/blob/fca20f318722c1fa89371e94878ba08b114c73b7/docs/asset-guidelines.md#L77-L80), [docs/asset-guidelines.md#L3-L3](https://github.com/InsForge/InsForge/blob/fca20f318722c1fa89371e94878ba08b114c73b7/docs/asset-guidelines.md#L3-L3), [docs/asset-guidelines.md#L68-L73](https://github.com/InsForge/InsForge/blob/fca20f318722c1fa89371e94878ba08b114c73b7/docs/asset-guidelines.md#L68-L73) (`clm_38afe73055d6ed8e4fb0e2cb16e8a2f7ae324c4289896a46f041d49c75031588`)
- [observation/documented] Repository development practice: the .claude/skills and .agents/skills directories are internal contributor skills for working on the InsForge OSS repository, distinct from the public plugin maintained in InsForge/insforge-skills. -- evidence: [CLAUDE_PLUGIN.md#L69-L72](https://github.com/InsForge/InsForge/blob/fca20f318722c1fa89371e94878ba08b114c73b7/CLAUDE_PLUGIN.md#L69-L72) (`clm_77f6f395e94062ce53ef8efd9b3aa11d765bcd636a40278a3b5aa99e4037d835`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] Coding agents interact with InsForge through two interfaces: an MCP server (self-hosted and cloud) exposing operations as tools, and a cloud-only CLI paired with Skills invoked from the terminal. -- evidence: [README.md#L48-L48](https://github.com/InsForge/InsForge/blob/fca20f318722c1fa89371e94878ba08b114c73b7/README.md#L48-L48), [README.md#L50-L51](https://github.com/InsForge/InsForge/blob/fca20f318722c1fa89371e94878ba08b114c73b7/README.md#L50-L51) (`clm_b75a5618cf4e209f2bebc0f44ba8868fe6e714c40d1f93dd87cdcdf77e9fcb32`)
- [observation/documented] Through its interfaces agents can read backend context (docs, schemas, metadata such as deployed functions, bucket contents, auth config, and runtime logs) and configure primitives like edge functions, migrations, buckets, and auth providers. -- evidence: [README.md#L55-L56](https://github.com/InsForge/InsForge/blob/fca20f318722c1fa89371e94878ba08b114c73b7/README.md#L55-L56) (`clm_af3e6a0b6e84ccc9de090eb958405c7395e59ddf0000400fdaf20281c5eb503e`)
- [observation/documented] Google OAuth is documented with endpoints GET /api/auth/v1/google-auth (returns an auth_url) and GET /api/auth/oauth/google/callback, which redirects with token (JWT), user_id, email, and name as URL parameters. -- evidence: [GOOGLE_OAUTH_SETUP.md#L54-L54](https://github.com/InsForge/InsForge/blob/fca20f318722c1fa89371e94878ba08b114c73b7/GOOGLE_OAUTH_SETUP.md#L54-L54), [GOOGLE_OAUTH_SETUP.md#L32-L32](https://github.com/InsForge/InsForge/blob/fca20f318722c1fa89371e94878ba08b114c73b7/GOOGLE_OAUTH_SETUP.md#L32-L32), [GOOGLE_OAUTH_SETUP.md#L37-L45](https://github.com/InsForge/InsForge/blob/fca20f318722c1fa89371e94878ba08b114c73b7/GOOGLE_OAUTH_SETUP.md#L37-L45), [GOOGLE_OAUTH_SETUP.md#L68-L71](https://github.com/InsForge/InsForge/blob/fca20f318722c1fa89371e94878ba08b114c73b7/GOOGLE_OAUTH_SETUP.md#L68-L71) (`clm_bd373b5f39446aff159818ab6d913fdb04971853d72ae498e94408d0a947609f`)

## memory-state (1 claim(s))

- [observation/documented] On first Google login the system creates records in auth, identifies, and profiles tables; returning users are looked up by provider and provider_id in the identifies table and have last_login_at updated. -- evidence: [GOOGLE_OAUTH_SETUP.md#L85-L90](https://github.com/InsForge/InsForge/blob/fca20f318722c1fa89371e94878ba08b114c73b7/GOOGLE_OAUTH_SETUP.md#L85-L90), [GOOGLE_OAUTH_SETUP.md#L76-L82](https://github.com/InsForge/InsForge/blob/fca20f318722c1fa89371e94878ba08b114c73b7/GOOGLE_OAUTH_SETUP.md#L76-L82) (`clm_7894865097da0a5b2acecb2cfd153df29f711987cc62fa75444943d9c5c69223`)

## orchestration (1 claim(s))

- [observation/documented] Multiple isolated instances are supported by giving each project its own directory, COMPOSE_PROJECT_NAME, and ports; directories sharing a project name share containers, while distinct names yield separate containers, volumes, databases, and secrets. -- evidence: [README.md#L194-L197](https://github.com/InsForge/InsForge/blob/fca20f318722c1fa89371e94878ba08b114c73b7/README.md#L194-L197), [README.md#L218-L219](https://github.com/InsForge/InsForge/blob/fca20f318722c1fa89371e94878ba08b114c73b7/README.md#L218-L219) (`clm_77710d899fdccae6207da39f19fbeb307462896b6b5aafb612a49c4a89ca939d`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] Self-hosting via Docker Compose requires Docker with Compose v2; a setup script generates secrets including JWT_SECRET, ENCRYPTION_KEY, POSTGRES_PASSWORD, ROOT_ADMIN_PASSWORD, and access keys into ~/insforge/.env (mode 600) without starting anything. -- evidence: [README.md#L117-L117](https://github.com/InsForge/InsForge/blob/fca20f318722c1fa89371e94878ba08b114c73b7/README.md#L117-L117), [README.md#L125-L129](https://github.com/InsForge/InsForge/blob/fca20f318722c1fa89371e94878ba08b114c73b7/README.md#L125-L129) (`clm_e9b9f7552a2ec2507f84366960cf6d977dbdfe73deb2dd863905f2b420dea60d`)
- [observation/documented] The project is licensed under Apache License 2.0, while the public InsForge skills plugin is MIT-licensed. -- evidence: [README.md#L285-L285](https://github.com/InsForge/InsForge/blob/fca20f318722c1fa89371e94878ba08b114c73b7/README.md#L285-L285), [CLAUDE_PLUGIN.md#L89-L89](https://github.com/InsForge/InsForge/blob/fca20f318722c1fa89371e94878ba08b114c73b7/CLAUDE_PLUGIN.md#L89-L89) (`clm_268fa60143b4e9deb04a145622a3f2e61dde914be20d16d007fda4c47fa92cff`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

