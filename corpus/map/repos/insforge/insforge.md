# insforge/insforge

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit fca20f318722 @ 4305e1ce136d7730

## Summary (orientation draft, not independently verified)

Selected evidence records: InsForge is described as an all-in-one, open-source backend platform for agentic coding, giving coding agents database, auth, storage, compute, hosting, and an AI gateway. Coding agents interact with InsForge through two interfaces: an MCP server (self-hosted and cloud) exposing operations as tools, and a cloud-only CLI paired with Skills invoked from the terminal.

## Source coverage

Source coverage (partial): 6 of 357 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 13 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

13 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] InsForge is described as an all-in-one, open-source backend platform for agentic coding, giving coding agents database, auth, storage, compute, hosting, and an AI gateway. -- evidence: [README.md#L42-L42](https://github.com/InsForge/InsForge/blob/fca20f318722c1fa89371e94878ba08b114c73b7/README.md#L42-L42)
- components (1 claim(s)):
  - [observation/documented] Core products include authentication, Postgres database, S3-compatible storage, an OpenAI-compatible model gateway, edge functions, compute (private preview), and site deployment. -- evidence: [README.md#L92-L98](https://github.com/InsForge/InsForge/blob/fca20f318722c1fa89371e94878ba08b114c73b7/README.md#L92-L98)
- design-choices (2 claim(s)):
  - [observation/documented] The MCP server and CLI expose infrastructure as structured, machine-readable context so AI coding agents can plan and execute operations autonomously within scoped permissions. -- evidence: [docs/alternatives.mdx#L11-L15](https://github.com/InsForge/InsForge/blob/fca20f318722c1fa89371e94878ba08b114c73b7/docs/alternatives.mdx#L11-L15)
  - [observation/documented] Storage defaults to the local filesystem; S3-compatible backing storage enables an S3 gateway at /storage/v1/s3, with bundled MinIO or RustFS compose overlays or bring-your-own S3 settings (S3_BUCKET, S3_REGION, keys, optional endpoint and presigned-URL mode). -- evidence: [README.md#L240-L240](https://github.com/InsForge/InsForge/blob/fca20f318722c1fa89371e94878ba08b114c73b7/README.md#L240-L240), [README.md#L233-L234](https://github.com/InsForge/InsForge/blob/fca20f318722c1fa89371e94878ba08b114c73b7/README.md#L233-L234), [README.md#L251-L251](https://github.com/InsForge/InsForge/blob/fca20f318722c1fa89371e94878ba08b114c73b7/README.md#L251-L251), [README.md#L231-L231](https://github.com/InsForge/InsForge/blob/fca20f318722c1fa89371e94878ba08b114c73b7/README.md#L231-L231)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: docs/asset-guidelines.md instructs contributors to review and optimize documentation media before committing, with a PR checklist and recommended tools (FFmpeg, pngquant, jpegoptim, SVGO). -- evidence: [docs/asset-guidelines.md#L77-L80](https://github.com/InsForge/InsForge/blob/fca20f318722c1fa89371e94878ba08b114c73b7/docs/asset-guidelines.md#L77-L80), [docs/asset-guidelines.md#L3-L3](https://github.com/InsForge/InsForge/blob/fca20f318722c1fa89371e94878ba08b114c73b7/docs/asset-guidelines.md#L3-L3), [docs/asset-guidelines.md#L68-L73](https://github.com/InsForge/InsForge/blob/fca20f318722c1fa89371e94878ba08b114c73b7/docs/asset-guidelines.md#L68-L73)
  - [observation/documented] Repository development practice: the .claude/skills and .agents/skills directories are internal contributor skills for working on the InsForge OSS repository, distinct from the public plugin maintained in InsForge/insforge-skills. -- evidence: [CLAUDE_PLUGIN.md#L69-L72](https://github.com/InsForge/InsForge/blob/fca20f318722c1fa89371e94878ba08b114c73b7/CLAUDE_PLUGIN.md#L69-L72)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] Coding agents interact with InsForge through two interfaces: an MCP server (self-hosted and cloud) exposing operations as tools, and a cloud-only CLI paired with Skills invoked from the terminal. -- evidence: [README.md#L48-L48](https://github.com/InsForge/InsForge/blob/fca20f318722c1fa89371e94878ba08b114c73b7/README.md#L48-L48), [README.md#L50-L51](https://github.com/InsForge/InsForge/blob/fca20f318722c1fa89371e94878ba08b114c73b7/README.md#L50-L51)
  - [observation/documented] Through its interfaces agents can read backend context (docs, schemas, metadata such as deployed functions, bucket contents, auth config, and runtime logs) and configure primitives like edge functions, migrations, buckets, and auth providers. -- evidence: [README.md#L55-L56](https://github.com/InsForge/InsForge/blob/fca20f318722c1fa89371e94878ba08b114c73b7/README.md#L55-L56)
- memory-state (1 claim(s)):
  - [observation/documented] On first Google login the system creates records in auth, identifies, and profiles tables; returning users are looked up by provider and provider_id in the identifies table and have last_login_at updated. -- evidence: [GOOGLE_OAUTH_SETUP.md#L85-L90](https://github.com/InsForge/InsForge/blob/fca20f318722c1fa89371e94878ba08b114c73b7/GOOGLE_OAUTH_SETUP.md#L85-L90), [GOOGLE_OAUTH_SETUP.md#L76-L82](https://github.com/InsForge/InsForge/blob/fca20f318722c1fa89371e94878ba08b114c73b7/GOOGLE_OAUTH_SETUP.md#L76-L82)
- orchestration (1 claim(s)):
More evidence: [full detail](insforge.detail.md)

Metadata and full claim list: [full detail](insforge.detail.md)
Human notes ([notes](insforge.notes.md), never overwritten by build)

[Back to map index](../../index.md)
