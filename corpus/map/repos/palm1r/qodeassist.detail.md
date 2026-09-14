# palm1r/qodeassist -- full detail

[Back to orientation](qodeassist.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/palm1r/qodeassist/558208df21ce8dfd844fdc0d7d07a75a2fb5d5a5/68a0798e723b5f74.json](../../../wiki/dossiers/palm1r/qodeassist/558208df21ce8dfd844fdc0d7d07a75a2fb5d5a5/68a0798e723b5f74.json)

## specifications (2 claim(s))

- [observation/documented] QodeAssist is licensed under GPL-3.0 with additional attribution terms under GPLv3 Section 7(b), and a separate commercial license is offered for proprietary use. -- evidence: [README.md#L532-L534](https://github.com/Palm1r/QodeAssist/blob/558208df21ce8dfd844fdc0d7d07a75a2fb5d5a5/README.md#L532-L534), [README.md#L545-L547](https://github.com/Palm1r/QodeAssist/blob/558208df21ce8dfd844fdc0d7d07a75a2fb5d5a5/README.md#L545-L547) (`clm_a6b931ad259e938270470585f244e42862fc145863c66b0092e8800edfdfff44`)
- [observation/documented] The README states the project is archived: the author shut it down after copyright notices were removed without permission. -- evidence: [README.md#L10-L15](https://github.com/Palm1r/QodeAssist/blob/558208df21ce8dfd844fdc0d7d07a75a2fb5d5a5/README.md#L10-L15) (`clm_cc013d19a1426585cbf5372c5d7c3f4e1da4ec58cd6260cfba4caffa45e8e63b`)

## components (1 claim(s))

- [observation/documented] The plugin adds AI code completion for C++ and QML, multi-panel chat, inline quick refactoring, agent tools, skills, and MCP server/client capabilities to Qt Creator. -- evidence: [README.md#L18-L18](https://github.com/Palm1r/QodeAssist/blob/558208df21ce8dfd844fdc0d7d07a75a2fb5d5a5/README.md#L18-L18), [README.md#L37-L47](https://github.com/Palm1r/QodeAssist/blob/558208df21ce8dfd844fdc0d7d07a75a2fb5d5a5/README.md#L37-L47) (`clm_a8789b4fd77eb0f32d178b25bf5aab6c8106e0c0a388cdf20ec55e1cca6eb6fd`)

## design-choices (2 claim(s))

- [observation/documented] Code completion offers two trigger modes: hint-based (indicator after typing 3+ characters, suited to paid APIs to avoid charges) and automatic (default, suited to local models). -- evidence: [README.md#L206-L206](https://github.com/Palm1r/QodeAssist/blob/558208df21ce8dfd844fdc0d7d07a75a2fb5d5a5/README.md#L206-L206), [README.md#L208-L213](https://github.com/Palm1r/QodeAssist/blob/558208df21ce8dfd844fdc0d7d07a75a2fb5d5a5/README.md#L208-L213), [README.md#L215-L219](https://github.com/Palm1r/QodeAssist/blob/558208df21ce8dfd844fdc0d7d07a75a2fb5d5a5/README.md#L215-L219) (`clm_5b629ab76b98c31013e709f5326e7dec65cf9e260d5f27b59284b040cc41abed`)
- [observation/documented] Prompt composition differs by model type: FIM models get a template with prefix/suffix code context, while non-FIM chat models get a system prompt with formatting instructions plus a user completion request. -- evidence: [README.md#L315-L332](https://github.com/Palm1r/QodeAssist/blob/558208df21ce8dfd844fdc0d7d07a75a2fb5d5a5/README.md#L315-L332), [README.md#L424-L431](https://github.com/Palm1r/QodeAssist/blob/558208df21ce8dfd844fdc0d7d07a75a2fb5d5a5/README.md#L424-L431), [README.md#L339-L359](https://github.com/Palm1r/QodeAssist/blob/558208df21ce8dfd844fdc0d7d07a75a2fb5d5a5/README.md#L339-L359) (`clm_3751999dc24126572a8732943e6ce0774ca950a5a00b5692b115ed3196bb7714`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: contributors should follow the QML Coding Guide, use the project's .clang-format for C++, and run formatting before submitting PRs; detailed guidelines live in .cursor/rules.mdc. -- evidence: [README.md#L522-L524](https://github.com/Palm1r/QodeAssist/blob/558208df21ce8dfd844fdc0d7d07a75a2fb5d5a5/README.md#L522-L524), [README.md#L528-L528](https://github.com/Palm1r/QodeAssist/blob/558208df21ce8dfd844fdc0d7d07a75a2fb5d5a5/README.md#L528-L528) (`clm_80da7e3d8f5a9a646310a8a840aa0ae85bfe53d3e3ab4a8dc2f6dd22026d9204`)
- [observation/documented] Repository development practice: build steps are mkdir build, then cmake with CMAKE_PREFIX_PATH pointing at Qt Creator and RelWithDebInfo, followed by cmake --build. -- evidence: [README.md#L507-L510](https://github.com/Palm1r/QodeAssist/blob/558208df21ce8dfd844fdc0d7d07a75a2fb5d5a5/README.md#L507-L510), [README.md#L501-L503](https://github.com/Palm1r/QodeAssist/blob/558208df21ce8dfd844fdc0d7d07a75a2fb5d5a5/README.md#L501-L503), [README.md#L512-L516](https://github.com/Palm1r/QodeAssist/blob/558208df21ce8dfd844fdc0d7d07a75a2fb5d5a5/README.md#L512-L516) (`clm_f1904200c3a2b5ac553834b4973426cb716687945120636a5166730dd9b7287f`)

## skills-patterns (2 claim(s))

- [observation/documented] Agent Skills follow the open agentskills.io format: a folder with a SKILL.md containing YAML frontmatter (name, description) plus Markdown instructions, discovered from .qodeassist/skills/ and .claude/skills/ plus global directories. -- evidence: [README.md#L261-L261](https://github.com/Palm1r/QodeAssist/blob/558208df21ce8dfd844fdc0d7d07a75a2fb5d5a5/README.md#L261-L261), [README.md#L279-L281](https://github.com/Palm1r/QodeAssist/blob/558208df21ce8dfd844fdc0d7d07a75a2fb5d5a5/README.md#L279-L281), [README.md#L259-L259](https://github.com/Palm1r/QodeAssist/blob/558208df21ce8dfd844fdc0d7d07a75a2fb5d5a5/README.md#L259-L259) (`clm_6c77b34f6d4e8779ecd9fdec009db1fa1481986e7fc134863a4b1668a3005ade`)
- [observation/documented] Skills are used in chat three ways: automatically via a load_skill tool (requires tool-calling models), explicitly via a / command, or always-on when frontmatter sets metadata always-on to true. -- evidence: [README.md#L285-L288](https://github.com/Palm1r/QodeAssist/blob/558208df21ce8dfd844fdc0d7d07a75a2fb5d5a5/README.md#L285-L288) (`clm_8c00d2782511a31f3bf26940972e7715b0cf0d6d589be3af577798db0a9a8f30`)

## interfaces (4 claim(s))

- [observation/documented] Chat and Quick Refactor can invoke tools such as list_project_files, read_file, edit_file, build_project, get_issues_list, execute_terminal_command (with confirmation), and todo_tool, each individually toggleable in settings. -- evidence: [README.md#L244-L255](https://github.com/Palm1r/QodeAssist/blob/558208df21ce8dfd844fdc0d7d07a75a2fb5d5a5/README.md#L244-L255), [README.md#L242-L242](https://github.com/Palm1r/QodeAssist/blob/558208df21ce8dfd844fdc0d7d07a75a2fb5d5a5/README.md#L242-L242) (`clm_2fb466491db1d97f07d3b92ef6e28bc9e6bdfee4533ca6cb1cd8c02a5f563762`)
- [observation/documented] QodeAssist can run an MCP server on localhost (HTTP+SSE by default, with a stdio bridge) exposing its project-aware tools to external clients like Claude Code, VS Code, and Claude Desktop. -- evidence: [README.md#L294-L294](https://github.com/Palm1r/QodeAssist/blob/558208df21ce8dfd844fdc0d7d07a75a2fb5d5a5/README.md#L294-L294), [README.md#L296-L298](https://github.com/Palm1r/QodeAssist/blob/558208df21ce8dfd844fdc0d7d07a75a2fb5d5a5/README.md#L296-L298) (`clm_ce8a66f0e9da17ab3ae70a29f62db53df17b85f950832eae80cbb790bce136f1`)
- [observation/documented] As an MCP client, QodeAssist connects to external MCP servers over stdio and HTTP/SSE and makes their tools available in Chat and Quick Refactor. -- evidence: [README.md#L304-L306](https://github.com/Palm1r/QodeAssist/blob/558208df21ce8dfd844fdc0d7d07a75a2fb5d5a5/README.md#L304-L306), [README.md#L302-L302](https://github.com/Palm1r/QodeAssist/blob/558208df21ce8dfd844fdc0d7d07a75a2fb5d5a5/README.md#L302-L302) (`clm_f9a220d806838b5bfebce31c36a5e85f6d5d32d784506864ac8a0fb603c43be1`)
- [observation/documented] Default hotkeys include opening the chat window (Ctrl/Cmd+Alt+W), manual suggestion (Ctrl/Cmd+Alt+Q), Tab to accept a suggestion, and quick refactor (Ctrl/Cmd+Alt+R), all customizable in Qt Creator settings. -- evidence: [README.md#L450-L450](https://github.com/Palm1r/QodeAssist/blob/558208df21ce8dfd844fdc0d7d07a75a2fb5d5a5/README.md#L450-L450), [README.md#L452-L459](https://github.com/Palm1r/QodeAssist/blob/558208df21ce8dfd844fdc0d7d07a75a2fb5d5a5/README.md#L452-L459) (`clm_1c6914b51c157d03dc8b0b56fdc3be622935eed2bbb9df335e6c5f1f00eabe64`)

## memory-state (1 claim(s))

- [observation/documented] Chat history is auto-saved and restored, and Chat Summarization compresses long conversations into a new chat file (original preserved) targeting roughly 30-40% of the original length, filtering out tool results, edits, and thinking blocks. -- evidence: [README.md#L226-L231](https://github.com/Palm1r/QodeAssist/blob/558208df21ce8dfd844fdc0d7d07a75a2fb5d5a5/README.md#L226-L231), [docs/chat-summarization.md#L13-L17](https://github.com/Palm1r/QodeAssist/blob/558208df21ce8dfd844fdc0d7d07a75a2fb5d5a5/docs/chat-summarization.md#L13-L17), [docs/chat-summarization.md#L51-L54](https://github.com/Palm1r/QodeAssist/blob/558208df21ce8dfd844fdc0d7d07a75a2fb5d5a5/docs/chat-summarization.md#L51-L54), [docs/chat-summarization.md#L43-L47](https://github.com/Palm1r/QodeAssist/blob/558208df21ce8dfd844fdc0d7d07a75a2fb5d5a5/docs/chat-summarization.md#L43-L47), [docs/chat-summarization.md#L58-L68](https://github.com/Palm1r/QodeAssist/blob/558208df21ce8dfd844fdc0d7d07a75a2fb5d5a5/docs/chat-summarization.md#L58-L68) (`clm_00c49aec09735a19a74393089a38aeb1dc1648637d24ca554c2fbab54ba8e741`)

## orchestration (2 claim(s))

- [observation/documented] QodeAssist integrates external ACP coding agents: an Agents settings page merges user JSON files, a downloadable registry, and a bundled snapshot, and a Test button runs the ACP initialize handshake to report agent capabilities. -- evidence: [docs/acp-agents.md#L13-L19](https://github.com/Palm1r/QodeAssist/blob/558208df21ce8dfd844fdc0d7d07a75a2fb5d5a5/docs/acp-agents.md#L13-L19), [docs/acp-agents.md#L102-L106](https://github.com/Palm1r/QodeAssist/blob/558208df21ce8dfd844fdc0d7d07a75a2fb5d5a5/docs/acp-agents.md#L102-L106), [docs/acp-agents.md#L3-L6](https://github.com/Palm1r/QodeAssist/blob/558208df21ce8dfd844fdc0d7d07a75a2fb5d5a5/docs/acp-agents.md#L3-L6) (`clm_79146146de4281abb652f0dfffc1218fe59426607419d29bced447beac56efb5`)
- [observation/documented] For ACP agents, a Hand over button summarizes the transcript with the Chat Assistant configuration and starts a fresh agent session seeded with that summary; auto-compression never triggers for agent sessions. -- evidence: [docs/chat-summarization.md#L36-L39](https://github.com/Palm1r/QodeAssist/blob/558208df21ce8dfd844fdc0d7d07a75a2fb5d5a5/docs/chat-summarization.md#L36-L39), [docs/chat-summarization.md#L30-L34](https://github.com/Palm1r/QodeAssist/blob/558208df21ce8dfd844fdc0d7d07a75a2fb5d5a5/docs/chat-summarization.md#L30-L34), [docs/acp-agents.md#L110-L114](https://github.com/Palm1r/QodeAssist/blob/558208df21ce8dfd844fdc0d7d07a75a2fb5d5a5/docs/acp-agents.md#L110-L114) (`clm_2717565ae2c198ba3020e1583a5011bf4ce11715365d9a0bb88e0554ecbcaac9`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] Building the plugin requires CMake 3.16+, a C++20-compatible compiler, and Qt Creator development files; it incorporates Qt Creator components under GPLv3 with The Qt Company GPL Exception 1.0. -- evidence: [README.md#L493-L495](https://github.com/Palm1r/QodeAssist/blob/558208df21ce8dfd844fdc0d7d07a75a2fb5d5a5/README.md#L493-L495), [README.md#L555-L561](https://github.com/Palm1r/QodeAssist/blob/558208df21ce8dfd844fdc0d7d07a75a2fb5d5a5/README.md#L555-L561), [README.md#L551-L553](https://github.com/Palm1r/QodeAssist/blob/558208df21ce8dfd844fdc0d7d07a75a2fb5d5a5/README.md#L551-L553) (`clm_a442727046baaa4c60783b97e02933e1982450f968f5585065d0dcd3cdfe5278`)
- [observation/documented] Supported providers include local runtimes (Ollama, llama.cpp, LM Studio) and cloud providers (Claude, OpenAI, Google AI, Mistral/Codestral, OpenRouter, Qwen, DeepSeek, and any OpenAI-compatible endpoint). -- evidence: [README.md#L18-L18](https://github.com/Palm1r/QodeAssist/blob/558208df21ce8dfd844fdc0d7d07a75a2fb5d5a5/README.md#L18-L18), [README.md#L164-L171](https://github.com/Palm1r/QodeAssist/blob/558208df21ce8dfd844fdc0d7d07a75a2fb5d5a5/README.md#L164-L171), [README.md#L157-L162](https://github.com/Palm1r/QodeAssist/blob/558208df21ce8dfd844fdc0d7d07a75a2fb5d5a5/README.md#L157-L162) (`clm_032636e347a59397df225230de99774da00537696cbff0dadb90de84ad361123`)

## limitations (1 claim(s))

- [observation/documented] Authenticated MCP servers (OAuth or token-protected) are not supported yet; only unauthenticated local connections work. -- evidence: [README.md#L304-L306](https://github.com/Palm1r/QodeAssist/blob/558208df21ce8dfd844fdc0d7d07a75a2fb5d5a5/README.md#L304-L306) (`clm_c29ff2e92f6ff8a0f110b46c5fa2b5ef323995e420c22153a0d8aba3f62bf7ab`)

## relevance (1 claim(s))

- [observation/documented] The plugin targets Qt Creator users wanting AI assistance for C++/QML, with version compatibility documented from Qt Creator 14.0.1 through 17.0.0+. -- evidence: [README.md#L18-L18](https://github.com/Palm1r/QodeAssist/blob/558208df21ce8dfd844fdc0d7d07a75a2fb5d5a5/README.md#L18-L18), [README.md#L437-L446](https://github.com/Palm1r/QodeAssist/blob/558208df21ce8dfd844fdc0d7d07a75a2fb5d5a5/README.md#L437-L446) (`clm_9f61530017e4965672f77190e73702cd3ae5750e57572c6d58f0ef27163b0c6f`)

