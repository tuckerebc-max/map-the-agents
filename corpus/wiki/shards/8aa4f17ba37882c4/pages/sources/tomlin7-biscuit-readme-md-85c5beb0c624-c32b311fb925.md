---
access: public
aliases: []
claim_ids:
- clm_476218364a80222ce97f6907ae611b1ed01afc6d29028c4b04679d8b7e7bbbbb
- clm_60d844d9217015d89201914f2b57f8425aed37dc19e3ae40d2dac2bdb840784f
- clm_7878b95867aa8d35473f1c4398098296e09bf68f091a9a5123981356e6206d2e
- clm_a48fad887d5b6a96a1e3c123e1944612268a4ee01a7a69e669d2c725824cff28
- clm_aa3163a8490f476852ff672986d4e6275bc7987e82977a700d6ae98f1e9a808d
- clm_c9061fde8880895b165c7a61361b6ed8fa8119479150eb2af5c3420985095494
- clm_d1a3d8738564346186256a7d96adeab5c270a71c80fa7795ca0218e3684e0f42
- clm_ed00676f8acf685710ec605ca6658485b7af8ab3572b2f6c2593b90fd4496e14
- clm_f7fd5e4d88aba0ae25efcf4fa2f6fb07f088c8d9be136f5659657ffa211bbc8e
maturity: draft
page_id: pg_0fd5ad40b16457dba260c32b311fb925
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_a066be3d6e1e5368aa6aa09d35136b01
title: tomlin7/biscuit/README.md @ 85c5beb0c624
updated_at: '2026-09-14T03:19:52Z'
---

# tomlin7/biscuit/README.md @ 85c5beb0c624

<!-- rcw:begin owner=source:src_a066be3d6e1e5368aa6aa09d35136b01 block=evidence -->
- Repository development practice: contributors are directed to a contributing guide and docs for project structure and environment setup, and the project supports both Poetry and uv for dependency management. [@claim:clm_476218364a80222ce97f6907ae611b1ed01afc6d29028c4b04679d8b7e7bbbbb]
- Per the README checklist, full DAP client integration, vim mode support, LLM provider extension examples, and an ollama extension rewrite remain incomplete; the old ollama and several formatter extensions are deprecated. [@claim:clm_60d844d9217015d89201914f2b57f8425aed37dc19e3ae40d2dac2bdb840784f]
- Source control features include a split diff viewer, git operations (push, pull, commit, stage, unstage, branch switching), and repository cloning; GitHub issues/PR viewing is currently disabled pending conversion to an extension. [@claim:clm_7878b95867aa8d35473f1c4398098296e09bf68f091a9a5123981356e6206d2e]
- Biscuit is described as a fast, extensible native code editor with agents, under 20 MB in size, installable in seconds. [@claim:clm_a48fad887d5b6a96a1e3c123e1944612268a4ee01a7a69e669d2c725824cff28]
- The agent supports Gemini and Anthropic APIs (claude-4-5-opus/sonnet/haiku, gemini-2-5-flash/pro), file attachment for chat context, and additional LLM providers via extensions. [@claim:clm_aa3163a8490f476852ff672986d4e6275bc7987e82977a700d6ae98f1e9a808d]
- Code intelligence features tree-sitter parsing/highlights, completions, hover docs, symbol outline, symbol search, peek-to-definition, and references, with more language servers added via extensions. [@claim:clm_c9061fde8880895b165c7a61361b6ed8fa8119479150eb2af5c3420985095494]
- The built-in planning agent ships with eleven tools, including ReadFile, EditFile, DeleteFile, ListDir, GlobFileSearch, Grep, CodebaseSearch, RunTerminalCmd, TodoWrite, GetWorkspaceInfo, and GetActiveEditor. [@claim:clm_d1a3d8738564346186256a7d96adeab5c270a71c80fa7795ca0218e3684e0f42]
- Debugging includes breakpoints, runtime variable inspection and modification, call stack visualization, and a built-in Python debugger; additional debuggers can be registered via extensions. [@claim:clm_ed00676f8acf685710ec605ca6658485b7af8ab3572b2f6c2593b90fd4496e14]
- Search is ripgrep-based with regex and case-sensitivity support, individual or bulk replace, and a floating find-replace widget in open editors. [@claim:clm_f7fd5e4d88aba0ae25efcf4fa2f6fb07f088c8d9be136f5659657ffa211bbc8e]
<!-- rcw:end owner=source:src_a066be3d6e1e5368aa6aa09d35136b01 block=evidence -->

## Researcher notes

