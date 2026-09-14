# terragon-labs/terragon-oss -- full detail

[Back to orientation](terragon-oss.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/terragon-labs/terragon-oss/83142a17f3970df3e14d1879234a603db6e4f615/855649a683fe5a0c.json](../../../wiki/dossiers/terragon-labs/terragon-oss/83142a17f3970df3e14d1879234a603db6e4f615/855649a683fe5a0c.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (2 claim(s))

- [observation/documented] Each agent runs in an isolated sandbox container with its own repository copy, letting it read files, edit, and run tests without affecting concurrent tasks or the local environment. -- evidence: [README.md#L13-L20](https://github.com/terragon-labs/terragon-oss/blob/83142a17f3970df3e14d1879234a603db6e4f615/README.md#L13-L20) (`clm_80b5f11c0dcbfbf96324b30e75167c52f71866eb3f1095fd8c3d9a7c1cfb33be`)
- [observation/documented] Tasks get unique branches, and agent work is checkpointed to GitHub with AI-generated commits and pull requests; this git workflow can be disabled for flexibility. -- evidence: [README.md#L13-L20](https://github.com/terragon-labs/terragon-oss/blob/83142a17f3970df3e14d1879234a603db6e4f615/README.md#L13-L20) (`clm_c1c5a01a90d43b81498751c2f48461ded03005c665bca22a3dd20602ce3b5e79`)

## workflows (6 claim(s))

- [observation/documented] Repository development practice: local development requires Node.js 20+, pnpm 10.14.0+, Docker for PostgreSQL/Redis containers, and Stripe CLI for webhook forwarding; dependencies install via 'pnpm install'. -- evidence: [README.md#L39-L41](https://github.com/terragon-labs/terragon-oss/blob/83142a17f3970df3e14d1879234a603db6e4f615/README.md#L39-L41), [README.md#L24-L27](https://github.com/terragon-labs/terragon-oss/blob/83142a17f3970df3e14d1879234a603db6e4f615/README.md#L24-L27) (`clm_09fa607ceb81ccc4a8b44c385ab92d5aee194654d77ba59c3e37f36a4fe8cf67`)
- [observation/documented] Repository development practice: after schema changes, contributors push the Drizzle schema to the dev database with 'pnpm -C packages/shared drizzle-kit-push-dev', and 'pnpm dev' starts all development services. -- evidence: [README.md#L81-L81](https://github.com/terragon-labs/terragon-oss/blob/83142a17f3970df3e14d1879234a603db6e4f615/README.md#L81-L81), [README.md#L77-L79](https://github.com/terragon-labs/terragon-oss/blob/83142a17f3970df3e14d1879234a603db6e4f615/README.md#L77-L79), [README.md#L71-L73](https://github.com/terragon-labs/terragon-oss/blob/83142a17f3970df3e14d1879234a603db6e4f615/README.md#L71-L73), [README.md#L69-L69](https://github.com/terragon-labs/terragon-oss/blob/83142a17f3970df3e14d1879234a603db6e4f615/README.md#L69-L69) (`clm_bfe2ae56a802f0a7298b7b4fbc9b5c1ce9430ebdd46d88432d6f1f691b4135de`)
- [observation/documented] Repository development practice: tests run per workspace (apps/www, packages/shared, packages/daemon, packages/sandbox) via 'pnpm -C <dir> test', with type checking via 'pnpm tsc-check'. -- evidence: [AGENTS.md#L46-L49](https://github.com/terragon-labs/terragon-oss/blob/83142a17f3970df3e14d1879234a603db6e4f615/AGENTS.md#L46-L49), [AGENTS.md#L52-L53](https://github.com/terragon-labs/terragon-oss/blob/83142a17f3970df3e14d1879234a603db6e4f615/AGENTS.md#L52-L53) (`clm_6474bcc7f0094b6a068b4bc3c88cda8143a315a2d021da68a8c07f2cce6a5a3e`)
- [observation/documented] Repository development practice: 'pnpm dev' starts Docker containers, the Next.js frontend, docs site, broadcast realtime service, daemon builds, an MCP server, an ngrok tunnel, cron jobs, and the CLI in dev mode. -- evidence: [AGENTS.md#L32-L40](https://github.com/terragon-labs/terragon-oss/blob/83142a17f3970df3e14d1879234a603db6e4f615/AGENTS.md#L32-L40) (`clm_24bdb411dddfa9489de24ea6b7a5d48de47deb39c609502cfb341ad185bbe47e`)
- [observation/documented] Repository development practice: new feature flags are defined in feature-flags-definitions.ts, consumed via a useFeatureFlag hook, and configured on an admin page with global defaults and per-user overrides. -- evidence: [AGENTS.md#L131-L131](https://github.com/terragon-labs/terragon-oss/blob/83142a17f3970df3e14d1879234a603db6e4f615/AGENTS.md#L131-L131), [AGENTS.md#L119-L119](https://github.com/terragon-labs/terragon-oss/blob/83142a17f3970df3e14d1879234a603db6e4f615/AGENTS.md#L119-L119), [AGENTS.md#L145-L148](https://github.com/terragon-labs/terragon-oss/blob/83142a17f3970df3e14d1879234a603db6e4f615/AGENTS.md#L145-L148) (`clm_cab5afd740fc4a66a7deb26c5baa56c673dd1c363aae41a391f54bff86aaef15`)
- [observation/documented] Repository development practice: after adding a release-notes entry, contributors must increment RELEASE_NOTES_VERSION in apps/www constants, which triggers the release-notes badge for users. -- evidence: [AGENTS.md#L301-L303](https://github.com/terragon-labs/terragon-oss/blob/83142a17f3970df3e14d1879234a603db6e4f615/AGENTS.md#L301-L303) (`clm_b0418dbf22eebb19e47a0f85e24d9349d18e9432ef3a13cae1fd02785352eb18`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] The product ships a 'terry' CLI for local task takeover and continuation, plus an MCP server so MCP-compatible clients like Cursor and Claude Code can create and manage tasks. -- evidence: [README.md#L13-L20](https://github.com/terragon-labs/terragon-oss/blob/83142a17f3970df3e14d1879234a603db6e4f615/README.md#L13-L20) (`clm_a15105b67f635d6a2bf09b8b3d7a9f77367c3c5fbd7989c10208842137ea3794`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (2 claim(s))

- [observation/documented] Terragon supports multiple coding agents—Claude Code, OpenAI Codex, Amp, and Gemini—and is designed so support for additional agents can be added. -- evidence: [README.md#L13-L20](https://github.com/terragon-labs/terragon-oss/blob/83142a17f3970df3e14d1879234a603db6e4f615/README.md#L13-L20) (`clm_5d77f26f953f0469f28f0fdeb51fa9c2fc8dcac4185ab3bcec0691f6cc67e85a`)
- [observation/documented] The product offers automations: recurring tasks or event-triggered workflows, such as triggers on new issues or pull requests, to automate repetitive development work. -- evidence: [README.md#L13-L20](https://github.com/terragon-labs/terragon-oss/blob/83142a17f3970df3e14d1879234a603db6e4f615/README.md#L13-L20) (`clm_a86c9e5a572778cabeeff1d8b431befc950957eb5541254c3e18b6294a47f1a2`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## limitations (1 claim(s))

- [observation/documented] The repository is an as-is snapshot taken at Terragon's shutdown, with no guarantees of maintenance, support, or completeness. -- evidence: [README.md#L3-L3](https://github.com/terragon-labs/terragon-oss/blob/83142a17f3970df3e14d1879234a603db6e4f615/README.md#L3-L3) (`clm_ad6b837c7f991284a6be97ae872399956885b2d86bc86dba20e236ddf592f329`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

