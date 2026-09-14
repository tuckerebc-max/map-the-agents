# foundationagents/metagpt -- full detail

[Back to orientation](metagpt.md)

## Origins

- github-rename-resolution
- alltheagents.org-backing
- github-verified-rename

## Projects

- navy-yard
- Observatory

Full evidence record (JSON): [wiki/dossiers/foundationagents/metagpt/11cdf466d042aece04fc6cfd13b28e1a70341b1f/32a1dc0084829e9e.json](../../../wiki/dossiers/foundationagents/metagpt/11cdf466d042aece04fc6cfd13b28e1a70341b1f/32a1dc0084829e9e.json)

## specifications (1 claim(s))

- [observation/documented] MetaGPT takes a one-line requirement as input and outputs artifacts such as user stories, competitive analysis, requirements, data structures, APIs, and documents. -- evidence: [README.md#L42-L44](https://github.com/FoundationAgents/MetaGPT/blob/11cdf466d042aece04fc6cfd13b28e1a70341b1f/README.md#L42-L44) (`clm_ab15aab1a20e5dcd259cc6632555f753b00a4986a5bfbb32e8518c12b3b71e87`)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (1 claim(s))

- [observation/documented] Internally the system models a software company with product manager, architect, project manager, and engineer roles orchestrated via SOPs, summarized by the philosophy 'Code = SOP(Team)'. -- evidence: [README.md#L42-L44](https://github.com/FoundationAgents/MetaGPT/blob/11cdf466d042aece04fc6cfd13b28e1a70341b1f/README.md#L42-L44) (`clm_ee0bf87e7958b9e6e6c4768e142b2f5813035055eb90a93bdff5f15f4500486d`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (5 claim(s))

- [observation/documented] The product exposes a CLI: running `metagpt "Create a 2048 game"` generates a repository in ./workspace. -- evidence: [README.md#L90-L92](https://github.com/FoundationAgents/MetaGPT/blob/11cdf466d042aece04fc6cfd13b28e1a70341b1f/README.md#L90-L92), [README.md#L88-L88](https://github.com/FoundationAgents/MetaGPT/blob/11cdf466d042aece04fc6cfd13b28e1a70341b1f/README.md#L88-L88) (`clm_963905395c9f1dde28c904350d4c6a38f68edea0b737bba4ddb5301db8e2c355`)
- [observation/documented] MetaGPT can also be used as a Python library via `metagpt.software_company.generate_repo`, which returns a ProjectRepo whose structure can be printed. -- evidence: [README.md#L100-L102](https://github.com/FoundationAgents/MetaGPT/blob/11cdf466d042aece04fc6cfd13b28e1a70341b1f/README.md#L100-L102), [README.md#L96-L98](https://github.com/FoundationAgents/MetaGPT/blob/11cdf466d042aece04fc6cfd13b28e1a70341b1f/README.md#L96-L98), [README.md#L94-L94](https://github.com/FoundationAgents/MetaGPT/blob/11cdf466d042aece04fc6cfd13b28e1a70341b1f/README.md#L94-L94) (`clm_cd843948ea7ceb4160ab60df2728d0dd571866c25d1973d08b0811a7719b102c`)
- [observation/documented] A DataInterpreter role (metagpt.roles.di.data_interpreter) can be run asynchronously with a natural-language task such as analyzing the sklearn Iris dataset with a plot. -- evidence: [README.md#L110-L112](https://github.com/FoundationAgents/MetaGPT/blob/11cdf466d042aece04fc6cfd13b28e1a70341b1f/README.md#L110-L112), [README.md#L104-L104](https://github.com/FoundationAgents/MetaGPT/blob/11cdf466d042aece04fc6cfd13b28e1a70341b1f/README.md#L104-L104), [README.md#L106-L108](https://github.com/FoundationAgents/MetaGPT/blob/11cdf466d042aece04fc6cfd13b28e1a70341b1f/README.md#L106-L108) (`clm_0e7551934ea117c3f98cd03e416d2af2727ac1efb137fa221ab5c642eabc6cf3`)
- [observation/documented] Configuration is initialized with `metagpt --init-config`, creating ~/.metagpt/config2.yaml which users edit; the example config supports api_type values like openai, azure, ollama, and groq with model, base_url, and api_key fields. -- evidence: [README.md#L78-L84](https://github.com/FoundationAgents/MetaGPT/blob/11cdf466d042aece04fc6cfd13b28e1a70341b1f/README.md#L78-L84), [README.md#L73-L74](https://github.com/FoundationAgents/MetaGPT/blob/11cdf466d042aece04fc6cfd13b28e1a70341b1f/README.md#L73-L74), [README.md#L76-L76](https://github.com/FoundationAgents/MetaGPT/blob/11cdf466d042aece04fc6cfd13b28e1a70341b1f/README.md#L76-L76), [README.md#L70-L71](https://github.com/FoundationAgents/MetaGPT/blob/11cdf466d042aece04fc6cfd13b28e1a70341b1f/README.md#L70-L71) (`clm_a064ad78d4e9c3be24b97956392ef696a38d8730b5120f2c65f0a97519f8795e`)
- [observation/documented] A Docker workflow is documented: pulling metagpt/metagpt:latest, mounting config2.yaml and a workspace directory, and running a prompt inside the container. -- evidence: [docs/README_CN.md#L56-L59](https://github.com/FoundationAgents/MetaGPT/blob/11cdf466d042aece04fc6cfd13b28e1a70341b1f/docs/README_CN.md#L56-L59), [docs/README_CN.md#L62-L68](https://github.com/FoundationAgents/MetaGPT/blob/11cdf466d042aece04fc6cfd13b28e1a70341b1f/docs/README_CN.md#L62-L68) (`clm_99fdb809afa7d3d4c89c3bea16d5a9c2c2c284c8673c4817c91b0fce6af9cecc`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The README requires Python 3.9 or later but below 3.12, and instructs installing node and pnpm before actual use; installation is possible via pip, an editable git clone, or Docker. -- evidence: [README.md#L57-L58](https://github.com/FoundationAgents/MetaGPT/blob/11cdf466d042aece04fc6cfd13b28e1a70341b1f/README.md#L57-L58), [README.md#L65-L66](https://github.com/FoundationAgents/MetaGPT/blob/11cdf466d042aece04fc6cfd13b28e1a70341b1f/README.md#L65-L66), [README.md#L54-L55](https://github.com/FoundationAgents/MetaGPT/blob/11cdf466d042aece04fc6cfd13b28e1a70341b1f/README.md#L54-L55), [README.md#L63-L63](https://github.com/FoundationAgents/MetaGPT/blob/11cdf466d042aece04fc6cfd13b28e1a70341b1f/README.md#L63-L63) (`clm_0b8736027d5d31874c6dfd5bbfc7c6ef3ad538b94d632943ad10beb984404265`)

## limitations (2 claim(s))

- [observation/documented] Per the FAQ, incremental/differential updates (--inc with project path or name), multiple programming languages, and multiple natural languages are supported only in experimental versions. -- evidence: [docs/FAQ-EN.md#L40-L93](https://github.com/FoundationAgents/MetaGPT/blob/11cdf466d042aece04fc6cfd13b28e1a70341b1f/docs/FAQ-EN.md#L40-L93) (`clm_dd704caf7d906bc1ffa041557c9430b2f1386eeb70ac695f53c47a609aa35ed4`)
- [observation/documented] The FAQ states no quantitative success-rate analysis has been done, though gpt-4-turbo code generation reportedly succeeds significantly more often than gpt-3.5-turbo, and loading existing large projects is described as very difficult. -- evidence: [docs/FAQ-EN.md#L40-L93](https://github.com/FoundationAgents/MetaGPT/blob/11cdf466d042aece04fc6cfd13b28e1a70341b1f/docs/FAQ-EN.md#L40-L93) (`clm_e0d51138e9165e81452f9a7dbc0964e6fa601bb1b272c45eca158b60eb7bc63d`)

## relevance (1 claim(s))

- [observation/documented] The project is MIT-licensed, open-sourced June 2023, and its ICLR 2024 paper on multi-agent collaborative meta programming is cited alongside related work such as AFlow, SPO, AOT, FACT, and SELA. -- evidence: [docs/NEWS.md#L3-L3](https://github.com/FoundationAgents/MetaGPT/blob/11cdf466d042aece04fc6cfd13b28e1a70341b1f/docs/NEWS.md#L3-L3), [README.md#L167-L175](https://github.com/FoundationAgents/MetaGPT/blob/11cdf466d042aece04fc6cfd13b28e1a70341b1f/README.md#L167-L175), [README.md#L16-L20](https://github.com/FoundationAgents/MetaGPT/blob/11cdf466d042aece04fc6cfd13b28e1a70341b1f/README.md#L16-L20), [docs/ACADEMIC_WORK.md#L10-L60](https://github.com/FoundationAgents/MetaGPT/blob/11cdf466d042aece04fc6cfd13b28e1a70341b1f/docs/ACADEMIC_WORK.md#L10-L60), [docs/NEWS.md#L20-L20](https://github.com/FoundationAgents/MetaGPT/blob/11cdf466d042aece04fc6cfd13b28e1a70341b1f/docs/NEWS.md#L20-L20) (`clm_cf7a281f5f1048638a9e09ddbfdeb3c9e6af2d3bb23a8ca96f1db8ef5432c36c`)

