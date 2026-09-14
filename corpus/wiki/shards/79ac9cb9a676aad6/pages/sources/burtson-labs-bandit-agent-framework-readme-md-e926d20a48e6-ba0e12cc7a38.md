---
access: public
aliases: []
claim_ids:
- clm_117d5b932ab2dc04cb2b29d749481e018a2b03714517bba6b9bdab72d3da06e4
- clm_1dbbbdb85218b30d9152e205e6bc411774314fa1eb5e154ddf2245e36d97dc0b
- clm_3570b701bdb26bed063ca22ce75d9f3e28d8ef66bf4ba9fca0a6dcc7220a78f3
- clm_368c811b2f240b0eb27d8d650b71cbf0e30518db9771dcd1e0cf829ceca18eeb
- clm_684a550a16caee7f470af13ddda067f9f4da2aa8d1f58bc88d8b6581bd1dc23e
- clm_7e0a4441f147aec848bce9c9bb65b312e48ffc98c4eae25fd36a05842ffff777
- clm_7e716087bf8447d90a47a8bc062defccc9343339f0d2ea65157bf89072c3aa0e
- clm_7f949bfb1e8a5de4019db59c9021065ca79d964b271e0aab8f2194fafcdd3b5b
- clm_80552685c338060e46d875c12c80b31b61e7337a6c99684fd454ece4f28d0233
- clm_86c2c1a06c2562134d3d737bf93c7378657c9c112f083261cd1f2a844d8683fb
- clm_98d0a292e320cc708dde134f1e1cbf94eccf13812eb6a40e66ad61c5e0e469b9
- clm_a038da8ae22405f36d982eb495b5528892dcfae8b635cfcff48c01474f92bfe5
- clm_a2287ad834121f12a6c0d5acc61f674360815699748900a7c9f4390a7900e309
- clm_a9d3ebab90df761807b0c54ea64938edde31f9c4a7acb025d701b97ed849f3fb
- clm_ac5ff94bc857614f3616ae21e74660dff389c3014232521bd2d7bff1d4e5bc2e
- clm_b3b7e55327a9f0b522b19994c79eaa233f03d7dff3fc50dd039d3b2effac0bce
- clm_b4cf88bb45a9446372f3045c3c8b769337cc985b5912824d46df790098820d3b
- clm_d5bf5513b4c9e4e4eabf5963d91d9c1128296926518a6a8754c0e250fc52d6fd
- clm_e0cc24667cc91c70001515cff6d6e5b39e178622f92fee0ca28f9ce1a9e39100
maturity: draft
page_id: pg_00477ce93dd85f4d8478ba0e12cc7a38
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_79d1725cc298549eb0d057a2427ab10d
title: Burtson-Labs/bandit-agent-framework/README.md @ e926d20a48e6
updated_at: '2026-09-14T01:38:53Z'
---

# Burtson-Labs/bandit-agent-framework/README.md @ e926d20a48e6

<!-- rcw:begin owner=source:src_79d1725cc298549eb0d057a2427ab10d block=evidence -->
- web_fetch is SSRF-guarded, refusing RFC1918, loopback, and cloud-metadata targets unless BANDIT_ALLOW_PRIVATE_WEB_FETCH=1 is set. [@claim:clm_117d5b932ab2dc04cb2b29d749481e018a2b03714517bba6b9bdab72d3da06e4]
- Stated design rules include local models as first-class citizens, one host-agnostic runtime, language adapters validating before write so invalid content never reaches disk, and intent-based skill activation. [@claim:clm_1dbbbdb85218b30d9152e205e6bc411774314fa1eb5e154ddf2245e36d97dc0b]
- The agent auto-loads BANDIT.md, CLAUDE.md, or AGENTS.md from the workspace root into the system prompt; /remember appends facts and /init scaffolds a new BANDIT.md. [@claim:clm_3570b701bdb26bed063ca22ce75d9f3e28d8ef66bf4ba9fca0a6dcc7220a78f3]
- Prompts can prefix a path with @ to inline file contents before the model sees them, up to 8 mentions per prompt at 64 KB each with auto-truncation. [@claim:clm_368c811b2f240b0eb27d8d650b71cbf0e30518db9771dcd1e0cf829ceca18eeb]
- The default skill set includes always-on filesystem and git skills plus context-triggered code review, testing, planning, semantic search, and Gmail-dependent mail search skills. [@claim:clm_684a550a16caee7f470af13ddda067f9f4da2aa8d1f58bc88d8b6581bd1dc23e]
- Repository development practice: contributors run pnpm test (what CI runs on PRs), add contract tests for new behaviors, and add real-trace replay fixtures for recurring failure modes per the agent-core test docs. [@claim:clm_7e0a4441f147aec848bce9c9bb65b312e48ffc98c4eae25fd36a05842ffff777]
- Auto mode runs routine work unprompted but always asks before destructive actions (deletions, history rewrites, credential files, exfiltration-style sends), and this floor cannot be disabled by settings or saved allow rules. [@claim:clm_7e716087bf8447d90a47a8bc062defccc9343339f0d2ea65157bf89072c3aa0e]
- REPL sessions persist as JSONL under ~/.bandit/sessions/ and can be resumed via bandit --resume or /session resume. [@claim:clm_7f949bfb1e8a5de4019db59c9021065ca79d964b271e0aab8f2194fafcdd3b5b]
- The agent can spawn background subagents whose synopses inject into the parent's next iteration; /tasks inspects and cancels them, and stopping cascades to in-flight subagents. [@claim:clm_80552685c338060e46d875c12c80b31b61e7337a6c99684fd454ece4f28d0233]
- The README lists maturing areas: plan mode in the CLI, status-line/TUI polish, and lossless trace replay for native-tool runs; PreToolUse hook failures warn but do not yet abort. [@claim:clm_86c2c1a06c2562134d3d737bf93c7378657c9c112f083261cd1f2a844d8683fb]
- The product ships two hosts — a VS Code/Cursor extension (Bandit Stealth) and a terminal CLI — both backed by the same stealth-core-runtime package, with skills, memory files, and hooks working identically across them. [@claim:clm_98d0a292e320cc708dde134f1e1cbf94eccf13812eb6a40e66ad61c5e0e469b9]
- A MEMORY.md topic index (capped at 4 KB) loads every turn while linked memory/ files (32 KB cap) are lazily fetched via read_memory when the task matches. [@claim:clm_a038da8ae22405f36d982eb495b5528892dcfae8b635cfcff48c01474f92bfe5]
- Bandit speaks MCP as both client and server: MCP server tools surface as <server>.<tool>, and 'bandit mcp serve' exposes native tools over stdio with a --read-only mode. [@claim:clm_a2287ad834121f12a6c0d5acc61f674360815699748900a7c9f4390a7900e309]
- Skills are markdown files with YAML frontmatter in .bandit/skills/ that load on the next turn; triggers are regex matches on the user prompt, activation:always skills run every turn, and legacy JSON skills still load. [@claim:clm_a9d3ebab90df761807b0c54ea64938edde31f9c4a7acb025d701b97ed849f3fb]
- The runtime targets Ollama (local daemon or Ollama Cloud via the same API) and optionally Bandit Cloud hosted inference; web_search uses Tavily with a TAVILY_API_KEY. [@claim:clm_ac5ff94bc857614f3616ae21e74660dff389c3014232521bd2d7bff1d4e5bc2e]
- The tool-use loop is capped by BANDIT_MAX_ITERATIONS (default 20); a documented benchmark run hit this ceiling and was forced to synthesize after 13 exploration rounds. [@claim:clm_b3b7e55327a9f0b522b19994c79eaa233f03d7dff3fc50dd039d3b2effac0bce]
- The CLI offers slash commands including /help, /doctor, /model, /skills, /session, /memory, /remember, /trace, /insights, and /exit. [@claim:clm_b4cf88bb45a9446372f3045c3c8b769337cc985b5912824d46df790098820d3b]
- Every file-edit tool call passes an approval gate that shows a compact diff before touching disk, with scoped grant options such as allow once, allow turn, allow session, always allow, and deny; approving a command grants only that command pattern. [@claim:clm_d5bf5513b4c9e4e4eabf5963d91d9c1128296926518a6a8754c0e250fc52d6fd]
- The README reports two reproducible benchmark runs of the agent on repo deep-dive prompts, with metrics like turn duration, LLM iterations, and tool-call counts, plus reproduction commands. [@claim:clm_e0cc24667cc91c70001515cff6d6e5b39e178622f92fee0ca28f9ce1a9e39100]
<!-- rcw:end owner=source:src_79d1725cc298549eb0d057a2427ab10d block=evidence -->

## Researcher notes

