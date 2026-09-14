---
access: public
aliases: []
claim_ids:
- clm_02f2a23c23fe24ee3f772d87c6d992725a137449ca61d71b7a5e473383b4d1bf
- clm_1d9129f46271bcb1b386e9e19c357e6a4501dae83cee064e12120149c4c2a564
- clm_291dc2046107f3224aae634a123d14738a7b1fce8ef17a5d4c3d6d8b72fbb240
- clm_3a1de1f34e7509d24b2c77b27bb0890f92fab22cc2b1e373cd812db2deec1f81
- clm_4ce8e7c2fbc6da15c3f318746f12099ad334d4a9a48b1c55681ab904ee1e5098
- clm_602be5bcf774bf93e7699075bd9b84d799c1041baccda47b01f3600defd5af9e
- clm_84d434b87e0f6356f43d10bd1922c323fe71ab1fd21a723cbc83ce621c3c7ef6
- clm_86108d926e353d4af3873f001492eec3433e45360ead595fbeaaed170d568bf3
- clm_918e8b781e8ec5b70c50fee9d021b214a506668973ac0b3f43b4025fa00a7f76
- clm_b0aaf05eabcc2684f071595a857576aeabc9553a45845c78c77c095fe8e2fad6
- clm_ea23659b07cfd38b14aacb40ae2d4eea248f09a4a4f2daa2c505b9a9b0449c12
maturity: draft
page_id: pg_e0b12883be4c52c3a9e046a15c56ad30
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_347fdbab44f45611bb1906c3beb88dae
title: instadeepai/Mava/README.md @ 9f67e612654e
updated_at: '2026-09-14T03:58:15Z'
---

# instadeepai/Mava/README.md @ 9f67e612654e

<!-- rcw:begin owner=source:src_347fdbab44f45611bb1906c3beb88dae block=evidence -->
- Mava is a distributed multi-agent reinforcement learning framework implemented in JAX, aimed at fast research iteration with single-file algorithm implementations. [@claim:clm_02f2a23c23fe24ee3f772d87c6d992725a137449ca61d71b7a5e473383b4d1bf]
- Mava natively logs to json files following the Gorsane et al. (2022) standard, enabling downstream plotting and aggregation with the MARL-eval library. [@claim:clm_1d9129f46271bcb1b386e9e19c357e6a4501dae83cee064e12120149c4c2a564]
- Systems are run as Python scripts (e.g. mava/systems/ppo/anakin/ff_ippo.py) and configured via Hydra, with YAML configs in mava/configs/ overridable from the terminal (e.g. env=lbf, env=rware env/scenario=tiny-4ag). [@claim:clm_291dc2046107f3224aae634a123d14738a7b1fce8ef17a5d4c3d6d8b72fbb240]
- Mava supports both Anakin and Sebulba distribution architectures: Anakin for JAX-written environments with end-to-end JIT compilation, Sebulba for non-JAX environments. [@claim:clm_3a1de1f34e7509d24b2c77b27bb0890f92fab22cc2b1e373cd812db2deec1f81]
- The authors report a benchmark across 45 scenarios and 6 environment suites validating algorithm performance, with results in the Sable paper and plotted benchmark images in the repo. [@claim:clm_4ce8e7c2fbc6da15c3f318746f12099ad334d4a9a48b1c55681ab904ee1e5098]
- The repository includes implementations of on- and off-policy MARL algorithms (PPO variants, Q-learning IQL/QMix, SAC) following IL, CTDE, and heterogeneous-agent paradigms. [@claim:clm_602be5bcf774bf93e7699075bd9b84d799c1041baccda47b01f3600defd5af9e]
- Mava provides environment wrappers with out-of-the-box support for several MARL suites including Robot Warehouse, Level-based Foraging, SMAC, MaBrax, Matrax, and Multi-Particle Environments. [@claim:clm_84d434b87e0f6356f43d10bd1922c323fe71ab1fd21a723cbc83ce621c3c7ef6]
- Mava is not intended to be installed as a library but used as a research tool by cloning the repository, per the installation guidance. [@claim:clm_86108d926e353d4af3873f001492eec3433e45360ead595fbeaaed170d568bf3]
- Mava has been tested on Python 3.11 and 3.12 (earlier versions may work), with optional cuda12 and tpu extras for GPU/TPU-aware JAX installs. [@claim:clm_918e8b781e8ec5b70c50fee9d021b214a506668973ac0b3f43b4025fa00a7f76]
- The codebase is intentionally not a modular library and is not meant to be imported; it follows a CleanRL/PureJaxRL-style single-file philosophy with small shared utilities and Hydra configs. [@claim:clm_b0aaf05eabcc2684f071595a857576aeabc9553a45845c78c77c095fe8e2fad6]
- Recommended setup is cloning the repo and installing dependencies with uv (uv sync), with pip install -e as an alternative; Docker via make build/run is suggested when dependency issues arise. [@claim:clm_ea23659b07cfd38b14aacb40ae2d4eea248f09a4a4f2daa2c505b9a9b0449c12]
<!-- rcw:end owner=source:src_347fdbab44f45611bb1906c3beb88dae block=evidence -->

## Researcher notes

