# genia-dev/genia

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 39a206b85d84 @ b0f34378113763be

## Summary (orientation draft, not independently verified)

Selected evidence records: GeniA is built on OpenAI's function-calling capability (OpenAI or Azure) and requires an OpenAI API key to run. By default the product uses the gpt-3.5-turbo-0613 model; the FAQ notes gpt-4-0613 often gives better results but 3.5 was chosen as more cost-effective.

## Source coverage

Source coverage (partial): 6 of 19 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (1 claim(s)):
  - [observation/documented] The project positions the agent as a production-grade team member operating inside a team's Slack channel and executing tasks in the production environment on users' behalf. -- evidence: [README.md#L4-L15](https://github.com/genia-dev/GeniA/blob/39a206b85d84d72c8bab3ff1e724f821443e52ad/README.md#L4-L15), [README.md#L44-L44](https://github.com/genia-dev/GeniA/blob/39a206b85d84d72c8bab3ff1e724f821443e52ad/README.md#L44-L44)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: contributors fork the repo and submit pull requests, run tests with 'poetry run pytest tests', and can build/run the project via Docker or Poetry commands documented in the developer guide. -- evidence: [docs/developer-guide.md#L17-L19](https://github.com/genia-dev/GeniA/blob/39a206b85d84d72c8bab3ff1e724f821443e52ad/docs/developer-guide.md#L17-L19), [docs/developer-guide.md#L5-L9](https://github.com/genia-dev/GeniA/blob/39a206b85d84d72c8bab3ff1e724f821443e52ad/docs/developer-guide.md#L5-L9), [docs/developer-guide.md#L57-L59](https://github.com/genia-dev/GeniA/blob/39a206b85d84d72c8bab3ff1e724f821443e52ad/docs/developer-guide.md#L57-L59), [README.md#L124-L126](https://github.com/genia-dev/GeniA/blob/39a206b85d84d72c8bab3ff1e724f821443e52ad/README.md#L124-L126), [docs/developer-guide.md#L37-L39](https://github.com/genia-dev/GeniA/blob/39a206b85d84d72c8bab3ff1e724f821443e52ad/docs/developer-guide.md#L37-L39)
  - [observation/documented] Repository development practice: local setup requires copying .env.template to .env with OPENAI_API_KEY as the minimal secret, and the repo displays a CI workflow badge. -- evidence: [docs/developer-guide.md#L13-L13](https://github.com/genia-dev/GeniA/blob/39a206b85d84d72c8bab3ff1e724f821443e52ad/docs/developer-guide.md#L13-L13), [README.md#L1-L2](https://github.com/genia-dev/GeniA/blob/39a206b85d84d72c8bab3ff1e724f821443e52ad/README.md#L1-L2)
- skills-patterns (3 claim(s)):
  - [observation/documented] New tools are added via YAML specs following OpenAI JSON function-configuration standards, with usage guidance kept in a separate tools.yaml file. -- evidence: [docs/add-new-tool.md#L5-L6](https://github.com/genia-dev/GeniA/blob/39a206b85d84d72c8bab3ff1e724f821443e52ad/docs/add-new-tool.md#L5-L6)
  - [observation/documented] Tool specs support Python code tools (naming a class and method), URL tools performing GET requests via templated URLs, and OpenAPI Swagger-based integrations, the latter noted as still under development. -- evidence: [docs/add-new-tool.md#L22-L27](https://github.com/genia-dev/GeniA/blob/39a206b85d84d72c8bab3ff1e724f821443e52ad/docs/add-new-tool.md#L22-L27), [docs/add-new-tool.md#L12-L16](https://github.com/genia-dev/GeniA/blob/39a206b85d84d72c8bab3ff1e724f821443e52ad/docs/add-new-tool.md#L12-L16), [docs/add-new-tool.md#L29-L30](https://github.com/genia-dev/GeniA/blob/39a206b85d84d72c8bab3ff1e724f821443e52ad/docs/add-new-tool.md#L29-L30)
- interfaces (1 claim(s)):
  - [observation/documented] The product can run in three modes: a local terminal mode, a Slack app bot mode, and a Streamlit web app mode, per the developer guide and README. -- evidence: [docs/developer-guide.md#L17-L19](https://github.com/genia-dev/GeniA/blob/39a206b85d84d72c8bab3ff1e724f821443e52ad/docs/developer-guide.md#L17-L19), [docs/developer-guide.md#L45-L47](https://github.com/genia-dev/GeniA/blob/39a206b85d84d72c8bab3ff1e724f821443e52ad/docs/developer-guide.md#L45-L47), [README.md#L115-L117](https://github.com/genia-dev/GeniA/blob/39a206b85d84d72c8bab3ff1e724f821443e52ad/README.md#L115-L117), [README.md#L109-L111](https://github.com/genia-dev/GeniA/blob/39a206b85d84d72c8bab3ff1e724f821443e52ad/README.md#L109-L111), [docs/developer-guide.md#L51-L53](https://github.com/genia-dev/GeniA/blob/39a206b85d84d72c8bab3ff1e724f821443e52ad/docs/developer-guide.md#L51-L53), [docs/developer-guide.md#L23-L25](https://github.com/genia-dev/GeniA/blob/39a206b85d84d72c8bab3ff1e724f821443e52ad/docs/developer-guide.md#L23-L25)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
  - [observation/documented] GeniA is built on OpenAI's function-calling capability (OpenAI or Azure) and requires an OpenAI API key to run. -- evidence: [README.md#L32-L32](https://github.com/genia-dev/GeniA/blob/39a206b85d84d72c8bab3ff1e724f821443e52ad/README.md#L32-L32), [docs/faq.md#L3-L4](https://github.com/genia-dev/GeniA/blob/39a206b85d84d72c8bab3ff1e724f821443e52ad/docs/faq.md#L3-L4)
  - [observation/documented] By default the product uses the gpt-3.5-turbo-0613 model; the FAQ notes gpt-4-0613 often gives better results but 3.5 was chosen as more cost-effective. -- evidence: [docs/faq.md#L10-L11](https://github.com/genia-dev/GeniA/blob/39a206b85d84d72c8bab3ff1e724f821443e52ad/docs/faq.md#L10-L11)
- limitations (1 claim(s)):
More evidence: [full detail](genia.detail.md)

Metadata and full claim list: [full detail](genia.detail.md)
Human notes ([notes](genia.notes.md), never overwritten by build)

[Back to map index](../../index.md)
