# openhands/tom-swe

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 535f45f1639c @ 4447761c18d40e3c

## Summary (orientation draft, not independently verified)

ToM-SWE is a Theory of Mind package for software engineering agents, providing a TomModule consultation API, a three-tier memory system, OpenHands integration via TomCodeActAgent, CLI analysis tools, and litellm-based LLM configuration; an experiment log reports intent-prediction accuracy results.

## Source coverage

Source coverage (complete): 5 of 5 candidate file(s) selected; repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] ToM-SWE is a Theory of Mind package intended to give software engineering agents personalized user understanding and adaptive behavior. -- evidence: [README.md#L21-L21](https://github.com/OpenHands/ToM-SWE/blob/535f45f1639c9a355714140d3243208f177fd5b9/README.md#L21-L21)
- components (2 claim(s)):
  - [observation/documented] The package exposes a TomModule class importable from tom_swe.tom_module and instantiated inside an async demo function. -- evidence: [README.md#L71-L73](https://github.com/OpenHands/ToM-SWE/blob/535f45f1639c9a355714140d3243208f177fd5b9/README.md#L71-L73), [README.md#L75-L76](https://github.com/OpenHands/ToM-SWE/blob/535f45f1639c9a355714140d3243208f177fd5b9/README.md#L75-L76)
  - [observation/documented] OpenHands integration is provided through a TomCodeActAgent, set as default_agent in config, which automatically supplies consultation and personalized guidance and processes user sessions. -- evidence: [README.md#L125-L128](https://github.com/OpenHands/ToM-SWE/blob/535f45f1639c9a355714140d3243208f177fd5b9/README.md#L125-L128), [README.md#L121-L123](https://github.com/OpenHands/ToM-SWE/blob/535f45f1639c9a355714140d3243208f177fd5b9/README.md#L121-L123), [README.md#L119-L119](https://github.com/OpenHands/ToM-SWE/blob/535f45f1639c9a355714140d3243208f177fd5b9/README.md#L119-L119)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: tests run via pytest (e.g. uv run pytest tests/), with pre-commit hooks, black, isort, ruff, and mypy for code quality. -- evidence: [CLAUDE.md#L51-L52](https://github.com/OpenHands/ToM-SWE/blob/535f45f1639c9a355714140d3243208f177fd5b9/CLAUDE.md#L51-L52), [CLAUDE.md#L48-L48](https://github.com/OpenHands/ToM-SWE/blob/535f45f1639c9a355714140d3243208f177fd5b9/CLAUDE.md#L48-L48), [CLAUDE.md#L45-L45](https://github.com/OpenHands/ToM-SWE/blob/535f45f1639c9a355714140d3243208f177fd5b9/CLAUDE.md#L45-L45), [CLAUDE.md#L36-L36](https://github.com/OpenHands/ToM-SWE/blob/535f45f1639c9a355714140d3243208f177fd5b9/CLAUDE.md#L36-L36), [CLAUDE.md#L42-L42](https://github.com/OpenHands/ToM-SWE/blob/535f45f1639c9a355714140d3243208f177fd5b9/CLAUDE.md#L42-L42), [AGENTS.md#L51-L51](https://github.com/OpenHands/ToM-SWE/blob/535f45f1639c9a355714140d3243208f177fd5b9/AGENTS.md#L51-L51)
  - [observation/documented] Repository development practice: releases publish to PyPI automatically via a publish-to-pypi.yml trusted-publishing workflow triggered by a GitHub release on a pushed git tag. -- evidence: [RELEASE.md#L86-L89](https://github.com/OpenHands/ToM-SWE/blob/535f45f1639c9a355714140d3243208f177fd5b9/RELEASE.md#L86-L89), [RELEASE.md#L93-L101](https://github.com/OpenHands/ToM-SWE/blob/535f45f1639c9a355714140d3243208f177fd5b9/RELEASE.md#L93-L101), [RELEASE.md#L105-L109](https://github.com/OpenHands/ToM-SWE/blob/535f45f1639c9a355714140d3243208f177fd5b9/RELEASE.md#L105-L109)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] TomModule provides an async consult method taking user_id and current_context parameters and returning a consultation result that the demo prints. -- evidence: [README.md#L78-L83](https://github.com/OpenHands/ToM-SWE/blob/535f45f1639c9a355714140d3243208f177fd5b9/README.md#L78-L83)
  - [observation/documented] The project ships CLI commands including user-analysis, tom-test, tom-analyze, rag-agent, and tom-config, runnable via uv. -- evidence: [README.md#L106-L107](https://github.com/OpenHands/ToM-SWE/blob/535f45f1639c9a355714140d3243208f177fd5b9/README.md#L106-L107), [README.md#L110-L111](https://github.com/OpenHands/ToM-SWE/blob/535f45f1639c9a355714140d3243208f177fd5b9/README.md#L110-L111), [README.md#L90-L93](https://github.com/OpenHands/ToM-SWE/blob/535f45f1639c9a355714140d3243208f177fd5b9/README.md#L90-L93), [README.md#L114-L115](https://github.com/OpenHands/ToM-SWE/blob/535f45f1639c9a355714140d3243208f177fd5b9/README.md#L114-L115)
- memory-state (1 claim(s)):
  - [observation/documented] The system uses a three-tier memory structure: cleaned sessions, then session analyses, then user profiles. -- evidence: [README.md#L97-L100](https://github.com/OpenHands/ToM-SWE/blob/535f45f1639c9a355714140d3243208f177fd5b9/README.md#L97-L100), [AGENTS.md#L4-L4](https://github.com/OpenHands/ToM-SWE/blob/535f45f1639c9a355714140d3243208f177fd5b9/AGENTS.md#L4-L4)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation (1 claim(s)):
  - [observation/documented] An experiment log reports ToM intent-prediction accuracy of 65-82% across five users, plus suggestion helpfulness and user ratings. -- evidence: [EXPERIMENT_LOG.md#L51-L57](https://github.com/OpenHands/ToM-SWE/blob/535f45f1639c9a355714140d3243208f177fd5b9/EXPERIMENT_LOG.md#L51-L57)
- dependencies (2 claim(s)):
  - [observation/documented] LLM access is configured through a .env file with LITELLM_API_KEY, LITELLM_BASE_URL, and a default model of litellm_proxy/claude-sonnet-4-20250514. -- evidence: [README.md#L61-L65](https://github.com/OpenHands/ToM-SWE/blob/535f45f1639c9a355714140d3243208f177fd5b9/README.md#L61-L65), [CLAUDE.md#L145-L149](https://github.com/OpenHands/ToM-SWE/blob/535f45f1639c9a355714140d3243208f177fd5b9/CLAUDE.md#L145-L149)
  - [observation/documented] README requirements list Python 3.8+, the uv package manager, and an LLM API key obtained from All Hands AI. -- evidence: [README.md#L137-L139](https://github.com/OpenHands/ToM-SWE/blob/535f45f1639c9a355714140d3243208f177fd5b9/README.md#L137-L139)
- limitations: unknown (no source-linked claim submitted for this facet)
- relevance: unknown (no source-linked claim submitted for this facet)
More evidence: [full detail](tom-swe.detail.md)

Metadata and full claim list: [full detail](tom-swe.detail.md)
Human notes ([notes](tom-swe.notes.md), never overwritten by build)

[Back to map index](../../index.md)
