# openhands/tom-swe -- full detail

[Back to orientation](tom-swe.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/openhands/tom-swe/535f45f1639c9a355714140d3243208f177fd5b9/4447761c18d40e3c.json](../../../wiki/dossiers/openhands/tom-swe/535f45f1639c9a355714140d3243208f177fd5b9/4447761c18d40e3c.json)

## specifications (1 claim(s))

- [observation/documented] ToM-SWE is a Theory of Mind package intended to give software engineering agents personalized user understanding and adaptive behavior. -- evidence: [README.md#L21-L21](https://github.com/OpenHands/ToM-SWE/blob/535f45f1639c9a355714140d3243208f177fd5b9/README.md#L21-L21) (`clm_184d3e1b65131040a752b93e065831af8844753529e371cd1acfa55df8f84fac`)

## components (2 claim(s))

- [observation/documented] The package exposes a TomModule class importable from tom_swe.tom_module and instantiated inside an async demo function. -- evidence: [README.md#L71-L73](https://github.com/OpenHands/ToM-SWE/blob/535f45f1639c9a355714140d3243208f177fd5b9/README.md#L71-L73), [README.md#L75-L76](https://github.com/OpenHands/ToM-SWE/blob/535f45f1639c9a355714140d3243208f177fd5b9/README.md#L75-L76) (`clm_217056c77de82371e9f7f3a8e534544d59ea65367c8fa14b64b2c9c4c36722de`)
- [observation/documented] OpenHands integration is provided through a TomCodeActAgent, set as default_agent in config, which automatically supplies consultation and personalized guidance and processes user sessions. -- evidence: [README.md#L125-L128](https://github.com/OpenHands/ToM-SWE/blob/535f45f1639c9a355714140d3243208f177fd5b9/README.md#L125-L128), [README.md#L121-L123](https://github.com/OpenHands/ToM-SWE/blob/535f45f1639c9a355714140d3243208f177fd5b9/README.md#L121-L123), [README.md#L119-L119](https://github.com/OpenHands/ToM-SWE/blob/535f45f1639c9a355714140d3243208f177fd5b9/README.md#L119-L119) (`clm_49b718ce73a898506c17ed8ce206ee98616694a8b5664d359b409ddb71d119e8`)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: tests run via pytest (e.g. uv run pytest tests/), with pre-commit hooks, black, isort, ruff, and mypy for code quality. -- evidence: [CLAUDE.md#L51-L52](https://github.com/OpenHands/ToM-SWE/blob/535f45f1639c9a355714140d3243208f177fd5b9/CLAUDE.md#L51-L52), [CLAUDE.md#L48-L48](https://github.com/OpenHands/ToM-SWE/blob/535f45f1639c9a355714140d3243208f177fd5b9/CLAUDE.md#L48-L48), [CLAUDE.md#L45-L45](https://github.com/OpenHands/ToM-SWE/blob/535f45f1639c9a355714140d3243208f177fd5b9/CLAUDE.md#L45-L45), [CLAUDE.md#L36-L36](https://github.com/OpenHands/ToM-SWE/blob/535f45f1639c9a355714140d3243208f177fd5b9/CLAUDE.md#L36-L36), [CLAUDE.md#L42-L42](https://github.com/OpenHands/ToM-SWE/blob/535f45f1639c9a355714140d3243208f177fd5b9/CLAUDE.md#L42-L42), [AGENTS.md#L51-L51](https://github.com/OpenHands/ToM-SWE/blob/535f45f1639c9a355714140d3243208f177fd5b9/AGENTS.md#L51-L51) (`clm_3e5c1fcbd3d511f0c4a7c18a1bfe69befb21f83849e6f6c291d6d7b421d303ee`)
- [observation/documented] Repository development practice: releases publish to PyPI automatically via a publish-to-pypi.yml trusted-publishing workflow triggered by a GitHub release on a pushed git tag. -- evidence: [RELEASE.md#L86-L89](https://github.com/OpenHands/ToM-SWE/blob/535f45f1639c9a355714140d3243208f177fd5b9/RELEASE.md#L86-L89), [RELEASE.md#L93-L101](https://github.com/OpenHands/ToM-SWE/blob/535f45f1639c9a355714140d3243208f177fd5b9/RELEASE.md#L93-L101), [RELEASE.md#L105-L109](https://github.com/OpenHands/ToM-SWE/blob/535f45f1639c9a355714140d3243208f177fd5b9/RELEASE.md#L105-L109) (`clm_b89b5a4298de24478ce8432fc3a948ec8df4247288cfc48dd6f10c98c48b8634`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] TomModule provides an async consult method taking user_id and current_context parameters and returning a consultation result that the demo prints. -- evidence: [README.md#L78-L83](https://github.com/OpenHands/ToM-SWE/blob/535f45f1639c9a355714140d3243208f177fd5b9/README.md#L78-L83) (`clm_98a1017f97e069986f4f2a0651b4389738280e278de846cb70a5d7b2ffc3a21b`)
- [observation/documented] The project ships CLI commands including user-analysis, tom-test, tom-analyze, rag-agent, and tom-config, runnable via uv. -- evidence: [README.md#L106-L107](https://github.com/OpenHands/ToM-SWE/blob/535f45f1639c9a355714140d3243208f177fd5b9/README.md#L106-L107), [README.md#L110-L111](https://github.com/OpenHands/ToM-SWE/blob/535f45f1639c9a355714140d3243208f177fd5b9/README.md#L110-L111), [README.md#L90-L93](https://github.com/OpenHands/ToM-SWE/blob/535f45f1639c9a355714140d3243208f177fd5b9/README.md#L90-L93), [README.md#L114-L115](https://github.com/OpenHands/ToM-SWE/blob/535f45f1639c9a355714140d3243208f177fd5b9/README.md#L114-L115) (`clm_2c3c1800f852dd30312e11d2cebcf6baaf28a61c84fb0f6081790446768d855a`)

## memory-state (1 claim(s))

- [observation/documented] The system uses a three-tier memory structure: cleaned sessions, then session analyses, then user profiles. -- evidence: [README.md#L97-L100](https://github.com/OpenHands/ToM-SWE/blob/535f45f1639c9a355714140d3243208f177fd5b9/README.md#L97-L100), [AGENTS.md#L4-L4](https://github.com/OpenHands/ToM-SWE/blob/535f45f1639c9a355714140d3243208f177fd5b9/AGENTS.md#L4-L4) (`clm_9230a771c56198945d13cc4947ca206371243d2f6860597207db354a7ac7e571`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (1 claim(s))

- [observation/documented] An experiment log reports ToM intent-prediction accuracy of 65-82% across five users, plus suggestion helpfulness and user ratings. -- evidence: [EXPERIMENT_LOG.md#L51-L57](https://github.com/OpenHands/ToM-SWE/blob/535f45f1639c9a355714140d3243208f177fd5b9/EXPERIMENT_LOG.md#L51-L57) (`clm_0c32759eb40b2b94b60f9e8fc8908cd8e81a287902a4f11b0a67e5980e4dd426`)

## dependencies (2 claim(s))

- [observation/documented] LLM access is configured through a .env file with LITELLM_API_KEY, LITELLM_BASE_URL, and a default model of litellm_proxy/claude-sonnet-4-20250514. -- evidence: [README.md#L61-L65](https://github.com/OpenHands/ToM-SWE/blob/535f45f1639c9a355714140d3243208f177fd5b9/README.md#L61-L65), [CLAUDE.md#L145-L149](https://github.com/OpenHands/ToM-SWE/blob/535f45f1639c9a355714140d3243208f177fd5b9/CLAUDE.md#L145-L149) (`clm_1378b366fd2cd78902aeb6cf9629d535c58510fddab83ef0ea8730f0b1469ad4`)
- [observation/documented] README requirements list Python 3.8+, the uv package manager, and an LLM API key obtained from All Hands AI. -- evidence: [README.md#L137-L139](https://github.com/OpenHands/ToM-SWE/blob/535f45f1639c9a355714140d3243208f177fd5b9/README.md#L137-L139) (`clm_5313374995c16ecd961d538b34a45a799ba11edac9a0c164a18a5fa09f2ac7a3`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

