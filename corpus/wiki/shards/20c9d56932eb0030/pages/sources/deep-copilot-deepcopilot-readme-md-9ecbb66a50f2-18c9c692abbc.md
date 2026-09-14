---
access: public
aliases: []
claim_ids:
- clm_0ae3432a0c5dffce177156c0b7f3ad0592df5d5f5cf37cd16b05b05e9687e706
- clm_146df6cec41291018df820854b62505b4b6ba2ff1453c7a394e9a653a72e9560
- clm_2266a2f451a2bc4e1ee8258155d081f250af9563c3e71780956edaf09ff26f92
- clm_576f109aebffc514187e71f1f4576d4574a5e6f2ae2b81774fed3f1981f54ee3
- clm_5e43133a9ad3fcd29c3fc38999fc15db2db757186313cdf63d6d2f296679ef36
- clm_7320e30a4594015d5b870f05f38ddb5f33151f76c3b49a4397cefad506f7dc26
- clm_7a697b29e33d57d738028fb6c809bf1eb56f864553dc016c8a6cddf6df93f6d9
- clm_7accfde7e7cc5b854763c94739b9a6bc0acc8e26525418e919fc13f3df6222cd
- clm_969af00f69e57b7c54012a599bc7aff9539d4b48bb01eed0855d791c90231a79
- clm_aba53ea8d94f2c20ca7aff75ea278708aa3bb8d609126e68355d0012c2fb5682
- clm_acd68e7bfdde61db57c9c7cf0d0bf8928cd0bc9bfc28af3120cfca29688d7343
- clm_adce63a41aa6f2816fb5edb0401eaa628387e6eee133239224aa6724786af5f5
- clm_b729167333db46a9899fb7278b20ce8bfe65bed166e993facc0d362435cf26bc
- clm_ce9dc31e81909fe9bd85f8d722f955113730994e56b997d14aed3db8b17f030a
- clm_f76b3c04d0b31ee8317e04d05c453745be9f352c4a9785a459d2474976f31cc1
- clm_ffc500fd6f8ee21fb67384a4827e71b2624ca3953d7fe73d67978585e21bb8c8
maturity: draft
page_id: pg_5267cd6e77885291a3c218c9c692abbc
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_2d3ac89f7cf45fd48910b31d035aa52e
title: deep-copilot/DeepCopilot/README.md @ 9ecbb66a50f2
updated_at: '2026-09-14T02:00:32Z'
---

# deep-copilot/DeepCopilot/README.md @ 9ecbb66a50f2

<!-- rcw:begin owner=source:src_2d3ac89f7cf45fd48910b31d035aa52e block=evidence -->
- Chat history is persisted via VS Code globalState, and a per-session run map lets users switch sessions while a task runs, with buffered events replayed on return. [@claim:clm_0ae3432a0c5dffce177156c0b7f3ad0592df5d5f5cf37cd16b05b05e9687e706]
- Architecture places everything in the VS Code extension host: extension.js entry, a ChatViewProvider with a webview message bus and per-session run map, a DeepSeek SSE API client, and a tools module with schema and exec files. [@claim:clm_146df6cec41291018df820854b62505b4b6ba2ff1453c7a394e9a653a72e9560]
- The extension adds a sidebar chat panel opened via a whale icon in the activity bar, with a key button in the panel's bottom-right for entering API keys. [@claim:clm_2266a2f451a2bc4e1ee8258155d081f250af9563c3e71780956edaf09ff26f92]
- Documented keybindings include Ctrl/Cmd+Shift+D to open the sidebar, Enter to send, Esc to stop generation, and arrow keys to recall prompt history. [@claim:clm_576f109aebffc514187e71f1f4576d4574a5e6f2ae2b81774fed3f1981f54ee3]
- Repository development practice: the project uses plain JavaScript (no TypeScript), no runtime dependencies, and the webview communicates only via postMessage without importing vscode. [@claim:clm_5e43133a9ad3fcd29c3fc38999fc15db2db757186313cdf63d6d2f296679ef36]
- Approval is enforced in the extension itself, not just the UI: a model-issued write_file will not execute unless policy or the user allows it. [@claim:clm_7320e30a4594015d5b870f05f38ddb5f33151f76c3b49a4397cefad506f7dc26]
- External MCP stdio tool servers can be configured via deepseekAgent.mcp.servers, with their tools exposed as mcp__<server>__<toolName> alongside built-ins. [@claim:clm_7a697b29e33d57d738028fb6c809bf1eb56f864553dc016c8a6cddf6df93f6d9]
- A spawn_agent tool launches isolated sub-agents with their own context, and multiple sub-agent calls in one turn execute in parallel. [@claim:clm_7accfde7e7cc5b854763c94739b9a6bc0acc8e26525418e919fc13f3df6222cd]
- The extension has no runtime npm dependencies, relying on the VS Code Extension API and Node.js built-ins, with no additional service deployment required. [@claim:clm_969af00f69e57b7c54012a599bc7aff9539d4b48bb01eed0855d791c90231a79]
- Typing '#' in the chat input opens a context-reference picker supporting #file, #selection, #problems, #changes, #terminal, #symbol and #fetch references injected as attachment blocks. [@claim:clm_aba53ea8d94f2c20ca7aff75ea278708aa3bb8d609126e68355d0012c2fb5682]
- No agent performance benchmarks or evaluation harness appear in the provided evidence; the only test-related mention is a user-configurable post-tool hook that can run npm test, so evaluation capability is undocumented. [@claim:clm_acd68e7bfdde61db57c9c7cf0d0bf8928cd0bc9bfc28af3120cfca29688d7343]
- Skills are discovered from ~/.deepcopilot/skills, ~/.claude/skills and ~/.copilot/skills with YAML metadata, invoked via a skill_invoke tool or a /skill slash command. [@claim:clm_adce63a41aa6f2816fb5edb0401eaa628387e6eee133239224aa6724786af5f5]
- Tool-call approval has four modes: manual (default, prompts every write/shell), auto-edit, autopilot (auto-approve all, trusted workspaces only), and readonly. [@claim:clm_b729167333db46a9899fb7278b20ce8bfe65bed166e993facc0d362435cf26bc]
- The tool set exposed to the model is deliberately minimal, including file read/write/replace, apply_patch, directory listing, glob and ripgrep-style search, shell execution, web search, plan updates, and revert_last_turn. [@claim:clm_ce9dc31e81909fe9bd85f8d722f955113730994e56b997d14aed3db8b17f030a]
- A ~/.deepcopilot/memory.md file of cross-project preferences is injected into every system prompt, capped at 4 KB. [@claim:clm_f76b3c04d0b31ee8317e04d05c453745be9f352c4a9785a459d2474976f31cc1]
- A DEEPCOPILOT.md file at the workspace root is injected into the system prompt for every request in that workspace, for project conventions and do/don't rules. [@claim:clm_ffc500fd6f8ee21fb67384a4827e71b2624ca3953d7fe73d67978585e21bb8c8]
<!-- rcw:end owner=source:src_2d3ac89f7cf45fd48910b31d035aa52e block=evidence -->

## Researcher notes

