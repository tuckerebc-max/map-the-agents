# instadeepai/mava -- full detail

[Back to orientation](mava.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/instadeepai/mava/9f67e612654ecb7b7d45ff8052ce9ccfc6c68d93/eaf8d9d48d1541b3.json](../../../wiki/dossiers/instadeepai/mava/9f67e612654ecb7b7d45ff8052ce9ccfc6c68d93/eaf8d9d48d1541b3.json)

## specifications (1 claim(s))

- [observation/documented] Mava is a distributed multi-agent reinforcement learning framework implemented in JAX, aimed at fast research iteration with single-file algorithm implementations. -- evidence: [README.md#L7-L9](https://github.com/instadeepai/Mava/blob/9f67e612654ecb7b7d45ff8052ce9ccfc6c68d93/README.md#L7-L9), [README.md#L31-L31](https://github.com/instadeepai/Mava/blob/9f67e612654ecb7b7d45ff8052ce9ccfc6c68d93/README.md#L31-L31) (`clm_02f2a23c23fe24ee3f772d87c6d992725a137449ca61d71b7a5e473383b4d1bf`)

## components (2 claim(s))

- [observation/documented] The repository includes implementations of on- and off-policy MARL algorithms (PPO variants, Q-learning IQL/QMix, SAC) following IL, CTDE, and heterogeneous-agent paradigms. -- evidence: [README.md#L94-L94](https://github.com/instadeepai/Mava/blob/9f67e612654ecb7b7d45ff8052ce9ccfc6c68d93/README.md#L94-L94), [README.md#L96-L111](https://github.com/instadeepai/Mava/blob/9f67e612654ecb7b7d45ff8052ce9ccfc6c68d93/README.md#L96-L111) (`clm_602be5bcf774bf93e7699075bd9b84d799c1041baccda47b01f3600defd5af9e`)
- [observation/documented] Mava provides environment wrappers with out-of-the-box support for several MARL suites including Robot Warehouse, Level-based Foraging, SMAC, MaBrax, Matrax, and Multi-Particle Environments. -- evidence: [README.md#L115-L122](https://github.com/instadeepai/Mava/blob/9f67e612654ecb7b7d45ff8052ce9ccfc6c68d93/README.md#L115-L122), [README.md#L113-L113](https://github.com/instadeepai/Mava/blob/9f67e612654ecb7b7d45ff8052ce9ccfc6c68d93/README.md#L113-L113), [README.md#L35-L39](https://github.com/instadeepai/Mava/blob/9f67e612654ecb7b7d45ff8052ce9ccfc6c68d93/README.md#L35-L39) (`clm_84d434b87e0f6356f43d10bd1922c323fe71ab1fd21a723cbc83ce621c3c7ef6`)

## design-choices (2 claim(s))

- [observation/documented] Mava supports both Anakin and Sebulba distribution architectures: Anakin for JAX-written environments with end-to-end JIT compilation, Sebulba for non-JAX environments. -- evidence: [README.md#L94-L94](https://github.com/instadeepai/Mava/blob/9f67e612654ecb7b7d45ff8052ce9ccfc6c68d93/README.md#L94-L94), [README.md#L113-L113](https://github.com/instadeepai/Mava/blob/9f67e612654ecb7b7d45ff8052ce9ccfc6c68d93/README.md#L113-L113), [README.md#L35-L39](https://github.com/instadeepai/Mava/blob/9f67e612654ecb7b7d45ff8052ce9ccfc6c68d93/README.md#L35-L39) (`clm_3a1de1f34e7509d24b2c77b27bb0890f92fab22cc2b1e373cd812db2deec1f81`)
- [observation/documented] The codebase is intentionally not a modular library and is not meant to be imported; it follows a CleanRL/PureJaxRL-style single-file philosophy with small shared utilities and Hydra configs. -- evidence: [README.md#L156-L156](https://github.com/instadeepai/Mava/blob/9f67e612654ecb7b7d45ff8052ce9ccfc6c68d93/README.md#L156-L156) (`clm_b0aaf05eabcc2684f071595a857576aeabc9553a45845c78c77c095fe8e2fad6`)

## workflows (2 claim(s))

- [observation/documented] Recommended setup is cloning the repo and installing dependencies with uv (uv sync), with pip install -e as an alternative; Docker via make build/run is suggested when dependency issues arise. -- evidence: [README.md#L50-L50](https://github.com/instadeepai/Mava/blob/9f67e612654ecb7b7d45ff8052ce9ccfc6c68d93/README.md#L50-L50), [README.md#L64-L66](https://github.com/instadeepai/Mava/blob/9f67e612654ecb7b7d45ff8052ce9ccfc6c68d93/README.md#L64-L66), [docs/DETAILED_INSTALL.md#L61-L63](https://github.com/instadeepai/Mava/blob/9f67e612654ecb7b7d45ff8052ce9ccfc6c68d93/docs/DETAILED_INSTALL.md#L61-L63), [README.md#L43-L43](https://github.com/instadeepai/Mava/blob/9f67e612654ecb7b7d45ff8052ce9ccfc6c68d93/README.md#L43-L43), [docs/DETAILED_INSTALL.md#L49-L49](https://github.com/instadeepai/Mava/blob/9f67e612654ecb7b7d45ff8052ce9ccfc6c68d93/docs/DETAILED_INSTALL.md#L49-L49), [docs/DETAILED_INSTALL.md#L55-L57](https://github.com/instadeepai/Mava/blob/9f67e612654ecb7b7d45ff8052ce9ccfc6c68d93/docs/DETAILED_INSTALL.md#L55-L57) (`clm_ea23659b07cfd38b14aacb40ae2d4eea248f09a4a4f2daa2c505b9a9b0449c12`)
- [observation/documented] Repository development practice: contributors must sign a Contributor License Agreement, follow conventional commits and feat/fix branch naming, install pre-commit hooks, and submit all changes via reviewed GitHub pull requests. -- evidence: [docs/CONTRIBUTING.md#L8-L12](https://github.com/instadeepai/Mava/blob/9f67e612654ecb7b7d45ff8052ce9ccfc6c68d93/docs/CONTRIBUTING.md#L8-L12), [docs/CONTRIBUTING.md#L39-L47](https://github.com/instadeepai/Mava/blob/9f67e612654ecb7b7d45ff8052ce9ccfc6c68d93/docs/CONTRIBUTING.md#L39-L47), [docs/CONTRIBUTING.md#L53-L53](https://github.com/instadeepai/Mava/blob/9f67e612654ecb7b7d45ff8052ce9ccfc6c68d93/docs/CONTRIBUTING.md#L53-L53), [docs/CONTRIBUTING.md#L51-L51](https://github.com/instadeepai/Mava/blob/9f67e612654ecb7b7d45ff8052ce9ccfc6c68d93/docs/CONTRIBUTING.md#L51-L51), [docs/CONTRIBUTING.md#L57-L60](https://github.com/instadeepai/Mava/blob/9f67e612654ecb7b7d45ff8052ce9ccfc6c68d93/docs/CONTRIBUTING.md#L57-L60) (`clm_5f4873d1752b1a9379e3de43e78abc223bf0ef348b5f606e9fbc2c4d625bcbc6`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] Systems are run as Python scripts (e.g. mava/systems/ppo/anakin/ff_ippo.py) and configured via Hydra, with YAML configs in mava/configs/ overridable from the terminal (e.g. env=lbf, env=rware env/scenario=tiny-4ag). -- evidence: [README.md#L78-L78](https://github.com/instadeepai/Mava/blob/9f67e612654ecb7b7d45ff8052ce9ccfc6c68d93/README.md#L78-L78), [README.md#L86-L88](https://github.com/instadeepai/Mava/blob/9f67e612654ecb7b7d45ff8052ce9ccfc6c68d93/README.md#L86-L88), [README.md#L74-L76](https://github.com/instadeepai/Mava/blob/9f67e612654ecb7b7d45ff8052ce9ccfc6c68d93/README.md#L74-L76), [README.md#L80-L82](https://github.com/instadeepai/Mava/blob/9f67e612654ecb7b7d45ff8052ce9ccfc6c68d93/README.md#L80-L82) (`clm_291dc2046107f3224aae634a123d14738a7b1fce8ef17a5d4c3d6d8b72fbb240`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (2 claim(s))

- [observation/documented] The authors report a benchmark across 45 scenarios and 6 environment suites validating algorithm performance, with results in the Sable paper and plotted benchmark images in the repo. -- evidence: [README.md#L128-L152](https://github.com/instadeepai/Mava/blob/9f67e612654ecb7b7d45ff8052ce9ccfc6c68d93/README.md#L128-L152), [README.md#L126-L126](https://github.com/instadeepai/Mava/blob/9f67e612654ecb7b7d45ff8052ce9ccfc6c68d93/README.md#L126-L126) (`clm_4ce8e7c2fbc6da15c3f318746f12099ad334d4a9a48b1c55681ab904ee1e5098`)
- [observation/documented] Mava natively logs to json files following the Gorsane et al. (2022) standard, enabling downstream plotting and aggregation with the MARL-eval library. -- evidence: [README.md#L35-L39](https://github.com/instadeepai/Mava/blob/9f67e612654ecb7b7d45ff8052ce9ccfc6c68d93/README.md#L35-L39) (`clm_1d9129f46271bcb1b386e9e19c357e6a4501dae83cee064e12120149c4c2a564`)

## dependencies (1 claim(s))

- [observation/documented] Mava has been tested on Python 3.11 and 3.12 (earlier versions may work), with optional cuda12 and tpu extras for GPU/TPU-aware JAX installs. -- evidence: [README.md#L68-L68](https://github.com/instadeepai/Mava/blob/9f67e612654ecb7b7d45ff8052ce9ccfc6c68d93/README.md#L68-L68), [README.md#L57-L60](https://github.com/instadeepai/Mava/blob/9f67e612654ecb7b7d45ff8052ce9ccfc6c68d93/README.md#L57-L60) (`clm_918e8b781e8ec5b70c50fee9d021b214a506668973ac0b3f43b4025fa00a7f76`)

## limitations (1 claim(s))

- [observation/documented] Mava is not intended to be installed as a library but used as a research tool by cloning the repository, per the installation guidance. -- evidence: [README.md#L43-L43](https://github.com/instadeepai/Mava/blob/9f67e612654ecb7b7d45ff8052ce9ccfc6c68d93/README.md#L43-L43) (`clm_86108d926e353d4af3873f001492eec3433e45360ead595fbeaaed170d568bf3`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

