---
access: public
aliases: []
claim_ids:
- clm_0b8736027d5d31874c6dfd5bbfc7c6ef3ad538b94d632943ad10beb984404265
- clm_0e7551934ea117c3f98cd03e416d2af2727ac1efb137fa221ab5c642eabc6cf3
- clm_963905395c9f1dde28c904350d4c6a38f68edea0b737bba4ddb5301db8e2c355
- clm_a064ad78d4e9c3be24b97956392ef696a38d8730b5120f2c65f0a97519f8795e
- clm_ab15aab1a20e5dcd259cc6632555f753b00a4986a5bfbb32e8518c12b3b71e87
- clm_cd843948ea7ceb4160ab60df2728d0dd571866c25d1973d08b0811a7719b102c
- clm_cf7a281f5f1048638a9e09ddbfdeb3c9e6af2d3bb23a8ca96f1db8ef5432c36c
- clm_ee0bf87e7958b9e6e6c4768e142b2f5813035055eb90a93bdff5f15f4500486d
maturity: draft
page_id: pg_25aeb63fdd4e52ed82854d0db27ffe67
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_de73073561d453b4aaa21d8d677387a3
title: FoundationAgents/MetaGPT/README.md @ 11cdf466d042
updated_at: '2026-09-14T03:51:29Z'
---

# FoundationAgents/MetaGPT/README.md @ 11cdf466d042

<!-- rcw:begin owner=source:src_de73073561d453b4aaa21d8d677387a3 block=evidence -->
- The README requires Python 3.9 or later but below 3.12, and instructs installing node and pnpm before actual use; installation is possible via pip, an editable git clone, or Docker. [@claim:clm_0b8736027d5d31874c6dfd5bbfc7c6ef3ad538b94d632943ad10beb984404265]
- A DataInterpreter role (metagpt.roles.di.data_interpreter) can be run asynchronously with a natural-language task such as analyzing the sklearn Iris dataset with a plot. [@claim:clm_0e7551934ea117c3f98cd03e416d2af2727ac1efb137fa221ab5c642eabc6cf3]
- The product exposes a CLI: running `metagpt "Create a 2048 game"` generates a repository in ./workspace. [@claim:clm_963905395c9f1dde28c904350d4c6a38f68edea0b737bba4ddb5301db8e2c355]
- Configuration is initialized with `metagpt --init-config`, creating ~/.metagpt/config2.yaml which users edit; the example config supports api_type values like openai, azure, ollama, and groq with model, base_url, and api_key fields. [@claim:clm_a064ad78d4e9c3be24b97956392ef696a38d8730b5120f2c65f0a97519f8795e]
- MetaGPT takes a one-line requirement as input and outputs artifacts such as user stories, competitive analysis, requirements, data structures, APIs, and documents. [@claim:clm_ab15aab1a20e5dcd259cc6632555f753b00a4986a5bfbb32e8518c12b3b71e87]
- MetaGPT can also be used as a Python library via `metagpt.software_company.generate_repo`, which returns a ProjectRepo whose structure can be printed. [@claim:clm_cd843948ea7ceb4160ab60df2728d0dd571866c25d1973d08b0811a7719b102c]
- The project is MIT-licensed, open-sourced June 2023, and its ICLR 2024 paper on multi-agent collaborative meta programming is cited alongside related work such as AFlow, SPO, AOT, FACT, and SELA. [@claim:clm_cf7a281f5f1048638a9e09ddbfdeb3c9e6af2d3bb23a8ca96f1db8ef5432c36c]
- Internally the system models a software company with product manager, architect, project manager, and engineer roles orchestrated via SOPs, summarized by the philosophy 'Code = SOP(Team)'. [@claim:clm_ee0bf87e7958b9e6e6c4768e142b2f5813035055eb90a93bdff5f15f4500486d]
<!-- rcw:end owner=source:src_de73073561d453b4aaa21d8d677387a3 block=evidence -->

## Researcher notes

