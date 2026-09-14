---
access: public
aliases: []
claim_ids:
- clm_0aeddd577efa6b777ee8fe7a5ce929cadb80943e8aaba05124e061d84b71abc8
- clm_0b89e239530f1af647e39fffff8a078322a46d63f022e131daf82699b93ffb2c
- clm_0fecf4359da23e32d684e4a579cc57934aef67c3cd9f8f0ceb129133c28ab3e7
- clm_208b61ed0cfb30564a8848adcf0a809b6a51df3395da1f07df1d1157d4abc78b
- clm_2c596ed9227d9f5f5c530f96af05829cf110889f277b6360f26c2d60f7777ec9
- clm_2f529893cb7f1f3f2aee96aedf55c04757de922a1d87e633f63feb1f0d15bfdb
- clm_3b2b5779f156ba13fabcabf542fc58bc8858d72c0a110e9eb05e516447c56dcd
- clm_41f22382a9a0abed077c9c38b70d07c54f6bc7dd173ccd3eea04958a9013a724
- clm_5b9b953b9bd2c7cfa9e70e584fb4a80b7c78136bb943a641d66181de05fb3f49
- clm_5ef96e5a3b53d406b86cec58595d15fa1ed35fa9663172307e5e075fb1733d63
- clm_623b7dbe686e15f9dacd4f08353698857d9c55f67d533f1d1a90efd470a9956c
- clm_69b007aad2bebb7a2f8eba8fe1737089ff6c55df340bd9a60a66e38efe552678
- clm_767ffd831c3bf3500fbbbb734af9e9237b98bddcf7c9dcca446fe9507e042743
- clm_da0fb545623e3264343a07cf90865aea83a308201e8369d02bc1b919c9d84a8f
maturity: draft
page_id: pg_a92eaa435f49520f99fd9ad62be2d313
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_671fe625baac55dcb29a2bcddf8366c8
title: ikamensh/kodo/README.md @ 51aebbfe5a30
updated_at: '2026-09-14T02:06:04Z'
---

# ikamensh/kodo/README.md @ 51aebbfe5a30

<!-- rcw:begin owner=source:src_671fe625baac55dcb29a2bcddf8366c8 block=evidence -->
- An orchestrator LLM delegates to a team of agents via tool calls; two implementations are described: ClaudeCodeOrchestrator (running on Claude Code with agents as MCP tools) and ApiOrchestrator on the Anthropic or Gemini API. [@claim:clm_0aeddd577efa6b777ee8fe7a5ce929cadb80943e8aaba05124e061d84b71abc8]
- Kodo targets Python 3.13+, is installed with uv (uv tool install kodo-agent), and requires at least one agent backend, with Claude Code plus one fast backend (Cursor, Codex, or Gemini CLI) recommended. [@claim:clm_0b89e239530f1af647e39fffff8a078322a46d63f022e131daf82699b93ffb2c]
- Four effort levels (low, standard, high, max) scale both orchestrator behavior and verification strictness, from basic test-passing checks up to skeptical rejection of technically correct but mediocre work. [@claim:clm_0fecf4359da23e32d684e4a579cc57934aef67c3cd9f8f0ceb129133c28ab3e7]
- Agents run with full permissions in bypassPermissions mode; they primarily work in the project directory but can access any file on the system, so users are advised to have a git commit or backup before launching. [@claim:clm_208b61ed0cfb30564a8848adcf0a809b6a51df3395da1f07df1d1157d4abc78b]
- Configuration flags include --team (full default, quick, test), --exchanges, --cycles, --orchestrator (api default, or claude-code/gemini-cli/codex/cursor), --orchestrator-model, --effort, --skip-intake, --auto-refine, --json, and --no-auto-commit. [@claim:clm_2c596ed9227d9f5f5c530f96af05829cf110889f277b6360f26c2d60f7777ec9]
- Runs are stored under ~/.kodo/runs/ and can be resumed by ID or as the latest incomplete run; test-mode coverage tracking persists in .kodo/test-coverage.md so repeated runs skip previously tested features. [@claim:clm_2f529893cb7f1f3f2aee96aedf55c04757de922a1d87e633f63feb1f0d15bfdb]
- Custom teams are defined via team.json with lookup order project-level .kodo/team.json then user-level ~/.kodo/teams/{name}.json; agent fields include backend, model, description, system_prompt, max_turns (default 15), timeout_s, chrome, and fallback_model. [@claim:clm_3b2b5779f156ba13fabcabf542fc58bc8858d72c0a110e9eb05e516447c56dcd]
- An API model is recommended as orchestrator over CLI coding tools because CLI agents tend to write code, micromanage, or go off-script, while a plain API model stays in a coordinator role that delegates. [@claim:clm_41f22382a9a0abed077c9c38b70d07c54f6bc7dd173ccd3eea04958a9013a724]
- A session is a stateful conversation with a backend that tracks token usage and supports reset; an agent combines a prompt, session, and turn budget, invoked as agent.run(task, project_dir). [@claim:clm_5b9b953b9bd2c7cfa9e70e584fb4a80b7c78136bb943a641d66181de05fb3f49]
- Work is structured hierarchically: a cycle is one unit of orchestrated work, a run spans multiple cycles with summaries bridging context, and stages are independently verifiable plan pieces that run sequentially or in parallel git worktrees. [@claim:clm_5ef96e5a3b53d406b86cec58595d15fa1ed35fa9663172307e5e075fb1733d63]
- The default team comprises an orchestrator plus architect, worker_smart, worker_fast, tester, and tester_browser agents, each with a distinct role such as code survey, implementation, testing, or browser-based UI testing. [@claim:clm_623b7dbe686e15f9dacd4f08353698857d9c55f67d533f1d1a90efd470a9956c]
- The API orchestrator expects a GOOGLE_API_KEY (Gemini, described as recommended) or ANTHROPIC_API_KEY (Claude alternative) set in .env or the environment. [@claim:clm_69b007aad2bebb7a2f8eba8fe1737089ff6c55df340bd9a60a66e38efe552678]
- A published 100-task head-to-head benchmark using the same underlying model (Cursor composer-1.5) reports that adding Kodo's orchestration layer solves 24% more real-world GitHub issues, with methodology and interactive results available online. [@claim:clm_767ffd831c3bf3500fbbbb734af9e9237b98bddcf7c9dcca446fe9507e042743]
- Cost tracking separates an API bucket of real pay-per-token spend (e.g. ~$0.13/run for a Gemini Flash orchestrator) from a Virtual bucket showing what subscription-covered worker usage would have cost, which is not actually charged. [@claim:clm_da0fb545623e3264343a07cf90865aea83a308201e8369d02bc1b919c9d84a8f]
<!-- rcw:end owner=source:src_671fe625baac55dcb29a2bcddf8366c8 block=evidence -->

## Researcher notes

