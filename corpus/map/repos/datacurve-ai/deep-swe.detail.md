# datacurve-ai/deep-swe -- full detail

[Back to orientation](deep-swe.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/datacurve-ai/deep-swe/0b9fabbb63b9104d678fe965e1632f2dd9eaa2ea/a2fc1feb8fd2295f.json](../../../wiki/dossiers/datacurve-ai/deep-swe/0b9fabbb63b9104d678fe965e1632f2dd9eaa2ea/a2fc1feb8fd2295f.json)

## specifications (2 claim(s))

- [observation/documented] DeepSWE is a benchmark measuring frontier coding agents on original, long-horizon software engineering tasks drawn from active open-source repositories. -- evidence: [README.md#L3-L3](https://github.com/datacurve-ai/deep-swe/blob/0b9fabbb63b9104d678fe965e1632f2dd9eaa2ea/README.md#L3-L3) (`clm_4f8d0980b671bc30ae0fa074f068644e8b893ca12730f6368ec6bb70c3cba0b9`)
- [observation/documented] The benchmark comprises 113 tasks spanning TypeScript, Go, Python, JavaScript, and Rust, with isolated environments and program-based verifiers. -- evidence: [README.md#L3-L3](https://github.com/datacurve-ai/deep-swe/blob/0b9fabbb63b9104d678fe965e1632f2dd9eaa2ea/README.md#L3-L3) (`clm_136be139d93078e7a01a6a3da4340afd8ac1775984948462c464518f733e0261`)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (1 claim(s))

- [observation/documented] The benchmark is run via Pier, installed with uv, using commands like 'pier run -p deep-swe/tasks --agent mini-swe-agent' with model-specific API keys exported. -- evidence: [README.md#L46-L48](https://github.com/datacurve-ai/deep-swe/blob/0b9fabbb63b9104d678fe965e1632f2dd9eaa2ea/README.md#L46-L48), [README.md#L35-L35](https://github.com/datacurve-ai/deep-swe/blob/0b9fabbb63b9104d678fe965e1632f2dd9eaa2ea/README.md#L35-L35), [README.md#L37-L39](https://github.com/datacurve-ai/deep-swe/blob/0b9fabbb63b9104d678fe965e1632f2dd9eaa2ea/README.md#L37-L39), [README.md#L42-L43](https://github.com/datacurve-ai/deep-swe/blob/0b9fabbb63b9104d678fe965e1632f2dd9eaa2ea/README.md#L42-L43) (`clm_ecfb844fd722440ca026adccddf7966888d4332354a78d8cee5935bb344eac3b`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] Tasks use the Harbor task format, with task.toml metadata, instruction.md, an environment Dockerfile, tests, and a held-out reference solution. -- evidence: [README.md#L9-L15](https://github.com/datacurve-ai/deep-swe/blob/0b9fabbb63b9104d678fe965e1632f2dd9eaa2ea/README.md#L9-L15), [README.md#L7-L7](https://github.com/datacurve-ai/deep-swe/blob/0b9fabbb63b9104d678fe965e1632f2dd9eaa2ea/README.md#L7-L7) (`clm_515b61b28c01e6812634967f1ccbeb0fd8d71c2f79a74584035395d6e6d7dc91`)
- [observation/documented] Runs can be subsetted deterministically via --n-tasks with --sample-seed, or targeted at a single task by passing a task-id path to pier run. -- evidence: [README.md#L70-L72](https://github.com/datacurve-ai/deep-swe/blob/0b9fabbb63b9104d678fe965e1632f2dd9eaa2ea/README.md#L70-L72), [README.md#L64-L66](https://github.com/datacurve-ai/deep-swe/blob/0b9fabbb63b9104d678fe965e1632f2dd9eaa2ea/README.md#L64-L66), [README.md#L62-L62](https://github.com/datacurve-ai/deep-swe/blob/0b9fabbb63b9104d678fe965e1632f2dd9eaa2ea/README.md#L62-L62) (`clm_f21fc26059000f3bae36d300a3ca2a4c9f2d891a937f157c9ad11552d6d78c26`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (2 claim(s))

- [observation/documented] Since v1.1, grading uses Harbor's separate verifier environment: the agent works in isolation, commits its work, and a collect hook extracts commits as a patch applied and graded in a pristine container. -- evidence: [README.md#L20-L20](https://github.com/datacurve-ai/deep-swe/blob/0b9fabbb63b9104d678fe965e1632f2dd9eaa2ea/README.md#L20-L20) (`clm_4e2ddcdbd7f515d20e8eda03065f1b7aaa7f47bf30f95f4f8afe97870be2bcfa`)
- [observation/documented] Pier supports multiple agents: mini-swe-agent is model-agnostic, and Pier also drives claude-code, codex, gemini-cli, and opencode; --env modal runs parallel sandboxes on Modal. -- evidence: [README.md#L58-L58](https://github.com/datacurve-ai/deep-swe/blob/0b9fabbb63b9104d678fe965e1632f2dd9eaa2ea/README.md#L58-L58) (`clm_ffede67f18689a3bb68db8c95fed03885addb7a11120a43100c4a8e6e3139ae8`)

## tools-permissions (1 claim(s))

- [observation/documented] Pier, a Harbor-compatible eval framework, adds per-agent network allowlists so agents get only needed network access while the task environment stays isolated, unlike Harbor's blanket blocking in no-internet tasks. -- evidence: [README.md#L52-L52](https://github.com/datacurve-ai/deep-swe/blob/0b9fabbb63b9104d678fe965e1632f2dd9eaa2ea/README.md#L52-L52) (`clm_3bab233abd5bfce5d559362fcd663fcc102bdc351189e2f0c54bac19294f78b4`)

## evaluation (2 claim(s))

- [observation/documented] The verifier accepts any solution whose observable behavior is correct, regardless of internal symbol names or structure, and the reference patch is never used at grading time. -- evidence: [README.md#L17-L18](https://github.com/datacurve-ai/deep-swe/blob/0b9fabbb63b9104d678fe965e1632f2dd9eaa2ea/README.md#L17-L18) (`clm_2fbca97b9da7abbbdbfff1842c20f3361eaf18397db44760d59072a7e2291891`)
- [observation/documented] Each run produces verifier outputs including reward.json with binary reward and pass fractions, ctrf.json test reports, raw stdout logs, and framework-native grader reports. -- evidence: [README.md#L24-L31](https://github.com/datacurve-ai/deep-swe/blob/0b9fabbb63b9104d678fe965e1632f2dd9eaa2ea/README.md#L24-L31) (`clm_58ecac9b533fb9cb23ab9c69e876737673c814a7041cc6c063b58809fd54316e`)

## dependencies (2 claim(s))

- [observation/documented] The separate-verifier grading flow requires the datacurve-pier package at a version newer than 0.3.0. -- evidence: [README.md#L20-L20](https://github.com/datacurve-ai/deep-swe/blob/0b9fabbb63b9104d678fe965e1632f2dd9eaa2ea/README.md#L20-L20) (`clm_f4bd4e999040000f03c5c6adad572761915de4b5be2b26ab519f93c7aab8a303`)
- [observation/documented] Tasks derive from upstream open-source projects under permissive licenses (e.g., MIT, Apache-2.0, BSD-3-Clause); the repo's Apache-2.0 license covers only Datacurve's original contributions, not upstream code. -- evidence: [PROVENANCE.md#L8-L122](https://github.com/datacurve-ai/deep-swe/blob/0b9fabbb63b9104d678fe965e1632f2dd9eaa2ea/PROVENANCE.md#L8-L122), [PROVENANCE.md#L5-L5](https://github.com/datacurve-ai/deep-swe/blob/0b9fabbb63b9104d678fe965e1632f2dd9eaa2ea/PROVENANCE.md#L5-L5), [PROVENANCE.md#L1-L1](https://github.com/datacurve-ai/deep-swe/blob/0b9fabbb63b9104d678fe965e1632f2dd9eaa2ea/PROVENANCE.md#L1-L1), [PROVENANCE.md#L3-L3](https://github.com/datacurve-ai/deep-swe/blob/0b9fabbb63b9104d678fe965e1632f2dd9eaa2ea/PROVENANCE.md#L3-L3) (`clm_75b0561525b3a82ece80d1a6854b68c9d92d9bb998173737e7193788fc3d7f8d`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

