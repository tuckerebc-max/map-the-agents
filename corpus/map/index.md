# Map the Agents -- Observatory index

Coverage: 990 of 1062 known/total (distilled with kernel-applied, currently valid evidence).
Known-dossier source depth (distinct from freshness -- a current commit is not complete source coverage): complete=454, partial=536, unknown=0 (legacy dossiers with no packet coverage recorded).

Status counts: discovered=10, distilled=990, blocked=62

Freshness counts: current=974, pending=10, stale=16, refresh-failed=62

Identity: 34 repo(s) carry a verified GitHub rename lineage (see their repo pages).

Navigation: [classes](classes/index.md) | [agents](agents/index.md) | [components](components/index.md) | [patterns](patterns/index.md) | [features](features/index.md) | [gaps](gaps/index.md) | [freshness](freshness/index.md) | [directory](directory/index.md)

## Classes

Full index: [classes/index.md](classes/index.md) (4 class(es)).

- [agent](classes/agent.md) (444 repo(s))
- [agent-sdk](classes/agent-sdk.md) (25 repo(s))
- [multiplexer](classes/multiplexer.md) (182 repo(s))
- [uncategorized](classes/uncategorized.md) (411 repo(s))

## Agents

Full index: [agents/index.md](agents/index.md) (1062 repo(s)).

- [0xpayne/gpt-migrate](repos/0xpayne/gpt-migrate.md) -- status=blocked, freshness=refresh-failed
- [101dotxyz/gpteam](repos/101dotxyz/gpteam.md) -- status=distilled, freshness=current
- [1jehuang/jcode](repos/1jehuang/jcode.md) -- status=distilled, freshness=current
- [21st-dev/1code](repos/21st-dev/1code.md) -- status=distilled, freshness=current
- [233i/ore-code](repos/233i/ore-code.md) -- status=distilled, freshness=current
- [2389-research/2389-agent-rust](repos/2389-research/2389-agent-rust.md) -- status=distilled, freshness=current
- [2389-research/binary-re](repos/2389-research/binary-re.md) -- status=distilled, freshness=current
- [2389-research/breakaway-agent](repos/2389-research/breakaway-agent.md) -- status=distilled, freshness=current
- [2389-research/claude-plugins](repos/2389-research/claude-plugins.md) -- status=distilled, freshness=current
- [2389-research/coven](repos/2389-research/coven.md) -- status=distilled, freshness=current
- [2389-research/coven-gateway](repos/2389-research/coven-gateway.md) -- status=distilled, freshness=current
- [2389-research/dippin-lang](repos/2389-research/dippin-lang.md) -- status=distilled, freshness=current
- [2389-research/fleet-control](repos/2389-research/fleet-control.md) -- status=distilled, freshness=current
- [2389-research/gossip](repos/2389-research/gossip.md) -- status=distilled, freshness=current
- [2389-research/hex](repos/2389-research/hex.md) -- status=distilled, freshness=current
- [2389-research/mux-rs](repos/2389-research/mux-rs.md) -- status=distilled, freshness=current
- [2389-research/ourocodus](repos/2389-research/ourocodus.md) -- status=distilled, freshness=current
- [2389-research/packnplay](repos/2389-research/packnplay.md) -- status=distilled, freshness=current
- [2389-research/sift](repos/2389-research/sift.md) -- status=distilled, freshness=current
- [2389-research/simmer](repos/2389-research/simmer.md) -- status=distilled, freshness=current
- ... 1042 more; see agents/index.md

## Components

Full index: [components/index.md](components/index.md).

- [101dotxyz/gpteam](repos/101dotxyz/gpteam.md) [observation/documented] While the world runs, each agent's current state is written to a text file in the agents/ folder, letting users observe what agents are doing. -- evidence: [README.md#L47-L47](https://github.com/101dotxyz/GPTeam/blob/a216364ea2dbb208e6501468c5e5b791594cc3d5/README.md#L47-L47)
- [101dotxyz/gpteam](repos/101dotxyz/gpteam.md) [observation/documented] GPTeam uses GPT-4 to create multiple agents that collaborate to achieve predefined goals, aiming to explore GPT models' potential for multi-agent productivity and communication. -- evidence: [README.md#L21-L21](https://github.com/101dotxyz/GPTeam/blob/a216364ea2dbb208e6501468c5e5b791594cc3d5/README.md#L21-L21)
- [101dotxyz/gpteam](repos/101dotxyz/gpteam.md) [observation/documented] In the Discord integration, each world maps to a Discord guild, each location to a channel, each agent to a separate bot application, plus an announcer bot that announces agent movement between rooms. -- evidence: [DISCORD.md#L3-L8](https://github.com/101dotxyz/GPTeam/blob/a216364ea2dbb208e6501468c5e5b791594cc3d5/DISCORD.md#L3-L8)
- [101dotxyz/gpteam](repos/101dotxyz/gpteam.md) [observation/documented] The world is configured via a config.json file listing available agents and locations; after editing it, users reset the database and relaunch the world. -- evidence: [README.md#L53-L55](https://github.com/101dotxyz/GPTeam/blob/a216364ea2dbb208e6501468c5e5b791594cc3d5/README.md#L53-L55)
- [101dotxyz/gpteam](repos/101dotxyz/gpteam.md) [observation/documented] A --turbo flag runs all LLM calls with gpt3.5-turbo for lower cost, at the cost of worse results; a --claude flag uses claude-v1 and claude-v1-instant for some calls. -- evidence: [README.md#L37-L37](https://github.com/101dotxyz/GPTeam/blob/a216364ea2dbb208e6501468c5e5b791594cc3d5/README.md#L37-L37), [README.md#L63-L63](https://github.com/101dotxyz/GPTeam/blob/a216364ea2dbb208e6501468c5e5b791594cc3d5/README.md#L63-L63)
- [101dotxyz/gpteam](repos/101dotxyz/gpteam.md) [observation/documented] Each agent has its own memory and uses communication as a tool; agent memory and reflection are inspired by a cited research paper (arXiv 2304.03442). -- evidence: [README.md#L43-L43](https://github.com/101dotxyz/GPTeam/blob/a216364ea2dbb208e6501468c5e5b791594cc3d5/README.md#L43-L43)
- [1jehuang/jcode](repos/1jehuang/jcode.md) [observation/documented] Updates run via /update in the TUI or `jcode update`; dev builds compare the running binary's Git commit against the release tag and stop rather than risk a downgrade when ancestry cannot be verified. -- evidence: [README.md#L50-L52](https://github.com/1jehuang/jcode/blob/37159430c3d02545fd7c10b0bd13e754b49f871b/README.md#L50-L52), [README.md#L54-L59](https://github.com/1jehuang/jcode/blob/37159430c3d02545fd7c10b0bd13e754b49f871b/README.md#L54-L59)
- [1jehuang/jcode](repos/1jehuang/jcode.md) [observation/documented] User input is interleaved with the working agent as soon as it can be sent without breaking the KV cache; shift-enter instead queues the message until the agent finishes its turn. -- evidence: [README.md#L672-L672](https://github.com/1jehuang/jcode/blob/37159430c3d02545fd7c10b0bd13e754b49f871b/README.md#L672-L672)
- [1jehuang/jcode](repos/1jehuang/jcode.md) [observation/documented] MCP servers are configured in ~/.jcode/mcp.json (global) and .jcode/mcp.json (project-local); Claude Code config files (~/.claude.json, .mcp.json, .claude/mcp.json) are read live, and a one-time import from ~/.codex/config.toml is performed. -- evidence: [README.md#L573-L575](https://github.com/1jehuang/jcode/blob/37159430c3d02545fd7c10b0bd13e754b49f871b/README.md#L573-L575), [README.md#L568-L569](https://github.com/1jehuang/jcode/blob/37159430c3d02545fd7c10b0bd13e754b49f871b/README.md#L568-L569), [README.md#L577-L584](https://github.com/1jehuang/jcode/blob/37159430c3d02545fd7c10b0bd13e754b49f871b/README.md#L577-L584)
- [1jehuang/jcode](repos/1jehuang/jcode.md) [observation/documented] jcode offers built-in login flows via `jcode login --provider <id>` for providers including claude, openai, gemini, copilot, azure, fireworks, novita, minimax, lmstudio, ollama, and custom OpenAI-compatible endpoints. -- evidence: [README.md#L352-L364](https://github.com/1jehuang/jcode/blob/37159430c3d02545fd7c10b0bd13e754b49f871b/README.md#L352-L364)
- [1jehuang/jcode](repos/1jehuang/jcode.md) [observation/documented] An 'agent grep' tool augments grep output with file structure information (function lists, offsets) and adaptively truncates results based on what the agent has already seen to save context. -- evidence: [README.md#L670-L670](https://github.com/1jehuang/jcode/blob/37159430c3d02545fd7c10b0bd13e754b49f871b/README.md#L670-L670)
- [1jehuang/jcode](repos/1jehuang/jcode.md) [observation/documented] Headless OAuth is supported via --no-browser (printing auth URL/QR for manual paste), and a two-step --print-auth-url / --callback-url or --auth-code pattern exists for openai, gemini, claude, and antigravity. -- evidence: [README.md#L626-L627](https://github.com/1jehuang/jcode/blob/37159430c3d02545fd7c10b0bd13e754b49f871b/README.md#L626-L627), [README.md#L618-L620](https://github.com/1jehuang/jcode/blob/37159430c3d02545fd7c10b0bd13e754b49f871b/README.md#L618-L620), [README.md#L611-L611](https://github.com/1jehuang/jcode/blob/37159430c3d02545fd7c10b0bd13e754b49f871b/README.md#L611-L611), [README.md#L609-L609](https://github.com/1jehuang/jcode/blob/37159430c3d02545fd7c10b0bd13e754b49f871b/README.md#L609-L609)
- [1jehuang/jcode](repos/1jehuang/jcode.md) [observation/documented] The side panel can display files updated in real time, receive agent-written content, act as a diff viewer, and render mermaid diagrams inline in both panel and chat. -- evidence: [README.md#L311-L312](https://github.com/1jehuang/jcode/blob/37159430c3d02545fd7c10b0bd13e754b49f871b/README.md#L311-L312)
- [21st-dev/1code](repos/21st-dev/1code.md) [observation/documented] 1Code is described as an open-source coding agent client for running Claude Code, Codex, and other coding agents locally or in the cloud. -- evidence: [README.md#L5-L5](https://github.com/21st-dev/1code/blob/9f1bc76fa4372c18c565b5a4f8daf38ae3595f0e/README.md#L5-L5)
- [21st-dev/1code](repos/21st-dev/1code.md) [observation/documented] Documented features include a Kanban board for visualizing agent sessions and a built-in Git client supporting staging, diffs, and pull request creation. -- evidence: [README.md#L11-L34](https://github.com/21st-dev/1code/blob/9f1bc76fa4372c18c565b5a4f8daf38ae3595f0e/README.md#L11-L34)
- ... 5881 more; see the full index above

## Patterns

Full index: [patterns/index.md](patterns/index.md).

- [101dotxyz/gpteam](repos/101dotxyz/gpteam.md) [observation/documented] Repository development practice: contributors are asked to fork the repository, create a branch, implement changes, and submit a pull request, which maintainers will review with feedback. -- evidence: [README.md#L73-L76](https://github.com/101dotxyz/GPTeam/blob/a216364ea2dbb208e6501468c5e5b791594cc3d5/README.md#L73-L76), [README.md#L78-L78](https://github.com/101dotxyz/GPTeam/blob/a216364ea2dbb208e6501468c5e5b791594cc3d5/README.md#L78-L78)
- [101dotxyz/gpteam](repos/101dotxyz/gpteam.md) [observation/documented] Discord setup requires channel IDs per location in .env as <LOCATION_NAME>_CHANNEL_ID and bot tokens as <BOT_FIRST_NAME>_DISCORD_TOKEN, with the announcer bot needing Message Content Intent enabled. -- evidence: [DISCORD.md#L11-L22](https://github.com/101dotxyz/GPTeam/blob/a216364ea2dbb208e6501468c5e5b791594cc3d5/DISCORD.md#L11-L22), [DISCORD.md#L33-L49](https://github.com/101dotxyz/GPTeam/blob/a216364ea2dbb208e6501468c5e5b791594cc3d5/DISCORD.md#L33-L49)
- [101dotxyz/gpteam](repos/101dotxyz/gpteam.md) [observation/documented] Agents move around the world, perform tasks in different locations depending on their activity and other agents' positions, and can speak to each other and collaborate on tasks in parallel. -- evidence: [README.md#L43-L43](https://github.com/101dotxyz/GPTeam/blob/a216364ea2dbb208e6501468c5e5b791594cc3d5/README.md#L43-L43)
- [1jehuang/jcode](repos/1jehuang/jcode.md) [observation/documented] Multiple agents spawned in the same repo are managed by a server: when one agent edits a file another has read, the server notifies the reader, which can ignore it or check the diff; agents can DM, broadcast, or message repo-scoped peers. -- evidence: [README.md#L330-L330](https://github.com/1jehuang/jcode/blob/37159430c3d02545fd7c10b0bd13e754b49f871b/README.md#L330-L330)
- [1jehuang/jcode](repos/1jehuang/jcode.md) [observation/documented] Skills are not all loaded at startup; embedding hits on the conversation inject relevant skills automatically, and skills can also be activated manually via a skill tool or slash commands. -- evidence: [README.md#L680-L680](https://github.com/1jehuang/jcode/blob/37159430c3d02545fd7c10b0bd13e754b49f871b/README.md#L680-L680)
- [1jehuang/jcode](repos/1jehuang/jcode.md) [observation/documented] Agents have a swarm tool to autonomously spawn teammates for parallel work, turning the main agent into a coordinator; groups, messaging channels, and completion statuses are managed automatically, headed or headless. -- evidence: [README.md#L342-L342](https://github.com/1jehuang/jcode/blob/37159430c3d02545fd7c10b0bd13e754b49f871b/README.md#L342-L342)
- [21st-dev/1code](repos/21st-dev/1code.md) [observation/documented] The README states automations can be triggered from GitHub, Linear, or Slack events, or run manually from git events. -- evidence: [README.md#L109-L109](https://github.com/21st-dev/1code/blob/9f1bc76fa4372c18c565b5a4f8daf38ae3595f0e/README.md#L109-L109)
- [21st-dev/1code](repos/21st-dev/1code.md) [observation/documented] Documentation states each chat session runs in its own isolated git worktree, and background agents execute in cloud sandboxes while the local machine sleeps. -- evidence: [README.md#L88-L88](https://github.com/21st-dev/1code/blob/9f1bc76fa4372c18c565b5a4f8daf38ae3595f0e/README.md#L88-L88), [README.md#L44-L48](https://github.com/21st-dev/1code/blob/9f1bc76fa4372c18c565b5a4f8daf38ae3595f0e/README.md#L44-L48)
- [21st-dev/1code](repos/21st-dev/1code.md) [observation/documented] Documented features include custom skills and slash commands, plus custom sub-agents shown with a visual task display in the sidebar. -- evidence: [README.md#L11-L34](https://github.com/21st-dev/1code/blob/9f1bc76fa4372c18c565b5a4f8daf38ae3595f0e/README.md#L11-L34)
- [233i/ore-code](repos/233i/ore-code.md) [observation/documented] Skills are user-level reusable workflow instructions stored at ~/.ore-code/skills/<skill-id>/SKILL.md; each skill auto-registers a slash command and its content is injected into the current prompt. -- evidence: [docs/06-skill-system.md#L7-L9](https://github.com/233i/ore-code/blob/b36da0c05720cd033af68bdda75bb79acc5c5010/docs/06-skill-system.md#L7-L9), [docs/06-skill-system.md#L24-L24](https://github.com/233i/ore-code/blob/b36da0c05720cd033af68bdda75bb79acc5c5010/docs/06-skill-system.md#L24-L24), [docs/06-skill-system.md#L3-L3](https://github.com/233i/ore-code/blob/b36da0c05720cd033af68bdda75bb79acc5c5010/docs/06-skill-system.md#L3-L3), [docs/06-skill-system.md#L30-L30](https://github.com/233i/ore-code/blob/b36da0c05720cd033af68bdda75bb79acc5c5010/docs/06-skill-system.md#L30-L30)
- [233i/ore-code](repos/233i/ore-code.md) [observation/documented] Skills are documentation-like instructions, not plugin code, and do not execute arbitrary scripts; actual file, shell, and git actions still go through existing tools and the approval system. -- evidence: [docs/06-skill-system.md#L3-L3](https://github.com/233i/ore-code/blob/b36da0c05720cd033af68bdda75bb79acc5c5010/docs/06-skill-system.md#L3-L3), [docs/06-skill-system.md#L30-L30](https://github.com/233i/ore-code/blob/b36da0c05720cd033af68bdda75bb79acc5c5010/docs/06-skill-system.md#L30-L30)
- [233i/ore-code](repos/233i/ore-code.md) [observation/documented] Repository development practice: contributors use Node 22 (pinned in .node-version), pnpm 11.x, Rust stable, and Tauri 2 prerequisites; local checks run via pnpm ci:local plus per-package test/typecheck/lint filters. -- evidence: [README.md#L106-L109](https://github.com/233i/ore-code/blob/b36da0c05720cd033af68bdda75bb79acc5c5010/README.md#L106-L109), [docs/API_AND_COMPATIBILITY.md#L92-L95](https://github.com/233i/ore-code/blob/b36da0c05720cd033af68bdda75bb79acc5c5010/docs/API_AND_COMPATIBILITY.md#L92-L95), [README.md#L91-L95](https://github.com/233i/ore-code/blob/b36da0c05720cd033af68bdda75bb79acc5c5010/README.md#L91-L95), [docs/API_AND_COMPATIBILITY.md#L97-L97](https://github.com/233i/ore-code/blob/b36da0c05720cd033af68bdda75bb79acc5c5010/docs/API_AND_COMPATIBILITY.md#L97-L97)
- [2389-research/2389-agent-rust](repos/2389-research/2389-agent-rust.md) [observation/documented] Documentation describes an explicit agent lifecycle moving through Uninitialized, Initializing, Running, Stopping and Stopped, with any state able to transition to an Error state on failure. -- evidence: [docs/ARCHITECTURE.md#L69-L72](https://github.com/2389-research/2389-agent-rust/blob/9ebe8438dbdb0a9566ef9ce4d6f492fc253db689/docs/ARCHITECTURE.md#L69-L72), [docs/ARCHITECTURE.md#L556-L560](https://github.com/2389-research/2389-agent-rust/blob/9ebe8438dbdb0a9566ef9ce4d6f492fc253db689/docs/ARCHITECTURE.md#L556-L560)
- [2389-research/binary-re](repos/2389-research/binary-re.md) [observation/documented] The case study records lessons for the skill: compare known inputs/outputs first, trace circular-buffer wrap-around carefully, and watch for divergent code paths implementing the same operation. -- evidence: [docs/bad-compression-analysis-2026-01-06.md#L124-L124](https://github.com/2389-research/binary-re/blob/42aee9063f3f3d52616700df3aa16df82b848604/docs/bad-compression-analysis-2026-01-06.md#L124-L124), [docs/bad-compression-analysis-2026-01-06.md#L122-L122](https://github.com/2389-research/binary-re/blob/42aee9063f3f3d52616700df3aa16df82b848604/docs/bad-compression-analysis-2026-01-06.md#L122-L122), [docs/bad-compression-analysis-2026-01-06.md#L126-L126](https://github.com/2389-research/binary-re/blob/42aee9063f3f3d52616700df3aa16df82b848604/docs/bad-compression-analysis-2026-01-06.md#L126-L126)
- [2389-research/binary-re](repos/2389-research/binary-re.md) [observation/documented] The plugin ships a 'binary-re' skill described as a structured RE workflow with hypothesis-driven analysis, driven by hypothesis-testing rather than blind exploration. -- evidence: [README.md#L16-L16](https://github.com/2389-research/binary-re/blob/42aee9063f3f3d52616700df3aa16df82b848604/README.md#L16-L16), [README.md#L3-L3](https://github.com/2389-research/binary-re/blob/42aee9063f3f3d52616700df3aa16df82b848604/README.md#L3-L3)
- ... 2539 more; see the full index above

## Features

Facet-major comparison (components, tools-permissions, memory-state, orchestration, evaluation and every other facet) across every repository: [features/index.md](features/index.md).


## Gaps

Full index: [gaps/index.md](gaps/index.md).

- [specifications](gaps/specifications.md): missing in 476 distilled repo(s)
- [components](gaps/components.md): missing in 225 distilled repo(s)
- [design-choices](gaps/design-choices.md): missing in 157 distilled repo(s)
- [workflows](gaps/workflows.md): missing in 233 distilled repo(s)
- [skills-patterns](gaps/skills-patterns.md): missing in 786 distilled repo(s)
- [interfaces](gaps/interfaces.md): missing in 98 distilled repo(s)
- [memory-state](gaps/memory-state.md): missing in 503 distilled repo(s)
- [orchestration](gaps/orchestration.md): missing in 537 distilled repo(s)
- [tools-permissions](gaps/tools-permissions.md): missing in 573 distilled repo(s)
- [evaluation](gaps/evaluation.md): missing in 764 distilled repo(s)
- [dependencies](gaps/dependencies.md): missing in 114 distilled repo(s)
- [limitations](gaps/limitations.md): missing in 348 distilled repo(s)
- [relevance](gaps/relevance.md): missing in 716 distilled repo(s)

## Freshness

Full index: [freshness/index.md](freshness/index.md).

- [0xpayne/gpt-migrate](repos/0xpayne/gpt-migrate.md): refresh-failed (FetchFailed)
- [agentsmesh/agentsmesh](repos/agentsmesh/agentsmesh.md): stale (stale)
- [agnusdei1207/opencode-orchestrator](repos/agnusdei1207/opencode-orchestrator.md): stale (stale)
- [ahacker-1/cre-acquisition-orchestrator](repos/ahacker-1/cre-acquisition-orchestrator.md): stale (stale)
- [ai4finance-foundation/finrobot](repos/ai4finance-foundation/finrobot.md): stale (stale)
- [aider-ai/aider](repos/aider-ai/aider.md): stale (stale)
- [airtai/fastagency](repos/airtai/fastagency.md): refresh-failed (FetchFailed)
- [aizen-stack/aizen](repos/aizen-stack/aizen.md): refresh-failed (FetchFailed)
- [aizenvoltprime/damocles](repos/aizenvoltprime/damocles.md): stale (stale)
- [akarachen/2code](repos/akarachen/2code.md): stale (stale)
- [akashgit/remote-factory](repos/akashgit/remote-factory.md): stale (stale)
- [alanchen4/summer-2024-swe-internships](repos/alanchen4/summer-2024-swe-internships.md): stale (stale)
- [alchaincyf/fanbox](repos/alchaincyf/fanbox.md): stale (stale)
- [alex-reysa/singular-lite](repos/alex-reysa/singular-lite.md): stale (stale)
- [alexgreensh/outsourcerer](repos/alexgreensh/outsourcerer.md): stale (stale)
- [alibaba/open-code-review](repos/alibaba/open-code-review.md): stale (stale)
- [alihamzaazam/repomon](repos/alihamzaazam/repomon.md): stale (stale)
- [almanaccode/codealmanac](repos/almanaccode/codealmanac.md): stale (stale)
- [almogdepaz/wolfpack](repos/almogdepaz/wolfpack.md): stale (stale)
- [alpbahadur/49agents](repos/alpbahadur/49agents.md): refresh-failed (FetchFailed)
- ... 58 more; see freshness/index.md

## Directory

Full index: [directory/index.md](directory/index.md).
Catalog-evidence entries (no-repo included): 1362 (published=833, backing=1347, pages=75).
