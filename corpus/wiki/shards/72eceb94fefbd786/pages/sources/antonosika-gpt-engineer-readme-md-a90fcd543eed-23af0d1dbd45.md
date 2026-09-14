---
access: public
aliases: []
claim_ids:
- clm_094948b95144e1107865d19360c242ecb9ccd936647da6c0f8e4eb6bc90352aa
- clm_2cfe8e325151f496686c94c162a14084655b1b44963d0b6b392ee32cb04cad02
- clm_739a2fc9f068a38de9d1ba38d30b4873cb18f04fbb9874ee9d045e3c0b82cf72
- clm_7b7485ee33859e9e4cf8a6810cf5680be5446fcd66c8f8c598d8fbaa45b7581b
- clm_7fb1ce9c2372ca48d49429bda813c5194b82ca1ec9789c76b75abc9c67ed9b4e
- clm_82e2af3d3111cbb96cccccf372b8bbbfd0f29288e75324950f9fbe9008ac19d8
- clm_8859ccaa32842be75d6a1ef25c537b346822d1fa8949e105c027776d2330b3c7
- clm_a8680023473091ec4f8a64ce36add12c92ae2387744261c90908877e9c73226a
- clm_c49cb0e45504806921065f995a962f4dfe65e6d0687895f86627e7ad5f375d40
maturity: draft
page_id: pg_fd11d72a444453b28ab223af0d1dbd45
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_62b30ea94d5059c1b08b6969e830ff42
title: AntonOsika/gpt-engineer/README.md @ a90fcd543eed
updated_at: '2026-09-14T01:34:30Z'
---

# AntonOsika/gpt-engineer/README.md @ a90fcd543eed

<!-- rcw:begin owner=source:src_62b30ea94d5059c1b08b6969e830ff42 block=evidence -->
- Installing gpt-engineer provides a `bench` binary for benchmarking custom agent implementations against public datasets, currently APPS and MBPP, with a separate template repo for getting started. [@claim:clm_094948b95144e1107865d19360c242ecb9ccd936647da6c0f8e4eb6bc90352aa]
- Python 3.10-3.12 is actively supported; versions 0.2.6 and earlier were the last to support Python 3.8-3.9. [@claim:clm_2cfe8e325151f496686c94c162a14084655b1b44963d0b6b392ee32cb04cad02]
- Vision-capable models can receive image inputs via an image directory flag, with the model name given as the second CLI argument, e.g. gpt-4-vision-preview. [@claim:clm_739a2fc9f068a38de9d1ba38d30b4873cb18f04fbb9874ee9d045e3c0b82cf72]
- The tool installs via `python -m pip install gpt-engineer` for stable releases; development setup uses git clone plus poetry install and `poetry shell`. [@claim:clm_7b7485ee33859e9e4cf8a6810cf5680be5446fcd66c8f8c598d8fbaa45b7581b]
- The CLI accepts a `--use-custom-preprompts` flag to override the built-in preprompts folder, letting users change the agent's identity and persistence across projects. [@claim:clm_7fb1ce9c2372ca48d49429bda813c5194b82ca1ec9789c76b75abc9c67ed9b4e]
- Users run the `gpte` CLI against a project directory containing an extension-less `prompt` file with natural-language instructions, e.g. `gpte projects/my-new-project`. [@claim:clm_82e2af3d3111cbb96cccccf372b8bbbfd0f29288e75324950f9fbe9008ac19d8]
- Improving existing code is done by placing a `prompt` file in the target code folder and running `gpte <project_dir> -i`. [@claim:clm_8859ccaa32842be75d6a1ef25c537b346822d1fa8949e105c027776d2330b3c7]
- By default the tool supports OpenAI models via the OpenAI or Azure OpenAI APIs and Anthropic models; open-source models like WizardCoder require extra setup, and API keys are configured via env var or .env file. [@claim:clm_a8680023473091ec4f8a64ce36add12c92ae2387744261c90908877e9c73226a]
- The project positions itself as a code-generation experimentation platform where users specify software in natural language, watch AI write and execute code, and request improvements. [@claim:clm_c49cb0e45504806921065f995a962f4dfe65e6d0687895f86627e7ad5f375d40]
<!-- rcw:end owner=source:src_62b30ea94d5059c1b08b6969e830ff42 block=evidence -->

## Researcher notes

