# patched-codes/patchwork -- full detail

[Back to orientation](patchwork.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/patched-codes/patchwork/21948cbec44d3b7aec30715923ac7a0cd3fb1155/05fb15c6c171a6dd.json](../../../wiki/dossiers/patched-codes/patchwork/21948cbec44d3b7aec30715923ac7a0cd3fb1155/05fb15c6c171a6dd.json)

## specifications (1 claim(s))

- [observation/documented] Patchwork is licensed under AGPL-3.0 terms, while the separate patchwork template repository for creating and sharing custom patchflows and steps is licensed under Apache-2.0. -- evidence: [README.md#L188-L188](https://github.com/patched-codes/patchwork/blob/21948cbec44d3b7aec30715923ac7a0cd3fb1155/README.md#L188-L188) (`clm_eb9b3d058152902a155c12a496f1b71be8082f6ae154e12501d250edcf0aa543`)

## components (2 claim(s))

- [observation/documented] Patchwork is built from three key components: reusable atomic steps (e.g., create PR, commit changes, call an LLM), customizable prompt templates, and patchflows that combine steps and prompts into automations. -- evidence: [README.md#L26-L28](https://github.com/patched-codes/patchwork/blob/21948cbec44d3b7aec30715923ac7a0cd3fb1155/README.md#L26-L28) (`clm_f3c7c5b3e09dce8e228ddd65d370a6c1f9e3aaf2ad8139393c5482b1f24fc103`)
- [observation/documented] Predefined patchflows include GenerateDocstring, AutoFix, PRReview, GenerateREADME, DependencyUpgrade, and ResolveIssue, each linked to its own directory in the repository. -- evidence: [README.md#L134-L139](https://github.com/patched-codes/patchwork/blob/21948cbec44d3b7aec30715923ac7a0cd3fb1155/README.md#L134-L139) (`clm_75f6254c08b372942de2c68bb5b36429cb3889e0702246025a87d606ae2d89fc`)

## design-choices (2 claim(s))

- [observation/documented] Patchwork supports any OpenAI-compatible endpoint, enabling models from providers like Groq, Together AI, or Hugging Face, and local models via llama.cpp, ollama, vllm, or tgi. -- evidence: [README.md#L96-L96](https://github.com/patched-codes/patchwork/blob/21948cbec44d3b7aec30715923ac7a0cd3fb1155/README.md#L96-L96), [README.md#L118-L118](https://github.com/patched-codes/patchwork/blob/21948cbec44d3b7aec30715923ac7a0cd3fb1155/README.md#L118-L118) (`clm_bcfb9b614523b974f2dc868d667ecd693f46fa6660ac174d75cde8ed6334078c`)
- [observation/documented] Prompt templates use {{}} placeholder variables replaced at each run with data from steps or inputs; each patchflow ships with an optimized default template that users can override via prompt_template_file. -- evidence: [README.md#L159-L159](https://github.com/patched-codes/patchwork/blob/21948cbec44d3b7aec30715923ac7a0cd3fb1155/README.md#L159-L159), [README.md#L143-L143](https://github.com/patched-codes/patchwork/blob/21948cbec44d3b7aec30715923ac7a0cd3fb1155/README.md#L143-L143) (`clm_fd5514cb5bb578c53202434fd7f5d4a9fd1f940ecfd2d9489b350c8335be030b`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: building from source uses Poetry, with documented steps to install Poetry, clone the repository, activate a poetry shell, and run 'poetry install --all-extras'. -- evidence: [INSTALL.md#L5-L8](https://github.com/patched-codes/patchwork/blob/21948cbec44d3b7aec30715923ac7a0cd3fb1155/INSTALL.md#L5-L8), [INSTALL.md#L10-L13](https://github.com/patched-codes/patchwork/blob/21948cbec44d3b7aec30715923ac7a0cd3fb1155/INSTALL.md#L10-L13), [INSTALL.md#L25-L28](https://github.com/patched-codes/patchwork/blob/21948cbec44d3b7aec30715923ac7a0cd3fb1155/INSTALL.md#L25-L28), [INSTALL.md#L3-L3](https://github.com/patched-codes/patchwork/blob/21948cbec44d3b7aec30715923ac7a0cd3fb1155/INSTALL.md#L3-L3), [INSTALL.md#L20-L23](https://github.com/patched-codes/patchwork/blob/21948cbec44d3b7aec30715923ac7a0cd3fb1155/INSTALL.md#L20-L23) (`clm_07daf6fe71596bbf02fc228171e184fba93674dac7c8c42651c58df96c3c9020`)
- [observation/documented] Repository development practice: contributions for new patchflows, steps, or the core framework are welcomed, with separate instruction documents for creating patchflows and steps, plus a HuggingChat assistant to help author them. -- evidence: [README.md#L165-L166](https://github.com/patched-codes/patchwork/blob/21948cbec44d3b7aec30715923ac7a0cd3fb1155/README.md#L165-L166), [README.md#L163-L163](https://github.com/patched-codes/patchwork/blob/21948cbec44d3b7aec30715923ac7a0cd3fb1155/README.md#L163-L163), [README.md#L170-L170](https://github.com/patched-codes/patchwork/blob/21948cbec44d3b7aec30715923ac7a0cd3fb1155/README.md#L170-L170) (`clm_686d0ae78a78b7abfa03495ae02af2d265d48d1fa0bd948217215401a41acff4`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The CLI runs patchflows with the syntax 'patchwork <PatchFlow> <?Arguments>'; arguments override patchflow attributes as key=value pairs, and valueless keys are treated as boolean True flags. -- evidence: [README.md#L62-L64](https://github.com/patched-codes/patchwork/blob/21948cbec44d3b7aec30715923ac7a0cd3fb1155/README.md#L62-L64), [README.md#L60-L60](https://github.com/patched-codes/patchwork/blob/21948cbec44d3b7aec30715923ac7a0cd3fb1155/README.md#L60-L60), [README.md#L66-L67](https://github.com/patched-codes/patchwork/blob/21948cbec44d3b7aec30715923ac7a0cd3fb1155/README.md#L66-L67) (`clm_fabbbf3f4b19050237a43e34da3c6ffe92e35dba3c9f299ca5e1ec2c4331fb3e`)
- [observation/documented] Patchflow configuration can be supplied via a --config flag pointing to a directory of patchflow defaults or to a config.yml file specifying keys such as openai_api_key, client_base_url, and model. -- evidence: [README.md#L90-L92](https://github.com/patched-codes/patchwork/blob/21948cbec44d3b7aec30715923ac7a0cd3fb1155/README.md#L90-L92), [README.md#L114-L116](https://github.com/patched-codes/patchwork/blob/21948cbec44d3b7aec30715923ac7a0cd3fb1155/README.md#L114-L116), [README.md#L106-L110](https://github.com/patched-codes/patchwork/blob/21948cbec44d3b7aec30715923ac7a0cd3fb1155/README.md#L106-L110) (`clm_72b06c24e0f4a56797a3f1bd8e0e1589b98d7c34e9000f89a1c1714bd239a5fa`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] Optional pip dependency groups exist: 'security' (semgrep, depscan) required for AutoFix and DependencyUpgrade, 'rag' (chromadb) required for ResolveIssue, 'notifications' for notification steps, and 'all' which installs everything. -- evidence: [README.md#L48-L52](https://github.com/patched-codes/patchwork/blob/21948cbec44d3b7aec30715923ac7a0cd3fb1155/README.md#L48-L52) (`clm_1bbaba8205ee9df325123990282e47b1a15eb3e5527976716f1c00364c56160f`)
- [observation/documented] Installing patchwork-cli without any dependency group installs a core set of dependencies sufficient to run the GenerateDocstring, PRReview, and GenerateREADME patchflows. -- evidence: [README.md#L48-L52](https://github.com/patched-codes/patchwork/blob/21948cbec44d3b7aec30715923ac7a0cd3fb1155/README.md#L48-L52) (`clm_802ca562c52decf5f6155c4b3b52df561ea956d672a7b2205962c5aec10351fe`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (1 claim(s))

- [inference/documented] Patchwork appears relevant to security automation use cases, since its AutoFix patchflow patches vulnerabilities identified by Semgrep scans and DependencyUpgrade updates dependencies from vulnerable to fixed versions. -- evidence: [README.md#L134-L139](https://github.com/patched-codes/patchwork/blob/21948cbec44d3b7aec30715923ac7a0cd3fb1155/README.md#L134-L139), [README.md#L77-L77](https://github.com/patched-codes/patchwork/blob/21948cbec44d3b7aec30715923ac7a0cd3fb1155/README.md#L77-L77), [README.md#L71-L71](https://github.com/patched-codes/patchwork/blob/21948cbec44d3b7aec30715923ac7a0cd3fb1155/README.md#L71-L71) (`clm_507a34e5525d06859c2507d4f1deaee89f176d0a63b70e3be9c8035475eb795d`)

