# haseeb-heaven/open-agent

Status: distilled - Freshness: current
Catalog classes: agent
Origins: github-rename-resolution, alltheagents.org-backing, github-verified-rename - Projects: navy-yard, Observatory
Formerly: haseeb-heaven/code-interpreter (github id 701162675).
Latest snapshot: commit 575401684ec1 @ 37fd1230e5bca33c

## Summary (orientation draft, not independently verified)

OpenAgent is a terminal-based open-source coding/agent CLI (an Apache-2.0 fork of Gemini CLI) supporting multiple local and cloud model providers, sandboxed tool execution, Markdown-based memory, extensions, and Agent Skills. Evidence is mostly README and docs; no source code slices are present, so claims are documentation-based. Evidence coverage: 175 of 213 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 110 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 18 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

18 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] A web search tool (google_web_search) auto-selects a backend from available keys, with a no-key fallback chain of Exa (hosted MCP) then DuckDuckGo, and supports Brave, Tavily, and Serper, forcible via WEB_SEARCH_PROVIDER. -- evidence: [README.md#L93-L94](https://github.com/haseeb-heaven/open-agent/blob/575401684ec13df646fa831f1c824388b5b30574/README.md#L93-L94), [README.md#L83-L85](https://github.com/haseeb-heaven/open-agent/blob/575401684ec13df646fa831f1c824388b5b30574/README.md#L83-L85)
  - [observation/documented] Model definitions live in a registry file configs/models.toml, referenced from the README alongside a full matrix in Models.MD. -- evidence: [README.md#L113-L114](https://github.com/haseeb-heaven/open-agent/blob/575401684ec13df646fa831f1c824388b5b30574/README.md#L113-L114)
- design-choices (2 claim(s)):
  - [observation/documented] The tool is positioned as local-first and BYOK: it supports free OpenRouter models, local Ollama/LM Studio, runs on Windows/Mac/Linux, and requires no account. -- evidence: [README.md#L12-L13](https://github.com/haseeb-heaven/open-agent/blob/575401684ec13df646fa831f1c824388b5b30574/README.md#L12-L13), [README.md#L24-L25](https://github.com/haseeb-heaven/open-agent/blob/575401684ec13df646fa831f1c824388b5b30574/README.md#L24-L25)
  - [observation/documented] The project is a fork of Google's Gemini CLI (Apache-2.0) with modifications by Haseeb Mir, and is itself licensed Apache-2.0. -- evidence: [README.md#L180-L181](https://github.com/haseeb-heaven/open-agent/blob/575401684ec13df646fa831f1c824388b5b30574/README.md#L180-L181), [README.md#L185-L185](https://github.com/haseeb-heaven/open-agent/blob/575401684ec13df646fa831f1c824388b5b30574/README.md#L185-L185)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: tests run from repo root with npm test using Vitest, which auto-loads root .env (missing keys skip; live quota soft-skips); unit and live provider test commands are documented, with live tests gated by RUN_LIVE_PROVIDER_TESTS / RUN_LOCAL_PROVIDER_TESTS env vars. -- evidence: [README.md#L163-L163](https://github.com/haseeb-heaven/open-agent/blob/575401684ec13df646fa831f1c824388b5b30574/README.md#L163-L163), [README.md#L167-L168](https://github.com/haseeb-heaven/open-agent/blob/575401684ec13df646fa831f1c824388b5b30574/README.md#L167-L168), [README.md#L156-L157](https://github.com/haseeb-heaven/open-agent/blob/575401684ec13df646fa831f1c824388b5b30574/README.md#L156-L157), [README.md#L165-L165](https://github.com/haseeb-heaven/open-agent/blob/575401684ec13df646fa831f1c824388b5b30574/README.md#L165-L165), [README.md#L153-L154](https://github.com/haseeb-heaven/open-agent/blob/575401684ec13df646fa831f1c824388b5b30574/README.md#L153-L154)
  - [observation/documented] Repository development practice: canonical agent instructions for AI coding agents working in this repo live in OPENAGENT.md, referenced from GEMINI.md as applying to Claude Code, Gemini CLI, Codex, opencode, and OpenAgent itself. -- evidence: [GEMINI.md#L3-L5](https://github.com/haseeb-heaven/open-agent/blob/575401684ec13df646fa831f1c824388b5b30574/GEMINI.md#L3-L5)
- skills-patterns (1 claim(s)):
  - [observation/documented] Agent Skills follow a lifecycle of discovery (metadata injected into the system prompt), activation via an activate_skill tool, user consent, injection of SKILL.md content, and execution; skills are discovered from built-in, extension, user (~/.openagent/skills/), and workspace (.openagent/skills/) tiers with precedence rules. -- evidence: [docs/cli/skills.md#L40-L48](https://github.com/haseeb-heaven/open-agent/blob/575401684ec13df646fa831f1c824388b5b30574/docs/cli/skills.md#L40-L48), [docs/cli/skills.md#L52-L55](https://github.com/haseeb-heaven/open-agent/blob/575401684ec13df646fa831f1c824388b5b30574/docs/cli/skills.md#L52-L55), [docs/cli/skills.md#L20-L33](https://github.com/haseeb-heaven/open-agent/blob/575401684ec13df646fa831f1c824388b5b30574/docs/cli/skills.md#L20-L33)
- interfaces (3 claim(s)):
  - [observation/documented] The CLI exposes flags including --provider, -m/--model, --free, --models, --byok, and -y/--yolo for auto-approving tools in trusted workspaces. -- evidence: [README.md#L116-L123](https://github.com/haseeb-heaven/open-agent/blob/575401684ec13df646fa831f1c824388b5b30574/README.md#L116-L123)
  - [observation/documented] Interactive sessions support slash commands such as /models, /byok, /websearch, and /skills subcommands (list, link, enable, disable, reload). -- evidence: [README.md#L60-L60](https://github.com/haseeb-heaven/open-agent/blob/575401684ec13df646fa831f1c824388b5b30574/README.md#L60-L60), [docs/cli/skills.md#L92-L99](https://github.com/haseeb-heaven/open-agent/blob/575401684ec13df646fa831f1c824388b5b30574/docs/cli/skills.md#L92-L99)
- memory-state (1 claim(s)):
More evidence: [full detail](open-agent.detail.md)

Metadata and full claim list: [full detail](open-agent.detail.md)
Human notes ([notes](open-agent.notes.md), never overwritten by build)

[Back to map index](../../index.md)
