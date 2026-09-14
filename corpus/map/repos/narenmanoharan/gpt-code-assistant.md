# narenmanoharan/gpt-code-assistant

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 2bd455a16993 @ b7f97ce5a86938fe

## Summary (orientation draft, not independently verified)

gpt-code-assistant is a pip-installable CLI that indexes a local codebase with vector embeddings and lets users query it via LLMs, with project management commands and OpenAI as the model backend. Evidence is mostly README documentation plus contributor guides; no source code is included in the snapshot.

## Source coverage

Source coverage (complete): 3 of 3 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] Creating a project indexes all files by generating embeddings for each file and storing them in a local database. -- evidence: [README.md#L46-L46](https://github.com/narenmanoharan/gpt-code-assistant/blob/2bd455a1699320dca85f215c05c11626d99f3539/README.md#L46-L46)
- design-choices (2 claim(s)):
  - [observation/documented] The tool is described as privacy-centric: code snippets are only sent when a question is asked and the LLM requests relevant code, though snippets are shared with OpenAI. -- evidence: [README.md#L27-L30](https://github.com/narenmanoharan/gpt-code-assistant/blob/2bd455a1699320dca85f215c05c11626d99f3539/README.md#L27-L30)
  - [observation/documented] The tool is designed to work directly on any local codebase and claims language-agnostic support for multiple programming languages. -- evidence: [README.md#L27-L30](https://github.com/narenmanoharan/gpt-code-assistant/blob/2bd455a1699320dca85f215c05c11626d99f3539/README.md#L27-L30)
- workflows (3 claim(s)):
  - [observation/documented] Repository development practice: contributors fork the repo, create a descriptively named branch, install dependencies with poetry, install pre-commit hooks, and submit pull requests for maintainer review. -- evidence: [CONTRIBUTING.md#L47-L49](https://github.com/narenmanoharan/gpt-code-assistant/blob/2bd455a1699320dca85f215c05c11626d99f3539/CONTRIBUTING.md#L47-L49), [CONTRIBUTING.md#L37-L37](https://github.com/narenmanoharan/gpt-code-assistant/blob/2bd455a1699320dca85f215c05c11626d99f3539/CONTRIBUTING.md#L37-L37), [CONTRIBUTING.md#L13-L13](https://github.com/narenmanoharan/gpt-code-assistant/blob/2bd455a1699320dca85f215c05c11626d99f3539/CONTRIBUTING.md#L13-L13), [CONTRIBUTING.md#L17-L19](https://github.com/narenmanoharan/gpt-code-assistant/blob/2bd455a1699320dca85f215c05c11626d99f3539/CONTRIBUTING.md#L17-L19), [CONTRIBUTING.md#L79-L84](https://github.com/narenmanoharan/gpt-code-assistant/blob/2bd455a1699320dca85f215c05c11626d99f3539/CONTRIBUTING.md#L79-L84)
  - [observation/documented] Repository development practice: local development sets the LOCAL_DEV environment variable to true and runs the project via 'poetry run gpt-code-assistant'. -- evidence: [CONTRIBUTING.md#L51-L51](https://github.com/narenmanoharan/gpt-code-assistant/blob/2bd455a1699320dca85f215c05c11626d99f3539/CONTRIBUTING.md#L51-L51), [CONTRIBUTING.md#L59-L61](https://github.com/narenmanoharan/gpt-code-assistant/blob/2bd455a1699320dca85f215c05c11626d99f3539/CONTRIBUTING.md#L59-L61), [CONTRIBUTING.md#L53-L55](https://github.com/narenmanoharan/gpt-code-assistant/blob/2bd455a1699320dca85f215c05c11626d99f3539/CONTRIBUTING.md#L53-L55)
- skills-patterns (1 claim(s)):
  - [observation/documented] Documentation advises that mentioning a specific file name or keywords in a query improves search accuracy. -- evidence: [README.md#L64-L64](https://github.com/narenmanoharan/gpt-code-assistant/blob/2bd455a1699320dca85f215c05c11626d99f3539/README.md#L64-L64), [README.md#L76-L76](https://github.com/narenmanoharan/gpt-code-assistant/blob/2bd455a1699320dca85f215c05c11626d99f3539/README.md#L76-L76)
- interfaces (2 claim(s)):
  - [observation/documented] The product is a terminal CLI named gpt-code-assistant with subcommands including create-project, query, list-projects, refresh-project, delete-project, and select-model. -- evidence: [README.md#L106-L108](https://github.com/narenmanoharan/gpt-code-assistant/blob/2bd455a1699320dca85f215c05c11626d99f3539/README.md#L106-L108), [README.md#L82-L84](https://github.com/narenmanoharan/gpt-code-assistant/blob/2bd455a1699320dca85f215c05c11626d99f3539/README.md#L82-L84), [README.md#L90-L92](https://github.com/narenmanoharan/gpt-code-assistant/blob/2bd455a1699320dca85f215c05c11626d99f3539/README.md#L90-L92), [README.md#L58-L60](https://github.com/narenmanoharan/gpt-code-assistant/blob/2bd455a1699320dca85f215c05c11626d99f3539/README.md#L58-L60), [README.md#L48-L49](https://github.com/narenmanoharan/gpt-code-assistant/blob/2bd455a1699320dca85f215c05c11626d99f3539/README.md#L48-L49), [README.md#L98-L100](https://github.com/narenmanoharan/gpt-code-assistant/blob/2bd455a1699320dca85f215c05c11626d99f3539/README.md#L98-L100)
  - [observation/documented] The selected model is persisted in $HOME/.gpt-code-assistant/config.toml. -- evidence: [README.md#L110-L110](https://github.com/narenmanoharan/gpt-code-assistant/blob/2bd455a1699320dca85f215c05c11626d99f3539/README.md#L110-L110)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
  - [observation/documented] The tool uses OpenAI's API; it prompts the user to configure OPENAI_API_KEY if not already set, and defaults to the gpt-3.5-turbo-16k model. -- evidence: [README.md#L110-L110](https://github.com/narenmanoharan/gpt-code-assistant/blob/2bd455a1699320dca85f215c05c11626d99f3539/README.md#L110-L110), [README.md#L114-L114](https://github.com/narenmanoharan/gpt-code-assistant/blob/2bd455a1699320dca85f215c05c11626d99f3539/README.md#L114-L114)
  - [observation/documented] The package is installable via pip as gpt-code-assistant. -- evidence: [README.md#L38-L40](https://github.com/narenmanoharan/gpt-code-assistant/blob/2bd455a1699320dca85f215c05c11626d99f3539/README.md#L38-L40)
- limitations (1 claim(s)):
  - [observation/documented] Per the roadmap, support for additional models (Claude, Bedrock), local models (Llama2, Starcoder), code generation saved to files, and multi-codebase search are planned but not yet implemented. -- evidence: [README.md#L129-L135](https://github.com/narenmanoharan/gpt-code-assistant/blob/2bd455a1699320dca85f215c05c11626d99f3539/README.md#L129-L135)
More evidence: [full detail](gpt-code-assistant.detail.md)

Metadata and full claim list: [full detail](gpt-code-assistant.detail.md)
Human notes ([notes](gpt-code-assistant.notes.md), never overwritten by build)

[Back to map index](../../index.md)
