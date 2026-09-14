---
access: public
aliases: []
claim_ids:
- clm_00c49aec09735a19a74393089a38aeb1dc1648637d24ca554c2fbab54ba8e741
- clm_032636e347a59397df225230de99774da00537696cbff0dadb90de84ad361123
- clm_1c6914b51c157d03dc8b0b56fdc3be622935eed2bbb9df335e6c5f1f00eabe64
- clm_2fb466491db1d97f07d3b92ef6e28bc9e6bdfee4533ca6cb1cd8c02a5f563762
- clm_3751999dc24126572a8732943e6ce0774ca950a5a00b5692b115ed3196bb7714
- clm_5b629ab76b98c31013e709f5326e7dec65cf9e260d5f27b59284b040cc41abed
- clm_6c77b34f6d4e8779ecd9fdec009db1fa1481986e7fc134863a4b1668a3005ade
- clm_80da7e3d8f5a9a646310a8a840aa0ae85bfe53d3e3ab4a8dc2f6dd22026d9204
- clm_8c00d2782511a31f3bf26940972e7715b0cf0d6d589be3af577798db0a9a8f30
- clm_9f61530017e4965672f77190e73702cd3ae5750e57572c6d58f0ef27163b0c6f
- clm_a442727046baaa4c60783b97e02933e1982450f968f5585065d0dcd3cdfe5278
- clm_a6b931ad259e938270470585f244e42862fc145863c66b0092e8800edfdfff44
- clm_a8789b4fd77eb0f32d178b25bf5aab6c8106e0c0a388cdf20ec55e1cca6eb6fd
- clm_c29ff2e92f6ff8a0f110b46c5fa2b5ef323995e420c22153a0d8aba3f62bf7ab
- clm_cc013d19a1426585cbf5372c5d7c3f4e1da4ec58cd6260cfba4caffa45e8e63b
- clm_ce8a66f0e9da17ab3ae70a29f62db53df17b85f950832eae80cbb790bce136f1
- clm_f1904200c3a2b5ac553834b4973426cb716687945120636a5166730dd9b7287f
- clm_f9a220d806838b5bfebce31c36a5e85f6d5d32d784506864ac8a0fb603c43be1
maturity: draft
page_id: pg_c03ccc73563a5320a4494204c0bc3439
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_cb131f9be6fc5cf881a436e4dce2b135
title: Palm1r/QodeAssist/README.md @ 558208df21ce
updated_at: '2026-09-14T02:28:23Z'
---

# Palm1r/QodeAssist/README.md @ 558208df21ce

<!-- rcw:begin owner=source:src_cb131f9be6fc5cf881a436e4dce2b135 block=evidence -->
- Chat history is auto-saved and restored, and Chat Summarization compresses long conversations into a new chat file (original preserved) targeting roughly 30-40% of the original length, filtering out tool results, edits, and thinking blocks. [@claim:clm_00c49aec09735a19a74393089a38aeb1dc1648637d24ca554c2fbab54ba8e741]
- Supported providers include local runtimes (Ollama, llama.cpp, LM Studio) and cloud providers (Claude, OpenAI, Google AI, Mistral/Codestral, OpenRouter, Qwen, DeepSeek, and any OpenAI-compatible endpoint). [@claim:clm_032636e347a59397df225230de99774da00537696cbff0dadb90de84ad361123]
- Default hotkeys include opening the chat window (Ctrl/Cmd+Alt+W), manual suggestion (Ctrl/Cmd+Alt+Q), Tab to accept a suggestion, and quick refactor (Ctrl/Cmd+Alt+R), all customizable in Qt Creator settings. [@claim:clm_1c6914b51c157d03dc8b0b56fdc3be622935eed2bbb9df335e6c5f1f00eabe64]
- Chat and Quick Refactor can invoke tools such as list_project_files, read_file, edit_file, build_project, get_issues_list, execute_terminal_command (with confirmation), and todo_tool, each individually toggleable in settings. [@claim:clm_2fb466491db1d97f07d3b92ef6e28bc9e6bdfee4533ca6cb1cd8c02a5f563762]
- Prompt composition differs by model type: FIM models get a template with prefix/suffix code context, while non-FIM chat models get a system prompt with formatting instructions plus a user completion request. [@claim:clm_3751999dc24126572a8732943e6ce0774ca950a5a00b5692b115ed3196bb7714]
- Code completion offers two trigger modes: hint-based (indicator after typing 3+ characters, suited to paid APIs to avoid charges) and automatic (default, suited to local models). [@claim:clm_5b629ab76b98c31013e709f5326e7dec65cf9e260d5f27b59284b040cc41abed]
- Agent Skills follow the open agentskills.io format: a folder with a SKILL.md containing YAML frontmatter (name, description) plus Markdown instructions, discovered from .qodeassist/skills/ and .claude/skills/ plus global directories. [@claim:clm_6c77b34f6d4e8779ecd9fdec009db1fa1481986e7fc134863a4b1668a3005ade]
- Repository development practice: contributors should follow the QML Coding Guide, use the project's .clang-format for C++, and run formatting before submitting PRs; detailed guidelines live in .cursor/rules.mdc. [@claim:clm_80da7e3d8f5a9a646310a8a840aa0ae85bfe53d3e3ab4a8dc2f6dd22026d9204]
- Skills are used in chat three ways: automatically via a load_skill tool (requires tool-calling models), explicitly via a / command, or always-on when frontmatter sets metadata always-on to true. [@claim:clm_8c00d2782511a31f3bf26940972e7715b0cf0d6d589be3af577798db0a9a8f30]
- The plugin targets Qt Creator users wanting AI assistance for C++/QML, with version compatibility documented from Qt Creator 14.0.1 through 17.0.0+. [@claim:clm_9f61530017e4965672f77190e73702cd3ae5750e57572c6d58f0ef27163b0c6f]
- Building the plugin requires CMake 3.16+, a C++20-compatible compiler, and Qt Creator development files; it incorporates Qt Creator components under GPLv3 with The Qt Company GPL Exception 1.0. [@claim:clm_a442727046baaa4c60783b97e02933e1982450f968f5585065d0dcd3cdfe5278]
- QodeAssist is licensed under GPL-3.0 with additional attribution terms under GPLv3 Section 7(b), and a separate commercial license is offered for proprietary use. [@claim:clm_a6b931ad259e938270470585f244e42862fc145863c66b0092e8800edfdfff44]
- The plugin adds AI code completion for C++ and QML, multi-panel chat, inline quick refactoring, agent tools, skills, and MCP server/client capabilities to Qt Creator. [@claim:clm_a8789b4fd77eb0f32d178b25bf5aab6c8106e0c0a388cdf20ec55e1cca6eb6fd]
- Authenticated MCP servers (OAuth or token-protected) are not supported yet; only unauthenticated local connections work. [@claim:clm_c29ff2e92f6ff8a0f110b46c5fa2b5ef323995e420c22153a0d8aba3f62bf7ab]
- The README states the project is archived: the author shut it down after copyright notices were removed without permission. [@claim:clm_cc013d19a1426585cbf5372c5d7c3f4e1da4ec58cd6260cfba4caffa45e8e63b]
- QodeAssist can run an MCP server on localhost (HTTP+SSE by default, with a stdio bridge) exposing its project-aware tools to external clients like Claude Code, VS Code, and Claude Desktop. [@claim:clm_ce8a66f0e9da17ab3ae70a29f62db53df17b85f950832eae80cbb790bce136f1]
- Repository development practice: build steps are mkdir build, then cmake with CMAKE_PREFIX_PATH pointing at Qt Creator and RelWithDebInfo, followed by cmake --build. [@claim:clm_f1904200c3a2b5ac553834b4973426cb716687945120636a5166730dd9b7287f]
- As an MCP client, QodeAssist connects to external MCP servers over stdio and HTTP/SSE and makes their tools available in Chat and Quick Refactor. [@claim:clm_f9a220d806838b5bfebce31c36a5e85f6d5d32d784506864ac8a0fb603c43be1]
<!-- rcw:end owner=source:src_cb131f9be6fc5cf881a436e4dce2b135 block=evidence -->

## Researcher notes

