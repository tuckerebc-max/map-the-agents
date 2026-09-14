# orionstarai/easycode

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 887b8bb4b5a8 @ a79807b5d6c7fa03

## Summary (orientation draft, not independently verified)

README evidence describes Easy Code, an AI coding agent CLI (npm package easycode-ai) with a monorepo of CLI/core/VS Code packages, built-in tools, MCP support, hooks, sessions, custom models, and ACP delegation to Claude Code/Codex. Most claims are documentation-based; no code inspection is available in these slices. Evidence coverage: 198 of 400 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 127 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The project is a monorepo with a CLI package (React Ink terminal UI, commands, services, auth) and a core package containing tools, MCP engine, prompts, hooks, skills, and config modules. -- evidence: [README.md#L503-L513](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L503-L513), [README.md#L430-L499](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L430-L499), [README.md#L426-L426](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L426-L426)
- design-choices (1 claim(s)):
  - [observation/documented] MCP servers can be configured in .easycode/settings.json either as local processes (command/args/env) or via Streamable HTTP endpoints with headers, including trust and include/exclude tool options. -- evidence: [README.md#L674-L674](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L674-L674), [README.md#L680-L696](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L680-L696), [README.md#L740-L746](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L740-L746), [README.md#L712-L730](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L712-L730), [README.md#L698-L706](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L698-L706), [README.md#L732-L736](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L732-L736)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributors clone the repo, run npm install, build with npm run build, test with npm run test, and run lint and typecheck before committing. -- evidence: [README.md#L1140-L1144](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L1140-L1144), [README.md#L1115-L1116](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L1115-L1116), [README.md#L1124-L1136](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L1124-L1136), [README.md#L1119-L1120](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L1119-L1120)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The product is a CLI launched with the `easycode` command, supporting options such as --model, --prompt, --sandbox, --yolo, --continue, --session, --workdir, and --list-sessions. -- evidence: [README.md#L282-L284](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L282-L284), [README.md#L228-L230](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L228-L230), [README.md#L286-L300](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L286-L300)
  - [observation/documented] Interactive mode provides slash commands including /help, /session, /model, /compress, /tools, /mcp, /memory, /plan, /yolo, /restore, /theme, /auth, and /init. -- evidence: [README.md#L384-L389](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L384-L389), [README.md#L375-L380](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L375-L380), [README.md#L409-L412](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L409-L412), [README.md#L416-L420](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L416-L420), [README.md#L359-L363](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L359-L363), [README.md#L350-L355](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L350-L355), [README.md#L367-L371](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L367-L371), [README.md#L341-L346](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L341-L346)
- memory-state (1 claim(s)):
  - [observation/documented] Sessions are persisted with automatic history saving, resumable via --continue or --session, with history compression to save tokens and checkpoint-based file rollback via /restore. -- evidence: [README.md#L375-L380](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L375-L380), [README.md#L166-L169](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L166-L169), [README.md#L350-L355](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L350-L355), [README.md#L286-L300](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L286-L300)
- orchestration (2 claim(s)):
  - [observation/documented] Easy Code can act as an ACP orchestrator, delegating coding tasks to locally installed Claude Code or Codex via pinned ACP bridge packages, triggered by the model, @cc/@codex prefixes, or /bind in Feishu. -- evidence: [README.md#L975-L978](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L975-L978), [README.md#L971-L971](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L971-L971), [README.md#L982-L986](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L982-L986)
  - [observation/documented] Delegated external-agent sessions can be resumed with a resume sub-syntax that reloads full session history via session/load, and task records persist under ~/.easycode-user/delegate-tasks/. -- evidence: [README.md#L997-L997](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L997-L997), [README.md#L1008-L1008](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L1008-L1008), [README.md#L1003-L1006](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L1003-L1006), [README.md#L1001-L1001](https://github.com/OrionStarAI/EasyCode/blob/887b8bb4b5a8acfbb3dfe8b69953e7d850c30547/README.md#L1001-L1001)
- tools-permissions (2 claim(s)):
More evidence: [full detail](easycode.detail.md)

Metadata and full claim list: [full detail](easycode.detail.md)
Human notes ([notes](easycode.notes.md), never overwritten by build)

[Back to map index](../../index.md)
