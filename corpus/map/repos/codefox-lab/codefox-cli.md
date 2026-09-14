# codefox-lab/codefox-cli

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 7b5f855fb6b5 @ 33c5a99fd2de433d

## Summary (orientation draft, not independently verified)

Selected evidence records: The CLI exposes commands: init, list, scan, version, clean, and --help, per the commands table. The scan command collects the current git diff, loads project context, sends a review request to the configured model, and returns review comments with optional fix suggestions.

## Source coverage

Source coverage (partial): 6 of 7 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 5 facet(s); 8 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] RAG-based context retrieval is configurable: chunk size, overlap, max RAG characters, embedding batch size, and lazy loading, with fastembed embedding defaulting to BAAI/bge-small-en-v1.5. -- evidence: [WIKI.md#L194-L209](https://github.com/codefox-lab/CodeFox-CLI/blob/7b5f855fb6b5fb6d842327a40702d785aa379fb4/WIKI.md#L194-L209), [WIKI.md#L177-L177](https://github.com/codefox-lab/CodeFox-CLI/blob/7b5f855fb6b5fb6d842327a40702d785aa379fb4/WIKI.md#L177-L177), [WIKI.md#L175-L175](https://github.com/codefox-lab/CodeFox-CLI/blob/7b5f855fb6b5fb6d842327a40702d785aa379fb4/WIKI.md#L175-L175)
- design-choices (4 claim(s)):
  - [observation/documented] The tool is positioned as a CLI-first diff review tool, explicitly not an IDE coding assistant like Cursor or Claude Code. -- evidence: [README.md#L63-L63](https://github.com/codefox-lab/CodeFox-CLI/blob/7b5f855fb6b5fb6d842327a40702d785aa379fb4/README.md#L63-L63), [README.md#L65-L66](https://github.com/codefox-lab/CodeFox-CLI/blob/7b5f855fb6b5fb6d842327a40702d785aa379fb4/README.md#L65-L66)
  - [observation/documented] Supported providers are Gemini (default), Ollama for local/remote servers, and OpenRouter; Ollama allows fully local reviews. -- evidence: [README.md#L83-L85](https://github.com/codefox-lab/CodeFox-CLI/blob/7b5f855fb6b5fb6d842327a40702d785aa379fb4/README.md#L83-L85), [README.md#L33-L35](https://github.com/codefox-lab/CodeFox-CLI/blob/7b5f855fb6b5fb6d842327a40702d785aa379fb4/README.md#L33-L35), [WIKI.md#L47-L49](https://github.com/codefox-lab/CodeFox-CLI/blob/7b5f855fb6b5fb6d842327a40702d785aa379fb4/WIKI.md#L47-L49), [WIKI.md#L53-L57](https://github.com/codefox-lab/CodeFox-CLI/blob/7b5f855fb6b5fb6d842327a40702d785aa379fb4/WIKI.md#L53-L57)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: dev setup installs pytest, mypy, ruff, and types-PyYAML; tests run with 'pytest tests -v', linting via ruff, and type checking via mypy codefox. -- evidence: [README.md#L240-L243](https://github.com/codefox-lab/CodeFox-CLI/blob/7b5f855fb6b5fb6d842327a40702d785aa379fb4/README.md#L240-L243), [README.md#L247-L249](https://github.com/codefox-lab/CodeFox-CLI/blob/7b5f855fb6b5fb6d842327a40702d785aa379fb4/README.md#L247-L249), [README.md#L219-L219](https://github.com/codefox-lab/CodeFox-CLI/blob/7b5f855fb6b5fb6d842327a40702d785aa379fb4/README.md#L219-L219), [requirements-dev.txt#L3-L8](https://github.com/codefox-lab/CodeFox-CLI/blob/7b5f855fb6b5fb6d842327a40702d785aa379fb4/requirements-dev.txt#L3-L8), [README.md#L234-L236](https://github.com/codefox-lab/CodeFox-CLI/blob/7b5f855fb6b5fb6d842327a40702d785aa379fb4/README.md#L234-L236)
  - [observation/documented] Repository development practice: bug reports, pull requests, and documentation improvements are welcome, and a Contributor Covenant-based code of conduct governs the community. -- evidence: [CODE_OF_CONDUCT.md#L117-L119](https://github.com/codefox-lab/CodeFox-CLI/blob/7b5f855fb6b5fb6d842327a40702d785aa379fb4/CODE_OF_CONDUCT.md#L117-L119), [README.md#L255-L255](https://github.com/codefox-lab/CodeFox-CLI/blob/7b5f855fb6b5fb6d842327a40702d785aa379fb4/README.md#L255-L255)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The CLI exposes commands: init, list, scan, version, clean, and --help, per the commands table. -- evidence: [README.md#L190-L197](https://github.com/codefox-lab/CodeFox-CLI/blob/7b5f855fb6b5fb6d842327a40702d785aa379fb4/README.md#L190-L197)
  - [observation/documented] The scan command collects the current git diff, loads project context, sends a review request to the configured model, and returns review comments with optional fix suggestions. -- evidence: [README.md#L131-L131](https://github.com/codefox-lab/CodeFox-CLI/blob/7b5f855fb6b5fb6d842327a40702d785aa379fb4/README.md#L131-L131), [README.md#L127-L127](https://github.com/codefox-lab/CodeFox-CLI/blob/7b5f855fb6b5fb6d842327a40702d785aa379fb4/README.md#L127-L127), [README.md#L135-L135](https://github.com/codefox-lab/CodeFox-CLI/blob/7b5f855fb6b5fb6d842327a40702d785aa379fb4/README.md#L135-L135), [README.md#L133-L133](https://github.com/codefox-lab/CodeFox-CLI/blob/7b5f855fb6b5fb6d842327a40702d785aa379fb4/README.md#L133-L133), [README.md#L129-L129](https://github.com/codefox-lab/CodeFox-CLI/blob/7b5f855fb6b5fb6d842327a40702d785aa379fb4/README.md#L129-L129), [README.md#L122-L125](https://github.com/codefox-lab/CodeFox-CLI/blob/7b5f855fb6b5fb6d842327a40702d785aa379fb4/README.md#L122-L125)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] Runtime dependencies include GitPython, google-genai, ollama, openai, qdrant-client, fastembed, typer, rich, PyGithub, and python-gitlab, per requirements.txt. -- evidence: [requirements.txt#L1-L19](https://github.com/codefox-lab/CodeFox-CLI/blob/7b5f855fb6b5fb6d842327a40702d785aa379fb4/requirements.txt#L1-L19)
- limitations: unknown (no source-linked claim submitted for this facet)
- relevance: unknown (no source-linked claim submitted for this facet)

(3 additional claim(s) omitted for length; see [full detail](codefox-cli.detail.md) for every claim.)

Metadata and full claim list: [full detail](codefox-cli.detail.md)
Human notes ([notes](codefox-cli.notes.md), never overwritten by build)

[Back to map index](../../index.md)
