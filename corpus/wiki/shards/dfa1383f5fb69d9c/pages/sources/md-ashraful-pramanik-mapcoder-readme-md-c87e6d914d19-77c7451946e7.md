---
access: public
aliases: []
claim_ids:
- clm_2a37229610a9c1c2f8a435551b8748ef0ace7f16091e4786c83f6f1cd2a4bfd2
- clm_371fa80e9df7d9688d4d16b159bb446cd67e5b3098ff6523d1907dfbcf6791bf
- clm_40504d8871a31ad1ecbfc1a4487073194aed3c3dcc79d8f1cb096254c8814d1c
- clm_408633720bddb37404dbffb772876b50b49b92b1133c4eaf6d2d6952c134e1c8
- clm_62e8f3b06aa27555d282fd737b09c62952d0e587b15c70eefb1707925ae4e213
- clm_65bb3e9986beb8e87c4acd126a61f3302b1e8e832d41cb4b8b06ea1cd3aa514f
- clm_6e57b8870ee84ed513f5c2ef1d953f2b15e2f7aa7676beeb4c8fa29b00eb85f4
- clm_ac44dfdac7f8f2b421de1ee901045777f8432fc23e21a3c6939818cc5bfd04a8
- clm_c627d387a63a52867a02a44c4075f93d34f10b7af632d43a8b8d1594783151ae
- clm_dfcc1581b76db3195dc0ae2686f8f7cbd82de3e7cd383edb9faabec05e0005f7
- clm_ff8558af8873181748d1d3df15b05b0d968c75e813dbbd75359ee99e04bc632d
maturity: draft
page_id: pg_ff691da5c70c5ebdbc4177c7451946e7
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_c6aafec9faef522795fb398a0f98c078
title: Md-Ashraful-Pramanik/MapCoder/README.md @ c87e6d914d19
updated_at: '2026-09-14T02:17:46Z'
---

# Md-Ashraful-Pramanik/MapCoder/README.md @ c87e6d914d19

<!-- rcw:begin owner=source:src_c6aafec9faef522795fb398a0f98c078 block=evidence -->
- The coding agent turns a plan into code, tests it on sample I/O, hands failures to the debugging agent, and otherwise predicts it as the final solution. [@claim:clm_2a37229610a9c1c2f8a435551b8748ef0ace7f16091e4786c83f6f1cd2a4bfd2]
- The debugging agent is supplemented with plans from the planning agent, analogous to humans cross-checking their plan while fixing bugs. [@claim:clm_371fa80e9df7d9688d4d16b159bb446cd67e5b3098ff6523d1907dfbcf6791bf]
- Setup involves cloning the repo, creating a conda or python virtual environment, installing requirements.txt, and configuring a .env file from an example. [@claim:clm_40504d8871a31ad1ecbfc1a4487073194aed3c3dcc79d8f1cb096254c8814d1c]
- The work was accepted at ACL 2024, released under the MIT License, and has an associated arXiv paper (2405.11403). [@claim:clm_408633720bddb37404dbffb772876b50b49b92b1133c4eaf6d2d6952c134e1c8]
- Running competitive datasets requires setting up ExecEval in a Docker container on port 5000, with configuration in src/evaluations/api_comm.py. [@claim:clm_62e8f3b06aa27555d282fd737b09c62952d0e587b15c70eefb1707925ae4e213]
- MapCoder uses four LLM agents mirroring the human programming cycle: retrieval, planning, code generation, and debugging. [@claim:clm_65bb3e9986beb8e87c4acd126a61f3302b1e8e832d41cb4b8b06ea1cd3aa514f]
- Reported pass@1 results include HumanEval 93.9%, MBPP 83.1%, APPS 22.0%, CodeContests 28.5%, and xCodeEval 45.3%. [@claim:clm_6e57b8870ee84ed513f5c2ef1d953f2b15e2f7aa7676beeb4c8fa29b00eb85f4]
- The maintainers state this repository will no longer be maintained, pointing users to an improved model called CodeSIM. [@claim:clm_ac44dfdac7f8f2b421de1ee901045777f8432fc23e21a3c6939818cc5bfd04a8]
- MapCoder features an adaptive agent traversal schema that dynamically routes among agents, e.g. iteratively fixing bugs, rather than a fixed pipeline. [@claim:clm_c627d387a63a52867a02a44c4075f93d34f10b7af632d43a8b8d1594783151ae]
- The retrieval agent generates k user-defined similar problems using the LLM itself, without manual crafting or external retrieval models. [@claim:clm_dfcc1581b76db3195dc0ae2686f8f7cbd82de3e7cd383edb9faabec05e0005f7]
- The CLI entry point is src/main.py with options such as --model, --dataset, and --strategy (e.g. ChatGPT, HumanEval, MapCoder). [@claim:clm_ff8558af8873181748d1d3df15b05b0d968c75e813dbbd75359ee99e04bc632d]
<!-- rcw:end owner=source:src_c6aafec9faef522795fb398a0f98c078 block=evidence -->

## Researcher notes

