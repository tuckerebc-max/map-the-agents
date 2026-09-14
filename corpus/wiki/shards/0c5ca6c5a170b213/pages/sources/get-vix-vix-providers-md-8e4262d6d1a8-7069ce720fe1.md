---
access: public
aliases: []
claim_ids:
- clm_020a496a591bcacc57dc87e0a3dcf7401640c6e3e1128853ba970b17fb82ebe7
- clm_11d79d5e65c091396041c791d76df936842330d482f6b1e55b4d294a3a17f1e6
- clm_8624316264fceb42feac30c1bf13c2dbf6cf44166f2e8aa07bb2dbb17b6f4ded
- clm_b8e46ecd9b155effeb248f4b2382de30c9607eab80d846fc35e3c0cdf2efbb9c
- clm_ebfe153201e4121ed4c396c411725a8a6b69e32bf6b230a052ec0bb5ce5c779b
maturity: draft
page_id: pg_3fc65fb097cf54e4b8897069ce720fe1
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_03f2deb9c7e851499ba61146fe05d758
title: get-vix/vix/PROVIDERS.md @ 8e4262d6d1a8
updated_at: '2026-09-14T01:51:04Z'
---

# get-vix/vix/PROVIDERS.md @ 8e4262d6d1a8

<!-- rcw:begin owner=source:src_03f2deb9c7e851499ba61146fe05d758 block=evidence -->
- Vix ships built-in provider support for Anthropic, OpenAI, OpenRouter, OrcaRouter, AWS Bedrock, Ollama, llama.cpp, and Lemonade, among others. [@claim:clm_020a496a591bcacc57dc87e0a3dcf7401640c6e3e1128853ba970b17fb82ebe7]
- With local:true, the model list is fetched live from an OpenAI-compatible GET /models endpoint (cached 5 seconds), with Ollama- and llama.cpp-specific probes for loaded models and context lengths; unreachable servers show as offline after a 1.5s timeout. [@claim:clm_11d79d5e65c091396041c791d76df936842330d482f6b1e55b4d294a3a17f1e6]
- The wire_format field selects among a closed set of compiled HTTP adapters: chat_completions (OpenAI-compatible), messages (Anthropic), and responses (OpenAI Responses API); other values are rejected at load. [@claim:clm_8624316264fceb42feac30c1bf13c2dbf6cf44166f2e8aa07bb2dbb17b6f4ded]
- Credential methods are tried in order and the first to resolve wins; kinds include api_key (env var or keyring), none, and OAuth flows (oauth_token, oauth_mint_key) referencing auth_logins entries by login_id. [@claim:clm_b8e46ecd9b155effeb248f4b2382de30c9607eab80d846fc35e3c0cdf2efbb9c]
- Providers are configured via a providers.json overlay in ~/.vix/ or ./.vix/ merged over an embedded base: same-id entries are field-patched, new ids appended, and models/credential_methods arrays replace wholesale. [@claim:clm_ebfe153201e4121ed4c396c411725a8a6b69e32bf6b230a052ec0bb5ce5c779b]
<!-- rcw:end owner=source:src_03f2deb9c7e851499ba61146fe05d758 block=evidence -->

## Researcher notes

