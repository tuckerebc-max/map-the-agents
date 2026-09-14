# md-ashraful-pramanik/mapcoder -- full detail

[Back to orientation](mapcoder.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/md-ashraful-pramanik/mapcoder/c87e6d914d196e12fa2b144882122459a4b98007/2850d7b1842d8acf.json](../../../wiki/dossiers/md-ashraful-pramanik/mapcoder/c87e6d914d196e12fa2b144882122459a4b98007/2850d7b1842d8acf.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] MapCoder uses four LLM agents mirroring the human programming cycle: retrieval, planning, code generation, and debugging. -- evidence: [README.md#L27-L28](https://github.com/Md-Ashraful-Pramanik/MapCoder/blob/c87e6d914d196e12fa2b144882122459a4b98007/README.md#L27-L28), [README.md#L22-L23](https://github.com/Md-Ashraful-Pramanik/MapCoder/blob/c87e6d914d196e12fa2b144882122459a4b98007/README.md#L22-L23) (`clm_65bb3e9986beb8e87c4acd126a61f3302b1e8e832d41cb4b8b06ea1cd3aa514f`)
- [observation/documented] The coding agent turns a plan into code, tests it on sample I/O, hands failures to the debugging agent, and otherwise predicts it as the final solution. -- evidence: [README.md#L35-L35](https://github.com/Md-Ashraful-Pramanik/MapCoder/blob/c87e6d914d196e12fa2b144882122459a4b98007/README.md#L35-L35) (`clm_2a37229610a9c1c2f8a435551b8748ef0ace7f16091e4786c83f6f1cd2a4bfd2`)

## design-choices (3 claim(s))

- [observation/documented] The retrieval agent generates k user-defined similar problems using the LLM itself, without manual crafting or external retrieval models. -- evidence: [README.md#L31-L31](https://github.com/Md-Ashraful-Pramanik/MapCoder/blob/c87e6d914d196e12fa2b144882122459a4b98007/README.md#L31-L31) (`clm_dfcc1581b76db3195dc0ae2686f8f7cbd82de3e7cd383edb9faabec05e0005f7`)
- [observation/documented] MapCoder features an adaptive agent traversal schema that dynamically routes among agents, e.g. iteratively fixing bugs, rather than a fixed pipeline. -- evidence: [README.md#L27-L28](https://github.com/Md-Ashraful-Pramanik/MapCoder/blob/c87e6d914d196e12fa2b144882122459a4b98007/README.md#L27-L28) (`clm_c627d387a63a52867a02a44c4075f93d34f10b7af632d43a8b8d1594783151ae`)
- [observation/documented] The debugging agent is supplemented with plans from the planning agent, analogous to humans cross-checking their plan while fixing bugs. -- evidence: [README.md#L37-L37](https://github.com/Md-Ashraful-Pramanik/MapCoder/blob/c87e6d914d196e12fa2b144882122459a4b98007/README.md#L37-L37) (`clm_371fa80e9df7d9688d4d16b159bb446cd67e5b3098ff6523d1907dfbcf6791bf`)

## workflows (2 claim(s))

- [observation/documented] Setup involves cloning the repo, creating a conda or python virtual environment, installing requirements.txt, and configuring a .env file from an example. -- evidence: [README.md#L73-L73](https://github.com/Md-Ashraful-Pramanik/MapCoder/blob/c87e6d914d196e12fa2b144882122459a4b98007/README.md#L73-L73), [README.md#L63-L66](https://github.com/Md-Ashraful-Pramanik/MapCoder/blob/c87e6d914d196e12fa2b144882122459a4b98007/README.md#L63-L66), [README.md#L68-L71](https://github.com/Md-Ashraful-Pramanik/MapCoder/blob/c87e6d914d196e12fa2b144882122459a4b98007/README.md#L68-L71) (`clm_40504d8871a31ad1ecbfc1a4487073194aed3c3dcc79d8f1cb096254c8814d1c`)
- [observation/documented] Running competitive datasets requires setting up ExecEval in a Docker container on port 5000, with configuration in src/evaluations/api_comm.py. -- evidence: [README.md#L85-L85](https://github.com/Md-Ashraful-Pramanik/MapCoder/blob/c87e6d914d196e12fa2b144882122459a4b98007/README.md#L85-L85) (`clm_62e8f3b06aa27555d282fd737b09c62952d0e587b15c70eefb1707925ae4e213`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] The CLI entry point is src/main.py with options such as --model, --dataset, and --strategy (e.g. ChatGPT, HumanEval, MapCoder). -- evidence: [README.md#L80-L83](https://github.com/Md-Ashraful-Pramanik/MapCoder/blob/c87e6d914d196e12fa2b144882122459a4b98007/README.md#L80-L83), [README.md#L75-L78](https://github.com/Md-Ashraful-Pramanik/MapCoder/blob/c87e6d914d196e12fa2b144882122459a4b98007/README.md#L75-L78) (`clm_ff8558af8873181748d1d3df15b05b0d968c75e813dbbd75359ee99e04bc632d`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (1 claim(s))

- [observation/documented] Reported pass@1 results include HumanEval 93.9%, MBPP 83.1%, APPS 22.0%, CodeContests 28.5%, and xCodeEval 45.3%. -- evidence: [README.md#L44-L58](https://github.com/Md-Ashraful-Pramanik/MapCoder/blob/c87e6d914d196e12fa2b144882122459a4b98007/README.md#L44-L58), [README.md#L22-L23](https://github.com/Md-Ashraful-Pramanik/MapCoder/blob/c87e6d914d196e12fa2b144882122459a4b98007/README.md#L22-L23) (`clm_6e57b8870ee84ed513f5c2ef1d953f2b15e2f7aa7676beeb4c8fa29b00eb85f4`)

## dependencies (1 claim(s))

- [observation/documented] Dependencies include openai, google-generativeai, tiktoken, gensim, accelerate, and others listed in requirements.txt. -- evidence: [requirements.txt#L2-L15](https://github.com/Md-Ashraful-Pramanik/MapCoder/blob/c87e6d914d196e12fa2b144882122459a4b98007/requirements.txt#L2-L15) (`clm_34376950ec19436ab95f6fd7ee6e5ccf7856c724f4113d9bb98df83474357519`)

## limitations (1 claim(s))

- [observation/documented] The maintainers state this repository will no longer be maintained, pointing users to an improved model called CodeSIM. -- evidence: [README.md#L15-L18](https://github.com/Md-Ashraful-Pramanik/MapCoder/blob/c87e6d914d196e12fa2b144882122459a4b98007/README.md#L15-L18) (`clm_ac44dfdac7f8f2b421de1ee901045777f8432fc23e21a3c6939818cc5bfd04a8`)

## relevance (1 claim(s))

- [observation/documented] The work was accepted at ACL 2024, released under the MIT License, and has an associated arXiv paper (2405.11403). -- evidence: [README.md#L15-L18](https://github.com/Md-Ashraful-Pramanik/MapCoder/blob/c87e6d914d196e12fa2b144882122459a4b98007/README.md#L15-L18), [README.md#L8-L12](https://github.com/Md-Ashraful-Pramanik/MapCoder/blob/c87e6d914d196e12fa2b144882122459a4b98007/README.md#L8-L12), [README.md#L89-L96](https://github.com/Md-Ashraful-Pramanik/MapCoder/blob/c87e6d914d196e12fa2b144882122459a4b98007/README.md#L89-L96) (`clm_408633720bddb37404dbffb772876b50b49b92b1133c4eaf6d2d6952c134e1c8`)

