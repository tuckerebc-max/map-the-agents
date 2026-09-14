# md-ashraful-pramanik/mapcoder

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit c87e6d914d19 @ 2850d7b1842d8acf

## Summary (orientation draft, not independently verified)

MapCoder is a multi-agent LLM code-generation framework with retrieval, planning, coding, and debugging agents, evaluated on competitive-programming benchmarks; the README documents CLI usage, setup steps, and notes the repo is no longer maintained.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] MapCoder uses four LLM agents mirroring the human programming cycle: retrieval, planning, code generation, and debugging. -- evidence: [README.md#L27-L28](https://github.com/Md-Ashraful-Pramanik/MapCoder/blob/c87e6d914d196e12fa2b144882122459a4b98007/README.md#L27-L28), [README.md#L22-L23](https://github.com/Md-Ashraful-Pramanik/MapCoder/blob/c87e6d914d196e12fa2b144882122459a4b98007/README.md#L22-L23)
  - [observation/documented] The coding agent turns a plan into code, tests it on sample I/O, hands failures to the debugging agent, and otherwise predicts it as the final solution. -- evidence: [README.md#L35-L35](https://github.com/Md-Ashraful-Pramanik/MapCoder/blob/c87e6d914d196e12fa2b144882122459a4b98007/README.md#L35-L35)
- design-choices (3 claim(s)):
  - [observation/documented] The retrieval agent generates k user-defined similar problems using the LLM itself, without manual crafting or external retrieval models. -- evidence: [README.md#L31-L31](https://github.com/Md-Ashraful-Pramanik/MapCoder/blob/c87e6d914d196e12fa2b144882122459a4b98007/README.md#L31-L31)
  - [observation/documented] MapCoder features an adaptive agent traversal schema that dynamically routes among agents, e.g. iteratively fixing bugs, rather than a fixed pipeline. -- evidence: [README.md#L27-L28](https://github.com/Md-Ashraful-Pramanik/MapCoder/blob/c87e6d914d196e12fa2b144882122459a4b98007/README.md#L27-L28)
- workflows (2 claim(s)):
  - [observation/documented] Setup involves cloning the repo, creating a conda or python virtual environment, installing requirements.txt, and configuring a .env file from an example. -- evidence: [README.md#L73-L73](https://github.com/Md-Ashraful-Pramanik/MapCoder/blob/c87e6d914d196e12fa2b144882122459a4b98007/README.md#L73-L73), [README.md#L63-L66](https://github.com/Md-Ashraful-Pramanik/MapCoder/blob/c87e6d914d196e12fa2b144882122459a4b98007/README.md#L63-L66), [README.md#L68-L71](https://github.com/Md-Ashraful-Pramanik/MapCoder/blob/c87e6d914d196e12fa2b144882122459a4b98007/README.md#L68-L71)
  - [observation/documented] Running competitive datasets requires setting up ExecEval in a Docker container on port 5000, with configuration in src/evaluations/api_comm.py. -- evidence: [README.md#L85-L85](https://github.com/Md-Ashraful-Pramanik/MapCoder/blob/c87e6d914d196e12fa2b144882122459a4b98007/README.md#L85-L85)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] The CLI entry point is src/main.py with options such as --model, --dataset, and --strategy (e.g. ChatGPT, HumanEval, MapCoder). -- evidence: [README.md#L80-L83](https://github.com/Md-Ashraful-Pramanik/MapCoder/blob/c87e6d914d196e12fa2b144882122459a4b98007/README.md#L80-L83), [README.md#L75-L78](https://github.com/Md-Ashraful-Pramanik/MapCoder/blob/c87e6d914d196e12fa2b144882122459a4b98007/README.md#L75-L78)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation (1 claim(s)):
  - [observation/documented] Reported pass@1 results include HumanEval 93.9%, MBPP 83.1%, APPS 22.0%, CodeContests 28.5%, and xCodeEval 45.3%. -- evidence: [README.md#L44-L58](https://github.com/Md-Ashraful-Pramanik/MapCoder/blob/c87e6d914d196e12fa2b144882122459a4b98007/README.md#L44-L58), [README.md#L22-L23](https://github.com/Md-Ashraful-Pramanik/MapCoder/blob/c87e6d914d196e12fa2b144882122459a4b98007/README.md#L22-L23)
- dependencies (1 claim(s)):
  - [observation/documented] Dependencies include openai, google-generativeai, tiktoken, gensim, accelerate, and others listed in requirements.txt. -- evidence: [requirements.txt#L2-L15](https://github.com/Md-Ashraful-Pramanik/MapCoder/blob/c87e6d914d196e12fa2b144882122459a4b98007/requirements.txt#L2-L15)
- limitations (1 claim(s)):
  - [observation/documented] The maintainers state this repository will no longer be maintained, pointing users to an improved model called CodeSIM. -- evidence: [README.md#L15-L18](https://github.com/Md-Ashraful-Pramanik/MapCoder/blob/c87e6d914d196e12fa2b144882122459a4b98007/README.md#L15-L18)
- relevance (1 claim(s)):
  - [observation/documented] The work was accepted at ACL 2024, released under the MIT License, and has an associated arXiv paper (2405.11403). -- evidence: [README.md#L15-L18](https://github.com/Md-Ashraful-Pramanik/MapCoder/blob/c87e6d914d196e12fa2b144882122459a4b98007/README.md#L15-L18), [README.md#L8-L12](https://github.com/Md-Ashraful-Pramanik/MapCoder/blob/c87e6d914d196e12fa2b144882122459a4b98007/README.md#L8-L12), [README.md#L89-L96](https://github.com/Md-Ashraful-Pramanik/MapCoder/blob/c87e6d914d196e12fa2b144882122459a4b98007/README.md#L89-L96)

(1 additional claim(s) omitted for length; see [full detail](mapcoder.detail.md) for every claim.)

Metadata and full claim list: [full detail](mapcoder.detail.md)
Human notes ([notes](mapcoder.notes.md), never overwritten by build)

[Back to map index](../../index.md)
