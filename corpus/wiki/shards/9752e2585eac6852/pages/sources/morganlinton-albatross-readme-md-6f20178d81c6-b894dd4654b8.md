---
access: public
aliases: []
claim_ids:
- clm_06a561b957412edea50d5b34afd55116963c8fd64d61219c2bcf8a84db8f47fe
- clm_0aa5ee71275493ddc270b05e814695539f4c62ab8988f950459e13c9cc4c098d
- clm_104a5121b42ac65e6501769453435fc6832556e16812cebc5ec71405cbc7905f
- clm_169a5d896953bb4718358a2326a51ee6477c4cc6e10460db0f4dad53bc923e27
- clm_173a216713cb24d0d66f9771f92bab2b63d569a916bdc6d1445a0bd9f795e8aa
- clm_1888bef8deb5d8db0e08c31706c228c2b77003987352aac9eeac7a629b5af2e8
- clm_372a50951c15889a12c71a995249715fccdf0c21afba89ad3600cfad0a1c7747
- clm_3783a970a91bd025085e5a00090ede0952c975b4aba919c3a5026258cc897d46
- clm_a3dca4499469dcfeab060e0021b7c4be17ade50d3ad8c4a7b25727a3cfee3579
- clm_a3e2512549683fb2c1cf62f95632718471d5096ac69f5973029bb8e04443ac71
- clm_c43095695e7fb51ac011438e4a1b9b176b80be40736eff18437f0deed7a769b1
- clm_e1b2c7777481bb71b5fa25435a3fb99209ddb3456449508f2b36a986a72fd613
maturity: draft
page_id: pg_353634ee9b325202bc8db894dd4654b8
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_5664aa6a6ad353fcbf3ec91e36d43a8b
title: morganlinton/Albatross/README.md @ 6f20178d81c6
updated_at: '2026-09-14T02:20:20Z'
---

# morganlinton/Albatross/README.md @ 6f20178d81c6

<!-- rcw:begin owner=source:src_5664aa6a6ad353fcbf3ec91e36d43a8b block=evidence -->
- Repository development practice: the README shows a GitHub Actions CI badge for the repository's ci.yml workflow, indicating automated CI runs on the project. [@claim:clm_06a561b957412edea50d5b34afd55116963c8fd64d61219c2bcf8a84db8f47fe]
- Approval policies are always (default, prompts with diff preview), dangerous-only (prompts on non-obviously-safe mutations and strips hydrated API-key env vars from shell children), and never; per-prompt options include always-for-this-tool and session-allow for the exact call. [@claim:clm_0aa5ee71275493ddc270b05e814695539f4c62ab8988f950459e13c9cc4c098d]
- The agent talks to one provider at a time, but providers can be switched mid-session with /provider while tools, commands, and the session log stay unchanged; Ollama is the default provider. [@claim:clm_104a5121b42ac65e6501769453435fc6832556e16812cebc5ec71405cbc7905f]
- Albatross is a terminal TUI coding agent launched via the `albatross` binary, with slash commands including /provider, /model, /plan, /ship, /undo, /auto, and `--continue` to resume the most recent session in the cwd. [@claim:clm_169a5d896953bb4718358a2326a51ee6477c4cc6e10460db0f4dad53bc923e27]
- /iterate runs a generate-evaluate loop where a separate read-only critic agent scores work 0-10 against a weighted rubric; the harness itself computes the weighted total and pass/fail, and an optional evaluator model can differ from the generator. [@claim:clm_173a216713cb24d0d66f9771f92bab2b63d569a916bdc6d1445a0bd9f795e8aa]
- Albatross supports the open Agent Skills directory/frontmatter standard, discovering skills from project and user roots plus installed packages; only names and descriptions enter the initial prompt, with full instructions loaded on demand. [@claim:clm_1888bef8deb5d8db0e08c31706c228c2b77003987352aac9eeac7a629b5af2e8]
- /plan route builds a low/medium/high task graph in .albatross/plan.json using a configurable planner model, and /plan execute runs ready tasks sequentially, switching backend/model per task, with --yolo for unattended auto-approval. [@claim:clm_372a50951c15889a12c71a995249715fccdf0c21afba89ad3600cfad0a1c7747]
- MCP servers and extensions are executable programs that are not auto-spawned when new or changed; users must review and trust them, trust is stored per workspace and config hash, and their tool calls remain approval-gated by default. [@claim:clm_3783a970a91bd025085e5a00090ede0952c975b4aba919c3a5026258cc897d46]
- /auto repeats the iterate loop unattended with budget, deadline, round-ceiling, and stall-detection bounds, auto-fires /reset on context fill, and writes a report with verdict, per-round scores, criteria checklist, cost, and reset count. [@claim:clm_a3dca4499469dcfeab060e0021b7c4be17ade50d3ad8c4a7b25727a3cfee3579]
- Supported providers include Ollama, LM Studio, MLX, llama.cpp, OpenRouter, OpenAI, Anthropic, openai-codex (ChatGPT subscription OAuth), and grok (SuperGrok OAuth), each with documented default URLs and default models. [@claim:clm_a3e2512549683fb2c1cf62f95632718471d5096ac69f5973029bb8e04443ac71]
- Session memory features include /index and /map for project memory, /remember and /forget for durable notes, /compact for in-place summarization, and /reset which writes a handoff artifact to .albatross/continue.md and starts a fresh session seeded only with it. [@claim:clm_c43095695e7fb51ac011438e4a1b9b176b80be40736eff18437f0deed7a769b1]
- The tool surface includes read tools (file_read, grep, list_dir, glob, repo_search), approval-gated mutation tools (file_write, file_edit, apply_patch, batch_edit, shell), workflow tools such as run_tests and web_fetch, and MCP tools surfaced as mcp__<server>__<tool>. [@claim:clm_e1b2c7777481bb71b5fa25435a3fb99209ddb3456449508f2b36a986a72fd613]
<!-- rcw:end owner=source:src_5664aa6a6ad353fcbf3ec91e36d43a8b block=evidence -->

## Researcher notes

