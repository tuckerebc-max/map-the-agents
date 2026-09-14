# foundationagents/recode -- full detail

[Back to orientation](recode.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/foundationagents/recode/6e7223f71281d914762e78d7bbcf6446d362ecbc/f31fb93ce4e5f3e0.json](../../../wiki/dossiers/foundationagents/recode/6e7223f71281d914762e78d7bbcf6446d362ecbc/f31fb93ce4e5f3e0.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] Partial programs are organized in a tree where each node captures one sub-task and records its execution trace. -- evidence: [README.md#L17-L20](https://github.com/FoundationAgents/ReCode/blob/6e7223f71281d914762e78d7bbcf6446d362ecbc/README.md#L17-L20) (`clm_721246fc7c765c90322b6284177c63b2a4c18e25f74fac9250694bcd33ff0be1`)
- [observation/documented] The repository includes run.py as CLI entry point, agents/recode/ implementation, envs/ wrappers for alfworld, webshop, and sciworld, configs/, and utils/ with an async OpenAI wrapper and constrained executor. -- evidence: [README.md#L28-L33](https://github.com/FoundationAgents/ReCode/blob/6e7223f71281d914762e78d7bbcf6446d362ecbc/README.md#L28-L33) (`clm_45edd50f2672648a1d4dfb2fc6024f86274fc6a17445bfb8ac58981e37078e60`)

## design-choices (1 claim(s))

- [observation/documented] ReCode unifies plan and action into a single code representation, treating high-level plans as placeholder functions that recursively decompose into executable primitives. -- evidence: [README.md#L7-L7](https://github.com/FoundationAgents/ReCode/blob/6e7223f71281d914762e78d7bbcf6446d362ecbc/README.md#L7-L7) (`clm_ffb847cc2ddf28386453d5bb775269e8eb5e5b60b2723a82e445d3b6bb8727c7`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: setup requires a conda environment with Python 3.10 or newer, and the README suggests configuring the three benchmark environments separately since dependency conflicts are unconfirmed. -- evidence: [README.md#L59-L59](https://github.com/FoundationAgents/ReCode/blob/6e7223f71281d914762e78d7bbcf6446d362ecbc/README.md#L59-L59), [README.md#L61-L61](https://github.com/FoundationAgents/ReCode/blob/6e7223f71281d914762e78d7bbcf6446d362ecbc/README.md#L61-L61) (`clm_cf097eab89e8611c16a8261a2d5050cca27b04c5c56e6dc7c8fcff65c64064f9`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] run.py exposes flags including -a/--agent, -e/--env, -n/--instances, -c/--concurrent, --split, --seed, --max-depth, --profile, and -C/--config for YAML-based flag overrides. -- evidence: [README.md#L154-L160](https://github.com/FoundationAgents/ReCode/blob/6e7223f71281d914762e78d7bbcf6446d362ecbc/README.md#L154-L160) (`clm_95f55e37f0dd17298292ebc74421fff2e842e03f2211020afa3819da795845c3`)
- [observation/documented] LLM access is configured via named profiles in configs/profiles.yaml selected with --profile; OPENAI_API_KEY serves as a fallback, and cost tracking loads configs/prices.json with a track_costs toggle. -- evidence: [README.md#L114-L114](https://github.com/FoundationAgents/ReCode/blob/6e7223f71281d914762e78d7bbcf6446d362ecbc/README.md#L114-L114), [README.md#L132-L137](https://github.com/FoundationAgents/ReCode/blob/6e7223f71281d914762e78d7bbcf6446d362ecbc/README.md#L132-L137) (`clm_61c35d4d263c6703773a944e12e1bfef2e34c95b2b9742990c524edf78045add`)
- [observation/documented] New environments implement a base Env contract with reset, _run, is_done, is_success, and report, plus per-environment prompts and few-shot files under agents/recode/resources/. -- evidence: [README.md#L192-L198](https://github.com/FoundationAgents/ReCode/blob/6e7223f71281d914762e78d7bbcf6446d362ecbc/README.md#L192-L198) (`clm_cea2a64673e1fcee30bcf2a6881f8ec1146ed91798d6bdd0f32c7065e49b6cf9`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (1 claim(s))

- [observation/documented] A dynamic execution loop executes each node immediately, with fresh observations deciding whether to expand further, retry, or finish. -- evidence: [README.md#L17-L20](https://github.com/FoundationAgents/ReCode/blob/6e7223f71281d914762e78d7bbcf6446d362ecbc/README.md#L17-L20) (`clm_8a4871abab48bb47d8e6eef15a12b040b4a60235b39a18d3e11020d3bbbd1e26`)

## tools-permissions (1 claim(s))

- [observation/documented] A constrained Python executor maintains environment variables, validates code blocks, and exposes the toolset available to the agent. -- evidence: [README.md#L17-L20](https://github.com/FoundationAgents/ReCode/blob/6e7223f71281d914762e78d7bbcf6446d362ecbc/README.md#L17-L20) (`clm_6eb3a3e434db03eeabec6b8c5c00994b0db0f6aff15dfba227c6dcfb732d7fab`)

## evaluation (2 claim(s))

- [observation/documented] The README reports inference comparisons against ReAct, CodeAct, AdaPlanner, and ADaPT, claiming an average score of 60.8 (10.5 above the best baseline) and a perfect 100 in ALFWorld with claude-4-sonnet. -- evidence: [README.md#L39-L39](https://github.com/FoundationAgents/ReCode/blob/6e7223f71281d914762e78d7bbcf6446d362ecbc/README.md#L39-L39) (`clm_e098cece56a6f7c93277cc51090f0bfce3590d6f5e39ca1379775d691fc2e29a`)
- [observation/documented] The README reports SFT experiments with Qwen2.5-7B-Instruct giving ReCode+SFT an average of 70.4% versus ReAct+SFT (67.6%) and CodeAct+SFT (55.8%). -- evidence: [README.md#L47-L47](https://github.com/FoundationAgents/ReCode/blob/6e7223f71281d914762e78d7bbcf6446d362ecbc/README.md#L47-L47) (`clm_a4dfa0ef344f5a11532515bc193774a19b966baff05da8ed4b02e9fd649c3815`)

## dependencies (1 claim(s))

- [observation/documented] requirements.txt pins openai==2.6.1, rich==14.2.0, and torch==2.9.0. -- evidence: [requirements.txt#L1-L3](https://github.com/FoundationAgents/ReCode/blob/6e7223f71281d914762e78d7bbcf6446d362ecbc/requirements.txt#L1-L3) (`clm_e38ce9eca5eba7ebbbba868270a4a0cbb5faca41013f61bd5bcb7d99622d430f`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

