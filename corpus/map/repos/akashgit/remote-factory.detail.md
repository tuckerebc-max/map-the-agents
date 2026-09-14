# akashgit/remote-factory -- full detail

[Back to orientation](remote-factory.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/akashgit/remote-factory/4262d361ebbfd3fd9944aac45e5ab77e37d43f3d/cd2e332d94e06242.json](../../../wiki/dossiers/akashgit/remote-factory/4262d361ebbfd3fd9944aac45e5ab77e37d43f3d/cd2e332d94e06242.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (3 claim(s))

- [observation/documented] The system is described as four layers: a Python CLI, a workflow graph engine of Pydantic DAGs with typed nodes (AgentNode, FnNode, GateNode, ForkNode, JoinNode), a CEO orchestrator agent, and specialist Claude Code subprocess agents. -- evidence: [README.md#L272-L272](https://github.com/akashgit/remote-factory/blob/4262d361ebbfd3fd9944aac45e5ab77e37d43f3d/README.md#L272-L272), [README.md#L244-L266](https://github.com/akashgit/remote-factory/blob/4262d361ebbfd3fd9944aac45e5ab77e37d43f3d/README.md#L244-L266), [README.md#L274-L274](https://github.com/akashgit/remote-factory/blob/4262d361ebbfd3fd9944aac45e5ab77e37d43f3d/README.md#L274-L274), [README.md#L270-L270](https://github.com/akashgit/remote-factory/blob/4262d361ebbfd3fd9944aac45e5ab77e37d43f3d/README.md#L270-L270) (`clm_3576d03ca23a9ca7bdc0abee2d0a7cb17fa1b93cdb689155e55da1ac03ed52d5`)
- [observation/documented] Specialist agents include Researcher, Strategist, Builder, Reviewer, Evaluator, Archivist, Refiner, and Failure Analyst, each invoked as `factory agent <role> --task "..."` with a narrow responsibility. -- evidence: [docs/architecture.md#L29-L39](https://github.com/akashgit/remote-factory/blob/4262d361ebbfd3fd9944aac45e5ab77e37d43f3d/docs/architecture.md#L29-L39) (`clm_ae0d9a1d3064d01b27b07a13172c1d11ebc92edf5705486ef7c0032f64f43a8d`)
- [observation/documented] Shipped workflows include frontend-design, parallel-improve, deep-research, design-v2, deep-qa, and study, plus community-contributed benchmark workflows (swebench, featurebench, legacybench, devopsgym, terminalbench, and others) following a study→solver→gate→merge pattern. -- evidence: [README.md#L193-L193](https://github.com/akashgit/remote-factory/blob/4262d361ebbfd3fd9944aac45e5ab77e37d43f3d/README.md#L193-L193), [README.md#L182-L189](https://github.com/akashgit/remote-factory/blob/4262d361ebbfd3fd9944aac45e5ab77e37d43f3d/README.md#L182-L189), [README.md#L195-L204](https://github.com/akashgit/remote-factory/blob/4262d361ebbfd3fd9944aac45e5ab77e37d43f3d/README.md#L195-L204) (`clm_48ba8b306d91ee5b2d38650cd784466fc0e617e55754d4961b0e87a5912f7321`)

## design-choices (3 claim(s))

- [observation/documented] Design-v2 replaces hardcoded researchers and a single strategist with three Director agents that dynamically size N (3-7) research directions, M (2-5) strategy perspectives, and K (2-5) QA testers, following parallel generation, synthesis, then gating. -- evidence: [README.md#L108-L114](https://github.com/akashgit/remote-factory/blob/4262d361ebbfd3fd9944aac45e5ab77e37d43f3d/README.md#L108-L114), [README.md#L100-L100](https://github.com/akashgit/remote-factory/blob/4262d361ebbfd3fd9944aac45e5ab77e37d43f3d/README.md#L100-L100) (`clm_9f09e96cd9af30f094c300cef6398c3c551203087faf24c716f6ef1d43d46a95`)
- [observation/documented] ACE self-improvement derives playbook bullets from real experiment outcomes, tracks helpful/harmful counters per bullet, prunes negative-net-score rules, caps playbook size, and injects evolved playbooks into agent prompts at spawn time. -- evidence: [docs/ace.md#L98-L102](https://github.com/akashgit/remote-factory/blob/4262d361ebbfd3fd9944aac45e5ab77e37d43f3d/docs/ace.md#L98-L102), [docs/ace.md#L17-L21](https://github.com/akashgit/remote-factory/blob/4262d361ebbfd3fd9944aac45e5ab77e37d43f3d/docs/ace.md#L17-L21), [docs/ace.md#L25-L29](https://github.com/akashgit/remote-factory/blob/4262d361ebbfd3fd9944aac45e5ab77e37d43f3d/docs/ace.md#L25-L29), [docs/ace.md#L33-L33](https://github.com/akashgit/remote-factory/blob/4262d361ebbfd3fd9944aac45e5ab77e37d43f3d/docs/ace.md#L33-L33), [docs/ace.md#L57-L60](https://github.com/akashgit/remote-factory/blob/4262d361ebbfd3fd9944aac45e5ab77e37d43f3d/docs/ace.md#L57-L60) (`clm_6eccd6a991efc6cc435e86bcab9e27965b6d8e6f1a1bb1ff13f63df4623b49e6`)
- [observation/documented] Agent prompts resolve through a three-tier lookup — project-specific override, user-global override, then the factory default — and a plugin system via the `factory.plugins` entry-point group can extend modes, commands, and agent roles with builtins winning collisions. -- evidence: [docs/architecture.md#L41-L44](https://github.com/akashgit/remote-factory/blob/4262d361ebbfd3fd9944aac45e5ab77e37d43f3d/docs/architecture.md#L41-L44), [docs/architecture.md#L50-L50](https://github.com/akashgit/remote-factory/blob/4262d361ebbfd3fd9944aac45e5ab77e37d43f3d/docs/architecture.md#L50-L50), [docs/architecture.md#L52-L52](https://github.com/akashgit/remote-factory/blob/4262d361ebbfd3fd9944aac45e5ab77e37d43f3d/docs/architecture.md#L52-L52) (`clm_962c453b48dd39bec12c357cb717f7fc64d1457675cb62a7fd44ea1f520f002d`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: contributors install dev deps with `uv sync --all-groups`, run `pytest -v`, lint with `ruff check .`, and type-check with `mypy factory/`; a contributing guide covers dev setup, code style, testing, and PR workflow. -- evidence: [README.md#L470-L475](https://github.com/akashgit/remote-factory/blob/4262d361ebbfd3fd9944aac45e5ab77e37d43f3d/README.md#L470-L475), [README.md#L465-L466](https://github.com/akashgit/remote-factory/blob/4262d361ebbfd3fd9944aac45e5ab77e37d43f3d/README.md#L465-L466) (`clm_2e79f6cbc445267e043fc325c57984bccf8c193287c97134b3e4b9c18052ced9`)
- [observation/documented] Repository development practice: after editing a workflow graph in `factory/workflow/definitions.py`, contributors re-export skills via `factory workflow export-skills` and test with `pytest tests/test_workflow.py -v`. -- evidence: [README.md#L151-L153](https://github.com/akashgit/remote-factory/blob/4262d361ebbfd3fd9944aac45e5ab77e37d43f3d/README.md#L151-L153) (`clm_a44717dbddbadf2b1f5ad6eb79c3d44d385d3fdab98a5d35331e82c15392cd89`)

## skills-patterns (1 claim(s))

- [observation/documented] Workflow graphs are exported to SKILL.md prose playbooks through a verified pipeline (templatize, review agent, guard, split) producing SKILL.md plus SKILL.annotations.yaml, with a CI regression test guarding drift between definitions and exported skills. -- evidence: [README.md#L383-L383](https://github.com/akashgit/remote-factory/blob/4262d361ebbfd3fd9944aac45e5ab77e37d43f3d/README.md#L383-L383), [README.md#L385-L390](https://github.com/akashgit/remote-factory/blob/4262d361ebbfd3fd9944aac45e5ab77e37d43f3d/README.md#L385-L390), [README.md#L402-L402](https://github.com/akashgit/remote-factory/blob/4262d361ebbfd3fd9944aac45e5ab77e37d43f3d/README.md#L402-L402), [README.md#L392-L394](https://github.com/akashgit/remote-factory/blob/4262d361ebbfd3fd9944aac45e5ab77e37d43f3d/README.md#L392-L394) (`clm_769193f44278cef171e83166d0cc0fc6c4ed8a29d0241e461ad90c8e978efafb`)

## interfaces (4 claim(s))

- [observation/documented] The primary CLI is `factory ceo <path> --mode <mode>` with modes including design, design-v2, create, meta, and outer-loop (run headless), plus `--focus` to target a backlog item, GitHub issue, or topic. -- evidence: [README.md#L102-L106](https://github.com/akashgit/remote-factory/blob/4262d361ebbfd3fd9944aac45e5ab77e37d43f3d/README.md#L102-L106), [README.md#L68-L71](https://github.com/akashgit/remote-factory/blob/4262d361ebbfd3fd9944aac45e5ab77e37d43f3d/README.md#L68-L71), [README.md#L219-L220](https://github.com/akashgit/remote-factory/blob/4262d361ebbfd3fd9944aac45e5ab77e37d43f3d/README.md#L219-L220), [README.md#L284-L286](https://github.com/akashgit/remote-factory/blob/4262d361ebbfd3fd9944aac45e5ab77e37d43f3d/README.md#L284-L286), [README.md#L165-L172](https://github.com/akashgit/remote-factory/blob/4262d361ebbfd3fd9944aac45e5ab77e37d43f3d/README.md#L165-L172), [README.md#L20-L20](https://github.com/akashgit/remote-factory/blob/4262d361ebbfd3fd9944aac45e5ab77e37d43f3d/README.md#L20-L20) (`clm_4ac2a362fa3af9474cb702bd6f65d30d415aa5000881f91e77d93cd0867669a2`)
- [observation/documented] Additional CLI surface includes `factory outer-loop calibrate`, `factory run --loop --interval`, `factory tmux --loop`, `factory discover`, `factory ace`, `factory install`, and `factory workflow export-skills`. -- evidence: [README.md#L236-L236](https://github.com/akashgit/remote-factory/blob/4262d361ebbfd3fd9944aac45e5ab77e37d43f3d/README.md#L236-L236), [README.md#L370-L375](https://github.com/akashgit/remote-factory/blob/4262d361ebbfd3fd9944aac45e5ab77e37d43f3d/README.md#L370-L375), [README.md#L212-L217](https://github.com/akashgit/remote-factory/blob/4262d361ebbfd3fd9944aac45e5ab77e37d43f3d/README.md#L212-L217), [docs/ace.md#L66-L66](https://github.com/akashgit/remote-factory/blob/4262d361ebbfd3fd9944aac45e5ab77e37d43f3d/docs/ace.md#L66-L66), [README.md#L429-L432](https://github.com/akashgit/remote-factory/blob/4262d361ebbfd3fd9944aac45e5ab77e37d43f3d/README.md#L429-L432), [README.md#L398-L400](https://github.com/akashgit/remote-factory/blob/4262d361ebbfd3fd9944aac45e5ab77e37d43f3d/README.md#L398-L400) (`clm_ea3d0bb4e9fa30f07c0f2f6a9c2f1d677bae9e9892e403233566d989f00940c4`)
- [observation/documented] re:factory is also distributed as a Claude Code plugin exposing a `/factory:implement` slash command, namespaced subagents like `factory:ceo`, and bundled skills; the plugin still shells out to the globally installed `factory` CLI. -- evidence: [README.md#L360-L360](https://github.com/akashgit/remote-factory/blob/4262d361ebbfd3fd9944aac45e5ab77e37d43f3d/README.md#L360-L360), [README.md#L356-L358](https://github.com/akashgit/remote-factory/blob/4262d361ebbfd3fd9944aac45e5ab77e37d43f3d/README.md#L356-L358), [README.md#L344-L344](https://github.com/akashgit/remote-factory/blob/4262d361ebbfd3fd9944aac45e5ab77e37d43f3d/README.md#L344-L344) (`clm_d4c4d2868c3b0afdb628b0aa96067462dfc7d7f3fff2ae8ed5284dac86893d31`)
- [observation/documented] In create mode, prefixing `--focus` with a mode name and colon (e.g. "improve: ...") updates an existing registered workflow, while a focus without a colon always creates a new mode. -- evidence: [README.md#L132-L132](https://github.com/akashgit/remote-factory/blob/4262d361ebbfd3fd9944aac45e5ab77e37d43f3d/README.md#L132-L132), [README.md#L134-L137](https://github.com/akashgit/remote-factory/blob/4262d361ebbfd3fd9944aac45e5ab77e37d43f3d/README.md#L134-L137), [README.md#L139-L139](https://github.com/akashgit/remote-factory/blob/4262d361ebbfd3fd9944aac45e5ab77e37d43f3d/README.md#L139-L139) (`clm_149adf6e2b18fb414afd4d1dc814d3cfb5a53954580811415e4cda1b36e350af`)

## memory-state (1 claim(s))

- [observation/documented] All state is local: per-project state lives in `.factory/` (recommended for .gitignore) and global state in `~/.factory/`, including a registry at `~/.factory/registry.json` and evolved playbooks under `~/.factory/playbooks/`. -- evidence: [docs/ace.md#L17-L21](https://github.com/akashgit/remote-factory/blob/4262d361ebbfd3fd9944aac45e5ab77e37d43f3d/docs/ace.md#L17-L21), [docs/ace.md#L37-L37](https://github.com/akashgit/remote-factory/blob/4262d361ebbfd3fd9944aac45e5ab77e37d43f3d/docs/ace.md#L37-L37), [README.md#L36-L36](https://github.com/akashgit/remote-factory/blob/4262d361ebbfd3fd9944aac45e5ab77e37d43f3d/README.md#L36-L36) (`clm_f8b13a279b9a761d3ec1eda3fb2aad88901a66a0b2bf6ca7d4ef56fe846c992c`)

## orchestration (1 claim(s))

- [observation/documented] The CEO agent detects project state, reads SKILL.md playbooks, spawns specialist agents via `factory agent <role>`, and makes keep/revert decisions based on eval scores. -- evidence: [README.md#L272-L272](https://github.com/akashgit/remote-factory/blob/4262d361ebbfd3fd9944aac45e5ab77e37d43f3d/README.md#L272-L272), [docs/architecture.md#L17-L21](https://github.com/akashgit/remote-factory/blob/4262d361ebbfd3fd9944aac45e5ab77e37d43f3d/docs/architecture.md#L17-L21), [README.md#L274-L274](https://github.com/akashgit/remote-factory/blob/4262d361ebbfd3fd9944aac45e5ab77e37d43f3d/README.md#L274-L274) (`clm_564419e94a8ee8d48902fe6a4f50b05b0c12f52b2c4116c10130e8e60cad44a8`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (2 claim(s))

- [observation/documented] The eval system scores each change with a weighted composite across Hygiene (6 dimensions), Growth (5 dimensions), and user-defined Project tiers; `factory discover` auto-detects language and framework to generate the eval profile. -- evidence: [README.md#L236-L236](https://github.com/akashgit/remote-factory/blob/4262d361ebbfd3fd9944aac45e5ab77e37d43f3d/README.md#L236-L236), [README.md#L230-L234](https://github.com/akashgit/remote-factory/blob/4262d361ebbfd3fd9944aac45e5ab77e37d43f3d/README.md#L230-L234) (`clm_2a53c31d2925de4221f9f297d52bb62bca1a25aa6720e25839d0d9b36571589d`)
- [observation/documented] An outer loop evolves workflow DAGs against benchmarks via MAP-Elites: it mutates workflow structure, evaluates candidates on a real benchmark instance, and selects for higher test pass rates. -- evidence: [README.md#L222-L222](https://github.com/akashgit/remote-factory/blob/4262d361ebbfd3fd9944aac45e5ab77e37d43f3d/README.md#L222-L222) (`clm_612402e8c8d146e9c5a8673d4b6a7d2d8a0970ba9f32ee1044ed1d4279e145ae`)

## dependencies (1 claim(s))

- [observation/documented] Prerequisites are Python 3.11+, the uv package manager, and an installed, authenticated Claude Code; LangFuse tracing additionally requires Docker or Podman with a compose tool. -- evidence: [README.md#L329-L329](https://github.com/akashgit/remote-factory/blob/4262d361ebbfd3fd9944aac45e5ab77e37d43f3d/README.md#L329-L329), [README.md#L42-L42](https://github.com/akashgit/remote-factory/blob/4262d361ebbfd3fd9944aac45e5ab77e37d43f3d/README.md#L42-L42) (`clm_a38fc0c3f7be31d02d4a7d7f4b0b7782dc77e9f7b624a8bbd4a7c1628216ae77`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

