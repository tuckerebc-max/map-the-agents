---
access: public
aliases: []
claim_ids:
- clm_45e4739c007133a748e6984bce4c1cf2a9a8c7673eab49de40ba44d1b9f5f911
- clm_531732df3e25e5901e4d6b0de3d6f637260714d9113b2e2f217d8c72fdc9f2ab
- clm_80e3177c2e4d9d0cad0f89895e55406d808fae615414a5dc07f475d37f888c14
- clm_8f9a73ef3a72c6e7b7b985b69bf7f647b3f278bb0ed6072c07c1844549545410
- clm_99963fd4e80e339846d1f08f6e72472738cc966c137573b914238755a9b1d8db
- clm_b33079a20f70abeaac9d48e6dfeb65d0e22a770a6fa8eb71790b772c8667736c
- clm_f4e4835e7798b232aa17cc2cfec8c700b3f112c086a09a90164502a178692642
- clm_fe12b96858f7fbcd379d50aae99e7136c7faddd750b44f9f73526fbf372ffcfd
maturity: draft
page_id: pg_554aa72f139954b7acad0a699a979692
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_2fad2636cbb55ce286d06dc4c3db0261
title: 2389-research/translator/README.md @ e9ccc74351d8
updated_at: '2026-09-14T03:29:58Z'
---

# 2389-research/translator/README.md @ e9ccc74351d8

<!-- rcw:begin owner=source:src_2fad2636cbb55ce286d06dc4c3db0261 block=evidence -->
- The tool specially supports markdown files with YAML frontmatter, detecting and preserving frontmatter metadata used by static site generators like Jekyll and Hugo. [@claim:clm_45e4739c007133a748e6984bce4c1cf2a9a8c7673eab49de40ba44d1b9f5f911]
- An interactive 'translator config' command walks users through setup, including where to store .env configuration, the OpenAI API key, and optional settings such as the default model. [@claim:clm_531732df3e25e5901e4d6b0de3d6f637260714d9113b2e2f217d8c72fdc9f2ab]
- Optional .env settings include DEFAULT_MODEL (shown as o3 in an example), OUTPUT_DIR for translated files, and LOG_LEVEL with options DEBUG through CRITICAL. [@claim:clm_80e3177c2e4d9d0cad0f89895e55406d808fae615414a5dc07f475d37f888c14]
- The codebase is modular, with files for CLI, config, cost, file I/O, frontmatter, language codes, log interpretation, prompts, token counting, and core translation logic. [@claim:clm_8f9a73ef3a72c6e7b7b985b69bf7f647b3f278bb0ed6072c07c1844549545410]
- Configuration is resolved by precedence: environment variables, then a local .env file, then ~/.translator/.env, then ~/.config/translator/.env; OPENAI_API_KEY is required for OpenAI models. [@claim:clm_99963fd4e80e339846d1f08f6e72472738cc966c137573b914238755a9b1d8db]
- Translation follows a multi-stage pipeline: initial translation preserving formatting, an expert editing pass, and critique-revision cycles configurable from 1 to 5 loops for quality improvement. [@claim:clm_b33079a20f70abeaac9d48e6dfeb65d0e22a770a6fa8eb71790b772c8667736c]
- Repository development practice: the project uses pytest for testing, run via 'uv run pytest', with a test suite covering modules including CLI, file handling, cost, and streaming. [@claim:clm_f4e4835e7798b232aa17cc2cfec8c700b3f112c086a09a90164502a178692642]
- Runtime dependencies include openai>=1.78.1, python-dotenv, rich, tiktoken, pycountry, and python-frontmatter, with pytest for testing; Python 3.13+ is required. [@claim:clm_fe12b96858f7fbcd379d50aae99e7136c7faddd750b44f9f73526fbf372ffcfd]
<!-- rcw:end owner=source:src_2fad2636cbb55ce286d06dc4c3db0261 block=evidence -->

## Researcher notes

