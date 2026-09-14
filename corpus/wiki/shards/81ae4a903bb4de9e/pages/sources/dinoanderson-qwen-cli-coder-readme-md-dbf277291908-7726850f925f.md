---
access: public
aliases: []
claim_ids:
- clm_28430d8cb72ff365311fcfa9ae73ccb9a5c856b8e88266acef4ae085f54ae318
- clm_2b3c2494f21bce0938a752fef934ee454339ef2f371e0e7e1ffea15ab4f81087
- clm_8cd86934207a9f1854c5fa293eb105640d825bed31e9df9b9ea13ed39fa0f262
- clm_d06dfa68b325af753709850eeda2cef7e9b67ba7491afc6559bdda0b7b68d2ca
- clm_d45d54c32dc5b65f44055756fcb7b91ce880cfdf2a82f5bd33f7e1ce2465918e
- clm_df4e9ba854adec92754593aace44cb45803b46cbd65f141bd1f67cf2fcc4cfe8
- clm_f20e44e77791b3083b5444559fb2aee65000939a8937166362bd2459da26d5e1
- clm_f3b6c8a65fb217e01956562fe6c38e7035c5121894fffd7b25adf4bd6fb43767
maturity: draft
page_id: pg_ec8e0f4253c65b6a89297726850f925f
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_a2f84ecd173455eb86fb66763d359908
title: dinoanderson/qwen_cli_coder/README.md @ dbf277291908
updated_at: '2026-09-14T01:46:09Z'
---

# dinoanderson/qwen_cli_coder/README.md @ dbf277291908

<!-- rcw:begin owner=source:src_a2f84ecd173455eb86fb66763d359908 block=evidence -->
- The project is a community-maintained fork of Google's Gemini CLI, modified to work with Qwen models from Alibaba Cloud, under Apache License 2.0. [@claim:clm_28430d8cb72ff365311fcfa9ae73ccb9a5c856b8e88266acef4ae085f54ae318]
- The fork is not published to npm registries, so installation requires cloning and building from source with npm install, build, and bundle steps. [@claim:clm_2b3c2494f21bce0938a752fef934ee454339ef2f371e0e7e1ffea15ab4f81087]
- Repository development practice: contributors are directed to CONTRIBUTING.md for guidelines specific to this community fork. [@claim:clm_8cd86934207a9f1854c5fa293eb105640d825bed31e9df9b9ea13ed39fa0f262]
- Supported models include qwen-turbo-latest (1M context), qwen3-235b-a22b (131k context), and qwen-vl-plus-latest (32k context, vision). [@claim:clm_d06dfa68b325af753709850eeda2cef7e9b67ba7491afc6559bdda0b7b68d2ca]
- An Assistant Mode launched via 'node bundle/qwen.js --assistant' opens a browser chat interface with file upload, session-based storage, and dark mode detection. [@claim:clm_d45d54c32dc5b65f44055756fcb7b91ce880cfdf2a82f5bd33f7e1ce2465918e]
- Requires Node.js 18 or higher; authentication uses a DashScope API key via DASHSCOPE_API_KEY or QWEN_API_KEY with region-specific QWEN_BASE_URL endpoints. [@claim:clm_df4e9ba854adec92754593aace44cb45803b46cbd65f141bd1f67cf2fcc4cfe8]
- Multi-agent tools (spawn_sub_agent, delegate_task, aggregate_results) support up to 5 concurrent agents with priority-based scheduling and multiple aggregation formats. [@claim:clm_f20e44e77791b3083b5444559fb2aee65000939a8937166362bd2459da26d5e1]
- The CLI provides slash commands including /model for interactive model switching, /lang for English/Chinese localization, /theme, /auth, /mcp, and /tools. [@claim:clm_f3b6c8a65fb217e01956562fe6c38e7035c5121894fffd7b25adf4bd6fb43767]
<!-- rcw:end owner=source:src_a2f84ecd173455eb86fb66763d359908 block=evidence -->

## Researcher notes

