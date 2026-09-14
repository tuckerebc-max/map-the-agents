# scaleapi/swe-interact -- full detail

[Back to orientation](swe-interact.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/scaleapi/swe-interact/b32f98c3b8f76ca65e84341d1f30e5af7135f85d/48f528eef0784222.json](../../../wiki/dossiers/scaleapi/swe-interact/b32f98c3b8f76ca65e84341d1f30e5af7135f85d/48f528eef0784222.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The repository ships task data under data/multiturn and example run configs under run_configs/multiturn that correspond to that data directory. -- evidence: [README.md#L9-L14](https://github.com/scaleapi/SWE-Interact/blob/b32f98c3b8f76ca65e84341d1f30e5af7135f85d/README.md#L9-L14) (`clm_74c4f58be9edf75c088f9459d5f638f508d6404b9af72586c89041a08d99b668`)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (2 claim(s))

- [observation/documented] Runs are launched from the repository root by executing a run config script, e.g. bash run_configs/multiturn/gpt-5p5-high_codex.sh; a single-turn baseline example is also provided. -- evidence: [README.md#L67-L67](https://github.com/scaleapi/SWE-Interact/blob/b32f98c3b8f76ca65e84341d1f30e5af7135f85d/README.md#L67-L67), [README.md#L79-L81](https://github.com/scaleapi/SWE-Interact/blob/b32f98c3b8f76ca65e84341d1f30e5af7135f85d/README.md#L79-L81), [README.md#L71-L73](https://github.com/scaleapi/SWE-Interact/blob/b32f98c3b8f76ca65e84341d1f30e5af7135f85d/README.md#L71-L73), [README.md#L77-L77](https://github.com/scaleapi/SWE-Interact/blob/b32f98c3b8f76ca65e84341d1f30e5af7135f85d/README.md#L77-L77) (`clm_1cf045c138894d6a98637646e2305274b22e7959a56bbe93359f3d84ea2ff5ea`)
- [observation/documented] Run scripts write outputs under results/, and custom configs are made by copying an existing script and adjusting the agent, model, sampling count, or Harbor arguments. -- evidence: [README.md#L83-L83](https://github.com/scaleapi/SWE-Interact/blob/b32f98c3b8f76ca65e84341d1f30e5af7135f85d/README.md#L83-L83) (`clm_3d756c464c48877f6ac4619ca3be8b4701cd7b35802ae6efd521137287be81d7`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] Run configs load credentials from a harbor/.env file located relative to the repository root, which must be created before launching a run. -- evidence: [README.md#L37-L40](https://github.com/scaleapi/SWE-Interact/blob/b32f98c3b8f76ca65e84341d1f30e5af7135f85d/README.md#L37-L40), [README.md#L35-L35](https://github.com/scaleapi/SWE-Interact/blob/b32f98c3b8f76ca65e84341d1f30e5af7135f85d/README.md#L35-L35) (`clm_e12e970d694a1febeaa1801002dcccda5099b5bbf805f01114ca64e32074a48c`)
- [observation/documented] Per-agent configs require different credentials: Codex configs need only the common block, Claude Code configs need ANTHROPIC_API_KEY, OpenCode needs GEMINI_API_KEY, and kimi-cli needs an OpenAI-compatible endpoint. -- evidence: [README.md#L57-L63](https://github.com/scaleapi/SWE-Interact/blob/b32f98c3b8f76ca65e84341d1f30e5af7135f85d/README.md#L57-L63) (`clm_13fcef1ae52698d9948197d72669883f086d8f6ba7fe9b83d1bf8b6b564b0094`)
- [observation/documented] Multi-turn run configs set the simulated user model to openai/gpt-5.5 through the SIM_USER_MODEL variable. -- evidence: [README.md#L75-L75](https://github.com/scaleapi/SWE-Interact/blob/b32f98c3b8f76ca65e84341d1f30e5af7135f85d/README.md#L75-L75) (`clm_3367429383423186304e142183e99eab653d1e43ca258d6590092ce051076d5e`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (2 claim(s))

- [observation/documented] The benchmark uses a simulated user (GPT 5.5 high) and rubric grading; the RF task default rubric model is Anthropic Opus 4.5, matching the original SWE Atlas Refactoring task. -- evidence: [README.md#L44-L44](https://github.com/scaleapi/SWE-Interact/blob/b32f98c3b8f76ca65e84341d1f30e5af7135f85d/README.md#L44-L44) (`clm_79f46fb8f916fcbf0fed1fc9d1b87f8f456f71e8fd20e20e28ed0177f71a7c75`)
- [observation/documented] The configured API gateway must support both openai/gpt-5.5 and the rubric model anthropic/claude-opus-4-5-20251101; a LiteLLM gateway works, while direct OpenAI endpoints need an EVAL_MODEL override. -- evidence: [README.md#L51-L51](https://github.com/scaleapi/SWE-Interact/blob/b32f98c3b8f76ca65e84341d1f30e5af7135f85d/README.md#L51-L51) (`clm_cd5435c7dff41ff183a8e3789f41666f895d9d386fbb3e2e139e8f2686a44acf`)

## dependencies (2 claim(s))

- [observation/documented] Running the tasks requires installing Harbor, done by cloning the laude-institute/harbor repository and installing it with uv tool install. -- evidence: [README.md#L20-L24](https://github.com/scaleapi/SWE-Interact/blob/b32f98c3b8f76ca65e84341d1f30e5af7135f85d/README.md#L20-L24), [README.md#L18-L18](https://github.com/scaleapi/SWE-Interact/blob/b32f98c3b8f76ca65e84341d1f30e5af7135f85d/README.md#L18-L18) (`clm_b686418741edf4ba6d7a9d48a3ce12436e74572079770c3e84db5c1db8dd2d37`)
- [observation/documented] Modal is set up to provide sandbox environments, via installing the modal package with uv pip and running modal setup. -- evidence: [README.md#L26-L26](https://github.com/scaleapi/SWE-Interact/blob/b32f98c3b8f76ca65e84341d1f30e5af7135f85d/README.md#L26-L26), [README.md#L28-L31](https://github.com/scaleapi/SWE-Interact/blob/b32f98c3b8f76ca65e84341d1f30e5af7135f85d/README.md#L28-L31) (`clm_0d2c6407043f93932ea467ed70c3d65bd76bf7093381a73dc2821fc9257c2103`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (1 claim(s))

- [observation/documented] The work is associated with an arXiv paper (2606.30573) titled 'SWE-INTERACT: Reimagining SWE Benchmarks as User-Driven Long-Horizon Coding Sessions' by Raghavendra, Gunjal, Sabharwal, and He. -- evidence: [README.md#L3-L3](https://github.com/scaleapi/SWE-Interact/blob/b32f98c3b8f76ca65e84341d1f30e5af7135f85d/README.md#L3-L3), [README.md#L89-L99](https://github.com/scaleapi/SWE-Interact/blob/b32f98c3b8f76ca65e84341d1f30e5af7135f85d/README.md#L89-L99) (`clm_1caa37303fed99480a7ce966db1b0a01d4faf742ee8cc7666f21d0c75e7565f5`)

