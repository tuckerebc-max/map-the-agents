---
access: public
aliases: []
claim_ids:
- clm_1237b87b10953e38c7cb8aab718dcc62c645bbd626c91b2ae6bf8ea340c4a33f
- clm_1561d16e3c18bdfa2a4e070c416a37d8e71cd3c1c116ca66ad29d27714773882
- clm_3a201638417ed92d8adc18ed4a376bafe0763cbeebf626a1a947b0ab287344fb
- clm_5588a8342f3ace10314a02d4cebd747ff1937202b4528caa37e4fd5e7f8876df
- clm_a466f19b3198a1faef61d08b80bd5b16594978d7455e4387f93f708b6d2af9dc
- clm_ac03c62e4edd93b3f87de8f7adbb13defc4dbcadc0059ee6f5fd6bbc7d9ba421
- clm_c5d4dcb7b586f28bac7bfe1d42d60acdf54d61e75267bedc718a63e234ba6942
- clm_e0bc7f42fde1e400631e8ccbd4af452b56b3082bc6269ef5a45363d645f48a89
- clm_f3f3f6931e228ef502bad0b250cdb3cbdc3f47c8b06d880259acdfc7db7d5b8e
- clm_f770a7da148a22dc7c290bd622544031dc09e63d261359e243ba1b971b87fe73
- clm_f835d5bb76b505be2e094af333cd641ffe2b0b689e8862a47e15a80d8d82a959
maturity: draft
page_id: pg_a17c6a48c95c5beb90fbcffa0fe1ac53
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_2d809baffcdf5c63acdcf2b26e2d84b4
title: elpsykongloo/PaperBanana-Pro/README.md @ 3d9d1f11647e
updated_at: '2026-09-14T03:49:07Z'
---

# elpsykongloo/PaperBanana-Pro/README.md @ 3d9d1f11647e

<!-- rcw:begin owner=source:src_2d809baffcdf5c63acdcf2b26e2d84b4 block=evidence -->
- A CLI batch mode exists via `paperbanana run` with parameters including `--task_name` (diagram/plot), `--exp_mode`, `--provider`, `--max_critic_rounds`, `--retrieval_setting`, and `--resume`. [@claim:clm_1237b87b10953e38c7cb8aab718dcc62c645bbd626c91b2ae6bf8ea340c4a33f]
- Generation runs as background async jobs with a real-time event timeline, supporting 40+ concurrent candidates, and results are packaged in a `Bundle v1` `.bundle.json` format preserving timelines and review records. [@claim:clm_1561d16e3c18bdfa2a4e070c416a37d8e71cd3c1c116ca66ad29d27714773882]
- The README describes a registry-driven pipeline (Pipeline Registry) intended to replace hardcoded branching so new flows can be added via configuration. [@claim:clm_3a201638417ed92d8adc18ed4a376bafe0763cbeebf626a1a947b0ab287344fb]
- A refinement workspace supports 2K/4K upscaling with concurrent multi-version redraws, tree-shaped version chains, and rollback to any historical version. [@claim:clm_5588a8342f3ace10314a02d4cebd747ff1937202b4528caa37e4fd5e7f8876df]
- The documented pipeline comprises six stages: Retriever (few-shot retrieval), Planner (structured visual descriptions), Stylist, Visualizer (image or Matplotlib code), Critic (multi-round review), and optional Polish. [@claim:clm_a466f19b3198a1faef61d08b80bd5b16594978d7455e4387f93f708b6d2af9dc]
- The README states Google has patented the original PaperBanana multi-agent pipeline methodology, so the pipeline logic must not be used commercially, a restriction that also applies to PaperBanana-Pro. [@claim:clm_ac03c62e4edd93b3f87de8f7adbb13defc4dbcadc0059ee6f5fd6bbc7d9ba421]
- The optional PaperBananaBench dataset (dwzhu/PaperBananaBench on Hugging Face) supplies few-shot reference examples and an evaluation benchmark; retrieval can be set to `none` to skip it. [@claim:clm_c5d4dcb7b586f28bac7bfe1d42d60acdf54d61e75267bedc718a63e234ba6942]
- The project targets Python 3.12 or later, installs via `uv sync --locked` plus `uv tool install --editable .`, and requirements.txt contains an editable self-dependency. [@claim:clm_e0bc7f42fde1e400631e8ccbd4af452b56b3082bc6269ef5a45363d645f48a89]
- Four providers are officially supported: Gemini, OpenAI, Openrouter, and Evolink; any OpenAI-compatible API can also be added by supplying a Base URL. [@claim:clm_f3f3f6931e228ef502bad0b250cdb3cbdc3f47c8b06d880259acdfc7db7d5b8e]
- The product exposes a `paperbanana` command whose default form launches a GUI frontend on port 8501, equivalent to `paperbanana gui`. [@claim:clm_f770a7da148a22dc7c290bd622544031dc09e63d261359e243ba1b971b87fe73]
- A viewer subcommand offers `paperbanana viewer evolution` for pipeline evolution and `paperbanana viewer eval` for evaluation-with-reference review. [@claim:clm_f835d5bb76b505be2e094af333cd641ffe2b0b689e8862a47e15a80d8d82a959]
<!-- rcw:end owner=source:src_2d809baffcdf5c63acdcf2b26e2d84b4 block=evidence -->

## Researcher notes

