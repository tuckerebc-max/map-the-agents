# antonosika/gpt-engineer -- full detail

[Back to orientation](gpt-engineer.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/antonosika/gpt-engineer/a90fcd543eedcc0ff2c34561bc0785d2ba83c47e/2f719d3003f5982a.json](../../../wiki/dossiers/antonosika/gpt-engineer/a90fcd543eedcc0ff2c34561bc0785d2ba83c47e/2f719d3003f5982a.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (1 claim(s))

- [observation/documented] Optional usage-data collection is opt-in: it occurs only when a consent file named .gpte_consent exists in the gpt-engineer directory. -- evidence: [TERMS_OF_USE.md#L11-L11](https://github.com/AntonOsika/gpt-engineer/blob/a90fcd543eedcc0ff2c34561bc0785d2ba83c47e/TERMS_OF_USE.md#L11-L11) (`clm_d61dbd155698026aeeea21bb1fc1ef8781a06acf5fd60ff08ee48c9d13bdf846`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributors can propose roadmap designs as Google Docs in Discord, submit PRs for roadmap items, or review others' PRs, with volunteer work acknowledged. -- evidence: [ROADMAP.md#L27-L29](https://github.com/AntonOsika/gpt-engineer/blob/a90fcd543eedcc0ff2c34561bc0785d2ba83c47e/ROADMAP.md#L27-L29), [ROADMAP.md#L31-L31](https://github.com/AntonOsika/gpt-engineer/blob/a90fcd543eedcc0ff2c34561bc0785d2ba83c47e/ROADMAP.md#L31-L31) (`clm_5fd829e063db32cbc86e594f718a09524b0aab69c0dcb2a86f763a4c6a4a3e5f`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (4 claim(s))

- [observation/documented] Users run the `gpte` CLI against a project directory containing an extension-less `prompt` file with natural-language instructions, e.g. `gpte projects/my-new-project`. -- evidence: [README.md#L57-L60](https://github.com/AntonOsika/gpt-engineer/blob/a90fcd543eedcc0ff2c34561bc0785d2ba83c47e/README.md#L57-L60) (`clm_82e2af3d3111cbb96cccccf372b8bbbfd0f29288e75324950f9fbe9008ac19d8`)
- [observation/documented] Improving existing code is done by placing a `prompt` file in the target code folder and running `gpte <project_dir> -i`. -- evidence: [README.md#L63-L66](https://github.com/AntonOsika/gpt-engineer/blob/a90fcd543eedcc0ff2c34561bc0785d2ba83c47e/README.md#L63-L66) (`clm_8859ccaa32842be75d6a1ef25c537b346822d1fa8949e105c027776d2330b3c7`)
- [observation/documented] The CLI accepts a `--use-custom-preprompts` flag to override the built-in preprompts folder, letting users change the agent's identity and persistence across projects. -- evidence: [README.md#L95-L95](https://github.com/AntonOsika/gpt-engineer/blob/a90fcd543eedcc0ff2c34561bc0785d2ba83c47e/README.md#L95-L95), [README.md#L93-L93](https://github.com/AntonOsika/gpt-engineer/blob/a90fcd543eedcc0ff2c34561bc0785d2ba83c47e/README.md#L93-L93) (`clm_7fb1ce9c2372ca48d49429bda813c5194b82ca1ec9789c76b75abc9c67ed9b4e`)
- [observation/documented] Vision-capable models can receive image inputs via an image directory flag, with the model name given as the second CLI argument, e.g. gpt-4-vision-preview. -- evidence: [README.md#L99-L99](https://github.com/AntonOsika/gpt-engineer/blob/a90fcd543eedcc0ff2c34561bc0785d2ba83c47e/README.md#L99-L99), [README.md#L101-L101](https://github.com/AntonOsika/gpt-engineer/blob/a90fcd543eedcc0ff2c34561bc0785d2ba83c47e/README.md#L101-L101) (`clm_739a2fc9f068a38de9d1ba38d30b4873cb18f04fbb9874ee9d045e3c0b82cf72`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (1 claim(s))

- [observation/documented] Installing gpt-engineer provides a `bench` binary for benchmarking custom agent implementations against public datasets, currently APPS and MBPP, with a separate template repo for getting started. -- evidence: [README.md#L69-L73](https://github.com/AntonOsika/gpt-engineer/blob/a90fcd543eedcc0ff2c34561bc0785d2ba83c47e/README.md#L69-L73) (`clm_094948b95144e1107865d19360c242ecb9ccd936647da6c0f8e4eb6bc90352aa`)

## dependencies (3 claim(s))

- [observation/documented] The tool installs via `python -m pip install gpt-engineer` for stable releases; development setup uses git clone plus poetry install and `poetry shell`. -- evidence: [README.md#L30-L34](https://github.com/AntonOsika/gpt-engineer/blob/a90fcd543eedcc0ff2c34561bc0785d2ba83c47e/README.md#L30-L34), [README.md#L28-L28](https://github.com/AntonOsika/gpt-engineer/blob/a90fcd543eedcc0ff2c34561bc0785d2ba83c47e/README.md#L28-L28) (`clm_7b7485ee33859e9e4cf8a6810cf5680be5446fcd66c8f8c598d8fbaa45b7581b`)
- [observation/documented] Python 3.10-3.12 is actively supported; versions 0.2.6 and earlier were the last to support Python 3.8-3.9. -- evidence: [README.md#L36-L36](https://github.com/AntonOsika/gpt-engineer/blob/a90fcd543eedcc0ff2c34561bc0785d2ba83c47e/README.md#L36-L36) (`clm_2cfe8e325151f496686c94c162a14084655b1b44963d0b6b392ee32cb04cad02`)
- [observation/documented] By default the tool supports OpenAI models via the OpenAI or Azure OpenAI APIs and Anthropic models; open-source models like WizardCoder require extra setup, and API keys are configured via env var or .env file. -- evidence: [README.md#L107-L107](https://github.com/AntonOsika/gpt-engineer/blob/a90fcd543eedcc0ff2c34561bc0785d2ba83c47e/README.md#L107-L107), [README.md#L105-L105](https://github.com/AntonOsika/gpt-engineer/blob/a90fcd543eedcc0ff2c34561bc0785d2ba83c47e/README.md#L105-L105), [README.md#L40-L47](https://github.com/AntonOsika/gpt-engineer/blob/a90fcd543eedcc0ff2c34561bc0785d2ba83c47e/README.md#L40-L47) (`clm_a8680023473091ec4f8a64ce36add12c92ae2387744261c90908877e9c73226a`)

## limitations (1 claim(s))

- [observation/documented] The project describes itself as an experimental application provided as-is without warranty, and warns that GPT-4 usage can be expensive, advising users to monitor their own API costs. -- evidence: [DISCLAIMER.md#L3-L3](https://github.com/AntonOsika/gpt-engineer/blob/a90fcd543eedcc0ff2c34561bc0785d2ba83c47e/DISCLAIMER.md#L3-L3), [DISCLAIMER.md#L7-L7](https://github.com/AntonOsika/gpt-engineer/blob/a90fcd543eedcc0ff2c34561bc0785d2ba83c47e/DISCLAIMER.md#L7-L7) (`clm_7ab7053d239ab35d4273036a7109ca202039f6f9ae471768f9e67632aee98e3f`)

## relevance (1 claim(s))

- [observation/documented] The project positions itself as a code-generation experimentation platform where users specify software in natural language, watch AI write and execute code, and request improvements. -- evidence: [README.md#L17-L20](https://github.com/AntonOsika/gpt-engineer/blob/a90fcd543eedcc0ff2c34561bc0785d2ba83c47e/README.md#L17-L20), [README.md#L10-L10](https://github.com/AntonOsika/gpt-engineer/blob/a90fcd543eedcc0ff2c34561bc0785d2ba83c47e/README.md#L10-L10) (`clm_c49cb0e45504806921065f995a962f4dfe65e6d0687895f86627e7ad5f375d40`)

