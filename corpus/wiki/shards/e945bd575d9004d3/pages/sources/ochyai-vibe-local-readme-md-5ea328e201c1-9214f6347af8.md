---
access: public
aliases: []
claim_ids:
- clm_067d82d1870ff6d40ea6f442b39855320867304920d588576cc0c9774be73ea1
- clm_10efd5a78099565b7d16da7a1d830d0d775dfdf7c6c8c6543f5997710d329ffb
- clm_31c41f71b5a62d98ba9b85994ca97d9e5436cc548d920dc79352b171d5bad5d2
- clm_61debc578af8a46ea49bd1cec4babad65aaa2d4da34e6e2ae374d01bc452d735
- clm_704b7611469125e0fafd703bebb82ce6d01ab6c53742b81871c0f9b7691475f4
- clm_926e59cf36e2adf58d05487f6fd6e1db015683a657c2f75a53ced5678944df35
- clm_9e908bb8989964a439f8341c3f587d050c804d465c68b6da9f49dfa1a2e610cf
- clm_9f562d743490fe4f909de449b1708f574db2f4e725259b737ecd4467f584247d
- clm_a602615b4d36e08eab0519541858deb2b955ff66ba4f311d9150c480d16e5374
- clm_a9a730c1631d4d5e469657a2f20a26ba54c99d36faab95a1fcfac6118a7f33b0
- clm_d7fd930642459020233e85abbc1ee22de9902f83422b16aae6f52f6f39eb5842
- clm_f2841605c081213a93ef8fbabcf14f3b464c0c3d83c49ccdfc2055a68cf7cafd
maturity: draft
page_id: pg_efeab5b6d9f05464b0e59214f6347af8
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_bcb254f9810a5a9a82a1fe085bb9fd86
title: ochyai/vibe-local/README.md @ 5ea328e201c1
updated_at: '2026-09-14T03:10:50Z'
---

# ochyai/vibe-local/README.md @ 5ea328e201c1

<!-- rcw:begin owner=source:src_bcb254f9810a5a9a82a1fe085bb9fd86 block=evidence -->
- The stack depends on Ollama, RAM-tiered local LLMs (qwen3-coder-next, qwen3.6:35b-a3b, gpt-oss:20b, qwen3.5:4b), and the OpenCode TUI; opencode is installed via brew if missing. [@claim:clm_067d82d1870ff6d40ea6f442b39855320867304920d588576cc0c9774be73ea1]
- The --classic mode drives the Claude Code CLI against local LLMs in a non-standard way that the README says may not comply with that CLI's terms of service. [@claim:clm_10efd5a78099565b7d16da7a1d830d0d775dfdf7c6c8c6543f5997710d329ffb]
- The tool targets offline workshops, students without paid AI plans, and beginners learning terminal operations via natural language, as a non-profit research/education utility; it is unaffiliated with Anthropic, Alibaba, OpenAI, or OpenCode. [@claim:clm_31c41f71b5a62d98ba9b85994ca97d9e5436cc548d920dc79352b171d5bad5d2]
- The v2 launcher detects RAM, selects a model, creates num_ctx-baked Ollama aliases (vibe-coder/vibe-fast) via ollama create, and generates OpenCode config without modifying the user's own OpenCode settings. [@claim:clm_61debc578af8a46ea49bd1cec4babad65aaa2d4da34e6e2ae374d01bc452d735]
- The vibe-coder engine includes a permission manager with safe/ask/deny tiers, and its approval prompt accepts Japanese, English, and Chinese yes, falling back to /dev/tty when stdin is not a TTY. [@claim:clm_704b7611469125e0fafd703bebb82ce6d01ab6c53742b81871c0f9b7691475f4]
- The README warns that local LLMs are less accurate than cloud AI and may unintentionally run dangerous commands, advising users to reject sudo, chmod/chown, dd/mkfs//dev/, config-overwriting redirects, and --force flags. [@claim:clm_926e59cf36e2adf58d05487f6fd6e1db015683a657c2f75a53ced5678944df35]
- An optional built-in Python engine, vibe-coder.py, is dependency-free (stdlib only), talks directly to Ollama's /api/chat with a tool-execution loop, and can run standalone via python3. [@claim:clm_9e908bb8989964a439f8341c3f587d050c804d465c68b6da9f49dfa1a2e610cf]
- v2 dropped the custom Anthropic-to-Ollama conversion proxy because Ollama natively implements the Anthropic Messages API (v0.14+); the old proxy and MLX server were archived under legacy/. [@claim:clm_9f562d743490fe4f909de449b1708f574db2f4e725259b737ecd4467f584247d]
- A minimal passthrough router (vibe-router) classifies input: greetings and short questions go to a small model for fast replies, while coding and tool-use requests go to a larger model; --no-router disables it. [@claim:clm_a602615b4d36e08eab0519541858deb2b955ff66ba4f311d9150c480d16e5374]
- v2 defaults to ask-before-every-action mode where the AI requests permission before file edits or command execution; the -y flag enables auto-approval of file writes, commands, and system changes. [@claim:clm_a9a730c1631d4d5e469657a2f20a26ba54c99d36faab95a1fcfac6118a7f33b0]
- Inside the TUI, /theme switches themes, Tab toggles Plan/Build mode, and /models (or --no-router) pins a specific model instead of the default vibe-auto routing. [@claim:clm_d7fd930642459020233e85abbc1ee22de9902f83422b16aae6f52f6f39eb5842]
- vibe-coder.py supports local RAG using sqlite3 and Ollama embeddings to inject relevant codebase context into the system prompt, with the index stored in .vibe/rag/ and tunable top-k and embedding model. [@claim:clm_f2841605c081213a93ef8fbabcf14f3b464c0c3d83c49ccdfc2055a68cf7cafd]
<!-- rcw:end owner=source:src_bcb254f9810a5a9a82a1fe085bb9fd86 block=evidence -->

## Researcher notes

