---
access: public
aliases: []
claim_ids:
- clm_12a1372bb5b9fddb47224483faf9b9c536614ecf069e64cee660d720f2cbafc7
- clm_1caada7e65f0ac390375356fa8fb6fb89f612fc880b7f0c08e0b80d1b0332dfa
- clm_27d632329ae4d7a2c4ca1eb771958e16c0578fd0dfd25ae88ebf6eaff153a42c
- clm_575569ac1f654cb1b650ab5a966ce5b41c46a2c31b535458b568122fd9bec913
- clm_62295c94ca81998249e9e5176f0c696e35b715d1ea43662cd02e11e663972c9c
- clm_7445708ba73ddc6a739174b65ac88ef7ca48cf1a8d9859ed3f22b0e47b929dca
- clm_8d16739bb680d63034229d0a977acd75bdcb86ba0310d462c3adb2319bff10f9
- clm_9ea47ce7a35356fd82e766f1ed905406b80c4fa9f087ceb8377fda8f984c7a41
- clm_bde8db0239c07b43d3b7867db1f336da3b5fc305016b0685a92a74a9e61380d4
- clm_cc9d2c2d1251526425d2eb443d378ee55b919a0947cb1dfedde8b265099cd495
- clm_ee6d1dcc4eafe287ba598b4617af5e94a9b3edd859451e67d8445edbb6ec5d0c
maturity: draft
page_id: pg_956e1b5a89225fcd93849ceea24df1bc
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_f399ba6cbfaa54aebf78ca04e6e21d98
title: mac999/BIM_LLM_code_agent/README.md @ 4aaa4458ec63
updated_at: '2026-09-14T02:14:56Z'
---

# mac999/BIM_LLM_code_agent/README.md @ 4aaa4458ec63

<!-- rcw:begin owner=source:src_f399ba6cbfaa54aebf78ca04e6e21d98 block=evidence -->
- The tool supports multiple file formats including IFC, PDF, JSON, TXT, and CSV. [@claim:clm_12a1372bb5b9fddb47224483faf9b9c536614ecf069e64cee660d720f2cbafc7]
- The author states the project is not perfect: behavior depends on parameters like LLM type, and it sometimes hallucinates or generates incomplete code, suggesting fixes via function calls, fine-tuning, and RAG. [@claim:clm_1caada7e65f0ac390375356fa8fb6fb89f612fc880b7f0c08e0b80d1b0332dfa]
- Setup involves cloning the repo, manually pip-installing libraries, creating a .env with API keys (OpenAI, LangChain, Tavily, HF token), and pulling Ollama models such as codegemma:7b and qwen2.5-coder:7b. [@claim:clm_27d632329ae4d7a2c4ca1eb771958e16c0578fd0dfd25ae88ebf6eaff153a42c]
- The stated purpose includes checking LLM agent performance on BIM tasks, but no benchmark results or metrics appear in the provided evidence. [@claim:clm_575569ac1f654cb1b650ab5a966ce5b41c46a2c31b535458b568122fd9bec913]
- Features include natural-language BIM query handling, automatic Python code generation, a Streamlit web interface, and generation of tables, charts, and summaries. [@claim:clm_62295c94ca81998249e9e5176f0c696e35b715d1ea43662cd02e11e663972c9c]
- Uploaded files are automatically processed for vectorized searches, implying a vector-store-backed memory over user documents (faiss-cpu/chromadb are listed dependencies). [@claim:clm_7445708ba73ddc6a739174b65ac88ef7ca48cf1a8d9859ed3f22b0e47b929dca]
- It uses a multi-agent LangChain system integrating LLMs, memory, and vector stores, plus a custom LangChain chain specialized for BIM queries. [@claim:clm_8d16739bb680d63034229d0a977acd75bdcb86ba0310d462c3adb2319bff10f9]
- The project combines BIM with LLMs to handle queries and automate tasks on BIM/IFC files, aimed at evaluating LLM agent performance on complex IFC data for a paper. [@claim:clm_9ea47ce7a35356fd82e766f1ed905406b80c4fa9f087ceb8377fda8f984c7a41]
- The product is launched via 'streamlit run bim_code_agent_app.py' and accessed in a browser at http://localhost:8501. [@claim:clm_bde8db0239c07b43d3b7867db1f336da3b5fc305016b0685a92a74a9e61380d4]
- Prerequisites are Python 3.8+, an OpenAI API key, and an Ollama installation; LangChain and Tavily API keys are optional for extra features. [@claim:clm_cc9d2c2d1251526425d2eb443d378ee55b919a0947cb1dfedde8b265099cd495]
- Repository development practice: contributors are asked to fork the repository, create a feature branch, and submit a pull request with a clear explanation of changes. [@claim:clm_ee6d1dcc4eafe287ba598b4617af5e94a9b3edd859451e67d8445edbb6ec5d0c]
<!-- rcw:end owner=source:src_f399ba6cbfaa54aebf78ca04e6e21d98 block=evidence -->

## Researcher notes

