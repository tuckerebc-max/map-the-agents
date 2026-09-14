---
access: public
aliases: []
claim_ids:
- clm_02367a87d2e4f4f8b05da1cbb3dabfdcf9736ddf92d5d645602e66a2af37c40a
- clm_1933f7b06f479954cf4e927e175d9d24c20a1e3559135d64be36c83ab5b71e38
- clm_2dcca38688ee0625eab95ed44b9ed9193fc99e8598ea5ec0d570a4ca0f9a2aec
- clm_44ecd83571c6a22f7d89b48e6e9ff9ceda1d8216fe6dbd4da09e47a80acb2169
- clm_6a3dcfe435be68dfe795142ab616268cb78e4c87b9c1a9dd96357fa7855fadcd
- clm_806b4d140395e05f2309adbc0152cd9e79f7f65d9d09b1ba0499ee427f88786f
- clm_88be92335b0883c5d5ad2646d943896646fa529af360bcf0e3ccdd8102b48187
- clm_9e245e5659bbe63b23023cc50a9638cada6778118bc72cbe36ecb10809cff9c3
- clm_c034bbe750f478f3d047b29b135dce470854222ee16ea19a1d8e36add1daf7d6
maturity: draft
page_id: pg_d51ac25df3975dcd875daff10cb2d6ab
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_265bdda968b45ba98ac228729504cd35
title: cuga-project/cuga-agent/README.md @ 65bdf2fb376d
updated_at: '2026-09-14T01:44:13Z'
---

# cuga-project/cuga-agent/README.md @ 65bdf2fb376d

<!-- rcw:begin owner=source:src_265bdda968b45ba98ac228729504cd35 block=evidence -->
- A built-in knowledge engine ingests PDFs, Office files, HTML, Markdown, and images via Docling, with documents scoped either agent-level (permanent, shared) or session-level (per-thread, isolated). [@claim:clm_02367a87d2e4f4f8b05da1cbb3dabfdcf9736ddf92d5d645602e66a2af37c40a]
- Configuration resolution priority is documented as environment variables highest, TOML configuration medium, and default values lowest. [@claim:clm_1933f7b06f479954cf4e927e175d9d24c20a1e3559135d64be36c83ab5b71e38]
- The final answer appears to be composed by a separately configurable LLM step that can be disabled in fast mode and shaped by a deterministic (str)->str function pointed at trusted code. [@claim:clm_2dcca38688ee0625eab95ed44b9ed9193fc99e8598ea5ec0d570a4ca0f9a2aec]
- The Python SDK exposes CugaAgent(tools=[...]) with await agent.invoke(message), real-time agent.stream(), per-user thread_id session isolation, and access to the underlying LangGraph graph. [@claim:clm_44ecd83571c6a22f7d89b48e6e9ff9ceda1d8216fe6dbd4da09e47a80acb2169]
- The optional run receipt (run_receipt, default false) records tool data in timings-only mode: name, app, and duration only, never arguments, results, or errors, unless track_tool_calls=True is set. [@claim:clm_6a3dcfe435be68dfe795142ab616268cb78e4c87b9c1a9dd96357fa7855fadcd]
- A single skills root is configured via [skills] root in settings.toml or DYNACONF_SKILLS__ROOT (default 'cuga'); CUGA scans one directory only, with no merge across paths. [@claim:clm_806b4d140395e05f2309adbc0152cd9e79f7f65d9d09b1ba0499ee427f88786f]
- Skills are SKILL.md files with YAML frontmatter requiring name and description; CUGA lists short descriptions in the prompt and exposes a load_skill tool that returns the full markdown body on demand. [@claim:clm_88be92335b0883c5d5ad2646d943896646fa529af360bcf0e3ccdd8102b48187]
- The README claims #1 rankings on AppWorld (07/25–02/26, 750 tasks across 457 APIs) and WebArena (02/25–09/25); these are self-reported leaderboard positions, not measured in this snapshot. [@claim:clm_9e245e5659bbe63b23023cc50a9638cada6778118bc72cbe36ecb10809cff9c3]
- Documented LLM provider support includes OpenAI (plus LiteLLM via base URL override), IBM WatsonX, Azure OpenAI, Groq, RITS, OpenRouter, and watsonx Orchestrate, each with a dedicated settings TOML. [@claim:clm_c034bbe750f478f3d047b29b135dce470854222ee16ea19a1d8e36add1daf7d6]
<!-- rcw:end owner=source:src_265bdda968b45ba98ac228729504cd35 block=evidence -->

## Researcher notes

