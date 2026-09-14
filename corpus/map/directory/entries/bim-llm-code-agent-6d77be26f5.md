# BIM_LLM_code_agent (`bim-llm-code-agent`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: mac999
- License: MIT
- Language: Python
- Interface: install=Clone repo, pip install dependencies, set up .env with API keys, pull Ollama models, run with streamlit run bim_code_agent_app.py
- Model providers: OpenAI, Ollama (CodeGemma, Qwen2.5-coder, Llama3, Gemma3), optionally LangChain/HuggingFace/Tavily via API keys
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: True (reported)
  - hooks: False (reported)
  - plan_mode: False (reported)

Repository map entry: [mac999/bim_llm_code_agent](../../repos/mac999/bim_llm_code_agent.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Open-source BIM (Building Information Modeling) LLM Code Agent tailored for the AEC (Architecture, Engineering, Construction) industry, bridging complex BIM/IFC file analysis and LLM-driven code generation/reasoning via Vector and Graph RAG. Acts as an interactive knowledge expert for BIM professionals to automate data extraction and visualization.

(captured site page body (agents/bim-llm-code-agent.md), not a verified repo-code finding)
BIM (Building Information Modeling) files in the IFC format are large, semantically dense structures that general-purpose coding tools handle poorly, so this research agent targets the AEC industry specifically. It answers natural-language questions about building models by generating and running Python code against ifcopenshell, supported by a LangChain multi-agent system with memory layers, FAISS vector stores, and a code knowledge base accessed through both Vector RAG and Graph RAG. It runs OpenAI models alongside local Ollama models (codegemma, qwen2.5-coder, llama3, llama3), and a Streamlit web UI makes it approachable for AEC professionals who do not write code. Outputs include extracted data tables and 2D/3D Plotly visualizations. The project is a research artifact tied to published academic work, actively iterated by its author with an English/Korean bilingual README, and used by BIM researchers and AEC practitioners exploring LLM-driven IFC analysis.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/bim-llm-code-agent.md)
