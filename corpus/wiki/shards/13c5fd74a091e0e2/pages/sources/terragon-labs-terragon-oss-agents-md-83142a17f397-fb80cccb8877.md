---
access: public
aliases: []
claim_ids:
- clm_24bdb411dddfa9489de24ea6b7a5d48de47deb39c609502cfb341ad185bbe47e
- clm_6474bcc7f0094b6a068b4bc3c88cda8143a315a2d021da68a8c07f2cce6a5a3e
- clm_b0418dbf22eebb19e47a0f85e24d9349d18e9432ef3a13cae1fd02785352eb18
- clm_cab5afd740fc4a66a7deb26c5baa56c673dd1c363aae41a391f54bff86aaef15
maturity: draft
page_id: pg_39a684b6ae935511bacdfb80cccb8877
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_dd5f29b4523b588dba2e152e5e155aba
title: terragon-labs/terragon-oss/AGENTS.md @ 83142a17f397
updated_at: '2026-09-14T03:18:49Z'
---

# terragon-labs/terragon-oss/AGENTS.md @ 83142a17f397

<!-- rcw:begin owner=source:src_dd5f29b4523b588dba2e152e5e155aba block=evidence -->
- Repository development practice: 'pnpm dev' starts Docker containers, the Next.js frontend, docs site, broadcast realtime service, daemon builds, an MCP server, an ngrok tunnel, cron jobs, and the CLI in dev mode. [@claim:clm_24bdb411dddfa9489de24ea6b7a5d48de47deb39c609502cfb341ad185bbe47e]
- Repository development practice: tests run per workspace (apps/www, packages/shared, packages/daemon, packages/sandbox) via 'pnpm -C <dir> test', with type checking via 'pnpm tsc-check'. [@claim:clm_6474bcc7f0094b6a068b4bc3c88cda8143a315a2d021da68a8c07f2cce6a5a3e]
- Repository development practice: after adding a release-notes entry, contributors must increment RELEASE_NOTES_VERSION in apps/www constants, which triggers the release-notes badge for users. [@claim:clm_b0418dbf22eebb19e47a0f85e24d9349d18e9432ef3a13cae1fd02785352eb18]
- Repository development practice: new feature flags are defined in feature-flags-definitions.ts, consumed via a useFeatureFlag hook, and configured on an admin page with global defaults and per-user overrides. [@claim:clm_cab5afd740fc4a66a7deb26c5baa56c673dd1c363aae41a391f54bff86aaef15]
<!-- rcw:end owner=source:src_dd5f29b4523b588dba2e152e5e155aba block=evidence -->

## Researcher notes

