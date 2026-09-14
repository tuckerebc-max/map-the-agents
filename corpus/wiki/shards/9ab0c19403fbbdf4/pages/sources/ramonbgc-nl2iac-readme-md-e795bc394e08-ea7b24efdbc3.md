---
access: public
aliases: []
claim_ids:
- clm_39bafbb3dcbc8b72c11fa4e6235543f41ce2ed0b8596ec99b9fc8309aeb45c1c
- clm_5b148b74a73dee4e0eac99985ebd3b56963d779a8a2817247706f7b5cc92ddb1
- clm_73ce51a30d2822d906c2531e795df118f654146218476dd4669e4700d09c670e
- clm_9ed13ad6ab1da74e2cd375b3d181f68289c69d5f22a4eecc621136085a9f17df
- clm_af045db1eed66d3ca2e165208e9d0ed94617a8229c0abb408f14b422bf072906
- clm_d281f53a01f0ad43a699c825dd4a70443662d45cfd8c0b1ec12e6f74e27f793c
maturity: draft
page_id: pg_8d2533a3b3de5a7ebbd1ea7b24efdbc3
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_0d3024f36ae55e72b5c5f4403e72af9b
title: ramonbgc/nl2iac/README.md @ e795bc394e08
updated_at: '2026-09-14T03:12:09Z'
---

# ramonbgc/nl2iac/README.md @ e795bc394e08

<!-- rcw:begin owner=source:src_0d3024f36ae55e72b5c5f4403e72af9b block=evidence -->
- Installation involves optionally creating a Python virtualenv (recommended, not mandatory), cloning the repo, and installing requirements via pip. [@claim:clm_39bafbb3dcbc8b72c11fa4e6235543f41ce2ed0b8596ec99b9fc8309aeb45c1c]
- Configuration is supplied through a .streamlit/secrets.toml file whose values the user must fill in, indicating a Streamlit-based application. [@claim:clm_5b148b74a73dee4e0eac99985ebd3b56963d779a8a2817247706f7b5cc92ddb1]
- The agent targets GCP deployments, requiring a service account JSON path, GCP region, and project ID in its configuration. [@claim:clm_73ce51a30d2822d906c2531e795df118f654146218476dd4669e4700d09c670e]
- The tool supports Google Vertex AI (default model gemini-1.5-flash) and optionally OpenAI (default gpt-4o), with a MULTIPROVIDER setting and optional LangChain API key/project tracking. [@claim:clm_9ed13ad6ab1da74e2cd375b3d181f68289c69d5f22a4eecc621136085a9f17df]
- Dependencies include streamlit, langchain, langchain-google-vertexai, and langchain_openai, installed via pip from requirements.txt. [@claim:clm_af045db1eed66d3ca2e165208e9d0ed94617a8229c0abb408f14b422bf072906]
- The project is described as an AI agent for IaC deployments. [@claim:clm_d281f53a01f0ad43a699c825dd4a70443662d45cfd8c0b1ec12e6f74e27f793c]
<!-- rcw:end owner=source:src_0d3024f36ae55e72b5c5f4403e72af9b block=evidence -->

## Researcher notes

