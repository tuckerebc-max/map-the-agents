# gszhangwei/open-spdd

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 59669ac18c1c @ 6eae32fd657aa164

## Summary (orientation draft, not independently verified)

Selected evidence records: The tool auto-detects the user's AI coding environment and writes command templates into tool-specific directories, e.g. .cursor/commands/, .claude/commands/, .github/copilot-prompts/, and .agents/skills/ for Codex. The methodology centers on a 7-dimension REASONS Canvas (Requirements, Entities, Approach, Structure, Operations, Norms, Safeguards) treating prompts as executable design contracts rather than task lists.

## Source coverage

Source coverage (complete): 5 of 5 candidate file(s) selected; repository tree complete. Claims by basis: 10 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

10 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The tool auto-detects the user's AI coding environment and writes command templates into tool-specific directories, e.g. .cursor/commands/, .claude/commands/, .github/copilot-prompts/, and .agents/skills/ for Codex. -- evidence: [README.md#L262-L269](https://github.com/gszhangwei/open-spdd/blob/59669ac18c1c0bdee76b780771ac51567a73d52c/README.md#L262-L269), [README.md#L96-L100](https://github.com/gszhangwei/open-spdd/blob/59669ac18c1c0bdee76b780771ac51567a73d52c/README.md#L96-L100)
- design-choices (4 claim(s)):
  - [observation/documented] The methodology centers on a 7-dimension REASONS Canvas (Requirements, Entities, Approach, Structure, Operations, Norms, Safeguards) treating prompts as executable design contracts rather than task lists. -- evidence: [README.md#L17-L17](https://github.com/gszhangwei/open-spdd/blob/59669ac18c1c0bdee76b780771ac51567a73d52c/README.md#L17-L17), [README.md#L38-L52](https://github.com/gszhangwei/open-spdd/blob/59669ac18c1c0bdee76b780771ac51567a73d52c/README.md#L38-L52), [README.md#L32-L32](https://github.com/gszhangwei/open-spdd/blob/59669ac18c1c0bdee76b780771ac51567a73d52c/README.md#L32-L32), [README.md#L36-L36](https://github.com/gszhangwei/open-spdd/blob/59669ac18c1c0bdee76b780771ac51567a73d52c/README.md#L36-L36)
  - [observation/documented] All templates are embedded in a single Go binary via Go's embed directive, and the tool provides an interactive terminal UI for command selection. -- evidence: [README.md#L96-L100](https://github.com/gszhangwei/open-spdd/blob/59669ac18c1c0bdee76b780771ac51567a73d52c/README.md#L96-L100)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributors run tests with go test ./tests/..., with verbose and per-module variants like ./tests/detector/... and ./tests/templates/..., and can build from source with go build ./cmd/openspdd. -- evidence: [README.md#L384-L389](https://github.com/gszhangwei/open-spdd/blob/59669ac18c1c0bdee76b780771ac51567a73d52c/README.md#L384-L389), [README.md#L398-L398](https://github.com/gszhangwei/open-spdd/blob/59669ac18c1c0bdee76b780771ac51567a73d52c/README.md#L398-L398), [README.md#L401-L403](https://github.com/gszhangwei/open-spdd/blob/59669ac18c1c0bdee76b780771ac51567a73d52c/README.md#L401-L403), [README.md#L395-L395](https://github.com/gszhangwei/open-spdd/blob/59669ac18c1c0bdee76b780771ac51567a73d52c/README.md#L395-L395)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] The uninstall command detects the install method (Homebrew or go install), prints a plan, requires confirmation by default, and refuses to act on unclassifiable installs such as manually copied binaries. -- evidence: [README.md#L150-L150](https://github.com/gszhangwei/open-spdd/blob/59669ac18c1c0bdee76b780771ac51567a73d52c/README.md#L150-L150), [README.md#L163-L163](https://github.com/gszhangwei/open-spdd/blob/59669ac18c1c0bdee76b780771ac51567a73d52c/README.md#L163-L163)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] The tool is written in Go and installable via Homebrew (gszhangwei/tools/openspdd), go install from cmd/openspdd, a scripts/install.sh script, or prebuilt GitHub Releases binaries. -- evidence: [README.md#L384-L389](https://github.com/gszhangwei/open-spdd/blob/59669ac18c1c0bdee76b780771ac51567a73d52c/README.md#L384-L389), [README.md#L106-L108](https://github.com/gszhangwei/open-spdd/blob/59669ac18c1c0bdee76b780771ac51567a73d52c/README.md#L106-L108), [README.md#L119-L121](https://github.com/gszhangwei/open-spdd/blob/59669ac18c1c0bdee76b780771ac51567a73d52c/README.md#L119-L121), [README.md#L137-L137](https://github.com/gszhangwei/open-spdd/blob/59669ac18c1c0bdee76b780771ac51567a73d52c/README.md#L137-L137), [README.md#L146-L146](https://github.com/gszhangwei/open-spdd/blob/59669ac18c1c0bdee76b780771ac51567a73d52c/README.md#L146-L146)
- limitations (1 claim(s)):
  - [observation/documented] On some Codex versions, skills from untrusted projects are silently ignored; users must mark the project trusted in ~/.codex/config.toml or restart Codex if skills do not appear. -- evidence: [README.md#L275-L275](https://github.com/gszhangwei/open-spdd/blob/59669ac18c1c0bdee76b780771ac51567a73d52c/README.md#L275-L275)
- relevance (1 claim(s)):
  - [observation/documented] The project targets AI-assisted business development where design-intent drift causes rework, recommending itself for enterprise features, team collaboration, and complex refactoring, but not for one-off scripts. -- evidence: [docs/design-philosophy.md#L3-L3](https://github.com/gszhangwei/open-spdd/blob/59669ac18c1c0bdee76b780771ac51567a73d52c/docs/design-philosophy.md#L3-L3), [docs/design-philosophy.md#L15-L15](https://github.com/gszhangwei/open-spdd/blob/59669ac18c1c0bdee76b780771ac51567a73d52c/docs/design-philosophy.md#L15-L15), [README.md#L373-L380](https://github.com/gszhangwei/open-spdd/blob/59669ac18c1c0bdee76b780771ac51567a73d52c/README.md#L373-L380)
More evidence: [full detail](open-spdd.detail.md)

Metadata and full claim list: [full detail](open-spdd.detail.md)
Human notes ([notes](open-spdd.notes.md), never overwritten by build)

[Back to map index](../../index.md)
