# deep-copilot/deepcopilot -- full detail

[Back to orientation](deepcopilot.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/deep-copilot/deepcopilot/9ecbb66a50f211dfc01a44e85e327719495b4e95/a7bd145c95c3ea30.json](../../../wiki/dossiers/deep-copilot/deepcopilot/9ecbb66a50f211dfc01a44e85e327719495b4e95/a7bd145c95c3ea30.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] Architecture places everything in the VS Code extension host: extension.js entry, a ChatViewProvider with a webview message bus and per-session run map, a DeepSeek SSE API client, and a tools module with schema and exec files. -- evidence: [README.md#L278-L317](https://github.com/deep-copilot/DeepCopilot/blob/9ecbb66a50f211dfc01a44e85e327719495b4e95/README.md#L278-L317) (`clm_146df6cec41291018df820854b62505b4b6ba2ff1453c7a394e9a653a72e9560`)

## design-choices (2 claim(s))

- [observation/documented] The tool set exposed to the model is deliberately minimal, including file read/write/replace, apply_patch, directory listing, glob and ripgrep-style search, shell execution, web search, plan updates, and revert_last_turn. -- evidence: [README.md#L251-L252](https://github.com/deep-copilot/DeepCopilot/blob/9ecbb66a50f211dfc01a44e85e327719495b4e95/README.md#L251-L252), [README.md#L254-L268](https://github.com/deep-copilot/DeepCopilot/blob/9ecbb66a50f211dfc01a44e85e327719495b4e95/README.md#L254-L268) (`clm_ce9dc31e81909fe9bd85f8d722f955113730994e56b997d14aed3db8b17f030a`)
- [observation/documented] A DEEPCOPILOT.md file at the workspace root is injected into the system prompt for every request in that workspace, for project conventions and do/don't rules. -- evidence: [README.md#L417-L417](https://github.com/deep-copilot/DeepCopilot/blob/9ecbb66a50f211dfc01a44e85e327719495b4e95/README.md#L417-L417), [README.md#L415-L415](https://github.com/deep-copilot/DeepCopilot/blob/9ecbb66a50f211dfc01a44e85e327719495b4e95/README.md#L415-L415) (`clm_ffc500fd6f8ee21fb67384a4827e71b2624ca3953d7fe73d67978585e21bb8c8`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: the project uses plain JavaScript (no TypeScript), no runtime dependencies, and the webview communicates only via postMessage without importing vscode. -- evidence: [README.md#L456-L461](https://github.com/deep-copilot/DeepCopilot/blob/9ecbb66a50f211dfc01a44e85e327719495b4e95/README.md#L456-L461) (`clm_5e43133a9ad3fcd29c3fc38999fc15db2db757186313cdf63d6d2f296679ef36`)

## skills-patterns (1 claim(s))

- [observation/documented] Skills are discovered from ~/.deepcopilot/skills, ~/.claude/skills and ~/.copilot/skills with YAML metadata, invoked via a skill_invoke tool or a /skill slash command. -- evidence: [README.md#L513-L514](https://github.com/deep-copilot/DeepCopilot/blob/9ecbb66a50f211dfc01a44e85e327719495b4e95/README.md#L513-L514), [README.md#L587-L594](https://github.com/deep-copilot/DeepCopilot/blob/9ecbb66a50f211dfc01a44e85e327719495b4e95/README.md#L587-L594) (`clm_adce63a41aa6f2816fb5edb0401eaa628387e6eee133239224aa6724786af5f5`)

## interfaces (4 claim(s))

- [observation/documented] The extension adds a sidebar chat panel opened via a whale icon in the activity bar, with a key button in the panel's bottom-right for entering API keys. -- evidence: [README.md#L38-L41](https://github.com/deep-copilot/DeepCopilot/blob/9ecbb66a50f211dfc01a44e85e327719495b4e95/README.md#L38-L41), [README.md#L130-L132](https://github.com/deep-copilot/DeepCopilot/blob/9ecbb66a50f211dfc01a44e85e327719495b4e95/README.md#L130-L132), [README.md#L43-L46](https://github.com/deep-copilot/DeepCopilot/blob/9ecbb66a50f211dfc01a44e85e327719495b4e95/README.md#L43-L46) (`clm_2266a2f451a2bc4e1ee8258155d081f250af9563c3e71780956edaf09ff26f92`)
- [observation/documented] Documented keybindings include Ctrl/Cmd+Shift+D to open the sidebar, Enter to send, Esc to stop generation, and arrow keys to recall prompt history. -- evidence: [README.md#L235-L245](https://github.com/deep-copilot/DeepCopilot/blob/9ecbb66a50f211dfc01a44e85e327719495b4e95/README.md#L235-L245) (`clm_576f109aebffc514187e71f1f4576d4574a5e6f2ae2b81774fed3f1981f54ee3`)
- [observation/documented] Typing '#' in the chat input opens a context-reference picker supporting #file, #selection, #problems, #changes, #terminal, #symbol and #fetch references injected as attachment blocks. -- evidence: [README.md#L518-L519](https://github.com/deep-copilot/DeepCopilot/blob/9ecbb66a50f211dfc01a44e85e327719495b4e95/README.md#L518-L519) (`clm_aba53ea8d94f2c20ca7aff75ea278708aa3bb8d609126e68355d0012c2fb5682`)
- [observation/documented] External MCP stdio tool servers can be configured via deepseekAgent.mcp.servers, with their tools exposed as mcp__<server>__<toolName> alongside built-ins. -- evidence: [README.md#L435-L435](https://github.com/deep-copilot/DeepCopilot/blob/9ecbb66a50f211dfc01a44e85e327719495b4e95/README.md#L435-L435), [README.md#L429-L433](https://github.com/deep-copilot/DeepCopilot/blob/9ecbb66a50f211dfc01a44e85e327719495b4e95/README.md#L429-L433), [README.md#L437-L437](https://github.com/deep-copilot/DeepCopilot/blob/9ecbb66a50f211dfc01a44e85e327719495b4e95/README.md#L437-L437), [README.md#L613-L622](https://github.com/deep-copilot/DeepCopilot/blob/9ecbb66a50f211dfc01a44e85e327719495b4e95/README.md#L613-L622) (`clm_7a697b29e33d57d738028fb6c809bf1eb56f864553dc016c8a6cddf6df93f6d9`)

## memory-state (2 claim(s))

- [observation/documented] A ~/.deepcopilot/memory.md file of cross-project preferences is injected into every system prompt, capped at 4 KB. -- evidence: [README.md#L421-L421](https://github.com/deep-copilot/DeepCopilot/blob/9ecbb66a50f211dfc01a44e85e327719495b4e95/README.md#L421-L421), [README.md#L423-L423](https://github.com/deep-copilot/DeepCopilot/blob/9ecbb66a50f211dfc01a44e85e327719495b4e95/README.md#L423-L423), [README.md#L613-L622](https://github.com/deep-copilot/DeepCopilot/blob/9ecbb66a50f211dfc01a44e85e327719495b4e95/README.md#L613-L622) (`clm_f76b3c04d0b31ee8317e04d05c453745be9f352c4a9785a459d2474976f31cc1`)
- [observation/documented] Chat history is persisted via VS Code globalState, and a per-session run map lets users switch sessions while a task runs, with buffered events replayed on return. -- evidence: [README.md#L278-L317](https://github.com/deep-copilot/DeepCopilot/blob/9ecbb66a50f211dfc01a44e85e327719495b4e95/README.md#L278-L317), [README.md#L321-L330](https://github.com/deep-copilot/DeepCopilot/blob/9ecbb66a50f211dfc01a44e85e327719495b4e95/README.md#L321-L330) (`clm_0ae3432a0c5dffce177156c0b7f3ad0592df5d5f5cf37cd16b05b05e9687e706`)

## orchestration (1 claim(s))

- [observation/documented] A spawn_agent tool launches isolated sub-agents with their own context, and multiple sub-agent calls in one turn execute in parallel. -- evidence: [README.md#L569-L574](https://github.com/deep-copilot/DeepCopilot/blob/9ecbb66a50f211dfc01a44e85e327719495b4e95/README.md#L569-L574) (`clm_7accfde7e7cc5b854763c94739b9a6bc0acc8e26525418e919fc13f3df6222cd`)

## tools-permissions (2 claim(s))

- [observation/documented] Tool-call approval has four modes: manual (default, prompts every write/shell), auto-edit, autopilot (auto-approve all, trusted workspaces only), and readonly. -- evidence: [README.md#L222-L227](https://github.com/deep-copilot/DeepCopilot/blob/9ecbb66a50f211dfc01a44e85e327719495b4e95/README.md#L222-L227) (`clm_b729167333db46a9899fb7278b20ce8bfe65bed166e993facc0d362435cf26bc`)
- [observation/documented] Approval is enforced in the extension itself, not just the UI: a model-issued write_file will not execute unless policy or the user allows it. -- evidence: [README.md#L321-L330](https://github.com/deep-copilot/DeepCopilot/blob/9ecbb66a50f211dfc01a44e85e327719495b4e95/README.md#L321-L330) (`clm_7320e30a4594015d5b870f05f38ddb5f33151f76c3b49a4397cefad506f7dc26`)

## evaluation (1 claim(s))

- [inference/documented] No agent performance benchmarks or evaluation harness appear in the provided evidence; the only test-related mention is a user-configurable post-tool hook that can run npm test, so evaluation capability is undocumented. -- evidence: [README.md#L443-L448](https://github.com/deep-copilot/DeepCopilot/blob/9ecbb66a50f211dfc01a44e85e327719495b4e95/README.md#L443-L448), [README.md#L450-L450](https://github.com/deep-copilot/DeepCopilot/blob/9ecbb66a50f211dfc01a44e85e327719495b4e95/README.md#L450-L450) (`clm_acd68e7bfdde61db57c9c7cf0d0bf8928cd0bc9bfc28af3120cfca29688d7343`)

## dependencies (1 claim(s))

- [observation/documented] The extension has no runtime npm dependencies, relying on the VS Code Extension API and Node.js built-ins, with no additional service deployment required. -- evidence: [README.md#L20-L22](https://github.com/deep-copilot/DeepCopilot/blob/9ecbb66a50f211dfc01a44e85e327719495b4e95/README.md#L20-L22), [README.md#L456-L461](https://github.com/deep-copilot/DeepCopilot/blob/9ecbb66a50f211dfc01a44e85e327719495b4e95/README.md#L456-L461) (`clm_969af00f69e57b7c54012a599bc7aff9539d4b48bb01eed0855d791c90231a79`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

