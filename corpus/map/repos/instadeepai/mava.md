# instadeepai/mava

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 9f67e612654e @ eaf8d9d48d1541b3

## Summary (orientation draft, not independently verified)

Mava is a JAX-based distributed multi-agent reinforcement learning research codebase with single-file algorithm implementations, Hydra configs, Anakin/Sebulba scaling architectures, and benchmarking across many MARL scenarios. Installation, Docker, and contributor workflow guidance is documented in the README and docs.

## Source coverage

Source coverage (complete): 4 of 4 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Mava is a distributed multi-agent reinforcement learning framework implemented in JAX, aimed at fast research iteration with single-file algorithm implementations. -- evidence: [README.md#L7-L9](https://github.com/instadeepai/Mava/blob/9f67e612654ecb7b7d45ff8052ce9ccfc6c68d93/README.md#L7-L9), [README.md#L31-L31](https://github.com/instadeepai/Mava/blob/9f67e612654ecb7b7d45ff8052ce9ccfc6c68d93/README.md#L31-L31)
- components (2 claim(s)):
  - [observation/documented] The repository includes implementations of on- and off-policy MARL algorithms (PPO variants, Q-learning IQL/QMix, SAC) following IL, CTDE, and heterogeneous-agent paradigms. -- evidence: [README.md#L94-L94](https://github.com/instadeepai/Mava/blob/9f67e612654ecb7b7d45ff8052ce9ccfc6c68d93/README.md#L94-L94), [README.md#L96-L111](https://github.com/instadeepai/Mava/blob/9f67e612654ecb7b7d45ff8052ce9ccfc6c68d93/README.md#L96-L111)
  - [observation/documented] Mava provides environment wrappers with out-of-the-box support for several MARL suites including Robot Warehouse, Level-based Foraging, SMAC, MaBrax, Matrax, and Multi-Particle Environments. -- evidence: [README.md#L115-L122](https://github.com/instadeepai/Mava/blob/9f67e612654ecb7b7d45ff8052ce9ccfc6c68d93/README.md#L115-L122), [README.md#L113-L113](https://github.com/instadeepai/Mava/blob/9f67e612654ecb7b7d45ff8052ce9ccfc6c68d93/README.md#L113-L113), [README.md#L35-L39](https://github.com/instadeepai/Mava/blob/9f67e612654ecb7b7d45ff8052ce9ccfc6c68d93/README.md#L35-L39)
- design-choices (2 claim(s)):
  - [observation/documented] Mava supports both Anakin and Sebulba distribution architectures: Anakin for JAX-written environments with end-to-end JIT compilation, Sebulba for non-JAX environments. -- evidence: [README.md#L94-L94](https://github.com/instadeepai/Mava/blob/9f67e612654ecb7b7d45ff8052ce9ccfc6c68d93/README.md#L94-L94), [README.md#L113-L113](https://github.com/instadeepai/Mava/blob/9f67e612654ecb7b7d45ff8052ce9ccfc6c68d93/README.md#L113-L113), [README.md#L35-L39](https://github.com/instadeepai/Mava/blob/9f67e612654ecb7b7d45ff8052ce9ccfc6c68d93/README.md#L35-L39)
  - [observation/documented] The codebase is intentionally not a modular library and is not meant to be imported; it follows a CleanRL/PureJaxRL-style single-file philosophy with small shared utilities and Hydra configs. -- evidence: [README.md#L156-L156](https://github.com/instadeepai/Mava/blob/9f67e612654ecb7b7d45ff8052ce9ccfc6c68d93/README.md#L156-L156)
- workflows (2 claim(s)):
  - [observation/documented] Recommended setup is cloning the repo and installing dependencies with uv (uv sync), with pip install -e as an alternative; Docker via make build/run is suggested when dependency issues arise. -- evidence: [README.md#L50-L50](https://github.com/instadeepai/Mava/blob/9f67e612654ecb7b7d45ff8052ce9ccfc6c68d93/README.md#L50-L50), [README.md#L64-L66](https://github.com/instadeepai/Mava/blob/9f67e612654ecb7b7d45ff8052ce9ccfc6c68d93/README.md#L64-L66), [docs/DETAILED_INSTALL.md#L61-L63](https://github.com/instadeepai/Mava/blob/9f67e612654ecb7b7d45ff8052ce9ccfc6c68d93/docs/DETAILED_INSTALL.md#L61-L63), [README.md#L43-L43](https://github.com/instadeepai/Mava/blob/9f67e612654ecb7b7d45ff8052ce9ccfc6c68d93/README.md#L43-L43), [docs/DETAILED_INSTALL.md#L49-L49](https://github.com/instadeepai/Mava/blob/9f67e612654ecb7b7d45ff8052ce9ccfc6c68d93/docs/DETAILED_INSTALL.md#L49-L49), [docs/DETAILED_INSTALL.md#L55-L57](https://github.com/instadeepai/Mava/blob/9f67e612654ecb7b7d45ff8052ce9ccfc6c68d93/docs/DETAILED_INSTALL.md#L55-L57)
  - [observation/documented] Repository development practice: contributors must sign a Contributor License Agreement, follow conventional commits and feat/fix branch naming, install pre-commit hooks, and submit all changes via reviewed GitHub pull requests. -- evidence: [docs/CONTRIBUTING.md#L8-L12](https://github.com/instadeepai/Mava/blob/9f67e612654ecb7b7d45ff8052ce9ccfc6c68d93/docs/CONTRIBUTING.md#L8-L12), [docs/CONTRIBUTING.md#L39-L47](https://github.com/instadeepai/Mava/blob/9f67e612654ecb7b7d45ff8052ce9ccfc6c68d93/docs/CONTRIBUTING.md#L39-L47), [docs/CONTRIBUTING.md#L53-L53](https://github.com/instadeepai/Mava/blob/9f67e612654ecb7b7d45ff8052ce9ccfc6c68d93/docs/CONTRIBUTING.md#L53-L53), [docs/CONTRIBUTING.md#L51-L51](https://github.com/instadeepai/Mava/blob/9f67e612654ecb7b7d45ff8052ce9ccfc6c68d93/docs/CONTRIBUTING.md#L51-L51), [docs/CONTRIBUTING.md#L57-L60](https://github.com/instadeepai/Mava/blob/9f67e612654ecb7b7d45ff8052ce9ccfc6c68d93/docs/CONTRIBUTING.md#L57-L60)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] Systems are run as Python scripts (e.g. mava/systems/ppo/anakin/ff_ippo.py) and configured via Hydra, with YAML configs in mava/configs/ overridable from the terminal (e.g. env=lbf, env=rware env/scenario=tiny-4ag). -- evidence: [README.md#L78-L78](https://github.com/instadeepai/Mava/blob/9f67e612654ecb7b7d45ff8052ce9ccfc6c68d93/README.md#L78-L78), [README.md#L86-L88](https://github.com/instadeepai/Mava/blob/9f67e612654ecb7b7d45ff8052ce9ccfc6c68d93/README.md#L86-L88), [README.md#L74-L76](https://github.com/instadeepai/Mava/blob/9f67e612654ecb7b7d45ff8052ce9ccfc6c68d93/README.md#L74-L76), [README.md#L80-L82](https://github.com/instadeepai/Mava/blob/9f67e612654ecb7b7d45ff8052ce9ccfc6c68d93/README.md#L80-L82)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation (2 claim(s)):
  - [observation/documented] The authors report a benchmark across 45 scenarios and 6 environment suites validating algorithm performance, with results in the Sable paper and plotted benchmark images in the repo. -- evidence: [README.md#L128-L152](https://github.com/instadeepai/Mava/blob/9f67e612654ecb7b7d45ff8052ce9ccfc6c68d93/README.md#L128-L152), [README.md#L126-L126](https://github.com/instadeepai/Mava/blob/9f67e612654ecb7b7d45ff8052ce9ccfc6c68d93/README.md#L126-L126)
More evidence: [full detail](mava.detail.md)

Metadata and full claim list: [full detail](mava.detail.md)
Human notes ([notes](mava.notes.md), never overwritten by build)

[Back to map index](../../index.md)
