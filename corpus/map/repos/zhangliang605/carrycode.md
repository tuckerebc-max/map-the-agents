# zhangliang605/carrycode

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 090431f9651f @ 53270305d1f756d7

## Summary (orientation draft, not independently verified)

The snapshot consists only of README documentation (English and Chinese) for CarryCode, a terminal-native AI coding agent. Claims below are documentation-based descriptions of the product's advertised features, CLI, configuration, and contributor build instructions.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] Configuration lives in ~/.carry/carrycode.json (provider credentials and preferences) and ~/.carry/carrycode-runtime.json (language, default model, theme), with paths overridable via CARRYCODE_CONFIG_DIR or CARRYCODE_CONFIG_FILE. -- evidence: [README.md#L219-L223](https://github.com/zhangliang605/carrycode/blob/090431f9651fdf4bec87ee4b7a028364e031b725/README.md#L219-L223), [README.md#L225-L225](https://github.com/zhangliang605/carrycode/blob/090431f9651fdf4bec87ee4b7a028364e031b725/README.md#L225-L225)
- design-choices (1 claim(s)):
  - [observation/documented] The agent has two modes: Build mode for autonomous code generation and editing, and Plan mode for read-only analysis and planning. -- evidence: [README.md#L46-L62](https://github.com/zhangliang605/carrycode/blob/090431f9651fdf4bec87ee4b7a028364e031b725/README.md#L46-L62)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: building from source requires Rust (latest stable), Node.js v18+, Bun, and OS build tools; contributors use bun install, bun run build (or build:rust / build:ts), bun run dev, and bun run clean, producing ./target/index.js and a native Rust .node module. -- evidence: [README.md#L130-L130](https://github.com/zhangliang605/carrycode/blob/090431f9651fdf4bec87ee4b7a028364e031b725/README.md#L130-L130), [README.md#L118-L124](https://github.com/zhangliang605/carrycode/blob/090431f9651fdf4bec87ee4b7a028364e031b725/README.md#L118-L124), [README.md#L140-L141](https://github.com/zhangliang605/carrycode/blob/090431f9651fdf4bec87ee4b7a028364e031b725/README.md#L140-L141), [README.md#L133-L133](https://github.com/zhangliang605/carrycode/blob/090431f9651fdf4bec87ee4b7a028364e031b725/README.md#L133-L133), [README.md#L145-L147](https://github.com/zhangliang605/carrycode/blob/090431f9651fdf4bec87ee4b7a028364e031b725/README.md#L145-L147), [README.md#L136-L137](https://github.com/zhangliang605/carrycode/blob/090431f9651fdf4bec87ee4b7a028364e031b725/README.md#L136-L137), [README.md#L158-L161](https://github.com/zhangliang605/carrycode/blob/090431f9651fdf4bec87ee4b7a028364e031b725/README.md#L158-L161)
  - [observation/documented] Repository development practice: the recommended install path is a one-line script (curl ... install.sh | sudo sh on macOS/Linux, irm ... install.ps1 | iex on Windows) that auto-detects the platform, downloads the binary, verifies the checksum, and installs to /usr/local/bin. -- evidence: [README.md#L73-L74](https://github.com/zhangliang605/carrycode/blob/090431f9651fdf4bec87ee4b7a028364e031b725/README.md#L73-L74), [README.md#L76-L76](https://github.com/zhangliang605/carrycode/blob/090431f9651fdf4bec87ee4b7a028364e031b725/README.md#L76-L76), [README.md#L70-L70](https://github.com/zhangliang605/carrycode/blob/090431f9651fdf4bec87ee4b7a028364e031b725/README.md#L70-L70)
- skills-patterns (1 claim(s)):
  - [observation/documented] A skills system loads predefined or custom skills compatible with Claude Code, managed via /skill, with SkillHub integration to search Tencent SkillHub and install skills directly from results. -- evidence: [README.md#L25-L25](https://github.com/zhangliang605/carrycode/blob/090431f9651fdf4bec87ee4b7a028364e031b725/README.md#L25-L25), [README.md#L46-L62](https://github.com/zhangliang605/carrycode/blob/090431f9651fdf4bec87ee4b7a028364e031b725/README.md#L46-L62)
- interfaces (3 claim(s)):
  - [observation/documented] The CLI is invoked as 'carry'; it offers an interactive terminal UI mode plus a single-shot mode via 'carry --once "..."' with an optional --timeout-ms flag, suited to scripting and CI. -- evidence: [README.md#L96-L98](https://github.com/zhangliang605/carrycode/blob/090431f9651fdf4bec87ee4b7a028364e031b725/README.md#L96-L98), [README.md#L107-L107](https://github.com/zhangliang605/carrycode/blob/090431f9651fdf4bec87ee4b7a028364e031b725/README.md#L107-L107), [README.md#L109-L112](https://github.com/zhangliang605/carrycode/blob/090431f9651fdf4bec87ee4b7a028364e031b725/README.md#L109-L112)
  - [observation/documented] The interactive UI exposes slash commands including /model, /mcp, /skill, /rule, /theme, /language, /approval, /session, /compact, /update, and /exit. -- evidence: [README.md#L167-L179](https://github.com/zhangliang605/carrycode/blob/090431f9651fdf4bec87ee4b7a028364e031b725/README.md#L167-L179)
- memory-state (1 claim(s)):
  - [observation/documented] Sessions can be created, switched, and resumed with context persisting across conversations, and /compact compresses the current session context; long conversations are automatically compressed to fit token limits. -- evidence: [README.md#L167-L179](https://github.com/zhangliang605/carrycode/blob/090431f9651fdf4bec87ee4b7a028364e031b725/README.md#L167-L179), [README_CN.md#L44-L60](https://github.com/zhangliang605/carrycode/blob/090431f9651fdf4bec87ee4b7a028364e031b725/README_CN.md#L44-L60)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
  - [observation/documented] Approval modes control the agent's permissions at runtime: read-only, agent (read/write plus execution), and agent-full (unrestricted), selectable via /approval. -- evidence: [README.md#L167-L179](https://github.com/zhangliang605/carrycode/blob/090431f9651fdf4bec87ee4b7a028364e031b725/README.md#L167-L179), [README_CN.md#L44-L60](https://github.com/zhangliang605/carrycode/blob/090431f9651fdf4bec87ee4b7a028364e031b725/README_CN.md#L44-L60)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
More evidence: [full detail](carrycode.detail.md)

Metadata and full claim list: [full detail](carrycode.detail.md)
Human notes ([notes](carrycode.notes.md), never overwritten by build)

[Back to map index](../../index.md)
