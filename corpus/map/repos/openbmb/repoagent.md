# openbmb/repoagent

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 825d988127d7 @ eea8cc889eeddaae

## Summary (orientation draft, not independently verified)

RepoAgent is an LLM-powered framework for repository-level code documentation generation, distributed on PyPI and described in arXiv 2402.16667. Evidence is README-only (English and Chinese), documenting a CLI, configurable flags, pre-commit integration, and a chat-with-repo prototype; no source-code slices are present.

## Source coverage

Source coverage (partial): 2 of 3 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (2 claim(s)):
  - [observation/documented] Per its README features, RepoAgent detects Git changes (additions, deletions, modifications), analyzes code structure via AST to document individual objects, and identifies bidirectional inter-object invocation relationships. -- evidence: [README.md#L45-L51](https://github.com/OpenBMB/RepoAgent/blob/825d988127d7bfd757237d9c4e8678d9104030f0/README.md#L45-L51)
  - [observation/documented] The README states the tool replaces Markdown content based on changes and uses multi-threaded concurrent operations to improve documentation-generation efficiency. -- evidence: [README.md#L45-L51](https://github.com/OpenBMB/RepoAgent/blob/825d988127d7bfd757237d9c4e8678d9104030f0/README.md#L45-L51)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: contributors set up a development environment with PDM (pdm venv create --name repoagent, then pdm install), with a GitHub Codespace option offered as the easiest route. -- evidence: [README.md#L77-L78](https://github.com/OpenBMB/RepoAgent/blob/825d988127d7bfd757237d9c4e8678d9104030f0/README.md#L77-L78), [README.md#L72-L72](https://github.com/OpenBMB/RepoAgent/blob/825d988127d7bfd757237d9c4e8678d9104030f0/README.md#L72-L72), [README.md#L93-L95](https://github.com/OpenBMB/RepoAgent/blob/825d988127d7bfd757237d9c4e8678d9104030f0/README.md#L93-L95), [README.md#L101-L103](https://github.com/OpenBMB/RepoAgent/blob/825d988127d7bfd757237d9c4e8678d9104030f0/README.md#L101-L103)
  - [observation/documented] In a target git repository, users can configure a pre-commit hook (entry: repoagent, types: [python]) so each git commit triggers automatic change detection and document generation, with RepoAgent modifying staged files before the commit completes. -- evidence: [README.md#L183-L186](https://github.com/OpenBMB/RepoAgent/blob/825d988127d7bfd757237d9c4e8678d9104030f0/README.md#L183-L186), [README.md#L188-L189](https://github.com/OpenBMB/RepoAgent/blob/825d988127d7bfd757237d9c4e8678d9104030f0/README.md#L188-L189), [README.md#L163-L174](https://github.com/OpenBMB/RepoAgent/blob/825d988127d7bfd757237d9c4e8678d9104030f0/README.md#L163-L174)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (4 claim(s)):
  - [observation/documented] RepoAgent provides a CLI: 'repoagent run' generates or updates docs, 'repoagent clean' removes repoagent-related cache, and 'repoagent diff' previews which docs would be updated or generated from current code changes. -- evidence: [README.md#L138-L141](https://github.com/OpenBMB/RepoAgent/blob/825d988127d7bfd757237d9c4e8678d9104030f0/README.md#L138-L141), [README.md#L117-L121](https://github.com/OpenBMB/RepoAgent/blob/825d988127d7bfd757237d9c4e8678d9104030f0/README.md#L117-L121)
  - [observation/documented] The run command accepts optional flags overriding config defaults, including --model (default gpt-3.5-turbo), --temperature (0.2), --request-timeout (60), --base-url, --target-repo-path, --hierarchy-path, --markdown-docs-path, --ignore-list, --language (default Chinese), and --log-level. -- evidence: [README.md#L125-L134](https://github.com/OpenBMB/RepoAgent/blob/825d988127d7bfd757237d9c4e8678d9104030f0/README.md#L125-L134), [README.md#L123-L123](https://github.com/OpenBMB/RepoAgent/blob/825d988127d7bfd757237d9c4e8678d9104030f0/README.md#L123-L123)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] Before configuring parameters, the OpenAI API key must be set as an environment variable, with instructions given for Linux/Mac, Windows cmd, and PowerShell. -- evidence: [README.md#L107-L107](https://github.com/OpenBMB/RepoAgent/blob/825d988127d7bfd757237d9c4e8678d9104030f0/README.md#L107-L107), [README.md#L109-L113](https://github.com/OpenBMB/RepoAgent/blob/825d988127d7bfd757237d9c4e8678d9104030f0/README.md#L109-L113)
- limitations (2 claim(s)):
  - [observation/documented] The pre-commit hook example notes that currently only Python is supported as a trigger file type, and the roadmap lists multi-language support (Java, C, C++) as an unchecked future-work item. -- evidence: [README.md#L212-L214](https://github.com/OpenBMB/RepoAgent/blob/825d988127d7bfd757237d9c4e8678d9104030f0/README.md#L212-L214), [README.md#L163-L174](https://github.com/OpenBMB/RepoAgent/blob/825d988127d7bfd757237d9c4e8678d9104030f0/README.md#L163-L174)
More evidence: [full detail](repoagent.detail.md)

Metadata and full claim list: [full detail](repoagent.detail.md)
Human notes ([notes](repoagent.notes.md), never overwritten by build)

[Back to map index](../../index.md)
