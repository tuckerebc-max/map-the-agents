# shotgun-sh/shotgun

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 4d344d5a46aa @ 8d70e09acc259e1e

## Summary (orientation draft, not independently verified)

Selected evidence records: Shotgun is described as a spec-driven development CLI that reads the whole codebase, plans features upfront, and splits work into staged PRs with file-by-file instructions for AI coding agents. A Router internally dispatches specialized sub-agents across Research, Specify, Plan, Tasks, and Export phases; users control only the Planning and Drafting execution modes.

## Source coverage

Source coverage (partial): 6 of 17 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Shotgun is described as a spec-driven development CLI that reads the whole codebase, plans features upfront, and splits work into staged PRs with file-by-file instructions for AI coding agents. -- evidence: [README.md#L7-L24](https://github.com/shotgun-sh/shotgun/blob/4d344d5a46aafc815de441ff670d4131187f33e6/README.md#L7-L24), [README.md#L42-L42](https://github.com/shotgun-sh/shotgun/blob/4d344d5a46aafc815de441ff670d4131187f33e6/README.md#L42-L42), [docs/CASE_STUDY.md#L5-L5](https://github.com/shotgun-sh/shotgun/blob/4d344d5a46aafc815de441ff670d4131187f33e6/docs/CASE_STUDY.md#L5-L5), [README.md#L40-L40](https://github.com/shotgun-sh/shotgun/blob/4d344d5a46aafc815de441ff670d4131187f33e6/README.md#L40-L40)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (1 claim(s)):
  - [observation/documented] Each phase (research, spec, plan, tasks, export) uses a separate specialized agent with phase-tailored prompts rather than a single general-purpose agent. -- evidence: [README.md#L295-L303](https://github.com/shotgun-sh/shotgun/blob/4d344d5a46aafc815de441ff670d4131187f33e6/README.md#L295-L303)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: the README points contributors to a Contributing Guide, Git Hooks (Lefthook, trufflehog, security scanning), CI/CD via GitHub Actions, observability, and Docker docs, and welcomes bug/feature/doc issue templates. -- evidence: [README.md#L382-L382](https://github.com/shotgun-sh/shotgun/blob/4d344d5a46aafc815de441ff670d4131187f33e6/README.md#L382-L382), [README.md#L400-L404](https://github.com/shotgun-sh/shotgun/blob/4d344d5a46aafc815de441ff670d4131187f33e6/README.md#L400-L404), [README.md#L386-L388](https://github.com/shotgun-sh/shotgun/blob/4d344d5a46aafc815de441ff670d4131187f33e6/README.md#L386-L388)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] Planning mode proposes a plan with confirmation checkpoints before file-changing agents run, while Drafting runs the full plan without intermediate prompts; Shift+Tab switches modes and '/' opens the command palette. -- evidence: [README.md#L171-L174](https://github.com/shotgun-sh/shotgun/blob/4d344d5a46aafc815de441ff670d4131187f33e6/README.md#L171-L174), [README.md#L176-L176](https://github.com/shotgun-sh/shotgun/blob/4d344d5a46aafc815de441ff670d4131187f33e6/README.md#L176-L176)
  - [observation/documented] Keyboard shortcuts include Shift+Tab for mode switching, Ctrl+C to cancel, Escape to exit Q&A or stop an agent, and Ctrl+U to view usage stats. -- evidence: [README.md#L201-L207](https://github.com/shotgun-sh/shotgun/blob/4d344d5a46aafc815de441ff670d4131187f33e6/README.md#L201-L207)
- memory-state (1 claim(s)):
  - [observation/documented] Codebase indexing runs locally using tree-sitter parsing, producing a searchable code graph stored under ~/.shotgun-sh/codebases/ that the FAQ says is never sent to a server. -- evidence: [README.md#L377-L377](https://github.com/shotgun-sh/shotgun/blob/4d344d5a46aafc815de441ff670d4131187f33e6/README.md#L377-L377), [README.md#L359-L359](https://github.com/shotgun-sh/shotgun/blob/4d344d5a46aafc815de441ff670d4131187f33e6/README.md#L359-L359)
- orchestration (1 claim(s)):
  - [observation/documented] A Router internally dispatches specialized sub-agents across Research, Specify, Plan, Tasks, and Export phases; users control only the Planning and Drafting execution modes. -- evidence: [README.md#L181-L193](https://github.com/shotgun-sh/shotgun/blob/4d344d5a46aafc815de441ff670d4131187f33e6/README.md#L181-L193), [README.md#L195-L195](https://github.com/shotgun-sh/shotgun/blob/4d344d5a46aafc815de441ff670d4131187f33e6/README.md#L195-L195), [README.md#L179-L179](https://github.com/shotgun-sh/shotgun/blob/4d344d5a46aafc815de441ff670d4131187f33e6/README.md#L179-L179)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
  - [observation/documented] Supported LLM providers are OpenAI, Anthropic (Claude), and Google Gemini; local LLM support is stated as planned, and internet access is required for LLM API calls. -- evidence: [README.md#L369-L369](https://github.com/shotgun-sh/shotgun/blob/4d344d5a46aafc815de441ff670d4131187f33e6/README.md#L369-L369), [README.md#L373-L373](https://github.com/shotgun-sh/shotgun/blob/4d344d5a46aafc815de441ff670d4131187f33e6/README.md#L373-L373), [README.md#L365-L365](https://github.com/shotgun-sh/shotgun/blob/4d344d5a46aafc815de441ff670d4131187f33e6/README.md#L365-L365)
More evidence: [full detail](shotgun.detail.md)

Metadata and full claim list: [full detail](shotgun.detail.md)
Human notes ([notes](shotgun.notes.md), never overwritten by build)

[Back to map index](../../index.md)
