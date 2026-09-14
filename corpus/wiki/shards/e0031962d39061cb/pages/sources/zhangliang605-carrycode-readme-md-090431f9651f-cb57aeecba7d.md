---
access: public
aliases: []
claim_ids:
- clm_0c469a46e3e9bc2ad55737e2ab922bfacca204b9b52bb2a920a21a7d9021e6bc
- clm_6fad38bfb1e474a106f22458f19c3142180fbc2914d0600ddd5f4f9aceab29fb
- clm_7d53701a6d132e62b613ac61019043fd7eaf1e53ba44011f4173e5569a744fa8
- clm_8ae0274b1398e1497749f21cc35f259d15071db1910ee73006f3383bd987a164
- clm_957eff14639612055eec2b7dae5abd8b72536091402abe4710733f72ff4eecdf
- clm_9d14e772aab1a0bd4bd06cc61f1c19cc2e6c19eb09b8fc176821e91d47c08daf
- clm_9f6a4043b3f9a946358eb5db34b5ce2a05ccbb67ce076e8534ad90ffc7018ed9
- clm_a36e2d4be2da291629dc9e81a69ab4acce515a0d11f1d683b314d8557dc53d05
- clm_ab146d466495b00cc7b6bff0da3a555f3f2a413055f15509f33be8df5d47bc7a
- clm_ad3595bbb1aef052f181189610b6e247c7eccae39abfab793dbe954a7ee0961c
- clm_b878108a92c74978bc712e231f592268223156cb3ae949f298dff036209c6709
- clm_efe0243de2a0ea55c4b7ff9c9aebd8c86305fe36996710f3d72af2932780c7e4
maturity: draft
page_id: pg_ef4c2d2a4b9f5f7f9b0acb57aeecba7d
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_6d04a5530c415a55b3d1d405fadba529
title: zhangliang605/carrycode/README.md @ 090431f9651f
updated_at: '2026-09-14T03:27:05Z'
---

# zhangliang605/carrycode/README.md @ 090431f9651f

<!-- rcw:begin owner=source:src_6d04a5530c415a55b3d1d405fadba529 block=evidence -->
- Sessions can be created, switched, and resumed with context persisting across conversations, and /compact compresses the current session context; long conversations are automatically compressed to fit token limits. [@claim:clm_0c469a46e3e9bc2ad55737e2ab922bfacca204b9b52bb2a920a21a7d9021e6bc]
- The product advertises support for 17+ LLM providers and 240+ models, including OpenAI, Anthropic, Google Gemini, DeepSeek, Kimi, GLM, MiniMax, Qwen, xAI Grok, Ollama, vLLM, and any OpenAI-compatible endpoint. [@claim:clm_6fad38bfb1e474a106f22458f19c3142180fbc2914d0600ddd5f4f9aceab29fb]
- Configuration lives in ~/.carry/carrycode.json (provider credentials and preferences) and ~/.carry/carrycode-runtime.json (language, default model, theme), with paths overridable via CARRYCODE_CONFIG_DIR or CARRYCODE_CONFIG_FILE. [@claim:clm_7d53701a6d132e62b613ac61019043fd7eaf1e53ba44011f4173e5569a744fa8]
- A skills system loads predefined or custom skills compatible with Claude Code, managed via /skill, with SkillHub integration to search Tencent SkillHub and install skills directly from results. [@claim:clm_8ae0274b1398e1497749f21cc35f259d15071db1910ee73006f3383bd987a164]
- The agent has two modes: Build mode for autonomous code generation and editing, and Plan mode for read-only analysis and planning. [@claim:clm_957eff14639612055eec2b7dae5abd8b72536091402abe4710733f72ff4eecdf]
- API keys can be supplied via environment variables such as OPENAI_API_KEY, ANTHROPIC_API_KEY, and GEMINI_API_KEY, or configured through the first-launch setup wizard or /model add. [@claim:clm_9d14e772aab1a0bd4bd06cc61f1c19cc2e6c19eb09b8fc176821e91d47c08daf]
- Approval modes control the agent's permissions at runtime: read-only, agent (read/write plus execution), and agent-full (unrestricted), selectable via /approval. [@claim:clm_9f6a4043b3f9a946358eb5db34b5ce2a05ccbb67ce076e8534ad90ffc7018ed9]
- Repository development practice: the recommended install path is a one-line script (curl ... install.sh | sudo sh on macOS/Linux, irm ... install.ps1 | iex on Windows) that auto-detects the platform, downloads the binary, verifies the checksum, and installs to /usr/local/bin. [@claim:clm_a36e2d4be2da291629dc9e81a69ab4acce515a0d11f1d683b314d8557dc53d05]
- The CLI is invoked as 'carry'; it offers an interactive terminal UI mode plus a single-shot mode via 'carry --once "..."' with an optional --timeout-ms flag, suited to scripting and CI. [@claim:clm_ab146d466495b00cc7b6bff0da3a555f3f2a413055f15509f33be8df5d47bc7a]
- The interactive UI exposes slash commands including /model, /mcp, /skill, /rule, /theme, /language, /approval, /session, /compact, /update, and /exit. [@claim:clm_ad3595bbb1aef052f181189610b6e247c7eccae39abfab793dbe954a7ee0961c]
- The usage terms prohibit modifying the project's Logo, Banner, or identifying marks when modifying or commercially using the source, directing such requests to us@carrycode.ai; this appears to be a branding restriction rather than a functional limitation. [@claim:clm_b878108a92c74978bc712e231f592268223156cb3ae949f298dff036209c6709]
- Repository development practice: building from source requires Rust (latest stable), Node.js v18+, Bun, and OS build tools; contributors use bun install, bun run build (or build:rust / build:ts), bun run dev, and bun run clean, producing ./target/index.js and a native Rust .node module. [@claim:clm_efe0243de2a0ea55c4b7ff9c9aebd8c86305fe36996710f3d72af2932780c7e4]
<!-- rcw:end owner=source:src_6d04a5530c415a55b3d1d405fadba529 block=evidence -->

## Researcher notes

