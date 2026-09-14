---
access: public
aliases: []
claim_ids:
- clm_092f123927b7cfb9727fdd1cdab77ee6dc3865665412f6acb13b3368d1f290f6
- clm_1af3e42696c05fccdfa99268a4af63ac2972d7171715e003f77280383261a0a3
- clm_1ee1daa61620bc82731565db57c7be45f1416011a633a7ca0609e6b5f8d7019c
- clm_258ef96da80b6c6352ae080d1315060b07eee0b08004d7ca55ab874dc27c5ab1
- clm_29b4858e0d0eefae73f70f7a4467bbc382696be3d86309f2db4f95709bd2d1f0
- clm_32d45750f01cadabf9ea7caaae1c3930e0d65ec8fc22ebb1740590a643003c44
- clm_4901f1c505d637f4e6956a7eebaac6b49bfa0e796543717cffe2b4343c7512bb
- clm_6221f6421c04067d701ebafb07996313accfc5149883d434fb72831811e7c143
- clm_6e375d19dfd95015fbd811ba9fbe2e5b8ac87a5e1e9b3d1039c0ae6103bd16a1
- clm_95beccbc791540fd0fd9123255ef231bbb859a3247c8e507291cbfa0f411dfda
- clm_b0a4759fd6bd63a9976c8ef484059174c72692dfa690240cf4a38292bf2a79cd
- clm_cb44563caa89b28ec5cac1985238874c07d3b6bbd8320994de254b5ef691effb
maturity: draft
page_id: pg_8b9a6357df9e576bb6e7ac75e2bc545e
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_c6997a7581dc5dea93da0d1fd58428d9
title: OrionStarAI/EasyCode/README.md @ 887b8bb4b5a8
updated_at: '2026-09-14T02:27:14Z'
---

# OrionStarAI/EasyCode/README.md @ 887b8bb4b5a8

<!-- rcw:begin owner=source:src_c6997a7581dc5dea93da0d1fd58428d9 block=evidence -->
- Built-in tools include file operations (read_file, write_file, replace, delete_file), search (glob, grep via ripgrep), shell execution, web_fetch/web_search, task sub-agent, todo_write, and memory. [@claim:clm_092f123927b7cfb9727fdd1cdab77ee6dc3865665412f6acb13b3368d1f290f6]
- The project is a monorepo with a CLI package (React Ink terminal UI, commands, services, auth) and a core package containing tools, MCP engine, prompts, hooks, skills, and config modules. [@claim:clm_1af3e42696c05fccdfa99268a4af63ac2972d7171715e003f77280383261a0a3]
- Delegated external-agent sessions can be resumed with a resume sub-syntax that reloads full session history via session/load, and task records persist under ~/.easycode-user/delegate-tasks/. [@claim:clm_1ee1daa61620bc82731565db57c7be45f1416011a633a7ca0609e6b5f8d7019c]
- MCP servers can be configured in .easycode/settings.json either as local processes (command/args/env) or via Streamable HTTP endpoints with headers, including trust and include/exclude tool options. [@claim:clm_258ef96da80b6c6352ae080d1315060b07eee0b08004d7ca55ab874dc27c5ab1]
- Interactive mode provides slash commands including /help, /session, /model, /compress, /tools, /mcp, /memory, /plan, /yolo, /restore, /theme, /auth, and /init. [@claim:clm_29b4858e0d0eefae73f70f7a4467bbc382696be3d86309f2db4f95709bd2d1f0]
- The stack uses TypeScript 5.x on Node.js 20+, React+Ink for CLI UI, esbuild for building, Vitest for tests, @google/genai for Gemini, and @modelcontextprotocol/sdk for MCP. [@claim:clm_32d45750f01cadabf9ea7caaae1c3930e0d65ec8fc22ebb1740590a643003c44]
- Custom models can be configured in OpenAI-compatible or Anthropic Claude formats via a /model management wizard or ~/.easycode-user/custom-models.json, with fields like provider, baseUrl, apiKey, modelId, and optional enableThinking. [@claim:clm_4901f1c505d637f4e6956a7eebaac6b49bfa0e796543717cffe2b4343c7512bb]
- Repository development practice: contributors clone the repo, run npm install, build with npm run build, test with npm run test, and run lint and typecheck before committing. [@claim:clm_6221f6421c04067d701ebafb07996313accfc5149883d434fb72831811e7c143]
- Tools carry documented safety levels: read-only tools like read_file and grep, confirmation-required tools like write_file, replace, and shell, with a --yolo mode that auto-executes all operations without confirmation. [@claim:clm_6e375d19dfd95015fbd811ba9fbe2e5b8ac87a5e1e9b3d1039c0ae6103bd16a1]
- The product is a CLI launched with the `easycode` command, supporting options such as --model, --prompt, --sandbox, --yolo, --continue, --session, --workdir, and --list-sessions. [@claim:clm_95beccbc791540fd0fd9123255ef231bbb859a3247c8e507291cbfa0f411dfda]
- Easy Code can act as an ACP orchestrator, delegating coding tasks to locally installed Claude Code or Codex via pinned ACP bridge packages, triggered by the model, @cc/@codex prefixes, or /bind in Feishu. [@claim:clm_b0a4759fd6bd63a9976c8ef484059174c72692dfa690240cf4a38292bf2a79cd]
- Sessions are persisted with automatic history saving, resumable via --continue or --session, with history compression to save tokens and checkpoint-based file rollback via /restore. [@claim:clm_cb44563caa89b28ec5cac1985238874c07d3b6bbd8320994de254b5ef691effb]
<!-- rcw:end owner=source:src_c6997a7581dc5dea93da0d1fd58428d9 block=evidence -->

## Researcher notes

