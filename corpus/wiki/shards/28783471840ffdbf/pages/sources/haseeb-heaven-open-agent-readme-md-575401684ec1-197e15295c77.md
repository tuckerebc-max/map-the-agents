---
access: public
aliases: []
claim_ids:
- clm_1c1f6a71d7299884be3e3e3131414a10ed170939206e5b50e4184e154d56d023
- clm_22f4fa86ee392f64e6390e9420e18aff548b990b1a3813c3c5a990273a2732c6
- clm_2a90ca5fcfb6bc246d49970c362b7f29a134f6fb8053b4a0b3adde4c1c7dd425
- clm_3309447abf730f003b0a346f99dc0a4c49d6b284260cf4854c6cddc799fefce2
- clm_46cdf845cb15ed25573e62229f3861127c7e235e94501c86bef3a11792babc2a
- clm_48e2c63efded4442153e778be4db95df3283d21b7f6db3301eeab5ba2382193b
- clm_5441a2e6c3f6353140a6343b08ec26f6e7481d1eae09875704ed271f54863bb8
- clm_72e29153a1b938bae6668649d18a9b37493835887ed2795639b83140672538e6
- clm_bb97f98c3b39d626bef4e5d449a9f80a2a6a3dd4215b80c5e14c8d44c9523ccd
- clm_bc552c8bb4c9506aa2ba14f95e6498304c955b506af5d878d7978ddcb3e38fa6
maturity: draft
page_id: pg_926eb6d2575e54f5aebc197e15295c77
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_595b8e1ad29a59b598c78be8e0f00240
title: haseeb-heaven/open-agent/README.md @ 575401684ec1
updated_at: '2026-09-14T03:56:06Z'
---

# haseeb-heaven/open-agent/README.md @ 575401684ec1

<!-- rcw:begin owner=source:src_595b8e1ad29a59b598c78be8e0f00240 block=evidence -->
- Cloud providers are configured via per-provider environment variables (e.g. OPENAI_API_KEY, ANTHROPIC_API_KEY, GEMINI_API_KEY, GROQ_API_KEY, OPENROUTER_API_KEY), while local Ollama and LM Studio need no key. [@claim:clm_1c1f6a71d7299884be3e3e3131414a10ed170939206e5b50e4184e154d56d023]
- The CLI exposes flags including --provider, -m/--model, --free, --models, --byok, and -y/--yolo for auto-approving tools in trusted workspaces. [@claim:clm_22f4fa86ee392f64e6390e9420e18aff548b990b1a3813c3c5a990273a2732c6]
- The project is a fork of Google's Gemini CLI (Apache-2.0) with modifications by Haseeb Mir, and is itself licensed Apache-2.0. [@claim:clm_2a90ca5fcfb6bc246d49970c362b7f29a134f6fb8053b4a0b3adde4c1c7dd425]
- A web search tool (google_web_search) auto-selects a backend from available keys, with a no-key fallback chain of Exa (hosted MCP) then DuckDuckGo, and supports Brave, Tavily, and Serper, forcible via WEB_SEARCH_PROVIDER. [@claim:clm_3309447abf730f003b0a346f99dc0a4c49d6b284260cf4854c6cddc799fefce2]
- Interactive sessions support slash commands such as /models, /byok, /websearch, and /skills subcommands (list, link, enable, disable, reload). [@claim:clm_46cdf845cb15ed25573e62229f3861127c7e235e94501c86bef3a11792babc2a]
- The tool is positioned as local-first and BYOK: it supports free OpenRouter models, local Ollama/LM Studio, runs on Windows/Mac/Linux, and requires no account. [@claim:clm_48e2c63efded4442153e778be4db95df3283d21b7f6db3301eeab5ba2382193b]
- Repository development practice: tests run from repo root with npm test using Vitest, which auto-loads root .env (missing keys skip; live quota soft-skips); unit and live provider test commands are documented, with live tests gated by RUN_LIVE_PROVIDER_TESTS / RUN_LOCAL_PROVIDER_TESTS env vars. [@claim:clm_5441a2e6c3f6353140a6343b08ec26f6e7481d1eae09875704ed271f54863bb8]
- Model definitions live in a registry file configs/models.toml, referenced from the README alongside a full matrix in Models.MD. [@claim:clm_72e29153a1b938bae6668649d18a9b37493835887ed2795639b83140672538e6]
- Extensions install from the Slack marketplace or Claude .claude-plugin manifests (plus open-agent-extension.json and .mcp.json formats) via --install-extension, with --auto skipping trust prompts for trusted extensions. [@claim:clm_bb97f98c3b39d626bef4e5d449a9f80a2a6a3dd4215b80c5e14c8d44c9523ccd]
- The project requires Node.js 22+ and is published on npm as @haseeb_heaven/open-agent, installable globally with npm install -g. [@claim:clm_bc552c8bb4c9506aa2ba14f95e6498304c955b506af5d878d7978ddcb3e38fa6]
<!-- rcw:end owner=source:src_595b8e1ad29a59b598c78be8e0f00240 block=evidence -->

## Researcher notes

