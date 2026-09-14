# jondot/picocode

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 064a2a6eaa18 @ 850b47d6cc5a3e69

## Summary (orientation draft, not independently verified)

picocode is a small Rust-based coding agent CLI supporting multiple LLM providers, personas, recipes, and a tool set, per its README. Evidence is documentation-only; no code slices are present.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] picocode is described as a minimal, high-performance coding agent written in Rust, shipped as a single compact binary. -- evidence: [README.md#L39-L44](https://github.com/jondot/picocode/blob/064a2a6eaa18bd0fd28b2fcb64216754b4e848b3/README.md#L39-L44), [README.md#L10-L10](https://github.com/jondot/picocode/blob/064a2a6eaa18bd0fd28b2fcb64216754b4e848b3/README.md#L10-L10)
- components (1 claim(s)):
  - [observation/documented] The agent exposes filesystem tools (read/write/edit/list/make/remove/move/copy), grep_text, glob_files, a bash tool, and an optional agent_browser for web automation. -- evidence: [README.md#L115-L118](https://github.com/jondot/picocode/blob/064a2a6eaa18bd0fd28b2fcb64216754b4e848b3/README.md#L115-L118)
- design-choices (2 claim(s)):
  - [observation/documented] Users can switch expert personas (e.g., architect, security, zen) via --persona to change how the agent thinks and speaks. -- evidence: [README.md#L50-L64](https://github.com/jondot/picocode/blob/064a2a6eaa18bd0fd28b2fcb64216754b4e848b3/README.md#L50-L64), [README.md#L48-L48](https://github.com/jondot/picocode/blob/064a2a6eaa18bd0fd28b2fcb64216754b4e848b3/README.md#L48-L48), [README.md#L39-L44](https://github.com/jondot/picocode/blob/064a2a6eaa18bd0fd28b2fcb64216754b4e848b3/README.md#L39-L44)
  - [observation/documented] A local AGENTS.md file can supply the agent with custom codebase-specific instructions. -- evidence: [README.md#L66-L67](https://github.com/jondot/picocode/blob/064a2a6eaa18bd0fd28b2fcb64216754b4e848b3/README.md#L66-L67)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: hacking on picocode requires Rust (latest stable) and a provider API key; new tools are added in src/tools.rs with #[rig_tool] and registered in src/agent.rs's build_rig_agent. -- evidence: [README.md#L126-L127](https://github.com/jondot/picocode/blob/064a2a6eaa18bd0fd28b2fcb64216754b4e848b3/README.md#L126-L127), [README.md#L142-L144](https://github.com/jondot/picocode/blob/064a2a6eaa18bd0fd28b2fcb64216754b4e848b3/README.md#L142-L144), [README.md#L122-L122](https://github.com/jondot/picocode/blob/064a2a6eaa18bd0fd28b2fcb64216754b4e848b3/README.md#L122-L122)
  - [observation/documented] Repository development practice: local development uses git clone followed by cargo run to build and execute the agent. -- evidence: [README.md#L137-L138](https://github.com/jondot/picocode/blob/064a2a6eaa18bd0fd28b2fcb64216754b4e848b3/README.md#L137-L138), [README.md#L133-L134](https://github.com/jondot/picocode/blob/064a2a6eaa18bd0fd28b2fcb64216754b4e848b3/README.md#L133-L134)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (4 claim(s)):
  - [observation/documented] The CLI offers interactive chat (default), single-prompt mode, and a recipe subcommand that runs named tasks from picocode.yaml. -- evidence: [README.md#L98-L100](https://github.com/jondot/picocode/blob/064a2a6eaa18bd0fd28b2fcb64216754b4e848b3/README.md#L98-L100), [README.md#L71-L71](https://github.com/jondot/picocode/blob/064a2a6eaa18bd0fd28b2fcb64216754b4e848b3/README.md#L71-L71)
  - [observation/documented] Flags include --provider, --model, --yolo to disable confirmations, --quiet for piping, --persona, and --tool-call-limit with a default of 50. -- evidence: [README.md#L104-L109](https://github.com/jondot/picocode/blob/064a2a6eaa18bd0fd28b2fcb64216754b4e848b3/README.md#L104-L109)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
  - [observation/documented] Destructive actions such as deleting files or running shell commands require manual confirmation by default; --yolo disables all confirmation prompts. -- evidence: [README.md#L39-L44](https://github.com/jondot/picocode/blob/064a2a6eaa18bd0fd28b2fcb64216754b4e848b3/README.md#L39-L44), [README.md#L104-L109](https://github.com/jondot/picocode/blob/064a2a6eaa18bd0fd28b2fcb64216754b4e848b3/README.md#L104-L109)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] Multi-provider LLM support (Anthropic, OpenAI, DeepSeek, Google, Ollama, and others) is provided via the Rig library. -- evidence: [README.md#L39-L44](https://github.com/jondot/picocode/blob/064a2a6eaa18bd0fd28b2fcb64216754b4e848b3/README.md#L39-L44), [README.md#L122-L122](https://github.com/jondot/picocode/blob/064a2a6eaa18bd0fd28b2fcb64216754b4e848b3/README.md#L122-L122)
- limitations: unknown (no source-linked claim submitted for this facet)
- relevance: unknown (no source-linked claim submitted for this facet)

(2 additional claim(s) omitted for length; see [full detail](picocode.detail.md) for every claim.)

Metadata and full claim list: [full detail](picocode.detail.md)
Human notes ([notes](picocode.notes.md), never overwritten by build)

[Back to map index](../../index.md)
