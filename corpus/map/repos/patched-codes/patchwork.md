# patched-codes/patchwork

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 21948cbec44d @ 05fb15c6c171a6dd

## Summary (orientation draft, not independently verified)

Patchwork is a CLI tool that automates development tasks such as PR reviews, bug fixing, and security patching using LLM-assisted patchflows built from reusable steps and prompt templates, installable via pip with optional dependency groups.

## Source coverage

Source coverage (partial): 3 of 4 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Patchwork is licensed under AGPL-3.0 terms, while the separate patchwork template repository for creating and sharing custom patchflows and steps is licensed under Apache-2.0. -- evidence: [README.md#L188-L188](https://github.com/patched-codes/patchwork/blob/21948cbec44d3b7aec30715923ac7a0cd3fb1155/README.md#L188-L188)
- components (2 claim(s)):
  - [observation/documented] Patchwork is built from three key components: reusable atomic steps (e.g., create PR, commit changes, call an LLM), customizable prompt templates, and patchflows that combine steps and prompts into automations. -- evidence: [README.md#L26-L28](https://github.com/patched-codes/patchwork/blob/21948cbec44d3b7aec30715923ac7a0cd3fb1155/README.md#L26-L28)
  - [observation/documented] Predefined patchflows include GenerateDocstring, AutoFix, PRReview, GenerateREADME, DependencyUpgrade, and ResolveIssue, each linked to its own directory in the repository. -- evidence: [README.md#L134-L139](https://github.com/patched-codes/patchwork/blob/21948cbec44d3b7aec30715923ac7a0cd3fb1155/README.md#L134-L139)
- design-choices (2 claim(s)):
  - [observation/documented] Patchwork supports any OpenAI-compatible endpoint, enabling models from providers like Groq, Together AI, or Hugging Face, and local models via llama.cpp, ollama, vllm, or tgi. -- evidence: [README.md#L96-L96](https://github.com/patched-codes/patchwork/blob/21948cbec44d3b7aec30715923ac7a0cd3fb1155/README.md#L96-L96), [README.md#L118-L118](https://github.com/patched-codes/patchwork/blob/21948cbec44d3b7aec30715923ac7a0cd3fb1155/README.md#L118-L118)
  - [observation/documented] Prompt templates use {{}} placeholder variables replaced at each run with data from steps or inputs; each patchflow ships with an optimized default template that users can override via prompt_template_file. -- evidence: [README.md#L159-L159](https://github.com/patched-codes/patchwork/blob/21948cbec44d3b7aec30715923ac7a0cd3fb1155/README.md#L159-L159), [README.md#L143-L143](https://github.com/patched-codes/patchwork/blob/21948cbec44d3b7aec30715923ac7a0cd3fb1155/README.md#L143-L143)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: building from source uses Poetry, with documented steps to install Poetry, clone the repository, activate a poetry shell, and run 'poetry install --all-extras'. -- evidence: [INSTALL.md#L5-L8](https://github.com/patched-codes/patchwork/blob/21948cbec44d3b7aec30715923ac7a0cd3fb1155/INSTALL.md#L5-L8), [INSTALL.md#L10-L13](https://github.com/patched-codes/patchwork/blob/21948cbec44d3b7aec30715923ac7a0cd3fb1155/INSTALL.md#L10-L13), [INSTALL.md#L25-L28](https://github.com/patched-codes/patchwork/blob/21948cbec44d3b7aec30715923ac7a0cd3fb1155/INSTALL.md#L25-L28), [INSTALL.md#L3-L3](https://github.com/patched-codes/patchwork/blob/21948cbec44d3b7aec30715923ac7a0cd3fb1155/INSTALL.md#L3-L3), [INSTALL.md#L20-L23](https://github.com/patched-codes/patchwork/blob/21948cbec44d3b7aec30715923ac7a0cd3fb1155/INSTALL.md#L20-L23)
  - [observation/documented] Repository development practice: contributions for new patchflows, steps, or the core framework are welcomed, with separate instruction documents for creating patchflows and steps, plus a HuggingChat assistant to help author them. -- evidence: [README.md#L165-L166](https://github.com/patched-codes/patchwork/blob/21948cbec44d3b7aec30715923ac7a0cd3fb1155/README.md#L165-L166), [README.md#L163-L163](https://github.com/patched-codes/patchwork/blob/21948cbec44d3b7aec30715923ac7a0cd3fb1155/README.md#L163-L163), [README.md#L170-L170](https://github.com/patched-codes/patchwork/blob/21948cbec44d3b7aec30715923ac7a0cd3fb1155/README.md#L170-L170)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The CLI runs patchflows with the syntax 'patchwork <PatchFlow> <?Arguments>'; arguments override patchflow attributes as key=value pairs, and valueless keys are treated as boolean True flags. -- evidence: [README.md#L62-L64](https://github.com/patched-codes/patchwork/blob/21948cbec44d3b7aec30715923ac7a0cd3fb1155/README.md#L62-L64), [README.md#L60-L60](https://github.com/patched-codes/patchwork/blob/21948cbec44d3b7aec30715923ac7a0cd3fb1155/README.md#L60-L60), [README.md#L66-L67](https://github.com/patched-codes/patchwork/blob/21948cbec44d3b7aec30715923ac7a0cd3fb1155/README.md#L66-L67)
  - [observation/documented] Patchflow configuration can be supplied via a --config flag pointing to a directory of patchflow defaults or to a config.yml file specifying keys such as openai_api_key, client_base_url, and model. -- evidence: [README.md#L90-L92](https://github.com/patched-codes/patchwork/blob/21948cbec44d3b7aec30715923ac7a0cd3fb1155/README.md#L90-L92), [README.md#L114-L116](https://github.com/patched-codes/patchwork/blob/21948cbec44d3b7aec30715923ac7a0cd3fb1155/README.md#L114-L116), [README.md#L106-L110](https://github.com/patched-codes/patchwork/blob/21948cbec44d3b7aec30715923ac7a0cd3fb1155/README.md#L106-L110)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
More evidence: [full detail](patchwork.detail.md)

Metadata and full claim list: [full detail](patchwork.detail.md)
Human notes ([notes](patchwork.notes.md), never overwritten by build)

[Back to map index](../../index.md)
