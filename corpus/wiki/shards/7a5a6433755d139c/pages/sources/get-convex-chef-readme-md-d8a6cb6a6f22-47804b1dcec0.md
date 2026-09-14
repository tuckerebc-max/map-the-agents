---
access: public
aliases: []
claim_ids:
- clm_0670296ae09a0c895e1b825d8681cc2d2f1d1b6e96a0370f2255ba6a82db4fb7
- clm_0df19dfd222069de6306dff2c54b94d7a675bd28cb82315aa46523c64c61e6ba
- clm_1b45ab38e4fca47cba084a492a14345bdc6735dfca5e6111b9209516a60460ba
- clm_404d2b59580c2a2890972343f16a66b3648f4810b8eb8721d1c8b730f94c7a6b
- clm_6e1f21bd72601b31658df6431dc11ead267b76a0b7d4c7c27a455aee47ff2ff3
- clm_7f2c53642a70c9c21ed2a2562831f851b3a40b5b3e916304a0ed9369c66a54b4
- clm_90ef85dd5ae41a7e79fcaec7358ecf21ffb0a14c4e86dba84e9645fc2e491d5d
- clm_afd88c5743746e471c7c033fe1cc90bd8d6a72e8335cf1ea96a63c0c5709ca20
- clm_c497889471984295119a9ff21cd91ab811eb9e4e79efa60673fca5f7dcf48c86
- clm_d316a8049b80ea00fca82483af7aaf9d81614463c6a19d0dcfe77e4545892437
maturity: draft
page_id: pg_a742b6c841745220b95e47804b1dcec0
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_dc4a92ba974555b4bed66c1116743109
title: get-convex/chef/README.md @ d8a6cb6a6f22
updated_at: '2026-09-14T01:51:03Z'
---

# get-convex/chef/README.md @ d8a6cb6a6f22

<!-- rcw:begin owner=source:src_dc4a92ba974555b4bed66c1116743109 block=evidence -->
- Chef is described as an AI app builder that creates full-stack web apps with a built-in database, zero-config auth, file uploads, real-time UIs, and background workflows. [@claim:clm_0670296ae09a0c895e1b825d8681cc2d2f1d1b6e96a0370f2255ba6a82db4fb7]
- The repository includes a template directory used as the starting point for all Chef projects, and a convex directory storing chats and user metadata. [@claim:clm_0df19dfd222069de6306dff2c54b94d7a675bd28cb82315aa46523c64c61e6ba]
- The project is a fork of the stable branch of bolt.diy. [@claim:clm_1b45ab38e4fca47cba084a492a14345bdc6735dfca5e6111b9209516a60460ba]
- Repository development practice: local setup uses nvm, pnpm, a VITE_CONVEX_URL placeholder, and 'npx convex dev --once' to provision a Convex project, then 'pnpm run dev' plus 'npx convex dev'. [@claim:clm_404d2b59580c2a2890972343f16a66b3648f4810b8eb8721d1c8b730f94c7a6b]
- A chefshot directory defines a CLI interface for interacting with the Chef webapp. [@claim:clm_6e1f21bd72601b31658df6431dc11ead267b76a0b7d4c7c27a455aee47ff2ff3]
- Local code generation is enabled by supplying API keys for providers including Anthropic, Google, OpenAI, and xAI, either via env file or the Chef settings page. [@claim:clm_7f2c53642a70c9c21ed2a2562831f851b3a40b5b3e916304a0ed9369c66a54b4]
- The chef-agent directory handles the agentic loop by injecting system prompts, defining tools, and calling model providers. [@claim:clm_90ef85dd5ae41a7e79fcaec7358ecf21ffb0a14c4e86dba84e9645fc2e491d5d]
- Chef is offered as a hosted webapp at chef.convex.dev with a free tier, and can also be run locally following README instructions. [@claim:clm_afd88c5743746e471c7c033fe1cc90bd8d6a72e8335cf1ea96a63c0c5709ca20]
- Chef ships with an authentication configuration tied to Convex's internal control plane for user accounts; forks for production must replace it with their own auth. [@claim:clm_c497889471984295119a9ff21cd91ab811eb9e4e79efa60673fca5f7dcf48c86]
- Chef's capabilities come from being built on Convex, whose APIs the README describes as an ideal fit for code generation. [@claim:clm_d316a8049b80ea00fca82483af7aaf9d81614463c6a19d0dcfe77e4545892437]
<!-- rcw:end owner=source:src_dc4a92ba974555b4bed66c1116743109 block=evidence -->

## Researcher notes

