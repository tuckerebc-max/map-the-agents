# ochyai/vibe-local -- full detail

[Back to orientation](vibe-local.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/ochyai/vibe-local/5ea328e201c1163cf8c264d8109fbcfdde81cc53/e19e0d0faae6df51.json](../../../wiki/dossiers/ochyai/vibe-local/5ea328e201c1163cf8c264d8109fbcfdde81cc53/e19e0d0faae6df51.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (3 claim(s))

- [observation/documented] The v2 launcher detects RAM, selects a model, creates num_ctx-baked Ollama aliases (vibe-coder/vibe-fast) via ollama create, and generates OpenCode config without modifying the user's own OpenCode settings. -- evidence: [README.md#L421-L433](https://github.com/ochyai/vibe-local/blob/5ea328e201c1163cf8c264d8109fbcfdde81cc53/README.md#L421-L433), [README.md#L545-L549](https://github.com/ochyai/vibe-local/blob/5ea328e201c1163cf8c264d8109fbcfdde81cc53/README.md#L545-L549) (`clm_61debc578af8a46ea49bd1cec4babad65aaa2d4da34e6e2ae374d01bc452d735`)
- [observation/documented] An optional built-in Python engine, vibe-coder.py, is dependency-free (stdlib only), talks directly to Ollama's /api/chat with a tool-execution loop, and can run standalone via python3. -- evidence: [RELEASE_NOTES.md#L62-L69](https://github.com/ochyai/vibe-local/blob/5ea328e201c1163cf8c264d8109fbcfdde81cc53/RELEASE_NOTES.md#L62-L69), [README.md#L441-L443](https://github.com/ochyai/vibe-local/blob/5ea328e201c1163cf8c264d8109fbcfdde81cc53/README.md#L441-L443), [README.md#L454-L455](https://github.com/ochyai/vibe-local/blob/5ea328e201c1163cf8c264d8109fbcfdde81cc53/README.md#L454-L455) (`clm_9e908bb8989964a439f8341c3f587d050c804d465c68b6da9f49dfa1a2e610cf`)
- [observation/documented] A minimal passthrough router (vibe-router) classifies input: greetings and short questions go to a small model for fast replies, while coding and tool-use requests go to a larger model; --no-router disables it. -- evidence: [README.md#L34-L40](https://github.com/ochyai/vibe-local/blob/5ea328e201c1163cf8c264d8109fbcfdde81cc53/README.md#L34-L40), [README.md#L114-L116](https://github.com/ochyai/vibe-local/blob/5ea328e201c1163cf8c264d8109fbcfdde81cc53/README.md#L114-L116) (`clm_a602615b4d36e08eab0519541858deb2b955ff66ba4f311d9150c480d16e5374`)

## design-choices (2 claim(s))

- [observation/documented] v2 dropped the custom Anthropic-to-Ollama conversion proxy because Ollama natively implements the Anthropic Messages API (v0.14+); the old proxy and MLX server were archived under legacy/. -- evidence: [README.md#L435-L437](https://github.com/ochyai/vibe-local/blob/5ea328e201c1163cf8c264d8109fbcfdde81cc53/README.md#L435-L437), [README.md#L44-L49](https://github.com/ochyai/vibe-local/blob/5ea328e201c1163cf8c264d8109fbcfdde81cc53/README.md#L44-L49) (`clm_9f562d743490fe4f909de449b1708f574db2f4e725259b737ecd4467f584247d`)
- [observation/documented] The TUI uses a VT100 DECSTBM scroll region so AI output scrolls above a fixed three-row footer, with a store-only update pattern, non-blocking resize locking, and single-syscall atomic writes. -- evidence: [RELEASE_NOTES.md#L22-L26](https://github.com/ochyai/vibe-local/blob/5ea328e201c1163cf8c264d8109fbcfdde81cc53/RELEASE_NOTES.md#L22-L26), [RELEASE_NOTES.md#L9-L9](https://github.com/ochyai/vibe-local/blob/5ea328e201c1163cf8c264d8109fbcfdde81cc53/RELEASE_NOTES.md#L9-L9), [RELEASE_NOTES.md#L96-L99](https://github.com/ochyai/vibe-local/blob/5ea328e201c1163cf8c264d8109fbcfdde81cc53/RELEASE_NOTES.md#L96-L99) (`clm_0a459826bd51137c6203a8929641ebb3fd3262bfadd38512c897a16a36458eba`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: release notes report 780 unit tests plus 7 PTY integration tests (787 total) for vibe-coder.py, stated to pass on macOS, Linux, and Windows WSL. -- evidence: [RELEASE_NOTES.md#L62-L69](https://github.com/ochyai/vibe-local/blob/5ea328e201c1163cf8c264d8109fbcfdde81cc53/RELEASE_NOTES.md#L62-L69), [RELEASE_NOTES.md#L102-L105](https://github.com/ochyai/vibe-local/blob/5ea328e201c1163cf8c264d8109fbcfdde81cc53/RELEASE_NOTES.md#L102-L105) (`clm_05c7220d696492261aabbc848875da9f160633de7f67e8e88bd6844d2857e757`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] Inside the TUI, /theme switches themes, Tab toggles Plan/Build mode, and /models (or --no-router) pins a specific model instead of the default vibe-auto routing. -- evidence: [README.md#L375-L375](https://github.com/ochyai/vibe-local/blob/5ea328e201c1163cf8c264d8109fbcfdde81cc53/README.md#L375-L375), [README.md#L276-L276](https://github.com/ochyai/vibe-local/blob/5ea328e201c1163cf8c264d8109fbcfdde81cc53/README.md#L276-L276), [README.md#L112-L112](https://github.com/ochyai/vibe-local/blob/5ea328e201c1163cf8c264d8109fbcfdde81cc53/README.md#L112-L112), [README.md#L114-L116](https://github.com/ochyai/vibe-local/blob/5ea328e201c1163cf8c264d8109fbcfdde81cc53/README.md#L114-L116) (`clm_d7fd930642459020233e85abbc1ee22de9902f83422b16aae6f52f6f39eb5842`)

## memory-state (2 claim(s))

- [observation/documented] vibe-coder.py supports local RAG using sqlite3 and Ollama embeddings to inject relevant codebase context into the system prompt, with the index stored in .vibe/rag/ and tunable top-k and embedding model. -- evidence: [README.md#L445-L452](https://github.com/ochyai/vibe-local/blob/5ea328e201c1163cf8c264d8109fbcfdde81cc53/README.md#L445-L452) (`clm_f2841605c081213a93ef8fbabcf14f3b464c0c3d83c49ccdfc2055a68cf7cafd`)
- [observation/documented] Sessions are persisted as JSONL with resume support via --resume and --session-id, plus context compaction, per the implementation status table. -- evidence: [ROADMAP.md#L17-L45](https://github.com/ochyai/vibe-local/blob/5ea328e201c1163cf8c264d8109fbcfdde81cc53/ROADMAP.md#L17-L45) (`clm_14d1488ab0d87fb8574c1fbbb6ce81a5c3506562180ea6005e689d6ccbafcf89`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (2 claim(s))

- [observation/documented] v2 defaults to ask-before-every-action mode where the AI requests permission before file edits or command execution; the -y flag enables auto-approval of file writes, commands, and system changes. -- evidence: [README.md#L528-L529](https://github.com/ochyai/vibe-local/blob/5ea328e201c1163cf8c264d8109fbcfdde81cc53/README.md#L528-L529), [README.md#L463-L465](https://github.com/ochyai/vibe-local/blob/5ea328e201c1163cf8c264d8109fbcfdde81cc53/README.md#L463-L465), [README.md#L511-L512](https://github.com/ochyai/vibe-local/blob/5ea328e201c1163cf8c264d8109fbcfdde81cc53/README.md#L511-L512) (`clm_a9a730c1631d4d5e469657a2f20a26ba54c99d36faab95a1fcfac6118a7f33b0`)
- [observation/documented] The vibe-coder engine includes a permission manager with safe/ask/deny tiers, and its approval prompt accepts Japanese, English, and Chinese yes, falling back to /dev/tty when stdin is not a TTY. -- evidence: [ROADMAP.md#L17-L45](https://github.com/ochyai/vibe-local/blob/5ea328e201c1163cf8c264d8109fbcfdde81cc53/ROADMAP.md#L17-L45), [README.md#L445-L452](https://github.com/ochyai/vibe-local/blob/5ea328e201c1163cf8c264d8109fbcfdde81cc53/README.md#L445-L452) (`clm_704b7611469125e0fafd703bebb82ce6d01ab6c53742b81871c0f9b7691475f4`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The stack depends on Ollama, RAM-tiered local LLMs (qwen3-coder-next, qwen3.6:35b-a3b, gpt-oss:20b, qwen3.5:4b), and the OpenCode TUI; opencode is installed via brew if missing. -- evidence: [README.md#L120-L126](https://github.com/ochyai/vibe-local/blob/5ea328e201c1163cf8c264d8109fbcfdde81cc53/README.md#L120-L126), [README.md#L304-L307](https://github.com/ochyai/vibe-local/blob/5ea328e201c1163cf8c264d8109fbcfdde81cc53/README.md#L304-L307), [README.md#L144-L147](https://github.com/ochyai/vibe-local/blob/5ea328e201c1163cf8c264d8109fbcfdde81cc53/README.md#L144-L147), [README.md#L44-L49](https://github.com/ochyai/vibe-local/blob/5ea328e201c1163cf8c264d8109fbcfdde81cc53/README.md#L44-L49), [README.md#L280-L286](https://github.com/ochyai/vibe-local/blob/5ea328e201c1163cf8c264d8109fbcfdde81cc53/README.md#L280-L286) (`clm_067d82d1870ff6d40ea6f442b39855320867304920d588576cc0c9774be73ea1`)

## limitations (2 claim(s))

- [observation/documented] The README warns that local LLMs are less accurate than cloud AI and may unintentionally run dangerous commands, advising users to reject sudo, chmod/chown, dd/mkfs//dev/, config-overwriting redirects, and --force flags. -- evidence: [README.md#L467-L467](https://github.com/ochyai/vibe-local/blob/5ea328e201c1163cf8c264d8109fbcfdde81cc53/README.md#L467-L467), [README.md#L516-L517](https://github.com/ochyai/vibe-local/blob/5ea328e201c1163cf8c264d8109fbcfdde81cc53/README.md#L516-L517), [README.md#L473-L480](https://github.com/ochyai/vibe-local/blob/5ea328e201c1163cf8c264d8109fbcfdde81cc53/README.md#L473-L480), [README.md#L514-L514](https://github.com/ochyai/vibe-local/blob/5ea328e201c1163cf8c264d8109fbcfdde81cc53/README.md#L514-L514) (`clm_926e59cf36e2adf58d05487f6fd6e1db015683a657c2f75a53ced5678944df35`)
- [observation/documented] The --classic mode drives the Claude Code CLI against local LLMs in a non-standard way that the README says may not comply with that CLI's terms of service. -- evidence: [README.md#L577-L587](https://github.com/ochyai/vibe-local/blob/5ea328e201c1163cf8c264d8109fbcfdde81cc53/README.md#L577-L587), [README.md#L564-L573](https://github.com/ochyai/vibe-local/blob/5ea328e201c1163cf8c264d8109fbcfdde81cc53/README.md#L564-L573) (`clm_10efd5a78099565b7d16da7a1d830d0d775dfdf7c6c8c6543f5997710d329ffb`)

## relevance (1 claim(s))

- [observation/documented] The tool targets offline workshops, students without paid AI plans, and beginners learning terminal operations via natural language, as a non-profit research/education utility; it is unaffiliated with Anthropic, Alibaba, OpenAI, or OpenCode. -- evidence: [README.md#L577-L587](https://github.com/ochyai/vibe-local/blob/5ea328e201c1163cf8c264d8109fbcfdde81cc53/README.md#L577-L587), [README.md#L26-L26](https://github.com/ochyai/vibe-local/blob/5ea328e201c1163cf8c264d8109fbcfdde81cc53/README.md#L26-L26) (`clm_31c41f71b5a62d98ba9b85994ca97d9e5436cc548d920dc79352b171d5bad5d2`)

