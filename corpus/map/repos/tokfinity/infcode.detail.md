# tokfinity/infcode -- full detail

[Back to orientation](infcode.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/tokfinity/infcode/1dfd4c14a8359a414a6b5bd1aa75d18b8bbf2be7/cb2e48a1909ab624.json](../../../wiki/dossiers/tokfinity/infcode/1dfd4c14a8359a414a6b5bd1aa75d18b8bbf2be7/cb2e48a1909ab624.json)

## specifications (1 claim(s))

- [observation/documented] InfCode is described as an adversarial multi-agent code agent system that uses LLMs to automatically analyze and fix repository issues, developed by Tokfinity's Code Research team and Beihang University. -- evidence: [README.md#L6-L6](https://github.com/Tokfinity/InfCode/blob/1dfd4c14a8359a414a6b5bd1aa75d18b8bbf2be7/README.md#L6-L6) (`clm_fb6caf8bfa167f383a746f378b714a3736ac956fb5f44764a5533ba02123d692`)

## components (3 claim(s))

- [observation/documented] The Patch Generator registers multiple generator groups, each in a separate container generating and repairing candidate patches in parallel, running up to 5 attempts and gathering all produced patches. -- evidence: [README.md#L22-L22](https://github.com/Tokfinity/InfCode/blob/1dfd4c14a8359a414a6b5bd1aa75d18b8bbf2be7/README.md#L22-L22) (`clm_fd762139d56f0054f80cc703d8b9ef917667b0b5d9c823951b496d87dec5898a`)
- [observation/documented] Inside the Generator, a Test Patch Generator strengthens tests to expose faults while a Code Patch Generator refines patches to satisfy the enhanced tests, in an adversarial loop. -- evidence: [README.md#L24-L24](https://github.com/Tokfinity/InfCode/blob/1dfd4c14a8359a414a6b5bd1aa75d18b8bbf2be7/README.md#L24-L24) (`clm_7ca9a74339684ca7084e23faf0f2c19201ce74cac3f66e6acb7a1fcfa36cb04d`)
- [observation/documented] Auxiliary modules include an Image Builder (per-example container images stored locally and reused), a Tool Executor (runs commands in containers and returns outputs), and an LLM API Manager. -- evidence: [README.md#L32-L32](https://github.com/Tokfinity/InfCode/blob/1dfd4c14a8359a414a6b5bd1aa75d18b8bbf2be7/README.md#L32-L32), [README.md#L34-L36](https://github.com/Tokfinity/InfCode/blob/1dfd4c14a8359a414a6b5bd1aa75d18b8bbf2be7/README.md#L34-L36) (`clm_2c01104390a38d7a52a30d586ad8825f364021fad2769f4141ed439c20c96294`)

## design-choices (1 claim(s))

- [observation/documented] The system uses a dual-agent adversarial refinement framework that iteratively improves both test patches and code patches, aiming to produce fixes verified under strengthened test suites. -- evidence: [README.md#L8-L8](https://github.com/Tokfinity/InfCode/blob/1dfd4c14a8359a414a6b5bd1aa75d18b8bbf2be7/README.md#L8-L8) (`clm_7952de424bdccaa9757528a2c39691c57e1fdf44db4aefb5cd1350c785ff456b`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: setup instructions direct users to create a .env file with API keys (e.g. OPENROUTER_API_KEY), install pip dependencies from requirements.txt, and ensure Docker is installed and running. -- evidence: [README.md#L72-L72](https://github.com/Tokfinity/InfCode/blob/1dfd4c14a8359a414a6b5bd1aa75d18b8bbf2be7/README.md#L72-L72), [README.md#L80-L83](https://github.com/Tokfinity/InfCode/blob/1dfd4c14a8359a414a6b5bd1aa75d18b8bbf2be7/README.md#L80-L83), [README.md#L132-L135](https://github.com/Tokfinity/InfCode/blob/1dfd4c14a8359a414a6b5bd1aa75d18b8bbf2be7/README.md#L132-L135), [README.md#L76-L77](https://github.com/Tokfinity/InfCode/blob/1dfd4c14a8359a414a6b5bd1aa75d18b8bbf2be7/README.md#L76-L77) (`clm_db0689e4e1fc9fdfb930d96977d0c4203bde1e3d566e80f497b11a4d0db06956`)
- [observation/documented] Repository development practice: configuration lives in config/config.yaml with sections for providers, runner (concurrency, iterations), builder (Docker image build), and log settings. -- evidence: [README.md#L123-L127](https://github.com/Tokfinity/InfCode/blob/1dfd4c14a8359a414a6b5bd1aa75d18b8bbf2be7/README.md#L123-L127) (`clm_5cf254e6e1ed8c90a8b86f0f9e196079f6f64f54c43385de4e18c8055eb6fae0`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The Result Submitter tool runs git diff inside the container to obtain and return the generated patch content after the LLM finishes patch generation and testing. -- evidence: [README.md#L62-L64](https://github.com/Tokfinity/InfCode/blob/1dfd4c14a8359a414a6b5bd1aa75d18b8bbf2be7/README.md#L62-L64) (`clm_7f08e2eb308c1ce923702c5c449c2f9455d107f26d0a41c54db007862c128b6a`)
- [observation/documented] A batch CLI (_batch_run.py) accepts flags for config file, run name, issue list, concurrency (default 20), output directory cleaning, and output directory. -- evidence: [README.md#L90-L92](https://github.com/Tokfinity/InfCode/blob/1dfd4c14a8359a414a6b5bd1aa75d18b8bbf2be7/README.md#L90-L92), [README.md#L96-L102](https://github.com/Tokfinity/InfCode/blob/1dfd4c14a8359a414a6b5bd1aa75d18b8bbf2be7/README.md#L96-L102) (`clm_7635ee7dfab8b20122b5594403f9ee5467e48055bf0638cfe69f984a7b98ea8a`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (1 claim(s))

- [observation/documented] InfCode adopts a generate-select architecture: Patch Generation produces candidate patches and Patch Selection picks the optimal one. -- evidence: [README.md#L20-L20](https://github.com/Tokfinity/InfCode/blob/1dfd4c14a8359a414a6b5bd1aa75d18b8bbf2be7/README.md#L20-L20) (`clm_c3544f193d90f5b2941cdd929e21f436acdb86c45b50b5769f2813f8eb7efe4f`)

## tools-permissions (1 claim(s))

- [observation/documented] Agents interact with tools including File Editor (view/create/str_replace/insert), File Searcher, Bash Executor, and Result Submitter, all operating within containerized environments. -- evidence: [README.md#L27-L27](https://github.com/Tokfinity/InfCode/blob/1dfd4c14a8359a414a6b5bd1aa75d18b8bbf2be7/README.md#L27-L27), [README.md#L44-L48](https://github.com/Tokfinity/InfCode/blob/1dfd4c14a8359a414a6b5bd1aa75d18b8bbf2be7/README.md#L44-L48), [README.md#L57-L59](https://github.com/Tokfinity/InfCode/blob/1dfd4c14a8359a414a6b5bd1aa75d18b8bbf2be7/README.md#L57-L59), [README.md#L62-L64](https://github.com/Tokfinity/InfCode/blob/1dfd4c14a8359a414a6b5bd1aa75d18b8bbf2be7/README.md#L62-L64), [README.md#L50-L52](https://github.com/Tokfinity/InfCode/blob/1dfd4c14a8359a414a6b5bd1aa75d18b8bbf2be7/README.md#L50-L52), [README.md#L22-L22](https://github.com/Tokfinity/InfCode/blob/1dfd4c14a8359a414a6b5bd1aa75d18b8bbf2be7/README.md#L22-L22) (`clm_aec938a77df1928f5bb99a69206768dc87853469b26ed6afef15d3e09e595909`)

## evaluation (2 claim(s))

- [observation/documented] An eval.sh script verifies generated patches using the official SWE-bench evaluation tool, with multi-process parallel evaluation (default 20 workers) and results including pass rates and failure reasons. -- evidence: [README.md#L113-L118](https://github.com/Tokfinity/InfCode/blob/1dfd4c14a8359a414a6b5bd1aa75d18b8bbf2be7/README.md#L113-L118), [README.md#L107-L109](https://github.com/Tokfinity/InfCode/blob/1dfd4c14a8359a414a6b5bd1aa75d18b8bbf2be7/README.md#L107-L109) (`clm_68005e7d743b28f600a450b55d3e52d11d23f90e9887c1e525323b5d20690e08`)
- [observation/documented] The README reports a 79.4% solution rate on SWE-Bench Verified, claimed as latest SOTA performance. -- evidence: [README.md#L10-L10](https://github.com/Tokfinity/InfCode/blob/1dfd4c14a8359a414a6b5bd1aa75d18b8bbf2be7/README.md#L10-L10) (`clm_ef6ccd1b88ec1c77f1d64c49abe2b8ed49747036ae78e3e4e466f868ed2b0a34`)

## dependencies (3 claim(s))

- [observation/documented] The LLM API Manager invokes models via the completion endpoint and supports OpenAI, OpenRouter, DeepSeek clients, and self-hosted LLM instances. -- evidence: [README.md#L34-L36](https://github.com/Tokfinity/InfCode/blob/1dfd4c14a8359a414a6b5bd1aa75d18b8bbf2be7/README.md#L34-L36) (`clm_e63cb73bd39e0753070f26cf188b3e805abc93c03a9e30544fc2e32f9d3281ff`)
- [observation/documented] The File Searcher tool is implemented on top of ripgrep, chosen for speed over traditional grep and fuzzy-matching support. -- evidence: [README.md#L54-L54](https://github.com/Tokfinity/InfCode/blob/1dfd4c14a8359a414a6b5bd1aa75d18b8bbf2be7/README.md#L54-L54) (`clm_cd4c4cb8b488ebfb9b85a4cf0a29023e340da6238da6bf33a37545cc49510146`)
- [inference/documented] The project appears MIT-licensed and acknowledges anthropic-quickstart and bytedance's trae-agent as references for tool building. -- evidence: [README.md#L166-L166](https://github.com/Tokfinity/InfCode/blob/1dfd4c14a8359a414a6b5bd1aa75d18b8bbf2be7/README.md#L166-L166), [README.md#L163-L163](https://github.com/Tokfinity/InfCode/blob/1dfd4c14a8359a414a6b5bd1aa75d18b8bbf2be7/README.md#L163-L163) (`clm_ae595767ed99c65b1312ade293bba5579142d045a5280cd2af734742293dd025`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

