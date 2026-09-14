# euniai/prometheus

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit acb83608ed7f @ 92d9be3a6b219c10

## Summary (orientation draft, not independently verified)

Prometheus is a LangGraph-based multi-agent platform for repository-level issue resolution, using a Neo4j knowledge graph and Docker-isolated validation, with documented SWE-Bench evaluation results. Evidence is mostly README/docs; no source code slices are present.

## Source coverage

Source coverage (complete): 5 of 5 candidate file(s) selected; repository tree complete. Claims by basis: 13 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

13 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Prometheus is described as a platform using unified knowledge graphs and multi-agent systems to operate on multilingual codebases, built on LangGraph state machines. -- evidence: [README.md#L90-L90](https://github.com/EuniAI/Prometheus/blob/acb83608ed7fcf3737a967f3059b799bbc3d2b6f/README.md#L90-L90)
- components (1 claim(s)):
  - [observation/documented] Core components include a Tree-sitter-based AST/semantic knowledge graph in Neo4j, LangGraph state machines with checkpointing, Docker containers for isolated build/test execution, and multi-tier LLM integration (GPT-4, Claude, Gemini). -- evidence: [README.md#L167-L171](https://github.com/EuniAI/Prometheus/blob/acb83608ed7fcf3737a967f3059b799bbc3d2b6f/README.md#L167-L171)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributors use ruff for linting/formatting, must write tests for every change, run the pytest suite (excluding git-marked tests) with coverage before pushing, and submit PRs that pass CI and maintainer review. -- evidence: [CONTRIBUTING.md#L71-L73](https://github.com/EuniAI/Prometheus/blob/acb83608ed7fcf3737a967f3059b799bbc3d2b6f/CONTRIBUTING.md#L71-L73), [CONTRIBUTING.md#L58-L60](https://github.com/EuniAI/Prometheus/blob/acb83608ed7fcf3737a967f3059b799bbc3d2b6f/CONTRIBUTING.md#L58-L60), [CONTRIBUTING.md#L31-L32](https://github.com/EuniAI/Prometheus/blob/acb83608ed7fcf3737a967f3059b799bbc3d2b6f/CONTRIBUTING.md#L31-L32), [CONTRIBUTING.md#L46-L50](https://github.com/EuniAI/Prometheus/blob/acb83608ed7fcf3737a967f3059b799bbc3d2b6f/CONTRIBUTING.md#L46-L50), [CONTRIBUTING.md#L43-L44](https://github.com/EuniAI/Prometheus/blob/acb83608ed7fcf3737a967f3059b799bbc3d2b6f/CONTRIBUTING.md#L43-L44)
- skills-patterns (2 claim(s)):
  - [observation/documented] The bug reproduction agent generates reproduction tests via LLM, executes them in Docker, evaluates success, and retries with feedback in iterative loops. -- evidence: [docs/Multi-Agent-Architecture.md#L56-L59](https://github.com/EuniAI/Prometheus/blob/acb83608ed7fcf3737a967f3059b799bbc3d2b6f/docs/Multi-Agent-Architecture.md#L56-L59), [docs/Multi-Agent-Architecture.md#L42-L48](https://github.com/EuniAI/Prometheus/blob/acb83608ed7fcf3737a967f3059b799bbc3d2b6f/docs/Multi-Agent-Architecture.md#L42-L48)
  - [observation/documented] The issue resolution agent generates multiple candidate patches, validates them against reproduction tests (required) plus optional regression and existing tests, and selects the best patch using an LLM with retry on failure. -- evidence: [docs/Multi-Agent-Architecture.md#L91-L102](https://github.com/EuniAI/Prometheus/blob/acb83608ed7fcf3737a967f3059b799bbc3d2b6f/docs/Multi-Agent-Architecture.md#L91-L102), [docs/Multi-Agent-Architecture.md#L108-L112](https://github.com/EuniAI/Prometheus/blob/acb83608ed7fcf3737a967f3059b799bbc3d2b6f/docs/Multi-Agent-Architecture.md#L108-L112)
- interfaces (2 claim(s)):
  - [observation/documented] The platform exposes an API at localhost:9002 under /v1.2 with interactive docs at /docs, and requires a JWT secret generated via a provided script for authentication. -- evidence: [README.md#L199-L203](https://github.com/EuniAI/Prometheus/blob/acb83608ed7fcf3737a967f3059b799bbc3d2b6f/README.md#L199-L203), [README.md#L215-L217](https://github.com/EuniAI/Prometheus/blob/acb83608ed7fcf3737a967f3059b799bbc3d2b6f/README.md#L215-L217)
  - [observation/documented] A github_issue_debug.py script accepts a GitHub token, repo, and issue number, with optional flags for build/test/reproduction/regression validation, Docker environment configuration, candidate patch count, and pushing fixes to a remote branch. -- evidence: [docs/GitHub-Issue-Debug-Guide.md#L39-L56](https://github.com/EuniAI/Prometheus/blob/acb83608ed7fcf3737a967f3059b799bbc3d2b6f/docs/GitHub-Issue-Debug-Guide.md#L39-L56), [docs/GitHub-Issue-Debug-Guide.md#L84-L84](https://github.com/EuniAI/Prometheus/blob/acb83608ed7fcf3737a967f3059b799bbc3d2b6f/docs/GitHub-Issue-Debug-Guide.md#L84-L84), [docs/GitHub-Issue-Debug-Guide.md#L70-L74](https://github.com/EuniAI/Prometheus/blob/acb83608ed7fcf3737a967f3059b799bbc3d2b6f/docs/GitHub-Issue-Debug-Guide.md#L70-L74), [docs/GitHub-Issue-Debug-Guide.md#L77-L81](https://github.com/EuniAI/Prometheus/blob/acb83608ed7fcf3737a967f3059b799bbc3d2b6f/docs/GitHub-Issue-Debug-Guide.md#L77-L81)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (2 claim(s)):
  - [observation/documented] A hierarchical multi-agent system routes user issues through a classification agent into bug, feature, and question pipelines, each with specialized downstream agents. -- evidence: [README.md#L131-L131](https://github.com/EuniAI/Prometheus/blob/acb83608ed7fcf3737a967f3059b799bbc3d2b6f/README.md#L131-L131), [README.md#L133-L165](https://github.com/EuniAI/Prometheus/blob/acb83608ed7fcf3737a967f3059b799bbc3d2b6f/README.md#L133-L165)
  - [observation/documented] Agents communicate through shared LangGraph state: each subgraph has a typed state dictionary, state flows through nodes, child subgraphs inherit parent state, and results return via state. -- evidence: [docs/Multi-Agent-Architecture.md#L157-L160](https://github.com/EuniAI/Prometheus/blob/acb83608ed7fcf3737a967f3059b799bbc3d2b6f/docs/Multi-Agent-Architecture.md#L157-L160), [docs/Multi-Agent-Architecture.md#L155-L155](https://github.com/EuniAI/Prometheus/blob/acb83608ed7fcf3737a967f3059b799bbc3d2b6f/docs/Multi-Agent-Architecture.md#L155-L155)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation (2 claim(s)):
More evidence: [full detail](prometheus.detail.md)

Metadata and full claim list: [full detail](prometheus.detail.md)
Human notes ([notes](prometheus.notes.md), never overwritten by build)

[Back to map index](../../index.md)
