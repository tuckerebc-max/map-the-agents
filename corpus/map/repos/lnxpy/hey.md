# lnxpy/hey

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 9b1b2ab680a4 @ f65bf68cccf6626a

## Summary (orientation draft, not independently verified)

Hey is a free CLI-based AI assistant powered by configurable LLM services, distributed on PyPI as hey-mindsdb, with commands for auth, asking questions, and configuration. Evidence is limited to README documentation and a dev requirements file.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 5 facet(s); 8 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (1 claim(s)):
  - [observation/documented] Configuration parameters include service URL, model (default gpt-3.5-turbo), a system prompt, code-block theme, loading text and spinner, and a never_style option to disable output styling for copying. -- evidence: [README.md#L98-L101](https://github.com/lnxpy/hey/blob/9b1b2ab680a4f4ed6b62aa7c2ea62f71b7d403dc/README.md#L98-L101), [README.md#L78-L81](https://github.com/lnxpy/hey/blob/9b1b2ab680a4f4ed6b62aa7c2ea62f71b7d403dc/README.md#L78-L81), [README.md#L89-L90](https://github.com/lnxpy/hey/blob/9b1b2ab680a4f4ed6b62aa7c2ea62f71b7d403dc/README.md#L89-L90), [README.md#L86-L87](https://github.com/lnxpy/hey/blob/9b1b2ab680a4f4ed6b62aa7c2ea62f71b7d403dc/README.md#L86-L87), [README.md#L92-L93](https://github.com/lnxpy/hey/blob/9b1b2ab680a4f4ed6b62aa7c2ea62f71b7d403dc/README.md#L92-L93), [README.md#L83-L84](https://github.com/lnxpy/hey/blob/9b1b2ab680a4f4ed6b62aa7c2ea62f71b7d403dc/README.md#L83-L84), [README.md#L95-L96](https://github.com/lnxpy/hey/blob/9b1b2ab680a4f4ed6b62aa7c2ea62f71b7d403dc/README.md#L95-L96)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: the dev requirements file includes pytest and coverage>=7.2.5, indicating a Python test setup for contributors. -- evidence: [requirements-dev.txt#L1-L2](https://github.com/lnxpy/hey/blob/9b1b2ab680a4f4ed6b62aa7c2ea62f71b7d403dc/requirements-dev.txt#L1-L2)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (5 claim(s)):
  - [observation/documented] Hey is a CLI-based AI assistant powered by LLMs, and users can choose which LLM service it connects to. -- evidence: [README.md#L9-L9](https://github.com/lnxpy/hey/blob/9b1b2ab680a4f4ed6b62aa7c2ea62f71b7d403dc/README.md#L9-L9)
  - [observation/documented] Running bare `hey` opens the default $EDITOR for composing longer questions; if unset, it falls back to vim on Unix-like systems and notepad on Windows. -- evidence: [README.md#L59-L59](https://github.com/lnxpy/hey/blob/9b1b2ab680a4f4ed6b62aa7c2ea62f71b7d403dc/README.md#L59-L59), [README.md#L54-L57](https://github.com/lnxpy/hey/blob/9b1b2ab680a4f4ed6b62aa7c2ea62f71b7d403dc/README.md#L54-L57)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (3 claim(s)):
  - [observation/documented] The package is installable from PyPI as hey-mindsdb, or directly from the GitHub repository via pip. -- evidence: [README.md#L20-L22](https://github.com/lnxpy/hey/blob/9b1b2ab680a4f4ed6b62aa7c2ea62f71b7d403dc/README.md#L20-L22), [README.md#L25-L27](https://github.com/lnxpy/hey/blob/9b1b2ab680a4f4ed6b62aa7c2ea62f71b7d403dc/README.md#L25-L27)
  - [observation/documented] The tool requires pip and Python 3.8 or newer on the user's machine. -- evidence: [README.md#L15-L15](https://github.com/lnxpy/hey/blob/9b1b2ab680a4f4ed6b62aa7c2ea62f71b7d403dc/README.md#L15-L15)
- limitations (1 claim(s)):
  - [observation/documented] The README recommends free tokens from mdb.ai but notes users are not limited to it and can point Hey at any other LLM service. -- evidence: [README.md#L11-L12](https://github.com/lnxpy/hey/blob/9b1b2ab680a4f4ed6b62aa7c2ea62f71b7d403dc/README.md#L11-L12)
- relevance: unknown (no source-linked claim submitted for this facet)

(4 additional claim(s) omitted for length; see [full detail](hey.detail.md) for every claim.)

Metadata and full claim list: [full detail](hey.detail.md)
Human notes ([notes](hey.notes.md), never overwritten by build)

[Back to map index](../../index.md)
