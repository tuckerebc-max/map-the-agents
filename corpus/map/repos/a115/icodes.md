# a115/icodes

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 8961152cb0a9 @ 36f1d6ab199e7277

## Summary (orientation draft, not independently verified)

iCODES is a Python CLI tool that uses LLMs (OpenAI backend) to analyze Git commit histories, build searchable commit-insight indexes, and suggest commit messages from staged changes. Evidence is limited to README documentation.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] iCODES analyzes and indexes Git commit histories using LLM techniques, summarizing commit intents and enabling semantic search over codebases. -- evidence: [README.md#L4-L4](https://github.com/a115/iCODES/blob/8961152cb0a9a517438ccf707c77a4218f93c6e6/README.md#L4-L4)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (1 claim(s)):
  - [inference/documented] The default model choice of gpt-3.5-turbo appears to reflect a deliberate price/quality tradeoff stated in the documentation. -- evidence: [README.md#L21-L21](https://github.com/a115/iCODES/blob/8961152cb0a9a517438ccf707c77a4218f93c6e6/README.md#L21-L21)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: when installing from a cloned repo, Poetry is recommended for dependency management via 'poetry install', and commands are prefixed with 'poetry run python icodes.py'. -- evidence: [README.md#L31-L31](https://github.com/a115/iCODES/blob/8961152cb0a9a517438ccf707c77a4218f93c6e6/README.md#L31-L31), [README.md#L33-L33](https://github.com/a115/iCODES/blob/8961152cb0a9a517438ccf707c77a4218f93c6e6/README.md#L33-L33), [README.md#L29-L29](https://github.com/a115/iCODES/blob/8961152cb0a9a517438ccf707c77a4218f93c6e6/README.md#L29-L29)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (4 claim(s)):
  - [observation/documented] The CLI provides an 'inspect-repo' command taking a repository path and an optional --branch-name flag; without a branch it uses the current branch and analyzes the latest commit. -- evidence: [README.md#L45-L45](https://github.com/a115/iCODES/blob/8961152cb0a9a517438ccf707c77a4218f93c6e6/README.md#L45-L45), [README.md#L41-L41](https://github.com/a115/iCODES/blob/8961152cb0a9a517438ccf707c77a4218f93c6e6/README.md#L41-L41), [README.md#L43-L43](https://github.com/a115/iCODES/blob/8961152cb0a9a517438ccf707c77a4218f93c6e6/README.md#L43-L43)
  - [observation/documented] The 'build-index' command generates an indexed database of commit insights for a given Git repository. -- evidence: [README.md#L52-L52](https://github.com/a115/iCODES/blob/8961152cb0a9a517438ccf707c77a4218f93c6e6/README.md#L52-L52), [README.md#L54-L54](https://github.com/a115/iCODES/blob/8961152cb0a9a517438ccf707c77a4218f93c6e6/README.md#L54-L54)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
  - [observation/documented] The tool requires Python 3.11 or higher and is installable via pip as the 'icodes' package. -- evidence: [README.md#L19-L19](https://github.com/a115/iCODES/blob/8961152cb0a9a517438ccf707c77a4218f93c6e6/README.md#L19-L19), [README.md#L17-L17](https://github.com/a115/iCODES/blob/8961152cb0a9a517438ccf707c77a4218f93c6e6/README.md#L17-L17)
  - [observation/documented] The only supported LLM backend is OpenAI; the OPENAI_API_KEY environment variable must be exported, and DEFAULT_MODEL selects the GPT model (default gpt-3.5-turbo). -- evidence: [README.md#L21-L21](https://github.com/a115/iCODES/blob/8961152cb0a9a517438ccf707c77a4218f93c6e6/README.md#L21-L21)
- limitations (1 claim(s)):
  - [observation/documented] Semantic search and a web-based UI are listed as 'coming soon' features, indicating they are not yet available in the current tool. -- evidence: [README.md#L8-L13](https://github.com/a115/iCODES/blob/8961152cb0a9a517438ccf707c77a4218f93c6e6/README.md#L8-L13)
- relevance (1 claim(s)):
  - [observation/documented] The tool targets developers seeking to understand and navigate codebases by analyzing commit history, trends, and code evolution patterns. -- evidence: [README.md#L4-L4](https://github.com/a115/iCODES/blob/8961152cb0a9a517438ccf707c77a4218f93c6e6/README.md#L4-L4), [README.md#L8-L13](https://github.com/a115/iCODES/blob/8961152cb0a9a517438ccf707c77a4218f93c6e6/README.md#L8-L13)

(2 additional claim(s) omitted for length; see [full detail](icodes.detail.md) for every claim.)

Metadata and full claim list: [full detail](icodes.detail.md)
Human notes ([notes](icodes.notes.md), never overwritten by build)

[Back to map index](../../index.md)
