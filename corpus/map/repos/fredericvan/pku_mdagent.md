# fredericvan/pku_mdagent

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 83fc74947c72 @ ba6c3f9e62616f21

## Summary (orientation draft, not independently verified)

MDAgent is a Peking University multi-agent LLM system (built on AutoGen) that generates, executes, and refines LAMMPS thermodynamic simulation code, with fine-tuning as the primary knowledge-integration method and RAGFlow-based RAG as an optional tool. Evidence is mostly README documentation; no code files are included in the snapshot.

## Source coverage

Source coverage (partial): 3 of 4 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 17 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

17 claim(s) across 10 facet(s); 3 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The system comprises a User Proxy Agent, Planner Agent, LAMMPS Worker Agent, LAMMPS Evaluator Agent, and a GroupChatManager coordinating agent communication and workflow. -- evidence: [README.md#L312-L330](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/README.md#L312-L330)
- design-choices (2 claim(s)):
  - [observation/documented] To mitigate LLM hallucinations and factual errors, the design uses an Actor-Critic (Worker-Evaluator) loop plus human-in-the-loop review, with the Evaluator prompt augmented by expert-summarized error types. -- evidence: [README.md#L365-L365](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/README.md#L365-L365), [README.md#L367-L367](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/README.md#L367-L367), [README.md#L361-L361](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/README.md#L361-L361), [README.md#L363-L363](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/README.md#L363-L363)
  - [observation/documented] Fine-tuning was chosen over RAG as the primary knowledge-integration method because RAG could not provide the parameter-level syntactic understanding needed for valid LAMMPS code; RAG is kept as an optional alternative. -- evidence: [README.md#L260-L260](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/README.md#L260-L260), [README.md#L236-L236](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/README.md#L236-L236), [README.md#L254-L254](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/README.md#L254-L254)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: the docs site deploys via GitHub Actions on pushes to main (or alternatively directly from the /docs folder), and can be previewed locally with 'python -m http.server 8000' from the docs directory. -- evidence: [docs/README.md#L13-L13](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/docs/README.md#L13-L13), [docs/DEPLOY.md#L29-L31](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/docs/DEPLOY.md#L29-L31), [docs/README.md#L11-L11](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/docs/README.md#L11-L11), [docs/DEPLOY.md#L16-L21](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/docs/DEPLOY.md#L16-L21), [docs/DEPLOY.md#L5-L8](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/docs/DEPLOY.md#L5-L8), [docs/README.md#L17-L17](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/docs/README.md#L17-L17), [docs/README.md#L7-L9](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/docs/README.md#L7-L9), [docs/README.md#L19-L22](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/docs/README.md#L19-L22)
- skills-patterns (2 claim(s)):
  - [observation/documented] The LSCF dataset contains 167 LAMMPS scripts with instruction/input/output fields, organized into Initialization, Modeling, and Computation sections, sourced from manual work, official docs, and online repositories. -- evidence: [README.md#L55-L55](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/README.md#L55-L55), [README.md#L61-L63](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/README.md#L61-L63), [README.md#L67-L72](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/README.md#L67-L72), [README.md#L57-L57](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/README.md#L57-L57)
  - [observation/documented] Fine-tuning uses the unsloth framework with QLoRA 4-bit quantization, 4096-token context, on Meta-Llama-3.1-8B-Instruct as the LammpsWorker LLM, with an alpaca-style prompt template. -- evidence: [README.md#L248-L248](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/README.md#L248-L248), [README.md#L242-L242](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/README.md#L242-L242), [README.md#L244-L244](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/README.md#L244-L244)
- interfaces (2 claim(s)):
  - [observation/documented] The user interacts through a Panel web UI served via 'panel serve material_system_UI.py', accessible by default at http://localhost:5006/material_system_UI, using dialogue-based interaction. -- evidence: [README.md#L214-L214](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/README.md#L214-L214), [README.md#L210-L210](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/README.md#L210-L210), [README.md#L206-L208](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/README.md#L206-L208)
  - [observation/documented] The underlying LLM is selectable: an online model such as GPT-4o-mini via OPENAI_API_KEY, or a local model deployed with Ollama (e.g., llama3.1:8b-instruct-q6_K with api_type 'ollama'). -- evidence: [README.md#L190-L190](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/README.md#L190-L190), [README.md#L182-L182](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/README.md#L182-L182), [README.md#L184-L184](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/README.md#L184-L184), [README.md#L192-L202](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/README.md#L192-L202)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (2 claim(s)):
  - [observation/documented] MDAgent is a multi-agent collaborative system built on Microsoft's AutoGen framework for materials-science simulation and analysis tasks. -- evidence: [README.md#L304-L304](https://github.com/FredericVAN/PKU_MDAgent/blob/83fc74947c72042c61c386adbc4faa5da1a44917/README.md#L304-L304)
More evidence: [full detail](pku_mdagent.detail.md)

Metadata and full claim list: [full detail](pku_mdagent.detail.md)
Human notes ([notes](pku_mdagent.notes.md), never overwritten by build)

[Back to map index](../../index.md)
