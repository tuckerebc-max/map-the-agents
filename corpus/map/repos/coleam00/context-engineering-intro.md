# coleam00/context-engineering-intro

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit a2d84b021cee @ a72b1e0983fece30

## Summary (orientation draft, not independently verified)

The repository is a documentation/template project for 'context engineering' with Claude Code, containing slash-command definitions, PRP templates, example feature requests, and a CLAUDE.md rules file; evidence is almost entirely instructional documentation rather than shipped runtime code.

## Source coverage

Source coverage (complete): 4 of 4 candidate file(s) selected; repository tree complete. Claims by basis: 14 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

14 claim(s) across 5 facet(s); 8 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] The template ships .claude/commands files (generate-prp.md, execute-prp.md), a PRPs folder with a base template and an example PRP, an examples/ folder, CLAUDE.md, INITIAL.md, and INITIAL_EXAMPLE.md. -- evidence: [README.md#L67-L83](https://github.com/coleam00/context-engineering-intro/blob/a2d84b021cee1e2f4e77ba854bba0be8cb319035/README.md#L67-L83)
  - [observation/documented] INITIAL.md is a fill-in template with FEATURE, EXAMPLES, DOCUMENTATION, and OTHER CONSIDERATIONS sections, and an INITIAL_EXAMPLE.md demonstrates a filled version describing a Pydantic AI multi-agent CLI with Gmail and Brave integrations. -- evidence: [INITIAL.md#L3-L3](https://github.com/coleam00/context-engineering-intro/blob/a2d84b021cee1e2f4e77ba854bba0be8cb319035/INITIAL.md#L3-L3), [INITIAL_EXAMPLE.md#L3-L6](https://github.com/coleam00/context-engineering-intro/blob/a2d84b021cee1e2f4e77ba854bba0be8cb319035/INITIAL_EXAMPLE.md#L3-L6), [INITIAL.md#L15-L15](https://github.com/coleam00/context-engineering-intro/blob/a2d84b021cee1e2f4e77ba854bba0be8cb319035/INITIAL.md#L15-L15), [INITIAL.md#L11-L11](https://github.com/coleam00/context-engineering-intro/blob/a2d84b021cee1e2f4e77ba854bba0be8cb319035/INITIAL.md#L11-L11), [INITIAL.md#L7-L7](https://github.com/coleam00/context-engineering-intro/blob/a2d84b021cee1e2f4e77ba854bba0be8cb319035/INITIAL.md#L7-L7)
- design-choices (3 claim(s)):
  - [observation/documented] The approach centers on PRPs (Product Requirements Prompts), described as comprehensive implementation blueprints with context, validation steps, error-handling patterns, and test requirements, tailored for AI coding assistants. -- evidence: [README.md#L123-L123](https://github.com/coleam00/context-engineering-intro/blob/a2d84b021cee1e2f4e77ba854bba0be8cb319035/README.md#L123-L123), [README.md#L130-L130](https://github.com/coleam00/context-engineering-intro/blob/a2d84b021cee1e2f4e77ba854bba0be8cb319035/README.md#L130-L130), [README.md#L125-L128](https://github.com/coleam00/context-engineering-intro/blob/a2d84b021cee1e2f4e77ba854bba0be8cb319035/README.md#L125-L128)
  - [observation/documented] The template deliberately excludes RAG and tooling aspects of context engineering, which the author says are planned for future work. -- evidence: [README.md#L85-L85](https://github.com/coleam00/context-engineering-intro/blob/a2d84b021cee1e2f4e77ba854bba0be8cb319035/README.md#L85-L85)
- workflows (6 claim(s)):
  - [observation/documented] Repository development practice: the generate-prp command is documented to research codebase patterns, gather documentation, create a blueprint with validation gates, and score its own confidence from 1 to 10. -- evidence: [README.md#L195-L198](https://github.com/coleam00/context-engineering-intro/blob/a2d84b021cee1e2f4e77ba854bba0be8cb319035/README.md#L195-L198), [README.md#L200-L203](https://github.com/coleam00/context-engineering-intro/blob/a2d84b021cee1e2f4e77ba854bba0be8cb319035/README.md#L200-L203), [README.md#L210-L212](https://github.com/coleam00/context-engineering-intro/blob/a2d84b021cee1e2f4e77ba854bba0be8cb319035/README.md#L210-L212), [README.md#L205-L208](https://github.com/coleam00/context-engineering-intro/blob/a2d84b021cee1e2f4e77ba854bba0be8cb319035/README.md#L205-L208)
  - [observation/documented] Repository development practice: the execute-prp flow is documented as loading the PRP, planning tasks with TodoWrite, implementing components, running tests and linting, and iterating on failures. -- evidence: [README.md#L216-L221](https://github.com/coleam00/context-engineering-intro/blob/a2d84b021cee1e2f4e77ba854bba0be8cb319035/README.md#L216-L221)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] Two custom Claude Code slash commands are exposed: /generate-prp, which takes a feature-request file, and /execute-prp, which takes a generated PRP file path. -- evidence: [README.md#L29-L30](https://github.com/coleam00/context-engineering-intro/blob/a2d84b021cee1e2f4e77ba854bba0be8cb319035/README.md#L29-L30), [README.md#L25-L25](https://github.com/coleam00/context-engineering-intro/blob/a2d84b021cee1e2f4e77ba854bba0be8cb319035/README.md#L25-L25), [README.md#L137-L139](https://github.com/coleam00/context-engineering-intro/blob/a2d84b021cee1e2f4e77ba854bba0be8cb319035/README.md#L137-L139)
  - [observation/documented] The slash commands use a $ARGUMENTS variable that receives whatever the user passes after the command name, such as INITIAL.md or a PRP path. -- evidence: [README.md#L141-L141](https://github.com/coleam00/context-engineering-intro/blob/a2d84b021cee1e2f4e77ba854bba0be8cb319035/README.md#L141-L141)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies: unknown (no source-linked claim submitted for this facet)
- limitations (1 claim(s)):
More evidence: [full detail](context-engineering-intro.detail.md)

Metadata and full claim list: [full detail](context-engineering-intro.detail.md)
Human notes ([notes](context-engineering-intro.notes.md), never overwritten by build)

[Back to map index](../../index.md)
