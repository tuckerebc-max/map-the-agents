---
access: public
aliases: []
claim_ids:
- clm_2506f3760d21790b78e79a536b1df6b4ffaf9b10a90ef6d50a5d4899d145654d
- clm_2f84f79da3b7f08884a863316b15a868cfeb3dda1bfce71a73c48c3b9d433314
- clm_3e246b954b17fa93a5670fdee46e75c9abea19882b34dab410de035246cc4b69
- clm_3f51c8db2f96792df3085cbd9ca4e15323f1901c342e5b731effe227f7073c59
- clm_432f38c4b48e5bf8e59d8b87c457fcc541fafc44cbac73cecf848b5f65b3c096
- clm_4b740e0958e20047e17b08aefca28b37a00abbe27d9e448ca512a951c382245e
- clm_54425624ae99a6b8f67a11f24dcedf05ef98b39fc502ad75da0eb3377a612977
- clm_62a5a93b1a9eb60b491d21222c93b7a613ef762eaeb3428e0ec4d66a1fd0673a
- clm_6394afb89232ba46b0a8601d724746e1bc40f8dac9916e3b62a947931fa9216b
- clm_6e6363796a33158f598348065271ff381c71586e9ba15dd5008ce0ce1cd5fdbf
- clm_74fab8916439f59f05415b28a2365c0352bf9f8415861c178e61408681fbce43
- clm_af0207da03e839f2609cd2559e85bcb0242ce2e02198bde1bc1f3781ee76cbd3
- clm_b37dfe1e1393fe26aa5e304d898aa9a6bac9884692ba73d0f35bd89d1626a259
- clm_bd655c4936ebddb4338111f5b4d615e7a7d0b8cedf41645f0d69ab97e2189a78
- clm_cb2e7fb682d74f0ca2ad7867898dc6818d3a3019216732debeaafbafbaea9e06
- clm_d508f7eba59a1b2a3ca8277e5f2c687e017b9f685918b6ba6617dc5c8a6de9c2
- clm_d79326fbc0e435186e89e19645c5156004dd3aa2080e485e94d07be2fd6e54bc
- clm_e2f41f85cb3c99c109f1481cb7327d019dc8a43c6adba8a759415c1ff2638cd5
- clm_ef39f17872b5d8387855093fa8aeeead6dbe718c0cb235f6c031481752ff5f51
- clm_f24e641bfb986ef1fb831eec1527569fe60d1f6e336b62d6a2b4987c22891b9f
maturity: draft
page_id: pg_7c98445220c0599fb4b02c1ccc0f523d
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_11694459cc3d53ff937ab5c48dd8a12a
title: intellegix/intellegix-code-agent-toolkit/README.md @ 852325000c29
updated_at: '2026-09-14T03:59:40Z'
---

# intellegix/intellegix-code-agent-toolkit/README.md @ 852325000c29

<!-- rcw:begin owner=source:src_11694459cc3d53ff937ab5c48dd8a12a block=evidence -->
- The loop never edits CLAUDE.md itself; the human operator revises it between runs as the project's source of truth, retaining editorial control. [@claim:clm_2506f3760d21790b78e79a536b1df6b4ffaf9b10a90ef6d50a5d4899d145654d]
- The toolkit requires Claude Code CLI, Python 3.11+ for the loop and council automation, Node.js 18+ for the browser bridge, and optionally a Perplexity Pro/Max subscription for research features. [@claim:clm_2f84f79da3b7f08884a863316b15a868cfeb3dda1bfce71a73c48c3b9d433314]
- The loop driver invokes Claude Code CLI with stream-json output and --resume for session continuity, parsing NDJSON events (init, assistant, result, system) to extract cost, turns, and completion markers. [@claim:clm_3e246b954b17fa93a5670fdee46e75c9abea19882b34dab410de035246cc4b69]
- The loop driver exposes CLI flags including --project, --max-iterations, --max-cost, --dry-run, --smoke-test, --model, --timeout, and --verbose. [@claim:clm_3f51c8db2f96792df3085cbd9ca4e15323f1901c342e5b731effe227f7073c59]
- The MCP browser bridge is a WebSocket link between Claude Code and a Chrome extension, with the extension auto-connecting to ws://127.0.0.1:8765 and servers configured in mcp.json rather than settings.json. [@claim:clm_432f38c4b48e5bf8e59d8b87c457fcc541fafc44cbac73cecf848b5f65b3c096]
- Three orchestrator commands cover greenfield bootstrapping, single-loop execution, and multi-agent parallel work via git worktrees; all enforce role separation so the orchestrator writes instructions without touching source code. [@claim:clm_4b740e0958e20047e17b08aefca28b37a00abbe27d9e448ca512a951c382245e]
- Portfolio governance defines a four-tier project system (T1 Production through T4 Archive) allocating effort percentages and constraining testing, CI, and monitoring per tier. [@claim:clm_54425624ae99a6b8f67a11f24dcedf05ef98b39fc502ad75da0eb3377a612977]
- The log_redactor.py module scrubs API keys from log output, secrets load from environment variables, and session cookie files are excluded from git. [@claim:clm_62a5a93b1a9eb60b491d21222c93b7a613ef762eaeb3428e0ec4d66a1fd0673a]
- The toolkit provides 31 custom slash commands, authored as plain markdown files in ~/.claude/commands/ with $ARGUMENTS substitution at invocation time. [@claim:clm_6394afb89232ba46b0a8601d724746e1bc40f8dac9916e3b62a947931fa9216b]
- The loop driver runs Claude Code with --dangerously-skip-permissions for autonomous operation, and the README warns users to understand the implications before using it. [@claim:clm_6e6363796a33158f598348065271ff381c71586e9ba15dd5008ce0ce1cd5fdbf]
- The /frontend-e2e command runs browser-based end-to-end tests in seven tiers covering rendering, accessibility, visual/UX, navigation, responsive breakpoints, interactivity, and performance, producing pass/fail reports with failure screenshots. [@claim:clm_74fab8916439f59f05415b28a2365c0352bf9f8415861c178e61408681fbce43]
- Claude Code settings.json supports allow/deny permission lists using Tool(pattern) syntax, with deny rules taking precedence over allow rules. [@claim:clm_af0207da03e839f2609cd2559e85bcb0242ce2e02198bde1bc1f3781ee76cbd3]
- The loop driver includes model-aware scaling (Opus gets 2x timeout and a 25-turn cap), Opus-to-Sonnet fallback after two consecutive timeouts, exponential backoff, stagnation detection, and per-iteration plus cumulative budget enforcement. [@claim:clm_b37dfe1e1393fe26aa5e304d898aa9a6bac9884692ba73d0f35bd89d1626a259]
- Failed research queries retry up to 3 times with exponential backoff and jitter, and a circuit breaker pauses research for 120 seconds after 5 consecutive failures. [@claim:clm_bd655c4936ebddb4338111f5b4d615e7a7d0b8cedf41645f0d69ab97e2189a78]
- Perplexity integration works by browser automation using cached session cookies (24h TTL) instead of an API key, typing /council, /research, and /labs shortcuts that users must create in Perplexity settings. [@claim:clm_cb2e7fb682d74f0ca2ad7867898dc6818d3a3019216732debeaafbafbaea9e06]
- The toolkit ships an automated loop driver (loop_driver.py with NDJSON parser, state tracker, research bridge, and log redactor), agent definitions, hooks, slash commands, council automation, and an MCP browser bridge. [@claim:clm_d508f7eba59a1b2a3ca8277e5f2c687e017b9f685918b6ba6617dc5c8a6de9c2]
- A SessionSemaphore caps browser concurrency at 3 slots, and 4+ simultaneous queries on one account may still hit Perplexity's own session limits. [@claim:clm_d79326fbc0e435186e89e19645c5156004dd3aa2080e485e94d07be2fd6e54bc]
- The loop exits with coded statuses: 0 for completion, 1 for max iterations, 2 for budget exceeded, and 3 for stagnation. [@claim:clm_e2f41f85cb3c99c109f1481cb7327d019dc8a43c6adba8a759415c1ff2638cd5]
- Orchestrator activation writes a sentinel file (.workflow/orchestrator-mode.json, 24-hour expiry) and a PreToolUse hook blocks source-file access while allowing CLAUDE.md, BLUEPRINT.md, markdown, and .workflow files; the hook is fail-open when no sentinel exists. [@claim:clm_ef39f17872b5d8387855093fa8aeeead6dbe718c0cb235f6c031481752ff5f51]
- The loop persists state under <project>/.workflow/: state.json with cycle history, append-only trace.jsonl events, metrics_summary.json on exit, and research_result.md. [@claim:clm_f24e641bfb986ef1fb831eec1527569fe60d1f6e336b62d6a2b4987c22891b9f]
<!-- rcw:end owner=source:src_11694459cc3d53ff937ab5c48dd8a12a block=evidence -->

## Researcher notes

