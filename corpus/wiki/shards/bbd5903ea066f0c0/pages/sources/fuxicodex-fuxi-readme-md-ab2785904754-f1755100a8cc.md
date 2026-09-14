---
access: public
aliases: []
claim_ids:
- clm_1ed1e451ac0798b98b6ec6988e60c30f7fe95b1295ba005cb4d95d63a9a993da
- clm_5bb1f3847f4984638c76a18d3c27a8df1cddf1c5ee443a5c338165a44b9d0a38
- clm_639ee5fabe7c55abd2aa268bd6483507d749312f36ab51860a108e802933efe4
- clm_6920e1412e414365b7e7e3f04f6a409ff062ee2b2d8713a9ea02e329e5c722c7
- clm_69f246579dd0af64583445181b87e87579175c693e7815b8d8477d26624cf843
- clm_6e0c0c38c0c4e4d787c181c835eee9e04bc4f7681f58cab2beb5430df9300ac9
- clm_a300fbc4166ce220b18aafa906be1ee3ecccd6905726b07d1adadc51aaa8f197
- clm_ab8341aabfd3ebff291e36f706f043ee5f89a1b5f9cf9286ef4457378de024b1
- clm_b24b23ff187da7326df112088f851726de351373db6fce4bdcbec5194197115a
- clm_bd5f199b443d927b519e8170830ebb4e569be917b8e713abee7f7923d0a21f1e
- clm_d0e8c9ab428966612f3c83877527df401f3cedcfe59eb36b03befe04d55e2c91
- clm_de0125b1027710e4759bf0c58e9c6d1703e655f983fcad6e46a975fef87d011b
maturity: draft
page_id: pg_c373b30e1b0f566eb830f1755100a8cc
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_887f5d32422a594782426ff7e3450d9f
title: fuxicodex/Fuxi/README.md @ ab2785904754
updated_at: '2026-09-14T02:01:12Z'
---

# fuxicodex/Fuxi/README.md @ ab2785904754

<!-- rcw:begin owner=source:src_887f5d32422a594782426ff7e3450d9f block=evidence -->
- FuXi is documented as a terminal AI coding agent built in Go, shipped as a single static binary with no runtime dependencies, positioned as a provider-agnostic alternative to Claude Code. [@claim:clm_1ed1e451ac0798b98b6ec6988e60c30f7fe95b1295ba005cb4d95d63a9a993da]
- The README reports a self-run head-to-head benchmark against another coding agent using an objective pytest+coverage scorer across 15 micro and 4 large-project dimensions, and explicitly cautions it is a small, non-third-party task set measuring the agent loop. [@claim:clm_5bb1f3847f4984638c76a18d3c27a8df1cddf1c5ee443a5c338165a44b9d0a38]
- The agent is described as running a Think → Act → Verify loop: it reasons about a task, acts with built-in tools, inspects results, and iterates until the work is verified. [@claim:clm_639ee5fabe7c55abd2aa268bd6483507d749312f36ab51860a108e802933efe4]
- Sessions are described as durable: transcripts persist to disk, checkpoints allow resume, rollback, or fork, long conversations auto-compact, and an idle 'dreaming' pass consolidates memory across sessions. [@claim:clm_6920e1412e414365b7e7e3f04f6a409ff062ee2b2d8713a9ea02e329e5c722c7]
- Shell commands reportedly pass an AST safety classifier and rule set before execution, with fine-grained permissions and audit logging; permission modes are default, plan, and bypassPermissions, plus a classifier-gated --auto mode with a circuit breaker. [@claim:clm_69f246579dd0af64583445181b87e87579175c693e7815b8d8477d26624cf843]
- The product exposes a TUI with slash commands (/model, /config, /cost, /usage, /context, /compact, /permissions, /commit, /review, etc.) plus CLI subcommands such as fuxi doctor, verify, wizard, update, proxy, and mcp serve. [@claim:clm_6e0c0c38c0c4e4d787c181c835eee9e04bc4f7681f58cab2beb5430df9300ac9]
- The repository hosts only documentation, release installers, and the issue tracker; the product source is proprietary and not published here, under a proprietary license. [@claim:clm_a300fbc4166ce220b18aafa906be1ee3ecccd6905726b07d1adadc51aaa8f197]
- The project states it currently ships without published scores on third-party benchmarks such as SWE-bench or Terminal-Bench, and instead offers a do-it-yourself evaluation checklist plus in-TUI /cost, /usage, /context, and /status commands. [@claim:clm_ab8341aabfd3ebff291e36f706f043ee5f89a1b5f9cf9286ef4457378de024b1]
- Documentation describes cost-aware routing across LLM providers with automatic failover, a smart routing proxy (fuxi proxy), and fork agents with a default fork concurrency of 4 (FUXI_FORK_MAX_CONCURRENCY). [@claim:clm_b24b23ff187da7326df112088f851726de351373db6fce4bdcbec5194197115a]
- Documentation claims 50+ built-in tools including file read/write/edit, bash and PowerShell shell, ripgrep search, web fetch, LSP diagnostics, Jupyter, browser use, background tasks, and parallel sub-agents. [@claim:clm_bd5f199b443d927b519e8170830ebb4e569be917b8e713abee7f7923d0a21f1e]
- The agent is documented as provider-agnostic: it accepts any OpenAI-compatible endpoint, Gemini, Bedrock/Vertex keys, or FuXi OAuth login, and acts as an MCP client. [@claim:clm_d0e8c9ab428966612f3c83877527df401f3cedcfe59eb36b03befe04d55e2c91]
- Configuration resolves with precedence environment variables > ~/.fuxi/config.yaml > built-in defaults, and config changes are said to hot-reload while the agent runs. [@claim:clm_de0125b1027710e4759bf0c58e9c6d1703e655f983fcad6e46a975fef87d011b]
<!-- rcw:end owner=source:src_887f5d32422a594782426ff7e3450d9f block=evidence -->

## Researcher notes

