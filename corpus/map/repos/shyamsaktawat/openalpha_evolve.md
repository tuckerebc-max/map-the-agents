# shyamsaktawat/openalpha_evolve

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 0389aea0e0a7 @ d4155f4b317d4239

## Summary (orientation draft, not independently verified)

Selected evidence records: The system uses a modular agent architecture with named agents: PromptDesignerAgent, CodeGeneratorAgent, EvaluatorAgent, DatabaseAgent, SelectionControllerAgent, and a task_manager agent that orchestrates the evolutionary loop and coordinates the others. Mutation and bug-fix prompts often request changes in diff format, and the code generator attempts to apply received diffs to the parent code; the features list describes diff-based mutations for targeted modifications.

## Source coverage

Source coverage (complete): 3 of 3 candidate file(s) selected; repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The system uses a modular agent architecture with named agents: PromptDesignerAgent, CodeGeneratorAgent, EvaluatorAgent, DatabaseAgent, SelectionControllerAgent, and a task_manager agent that orchestrates the evolutionary loop and coordinates the others. -- evidence: [README.md#L48-L63](https://github.com/shyamsaktawat/OpenAlpha_Evolve/blob/0389aea0e0a745b61babdc0fdd18ac61098dfa84/README.md#L48-L63), [README.md#L82-L99](https://github.com/shyamsaktawat/OpenAlpha_Evolve/blob/0389aea0e0a745b61babdc0fdd18ac61098dfa84/README.md#L82-L99)
- design-choices (1 claim(s)):
  - [observation/documented] Mutation and bug-fix prompts often request changes in diff format, and the code generator attempts to apply received diffs to the parent code; the features list describes diff-based mutations for targeted modifications. -- evidence: [README.md#L48-L63](https://github.com/shyamsaktawat/OpenAlpha_Evolve/blob/0389aea0e0a745b61babdc0fdd18ac61098dfa84/README.md#L48-L63), [README.md#L69-L76](https://github.com/shyamsaktawat/OpenAlpha_Evolve/blob/0389aea0e0a745b61babdc0fdd18ac61098dfa84/README.md#L69-L76)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributors are asked to report bugs or suggest features via GitHub issues, and to fork the repo, create a feature branch, write clean documented code, add tests if applicable, avoid breaking existing functionality, and submit pull requests with clear descriptions. -- evidence: [README.md#L257-L265](https://github.com/shyamsaktawat/OpenAlpha_Evolve/blob/0389aea0e0a745b61babdc0fdd18ac61098dfa84/README.md#L257-L265), [README.md#L255-L255](https://github.com/shyamsaktawat/OpenAlpha_Evolve/blob/0389aea0e0a745b61babdc0fdd18ac61098dfa84/README.md#L255-L255)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] A Gradio web interface is started with 'python app.py'; it displays a local URL (e.g., http://127.0.0.1:7860) and optionally a public share link, where users can define custom tasks and run evolution interactively. -- evidence: [README.md#L167-L172](https://github.com/shyamsaktawat/OpenAlpha_Evolve/blob/0389aea0e0a745b61babdc0fdd18ac61098dfa84/README.md#L167-L172)
  - [observation/documented] The CLI entry point runs an evolutionary run via 'python -m main <task.yaml>' (e.g., examples/shortest_path.yaml), with logs also saved to alpha_evolve.log by default. -- evidence: [README.md#L160-L165](https://github.com/shyamsaktawat/OpenAlpha_Evolve/blob/0389aea0e0a745b61babdc0fdd18ac61098dfa84/README.md#L160-L165)
- memory-state (1 claim(s)):
  - [observation/documented] The DatabaseAgent stores programs with code, fitness scores, generation, and lineage as a record of evolutionary history; the README notes this storage is currently in-memory. -- evidence: [README.md#L48-L63](https://github.com/shyamsaktawat/OpenAlpha_Evolve/blob/0389aea0e0a745b61babdc0fdd18ac61098dfa84/README.md#L48-L63)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
  - [observation/documented] Per the README feature list, generated code is executed in Docker containers for sandboxed evaluation, with configurable timeout mechanisms. -- evidence: [README.md#L69-L76](https://github.com/shyamsaktawat/OpenAlpha_Evolve/blob/0389aea0e0a745b61babdc0fdd18ac61098dfa84/README.md#L69-L76)
- evaluation (1 claim(s)):
  - [observation/documented] The EvaluatorAgent syntax-checks generated code, executes it in an isolated environment against task input/output examples, and scores fitness based on correctness (test cases passed), runtime efficiency, and other potential metrics. -- evidence: [README.md#L48-L63](https://github.com/shyamsaktawat/OpenAlpha_Evolve/blob/0389aea0e0a745b61babdc0fdd18ac61098dfa84/README.md#L48-L63)
- dependencies (2 claim(s)):
More evidence: [full detail](openalpha_evolve.detail.md)

Metadata and full claim list: [full detail](openalpha_evolve.detail.md)
Human notes ([notes](openalpha_evolve.notes.md), never overwritten by build)

[Back to map index](../../index.md)
