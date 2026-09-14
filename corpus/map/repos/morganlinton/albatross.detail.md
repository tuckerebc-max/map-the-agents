# morganlinton/albatross -- full detail

[Back to orientation](albatross.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/morganlinton/albatross/6f20178d81c6f0fdbb97ccf826b0d56f04a77faf/efa5ca6ad18bbc10.json](../../../wiki/dossiers/morganlinton/albatross/6f20178d81c6f0fdbb97ccf826b0d56f04a77faf/efa5ca6ad18bbc10.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (1 claim(s))

- [observation/documented] The agent talks to one provider at a time, but providers can be switched mid-session with /provider while tools, commands, and the session log stay unchanged; Ollama is the default provider. -- evidence: [README.md#L213-L213](https://github.com/morganlinton/Albatross/blob/6f20178d81c6f0fdbb97ccf826b0d56f04a77faf/README.md#L213-L213), [README.md#L135-L135](https://github.com/morganlinton/Albatross/blob/6f20178d81c6f0fdbb97ccf826b0d56f04a77faf/README.md#L135-L135), [README.md#L222-L223](https://github.com/morganlinton/Albatross/blob/6f20178d81c6f0fdbb97ccf826b0d56f04a77faf/README.md#L222-L223) (`clm_104a5121b42ac65e6501769453435fc6832556e16812cebc5ec71405cbc7905f`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: the README shows a GitHub Actions CI badge for the repository's ci.yml workflow, indicating automated CI runs on the project. -- evidence: [README.md#L19-L27](https://github.com/morganlinton/Albatross/blob/6f20178d81c6f0fdbb97ccf826b0d56f04a77faf/README.md#L19-L27) (`clm_06a561b957412edea50d5b34afd55116963c8fd64d61219c2bcf8a84db8f47fe`)

## skills-patterns (1 claim(s))

- [observation/documented] Albatross supports the open Agent Skills directory/frontmatter standard, discovering skills from project and user roots plus installed packages; only names and descriptions enter the initial prompt, with full instructions loaded on demand. -- evidence: [README.md#L832-L837](https://github.com/morganlinton/Albatross/blob/6f20178d81c6f0fdbb97ccf826b0d56f04a77faf/README.md#L832-L837) (`clm_1888bef8deb5d8db0e08c31706c228c2b77003987352aac9eeac7a629b5af2e8`)

## interfaces (2 claim(s))

- [observation/documented] Albatross is a terminal TUI coding agent launched via the `albatross` binary, with slash commands including /provider, /model, /plan, /ship, /undo, /auto, and `--continue` to resume the most recent session in the cwd. -- evidence: [README.md#L41-L45](https://github.com/morganlinton/Albatross/blob/6f20178d81c6f0fdbb97ccf826b0d56f04a77faf/README.md#L41-L45), [README.md#L419-L453](https://github.com/morganlinton/Albatross/blob/6f20178d81c6f0fdbb97ccf826b0d56f04a77faf/README.md#L419-L453), [README.md#L259-L278](https://github.com/morganlinton/Albatross/blob/6f20178d81c6f0fdbb97ccf826b0d56f04a77faf/README.md#L259-L278), [README.md#L125-L127](https://github.com/morganlinton/Albatross/blob/6f20178d81c6f0fdbb97ccf826b0d56f04a77faf/README.md#L125-L127) (`clm_169a5d896953bb4718358a2326a51ee6477c4cc6e10460db0f4dad53bc923e27`)
- [observation/documented] The tool surface includes read tools (file_read, grep, list_dir, glob, repo_search), approval-gated mutation tools (file_write, file_edit, apply_patch, batch_edit, shell), workflow tools such as run_tests and web_fetch, and MCP tools surfaced as mcp__<server>__<tool>. -- evidence: [README.md#L346-L351](https://github.com/morganlinton/Albatross/blob/6f20178d81c6f0fdbb97ccf826b0d56f04a77faf/README.md#L346-L351) (`clm_e1b2c7777481bb71b5fa25435a3fb99209ddb3456449508f2b36a986a72fd613`)

## memory-state (1 claim(s))

- [observation/documented] Session memory features include /index and /map for project memory, /remember and /forget for durable notes, /compact for in-place summarization, and /reset which writes a handoff artifact to .albatross/continue.md and starts a fresh session seeded only with it. -- evidence: [README.md#L690-L697](https://github.com/morganlinton/Albatross/blob/6f20178d81c6f0fdbb97ccf826b0d56f04a77faf/README.md#L690-L697), [README.md#L455-L470](https://github.com/morganlinton/Albatross/blob/6f20178d81c6f0fdbb97ccf826b0d56f04a77faf/README.md#L455-L470) (`clm_c43095695e7fb51ac011438e4a1b9b176b80be40736eff18437f0deed7a769b1`)

## orchestration (1 claim(s))

- [observation/documented] /plan route builds a low/medium/high task graph in .albatross/plan.json using a configurable planner model, and /plan execute runs ready tasks sequentially, switching backend/model per task, with --yolo for unattended auto-approval. -- evidence: [README.md#L636-L641](https://github.com/morganlinton/Albatross/blob/6f20178d81c6f0fdbb97ccf826b0d56f04a77faf/README.md#L636-L641), [README.md#L649-L651](https://github.com/morganlinton/Albatross/blob/6f20178d81c6f0fdbb97ccf826b0d56f04a77faf/README.md#L649-L651) (`clm_372a50951c15889a12c71a995249715fccdf0c21afba89ad3600cfad0a1c7747`)

## tools-permissions (2 claim(s))

- [observation/documented] Approval policies are always (default, prompts with diff preview), dangerous-only (prompts on non-obviously-safe mutations and strips hydrated API-key env vars from shell children), and never; per-prompt options include always-for-this-tool and session-allow for the exact call. -- evidence: [README.md#L361-L365](https://github.com/morganlinton/Albatross/blob/6f20178d81c6f0fdbb97ccf826b0d56f04a77faf/README.md#L361-L365), [README.md#L367-L368](https://github.com/morganlinton/Albatross/blob/6f20178d81c6f0fdbb97ccf826b0d56f04a77faf/README.md#L367-L368) (`clm_0aa5ee71275493ddc270b05e814695539f4c62ab8988f950459e13c9cc4c098d`)
- [observation/documented] MCP servers and extensions are executable programs that are not auto-spawned when new or changed; users must review and trust them, trust is stored per workspace and config hash, and their tool calls remain approval-gated by default. -- evidence: [README.md#L771-L776](https://github.com/morganlinton/Albatross/blob/6f20178d81c6f0fdbb97ccf826b0d56f04a77faf/README.md#L771-L776), [README.md#L780-L783](https://github.com/morganlinton/Albatross/blob/6f20178d81c6f0fdbb97ccf826b0d56f04a77faf/README.md#L780-L783), [README.md#L804-L807](https://github.com/morganlinton/Albatross/blob/6f20178d81c6f0fdbb97ccf826b0d56f04a77faf/README.md#L804-L807), [README.md#L762-L764](https://github.com/morganlinton/Albatross/blob/6f20178d81c6f0fdbb97ccf826b0d56f04a77faf/README.md#L762-L764) (`clm_3783a970a91bd025085e5a00090ede0952c975b4aba919c3a5026258cc897d46`)

## evaluation (2 claim(s))

- [observation/documented] /iterate runs a generate-evaluate loop where a separate read-only critic agent scores work 0-10 against a weighted rubric; the harness itself computes the weighted total and pass/fail, and an optional evaluator model can differ from the generator. -- evidence: [README.md#L676-L683](https://github.com/morganlinton/Albatross/blob/6f20178d81c6f0fdbb97ccf826b0d56f04a77faf/README.md#L676-L683), [README.md#L668-L674](https://github.com/morganlinton/Albatross/blob/6f20178d81c6f0fdbb97ccf826b0d56f04a77faf/README.md#L668-L674) (`clm_173a216713cb24d0d66f9771f92bab2b63d569a916bdc6d1445a0bd9f795e8aa`)
- [observation/documented] /auto repeats the iterate loop unattended with budget, deadline, round-ceiling, and stall-detection bounds, auto-fires /reset on context fill, and writes a report with verdict, per-round scores, criteria checklist, cost, and reset count. -- evidence: [README.md#L701-L705](https://github.com/morganlinton/Albatross/blob/6f20178d81c6f0fdbb97ccf826b0d56f04a77faf/README.md#L701-L705), [README.md#L728-L737](https://github.com/morganlinton/Albatross/blob/6f20178d81c6f0fdbb97ccf826b0d56f04a77faf/README.md#L728-L737), [README.md#L717-L726](https://github.com/morganlinton/Albatross/blob/6f20178d81c6f0fdbb97ccf826b0d56f04a77faf/README.md#L717-L726) (`clm_a3dca4499469dcfeab060e0021b7c4be17ade50d3ad8c4a7b25727a3cfee3579`)

## dependencies (1 claim(s))

- [observation/documented] Supported providers include Ollama, LM Studio, MLX, llama.cpp, OpenRouter, OpenAI, Anthropic, openai-codex (ChatGPT subscription OAuth), and grok (SuperGrok OAuth), each with documented default URLs and default models. -- evidence: [README.md#L284-L294](https://github.com/morganlinton/Albatross/blob/6f20178d81c6f0fdbb97ccf826b0d56f04a77faf/README.md#L284-L294), [README.md#L316-L326](https://github.com/morganlinton/Albatross/blob/6f20178d81c6f0fdbb97ccf826b0d56f04a77faf/README.md#L316-L326) (`clm_a3e2512549683fb2c1cf62f95632718471d5096ac69f5973029bb8e04443ac71`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

