---
access: public
aliases: []
claim_ids:
- clm_02bf3680c86e6f29590633c15bd7cf3e2ab09589845a3b75f9599ca5c2312ae4
- clm_0dbc28bf1e3bd2d2515e96271083a6becc65a96db72e04bc918953d55618d222
- clm_118ad66701349223fd4d3c55e7ab88986120a50f572fe97d253e307e131ef864
- clm_143e501554c75df257e6d5f7fb7f71a5686ac1e73a517369b02ea9093763ffcb
- clm_1525f581855ad425a957acebc0f6b4e1b386a2b20fcf223c174c3ff0a0a1745b
- clm_25353ac3b64ca924ddd111940ddcb15eb41c75a9c5558bc5f9ac4e83b253e624
- clm_2596d0ba20be1cd1ae724990abf96e64a718d61b59cff28eec02b938b27078d0
- clm_4bb5be2414b53f5f84636bfd8af20d00f735c9a812888b4eced17696053f9ef9
- clm_67d12d7ab85fa33885beda9102dbb4fd24d797f13692586957683ae9ab8e1504
- clm_9e7c4f8a1c92969547ddb06f9656e35e1e3979573fe0517fd072764f31ca9dcd
- clm_af02ca7869f469958835534f5ea616551575e61d3ba11059d328967af0976a16
- clm_b0a446043b2de82103f2b1847f4212b9cc2d8a1edbf1ae603b0d006585756db9
- clm_bb211f51f14236693c91a63d65896b07cd9aba11f68cd33cfaa4fda3ad0d866b
- clm_f409b7a6cf74d358673d6cadfcecfa9ed67682fe9dcc31ec896434f3fe0bd2fd
- clm_ffaf9029ce4641281d0c03dfa8831e498b21446dfd358b4c83f0ab03f8ff499d
maturity: draft
page_id: pg_2e24ac8c910a5b5181b7794476c45227
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_d81855c1790553b290c6da2c923539bc
title: he-yufeng/CoreCoder/README.md @ 069948d180cb
updated_at: '2026-09-14T02:03:42Z'
---

# he-yufeng/CoreCoder/README.md @ 069948d180cb

<!-- rcw:begin owner=source:src_d81855c1790553b290c6da2c923539bc block=evidence -->
- By design, the product omits several capabilities: bash dangerous-command blocking is only a regex blacklist (not a sandbox), retry is exponential backoff only (no fallback model or dollar budget), sub-agents are synchronous only, there is no RAG, and the MCP client implements no resources or prompts. [@claim:clm_02bf3680c86e6f29590633c15bd7cf3e2ab09589845a3b75f9599ca5c2312ae4]
- The product ships a CLI with an interactive REPL and a one-shot mode ('corecoder -p "..."' that exits when done), plus REPL slash commands such as /model, /compact, /tokens, /diff, /undo, /plan, /save, and /sessions. [@claim:clm_0dbc28bf1e3bd2d2515e96271083a6becc65a96db72e04bc918953d55618d222]
- The package layout includes agent.py (main loop, 213 lines), llm.py (streaming client, retry, cost, 267 lines), context.py (three-tier compaction), session.py, permissions.py, hooks.py, mcp.py, cli.py, config.py, and a tools/ directory with bash, edit, grep, glob, read, write, todo, and sub-agent tools. [@claim:clm_118ad66701349223fd4d3c55e7ab88986120a50f572fe97d253e307e131ef864]
- If ~/.corecoder/mcp.json exists, MCP servers start as stdio subprocesses and their tools register as mcp__<server>__<tool>, treated like built-ins by hook matchers and the consent gate; the client implements only initialize, tools/list, and tools/call, with 15s handshake and 60s call timeouts. [@claim:clm_143e501554c75df257e6d5f7fb7f71a5686ac1e73a517369b02ea9093763ffcb]
- Sessions can be saved and listed under ~/.corecoder/sessions; session IDs are sanitized to safe filename characters so a malicious session name cannot traverse out of the directory. [@claim:clm_1525f581855ad425a957acebc0f6b4e1b386a2b20fcf223c174c3ff0a0a1745b]
- Hooks configured in ~/.corecoder/hooks.json run user shell commands around tool calls: pre hooks receive tool_name/tool_input on stdin and can veto with exit code 2 (stderr returned to the model), post hooks only observe, and hooks that error or exceed ten seconds are skipped with a warning. [@claim:clm_25353ac3b64ca924ddd111940ddcb15eb41c75a9c5558bc5f9ac4e83b253e624]
- The agent speaks the OpenAI-compatible API by default; providers are configured via environment variables (OPENAI_API_KEY, OPENAI_BASE_URL, CORECODER_MODEL), with an optional LiteLLM extra routing to a hundred-plus providers and .env loading at startup. [@claim:clm_2596d0ba20be1cd1ae724990abf96e64a718d61b59cff28eec02b938b27078d0]
- Sub-agents get an isolated context and history with a toolset exactly one item shorter (lacking the agent tool, preventing recursive spawning), reuse the parent's model connection, truncate output past 5,000 characters, and run on a shorter round limit. [@claim:clm_4bb5be2414b53f5f84636bfd8af20d00f735c9a812888b4eced17696053f9ef9]
- CoreCoder is a Python 3.10+ coding-agent engine, MIT-licensed and published on PyPI as 'corecoder', described as a ~1,171-line engine within 2,398 total lines of pure Python. [@claim:clm_67d12d7ab85fa33885beda9102dbb4fd24d797f13692586957683ae9ab8e1504]
- The package can be imported as a library: the top level exports Agent, LLM, and Config, and an example constructs an LLM with model, api_key, and base_url and calls Agent(llm=llm).chat(...). [@claim:clm_9e7c4f8a1c92969547ddb06f9656e35e1e3979573fe0517fd072764f31ca9dcd]
- The agent loop is a bounded loop: it queries the model, runs requested tool calls in parallel, feeds results back, and returns when the model stops requesting tools, with a round limit preventing runaway execution. [@claim:clm_af02ca7869f469958835534f5ea616551575e61d3ba11059d328967af0976a16]
- Read-only tools (read_file, glob, grep, todo_write) run immediately, while mutating tools (edit_file, write_file, bash, sub-agent spawning) stop for user consent; the REPL offers allow-once, always-allow-per-tool, or deny, and one-shot mode refuses mutating calls unless --yes is passed. [@claim:clm_b0a446043b2de82103f2b1847f4212b9cc2d8a1edbf1ae603b0d006585756db9]
- Plan mode, toggled via /plan, refuses all mutating calls (writes, edits, bash, MCP tools, sub-agents) and returns refusals to the model as ordinary tool results until the user approves the presented plan; it is a single Agent flag plus a refusal branch ahead of the consent gate, with no plan file persisted. [@claim:clm_bb211f51f14236693c91a63d65896b07cd9aba11f68cd33cfaa4fda3ad0d866b]
- edit_file uses unique-match search-and-replace rather than line numbers: no match returns the file start for re-anchoring, multiple matches require more context, and success returns a diff. [@claim:clm_f409b7a6cf74d358673d6cadfcecfa9ed67682fe9dcc31ec896434f3fe0bd2fd]
- Context is compacted in three tiers: at 50% full it trims over-long tool outputs mechanically, at 70% the model summarizes older turns while keeping recent ones verbatim, and at 90% it compresses everything to its tightest form. [@claim:clm_ffaf9029ce4641281d0c03dfa8831e498b21446dfd358b4c83f0ab03f8ff499d]
<!-- rcw:end owner=source:src_d81855c1790553b290c6da2c923539bc block=evidence -->

## Researcher notes

