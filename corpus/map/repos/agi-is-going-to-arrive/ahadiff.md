# agi-is-going-to-arrive/ahadiff

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 36da35e9fd40 @ 6283c64863f1d387

## Summary (orientation draft, not independently verified)

ahadiff serve creates local state and opens a WebUI at http://127.0.0.1:8765, with a --no-browser option; ordinary folders work while init and doctor target Git repositories. The WebUI supports five learning sources: Git changes, two files, a pasted diff, a saved snapshot, or a single Markdown document, with local preview before a generation request.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] Deterministic scoring covers eight dimensions with required evidence and safety checks; an optional LLM judge gives feedback but cannot override the final verdict. -- evidence: [README.md#L128-L132](https://github.com/AGI-is-going-to-arrive/ahadiff/blob/36da35e9fd4092da79c00fadec03f3b62615ba58/README.md#L128-L132)
  - [observation/documented] Snapshots store a sanitized copy of an earlier file for later comparison without modifying originals, and are learning references rather than full backups. -- evidence: [README.md#L13-L17](https://github.com/AGI-is-going-to-arrive/ahadiff/blob/36da35e9fd4092da79c00fadec03f3b62615ba58/README.md#L13-L17), [README.md#L102-L102](https://github.com/AGI-is-going-to-arrive/ahadiff/blob/36da35e9fd4092da79c00fadec03f3b62615ba58/README.md#L102-L102)
- design-choices (1 claim(s)):
  - [observation/documented] Default privacy mode is strict_local; redacted_remote or explicit_remote must be chosen before remote providers, and the tool checks for secrets and suspicious instructions while advising user inspection. -- evidence: [README.md#L122-L122](https://github.com/AGI-is-going-to-arrive/ahadiff/blob/36da35e9fd4092da79c00fadec03f3b62615ba58/README.md#L122-L122)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: building from source requires cloning the repo, running 'uv sync --locked --dev', and building the viewer with pnpm before an editable uv tool install. -- evidence: [README.md#L188-L195](https://github.com/AGI-is-going-to-arrive/ahadiff/blob/36da35e9fd4092da79c00fadec03f3b62615ba58/README.md#L188-L195), [README.md#L186-L186](https://github.com/AGI-is-going-to-arrive/ahadiff/blob/36da35e9fd4092da79c00fadec03f3b62615ba58/README.md#L186-L186)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] ahadiff serve creates local state and opens a WebUI at http://127.0.0.1:8765, with a --no-browser option; ordinary folders work while init and doctor target Git repositories. -- evidence: [README.md#L54-L54](https://github.com/AGI-is-going-to-arrive/ahadiff/blob/36da35e9fd4092da79c00fadec03f3b62615ba58/README.md#L54-L54)
  - [observation/documented] The WebUI supports five learning sources: Git changes, two files, a pasted diff, a saved snapshot, or a single Markdown document, with local preview before a generation request. -- evidence: [README.md#L13-L17](https://github.com/AGI-is-going-to-arrive/ahadiff/blob/36da35e9fd4092da79c00fadec03f3b62615ba58/README.md#L13-L17), [README.md#L61-L67](https://github.com/AGI-is-going-to-arrive/ahadiff/blob/36da35e9fd4092da79c00fadec03f3b62615ba58/README.md#L61-L67)
- memory-state (1 claim(s)):
  - [observation/documented] Learning history and review records are stored under .ahadiff/ in each working folder; API keys go into a scope-specific .env with an environment-variable reference in config.toml. -- evidence: [README.md#L124-L124](https://github.com/AGI-is-going-to-arrive/ahadiff/blob/36da35e9fd4092da79c00fadec03f3b62615ba58/README.md#L124-L124), [README.md#L42-L42](https://github.com/AGI-is-going-to-arrive/ahadiff/blob/36da35e9fd4092da79c00fadec03f3b62615ba58/README.md#L42-L42)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
  - [observation/documented] Installable via pipx or uv tool; an optional 'optimizer' extra adds torch for FSRS parameter optimization, which base review and scheduling do not need. -- evidence: [README.md#L26-L26](https://github.com/AGI-is-going-to-arrive/ahadiff/blob/36da35e9fd4092da79c00fadec03f3b62615ba58/README.md#L26-L26), [README.md#L23-L24](https://github.com/AGI-is-going-to-arrive/ahadiff/blob/36da35e9fd4092da79c00fadec03f3b62615ba58/README.md#L23-L24), [README.md#L44-L44](https://github.com/AGI-is-going-to-arrive/ahadiff/blob/36da35e9fd4092da79c00fadec03f3b62615ba58/README.md#L44-L44)
  - [observation/documented] Provider classes include openai, openai_responses, gemini, anthropic, azure, newapi, openai_compat, lmstudio, and ollama, covering local and remote LLM endpoints. -- evidence: [README.md#L116-L116](https://github.com/AGI-is-going-to-arrive/ahadiff/blob/36da35e9fd4092da79c00fadec03f3b62615ba58/README.md#L116-L116)
- limitations (2 claim(s)):
More evidence: [full detail](ahadiff.detail.md)

Metadata and full claim list: [full detail](ahadiff.detail.md)
Human notes ([notes](ahadiff.notes.md), never overwritten by build)

[Back to map index](../../index.md)
