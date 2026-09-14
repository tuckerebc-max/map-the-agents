---
access: public
aliases: []
claim_ids:
- clm_1773e6c7cba31627581866f68555329783eeded32baf77f8ec715f0c2d6b353a
- clm_17d5f5fbbf5a76998b7885f28c2127c135da79dc9550891055d7fff88ce8f2ea
- clm_5b2b35906618dad123d4e97d2ea9a54b4b77757a9fb0ae984c4d2cfeb82ded6c
- clm_6d7ed083768bb9f67c429da0c57011804668192a6954874c040aa51f48683123
- clm_8d3b97bc088f8bc8dad41fe45c88178a80412c6a417098be9c6be33a3969a323
maturity: draft
page_id: pg_ed8bd4bf30615a86b05e36959a944e61
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_e9b8acb4fb3a5eebaed52cbc1a9cf04a
title: autohandai/code-cli/README.md @ f4775fdebd93
updated_at: '2026-09-14T01:35:30Z'
---

# autohandai/code-cli/README.md @ f4775fdebd93

<!-- rcw:begin owner=source:src_e9b8acb4fb3a5eebaed52cbc1a9cf04a block=evidence -->
- Every installer scans writable PATH directories and silently replaces any existing `agent` command so `agent` resolves to Autohand, which can break other tools' `agent` commands. [@claim:clm_1773e6c7cba31627581866f68555329783eeded32baf77f8ec715f0c2d6b353a]
- The CLI is exposed as `autohand`, `autohand-code`, and `agent`, with `autohand` as the canonical name. [@claim:clm_17d5f5fbbf5a76998b7885f28c2127c135da79dc9550891055d7fff88ce8f2ea]
- The product runs as a terminal REPL with file mentions, slash commands, keyboard shortcuts, provider switching, and session history available from one prompt. [@claim:clm_5b2b35906618dad123d4e97d2ea9a54b4b77757a9fb0ae984c4d2cfeb82ded6c]
- Skills declare a space-delimited allowed-tools list restricting which tools they may use, and the agent prompts before risky operations unless a different permission mode is chosen. [@claim:clm_6d7ed083768bb9f67c429da0c57011804668192a6954874c040aa51f48683123]
- The agent supports multiple LLM providers including OpenRouter, OpenAI, AWS Bedrock, DeepSeek, Azure, Z.ai, Vertex AI, Ollama, llama.cpp, MLX, and local models. [@claim:clm_8d3b97bc088f8bc8dad41fe45c88178a80412c6a417098be9c6be33a3969a323]
<!-- rcw:end owner=source:src_e9b8acb4fb3a5eebaed52cbc1a9cf04a block=evidence -->

## Researcher notes

