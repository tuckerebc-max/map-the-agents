# ramonbgc/nl2iac

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit e795bc394e08 @ 8f051ae43830e9bb

## Summary (orientation draft, not independently verified)

The snapshot shows a Python/Streamlit-based AI agent for IaC deployments, configurable via .streamlit/secrets.toml for GCP/Vertex AI (Gemini) or OpenAI models, with LangChain integration. Evidence is limited to README installation steps and requirements; no runtime behavior, architecture, or evaluation details are present.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 6 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

6 claim(s) across 5 facet(s); 8 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] The project is described as an AI agent for IaC deployments. -- evidence: [README.md#L2-L2](https://github.com/ramonbgc/nl2iac/blob/e795bc394e082274218de0380356dd0eda38d298/README.md#L2-L2)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (2 claim(s)):
  - [observation/documented] The tool supports Google Vertex AI (default model gemini-1.5-flash) and optionally OpenAI (default gpt-4o), with a MULTIPROVIDER setting and optional LangChain API key/project tracking. -- evidence: [README.md#L19-L29](https://github.com/ramonbgc/nl2iac/blob/e795bc394e082274218de0380356dd0eda38d298/README.md#L19-L29)
  - [observation/documented] The agent targets GCP deployments, requiring a service account JSON path, GCP region, and project ID in its configuration. -- evidence: [README.md#L19-L29](https://github.com/ramonbgc/nl2iac/blob/e795bc394e082274218de0380356dd0eda38d298/README.md#L19-L29)
- workflows (1 claim(s)):
  - [observation/documented] Installation involves optionally creating a Python virtualenv (recommended, not mandatory), cloning the repo, and installing requirements via pip. -- evidence: [README.md#L12-L17](https://github.com/ramonbgc/nl2iac/blob/e795bc394e082274218de0380356dd0eda38d298/README.md#L12-L17), [README.md#L5-L10](https://github.com/ramonbgc/nl2iac/blob/e795bc394e082274218de0380356dd0eda38d298/README.md#L5-L10)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] Configuration is supplied through a .streamlit/secrets.toml file whose values the user must fill in, indicating a Streamlit-based application. -- evidence: [README.md#L12-L17](https://github.com/ramonbgc/nl2iac/blob/e795bc394e082274218de0380356dd0eda38d298/README.md#L12-L17), [README.md#L19-L29](https://github.com/ramonbgc/nl2iac/blob/e795bc394e082274218de0380356dd0eda38d298/README.md#L19-L29)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] Dependencies include streamlit, langchain, langchain-google-vertexai, and langchain_openai, installed via pip from requirements.txt. -- evidence: [README.md#L12-L17](https://github.com/ramonbgc/nl2iac/blob/e795bc394e082274218de0380356dd0eda38d298/README.md#L12-L17), [requirements.txt#L1-L4](https://github.com/ramonbgc/nl2iac/blob/e795bc394e082274218de0380356dd0eda38d298/requirements.txt#L1-L4)
- limitations: unknown (no source-linked claim submitted for this facet)
- relevance: unknown (no source-linked claim submitted for this facet)

Every claim for this repository is shown above and in [full detail](nl2iac.detail.md).

Metadata and full claim list: [full detail](nl2iac.detail.md)
Human notes ([notes](nl2iac.notes.md), never overwritten by build)

[Back to map index](../../index.md)
