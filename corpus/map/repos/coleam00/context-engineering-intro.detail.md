# coleam00/context-engineering-intro -- full detail

[Back to orientation](context-engineering-intro.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/coleam00/context-engineering-intro/a2d84b021cee1e2f4e77ba854bba0be8cb319035/a72b1e0983fece30.json](../../../wiki/dossiers/coleam00/context-engineering-intro/a2d84b021cee1e2f4e77ba854bba0be8cb319035/a72b1e0983fece30.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] The template ships .claude/commands files (generate-prp.md, execute-prp.md), a PRPs folder with a base template and an example PRP, an examples/ folder, CLAUDE.md, INITIAL.md, and INITIAL_EXAMPLE.md. -- evidence: [README.md#L67-L83](https://github.com/coleam00/context-engineering-intro/blob/a2d84b021cee1e2f4e77ba854bba0be8cb319035/README.md#L67-L83) (`clm_01cde71315c5786f9cc38c2179754e84a7f3050de3f0084236847c83267d4d2e`)
- [observation/documented] INITIAL.md is a fill-in template with FEATURE, EXAMPLES, DOCUMENTATION, and OTHER CONSIDERATIONS sections, and an INITIAL_EXAMPLE.md demonstrates a filled version describing a Pydantic AI multi-agent CLI with Gmail and Brave integrations. -- evidence: [INITIAL.md#L3-L3](https://github.com/coleam00/context-engineering-intro/blob/a2d84b021cee1e2f4e77ba854bba0be8cb319035/INITIAL.md#L3-L3), [INITIAL_EXAMPLE.md#L3-L6](https://github.com/coleam00/context-engineering-intro/blob/a2d84b021cee1e2f4e77ba854bba0be8cb319035/INITIAL_EXAMPLE.md#L3-L6), [INITIAL.md#L15-L15](https://github.com/coleam00/context-engineering-intro/blob/a2d84b021cee1e2f4e77ba854bba0be8cb319035/INITIAL.md#L15-L15), [INITIAL.md#L11-L11](https://github.com/coleam00/context-engineering-intro/blob/a2d84b021cee1e2f4e77ba854bba0be8cb319035/INITIAL.md#L11-L11), [INITIAL.md#L7-L7](https://github.com/coleam00/context-engineering-intro/blob/a2d84b021cee1e2f4e77ba854bba0be8cb319035/INITIAL.md#L7-L7) (`clm_a1799224fe324850a11a203060a508f098b6ecdb388ac5efad2cd98e5eb83b77`)

## design-choices (3 claim(s))

- [observation/documented] The approach centers on PRPs (Product Requirements Prompts), described as comprehensive implementation blueprints with context, validation steps, error-handling patterns, and test requirements, tailored for AI coding assistants. -- evidence: [README.md#L123-L123](https://github.com/coleam00/context-engineering-intro/blob/a2d84b021cee1e2f4e77ba854bba0be8cb319035/README.md#L123-L123), [README.md#L130-L130](https://github.com/coleam00/context-engineering-intro/blob/a2d84b021cee1e2f4e77ba854bba0be8cb319035/README.md#L130-L130), [README.md#L125-L128](https://github.com/coleam00/context-engineering-intro/blob/a2d84b021cee1e2f4e77ba854bba0be8cb319035/README.md#L125-L128) (`clm_eb7cfcf7207a26b6543a2a305f2c9d854edb4c918cc8f1ca3b56e93ad8046b39`)
- [observation/documented] The template deliberately excludes RAG and tooling aspects of context engineering, which the author says are planned for future work. -- evidence: [README.md#L85-L85](https://github.com/coleam00/context-engineering-intro/blob/a2d84b021cee1e2f4e77ba854bba0be8cb319035/README.md#L85-L85) (`clm_345b3e681017ff9985bcc4bc40c489b3ff055ccd5867781f818e3ebd159dec47`)
- [observation/documented] The examples/ folder is treated as critical to the method's success, with the README advising users to include code-structure, testing, integration, and CLI patterns for the AI to mimic. -- evidence: [README.md#L227-L227](https://github.com/coleam00/context-engineering-intro/blob/a2d84b021cee1e2f4e77ba854bba0be8cb319035/README.md#L227-L227), [README.md#L231-L234](https://github.com/coleam00/context-engineering-intro/blob/a2d84b021cee1e2f4e77ba854bba0be8cb319035/README.md#L231-L234), [README.md#L241-L244](https://github.com/coleam00/context-engineering-intro/blob/a2d84b021cee1e2f4e77ba854bba0be8cb319035/README.md#L241-L244), [README.md#L246-L249](https://github.com/coleam00/context-engineering-intro/blob/a2d84b021cee1e2f4e77ba854bba0be8cb319035/README.md#L246-L249), [README.md#L236-L239](https://github.com/coleam00/context-engineering-intro/blob/a2d84b021cee1e2f4e77ba854bba0be8cb319035/README.md#L236-L239) (`clm_284aba45a62cf86086eaeb918fba55850f15690162052996d11916f8b7fbe600`)

## workflows (6 claim(s))

- [observation/documented] Repository development practice: the generate-prp command is documented to research codebase patterns, gather documentation, create a blueprint with validation gates, and score its own confidence from 1 to 10. -- evidence: [README.md#L195-L198](https://github.com/coleam00/context-engineering-intro/blob/a2d84b021cee1e2f4e77ba854bba0be8cb319035/README.md#L195-L198), [README.md#L200-L203](https://github.com/coleam00/context-engineering-intro/blob/a2d84b021cee1e2f4e77ba854bba0be8cb319035/README.md#L200-L203), [README.md#L210-L212](https://github.com/coleam00/context-engineering-intro/blob/a2d84b021cee1e2f4e77ba854bba0be8cb319035/README.md#L210-L212), [README.md#L205-L208](https://github.com/coleam00/context-engineering-intro/blob/a2d84b021cee1e2f4e77ba854bba0be8cb319035/README.md#L205-L208) (`clm_bd9658e039571d2d7b5a9c353750502d92b1aba4b9e2924ef6e729c6838cd010`)
- [observation/documented] Repository development practice: the execute-prp flow is documented as loading the PRP, planning tasks with TodoWrite, implementing components, running tests and linting, and iterating on failures. -- evidence: [README.md#L216-L221](https://github.com/coleam00/context-engineering-intro/blob/a2d84b021cee1e2f4e77ba854bba0be8cb319035/README.md#L216-L221) (`clm_c42238bc3d90497cb4016cca0da178b5da8fe909c1a62a25a974a50fbbd151dd`)
- [observation/documented] Repository development practice: CLAUDE.md instructs the assistant to read PLANNING.md at conversation start, check TASK.md before tasks, and use the venv_linux virtual environment for Python commands including tests. -- evidence: [CLAUDE.md#L2-L5](https://github.com/coleam00/context-engineering-intro/blob/a2d84b021cee1e2f4e77ba854bba0be8cb319035/CLAUDE.md#L2-L5) (`clm_ce60749007deb18e542be94cf56e325fa3e39b3f18764c2d12457f647e425dee`)
- [observation/documented] Repository development practice: CLAUDE.md mandates Pytest unit tests for new features in a /tests folder mirroring app structure, with at least an expected-use, edge-case, and failure-case test. -- evidence: [CLAUDE.md#L19-L25](https://github.com/coleam00/context-engineering-intro/blob/a2d84b021cee1e2f4e77ba854bba0be8cb319035/CLAUDE.md#L19-L25) (`clm_4b31bfec61ab8ff4bcfaeabf9aca3f2f10aba5b972d6033b58d921f4c9723138`)
- [observation/documented] Repository development practice: CLAUDE.md sets style rules including Python, PEP8, type hints, black formatting, pydantic validation, and Google-style docstrings for every function. -- evidence: [CLAUDE.md#L32-L40](https://github.com/coleam00/context-engineering-intro/blob/a2d84b021cee1e2f4e77ba854bba0be8cb319035/CLAUDE.md#L32-L40) (`clm_b445fa9a7e8dcab7c1596b72875e28792722badbd5456c27e7521d78ad108b13`)
- [observation/documented] Repository development practice: CLAUDE.md behavior rules forbid assuming missing context, hallucinating libraries, referencing unverified file paths, and deleting existing code without explicit instruction. -- evidence: [CLAUDE.md#L56-L59](https://github.com/coleam00/context-engineering-intro/blob/a2d84b021cee1e2f4e77ba854bba0be8cb319035/CLAUDE.md#L56-L59) (`clm_e66fe7aa5b91cc24d539b2498347f2b46de279790c58326f18a2840b15725b31`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] Two custom Claude Code slash commands are exposed: /generate-prp, which takes a feature-request file, and /execute-prp, which takes a generated PRP file path. -- evidence: [README.md#L29-L30](https://github.com/coleam00/context-engineering-intro/blob/a2d84b021cee1e2f4e77ba854bba0be8cb319035/README.md#L29-L30), [README.md#L25-L25](https://github.com/coleam00/context-engineering-intro/blob/a2d84b021cee1e2f4e77ba854bba0be8cb319035/README.md#L25-L25), [README.md#L137-L139](https://github.com/coleam00/context-engineering-intro/blob/a2d84b021cee1e2f4e77ba854bba0be8cb319035/README.md#L137-L139) (`clm_81386967363afd72d458ae2f37681a1fd019adc10495df94f1265e749eb58272`)
- [observation/documented] The slash commands use a $ARGUMENTS variable that receives whatever the user passes after the command name, such as INITIAL.md or a PRP path. -- evidence: [README.md#L141-L141](https://github.com/coleam00/context-engineering-intro/blob/a2d84b021cee1e2f4e77ba854bba0be8cb319035/README.md#L141-L141) (`clm_1028e4fd45bf9a6aef86cff52d0800b238449ee229e3e5e84d5d2a57fe291069`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## limitations (1 claim(s))

- [inference/documented] The evidence consists only of README, CLAUDE.md, and INITIAL template files; no implementation code for the slash commands' behavior appears in the provided slices, so their described steps appear to be documentation rather than inspected code. -- evidence: [README.md#L137-L139](https://github.com/coleam00/context-engineering-intro/blob/a2d84b021cee1e2f4e77ba854bba0be8cb319035/README.md#L137-L139), [README.md#L67-L83](https://github.com/coleam00/context-engineering-intro/blob/a2d84b021cee1e2f4e77ba854bba0be8cb319035/README.md#L67-L83) (`clm_d688749afa8c5aa51f96ab47ca90b5b6f12daa18d776b94b04f361e9f443f7e4`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

