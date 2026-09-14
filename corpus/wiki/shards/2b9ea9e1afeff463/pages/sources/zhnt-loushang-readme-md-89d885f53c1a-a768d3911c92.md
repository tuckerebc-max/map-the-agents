---
access: public
aliases: []
claim_ids:
- clm_0fc68fde52d563550c27d6e11d9e914f76e1dd35ea55c1d3430629e4f85c4526
- clm_398429fd77078216e050041812640bbc8965511e7f55d0e0f3d041d4f761a2d5
- clm_3b80c839ff4fe94da270af5359e37313e09a844637af63371223825f0f54a925
- clm_42db6cd5c884fa23bd3ce3a04528b19747e16c2ce8ef2b2e014b0f81a33ee28d
- clm_a5d20332662bed4cd17db01f11749498d0cee804c323974803fdfeaf0e9285be
- clm_ce0c26e1443a55dcd3d480879215783cda2d0eb8cd3edf9da5c64f2c5156e9f6
- clm_d428b6c2a8c8ab8f42e7ca5cd2982410a2a09c712538d9823e70ecdbb1098b01
- clm_db479b2adfa4034bcbfe216baf5a4cb738155f64a63a478793da4855d3dbea29
- clm_f6aa6fda4581943d3b9bece0fa2d52aa2b67e2bcf99086b34e0482a972f63d90
maturity: draft
page_id: pg_fe594e74fe0350ad8c88a768d3911c92
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_c6614789a2475064b7aab9c950e7a14c
title: zhnt/loushang/README.md @ 89d885f53c1a
updated_at: '2026-09-14T03:27:30Z'
---

# zhnt/loushang/README.md @ 89d885f53c1a

<!-- rcw:begin owner=source:src_c6614789a2475064b7aab9c950e7a14c block=evidence -->
- Sessions are durable coding conversations that can be resumed, forked, exported, and inspected, with diagnostics available. [@claim:clm_0fc68fde52d563550c27d6e11d9e914f76e1dd35ea55c1d3430629e4f85c4526]
- Loushang is described as a method-native AI work system for running complex work from intent to verified delivery, with the current focus on a coding CLI. [@claim:clm_398429fd77078216e050041812640bbc8965511e7f55d0e0f3d041d4f761a2d5]
- The system is organized into named layers: method (work contract), work (runtime fact), agent (execution kernel), ai (model access), harness (substrate), coding (V1 surface), tui, and channel. [@claim:clm_3b80c839ff4fe94da270af5359e37313e09a844637af63371223825f0f54a925]
- Tools are defined as executable capabilities made available to the agent under policy, and the product offers built-in coding tools plus configurable tool surfaces. [@claim:clm_42db6cd5c884fa23bd3ce3a04528b19747e16c2ce8ef2b2e014b0f81a33ee28d]
- The CLI exposes flags such as --help, --list-models, and --list-commands, and supports a prompt mode like `loushang -p "..."` for one-shot requests. [@claim:clm_a5d20332662bed4cd17db01f11749498d0cee804c323974803fdfeaf0e9285be]
- Loushang is in active early development; the stable focus is loushang code and the loushang.ai SDK, while work/research/ppt surfaces are roadmap directions only. [@claim:clm_ce0c26e1443a55dcd3d480879215783cda2d0eb8cd3edf9da5c64f2c5156e9f6]
- The loushang.ai SDK appears to provide provider-aware model access with a model registry, streaming, tool calls, and cost helpers, per the README feature list. [@claim:clm_d428b6c2a8c8ab8f42e7ca5cd2982410a2a09c712538d9823e70ecdbb1098b01]
- The project uses uv for virtual environment creation and pip-style editable installation with a [dev] extra, and third-party dependency information is documented in THIRD_PARTY_NOTICES.md. [@claim:clm_db479b2adfa4034bcbfe216baf5a4cb738155f64a63a478793da4855d3dbea29]
- Repository development practice: the recommended way to run Loushang is from source via git clone, a uv-created .venv, and editable install with the dev extra; `make bootstrap` automates this and no `make install` target exists. [@claim:clm_f6aa6fda4581943d3b9bece0fa2d52aa2b67e2bcf99086b34e0482a972f63d90]
<!-- rcw:end owner=source:src_c6614789a2475064b7aab9c950e7a14c block=evidence -->

## Researcher notes

