# ramonbgc/nl2iac -- full detail

[Back to orientation](nl2iac.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/ramonbgc/nl2iac/e795bc394e082274218de0380356dd0eda38d298/8f051ae43830e9bb.json](../../../wiki/dossiers/ramonbgc/nl2iac/e795bc394e082274218de0380356dd0eda38d298/8f051ae43830e9bb.json)

## specifications (1 claim(s))

- [observation/documented] The project is described as an AI agent for IaC deployments. -- evidence: [README.md#L2-L2](https://github.com/ramonbgc/nl2iac/blob/e795bc394e082274218de0380356dd0eda38d298/README.md#L2-L2) (`clm_d281f53a01f0ad43a699c825dd4a70443662d45cfd8c0b1ec12e6f74e27f793c`)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (2 claim(s))

- [observation/documented] The tool supports Google Vertex AI (default model gemini-1.5-flash) and optionally OpenAI (default gpt-4o), with a MULTIPROVIDER setting and optional LangChain API key/project tracking. -- evidence: [README.md#L19-L29](https://github.com/ramonbgc/nl2iac/blob/e795bc394e082274218de0380356dd0eda38d298/README.md#L19-L29) (`clm_9ed13ad6ab1da74e2cd375b3d181f68289c69d5f22a4eecc621136085a9f17df`)
- [observation/documented] The agent targets GCP deployments, requiring a service account JSON path, GCP region, and project ID in its configuration. -- evidence: [README.md#L19-L29](https://github.com/ramonbgc/nl2iac/blob/e795bc394e082274218de0380356dd0eda38d298/README.md#L19-L29) (`clm_73ce51a30d2822d906c2531e795df118f654146218476dd4669e4700d09c670e`)

## workflows (1 claim(s))

- [observation/documented] Installation involves optionally creating a Python virtualenv (recommended, not mandatory), cloning the repo, and installing requirements via pip. -- evidence: [README.md#L12-L17](https://github.com/ramonbgc/nl2iac/blob/e795bc394e082274218de0380356dd0eda38d298/README.md#L12-L17), [README.md#L5-L10](https://github.com/ramonbgc/nl2iac/blob/e795bc394e082274218de0380356dd0eda38d298/README.md#L5-L10) (`clm_39bafbb3dcbc8b72c11fa4e6235543f41ce2ed0b8596ec99b9fc8309aeb45c1c`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] Configuration is supplied through a .streamlit/secrets.toml file whose values the user must fill in, indicating a Streamlit-based application. -- evidence: [README.md#L12-L17](https://github.com/ramonbgc/nl2iac/blob/e795bc394e082274218de0380356dd0eda38d298/README.md#L12-L17), [README.md#L19-L29](https://github.com/ramonbgc/nl2iac/blob/e795bc394e082274218de0380356dd0eda38d298/README.md#L19-L29) (`clm_5b148b74a73dee4e0eac99985ebd3b56963d779a8a2817247706f7b5cc92ddb1`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Dependencies include streamlit, langchain, langchain-google-vertexai, and langchain_openai, installed via pip from requirements.txt. -- evidence: [README.md#L12-L17](https://github.com/ramonbgc/nl2iac/blob/e795bc394e082274218de0380356dd0eda38d298/README.md#L12-L17), [requirements.txt#L1-L4](https://github.com/ramonbgc/nl2iac/blob/e795bc394e082274218de0380356dd0eda38d298/requirements.txt#L1-L4) (`clm_af045db1eed66d3ca2e165208e9d0ed94617a8229c0abb408f14b422bf072906`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

