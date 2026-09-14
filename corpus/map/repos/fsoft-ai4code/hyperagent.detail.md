# fsoft-ai4code/hyperagent -- full detail

[Back to orientation](hyperagent.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/fsoft-ai4code/hyperagent/c3092f2601ab3bf7f890fac2cd5b1290d3f59256/0c32860f5740328f.json](../../../wiki/dossiers/fsoft-ai4code/hyperagent/c3092f2601ab3bf7f890fac2cd5b1290d3f59256/0c32860f5740328f.json)

## specifications (1 claim(s))

- [observation/documented] HyperAgent is described as a generalist multi-agent system for a wide range of software engineering tasks across programming languages, mimicking human developer workflows. -- evidence: [README.md#L24-L24](https://github.com/FSoft-AI4Code/HyperAgent/blob/c3092f2601ab3bf7f890fac2cd5b1290d3f59256/README.md#L24-L24) (`clm_4ac07b97f002f03fba8240f94ac5a77e39a02828ea07027ebe5de00f3eb3a309`)

## components (1 claim(s))

- [observation/documented] The system comprises four specialized agents: Planner, Navigator, Code Editor, and Executor, covering the SE task lifecycle from conception to verification. -- evidence: [README.md#L24-L24](https://github.com/FSoft-AI4Code/HyperAgent/blob/c3092f2601ab3bf7f890fac2cd5b1290d3f59256/README.md#L24-L24) (`clm_0d4acf8c87ce6457c0b4373cb82e21077c86bb58297f90ec4fc45e2218f7497f`)

## design-choices (1 claim(s))

- [observation/documented] Agent configuration is per-role: the config dict keys nav, edit, exec, and plan each take model settings (e.g., Claude models with API keys, stop sequences, base URLs), plus a 'type' field such as 'patch'. -- evidence: [README.md#L80-L115](https://github.com/FSoft-AI4Code/HyperAgent/blob/c3092f2601ab3bf7f890fac2cd5b1290d3f59256/README.md#L80-L115) (`clm_3583f0bab1f1da9c69758a7f5a1c737fe396a5711ae11a14173817037a38aaee`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: reproduction scripts are provided in the scripts folder for SWE-Bench, RepoExec, and Defects4J, e.g. run_swe_bench.py, run_defects4j_fl.py, and run_defects4j_apr.py. -- evidence: [README.md#L134-L136](https://github.com/FSoft-AI4Code/HyperAgent/blob/c3092f2601ab3bf7f890fac2cd5b1290d3f59256/README.md#L134-L136), [README.md#L131-L131](https://github.com/FSoft-AI4Code/HyperAgent/blob/c3092f2601ab3bf7f890fac2cd5b1290d3f59256/README.md#L131-L131), [README.md#L144-L146](https://github.com/FSoft-AI4Code/HyperAgent/blob/c3092f2601ab3bf7f890fac2cd5b1290d3f59256/README.md#L144-L146), [README.md#L139-L141](https://github.com/FSoft-AI4Code/HyperAgent/blob/c3092f2601ab3bf7f890fac2cd5b1290d3f59256/README.md#L139-L141) (`clm_abfadf4a69b40849c0a722fb0645406439abab413aa92dbe0d01f813cf71d45d`)

## skills-patterns (1 claim(s))

- [observation/documented] Tasks are implemented as task classes with a run(system, idx) method that constructs a prompt, calls system.query_codebase, and returns a result; example scripts live in the scripts folder and src/hyperagent/tasks. -- evidence: [README.md#L117-L117](https://github.com/FSoft-AI4Code/HyperAgent/blob/c3092f2601ab3bf7f890fac2cd5b1290d3f59256/README.md#L117-L117), [README.md#L119-L126](https://github.com/FSoft-AI4Code/HyperAgent/blob/c3092f2601ab3bf7f890fac2cd5b1290d3f59256/README.md#L119-L126), [README.md#L128-L128](https://github.com/FSoft-AI4Code/HyperAgent/blob/c3092f2601ab3bf7f890fac2cd5b1290d3f59256/README.md#L128-L128) (`clm_472a2fdfc08d8dd6af09eb4f69c9475f3ef3a51f9d4a60837623f09a71498d3d`)

## interfaces (2 claim(s))

- [observation/documented] A Python API exposes HyperAgent(repo, commit, language, clone_dir, config) for use, and a CLI via main.py accepts repo path, commit hash, language, clone dir, and a free-form prompt. -- evidence: [README.md#L72-L76](https://github.com/FSoft-AI4Code/HyperAgent/blob/c3092f2601ab3bf7f890fac2cd5b1290d3f59256/README.md#L72-L76), [README.md#L67-L70](https://github.com/FSoft-AI4Code/HyperAgent/blob/c3092f2601ab3bf7f890fac2cd5b1290d3f59256/README.md#L67-L70) (`clm_fa652421aae754c885aadb6715eb9ca7fe66ac697976972a1c5249038347718c`)
- [observation/documented] HyperAgent supports two modes: patch mode generates a patch for a task, and predict mode predicts the next token (e.g., for repoQA or fault location). -- evidence: [README.md#L78-L78](https://github.com/FSoft-AI4Code/HyperAgent/blob/c3092f2601ab3bf7f890fac2cd5b1290d3f59256/README.md#L78-L78) (`clm_e5a719fa3fa0bcf85e985621ff77e441090a3c4dc5c1fcf828e995eb72fc4806`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (2 claim(s))

- [observation/documented] Reported results include 31.4% resolved rate on SWE-Bench Verified and 25% on SWE-Bench Lite, with verification noted as in progress via a swe-bench experiments PR. -- evidence: [README.md#L28-L30](https://github.com/FSoft-AI4Code/HyperAgent/blob/c3092f2601ab3bf7f890fac2cd5b1290d3f59256/README.md#L28-L30) (`clm_fb55657a2a5b8644cfd58327bb594ea822280b175d65f8f262ddb208b409164c`)
- [observation/documented] Reported repository-level code generation result is 53.3% Pass@5 on RepoExec-Python, and 249 bugs fixed on Defects4J-Java for fault localization and repair. -- evidence: [README.md#L28-L30](https://github.com/FSoft-AI4Code/HyperAgent/blob/c3092f2601ab3bf7f890fac2cd5b1290d3f59256/README.md#L28-L30) (`clm_e3bf6bdbc6792c3b5d15c8bfd7195699ce4086a4aab582a99d3f60053134bf29`)

## dependencies (2 claim(s))

- [observation/documented] HyperAgent depends on Zoekt for code search, requiring a recent Go installation, plus universal-ctags with CTAGS_COMMAND=universal-ctags set for semantic code search. -- evidence: [README.md#L48-L48](https://github.com/FSoft-AI4Code/HyperAgent/blob/c3092f2601ab3bf7f890fac2cd5b1290d3f59256/README.md#L48-L48), [README.md#L56-L58](https://github.com/FSoft-AI4Code/HyperAgent/blob/c3092f2601ab3bf7f890fac2cd5b1290d3f59256/README.md#L56-L58) (`clm_cc73f83e42cc6881db95f65c6621b0d14743ef91d55fbcd9ba987785c7b754ed`)
- [observation/documented] Installation requires a conda environment named 'hyperagent' with Python 3.10, because the Executor uses a jupyter kernel of that name; the pinned requirements include anthropic, docker, GitPython, and e2b packages. -- evidence: [README.md#L60-L64](https://github.com/FSoft-AI4Code/HyperAgent/blob/c3092f2601ab3bf7f890fac2cd5b1290d3f59256/README.md#L60-L64), [requirements.txt#L1-L250](https://github.com/FSoft-AI4Code/HyperAgent/blob/c3092f2601ab3bf7f890fac2cd5b1290d3f59256/requirements.txt#L1-L250) (`clm_b3a030a47b253c69a1c59f927a3ae7246034eca268b12130f3b2ae265f837a67`)

## limitations (1 claim(s))

- [observation/documented] Currently only Python and Java are supported; expansion to other languages and benchmarks is planned for the future. -- evidence: [README.md#L32-L32](https://github.com/FSoft-AI4Code/HyperAgent/blob/c3092f2601ab3bf7f890fac2cd5b1290d3f59256/README.md#L32-L32) (`clm_723a24201ae3daec8ee92d9dc3ac62fe7b9f08c3e32ddb0f5748b8f0419c5bc9`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

