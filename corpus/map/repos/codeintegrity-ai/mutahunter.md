# codeintegrity-ai/mutahunter

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 97221a1aedca @ 71c01af5105f3c94

## Summary (orientation draft, not independently verified)

Selected evidence records: Mutahunter is described as open-source, language-agnostic, LLM-based mutation testing software. A CLI command 'mutahunter run' accepts a test command, model name, source file path, and test file path as arguments.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 8 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

8 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications (2 claim(s)):
  - [observation/documented] Mutahunter is described as open-source, language-agnostic, LLM-based mutation testing software. -- evidence: [README.md#L5-L5](https://github.com/codeintegrity-ai/mutahunter/blob/97221a1aedca8a8e92bf67843903af26cacab5b7/README.md#L5-L5)
  - [observation/documented] The project is licensed under AGPL 3.0. -- evidence: [README.md#L7-L12](https://github.com/codeintegrity-ai/mutahunter/blob/97221a1aedca8a8e92bf67843903af26cacab5b7/README.md#L7-L12)
- components (1 claim(s)):
  - [observation/documented] Generated mutants are written under a logs/_latest/mutants directory, and each mutant run is logged as survived or killed. -- evidence: [README.md#L27-L28](https://github.com/codeintegrity-ai/mutahunter/blob/97221a1aedca8a8e92bf67843903af26cacab5b7/README.md#L27-L28), [README.md#L30-L31](https://github.com/codeintegrity-ai/mutahunter/blob/97221a1aedca8a8e92bf67843903af26cacab5b7/README.md#L30-L31)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] A CLI command 'mutahunter run' accepts a test command, model name, source file path, and test file path as arguments. -- evidence: [README.md#L24-L24](https://github.com/codeintegrity-ai/mutahunter/blob/97221a1aedca8a8e92bf67843903af26cacab5b7/README.md#L24-L24)
  - [inference/documented] The tool appears to run the user-specified test command (e.g. 'mvn clean test') against each generated mutant to determine survival. -- evidence: [README.md#L27-L28](https://github.com/codeintegrity-ai/mutahunter/blob/97221a1aedca8a8e92bf67843903af26cacab5b7/README.md#L27-L28), [README.md#L30-L31](https://github.com/codeintegrity-ai/mutahunter/blob/97221a1aedca8a8e92bf67843903af26cacab5b7/README.md#L30-L31), [README.md#L24-L24](https://github.com/codeintegrity-ai/mutahunter/blob/97221a1aedca8a8e92bf67843903af26cacab5b7/README.md#L24-L24)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation (1 claim(s)):
  - [observation/documented] The tool reports mutation coverage metrics including total, survived, killed, timeout, and compile-error mutant counts plus total cost. -- evidence: [README.md#L40-L47](https://github.com/codeintegrity-ai/mutahunter/blob/97221a1aedca8a8e92bf67843903af26cacab5b7/README.md#L40-L47)
- dependencies (1 claim(s)):
  - [observation/documented] Usage involves setting an OPENAI_API_KEY environment variable, and the example run uses the gpt-4o-mini model. -- evidence: [README.md#L21-L21](https://github.com/codeintegrity-ai/mutahunter/blob/97221a1aedca8a8e92bf67843903af26cacab5b7/README.md#L21-L21), [README.md#L24-L24](https://github.com/codeintegrity-ai/mutahunter/blob/97221a1aedca8a8e92bf67843903af26cacab5b7/README.md#L24-L24)
- limitations: unknown (no source-linked claim submitted for this facet)
- relevance (1 claim(s)):
  - [observation/documented] The repository includes an examples directory with a Java Maven example demonstrating LLM-based mutation testing. -- evidence: [README.md#L57-L57](https://github.com/codeintegrity-ai/mutahunter/blob/97221a1aedca8a8e92bf67843903af26cacab5b7/README.md#L57-L57), [README.md#L55-L55](https://github.com/codeintegrity-ai/mutahunter/blob/97221a1aedca8a8e92bf67843903af26cacab5b7/README.md#L55-L55), [README.md#L59-L59](https://github.com/codeintegrity-ai/mutahunter/blob/97221a1aedca8a8e92bf67843903af26cacab5b7/README.md#L59-L59)

Every claim for this repository is shown above and in [full detail](mutahunter.detail.md).

Metadata and full claim list: [full detail](mutahunter.detail.md)
Human notes ([notes](mutahunter.notes.md), never overwritten by build)

[Back to map index](../../index.md)
