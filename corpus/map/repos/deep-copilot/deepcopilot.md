# deep-copilot/deepcopilot

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 9ecbb66a50f2 @ a7bd145c95c3ea30

## Summary (orientation draft, not independently verified)

Selected evidence records: The extension adds a sidebar chat panel opened via a whale icon in the activity bar, with a key button in the panel's bottom-right for entering API keys. Documented keybindings include Ctrl/Cmd+Shift+D to open the sidebar, Enter to send, Esc to stop generation, and arrow keys to recall prompt history.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 16 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

16 claim(s) across 10 facet(s); 3 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] Architecture places everything in the VS Code extension host: extension.js entry, a ChatViewProvider with a webview message bus and per-session run map, a DeepSeek SSE API client, and a tools module with schema and exec files. -- evidence: [README.md#L278-L317](https://github.com/deep-copilot/DeepCopilot/blob/9ecbb66a50f211dfc01a44e85e327719495b4e95/README.md#L278-L317)
- design-choices (2 claim(s)):
  - [observation/documented] The tool set exposed to the model is deliberately minimal, including file read/write/replace, apply_patch, directory listing, glob and ripgrep-style search, shell execution, web search, plan updates, and revert_last_turn. -- evidence: [README.md#L251-L252](https://github.com/deep-copilot/DeepCopilot/blob/9ecbb66a50f211dfc01a44e85e327719495b4e95/README.md#L251-L252), [README.md#L254-L268](https://github.com/deep-copilot/DeepCopilot/blob/9ecbb66a50f211dfc01a44e85e327719495b4e95/README.md#L254-L268)
  - [observation/documented] A DEEPCOPILOT.md file at the workspace root is injected into the system prompt for every request in that workspace, for project conventions and do/don't rules. -- evidence: [README.md#L417-L417](https://github.com/deep-copilot/DeepCopilot/blob/9ecbb66a50f211dfc01a44e85e327719495b4e95/README.md#L417-L417), [README.md#L415-L415](https://github.com/deep-copilot/DeepCopilot/blob/9ecbb66a50f211dfc01a44e85e327719495b4e95/README.md#L415-L415)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: the project uses plain JavaScript (no TypeScript), no runtime dependencies, and the webview communicates only via postMessage without importing vscode. -- evidence: [README.md#L456-L461](https://github.com/deep-copilot/DeepCopilot/blob/9ecbb66a50f211dfc01a44e85e327719495b4e95/README.md#L456-L461)
- skills-patterns (1 claim(s)):
  - [observation/documented] Skills are discovered from ~/.deepcopilot/skills, ~/.claude/skills and ~/.copilot/skills with YAML metadata, invoked via a skill_invoke tool or a /skill slash command. -- evidence: [README.md#L513-L514](https://github.com/deep-copilot/DeepCopilot/blob/9ecbb66a50f211dfc01a44e85e327719495b4e95/README.md#L513-L514), [README.md#L587-L594](https://github.com/deep-copilot/DeepCopilot/blob/9ecbb66a50f211dfc01a44e85e327719495b4e95/README.md#L587-L594)
- interfaces (4 claim(s)):
  - [observation/documented] The extension adds a sidebar chat panel opened via a whale icon in the activity bar, with a key button in the panel's bottom-right for entering API keys. -- evidence: [README.md#L38-L41](https://github.com/deep-copilot/DeepCopilot/blob/9ecbb66a50f211dfc01a44e85e327719495b4e95/README.md#L38-L41), [README.md#L130-L132](https://github.com/deep-copilot/DeepCopilot/blob/9ecbb66a50f211dfc01a44e85e327719495b4e95/README.md#L130-L132), [README.md#L43-L46](https://github.com/deep-copilot/DeepCopilot/blob/9ecbb66a50f211dfc01a44e85e327719495b4e95/README.md#L43-L46)
  - [observation/documented] Documented keybindings include Ctrl/Cmd+Shift+D to open the sidebar, Enter to send, Esc to stop generation, and arrow keys to recall prompt history. -- evidence: [README.md#L235-L245](https://github.com/deep-copilot/DeepCopilot/blob/9ecbb66a50f211dfc01a44e85e327719495b4e95/README.md#L235-L245)
- memory-state (2 claim(s)):
  - [observation/documented] A ~/.deepcopilot/memory.md file of cross-project preferences is injected into every system prompt, capped at 4 KB. -- evidence: [README.md#L421-L421](https://github.com/deep-copilot/DeepCopilot/blob/9ecbb66a50f211dfc01a44e85e327719495b4e95/README.md#L421-L421), [README.md#L423-L423](https://github.com/deep-copilot/DeepCopilot/blob/9ecbb66a50f211dfc01a44e85e327719495b4e95/README.md#L423-L423), [README.md#L613-L622](https://github.com/deep-copilot/DeepCopilot/blob/9ecbb66a50f211dfc01a44e85e327719495b4e95/README.md#L613-L622)
  - [observation/documented] Chat history is persisted via VS Code globalState, and a per-session run map lets users switch sessions while a task runs, with buffered events replayed on return. -- evidence: [README.md#L278-L317](https://github.com/deep-copilot/DeepCopilot/blob/9ecbb66a50f211dfc01a44e85e327719495b4e95/README.md#L278-L317), [README.md#L321-L330](https://github.com/deep-copilot/DeepCopilot/blob/9ecbb66a50f211dfc01a44e85e327719495b4e95/README.md#L321-L330)
- orchestration (1 claim(s)):
  - [observation/documented] A spawn_agent tool launches isolated sub-agents with their own context, and multiple sub-agent calls in one turn execute in parallel. -- evidence: [README.md#L569-L574](https://github.com/deep-copilot/DeepCopilot/blob/9ecbb66a50f211dfc01a44e85e327719495b4e95/README.md#L569-L574)
- tools-permissions (2 claim(s)):
More evidence: [full detail](deepcopilot.detail.md)

Metadata and full claim list: [full detail](deepcopilot.detail.md)
Human notes ([notes](deepcopilot.notes.md), never overwritten by build)

[Back to map index](../../index.md)
