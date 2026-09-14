---
access: public
aliases: []
claim_ids:
- clm_0e520d86afa2cb27376e5ec9bb734a9910c9541a3b870168becf78b8e5cd9426
- clm_38a87917d5ee26b5e212041f5ebef9b3be9a31632702b3812b9f1a5bec87dbee
- clm_84c026816ec92fad2fd804d66a572e8283e81bedbdb6ef9cd1b6fff52313f103
- clm_a972f6cb63c33ef32919a1680f96434409d7f268fa40adc57045ea757f00d838
- clm_da5a10718382ae1b39c451eaba587d16ca1dd0efbac06b36bc6c24404c207692
maturity: draft
page_id: pg_5322d9f220635a7fb72719645ded3983
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_6ecbb1d544745eaeb233d9f61153d1c8
title: lidge-jun/ima2-gen/docs/API.md @ 7fa7d426d928
updated_at: '2026-09-14T04:07:13Z'
---

# lidge-jun/ima2-gen/docs/API.md @ 7fa7d426d928

<!-- rcw:begin owner=source:src_6ecbb1d544745eaeb233d9f61153d1c8 block=evidence -->
- The local server exposes an HTTP API at localhost:3333, including /api/capabilities, /api/models, /api/auth/switch, /api/video/generate, and prompt-builder endpoints. [@claim:clm_0e520d86afa2cb27376e5ec9bb734a9910c9541a3b870168becf78b8e5cd9426]
- Loopback binds run single-user with no token; non-loopback binds require IMA2_LAN_TOKEN, protecting /api and /generated with in-memory, origin-bound sessions that expire after eight hours. [@claim:clm_38a87917d5ee26b5e212041f5ebef9b3be9a31632702b3812b9f1a5bec87dbee]
- NovelAI generation is text-to-image only: reference images, edits, and masks are refused rather than silently dropped, and its edit/video surfaces are declared unsupported. [@claim:clm_84c026816ec92fad2fd804d66a572e8283e81bedbdb6ef9cd1b6fff52313f103]
- Documented provider limits: the agy lane outputs fixed 1024x1024 JPEG, allows at most 3 reference images, has no web-search/quality/size/mask controls, and does not support video (AGY_VIDEO_UNSUPPORTED). [@claim:clm_a972f6cb63c33ef32919a1680f96434409d7f268fa40adc57045ea757f00d838]
- Image generation supports multiple provider lanes: oauth (local Codex proxy), api (OpenAI Responses API), grok (xAI OAuth), grok-api (XAI_API_KEY), nai (NovelAI), agy (Antigravity CLI spawning Gemini image generation), and gemini-api. [@claim:clm_da5a10718382ae1b39c451eaba587d16ca1dd0efbac06b36bc6c24404c207692]
<!-- rcw:end owner=source:src_6ecbb1d544745eaeb233d9f61153d1c8 block=evidence -->

## Researcher notes

