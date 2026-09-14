# mac999/bim_llm_code_agent -- full detail

[Back to orientation](bim_llm_code_agent.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/mac999/bim_llm_code_agent/4aaa4458ec63bfd560c7cc0e010f0240ab61de75/0c046e61dd5c46bc.json](../../../wiki/dossiers/mac999/bim_llm_code_agent/4aaa4458ec63bfd560c7cc0e010f0240ab61de75/0c046e61dd5c46bc.json)

## specifications (1 claim(s))

- [observation/documented] The project combines BIM with LLMs to handle queries and automate tasks on BIM/IFC files, aimed at evaluating LLM agent performance on complex IFC data for a paper. -- evidence: [README.md#L3-L4](https://github.com/mac999/BIM_LLM_code_agent/blob/4aaa4458ec63bfd560c7cc0e010f0240ab61de75/README.md#L3-L4) (`clm_9ea47ce7a35356fd82e766f1ed905406b80c4fa9f087ceb8377fda8f984c7a41`)

## components (1 claim(s))

- [observation/documented] Features include natural-language BIM query handling, automatic Python code generation, a Streamlit web interface, and generation of tables, charts, and summaries. -- evidence: [README.md#L29-L33](https://github.com/mac999/BIM_LLM_code_agent/blob/4aaa4458ec63bfd560c7cc0e010f0240ab61de75/README.md#L29-L33) (`clm_62295c94ca81998249e9e5176f0c696e35b715d1ea43662cd02e11e663972c9c`)

## design-choices (1 claim(s))

- [observation/documented] It uses a multi-agent LangChain system integrating LLMs, memory, and vector stores, plus a custom LangChain chain specialized for BIM queries. -- evidence: [README.md#L118-L120](https://github.com/mac999/BIM_LLM_code_agent/blob/4aaa4458ec63bfd560c7cc0e010f0240ab61de75/README.md#L118-L120) (`clm_8d16739bb680d63034229d0a977acd75bdcb86ba0310d462c3adb2319bff10f9`)

## workflows (2 claim(s))

- [observation/documented] Setup involves cloning the repo, manually pip-installing libraries, creating a .env with API keys (OpenAI, LangChain, Tavily, HF token), and pulling Ollama models such as codegemma:7b and qwen2.5-coder:7b. -- evidence: [README.md#L63-L67](https://github.com/mac999/BIM_LLM_code_agent/blob/4aaa4458ec63bfd560c7cc0e010f0240ab61de75/README.md#L63-L67), [README.md#L56-L61](https://github.com/mac999/BIM_LLM_code_agent/blob/4aaa4458ec63bfd560c7cc0e010f0240ab61de75/README.md#L56-L61), [README.md#L69-L77](https://github.com/mac999/BIM_LLM_code_agent/blob/4aaa4458ec63bfd560c7cc0e010f0240ab61de75/README.md#L69-L77), [README.md#L79-L85](https://github.com/mac999/BIM_LLM_code_agent/blob/4aaa4458ec63bfd560c7cc0e010f0240ab61de75/README.md#L79-L85) (`clm_27d632329ae4d7a2c4ca1eb771958e16c0578fd0dfd25ae88ebf6eaff153a42c`)
- [observation/documented] Repository development practice: contributors are asked to fork the repository, create a feature branch, and submit a pull request with a clear explanation of changes. -- evidence: [README.md#L124-L127](https://github.com/mac999/BIM_LLM_code_agent/blob/4aaa4458ec63bfd560c7cc0e010f0240ab61de75/README.md#L124-L127) (`clm_ee6d1dcc4eafe287ba598b4617af5e94a9b3edd859451e67d8445edbb6ec5d0c`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The product is launched via 'streamlit run bim_code_agent_app.py' and accessed in a browser at http://localhost:8501. -- evidence: [README.md#L93-L94](https://github.com/mac999/BIM_LLM_code_agent/blob/4aaa4458ec63bfd560c7cc0e010f0240ab61de75/README.md#L93-L94), [README.md#L87-L91](https://github.com/mac999/BIM_LLM_code_agent/blob/4aaa4458ec63bfd560c7cc0e010f0240ab61de75/README.md#L87-L91) (`clm_bde8db0239c07b43d3b7867db1f336da3b5fc305016b0685a92a74a9e61380d4`)
- [observation/documented] The tool supports multiple file formats including IFC, PDF, JSON, TXT, and CSV. -- evidence: [README.md#L29-L33](https://github.com/mac999/BIM_LLM_code_agent/blob/4aaa4458ec63bfd560c7cc0e010f0240ab61de75/README.md#L29-L33) (`clm_12a1372bb5b9fddb47224483faf9b9c536614ecf069e64cee660d720f2cbafc7`)

## memory-state (1 claim(s))

- [inference/documented] Uploaded files are automatically processed for vectorized searches, implying a vector-store-backed memory over user documents (faiss-cpu/chromadb are listed dependencies). -- evidence: [README.md#L118-L120](https://github.com/mac999/BIM_LLM_code_agent/blob/4aaa4458ec63bfd560c7cc0e010f0240ab61de75/README.md#L118-L120), [requirements.txt#L15-L16](https://github.com/mac999/BIM_LLM_code_agent/blob/4aaa4458ec63bfd560c7cc0e010f0240ab61de75/requirements.txt#L15-L16) (`clm_7445708ba73ddc6a739174b65ac88ef7ca48cf1a8d9859ed3f22b0e47b929dca`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (1 claim(s))

- [inference/documented] The stated purpose includes checking LLM agent performance on BIM tasks, but no benchmark results or metrics appear in the provided evidence. -- evidence: [README.md#L3-L4](https://github.com/mac999/BIM_LLM_code_agent/blob/4aaa4458ec63bfd560c7cc0e010f0240ab61de75/README.md#L3-L4) (`clm_575569ac1f654cb1b650ab5a966ce5b41c46a2c31b535458b568122fd9bec913`)

## dependencies (2 claim(s))

- [observation/documented] Requirements include LangChain packages, openai/ollama, faiss-cpu and chromadb vector stores, ifcopenshell/pyvista, streamlit, and tavily-python. -- evidence: [requirements.txt#L32-L33](https://github.com/mac999/BIM_LLM_code_agent/blob/4aaa4458ec63bfd560c7cc0e010f0240ab61de75/requirements.txt#L32-L33), [requirements.txt#L39-L39](https://github.com/mac999/BIM_LLM_code_agent/blob/4aaa4458ec63bfd560c7cc0e010f0240ab61de75/requirements.txt#L39-L39), [requirements.txt#L11-L12](https://github.com/mac999/BIM_LLM_code_agent/blob/4aaa4458ec63bfd560c7cc0e010f0240ab61de75/requirements.txt#L11-L12), [requirements.txt#L15-L16](https://github.com/mac999/BIM_LLM_code_agent/blob/4aaa4458ec63bfd560c7cc0e010f0240ab61de75/requirements.txt#L15-L16), [requirements.txt#L5-L8](https://github.com/mac999/BIM_LLM_code_agent/blob/4aaa4458ec63bfd560c7cc0e010f0240ab61de75/requirements.txt#L5-L8), [requirements.txt#L36-L36](https://github.com/mac999/BIM_LLM_code_agent/blob/4aaa4458ec63bfd560c7cc0e010f0240ab61de75/requirements.txt#L36-L36) (`clm_3bfee2314a9c8e262100953ebcdc732fae064ef60bd1aa1d56a9914e8ea3d6ba`)
- [observation/documented] Prerequisites are Python 3.8+, an OpenAI API key, and an Ollama installation; LangChain and Tavily API keys are optional for extra features. -- evidence: [README.md#L49-L52](https://github.com/mac999/BIM_LLM_code_agent/blob/4aaa4458ec63bfd560c7cc0e010f0240ab61de75/README.md#L49-L52) (`clm_cc9d2c2d1251526425d2eb443d378ee55b919a0947cb1dfedde8b265099cd495`)

## limitations (1 claim(s))

- [observation/documented] The author states the project is not perfect: behavior depends on parameters like LLM type, and it sometimes hallucinates or generates incomplete code, suggesting fixes via function calls, fine-tuning, and RAG. -- evidence: [README.md#L3-L4](https://github.com/mac999/BIM_LLM_code_agent/blob/4aaa4458ec63bfd560c7cc0e010f0240ab61de75/README.md#L3-L4) (`clm_1caada7e65f0ac390375356fa8fb6fb89f612fc880b7f0c08e0b80d1b0332dfa`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

