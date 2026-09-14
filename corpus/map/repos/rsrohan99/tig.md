# rsrohan99/tig

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 3df12189c01e @ ebda47659608a8ec

## Summary (orientation draft, not independently verified)

Tig is a terminal-based autonomous AI coding agent supporting multiple LLM providers, with Architect/Code modes, file and shell actions, and an optional auto-approve flag. Evidence is README-only, so claims are documentation-based.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 10 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

10 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Tig is described as an autonomous AI coding agent that runs in the terminal, comparable to Claude Code and OpenAI Codex but supporting more LLMs. -- evidence: [README.md#L2-L2](https://github.com/rsrohan99/tig/blob/3df12189c01e2674991bc998404af7217ae5b9d8/README.md#L2-L2)
- components (2 claim(s)):
  - [observation/documented] The agent can write code, fix bugs, execute shell commands, write tests, and analyze a codebase, all within the terminal. -- evidence: [README.md#L4-L9](https://github.com/rsrohan99/tig/blob/3df12189c01e2674991bc998404af7217ae5b9d8/README.md#L4-L9), [README.md#L11-L11](https://github.com/rsrohan99/tig/blob/3df12189c01e2674991bc998404af7217ae5b9d8/README.md#L11-L11)
  - [observation/documented] The toolchain uses LlamaIndex Workflows for orchestration and multi-LLM support, Tree-sitter for code-definition search and syntax-error checking, Ripgrep for regex search, and diff-match-patch for displaying diffs. -- evidence: [README.md#L35-L38](https://github.com/rsrohan99/tig/blob/3df12189c01e2674991bc998404af7217ae5b9d8/README.md#L35-L38)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows (1 claim(s)):
  - [observation/documented] Users start a session by running tig and entering a task at the 'New task' prompt. -- evidence: [README.md#L95-L100](https://github.com/rsrohan99/tig/blob/3df12189c01e2674991bc998404af7217ae5b9d8/README.md#L95-L100)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] Tig offers task modes: an Architect mode that designs systems and saves designs to a markdown file, and a Code mode that implements the architect's plan step by step. -- evidence: [README.md#L19-L21](https://github.com/rsrohan99/tig/blob/3df12189c01e2674991bc998404af7217ae5b9d8/README.md#L19-L21)
  - [observation/documented] Tig is installed via pip as the tig-code package and run with the tig command, optionally with a --mode flag choosing code or architect. -- evidence: [README.md#L68-L72](https://github.com/rsrohan99/tig/blob/3df12189c01e2674991bc998404af7217ae5b9d8/README.md#L68-L72), [README.md#L86-L93](https://github.com/rsrohan99/tig/blob/3df12189c01e2674991bc998404af7217ae5b9d8/README.md#L86-L93)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
  - [observation/documented] By default Tig's file read/write/update actions appear to require approval; a --auto-approve flag lets users auto-approve all actions. -- evidence: [README.md#L86-L93](https://github.com/rsrohan99/tig/blob/3df12189c01e2674991bc998404af7217ae5b9d8/README.md#L86-L93)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
  - [observation/documented] Supported LLM providers include Google Gemini, OpenAI, Claude, OpenRouter, Deepseek, Groq, and local models via Ollama. -- evidence: [README.md#L23-L30](https://github.com/rsrohan99/tig/blob/3df12189c01e2674991bc998404af7217ae5b9d8/README.md#L23-L30)
  - [observation/documented] Ripgrep is listed as an external tool Tig depends on, with per-OS install instructions (Homebrew on macOS, pacman on Arch, dnf on Fedora). -- evidence: [README.md#L56-L59](https://github.com/rsrohan99/tig/blob/3df12189c01e2674991bc998404af7217ae5b9d8/README.md#L56-L59), [README.md#L45-L45](https://github.com/rsrohan99/tig/blob/3df12189c01e2674991bc998404af7217ae5b9d8/README.md#L45-L45), [README.md#L43-L43](https://github.com/rsrohan99/tig/blob/3df12189c01e2674991bc998404af7217ae5b9d8/README.md#L43-L43), [README.md#L61-L64](https://github.com/rsrohan99/tig/blob/3df12189c01e2674991bc998404af7217ae5b9d8/README.md#L61-L64), [README.md#L49-L52](https://github.com/rsrohan99/tig/blob/3df12189c01e2674991bc998404af7217ae5b9d8/README.md#L49-L52)
- limitations: unknown (no source-linked claim submitted for this facet)
- relevance: unknown (no source-linked claim submitted for this facet)

(1 additional claim(s) omitted for length; see [full detail](tig.detail.md) for every claim.)

Metadata and full claim list: [full detail](tig.detail.md)
Human notes ([notes](tig.notes.md), never overwritten by build)

[Back to map index](../../index.md)
