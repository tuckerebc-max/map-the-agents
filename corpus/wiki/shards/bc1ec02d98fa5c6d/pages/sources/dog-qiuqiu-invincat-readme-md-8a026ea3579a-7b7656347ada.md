---
access: public
aliases: []
claim_ids:
- clm_20e987f0de1883b2c80c8be614b0764db59c2af4906e7bf97b5a49a719d643ff
- clm_2f77c31d3b465ee14e9fdd6c78b9cf5d48c530c3cefcddc8b08c313b7bf24917
- clm_52ad87263acd07224c23139442359f3f3061e9e49731509cd6db89420a1a8187
- clm_5537d5302129a49ebc86a9e3ce5655bf575f7ccd3d03a77e52aa7fb3bdecf9d8
- clm_9c6ff3f6c070b0cdf691928bac878cdfd0fae1952203d800d4d1dd18a35e6c2d
- clm_9cb53f6cc8cd933fb2d8a7a81deaa2bc555b30356c9d0e9aa8427eb36029fec9
- clm_9db1c58409ca0c3ed001fccbe1746aa7d23f303cb899e8938945888468f58adc
- clm_a8b2614e58bba5b8f0daac26b84143b28a6d1aad8bcdd4c683e195f2f1aa0648
- clm_cdc2529264955c6e45527d768d01f4c9147d82f6fa24ecdc9b71bb329420dd3a
- clm_dc54b40da60aaaeff5c4da4938890019d36e5084f2602970f2a6c13efcda5157
- clm_f0c6f0df1b9ccdf7d261d6ffd8473726cc046075128dc4a0e6916a4a8dd051ed
maturity: draft
page_id: pg_f5489a1d884957bb91957b7656347ada
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_ebe281ab90775f0db77af65a68f16f2a
title: dog-qiuqiu/invincat/README.md @ 8a026ea3579a
updated_at: '2026-09-14T03:06:54Z'
---

# dog-qiuqiu/invincat/README.md @ 8a026ea3579a

<!-- rcw:begin owner=source:src_ebe281ab90775f0db77af65a68f16f2a block=evidence -->
- Plan mode (/plan) first produces an execution checklist for user approval; the planner is restricted to read/planning tools, and implementation tools are reserved for post-approval execution by the main agent. [@claim:clm_20e987f0de1883b2c80c8be614b0764db59c2af4906e7bf97b5a49a719d643ff]
- An optional dedicated memory model can be set with /model 2 <provider:model> for post-turn memory extraction; otherwise extraction uses the current primary model. [@claim:clm_2f77c31d3b465ee14e9fdd6c78b9cf5d48c530c3cefcddc8b08c313b7bf24917]
- The WeCom bot daemon is configured with WECOM_BOT_ID and WECOM_BOT_SECRET environment variables, optionally overrides WECOM_WS_URL (default wss://openws.work.weixin.qq.com), and runs project-scoped remote turns and scheduled-task delivery. [@claim:clm_52ad87263acd07224c23139442359f3f3061e9e49731509cd6db89420a1a8187]
- Document-oriented skills rely on optional extras (invincat-cli[pdf], [office], [all-skills]) and may need system tools such as LibreOffice, Poppler, Tesseract, or Node.js packages. [@claim:clm_5537d5302129a49ebc86a9e3ce5655bf575f7ccd3d03a77e52aa7fb3bdecf9d8]
- Built-in subagents callable via the task tool include explorer (read-only codebase exploration), worker (bounded implementation), researcher (external research), and document-worker (document parsing/extraction for PDF, DOCX, PPTX, XLSX, Markdown, CSV, JSON). [@claim:clm_9c6ff3f6c070b0cdf691928bac878cdfd0fae1952203d800d4d1dd18a35e6c2d]
- The product exposes slash commands including /model, /plan, /goal, /memory, /schedule, /mcp, /threads, and /help, plus a wecombot subcommand to start the WeCom daemon. [@claim:clm_9cb53f6cc8cd933fb2d8a7a81deaa2bc555b30356c9d0e9aa8427eb36029fec9]
- File reads, edits, creation, and shell command execution are approval-gated, with shell commands running under configurable safety controls. [@claim:clm_9db1c58409ca0c3ed001fccbe1746aa7d23f303cb899e8938945888468f58adc]
- Model configuration is done via a /model manager (Ctrl+N to register provider, model name, API key, optional base URL) or through provider environment variables such as OPENAI_API_KEY, ANTHROPIC_API_KEY, GOOGLE_API_KEY, DEEPSEEK_API_KEY, and OPENROUTER_API_KEY. [@claim:clm_a8b2614e58bba5b8f0daac26b84143b28a6d1aad8bcdd4c683e195f2f1aa0648]
- The package is distributed on PyPI as invincat-cli, requires Python 3.11+, and can also be installed from source via an editable pip install. [@claim:clm_cdc2529264955c6e45527d768d01f4c9147d82f6fa24ecdc9b71bb329420dd3a]
- Skills are capability packs loaded when a task matches their description; built-in skills include docx, pdf, pptx, xlsx, and skill-creator, and custom skills can live at user, user-shared, project, or project-shared scope with project overriding user and custom overriding built-in. [@claim:clm_dc54b40da60aaaeff5c4da4938890019d36e5084f2602970f2a6c13efcda5157]
- Durable memory has two scopes: user memory at ~/.invincat/<agent>/memory_user.json and project memory at .invincat/memory_project.json; a background memory agent extracts updates after non-trivial turns, and /memory opens a manager UI. [@claim:clm_f0c6f0df1b9ccdf7d261d6ffd8473726cc046075128dc4a0e6916a4a8dd051ed]
<!-- rcw:end owner=source:src_ebe281ab90775f0db77af65a68f16f2a block=evidence -->

## Researcher notes

