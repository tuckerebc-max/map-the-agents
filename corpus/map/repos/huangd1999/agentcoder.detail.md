# huangd1999/agentcoder -- full detail

[Back to orientation](agentcoder.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/huangd1999/agentcoder/d8538d63675c2b805855e6deb7ddc39fefb5723d/7625ad548ee3dbae.json](../../../wiki/dossiers/huangd1999/agentcoder/d8538d63675c2b805855e6deb7ddc39fefb5723d/7625ad548ee3dbae.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The framework comprises three specialized agents: a programmer agent, a test designer agent, and a test executor agent that collaborate in an iterative feedback loop. -- evidence: [README.md#L3-L3](https://github.com/huangd1999/AgentCoder/blob/d8538d63675c2b805855e6deb7ddc39fefb5723d/README.md#L3-L3) (`clm_e5c8550fce86c7adf371cbb6154774307b874fdd9fa5bbe4b647947d6c7a0927`)

## design-choices (2 claim(s))

- [observation/documented] The test designer agent generates diverse, objective test cases independently of code generation, and the test executor runs them against generated code to feed refinement feedback. -- evidence: [README.md#L7-L10](https://github.com/huangd1999/AgentCoder/blob/d8538d63675c2b805855e6deb7ddc39fefb5723d/README.md#L7-L10) (`clm_a984b8679dfd25a98f0630720e927103217f8f80664791969211887568273126`)
- [observation/documented] The README describes a modular structure intended to allow easy integration with advanced models and future enhancements. -- evidence: [README.md#L7-L10](https://github.com/huangd1999/AgentCoder/blob/d8538d63675c2b805855e6deb7ddc39fefb5723d/README.md#L7-L10) (`clm_284070a83e09564b6e42041f2eb8c98e3a2da030488b8a9754a58fc49a5b0843`)

## workflows (2 claim(s))

- [observation/documented] Installation involves cloning the repo (plus CodeGeeX), running pip install -r requirements.txt, and adding an API key to a .env file. -- evidence: [README.md#L22-L25](https://github.com/huangd1999/AgentCoder/blob/d8538d63675c2b805855e6deb7ddc39fefb5723d/README.md#L22-L25), [README.md#L14-L20](https://github.com/huangd1999/AgentCoder/blob/d8538d63675c2b805855e6deb7ddc39fefb5723d/README.md#L14-L20), [README.md#L27-L30](https://github.com/huangd1999/AgentCoder/blob/d8538d63675c2b805855e6deb7ddc39fefb5723d/README.md#L27-L30) (`clm_3f1c514d0b3fa75b44483abf057b981bcd836ccd2cf26766bcfc40edd8e00b01`)
- [observation/documented] The README invites contributions via GitHub issues or pull requests. -- evidence: [README.md#L61-L61](https://github.com/huangd1999/AgentCoder/blob/d8538d63675c2b805855e6deb7ddc39fefb5723d/README.md#L61-L61) (`clm_ff2f9c04f54d2c8ee8cc2ff154021ee32f55c1ac77f304d0ec986bb4f455827e`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] Usage is via per-benchmark scripts: programmer_[humaneval/mbpp].py, test_designer_[humaneval/mbpp].py, and test_executor_[humaneval/mbpp].py. -- evidence: [README.md#L36-L40](https://github.com/huangd1999/AgentCoder/blob/d8538d63675c2b805855e6deb7ddc39fefb5723d/README.md#L36-L40), [README.md#L44-L48](https://github.com/huangd1999/AgentCoder/blob/d8538d63675c2b805855e6deb7ddc39fefb5723d/README.md#L44-L48), [README.md#L52-L56](https://github.com/huangd1999/AgentCoder/blob/d8538d63675c2b805855e6deb7ddc39fefb5723d/README.md#L52-L56) (`clm_f7ea061b51274c450114992125839cc6e3c2fc9c390351683b7f12f600ed7f1a`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (1 claim(s))

- [inference/documented] Script names referencing humaneval and mbpp suggest the framework targets the HumanEval and MBPP code generation benchmarks. -- evidence: [README.md#L36-L40](https://github.com/huangd1999/AgentCoder/blob/d8538d63675c2b805855e6deb7ddc39fefb5723d/README.md#L36-L40), [README.md#L44-L48](https://github.com/huangd1999/AgentCoder/blob/d8538d63675c2b805855e6deb7ddc39fefb5723d/README.md#L44-L48), [README.md#L52-L56](https://github.com/huangd1999/AgentCoder/blob/d8538d63675c2b805855e6deb7ddc39fefb5723d/README.md#L52-L56) (`clm_3030facb7d9bf638d7b49be9b44400608dd4e490b6224cd2d56f1c2eae58810b`)

## dependencies (3 claim(s))

- [observation/documented] requirements.txt pins datasets 3.3.1, openai 0.28.0, and python-dotenv 1.0.1. -- evidence: [requirements.txt#L1-L3](https://github.com/huangd1999/AgentCoder/blob/d8538d63675c2b805855e6deb7ddc39fefb5723d/requirements.txt#L1-L3) (`clm_b52b7c9f5619bd89750baf9e0050bd8d0cbf691cba1e4408b69572644d279218`)
- [observation/documented] The project requires an OpenAI or similar third-party provider API key, configured in a .env file as OPENAI_API_KEY. -- evidence: [README.md#L14-L20](https://github.com/huangd1999/AgentCoder/blob/d8538d63675c2b805855e6deb7ddc39fefb5723d/README.md#L14-L20), [README.md#L27-L30](https://github.com/huangd1999/AgentCoder/blob/d8538d63675c2b805855e6deb7ddc39fefb5723d/README.md#L27-L30) (`clm_e3d407d2626e6340a05d872938c80062b9768ea340e8e91bd0e8d53f6a49d62a`)
- [inference/documented] The installation instructions clone the THUDM/CodeGeeX repository, suggesting CodeGeeX is used as part of the setup, though its role is not stated in the evidence. -- evidence: [README.md#L14-L20](https://github.com/huangd1999/AgentCoder/blob/d8538d63675c2b805855e6deb7ddc39fefb5723d/README.md#L14-L20) (`clm_026c388a6cfaaa27139d753318104c6fae5ead1457fbb38a2c2bf15900aebc07`)

## limitations (1 claim(s))

- [observation/documented] The project is released under the MIT License and acknowledges AIOHUB for funding and support. -- evidence: [README.md#L65-L65](https://github.com/huangd1999/AgentCoder/blob/d8538d63675c2b805855e6deb7ddc39fefb5723d/README.md#L65-L65), [README.md#L69-L69](https://github.com/huangd1999/AgentCoder/blob/d8538d63675c2b805855e6deb7ddc39fefb5723d/README.md#L69-L69) (`clm_2f11c1c8f8f8a8a785bd81091710e8369689d3e6de1c56404fd55843744cd04d`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

