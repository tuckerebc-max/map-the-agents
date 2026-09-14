---
access: public
aliases: []
claim_ids:
- clm_1153a4567aec63fd56e8be5a7dd02c17e75fd2e75c08868e4254c1b62812af99
- clm_20d068f8e1cc00d3c29622ac36ed14acbac868546f854d3defa14d68c512b99a
- clm_2ad387874998c477d65e534b082df5c31930a6f284ae3fa473681a04188e59af
- clm_33b52fd12413901b72a930d99ec0b3a6fb790c9f23501134f7fb474d98d3f506
- clm_432a5f146be6dfa7357a70ab0968d76a9d30e955e7d1a768ac4eae3b442bfa4e
- clm_658acd5967d19269261de486795c819c53fbd3ce86521543847477224059ec5b
- clm_721a26cbe454ea51cd3886d428dd9aa26b99ebcd449bae9258ea426ec338d9e8
- clm_75ea4fe2e40dac035fe3fb43623545ee8ca4d97c38e4839f6114275d94f1e545
- clm_82abca4e5a09be83ec4f3a4e34c315073c324ad2d1cb545e7908398138ab7318
- clm_e84ccf9c333cc2fd9e51fd973c59808460c778a86ea5c652c65a1f9f9d0081fe
- clm_f1bde8ef6a719c03ac9426124604535b8752b557e99fda47e06b319acc6d4e02
maturity: draft
page_id: pg_a0e4271cb81a584c905effc487aaf6e8
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_d065bd85d7505ba6802d09640821a8d4
title: cfal/garcon/README.md @ 42a5322794a9
updated_at: '2026-09-14T01:39:41Z'
---

# cfal/garcon/README.md @ 42a5322794a9

<!-- rcw:begin owner=source:src_d065bd85d7505ba6802d09640821a8d4 block=evidence -->
- Running Garcon requires Bun, git, and a modern browser, plus at least one coding agent or API provider; optional pull-request support needs an authenticated GitHub CLI on the host. [@claim:clm_1153a4567aec63fd56e8be5a7dd02c17e75fd2e75c08868e4254c1b62812af99]
- Garcon supports Claude Code, Codex, Cursor Agent, OpenCode, Amp, Factory Droid, and Pi as coding agents, plus direct Anthropic Messages and OpenAI Responses/Chat Completions compatible endpoints and provider presets like Ollama and OpenRouter. [@claim:clm_20d068f8e1cc00d3c29622ac36ed14acbac868546f854d3defa14d68c512b99a]
- A CLI drives visible Garcon chats through a running server, supporting catalog discovery, sync/detached starts and resumes, steering, status, transcript search and reads, export, handoff, and stop controls. [@claim:clm_2ad387874998c477d65e534b082df5c31930a6f284ae3fa473681a04188e59af]
- A companion garcon-skills package exposes the control plane to skill-aware agents via skills like garcon-captain, garcon-agent, garcon-task, garcon-message, garcon-schedule, and garcon-amp, installed with a link.sh script. [@claim:clm_33b52fd12413901b72a930d99ec0b3a6fb790c9f23501134f7fb474d98d3f506]
- The web UI is served at http://127.0.0.1:8080 by default; first launch requires creating an account at /setup, and authentication is enabled by default. [@claim:clm_432a5f146be6dfa7357a70ab0968d76a9d30e955e7d1a768ac4eae3b442bfa4e]
- The CLI is invoked as `bun cli/main.ts --workspace <name>` with subcommands such as start-async, search, read, status, and resume-async, including flags like --parent, --agent, --model, and --permissions. [@claim:clm_658acd5967d19269261de486795c819c53fbd3ce86521543847477224059ec5b]
- Garcon does not sandbox agents or their commands, which run on the host under the user's account; the README warns against exposing an unauthenticated instance to an untrusted network. [@claim:clm_721a26cbe454ea51cd3886d428dd9aa26b99ebcd449bae9258ea426ec338d9e8]
- Tickets persist in the workspace's tickets.sqlite, independent of chats and transcripts; a damaged or unknown-schema store is left unavailable for explicit recovery rather than rebuilt from transcripts. [@claim:clm_75ea4fe2e40dac035fe3fb43623545ee8ca4d97c38e4839f6114275d94f1e545]
- Model names may carry a `[Nk]` suffix (100-1000, thousands of tokens) that sets a per-chat Claude auto-compaction window; the annotation overrides CLAUDE_CODE_AUTO_COMPACT_WINDOW for that child process only and requires Claude Code 2.1.238+. [@claim:clm_82abca4e5a09be83ec4f3a4e34c315073c324ad2d1cb545e7908398138ab7318]
- The repository is organized into a SvelteKit/Svelte 5 frontend (web/), a Bun server handling chat lifecycle, providers, Git, auth, and notifications (server/), agent-specific runtimes (server-agents/), shared contracts (common/), and black-box integration tests. [@claim:clm_e84ccf9c333cc2fd9e51fd973c59808460c778a86ea5c652c65a1f9f9d0081fe]
- Chats can exchange provenance-labeled messages, launch delegated child chats, and receive their final results while keeping parentage auditable; the workspace tiles up to four resizable windows and tracks lineage in Chat Map. [@claim:clm_f1bde8ef6a719c03ac9426124604535b8752b557e99fda47e06b319acc6d4e02]
<!-- rcw:end owner=source:src_d065bd85d7505ba6802d09640821a8d4 block=evidence -->

## Researcher notes

