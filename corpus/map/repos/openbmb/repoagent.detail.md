# openbmb/repoagent -- full detail

[Back to orientation](repoagent.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/openbmb/repoagent/825d988127d7bfd757237d9c4e8678d9104030f0/eea8cc889eeddaae.json](../../../wiki/dossiers/openbmb/repoagent/825d988127d7bfd757237d9c4e8678d9104030f0/eea8cc889eeddaae.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (2 claim(s))

- [observation/documented] Per its README features, RepoAgent detects Git changes (additions, deletions, modifications), analyzes code structure via AST to document individual objects, and identifies bidirectional inter-object invocation relationships. -- evidence: [README.md#L45-L51](https://github.com/OpenBMB/RepoAgent/blob/825d988127d7bfd757237d9c4e8678d9104030f0/README.md#L45-L51) (`clm_26cde967f1253d87580c97250ec6598703127fe9b981655ed2fdb1256a1d93fa`)
- [observation/documented] The README states the tool replaces Markdown content based on changes and uses multi-threaded concurrent operations to improve documentation-generation efficiency. -- evidence: [README.md#L45-L51](https://github.com/OpenBMB/RepoAgent/blob/825d988127d7bfd757237d9c4e8678d9104030f0/README.md#L45-L51) (`clm_aa2f18965d11a549bf00437120bc7eb7766b51e639064969c657701ea284c8d8`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: contributors set up a development environment with PDM (pdm venv create --name repoagent, then pdm install), with a GitHub Codespace option offered as the easiest route. -- evidence: [README.md#L77-L78](https://github.com/OpenBMB/RepoAgent/blob/825d988127d7bfd757237d9c4e8678d9104030f0/README.md#L77-L78), [README.md#L72-L72](https://github.com/OpenBMB/RepoAgent/blob/825d988127d7bfd757237d9c4e8678d9104030f0/README.md#L72-L72), [README.md#L93-L95](https://github.com/OpenBMB/RepoAgent/blob/825d988127d7bfd757237d9c4e8678d9104030f0/README.md#L93-L95), [README.md#L101-L103](https://github.com/OpenBMB/RepoAgent/blob/825d988127d7bfd757237d9c4e8678d9104030f0/README.md#L101-L103) (`clm_a670734d3d0cb88d2b6a934a1081dfe1df12e35092401ac7d11b9405b71fd353`)
- [observation/documented] In a target git repository, users can configure a pre-commit hook (entry: repoagent, types: [python]) so each git commit triggers automatic change detection and document generation, with RepoAgent modifying staged files before the commit completes. -- evidence: [README.md#L183-L186](https://github.com/OpenBMB/RepoAgent/blob/825d988127d7bfd757237d9c4e8678d9104030f0/README.md#L183-L186), [README.md#L188-L189](https://github.com/OpenBMB/RepoAgent/blob/825d988127d7bfd757237d9c4e8678d9104030f0/README.md#L188-L189), [README.md#L163-L174](https://github.com/OpenBMB/RepoAgent/blob/825d988127d7bfd757237d9c4e8678d9104030f0/README.md#L163-L174) (`clm_7b02934ac18746567547c49cf12f35c75324f25be301a20d80a8ffe6eae5ab99`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (4 claim(s))

- [observation/documented] RepoAgent provides a CLI: 'repoagent run' generates or updates docs, 'repoagent clean' removes repoagent-related cache, and 'repoagent diff' previews which docs would be updated or generated from current code changes. -- evidence: [README.md#L138-L141](https://github.com/OpenBMB/RepoAgent/blob/825d988127d7bfd757237d9c4e8678d9104030f0/README.md#L138-L141), [README.md#L117-L121](https://github.com/OpenBMB/RepoAgent/blob/825d988127d7bfd757237d9c4e8678d9104030f0/README.md#L117-L121) (`clm_17f42bdf6dd199f2bac8c4854c7b0ea429cc7379cc40dc8e238387c1ae99fab4`)
- [observation/documented] The run command accepts optional flags overriding config defaults, including --model (default gpt-3.5-turbo), --temperature (0.2), --request-timeout (60), --base-url, --target-repo-path, --hierarchy-path, --markdown-docs-path, --ignore-list, --language (default Chinese), and --log-level. -- evidence: [README.md#L125-L134](https://github.com/OpenBMB/RepoAgent/blob/825d988127d7bfd757237d9c4e8678d9104030f0/README.md#L125-L134), [README.md#L123-L123](https://github.com/OpenBMB/RepoAgent/blob/825d988127d7bfd757237d9c4e8678d9104030f0/README.md#L123-L123) (`clm_9cde1d58094281c30426472923de3f14fd78887cfd46896d9ce250eef9936a10`)
- [observation/documented] 'repoagent run --print-hierarchy' prints how repo-agent parses the target repository. -- evidence: [README.md#L117-L121](https://github.com/OpenBMB/RepoAgent/blob/825d988127d7bfd757237d9c4e8678d9104030f0/README.md#L117-L121) (`clm_bd40ff4b258c958cd96819ca15fc686df08cc067792dd78c398dc2ea8c5927b4`)
- [observation/documented] An optional 'chat-with-repo' prototype, installed via 'pip install repoagent[chat-with-repo]' and started with 'repoagent chat-with-repo', runs a server for automatic issue Q&A and code explanation. -- evidence: [README.md#L203-L203](https://github.com/OpenBMB/RepoAgent/blob/825d988127d7bfd757237d9c4e8678d9104030f0/README.md#L203-L203), [README.md#L205-L208](https://github.com/OpenBMB/RepoAgent/blob/825d988127d7bfd757237d9c4e8678d9104030f0/README.md#L205-L208) (`clm_b39bb4afc7fee012d4f1735dfe3594d2d787f1b153047cd09d368e1ef0828c49`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Before configuring parameters, the OpenAI API key must be set as an environment variable, with instructions given for Linux/Mac, Windows cmd, and PowerShell. -- evidence: [README.md#L107-L107](https://github.com/OpenBMB/RepoAgent/blob/825d988127d7bfd757237d9c4e8678d9104030f0/README.md#L107-L107), [README.md#L109-L113](https://github.com/OpenBMB/RepoAgent/blob/825d988127d7bfd757237d9c4e8678d9104030f0/README.md#L109-L113) (`clm_9f53fd5febb995b8e9c38be65c25e87985f124c366112bb4820603859b99288d`)

## limitations (2 claim(s))

- [observation/documented] The pre-commit hook example notes that currently only Python is supported as a trigger file type, and the roadmap lists multi-language support (Java, C, C++) as an unchecked future-work item. -- evidence: [README.md#L212-L214](https://github.com/OpenBMB/RepoAgent/blob/825d988127d7bfd757237d9c4e8678d9104030f0/README.md#L212-L214), [README.md#L163-L174](https://github.com/OpenBMB/RepoAgent/blob/825d988127d7bfd757237d9c4e8678d9104030f0/README.md#L163-L174) (`clm_28d14f54703e22b6494602c0cf978c2dced9bcb7e2dc9d5c5c3156f8431f738e`)
- [observation/documented] Chat With Repo is described as a preliminary prototype of one downstream task, with adapting its interface to various downstream applications left as future research. -- evidence: [README.md#L201-L201](https://github.com/OpenBMB/RepoAgent/blob/825d988127d7bfd757237d9c4e8678d9104030f0/README.md#L201-L201), [README.md#L203-L203](https://github.com/OpenBMB/RepoAgent/blob/825d988127d7bfd757237d9c4e8678d9104030f0/README.md#L203-L203) (`clm_6c1ec0a384781c6f1b2b87441c20cefd66f9e63d89b71add4f1cf4820af0c063`)

## relevance (1 claim(s))

- [observation/documented] RepoAgent is an LLM-powered framework for repository-level code documentation generation, published on PyPI and described in arXiv paper 2402.16667; its featured-cases section lists MiniCPM, ChatDev, XAgent, and EasyRL4Rec as projects that adopted it. -- evidence: [README.md#L1-L3](https://github.com/OpenBMB/RepoAgent/blob/825d988127d7bfd757237d9c4e8678d9104030f0/README.md#L1-L3), [README.md#L220-L223](https://github.com/OpenBMB/RepoAgent/blob/825d988127d7bfd757237d9c4e8678d9104030f0/README.md#L220-L223), [README.md#L5-L19](https://github.com/OpenBMB/RepoAgent/blob/825d988127d7bfd757237d9c4e8678d9104030f0/README.md#L5-L19), [README.md#L218-L218](https://github.com/OpenBMB/RepoAgent/blob/825d988127d7bfd757237d9c4e8678d9104030f0/README.md#L218-L218) (`clm_f2c59322a71d554b1bff78c3617f1fef62b1da11488d095044fd801a94a24b3a`)

