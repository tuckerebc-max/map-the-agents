---
access: public
aliases: []
claim_ids:
- clm_0e520d86afa2cb27376e5ec9bb734a9910c9541a3b870168becf78b8e5cd9426
- clm_2eef898f7def99b0d2c72e8b2a05a6cc7d98891a3c6e875370f34372446f16c9
- clm_4420ccfc6c0a91a3dc28a6872e8e168bece66baf6861cc30be9165d66df55b2c
- clm_5adca8b2779e44ff3ad0c000c085450287a2f76b5789124b52ca540dceb371a7
- clm_64871377a579f8db8ae5aff427563cb1dae60a2543f4fe9be99133d19cf578b1
- clm_668906c5d16123d024487e7859ce31ef90319bd0bfb919422a1a87b262282980
- clm_7e99dec95a27d557579a0b877b9b42c0c724789d4de9c66c73d05bfda83418cc
- clm_84c026816ec92fad2fd804d66a572e8283e81bedbdb6ef9cd1b6fff52313f103
- clm_8a2b48faf72de88d0452c25cf2857fa96fc5f730f8e64c4058db1e5f694157fd
- clm_da5a10718382ae1b39c451eaba587d16ca1dd0efbac06b36bc6c24404c207692
maturity: draft
page_id: pg_4c0ca213dc6d53dfb87d04707204306d
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_bbbb9ed08f74570590a79c4e070c7967
title: lidge-jun/ima2-gen/README.md @ 7fa7d426d928
updated_at: '2026-09-14T04:07:13Z'
---

# lidge-jun/ima2-gen/README.md @ 7fa7d426d928

<!-- rcw:begin owner=source:src_bbbb9ed08f74570590a79c4e070c7967 block=evidence -->
- The local server exposes an HTTP API at localhost:3333, including /api/capabilities, /api/models, /api/auth/switch, /api/video/generate, and prompt-builder endpoints. [@claim:clm_0e520d86afa2cb27376e5ec9bb734a9910c9541a3b870168becf78b8e5cd9426]
- The package ships three Markdown agent skills (core, frontend, UI/UX) exposed via ima2 skill commands, with listing, JSON wrappers, reference modules, and installation to an agent's skill directory. [@claim:clm_2eef898f7def99b0d2c72e8b2a05a6cc7d98891a3c6e875370f34372446f16c9]
- Repository development practice: contributors clone the repo, run npm install, npm run dev, npm run typecheck, npm test, and npm run build; npm run dev starts the TypeScript server with --watch and verbose diagnostics. [@claim:clm_4420ccfc6c0a91a3dc28a6872e8e168bece66baf6861cc30be9165d66df55b2c]
- If port 3333 is busy the server binds the next available port and records the actual URL in ~/.ima2/server.json; CLI commands follow the advertised URL, overridable via --server or IMA2_SERVER. [@claim:clm_5adca8b2779e44ff3ad0c000c085450287a2f76b5789124b52ca540dceb371a7]
- The product exposes a CLI (entry bin/ima2.js) with commands such as ima2 serve, setup, models, gen, video, edit, vectorize, multimode, skill, doctor, and stop. [@claim:clm_64871377a579f8db8ae5aff427563cb1dae60a2543f4fe9be99133d19cf578b1]
- CLI generation fails closed with NO_DEFAULT_MODEL until an explicit --model/--provider or a saved default is set, to prevent upgrades from silently switching providers or billing lanes. [@claim:clm_668906c5d16123d024487e7859ce31ef90319bd0bfb919422a1a87b262282980]
- The runtime requires Node >=22, pins npm@11.18.0, and depends on OpenAI SDK ^7.4.0 and Express ^5.1.0 per the generated runtime-install table. [@claim:clm_7e99dec95a27d557579a0b877b9b42c0c724789d4de9c66c73d05bfda83418cc]
- NovelAI generation is text-to-image only: reference images, edits, and masks are refused rather than silently dropped, and its edit/video surfaces are declared unsupported. [@claim:clm_84c026816ec92fad2fd804d66a572e8283e81bedbdb6ef9cd1b6fff52313f103]
- The web UI multiplexes all generation progress over a single GET /api/events SSE connection; async requests return 202 with a requestId, while legacy CLI clients without async:true still get per-request SSE streams. [@claim:clm_8a2b48faf72de88d0452c25cf2857fa96fc5f730f8e64c4058db1e5f694157fd]
- Image generation supports multiple provider lanes: oauth (local Codex proxy), api (OpenAI Responses API), grok (xAI OAuth), grok-api (XAI_API_KEY), nai (NovelAI), agy (Antigravity CLI spawning Gemini image generation), and gemini-api. [@claim:clm_da5a10718382ae1b39c451eaba587d16ca1dd0efbac06b36bc6c24404c207692]
<!-- rcw:end owner=source:src_bbbb9ed08f74570590a79c4e070c7967 block=evidence -->

## Researcher notes

