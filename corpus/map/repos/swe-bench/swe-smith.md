# swe-bench/swe-smith

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 9b74ac08118a @ b1674309486c77e4

## Summary (orientation draft, not independently verified)

SWE-smith is a Python toolkit (pip-installable, MIT-licensed) for generating synthetic software-engineering training data: it turns GitHub repos into SWE-gym environments, synthesizes task instances, and provides released datasets, Docker environments, and fine-tuned models. Evidence is documentation-only; no source code slices are present.

## Source coverage

Source coverage (partial): 6 of 17 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] SWE-smith is described as a toolkit for training SWE-agents that can turn any GitHub repository into a SWE-gym and create tasks such as file localization and program repair. -- evidence: [README.md#L28-L31](https://github.com/SWE-bench/SWE-smith/blob/9b74ac08118a85c39c356802f7961893af73e07f/README.md#L28-L31)
- components (3 claim(s)):
  - [observation/documented] Released assets include environments for 128 GitHub repositories as Docker images, downloadable via a bundled download_images.py script. -- evidence: [docs/getting_started/assets.md#L5-L8](https://github.com/SWE-bench/SWE-smith/blob/9b74ac08118a85c39c356802f7961893af73e07f/docs/getting_started/assets.md#L5-L8)
  - [observation/documented] Released assets include a HuggingFace dataset of 50k+ task instances, 5k expert trajectories, and fine-tuned 32B and 7B models based on Qwen 2.5 Coder Instruct. -- evidence: [docs/getting_started/assets.md#L10-L10](https://github.com/SWE-bench/SWE-smith/blob/9b74ac08118a85c39c356802f7961893af73e07f/docs/getting_started/assets.md#L10-L10), [docs/getting_started/assets.md#L12-L16](https://github.com/SWE-bench/SWE-smith/blob/9b74ac08118a85c39c356802f7961893af73e07f/docs/getting_started/assets.md#L12-L16)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows (3 claim(s)):
  - [observation/documented] The documented pipeline for building a dataset is: create an environment, synthesize task instances, keep tasks that break one or more unit tests, then generate issue text for the tasks. -- evidence: [README.md#L40-L44](https://github.com/SWE-bench/SWE-smith/blob/9b74ac08118a85c39c356802f7961893af73e07f/README.md#L40-L44)
  - [observation/documented] A quickstart shows concrete commands: an LM-based bug-generation module (e.g. swesmith.bug_gen.llm.modify with a config file, model, n_bugs, and worker count), patch collection, validation via swesmith.harness.valid, gathering valid instances, and issue generation. -- evidence: [docs/getting_started/quickstart.md#L16-L16](https://github.com/SWE-bench/SWE-smith/blob/9b74ac08118a85c39c356802f7961893af73e07f/docs/getting_started/quickstart.md#L16-L16), [docs/getting_started/quickstart.md#L25-L31](https://github.com/SWE-bench/SWE-smith/blob/9b74ac08118a85c39c356802f7961893af73e07f/docs/getting_started/quickstart.md#L25-L31), [docs/getting_started/quickstart.md#L9-L13](https://github.com/SWE-bench/SWE-smith/blob/9b74ac08118a85c39c356802f7961893af73e07f/docs/getting_started/quickstart.md#L9-L13), [docs/getting_started/quickstart.md#L19-L19](https://github.com/SWE-bench/SWE-smith/blob/9b74ac08118a85c39c356802f7961893af73e07f/docs/getting_started/quickstart.md#L19-L19), [docs/getting_started/quickstart.md#L22-L22](https://github.com/SWE-bench/SWE-smith/blob/9b74ac08118a85c39c356802f7961893af73e07f/docs/getting_started/quickstart.md#L22-L22)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The package exposes a Python API: a repo profile registry can fetch a RepoProfile from a task instance and obtain a Docker container with the task initialized. -- evidence: [README.md#L47-L54](https://github.com/SWE-bench/SWE-smith/blob/9b74ac08118a85c39c356802f7961893af73e07f/README.md#L47-L54)
  - [observation/documented] The toolkit is distributed as the pip package 'swesmith', with a source-install path via a setup.sh script in the cloned repository. -- evidence: [docs/getting_started/installation.md#L11-L15](https://github.com/SWE-bench/SWE-smith/blob/9b74ac08118a85c39c356802f7961893af73e07f/docs/getting_started/installation.md#L11-L15), [docs/getting_started/installation.md#L5-L7](https://github.com/SWE-bench/SWE-smith/blob/9b74ac08118a85c39c356802f7961893af73e07f/docs/getting_started/installation.md#L5-L7)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation (1 claim(s)):
  - [observation/documented] The fine-tuned SWE-agent-LM-32B reportedly achieves 40.2% pass@1 on SWE-bench Verified, and the README claims a 32% jump from fine-tuning Qwen 2.5 Coder with SWE-agent. -- evidence: [README.md#L64-L67](https://github.com/SWE-bench/SWE-smith/blob/9b74ac08118a85c39c356802f7961893af73e07f/README.md#L64-L67), [docs/getting_started/assets.md#L12-L16](https://github.com/SWE-bench/SWE-smith/blob/9b74ac08118a85c39c356802f7961893af73e07f/docs/getting_started/assets.md#L12-L16), [README.md#L59-L61](https://github.com/SWE-bench/SWE-smith/blob/9b74ac08118a85c39c356802f7961893af73e07f/README.md#L59-L61)
- dependencies (2 claim(s)):
  - [observation/documented] Creating execution environments requires Docker; the project was developed and tested on Ubuntu 22.04.4 LTS, and Windows or MacOS support is not planned. -- evidence: [README.md#L36-L38](https://github.com/SWE-bench/SWE-smith/blob/9b74ac08118a85c39c356802f7961893af73e07f/README.md#L36-L38)
More evidence: [full detail](swe-smith.detail.md)

Metadata and full claim list: [full detail](swe-smith.detail.md)
Human notes ([notes](swe-smith.notes.md), never overwritten by build)

[Back to map index](../../index.md)
