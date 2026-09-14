# mac999/bim_llm_code_agent

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 4aaa4458ec63 @ 0c046e61dd5c46bc

## Summary (orientation draft, not independently verified)

README-only evidence for a BIM/LLM agent that answers natural-language queries about IFC files, generates Python code, and runs as a Streamlit app using LangChain, Ollama models, and RAG; limitations and contribution workflow are documented by the author.

## Source coverage

Source coverage (complete): 3 of 3 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] The project combines BIM with LLMs to handle queries and automate tasks on BIM/IFC files, aimed at evaluating LLM agent performance on complex IFC data for a paper. -- evidence: [README.md#L3-L4](https://github.com/mac999/BIM_LLM_code_agent/blob/4aaa4458ec63bfd560c7cc0e010f0240ab61de75/README.md#L3-L4)
- components (1 claim(s)):
  - [observation/documented] Features include natural-language BIM query handling, automatic Python code generation, a Streamlit web interface, and generation of tables, charts, and summaries. -- evidence: [README.md#L29-L33](https://github.com/mac999/BIM_LLM_code_agent/blob/4aaa4458ec63bfd560c7cc0e010f0240ab61de75/README.md#L29-L33)
- design-choices (1 claim(s)):
  - [observation/documented] It uses a multi-agent LangChain system integrating LLMs, memory, and vector stores, plus a custom LangChain chain specialized for BIM queries. -- evidence: [README.md#L118-L120](https://github.com/mac999/BIM_LLM_code_agent/blob/4aaa4458ec63bfd560c7cc0e010f0240ab61de75/README.md#L118-L120)
- workflows (2 claim(s)):
  - [observation/documented] Setup involves cloning the repo, manually pip-installing libraries, creating a .env with API keys (OpenAI, LangChain, Tavily, HF token), and pulling Ollama models such as codegemma:7b and qwen2.5-coder:7b. -- evidence: [README.md#L63-L67](https://github.com/mac999/BIM_LLM_code_agent/blob/4aaa4458ec63bfd560c7cc0e010f0240ab61de75/README.md#L63-L67), [README.md#L56-L61](https://github.com/mac999/BIM_LLM_code_agent/blob/4aaa4458ec63bfd560c7cc0e010f0240ab61de75/README.md#L56-L61), [README.md#L69-L77](https://github.com/mac999/BIM_LLM_code_agent/blob/4aaa4458ec63bfd560c7cc0e010f0240ab61de75/README.md#L69-L77), [README.md#L79-L85](https://github.com/mac999/BIM_LLM_code_agent/blob/4aaa4458ec63bfd560c7cc0e010f0240ab61de75/README.md#L79-L85)
  - [observation/documented] Repository development practice: contributors are asked to fork the repository, create a feature branch, and submit a pull request with a clear explanation of changes. -- evidence: [README.md#L124-L127](https://github.com/mac999/BIM_LLM_code_agent/blob/4aaa4458ec63bfd560c7cc0e010f0240ab61de75/README.md#L124-L127)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The product is launched via 'streamlit run bim_code_agent_app.py' and accessed in a browser at http://localhost:8501. -- evidence: [README.md#L93-L94](https://github.com/mac999/BIM_LLM_code_agent/blob/4aaa4458ec63bfd560c7cc0e010f0240ab61de75/README.md#L93-L94), [README.md#L87-L91](https://github.com/mac999/BIM_LLM_code_agent/blob/4aaa4458ec63bfd560c7cc0e010f0240ab61de75/README.md#L87-L91)
  - [observation/documented] The tool supports multiple file formats including IFC, PDF, JSON, TXT, and CSV. -- evidence: [README.md#L29-L33](https://github.com/mac999/BIM_LLM_code_agent/blob/4aaa4458ec63bfd560c7cc0e010f0240ab61de75/README.md#L29-L33)
- memory-state (1 claim(s)):
  - [inference/documented] Uploaded files are automatically processed for vectorized searches, implying a vector-store-backed memory over user documents (faiss-cpu/chromadb are listed dependencies). -- evidence: [README.md#L118-L120](https://github.com/mac999/BIM_LLM_code_agent/blob/4aaa4458ec63bfd560c7cc0e010f0240ab61de75/README.md#L118-L120), [requirements.txt#L15-L16](https://github.com/mac999/BIM_LLM_code_agent/blob/4aaa4458ec63bfd560c7cc0e010f0240ab61de75/requirements.txt#L15-L16)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation (1 claim(s)):
  - [inference/documented] The stated purpose includes checking LLM agent performance on BIM tasks, but no benchmark results or metrics appear in the provided evidence. -- evidence: [README.md#L3-L4](https://github.com/mac999/BIM_LLM_code_agent/blob/4aaa4458ec63bfd560c7cc0e010f0240ab61de75/README.md#L3-L4)
- dependencies (2 claim(s)):
  - [observation/documented] Requirements include LangChain packages, openai/ollama, faiss-cpu and chromadb vector stores, ifcopenshell/pyvista, streamlit, and tavily-python. -- evidence: [requirements.txt#L32-L33](https://github.com/mac999/BIM_LLM_code_agent/blob/4aaa4458ec63bfd560c7cc0e010f0240ab61de75/requirements.txt#L32-L33), [requirements.txt#L39-L39](https://github.com/mac999/BIM_LLM_code_agent/blob/4aaa4458ec63bfd560c7cc0e010f0240ab61de75/requirements.txt#L39-L39), [requirements.txt#L11-L12](https://github.com/mac999/BIM_LLM_code_agent/blob/4aaa4458ec63bfd560c7cc0e010f0240ab61de75/requirements.txt#L11-L12), [requirements.txt#L15-L16](https://github.com/mac999/BIM_LLM_code_agent/blob/4aaa4458ec63bfd560c7cc0e010f0240ab61de75/requirements.txt#L15-L16), [requirements.txt#L5-L8](https://github.com/mac999/BIM_LLM_code_agent/blob/4aaa4458ec63bfd560c7cc0e010f0240ab61de75/requirements.txt#L5-L8), [requirements.txt#L36-L36](https://github.com/mac999/BIM_LLM_code_agent/blob/4aaa4458ec63bfd560c7cc0e010f0240ab61de75/requirements.txt#L36-L36)
  - [observation/documented] Prerequisites are Python 3.8+, an OpenAI API key, and an Ollama installation; LangChain and Tavily API keys are optional for extra features. -- evidence: [README.md#L49-L52](https://github.com/mac999/BIM_LLM_code_agent/blob/4aaa4458ec63bfd560c7cc0e010f0240ab61de75/README.md#L49-L52)
- limitations (1 claim(s)):
More evidence: [full detail](bim_llm_code_agent.detail.md)

Metadata and full claim list: [full detail](bim_llm_code_agent.detail.md)
Human notes ([notes](bim_llm_code_agent.notes.md), never overwritten by build)

[Back to map index](../../index.md)
