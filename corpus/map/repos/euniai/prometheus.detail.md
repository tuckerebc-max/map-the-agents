# euniai/prometheus -- full detail

[Back to orientation](prometheus.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/euniai/prometheus/acb83608ed7fcf3737a967f3059b799bbc3d2b6f/92d9be3a6b219c10.json](../../../wiki/dossiers/euniai/prometheus/acb83608ed7fcf3737a967f3059b799bbc3d2b6f/92d9be3a6b219c10.json)

## specifications (1 claim(s))

- [observation/documented] Prometheus is described as a platform using unified knowledge graphs and multi-agent systems to operate on multilingual codebases, built on LangGraph state machines. -- evidence: [README.md#L90-L90](https://github.com/EuniAI/Prometheus/blob/acb83608ed7fcf3737a967f3059b799bbc3d2b6f/README.md#L90-L90) (`clm_f24e628244b609e8f03050cdd02509be783eb23a4b6003100befbf9856eb6a8b`)

## components (1 claim(s))

- [observation/documented] Core components include a Tree-sitter-based AST/semantic knowledge graph in Neo4j, LangGraph state machines with checkpointing, Docker containers for isolated build/test execution, and multi-tier LLM integration (GPT-4, Claude, Gemini). -- evidence: [README.md#L167-L171](https://github.com/EuniAI/Prometheus/blob/acb83608ed7fcf3737a967f3059b799bbc3d2b6f/README.md#L167-L171) (`clm_e1f3dc42594528ec303261e906a0baf377c6928c123868c8fba36b419c4f4f5b`)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributors use ruff for linting/formatting, must write tests for every change, run the pytest suite (excluding git-marked tests) with coverage before pushing, and submit PRs that pass CI and maintainer review. -- evidence: [CONTRIBUTING.md#L71-L73](https://github.com/EuniAI/Prometheus/blob/acb83608ed7fcf3737a967f3059b799bbc3d2b6f/CONTRIBUTING.md#L71-L73), [CONTRIBUTING.md#L58-L60](https://github.com/EuniAI/Prometheus/blob/acb83608ed7fcf3737a967f3059b799bbc3d2b6f/CONTRIBUTING.md#L58-L60), [CONTRIBUTING.md#L31-L32](https://github.com/EuniAI/Prometheus/blob/acb83608ed7fcf3737a967f3059b799bbc3d2b6f/CONTRIBUTING.md#L31-L32), [CONTRIBUTING.md#L46-L50](https://github.com/EuniAI/Prometheus/blob/acb83608ed7fcf3737a967f3059b799bbc3d2b6f/CONTRIBUTING.md#L46-L50), [CONTRIBUTING.md#L43-L44](https://github.com/EuniAI/Prometheus/blob/acb83608ed7fcf3737a967f3059b799bbc3d2b6f/CONTRIBUTING.md#L43-L44) (`clm_93af3b69be5a67192d4a10c2cebbb23eb021f6f6a3a7c3da0b34c38f0d4268f5`)

## skills-patterns (2 claim(s))

- [observation/documented] The bug reproduction agent generates reproduction tests via LLM, executes them in Docker, evaluates success, and retries with feedback in iterative loops. -- evidence: [docs/Multi-Agent-Architecture.md#L56-L59](https://github.com/EuniAI/Prometheus/blob/acb83608ed7fcf3737a967f3059b799bbc3d2b6f/docs/Multi-Agent-Architecture.md#L56-L59), [docs/Multi-Agent-Architecture.md#L42-L48](https://github.com/EuniAI/Prometheus/blob/acb83608ed7fcf3737a967f3059b799bbc3d2b6f/docs/Multi-Agent-Architecture.md#L42-L48) (`clm_a7d623e87abb0a1562618cd4240ed1d87148e8a53ebe6746e1e32feeac92dc4b`)
- [observation/documented] The issue resolution agent generates multiple candidate patches, validates them against reproduction tests (required) plus optional regression and existing tests, and selects the best patch using an LLM with retry on failure. -- evidence: [docs/Multi-Agent-Architecture.md#L91-L102](https://github.com/EuniAI/Prometheus/blob/acb83608ed7fcf3737a967f3059b799bbc3d2b6f/docs/Multi-Agent-Architecture.md#L91-L102), [docs/Multi-Agent-Architecture.md#L108-L112](https://github.com/EuniAI/Prometheus/blob/acb83608ed7fcf3737a967f3059b799bbc3d2b6f/docs/Multi-Agent-Architecture.md#L108-L112) (`clm_5c55f8bdb469d823199c245dca25af81d6ebc7bfe9ae38ce991fcdbc1122d8c4`)

## interfaces (2 claim(s))

- [observation/documented] The platform exposes an API at localhost:9002 under /v1.2 with interactive docs at /docs, and requires a JWT secret generated via a provided script for authentication. -- evidence: [README.md#L199-L203](https://github.com/EuniAI/Prometheus/blob/acb83608ed7fcf3737a967f3059b799bbc3d2b6f/README.md#L199-L203), [README.md#L215-L217](https://github.com/EuniAI/Prometheus/blob/acb83608ed7fcf3737a967f3059b799bbc3d2b6f/README.md#L215-L217) (`clm_610b7a0ed807e18a8ea126fb8583085a5b542e09b41c06192521ee77eebe7767`)
- [observation/documented] A github_issue_debug.py script accepts a GitHub token, repo, and issue number, with optional flags for build/test/reproduction/regression validation, Docker environment configuration, candidate patch count, and pushing fixes to a remote branch. -- evidence: [docs/GitHub-Issue-Debug-Guide.md#L39-L56](https://github.com/EuniAI/Prometheus/blob/acb83608ed7fcf3737a967f3059b799bbc3d2b6f/docs/GitHub-Issue-Debug-Guide.md#L39-L56), [docs/GitHub-Issue-Debug-Guide.md#L84-L84](https://github.com/EuniAI/Prometheus/blob/acb83608ed7fcf3737a967f3059b799bbc3d2b6f/docs/GitHub-Issue-Debug-Guide.md#L84-L84), [docs/GitHub-Issue-Debug-Guide.md#L70-L74](https://github.com/EuniAI/Prometheus/blob/acb83608ed7fcf3737a967f3059b799bbc3d2b6f/docs/GitHub-Issue-Debug-Guide.md#L70-L74), [docs/GitHub-Issue-Debug-Guide.md#L77-L81](https://github.com/EuniAI/Prometheus/blob/acb83608ed7fcf3737a967f3059b799bbc3d2b6f/docs/GitHub-Issue-Debug-Guide.md#L77-L81) (`clm_e64e8c54b5f173a19cbd4734210c46a2ac20efdfd85764d2bef4bdc46997b7a7`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (2 claim(s))

- [observation/documented] A hierarchical multi-agent system routes user issues through a classification agent into bug, feature, and question pipelines, each with specialized downstream agents. -- evidence: [README.md#L131-L131](https://github.com/EuniAI/Prometheus/blob/acb83608ed7fcf3737a967f3059b799bbc3d2b6f/README.md#L131-L131), [README.md#L133-L165](https://github.com/EuniAI/Prometheus/blob/acb83608ed7fcf3737a967f3059b799bbc3d2b6f/README.md#L133-L165) (`clm_ad90ae8c769ec7ef371aefe1c085123297b9665c82e7c558c6d36143f0943421`)
- [observation/documented] Agents communicate through shared LangGraph state: each subgraph has a typed state dictionary, state flows through nodes, child subgraphs inherit parent state, and results return via state. -- evidence: [docs/Multi-Agent-Architecture.md#L157-L160](https://github.com/EuniAI/Prometheus/blob/acb83608ed7fcf3737a967f3059b799bbc3d2b6f/docs/Multi-Agent-Architecture.md#L157-L160), [docs/Multi-Agent-Architecture.md#L155-L155](https://github.com/EuniAI/Prometheus/blob/acb83608ed7fcf3737a967f3059b799bbc3d2b6f/docs/Multi-Agent-Architecture.md#L155-L155) (`clm_2481920edbd1cdf058591e47861baf814d430f893a4876f03c7f54ef5962a79e`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (2 claim(s))

- [observation/documented] An evaluation log records SWE-Bench results across versions and models, e.g. 28.67% resolved on SWE-Bench Lite (300 instances, DeepSeek V3) and 70% on SWE-bench_verified_lite (50 instances, GPT-5 + gpt-4o), with API costs tracked. -- evidence: [docs/Evaluation-log.md#L3-L11](https://github.com/EuniAI/Prometheus/blob/acb83608ed7fcf3737a967f3059b799bbc3d2b6f/docs/Evaluation-log.md#L3-L11) (`clm_f4bec26911ee8cdf34d9ca7413de627cb042465a80d6e690e18a3b3f3395aa4d`)
- [observation/documented] The README news section claims top-5 and top-1 rankings among GPT-5 agents on the SWE-bench leaderboard for automated software engineering as of 2025-11. -- evidence: [README.md#L83-L84](https://github.com/EuniAI/Prometheus/blob/acb83608ed7fcf3737a967f3059b799bbc3d2b6f/README.md#L83-L84) (`clm_b6dc40e2aa1b2397e4f838a476c907f7887851f5c228552c742d7e38030c53ba`)

## dependencies (1 claim(s))

- [observation/documented] Prerequisites include Docker and Docker Compose, Python 3.11+ for local development, and API keys for OpenAI, Anthropic, or Google Gemini; PostgreSQL and Neo4j are required services. -- evidence: [README.md#L259-L268](https://github.com/EuniAI/Prometheus/blob/acb83608ed7fcf3737a967f3059b799bbc3d2b6f/README.md#L259-L268), [README.md#L249-L257](https://github.com/EuniAI/Prometheus/blob/acb83608ed7fcf3737a967f3059b799bbc3d2b6f/README.md#L249-L257), [README.md#L181-L183](https://github.com/EuniAI/Prometheus/blob/acb83608ed7fcf3737a967f3059b799bbc3d2b6f/README.md#L181-L183) (`clm_714cdd3a88b182689ced3ed7c8102dfeccf237f985ab4eb7db6edc4125dc2da3`)

## limitations (1 claim(s))

- [observation/documented] The Environment Build Agent is documented as in-progress with only planned features (auto-detecting project type, installing dependencies, configuring build tools), and PR review, feature implementation, and documentation agents are listed as future enhancements. -- evidence: [docs/Multi-Agent-Architecture.md#L24-L24](https://github.com/EuniAI/Prometheus/blob/acb83608ed7fcf3737a967f3059b799bbc3d2b6f/docs/Multi-Agent-Architecture.md#L24-L24), [docs/Multi-Agent-Architecture.md#L28-L32](https://github.com/EuniAI/Prometheus/blob/acb83608ed7fcf3737a967f3059b799bbc3d2b6f/docs/Multi-Agent-Architecture.md#L28-L32), [docs/Multi-Agent-Architecture.md#L177-L180](https://github.com/EuniAI/Prometheus/blob/acb83608ed7fcf3737a967f3059b799bbc3d2b6f/docs/Multi-Agent-Architecture.md#L177-L180) (`clm_ffad3c20a3a1bdc9233b5338442c7b1002e6aedda687a51232a524c5b71af854`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

