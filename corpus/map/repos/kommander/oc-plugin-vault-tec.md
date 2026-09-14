# kommander/oc-plugin-vault-tec

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit a0184713d037 @ 1506c8a77987616d

## Summary (orientation draft, not independently verified)

The snapshot documents an OpenCode plugin that installs a Vault-Tec/RobCo-themed personality prompt and TUI theming, installable via CLI or in-app command, with configurable server and TUI options. The prompt file defines the persona, tone directives, Fallout lore knowledge base, and formatting rules such as a no-emoji policy.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] The plugin is described as a Vault-Tec personality matrix that turns the coding terminal into a pre-War RobCo engineering assistant, including 122 vault experiment dossiers. -- evidence: [README.md#L3-L3](https://github.com/kommander/oc-plugin-vault-tec/blob/a0184713d03795e641d1aae9b6d66f1a76cd9afc/README.md#L3-L3)
- components (3 claim(s)):
  - [observation/documented] Server-side options include enabled (default true), mode with append/replace values (default append), and an optional prompt override string. -- evidence: [README.md#L27-L29](https://github.com/kommander/oc-plugin-vault-tec/blob/a0184713d03795e641d1aae9b6d66f1a76cd9afc/README.md#L27-L29)
  - [observation/documented] TUI options cover enabled, theme (default 'vault-tec'), set_theme, scanlines, vignette (default 0.75), sidebar, and tips, all defaulting to true except vignette. -- evidence: [README.md#L33-L39](https://github.com/kommander/oc-plugin-vault-tec/blob/a0184713d03795e641d1aae9b6d66f1a76cd9afc/README.md#L33-L39)
- design-choices (3 claim(s)):
  - [observation/documented] Operating parameters state that engineering competency always takes priority: Vault-Tec communication standards never supersede engineering accuracy, and the agent should use all available tools to complete tasks. -- evidence: [prompt.txt#L155-L160](https://github.com/kommander/oc-plugin-vault-tec/blob/a0184713d03795e641d1aae9b6d66f1a76cd9afc/prompt.txt#L155-L160), [prompt.txt#L181-L181](https://github.com/kommander/oc-plugin-vault-tec/blob/a0184713d03795e641d1aae9b6d66f1a76cd9afc/prompt.txt#L181-L181)
  - [observation/documented] Responses should be formatted as terminal output with status lines like '[VT-OS] STATUS: OPERATIONAL', '>' prefixes, [WARNING]/[CAUTION] blocks, and terminal-style sign-offs. -- evidence: [prompt.txt#L162-L167](https://github.com/kommander/oc-plugin-vault-tec/blob/a0184713d03795e641d1aae9b6d66f1a76cd9afc/prompt.txt#L162-L167)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns (2 claim(s)):
  - [observation/documented] The prompt instructs the agent to speak as a pre-War Vault-Tec corporate terminal with 1950s atomic-age optimism, retro slogans, and themed jargon for bugs, errors, builds, tests, and deployments. -- evidence: [prompt.txt#L23-L39](https://github.com/kommander/oc-plugin-vault-tec/blob/a0184713d03795e641d1aae9b6d66f1a76cd9afc/prompt.txt#L23-L39)
  - [observation/documented] The prompt embeds a large Fallout lore knowledge base: corporate history, Project Safehouse, vault architecture, notable vault experiments, UOS, Pip-Boy, key technologies, factions, and pre/post-war world history. -- evidence: [prompt.txt#L63-L95](https://github.com/kommander/oc-plugin-vault-tec/blob/a0184713d03795e641d1aae9b6d66f1a76cd9afc/prompt.txt#L63-L95), [prompt.txt#L98-L104](https://github.com/kommander/oc-plugin-vault-tec/blob/a0184713d03795e641d1aae9b6d66f1a76cd9afc/prompt.txt#L98-L104), [prompt.txt#L135-L145](https://github.com/kommander/oc-plugin-vault-tec/blob/a0184713d03795e641d1aae9b6d66f1a76cd9afc/prompt.txt#L135-L145), [prompt.txt#L110-L119](https://github.com/kommander/oc-plugin-vault-tec/blob/a0184713d03795e641d1aae9b6d66f1a76cd9afc/prompt.txt#L110-L119), [prompt.txt#L122-L132](https://github.com/kommander/oc-plugin-vault-tec/blob/a0184713d03795e641d1aae9b6d66f1a76cd9afc/prompt.txt#L122-L132), [prompt.txt#L45-L45](https://github.com/kommander/oc-plugin-vault-tec/blob/a0184713d03795e641d1aae9b6d66f1a76cd9afc/prompt.txt#L45-L45), [prompt.txt#L52-L52](https://github.com/kommander/oc-plugin-vault-tec/blob/a0184713d03795e641d1aae9b6d66f1a76cd9afc/prompt.txt#L52-L52)
- interfaces (2 claim(s)):
  - [observation/documented] Installation is supported via the CLI command 'opencode plugin oc-plugin-vault-tec' or through OpenCode's Ctrl+P 'Install Plugin' flow. -- evidence: [README.md#L17-L19](https://github.com/kommander/oc-plugin-vault-tec/blob/a0184713d03795e641d1aae9b6d66f1a76cd9afc/README.md#L17-L19), [README.md#L11-L13](https://github.com/kommander/oc-plugin-vault-tec/blob/a0184713d03795e641d1aae9b6d66f1a76cd9afc/README.md#L11-L13)
  - [observation/documented] Plugin options are configured through the opencode.json and tui.json config files. -- evidence: [README.md#L23-L23](https://github.com/kommander/oc-plugin-vault-tec/blob/a0184713d03795e641d1aae9b6d66f1a76cd9afc/README.md#L23-L23)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies: unknown (no source-linked claim submitted for this facet)
- limitations: unknown (no source-linked claim submitted for this facet)
- relevance (1 claim(s)):
More evidence: [full detail](oc-plugin-vault-tec.detail.md)

Metadata and full claim list: [full detail](oc-plugin-vault-tec.detail.md)
Human notes ([notes](oc-plugin-vault-tec.notes.md), never overwritten by build)

[Back to map index](../../index.md)
