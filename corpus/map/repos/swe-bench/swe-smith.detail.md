# swe-bench/swe-smith -- full detail

[Back to orientation](swe-smith.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/swe-bench/swe-smith/9b74ac08118a85c39c356802f7961893af73e07f/b1674309486c77e4.json](../../../wiki/dossiers/swe-bench/swe-smith/9b74ac08118a85c39c356802f7961893af73e07f/b1674309486c77e4.json)

## specifications (1 claim(s))

- [observation/documented] SWE-smith is described as a toolkit for training SWE-agents that can turn any GitHub repository into a SWE-gym and create tasks such as file localization and program repair. -- evidence: [README.md#L28-L31](https://github.com/SWE-bench/SWE-smith/blob/9b74ac08118a85c39c356802f7961893af73e07f/README.md#L28-L31) (`clm_91847c08b29c3888c967faee8796c4e7421eaaf3eb5ea232b31cf6af747718a7`)

## components (3 claim(s))

- [observation/documented] Released assets include environments for 128 GitHub repositories as Docker images, downloadable via a bundled download_images.py script. -- evidence: [docs/getting_started/assets.md#L5-L8](https://github.com/SWE-bench/SWE-smith/blob/9b74ac08118a85c39c356802f7961893af73e07f/docs/getting_started/assets.md#L5-L8) (`clm_5b4c1b5c169308a82ba1673739587bb98790068c88c4e60316d9445214e1c473`)
- [observation/documented] Released assets include a HuggingFace dataset of 50k+ task instances, 5k expert trajectories, and fine-tuned 32B and 7B models based on Qwen 2.5 Coder Instruct. -- evidence: [docs/getting_started/assets.md#L10-L10](https://github.com/SWE-bench/SWE-smith/blob/9b74ac08118a85c39c356802f7961893af73e07f/docs/getting_started/assets.md#L10-L10), [docs/getting_started/assets.md#L12-L16](https://github.com/SWE-bench/SWE-smith/blob/9b74ac08118a85c39c356802f7961893af73e07f/docs/getting_started/assets.md#L12-L16) (`clm_2f242f840e3c074f4dbd671664a685160c6a7130a757c2b6b304dea3e33721ca`)
- [observation/documented] SWE-Rater-32B, a Qwen 2.5 Coder Instruct 32B model fine-tuned on human-annotated ratings of SWE-bench task difficulty, is released as a HuggingFace model. -- evidence: [docs/getting_started/assets.md#L18-L19](https://github.com/SWE-bench/SWE-smith/blob/9b74ac08118a85c39c356802f7961893af73e07f/docs/getting_started/assets.md#L18-L19) (`clm_e27e56b12ae476c820e293de5738224250e9f4630b15133ce432e114c9ea1b02`)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (3 claim(s))

- [observation/documented] The documented pipeline for building a dataset is: create an environment, synthesize task instances, keep tasks that break one or more unit tests, then generate issue text for the tasks. -- evidence: [README.md#L40-L44](https://github.com/SWE-bench/SWE-smith/blob/9b74ac08118a85c39c356802f7961893af73e07f/README.md#L40-L44) (`clm_60304b7fe55ae495e4887467f3bae786d43986fb0c3ac526a774a489d8af1a71`)
- [observation/documented] A quickstart shows concrete commands: an LM-based bug-generation module (e.g. swesmith.bug_gen.llm.modify with a config file, model, n_bugs, and worker count), patch collection, validation via swesmith.harness.valid, gathering valid instances, and issue generation. -- evidence: [docs/getting_started/quickstart.md#L16-L16](https://github.com/SWE-bench/SWE-smith/blob/9b74ac08118a85c39c356802f7961893af73e07f/docs/getting_started/quickstart.md#L16-L16), [docs/getting_started/quickstart.md#L25-L31](https://github.com/SWE-bench/SWE-smith/blob/9b74ac08118a85c39c356802f7961893af73e07f/docs/getting_started/quickstart.md#L25-L31), [docs/getting_started/quickstart.md#L9-L13](https://github.com/SWE-bench/SWE-smith/blob/9b74ac08118a85c39c356802f7961893af73e07f/docs/getting_started/quickstart.md#L9-L13), [docs/getting_started/quickstart.md#L19-L19](https://github.com/SWE-bench/SWE-smith/blob/9b74ac08118a85c39c356802f7961893af73e07f/docs/getting_started/quickstart.md#L19-L19), [docs/getting_started/quickstart.md#L22-L22](https://github.com/SWE-bench/SWE-smith/blob/9b74ac08118a85c39c356802f7961893af73e07f/docs/getting_started/quickstart.md#L22-L22) (`clm_53229cee4b3c76a6753e28dea31f0e88f296efa7ccf108dc7012aad1b9571a01`)
- [observation/documented] Repository development practice: contributors are asked to additionally run 'pre-commit install' after setup, and a Contributing Guide is referenced for further details. -- evidence: [docs/getting_started/installation.md#L17-L17](https://github.com/SWE-bench/SWE-smith/blob/9b74ac08118a85c39c356802f7961893af73e07f/docs/getting_started/installation.md#L17-L17), [docs/getting_started/installation.md#L19-L21](https://github.com/SWE-bench/SWE-smith/blob/9b74ac08118a85c39c356802f7961893af73e07f/docs/getting_started/installation.md#L19-L21), [README.md#L72-L73](https://github.com/SWE-bench/SWE-smith/blob/9b74ac08118a85c39c356802f7961893af73e07f/README.md#L72-L73) (`clm_a5860cc1cd80681c39ff1ab13cc4e9adcbc85ed48aeb96025dbe482d9d33d489`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The package exposes a Python API: a repo profile registry can fetch a RepoProfile from a task instance and obtain a Docker container with the task initialized. -- evidence: [README.md#L47-L54](https://github.com/SWE-bench/SWE-smith/blob/9b74ac08118a85c39c356802f7961893af73e07f/README.md#L47-L54) (`clm_00c534d9a19f30c0aeb36b258579b173bd2750877bf9deeee2b3023b615875ed`)
- [observation/documented] The toolkit is distributed as the pip package 'swesmith', with a source-install path via a setup.sh script in the cloned repository. -- evidence: [docs/getting_started/installation.md#L11-L15](https://github.com/SWE-bench/SWE-smith/blob/9b74ac08118a85c39c356802f7961893af73e07f/docs/getting_started/installation.md#L11-L15), [docs/getting_started/installation.md#L5-L7](https://github.com/SWE-bench/SWE-smith/blob/9b74ac08118a85c39c356802f7961893af73e07f/docs/getting_started/installation.md#L5-L7) (`clm_360be28bf80117d07582c07a13d4bcc332c309d8d31f9d1069da1a95fd548408`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (1 claim(s))

- [observation/documented] The fine-tuned SWE-agent-LM-32B reportedly achieves 40.2% pass@1 on SWE-bench Verified, and the README claims a 32% jump from fine-tuning Qwen 2.5 Coder with SWE-agent. -- evidence: [README.md#L64-L67](https://github.com/SWE-bench/SWE-smith/blob/9b74ac08118a85c39c356802f7961893af73e07f/README.md#L64-L67), [docs/getting_started/assets.md#L12-L16](https://github.com/SWE-bench/SWE-smith/blob/9b74ac08118a85c39c356802f7961893af73e07f/docs/getting_started/assets.md#L12-L16), [README.md#L59-L61](https://github.com/SWE-bench/SWE-smith/blob/9b74ac08118a85c39c356802f7961893af73e07f/README.md#L59-L61) (`clm_4671d0338deb3388a32eccf75e4677a78c6184b9900e8efe1237c2ac61d9d3c0`)

## dependencies (2 claim(s))

- [observation/documented] Creating execution environments requires Docker; the project was developed and tested on Ubuntu 22.04.4 LTS, and Windows or MacOS support is not planned. -- evidence: [README.md#L36-L38](https://github.com/SWE-bench/SWE-smith/blob/9b74ac08118a85c39c356802f7961893af73e07f/README.md#L36-L38) (`clm_2b5b9d02bf71631cf3e0ece14eaf3a1bc356c5e0512ea8f5f66ed92bc82b2674`)
- [observation/documented] The README badge indicates Python 3.10+ is required, and the project is MIT licensed. -- evidence: [README.md#L79-L79](https://github.com/SWE-bench/SWE-smith/blob/9b74ac08118a85c39c356802f7961893af73e07f/README.md#L79-L79), [README.md#L1-L24](https://github.com/SWE-bench/SWE-smith/blob/9b74ac08118a85c39c356802f7961893af73e07f/README.md#L1-L24) (`clm_cf059549e5d7d1524f164073af267f0d6342b4cde38de156abe48924f8fd9cee`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

