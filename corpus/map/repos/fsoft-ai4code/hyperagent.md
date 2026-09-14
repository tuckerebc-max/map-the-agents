# fsoft-ai4code/hyperagent

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit c3092f2601ab @ 0c32860f5740328f

## Summary (orientation draft, not independently verified)

The snapshot is README-only evidence for HyperAgent, a generalist multi-agent software engineering system with four agents (Planner, Navigator, Code Editor, Executor), supporting Python and Java, with documented benchmark results and installation/usage instructions.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] HyperAgent is described as a generalist multi-agent system for a wide range of software engineering tasks across programming languages, mimicking human developer workflows. -- evidence: [README.md#L24-L24](https://github.com/FSoft-AI4Code/HyperAgent/blob/c3092f2601ab3bf7f890fac2cd5b1290d3f59256/README.md#L24-L24)
- components (1 claim(s)):
  - [observation/documented] The system comprises four specialized agents: Planner, Navigator, Code Editor, and Executor, covering the SE task lifecycle from conception to verification. -- evidence: [README.md#L24-L24](https://github.com/FSoft-AI4Code/HyperAgent/blob/c3092f2601ab3bf7f890fac2cd5b1290d3f59256/README.md#L24-L24)
- design-choices (1 claim(s)):
  - [observation/documented] Agent configuration is per-role: the config dict keys nav, edit, exec, and plan each take model settings (e.g., Claude models with API keys, stop sequences, base URLs), plus a 'type' field such as 'patch'. -- evidence: [README.md#L80-L115](https://github.com/FSoft-AI4Code/HyperAgent/blob/c3092f2601ab3bf7f890fac2cd5b1290d3f59256/README.md#L80-L115)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: reproduction scripts are provided in the scripts folder for SWE-Bench, RepoExec, and Defects4J, e.g. run_swe_bench.py, run_defects4j_fl.py, and run_defects4j_apr.py. -- evidence: [README.md#L134-L136](https://github.com/FSoft-AI4Code/HyperAgent/blob/c3092f2601ab3bf7f890fac2cd5b1290d3f59256/README.md#L134-L136), [README.md#L131-L131](https://github.com/FSoft-AI4Code/HyperAgent/blob/c3092f2601ab3bf7f890fac2cd5b1290d3f59256/README.md#L131-L131), [README.md#L144-L146](https://github.com/FSoft-AI4Code/HyperAgent/blob/c3092f2601ab3bf7f890fac2cd5b1290d3f59256/README.md#L144-L146), [README.md#L139-L141](https://github.com/FSoft-AI4Code/HyperAgent/blob/c3092f2601ab3bf7f890fac2cd5b1290d3f59256/README.md#L139-L141)
- skills-patterns (1 claim(s)):
  - [observation/documented] Tasks are implemented as task classes with a run(system, idx) method that constructs a prompt, calls system.query_codebase, and returns a result; example scripts live in the scripts folder and src/hyperagent/tasks. -- evidence: [README.md#L117-L117](https://github.com/FSoft-AI4Code/HyperAgent/blob/c3092f2601ab3bf7f890fac2cd5b1290d3f59256/README.md#L117-L117), [README.md#L119-L126](https://github.com/FSoft-AI4Code/HyperAgent/blob/c3092f2601ab3bf7f890fac2cd5b1290d3f59256/README.md#L119-L126), [README.md#L128-L128](https://github.com/FSoft-AI4Code/HyperAgent/blob/c3092f2601ab3bf7f890fac2cd5b1290d3f59256/README.md#L128-L128)
- interfaces (2 claim(s)):
  - [observation/documented] A Python API exposes HyperAgent(repo, commit, language, clone_dir, config) for use, and a CLI via main.py accepts repo path, commit hash, language, clone dir, and a free-form prompt. -- evidence: [README.md#L72-L76](https://github.com/FSoft-AI4Code/HyperAgent/blob/c3092f2601ab3bf7f890fac2cd5b1290d3f59256/README.md#L72-L76), [README.md#L67-L70](https://github.com/FSoft-AI4Code/HyperAgent/blob/c3092f2601ab3bf7f890fac2cd5b1290d3f59256/README.md#L67-L70)
  - [observation/documented] HyperAgent supports two modes: patch mode generates a patch for a task, and predict mode predicts the next token (e.g., for repoQA or fault location). -- evidence: [README.md#L78-L78](https://github.com/FSoft-AI4Code/HyperAgent/blob/c3092f2601ab3bf7f890fac2cd5b1290d3f59256/README.md#L78-L78)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation (2 claim(s)):
  - [observation/documented] Reported results include 31.4% resolved rate on SWE-Bench Verified and 25% on SWE-Bench Lite, with verification noted as in progress via a swe-bench experiments PR. -- evidence: [README.md#L28-L30](https://github.com/FSoft-AI4Code/HyperAgent/blob/c3092f2601ab3bf7f890fac2cd5b1290d3f59256/README.md#L28-L30)
  - [observation/documented] Reported repository-level code generation result is 53.3% Pass@5 on RepoExec-Python, and 249 bugs fixed on Defects4J-Java for fault localization and repair. -- evidence: [README.md#L28-L30](https://github.com/FSoft-AI4Code/HyperAgent/blob/c3092f2601ab3bf7f890fac2cd5b1290d3f59256/README.md#L28-L30)
- dependencies (2 claim(s)):
  - [observation/documented] HyperAgent depends on Zoekt for code search, requiring a recent Go installation, plus universal-ctags with CTAGS_COMMAND=universal-ctags set for semantic code search. -- evidence: [README.md#L48-L48](https://github.com/FSoft-AI4Code/HyperAgent/blob/c3092f2601ab3bf7f890fac2cd5b1290d3f59256/README.md#L48-L48), [README.md#L56-L58](https://github.com/FSoft-AI4Code/HyperAgent/blob/c3092f2601ab3bf7f890fac2cd5b1290d3f59256/README.md#L56-L58)
More evidence: [full detail](hyperagent.detail.md)

Metadata and full claim list: [full detail](hyperagent.detail.md)
Human notes ([notes](hyperagent.notes.md), never overwritten by build)

[Back to map index](../../index.md)
