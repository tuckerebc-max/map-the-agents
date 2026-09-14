---
access: public
aliases: []
claim_ids:
- clm_018e30c72b409260de177f95b4fa64741bc99c7b87dbfc2e109e64a25651b93c
- clm_2b347d8345e6c34270edc78e462a8b9fe5ed3a2028b16b67d4eb22fe2f0a7f7f
- clm_3aecd57346c65c1f128501048c031576335c2b59d576c09b9026bbfda5898611
- clm_45e4739c007133a748e6984bce4c1cf2a9a8c7673eab49de40ba44d1b9f5f911
- clm_80e3177c2e4d9d0cad0f89895e55406d808fae615414a5dc07f475d37f888c14
- clm_99963fd4e80e339846d1f08f6e72472738cc966c137573b914238755a9b1d8db
- clm_b33079a20f70abeaac9d48e6dfeb65d0e22a770a6fa8eb71790b772c8667736c
- clm_c71fdbc188bde49dcf50eaa7e494c895c96561be423553524225f3bd2696e362
- clm_e49b44f280c8efc429c65888d2fc1ea079132ee5827b839dd71c7c3ebc78e6fb
- clm_f4e4835e7798b232aa17cc2cfec8c700b3f112c086a09a90164502a178692642
- clm_fe12b96858f7fbcd379d50aae99e7136c7faddd750b44f9f73526fbf372ffcfd
- clm_ff652c28fab1c9efa9c61895ab8cde91d18d7feb936cd6a651a542b38055ddfb
maturity: draft
page_id: pg_795fc2ac11385e1f88cbeff7c6856bc5
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_cbb1e47a4aae5bd9bfc28e0f8f333cf5
title: 2389-research/translator/spec.md @ e9ccc74351d8
updated_at: '2026-09-14T03:29:58Z'
---

# 2389-research/translator/spec.md @ e9ccc74351d8

<!-- rcw:begin owner=source:src_cbb1e47a4aae5bd9bfc28e0f8f333cf5 block=evidence -->
- Per the spec, a provider abstraction layer offers a unified interface for OpenAI and Anthropic APIs, with model prefixes like openai:model and anthropic:model and auto-detection for unprefixed names. [@claim:clm_018e30c72b409260de177f95b4fa64741bc99c7b87dbfc2e109e64a25651b93c]
- The spec additionally lists anthropic>=0.25.0 as a core API dependency and swarm (from GitHub) for future use. [@claim:clm_2b347d8345e6c34270edc78e462a8b9fe5ed3a2028b16b67d4eb22fe2f0a7f7f]
- The spec describes a layered flow: main.py bootstraps TranslatorCLI, which coordinates file reading, frontmatter extraction, token counting, cost estimation, translation, and output writing. [@claim:clm_3aecd57346c65c1f128501048c031576335c2b59d576c09b9026bbfda5898611]
- The tool specially supports markdown files with YAML frontmatter, detecting and preserving frontmatter metadata used by static site generators like Jekyll and Hugo. [@claim:clm_45e4739c007133a748e6984bce4c1cf2a9a8c7673eab49de40ba44d1b9f5f911]
- Optional .env settings include DEFAULT_MODEL (shown as o3 in an example), OUTPUT_DIR for translated files, and LOG_LEVEL with options DEBUG through CRITICAL. [@claim:clm_80e3177c2e4d9d0cad0f89895e55406d808fae615414a5dc07f475d37f888c14]
- Configuration is resolved by precedence: environment variables, then a local .env file, then ~/.translator/.env, then ~/.config/translator/.env; OPENAI_API_KEY is required for OpenAI models. [@claim:clm_99963fd4e80e339846d1f08f6e72472738cc966c137573b914238755a9b1d8db]
- Translation follows a multi-stage pipeline: initial translation preserving formatting, an expert editing pass, and critique-revision cycles configurable from 1 to 5 loops for quality improvement. [@claim:clm_b33079a20f70abeaac9d48e6dfeb65d0e22a770a6fa8eb71790b772c8667736c]
- The spec's issues analysis lists current limitations including inefficient streaming token counting, potential memory leaks in the cancellation handler, race conditions in streaming, and hard-coded parameters and paths. [@claim:clm_c71fdbc188bde49dcf50eaa7e494c895c96561be423553524225f3bd2696e362]
- The spec claims analytics including translation accuracy tracking and quality metrics; this appears to be documented intent rather than a demonstrated benchmark harness. [@claim:clm_e49b44f280c8efc429c65888d2fc1ea079132ee5827b839dd71c7c3ebc78e6fb]
- Repository development practice: the project uses pytest for testing, run via 'uv run pytest', with a test suite covering modules including CLI, file handling, cost, and streaming. [@claim:clm_f4e4835e7798b232aa17cc2cfec8c700b3f112c086a09a90164502a178692642]
- Runtime dependencies include openai>=1.78.1, python-dotenv, rich, tiktoken, pycountry, and python-frontmatter, with pytest for testing; Python 3.13+ is required. [@claim:clm_fe12b96858f7fbcd379d50aae99e7136c7faddd750b44f9f73526fbf372ffcfd]
- Documented limitations include no caching and single-file-only processing, both noted as future enhancements, plus file size constrained by model token limits. [@claim:clm_ff652c28fab1c9efa9c61895ab8cde91d18d7feb936cd6a651a542b38055ddfb]
<!-- rcw:end owner=source:src_cbb1e47a4aae5bd9bfc28e0f8f333cf5 block=evidence -->

## Researcher notes

