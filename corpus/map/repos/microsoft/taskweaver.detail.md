# microsoft/taskweaver -- full detail

[Back to orientation](taskweaver.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/microsoft/taskweaver/d44ddef23f90059fb17999d3095db4240e98f955/e3f1b857b4e7da9d.json](../../../wiki/dossiers/microsoft/taskweaver/d44ddef23f90059fb17999d3095db4240e98f955/e3f1b857b4e7da9d.json)

## specifications (2 claim(s))

- [observation/documented] TaskWeaver is described as a code-first agent framework for planning and executing data analytics tasks, interpreting user requests as code snippets and coordinating plugin functions in a stateful manner. -- evidence: [README.md#L13-L15](https://github.com/microsoft/TaskWeaver/blob/d44ddef23f90059fb17999d3095db4240e98f955/README.md#L13-L15) (`clm_5ac28aad81a5ae6cfe17a91db831a4ac7d2ed9a3e3c3399ae4f4e0ff794fdd89`)
- [observation/documented] The project requires Python 3.10 or 3.11 per its README badge and states Python >= 3.10 is required for installation. -- evidence: [README.md#L7-L9](https://github.com/microsoft/TaskWeaver/blob/d44ddef23f90059fb17999d3095db4240e98f955/README.md#L7-L9), [README.md#L78-L79](https://github.com/microsoft/TaskWeaver/blob/d44ddef23f90059fb17999d3095db4240e98f955/README.md#L78-L79) (`clm_a571a048c660e12740a4e21bea33f2f7d58b575d9984f971272ff9a0f46a15e4`)

## components (2 claim(s))

- [observation/documented] Generated code is executed via a Jupyter Kernel, chosen as a well-established interactive computing tool supporting many languages. -- evidence: [website/docs/code_execution.md#L8-L11](https://github.com/microsoft/TaskWeaver/blob/d44ddef23f90059fb17999d3095db4240e98f955/website/docs/code_execution.md#L8-L11) (`clm_b9791d56140c2af904f104fcfccc03828779718c0bfc688a94a359169c36da58`)
- [observation/documented] Plugins consist of paired Python and YAML files in a plugins folder (e.g. ascii_render.py and ascii_render.yaml) with required fields such as parameters and returns; sample plugins include anomaly_detection, ascii_render, klarna_search, and tell_joke. -- evidence: [website/docs/FAQ.md#L76-L77](https://github.com/microsoft/TaskWeaver/blob/d44ddef23f90059fb17999d3095db4240e98f955/website/docs/FAQ.md#L76-L77), [website/docs/FAQ.md#L53-L60](https://github.com/microsoft/TaskWeaver/blob/d44ddef23f90059fb17999d3095db4240e98f955/website/docs/FAQ.md#L53-L60), [website/docs/FAQ.md#L64-L65](https://github.com/microsoft/TaskWeaver/blob/d44ddef23f90059fb17999d3095db4240e98f955/website/docs/FAQ.md#L64-L65) (`clm_de4997394b6bac68582e9ff37a7e6f7572b8560d37671d47cd46a1277cf262b5`)

## design-choices (2 claim(s))

- [observation/documented] The default executor Docker image contains only dependencies from requirements.txt; users needing extra packages must modify the Dockerfile at TaskWeaver/docker/ces_container/Dockerfile and rebuild. -- evidence: [website/docs/code_execution.md#L62-L64](https://github.com/microsoft/TaskWeaver/blob/d44ddef23f90059fb17999d3095db4240e98f955/website/docs/code_execution.md#L62-L64) (`clm_96cf7bbea9574367a22df3f9f87ee918392a2122c8322c91ab82c8c990096f1f`)
- [observation/documented] Shared information is stored as attachments inside posts rather than a separate structure so that, if a round fails, its shared entries can be filtered out by round status, analogous to transaction logging. -- evidence: [website/docs/memory.md#L99-L102](https://github.com/microsoft/TaskWeaver/blob/d44ddef23f90059fb17999d3095db4240e98f955/website/docs/memory.md#L99-L102) (`clm_40d8986fa5da28efbff70827ee87237f9817d18e424d619b5df06072ce1f0d6f`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: installation from source involves cloning the repo and running pip install -r requirements.txt; earlier versions can be installed from release tags via pip install git+https://github.com/microsoft/TaskWeaver@<TAG>. -- evidence: [README.md#L85-L86](https://github.com/microsoft/TaskWeaver/blob/d44ddef23f90059fb17999d3095db4240e98f955/README.md#L85-L86), [README.md#L91-L94](https://github.com/microsoft/TaskWeaver/blob/d44ddef23f90059fb17999d3095db4240e98f955/README.md#L91-L94), [README.md#L88-L89](https://github.com/microsoft/TaskWeaver/blob/d44ddef23f90059fb17999d3095db4240e98f955/README.md#L88-L89) (`clm_fac63becd8b56d8a01633b936fbf73e6d433f4fa8295809020f0cda8b533c1e8`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] TaskWeaver can be used via a CLI (python -m taskweaver -p ./project/), a Web UI for demos, or imported as a library into existing projects. -- evidence: [README.md#L118-L121](https://github.com/microsoft/TaskWeaver/blob/d44ddef23f90059fb17999d3095db4240e98f955/README.md#L118-L121), [README.md#L139-L139](https://github.com/microsoft/TaskWeaver/blob/d44ddef23f90059fb17999d3095db4240e98f955/README.md#L139-L139), [README.md#L136-L136](https://github.com/microsoft/TaskWeaver/blob/d44ddef23f90059fb17999d3095db4240e98f955/README.md#L136-L136) (`clm_e293afa843ba3217a57240a49c50f36ab825309a151c5e2327a4a597a426bb44`)
- [observation/documented] LLM configuration is provided in a taskweaver_config.json file, e.g. llm.api_key and llm.model for OpenAI, with other LLMs and advanced configurations supported per the docs. -- evidence: [README.md#L107-L107](https://github.com/microsoft/TaskWeaver/blob/d44ddef23f90059fb17999d3095db4240e98f955/README.md#L107-L107), [README.md#L97-L97](https://github.com/microsoft/TaskWeaver/blob/d44ddef23f90059fb17999d3095db4240e98f955/README.md#L97-L97), [README.md#L100-L105](https://github.com/microsoft/TaskWeaver/blob/d44ddef23f90059fb17999d3095db4240e98f955/README.md#L100-L105) (`clm_396041a641794214f945b7487fc15568d7f2fbaba9f8d8cb2414e95ec75585e1`)

## memory-state (3 claim(s))

- [observation/documented] Unlike frameworks that track only chat history, TaskWeaver preserves both chat history and code execution history including in-memory data, which it says helps with complex data like high-dimensional tables. -- evidence: [README.md#L17-L17](https://github.com/microsoft/TaskWeaver/blob/d44ddef23f90059fb17999d3095db4240e98f955/README.md#L17-L17) (`clm_60910a6d43a6c3bf0a3b78620a2f083192a2f3c9ab4ee2d91e81752d002e9516`)
- [observation/documented] The memory module stores conversation history between the user and roles plus a shared memory of information purposefully shared between roles; implementation is in taskweaver/memory/memory.py. -- evidence: [website/docs/memory.md#L8-L8](https://github.com/microsoft/TaskWeaver/blob/d44ddef23f90059fb17999d3095db4240e98f955/website/docs/memory.md#L8-L8), [website/docs/memory.md#L3-L6](https://github.com/microsoft/TaskWeaver/blob/d44ddef23f90059fb17999d3095db4240e98f955/website/docs/memory.md#L3-L6), [website/docs/memory.md#L10-L11](https://github.com/microsoft/TaskWeaver/blob/d44ddef23f90059fb17999d3095db4240e98f955/website/docs/memory.md#L10-L11) (`clm_65617be7cc443092f16b715769d1c8ba4c472c67e2cc8a14e50d89c7ac331e0d`)
- [observation/documented] Shared memory entries are attachments on posts with fields type, content, scope ('round' or 'conversation'), and id; round-scoped entries expire with the round, and later entries with the same type from a role overwrite earlier ones. -- evidence: [website/docs/memory.md#L104-L106](https://github.com/microsoft/TaskWeaver/blob/d44ddef23f90059fb17999d3095db4240e98f955/website/docs/memory.md#L104-L106), [website/docs/memory.md#L87-L93](https://github.com/microsoft/TaskWeaver/blob/d44ddef23f90059fb17999d3095db4240e98f955/website/docs/memory.md#L87-L93), [website/docs/memory.md#L95-L97](https://github.com/microsoft/TaskWeaver/blob/d44ddef23f90059fb17999d3095db4240e98f955/website/docs/memory.md#L95-L97), [website/docs/memory.md#L83-L85](https://github.com/microsoft/TaskWeaver/blob/d44ddef23f90059fb17999d3095db4240e98f955/website/docs/memory.md#L83-L85) (`clm_d85f192d45fff6877b53c81a35024e91c2e8c587342b861ab086c11abcf961ba`)

## orchestration (2 claim(s))

- [observation/documented] Roles are orchestrated in a star topology with the Planner at the center: the User interacts only with the Planner, which plans and instructs peripheral roles, each of which knows only the Planner. -- evidence: [website/docs/memory.md#L34-L36](https://github.com/microsoft/TaskWeaver/blob/d44ddef23f90059fb17999d3095db4240e98f955/website/docs/memory.md#L34-L36), [website/docs/memory.md#L17-L20](https://github.com/microsoft/TaskWeaver/blob/d44ddef23f90059fb17999d3095db4240e98f955/website/docs/memory.md#L17-L20) (`clm_6060f9975e9a49c013a25c77253d1df82e520bbffe6a51cee50227af4cb264b1`)
- [observation/documented] In the default flow, the user query goes to the Planner, which generates a plan for the CodeInterpreter; the interpreter executes and returns results, and the Planner summarizes them back, possibly iterating multiple times. -- evidence: [website/docs/FAQ.md#L12-L17](https://github.com/microsoft/TaskWeaver/blob/d44ddef23f90059fb17999d3095db4240e98f955/website/docs/FAQ.md#L12-L17), [website/docs/FAQ.md#L5-L10](https://github.com/microsoft/TaskWeaver/blob/d44ddef23f90059fb17999d3095db4240e98f955/website/docs/FAQ.md#L5-L10) (`clm_95887d86b45a2639936f150f85a3c2ec68c930febe311c533d8f4ef8eb820c9b`)

## tools-permissions (2 claim(s))

- [observation/documented] Code execution supports 'local' and 'container' modes; container mode (the default) runs code in a Docker container for a more secure environment, while local mode runs code as a subprocess and could let malicious users or LLM-generated code harm the host. -- evidence: [website/docs/code_execution.md#L15-L21](https://github.com/microsoft/TaskWeaver/blob/d44ddef23f90059fb17999d3095db4240e98f955/website/docs/code_execution.md#L15-L21), [website/docs/code_execution.md#L31-L33](https://github.com/microsoft/TaskWeaver/blob/d44ddef23f90059fb17999d3095db4240e98f955/website/docs/code_execution.md#L31-L33) (`clm_8752994f192f36c00576c975dd0610ff2150b9bc7aa07a4e448be047b11596a7`)
- [observation/documented] The execution mode is configured via the execution_service.kernel_mode parameter in taskweaver_config.json, with 'container' as the default value. -- evidence: [website/docs/code_execution.md#L31-L33](https://github.com/microsoft/TaskWeaver/blob/d44ddef23f90059fb17999d3095db4240e98f955/website/docs/code_execution.md#L31-L33) (`clm_0e4c68c55bc086e9e46ff6810ae365a3b7b08fb71cc454ad4734515ae4b16b4e`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The sql_pull_data example plugin is implemented on top of Langchain and requires installing langchain and tabulate; the forecasting example requires yfinance and statsmodels. -- evidence: [README.md#L189-L193](https://github.com/microsoft/TaskWeaver/blob/d44ddef23f90059fb17999d3095db4240e98f955/README.md#L189-L193), [README.md#L177-L182](https://github.com/microsoft/TaskWeaver/blob/d44ddef23f90059fb17999d3095db4240e98f955/README.md#L177-L182) (`clm_fef015d078f924049fc7899d222735f8afbefb677c830d03c13eff7ab6f26ca1`)

## limitations (2 claim(s))

- [observation/documented] Container mode has documented limitations: slower startup, limited host access with only the session workspace directory mounted (files must be uploaded via /upload or the web upload button), and packages must be added to the Dockerfile and image rebuilt. -- evidence: [website/docs/code_execution.md#L92-L100](https://github.com/microsoft/TaskWeaver/blob/d44ddef23f90059fb17999d3095db4240e98f955/website/docs/code_execution.md#L92-L100) (`clm_314e8e526daeb73cac57a3faa2e35a795b9a57ae5ccf9b4ba7444e69ade76c96`)
- [observation/documented] The fixed star-topology orchestration is acknowledged by the docs as a limitation, though it preserves role independence. -- evidence: [website/docs/memory.md#L34-L36](https://github.com/microsoft/TaskWeaver/blob/d44ddef23f90059fb17999d3095db4240e98f955/website/docs/memory.md#L34-L36) (`clm_57168a4273beb7921e705cb4291ec282b5d9e6f2c90ad6b8aed04951555fa87f`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

