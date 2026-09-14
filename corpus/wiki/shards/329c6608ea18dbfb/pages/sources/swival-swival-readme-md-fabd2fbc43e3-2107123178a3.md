---
access: public
aliases: []
claim_ids:
- clm_3e012d1352601213dffd0973a1133eccbaf87fffde95febe42be1c7b0021491e
- clm_5822233be41eb2cef4e31caad35ea409adb785e9e35444406293fd1376ac97eb
- clm_70c615fa4d6c271a2ba75994b32d7091a1e0fcf6f48331a8bc09b0b03cd95818
- clm_79f637adbd809b006e54905000f28c7def0a657dc754aaf15f3306b1e0493fe3
- clm_85d77ba125288c89ef1c3098c81065180023a78db2b07af65e94ecd1b9f01764
- clm_9d7f41ed6163db3c0d52f4c4f6caa88f0af8b33c8b9fdc91b7665878f9422711
- clm_b06eb74d0f3cd40177c92824b2508433dd493323c6ec8a6d5e0cd3c517735463
- clm_bff6430f7a484d4dbce9649ab7da67b10ef726a0ad58a400d395e2383fd85b21
- clm_c66f42293247c5b0d7e754a39358f2f447e1e5cbb9629608c0e38484d958943e
- clm_ca3b36952376db5de9ec96fc7ffe07e7e8aab16b258b991355e20bef0d8f5713
- clm_d3904c4d6bc7a65e67f1eef81e37840b294859eab100143f4a785b2c4696d0a2
- clm_f02700fcf628494926724bcb7955bd62bc8f13e5ec261db52976cd6f3e9361f4
maturity: draft
page_id: pg_eb8cf403629c58bbb4262107123178a3
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_889217383b6d5512a3001db1cb368ae0
title: Swival/swival/README.md @ fabd2fbc43e3
updated_at: '2026-09-14T03:16:52Z'
---

# Swival/swival/README.md @ fabd2fbc43e3

<!-- rcw:begin owner=source:src_889217383b6d5512a3001db1cb368ae0 block=evidence -->
- With LM Studio and llama.cpp the agent auto-discovers the loaded model, requiring no configuration; the llama.cpp default base URL is http://127.0.0.1:8080, overridable with --base-url. [@claim:clm_3e012d1352601213dffd0973a1133eccbaf87fffde95febe42be1c7b0021491e]
- The agent is extensible with SKILL.md-based skills, MetaSKILLs (a safe Python subset, optional extra install), MCP tool servers, custom commands in ~/.config/swival/commands/ invoked with !name, and a configurable review loop with LLM-as-judge or external reviewer scripts. [@claim:clm_5822233be41eb2cef4e31caad35ea409adb785e9e35444406293fd1376ac97eb]
- The CLI supports providers including LM Studio, llama.cpp, HuggingFace, OpenRouter, Google Gemini, GEAP/Vertex AI, ChatGPT Plus/Pro, AWS Bedrock, Apple Foundation Models (experimental), generic OpenAI-compatible servers, and external commands, selected via flags like --provider and --model. [@claim:clm_70c615fa4d6c271a2ba75994b32d7091a1e0fcf6f48331a8bc09b0b03cd95818]
- Running swival --serve exposes the agent as an A2A HTTP endpoint with multi-turn context, streaming, rate limiting, and bearer auth; swival --acp speaks the Agent Client Protocol on stdio for editors like Zed. [@claim:clm_79f637adbd809b006e54905000f28c7def0a657dc754aaf15f3306b1e0493fe3]
- With --encrypt-secrets enabled, the agent detects API keys and credential tokens in LLM messages, encrypts them before they leave the machine, and decrypts locally on response so tools still work. [@claim:clm_85d77ba125288c89ef1c3098c81065180023a78db2b07af65e94ecd1b9f01764]
- Swival is a CLI coding agent; running it with a task argument starts an autonomous tool loop until it produces an answer, and stdout carries only the final answer with diagnostics on stderr. [@claim:clm_9d7f41ed6163db3c0d52f4c4f6caa88f0af8b33c8b9fdc91b7665878f9422711]
- If the positional task is omitted and stdin is piped, Swival reads the task from stdin, useful for long prompts and scripted workflows. [@claim:clm_b06eb74d0f3cd40177c92824b2508433dd493323c6ec8a6d5e0cd3c517735463]
- Cross-session memory stores notes in a local memory file and retrieves relevant entries per conversation using BM25 ranking; interrupted sessions save state to disk and resume in the same directory. [@claim:clm_bff6430f7a484d4dbce9649ab7da67b10ef726a0ad58a400d395e2383fd85b21]
- A REPL mode carries conversation history across questions, queues typed input during a turn, offers /model picker, /learn, /goal, /loop, /loops, /unloop, and /audit commands. [@claim:clm_c66f42293247c5b0d7e754a39358f2f447e1e5cbb9629608c0e38484d958943e]
- Passing --report report.json writes a machine-readable evaluation report with per-call LLM timing, tool success/failure counts, compaction events, and guardrail interventions for comparing models and settings. [@claim:clm_ca3b36952376db5de9ec96fc7ffe07e7e8aab16b258b991355e20bef0d8f5713]
- Context management targets small models: graduated compaction, persistent thinking notes, and a todo checklist survive context resets, per the README's design description. [@claim:clm_d3904c4d6bc7a65e67f1eef81e37840b294859eab100143f4a785b2c4696d0a2]
- Swival is pure Python with no framework, requires Python 3.13+, and is installable via uv tool install or Homebrew. [@claim:clm_f02700fcf628494926724bcb7955bd62bc8f13e5ec261db52976cd6f3e9361f4]
<!-- rcw:end owner=source:src_889217383b6d5512a3001db1cb368ae0 block=evidence -->

## Researcher notes

