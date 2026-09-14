---
access: public
aliases: []
claim_ids:
- clm_0411518ed975874696d801f60216b7ec62c449f9ef1db632599339515cdd43f7
- clm_431e205479994e2aaf4be0fffdc678f8a3e1e9b89bde2cb2418bb0c7942e3f70
- clm_5a5054962e7f62e5f7ffe5dc0c3e47bd4734c919319bd15439e9ca3ec5603742
- clm_7225ccde0f524d2c7ff44ad39db83e362d44a93fa272cc000388deffca84cc8a
- clm_7e4102305bfd68ca4ccba87b7f58ab2c175d0ac62e2c2adf931f5c033adc1079
- clm_c8af81d71844b747895c24a61502a0d15d5639e1f6df33dbe9737d2116a1789c
- clm_e3b6115fae1f540bc58cf051436693dad2f772e12d44f78a15b70ace82991c4e
- clm_f745f92ef6afffcc11ac1011bef71fc1ab933a434b24dfcad914c24aaafc700d
- clm_fd39b50ab4b25439b54249e86633fb6b220564146828fb0f3fbef988780abae6
maturity: draft
page_id: pg_29bdcace6726509a9e69ef723eef2b07
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_0aac67beaf5555fc942d07c14432354f
title: qaml-ai/camelAI/README.md @ 5f3c295d66fd
updated_at: '2026-09-14T02:33:58Z'
---

# qaml-ai/camelAI/README.md @ 5f3c295d66fd

<!-- rcw:begin owner=source:src_0aac67beaf5555fc942d07c14432354f block=evidence -->
- Project files live in WorkspaceFilesystemDO: small files in Durable Object SQLite, larger ones in R2, with git history provided by Cloudflare Artifacts. [@claim:clm_0411518ed975874696d801f60216b7ec62c449f9ef1db632599339515cdd43f7]
- The self-hosted target intentionally lacks outbound email, password-email verification, and multi-node failover. [@claim:clm_431e205479994e2aaf4be0fffdc678f8a3e1e9b89bde2cb2418bb0c7942e3f70]
- Linux sandbox containers are reserved for short-lived jobs (app builds, notebook analysis, SQL queries); project deploys flow through a build sandbox to Workers for Platforms, and a dispatcher Worker routes requests to published apps. [@claim:clm_5a5054962e7f62e5f7ffe5dc0c3e47bd4734c919319bd15439e9ca3ec5603742]
- The agent writes JavaScript instead of bash; Code Mode runs it in fresh V8 isolates with explicit platform and connection methods, and credentials remain outside the execution sandbox. [@claim:clm_7225ccde0f524d2c7ff44ad39db83e362d44a93fa272cc000388deffca84cc8a]
- The repository includes agent evals run via 'bun run test:eval <eval-id>' by manifest ID, requiring Docker and additional credentials. [@claim:clm_7e4102305bfd68ca4ccba87b7f58ab2c175d0ac62e2c2adf931f5c033adc1079]
- Each chat thread runs its own coding agent inside a Cloudflare Durable Object (ChatThreadDO), which owns the agent loop and persistent chat state. [@claim:clm_c8af81d71844b747895c24a61502a0d15d5639e1f6df33dbe9737d2116a1789c]
- The agent harness is camelAI's own, built from pi's lower-level agent-loop and state-management libraries; Anthropic, OpenAI, OpenRouter, Bedrock, and custom endpoints supply only the model, not the harness. [@claim:clm_e3b6115fae1f540bc58cf051436693dad2f772e12d44f78a15b70ace82991c4e]
- Repository development practice: contributors should run bun run typecheck, lint, and test:all before opening a pull request, add focused tests for behavior changes, and follow the architecture and code conventions in AGENTS.md. [@claim:clm_f745f92ef6afffcc11ac1011bef71fc1ab933a434b24dfcad914c24aaafc700d]
- Development requires Node.js 22+, Bun, a Cloudflare account, and Docker for sandbox-backed features and agent evals; in the self-host target the application runs under workerd. [@claim:clm_fd39b50ab4b25439b54249e86633fb6b220564146828fb0f3fbef988780abae6]
<!-- rcw:end owner=source:src_0aac67beaf5555fc942d07c14432354f block=evidence -->

## Researcher notes

