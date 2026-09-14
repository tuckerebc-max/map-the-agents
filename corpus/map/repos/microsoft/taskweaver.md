# microsoft/taskweaver

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit d44ddef23f90 @ e3f1b857b4e7da9d

## Summary (orientation draft, not independently verified)

TaskWeaver is described as a code-first agent framework for planning and executing data analytics tasks, interpreting user requests as code snippets and coordinating plugin functions in a stateful manner. The project requires Python 3.10 or 3.11 per its README badge and states Python >= 3.10 is required for installation.

## Source coverage

Source coverage (partial): 6 of 53 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 19 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

19 claim(s) across 10 facet(s); 3 facet(s) unknown.

- specifications (2 claim(s)):
  - [observation/documented] TaskWeaver is described as a code-first agent framework for planning and executing data analytics tasks, interpreting user requests as code snippets and coordinating plugin functions in a stateful manner. -- evidence: [README.md#L13-L15](https://github.com/microsoft/TaskWeaver/blob/d44ddef23f90059fb17999d3095db4240e98f955/README.md#L13-L15)
  - [observation/documented] The project requires Python 3.10 or 3.11 per its README badge and states Python >= 3.10 is required for installation. -- evidence: [README.md#L7-L9](https://github.com/microsoft/TaskWeaver/blob/d44ddef23f90059fb17999d3095db4240e98f955/README.md#L7-L9), [README.md#L78-L79](https://github.com/microsoft/TaskWeaver/blob/d44ddef23f90059fb17999d3095db4240e98f955/README.md#L78-L79)
- components (2 claim(s)):
  - [observation/documented] Generated code is executed via a Jupyter Kernel, chosen as a well-established interactive computing tool supporting many languages. -- evidence: [website/docs/code_execution.md#L8-L11](https://github.com/microsoft/TaskWeaver/blob/d44ddef23f90059fb17999d3095db4240e98f955/website/docs/code_execution.md#L8-L11)
  - [observation/documented] Plugins consist of paired Python and YAML files in a plugins folder (e.g. ascii_render.py and ascii_render.yaml) with required fields such as parameters and returns; sample plugins include anomaly_detection, ascii_render, klarna_search, and tell_joke. -- evidence: [website/docs/FAQ.md#L76-L77](https://github.com/microsoft/TaskWeaver/blob/d44ddef23f90059fb17999d3095db4240e98f955/website/docs/FAQ.md#L76-L77), [website/docs/FAQ.md#L53-L60](https://github.com/microsoft/TaskWeaver/blob/d44ddef23f90059fb17999d3095db4240e98f955/website/docs/FAQ.md#L53-L60), [website/docs/FAQ.md#L64-L65](https://github.com/microsoft/TaskWeaver/blob/d44ddef23f90059fb17999d3095db4240e98f955/website/docs/FAQ.md#L64-L65)
- design-choices (2 claim(s)):
  - [observation/documented] The default executor Docker image contains only dependencies from requirements.txt; users needing extra packages must modify the Dockerfile at TaskWeaver/docker/ces_container/Dockerfile and rebuild. -- evidence: [website/docs/code_execution.md#L62-L64](https://github.com/microsoft/TaskWeaver/blob/d44ddef23f90059fb17999d3095db4240e98f955/website/docs/code_execution.md#L62-L64)
  - [observation/documented] Shared information is stored as attachments inside posts rather than a separate structure so that, if a round fails, its shared entries can be filtered out by round status, analogous to transaction logging. -- evidence: [website/docs/memory.md#L99-L102](https://github.com/microsoft/TaskWeaver/blob/d44ddef23f90059fb17999d3095db4240e98f955/website/docs/memory.md#L99-L102)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: installation from source involves cloning the repo and running pip install -r requirements.txt; earlier versions can be installed from release tags via pip install git+https://github.com/microsoft/TaskWeaver@<TAG>. -- evidence: [README.md#L85-L86](https://github.com/microsoft/TaskWeaver/blob/d44ddef23f90059fb17999d3095db4240e98f955/README.md#L85-L86), [README.md#L91-L94](https://github.com/microsoft/TaskWeaver/blob/d44ddef23f90059fb17999d3095db4240e98f955/README.md#L91-L94), [README.md#L88-L89](https://github.com/microsoft/TaskWeaver/blob/d44ddef23f90059fb17999d3095db4240e98f955/README.md#L88-L89)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] TaskWeaver can be used via a CLI (python -m taskweaver -p ./project/), a Web UI for demos, or imported as a library into existing projects. -- evidence: [README.md#L118-L121](https://github.com/microsoft/TaskWeaver/blob/d44ddef23f90059fb17999d3095db4240e98f955/README.md#L118-L121), [README.md#L139-L139](https://github.com/microsoft/TaskWeaver/blob/d44ddef23f90059fb17999d3095db4240e98f955/README.md#L139-L139), [README.md#L136-L136](https://github.com/microsoft/TaskWeaver/blob/d44ddef23f90059fb17999d3095db4240e98f955/README.md#L136-L136)
  - [observation/documented] LLM configuration is provided in a taskweaver_config.json file, e.g. llm.api_key and llm.model for OpenAI, with other LLMs and advanced configurations supported per the docs. -- evidence: [README.md#L107-L107](https://github.com/microsoft/TaskWeaver/blob/d44ddef23f90059fb17999d3095db4240e98f955/README.md#L107-L107), [README.md#L97-L97](https://github.com/microsoft/TaskWeaver/blob/d44ddef23f90059fb17999d3095db4240e98f955/README.md#L97-L97), [README.md#L100-L105](https://github.com/microsoft/TaskWeaver/blob/d44ddef23f90059fb17999d3095db4240e98f955/README.md#L100-L105)
- memory-state (3 claim(s)):
  - [observation/documented] Unlike frameworks that track only chat history, TaskWeaver preserves both chat history and code execution history including in-memory data, which it says helps with complex data like high-dimensional tables. -- evidence: [README.md#L17-L17](https://github.com/microsoft/TaskWeaver/blob/d44ddef23f90059fb17999d3095db4240e98f955/README.md#L17-L17)
More evidence: [full detail](taskweaver.detail.md)

Metadata and full claim list: [full detail](taskweaver.detail.md)
Human notes ([notes](taskweaver.notes.md), never overwritten by build)

[Back to map index](../../index.md)
