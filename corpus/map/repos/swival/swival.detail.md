# swival/swival -- full detail

[Back to orientation](swival.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/swival/swival/fabd2fbc43e3851f3a377b544ce75b03bfcff1d3/e9e7934bcfa0719d.json](../../../wiki/dossiers/swival/swival/fabd2fbc43e3851f3a377b544ce75b03bfcff1d3/e9e7934bcfa0719d.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The agent is extensible with SKILL.md-based skills, MetaSKILLs (a safe Python subset, optional extra install), MCP tool servers, custom commands in ~/.config/swival/commands/ invoked with !name, and a configurable review loop with LLM-as-judge or external reviewer scripts. -- evidence: [README.md#L320-L323](https://github.com/Swival/swival/blob/fabd2fbc43e3851f3a377b544ce75b03bfcff1d3/README.md#L320-L323), [README.md#L307-L312](https://github.com/Swival/swival/blob/fabd2fbc43e3851f3a377b544ce75b03bfcff1d3/README.md#L307-L312), [README.md#L236-L239](https://github.com/Swival/swival/blob/fabd2fbc43e3851f3a377b544ce75b03bfcff1d3/README.md#L236-L239) (`clm_5822233be41eb2cef4e31caad35ea409adb785e9e35444406293fd1376ac97eb`)

## design-choices (1 claim(s))

- [observation/documented] Context management targets small models: graduated compaction, persistent thinking notes, and a todo checklist survive context resets, per the README's design description. -- evidence: [README.md#L213-L217](https://github.com/Swival/swival/blob/fabd2fbc43e3851f3a377b544ce75b03bfcff1d3/README.md#L213-L217) (`clm_d3904c4d6bc7a65e67f1eef81e37840b294859eab100143f4a785b2c4696d0a2`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (6 claim(s))

- [observation/documented] Swival is a CLI coding agent; running it with a task argument starts an autonomous tool loop until it produces an answer, and stdout carries only the final answer with diagnostics on stderr. -- evidence: [README.md#L317-L318](https://github.com/Swival/swival/blob/fabd2fbc43e3851f3a377b544ce75b03bfcff1d3/README.md#L317-L318), [README.md#L13-L25](https://github.com/Swival/swival/blob/fabd2fbc43e3851f3a377b544ce75b03bfcff1d3/README.md#L13-L25), [README.md#L7-L11](https://github.com/Swival/swival/blob/fabd2fbc43e3851f3a377b544ce75b03bfcff1d3/README.md#L7-L11) (`clm_9d7f41ed6163db3c0d52f4c4f6caa88f0af8b33c8b9fdc91b7665878f9422711`)
- [observation/documented] The CLI supports providers including LM Studio, llama.cpp, HuggingFace, OpenRouter, Google Gemini, GEAP/Vertex AI, ChatGPT Plus/Pro, AWS Bedrock, Apple Foundation Models (experimental), generic OpenAI-compatible servers, and external commands, selected via flags like --provider and --model. -- evidence: [README.md#L219-L234](https://github.com/Swival/swival/blob/fabd2fbc43e3851f3a377b544ce75b03bfcff1d3/README.md#L219-L234), [README.md#L31-L43](https://github.com/Swival/swival/blob/fabd2fbc43e3851f3a377b544ce75b03bfcff1d3/README.md#L31-L43), [README.md#L13-L25](https://github.com/Swival/swival/blob/fabd2fbc43e3851f3a377b544ce75b03bfcff1d3/README.md#L13-L25) (`clm_70c615fa4d6c271a2ba75994b32d7091a1e0fcf6f48331a8bc09b0b03cd95818`)
- [observation/documented] With LM Studio and llama.cpp the agent auto-discovers the loaded model, requiring no configuration; the llama.cpp default base URL is http://127.0.0.1:8080, overridable with --base-url. -- evidence: [README.md#L82-L95](https://github.com/Swival/swival/blob/fabd2fbc43e3851f3a377b544ce75b03bfcff1d3/README.md#L82-L95), [README.md#L13-L25](https://github.com/Swival/swival/blob/fabd2fbc43e3851f3a377b544ce75b03bfcff1d3/README.md#L13-L25), [README.md#L97-L97](https://github.com/Swival/swival/blob/fabd2fbc43e3851f3a377b544ce75b03bfcff1d3/README.md#L97-L97) (`clm_3e012d1352601213dffd0973a1133eccbaf87fffde95febe42be1c7b0021491e`)
- [observation/documented] A REPL mode carries conversation history across questions, queues typed input during a turn, offers /model picker, /learn, /goal, /loop, /loops, /unloop, and /audit commands. -- evidence: [README.md#L181-L187](https://github.com/Swival/swival/blob/fabd2fbc43e3851f3a377b544ce75b03bfcff1d3/README.md#L181-L187), [README.md#L299-L305](https://github.com/Swival/swival/blob/fabd2fbc43e3851f3a377b544ce75b03bfcff1d3/README.md#L299-L305), [README.md#L277-L287](https://github.com/Swival/swival/blob/fabd2fbc43e3851f3a377b544ce75b03bfcff1d3/README.md#L277-L287), [README.md#L254-L258](https://github.com/Swival/swival/blob/fabd2fbc43e3851f3a377b544ce75b03bfcff1d3/README.md#L254-L258), [README.md#L265-L275](https://github.com/Swival/swival/blob/fabd2fbc43e3851f3a377b544ce75b03bfcff1d3/README.md#L265-L275) (`clm_c66f42293247c5b0d7e754a39358f2f447e1e5cbb9629608c0e38484d958943e`)
- [observation/documented] If the positional task is omitted and stdin is piped, Swival reads the task from stdin, useful for long prompts and scripted workflows. -- evidence: [README.md#L200-L200](https://github.com/Swival/swival/blob/fabd2fbc43e3851f3a377b544ce75b03bfcff1d3/README.md#L200-L200), [README.md#L191-L192](https://github.com/Swival/swival/blob/fabd2fbc43e3851f3a377b544ce75b03bfcff1d3/README.md#L191-L192) (`clm_b06eb74d0f3cd40177c92824b2508433dd493323c6ec8a6d5e0cd3c517735463`)
- [observation/documented] Running swival --serve exposes the agent as an A2A HTTP endpoint with multi-turn context, streaming, rate limiting, and bearer auth; swival --acp speaks the Agent Client Protocol on stdio for editors like Zed. -- evidence: [README.md#L289-L291](https://github.com/Swival/swival/blob/fabd2fbc43e3851f3a377b544ce75b03bfcff1d3/README.md#L289-L291), [README.md#L293-L297](https://github.com/Swival/swival/blob/fabd2fbc43e3851f3a377b544ce75b03bfcff1d3/README.md#L293-L297) (`clm_79f637adbd809b006e54905000f28c7def0a657dc754aaf15f3306b1e0493fe3`)

## memory-state (1 claim(s))

- [observation/documented] Cross-session memory stores notes in a local memory file and retrieves relevant entries per conversation using BM25 ranking; interrupted sessions save state to disk and resume in the same directory. -- evidence: [README.md#L260-L263](https://github.com/Swival/swival/blob/fabd2fbc43e3851f3a377b544ce75b03bfcff1d3/README.md#L260-L263), [README.md#L254-L258](https://github.com/Swival/swival/blob/fabd2fbc43e3851f3a377b544ce75b03bfcff1d3/README.md#L254-L258) (`clm_bff6430f7a484d4dbce9649ab7da67b10ef726a0ad58a400d395e2383fd85b21`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] With --encrypt-secrets enabled, the agent detects API keys and credential tokens in LLM messages, encrypts them before they leave the machine, and decrypts locally on response so tools still work. -- evidence: [README.md#L247-L252](https://github.com/Swival/swival/blob/fabd2fbc43e3851f3a377b544ce75b03bfcff1d3/README.md#L247-L252) (`clm_85d77ba125288c89ef1c3098c81065180023a78db2b07af65e94ecd1b9f01764`)

## evaluation (1 claim(s))

- [observation/documented] Passing --report report.json writes a machine-readable evaluation report with per-call LLM timing, tool success/failure counts, compaction events, and guardrail interventions for comparing models and settings. -- evidence: [README.md#L241-L245](https://github.com/Swival/swival/blob/fabd2fbc43e3851f3a377b544ce75b03bfcff1d3/README.md#L241-L245) (`clm_ca3b36952376db5de9ec96fc7ffe07e7e8aab16b258b991355e20bef0d8f5713`)

## dependencies (1 claim(s))

- [observation/documented] Swival is pure Python with no framework, requires Python 3.13+, and is installable via uv tool install or Homebrew. -- evidence: [README.md#L61-L63](https://github.com/Swival/swival/blob/fabd2fbc43e3851f3a377b544ce75b03bfcff1d3/README.md#L61-L63), [README.md#L314-L315](https://github.com/Swival/swival/blob/fabd2fbc43e3851f3a377b544ce75b03bfcff1d3/README.md#L314-L315), [README.md#L13-L25](https://github.com/Swival/swival/blob/fabd2fbc43e3851f3a377b544ce75b03bfcff1d3/README.md#L13-L25), [README.md#L53-L59](https://github.com/Swival/swival/blob/fabd2fbc43e3851f3a377b544ce75b03bfcff1d3/README.md#L53-L59), [README.md#L67-L70](https://github.com/Swival/swival/blob/fabd2fbc43e3851f3a377b544ce75b03bfcff1d3/README.md#L67-L70) (`clm_f02700fcf628494926724bcb7955bd62bc8f13e5ec261db52976cd6f3e9361f4`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

