# elpsykongloo/paperbanana-pro -- full detail

[Back to orientation](paperbanana-pro.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/elpsykongloo/paperbanana-pro/3d9d1f11647ee956ec2b1e4c690f06f8942d4af4/b699785fdaa1e74d.json](../../../wiki/dossiers/elpsykongloo/paperbanana-pro/3d9d1f11647ee956ec2b1e4c690f06f8942d4af4/b699785fdaa1e74d.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The documented pipeline comprises six stages: Retriever (few-shot retrieval), Planner (structured visual descriptions), Stylist, Visualizer (image or Matplotlib code), Critic (multi-round review), and optional Polish. -- evidence: [README.md#L212-L219](https://github.com/elpsykongloo/PaperBanana-Pro/blob/3d9d1f11647ee956ec2b1e4c690f06f8942d4af4/README.md#L212-L219) (`clm_a466f19b3198a1faef61d08b80bd5b16594978d7455e4387f93f708b6d2af9dc`)

## design-choices (3 claim(s))

- [observation/documented] The README describes a registry-driven pipeline (Pipeline Registry) intended to replace hardcoded branching so new flows can be added via configuration. -- evidence: [README.md#L29-L40](https://github.com/elpsykongloo/PaperBanana-Pro/blob/3d9d1f11647ee956ec2b1e4c690f06f8942d4af4/README.md#L29-L40) (`clm_3a201638417ed92d8adc18ed4a376bafe0763cbeebf626a1a947b0ab287344fb`)
- [observation/documented] Generation runs as background async jobs with a real-time event timeline, supporting 40+ concurrent candidates, and results are packaged in a `Bundle v1` `.bundle.json` format preserving timelines and review records. -- evidence: [README.md#L29-L40](https://github.com/elpsykongloo/PaperBanana-Pro/blob/3d9d1f11647ee956ec2b1e4c690f06f8942d4af4/README.md#L29-L40) (`clm_1561d16e3c18bdfa2a4e070c416a37d8e71cd3c1c116ca66ad29d27714773882`)
- [observation/documented] A refinement workspace supports 2K/4K upscaling with concurrent multi-version redraws, tree-shaped version chains, and rollback to any historical version. -- evidence: [README.md#L78-L78](https://github.com/elpsykongloo/PaperBanana-Pro/blob/3d9d1f11647ee956ec2b1e4c690f06f8942d4af4/README.md#L78-L78), [README.md#L29-L40](https://github.com/elpsykongloo/PaperBanana-Pro/blob/3d9d1f11647ee956ec2b1e4c690f06f8942d4af4/README.md#L29-L40) (`clm_5588a8342f3ace10314a02d4cebd747ff1937202b4528caa37e4fd5e7f8876df`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: contributions require a Contributor License Agreement, and all submissions—including those from project members—must go through GitHub pull-request review. -- evidence: [CONTRIBUTING.md#L20-L23](https://github.com/elpsykongloo/PaperBanana-Pro/blob/3d9d1f11647ee956ec2b1e4c690f06f8942d4af4/CONTRIBUTING.md#L20-L23), [CONTRIBUTING.md#L8-L12](https://github.com/elpsykongloo/PaperBanana-Pro/blob/3d9d1f11647ee956ec2b1e4c690f06f8942d4af4/CONTRIBUTING.md#L8-L12) (`clm_5eb7e59133e88a78f602a2472254c1f35fcea3f6e3ac1f60dfef5b2bc4152a89`)
- [observation/documented] Repository development practice: the project adopts a Contributor Covenant v1.4-based code of conduct and follows Google's Open Source Community Guidelines. -- evidence: [code-of-conduct.md#L93-L95](https://github.com/elpsykongloo/PaperBanana-Pro/blob/3d9d1f11647ee956ec2b1e4c690f06f8942d4af4/code-of-conduct.md#L93-L95), [CONTRIBUTING.md#L27-L28](https://github.com/elpsykongloo/PaperBanana-Pro/blob/3d9d1f11647ee956ec2b1e4c690f06f8942d4af4/CONTRIBUTING.md#L27-L28) (`clm_c3f187c26298c37cd29811b8009d101f660b3bfdfc58683e88e02b7084d909dc`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The product exposes a `paperbanana` command whose default form launches a GUI frontend on port 8501, equivalent to `paperbanana gui`. -- evidence: [README.md#L161-L163](https://github.com/elpsykongloo/PaperBanana-Pro/blob/3d9d1f11647ee956ec2b1e4c690f06f8942d4af4/README.md#L161-L163) (`clm_f770a7da148a22dc7c290bd622544031dc09e63d261359e243ba1b971b87fe73`)
- [observation/documented] A CLI batch mode exists via `paperbanana run` with parameters including `--task_name` (diagram/plot), `--exp_mode`, `--provider`, `--max_critic_rounds`, `--retrieval_setting`, and `--resume`. -- evidence: [README.md#L188-L195](https://github.com/elpsykongloo/PaperBanana-Pro/blob/3d9d1f11647ee956ec2b1e4c690f06f8942d4af4/README.md#L188-L195), [README.md#L182-L184](https://github.com/elpsykongloo/PaperBanana-Pro/blob/3d9d1f11647ee956ec2b1e4c690f06f8942d4af4/README.md#L182-L184) (`clm_1237b87b10953e38c7cb8aab718dcc62c645bbd626c91b2ae6bf8ea340c4a33f`)
- [observation/documented] A viewer subcommand offers `paperbanana viewer evolution` for pipeline evolution and `paperbanana viewer eval` for evaluation-with-reference review. -- evidence: [README.md#L201-L204](https://github.com/elpsykongloo/PaperBanana-Pro/blob/3d9d1f11647ee956ec2b1e4c690f06f8942d4af4/README.md#L201-L204) (`clm_f835d5bb76b505be2e094af333cd641ffe2b0b689e8862a47e15a80d8d82a959`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (1 claim(s))

- [observation/documented] The optional PaperBananaBench dataset (dwzhu/PaperBananaBench on Hugging Face) supplies few-shot reference examples and an evaluation benchmark; retrieval can be set to `none` to skip it. -- evidence: [README.md#L135-L135](https://github.com/elpsykongloo/PaperBanana-Pro/blob/3d9d1f11647ee956ec2b1e4c690f06f8942d4af4/README.md#L135-L135), [README.md#L133-L133](https://github.com/elpsykongloo/PaperBanana-Pro/blob/3d9d1f11647ee956ec2b1e4c690f06f8942d4af4/README.md#L133-L133) (`clm_c5d4dcb7b586f28bac7bfe1d42d60acdf54d61e75267bedc718a63e234ba6942`)

## dependencies (2 claim(s))

- [observation/documented] The project targets Python 3.12 or later, installs via `uv sync --locked` plus `uv tool install --editable .`, and requirements.txt contains an editable self-dependency. -- evidence: [README.md#L12-L21](https://github.com/elpsykongloo/PaperBanana-Pro/blob/3d9d1f11647ee956ec2b1e4c690f06f8942d4af4/README.md#L12-L21), [requirements.txt#L3-L3](https://github.com/elpsykongloo/PaperBanana-Pro/blob/3d9d1f11647ee956ec2b1e4c690f06f8942d4af4/requirements.txt#L3-L3), [README.md#L118-L124](https://github.com/elpsykongloo/PaperBanana-Pro/blob/3d9d1f11647ee956ec2b1e4c690f06f8942d4af4/README.md#L118-L124) (`clm_e0bc7f42fde1e400631e8ccbd4af452b56b3082bc6269ef5a45363d645f48a89`)
- [observation/documented] Four providers are officially supported: Gemini, OpenAI, Openrouter, and Evolink; any OpenAI-compatible API can also be added by supplying a Base URL. -- evidence: [README.md#L148-L148](https://github.com/elpsykongloo/PaperBanana-Pro/blob/3d9d1f11647ee956ec2b1e4c690f06f8942d4af4/README.md#L148-L148), [README.md#L29-L40](https://github.com/elpsykongloo/PaperBanana-Pro/blob/3d9d1f11647ee956ec2b1e4c690f06f8942d4af4/README.md#L29-L40) (`clm_f3f3f6931e228ef502bad0b250cdb3cbdc3f47c8b06d880259acdfc7db7d5b8e`)

## limitations (1 claim(s))

- [observation/documented] The README states Google has patented the original PaperBanana multi-agent pipeline methodology, so the pipeline logic must not be used commercially, a restriction that also applies to PaperBanana-Pro. -- evidence: [README.md#L263-L263](https://github.com/elpsykongloo/PaperBanana-Pro/blob/3d9d1f11647ee956ec2b1e4c690f06f8942d4af4/README.md#L263-L263) (`clm_ac03c62e4edd93b3f87de8f7adbb13defc4dbcadc0059ee6f5fd6bbc7d9ba421`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

