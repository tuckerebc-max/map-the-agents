# swival/swival

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit fabd2fbc43e3 @ e9e7934bcfa0719d

## Summary (orientation draft, not independently verified)

The evidence is README-only documentation for Swival, a Python CLI coding agent that connects to many model providers and runs an autonomous tool loop, with REPL, scheduling, A2A/ACP server modes, memory, and audit features. No source code or contributor-workflow evidence is present.

## Source coverage

Source coverage (partial): 2 of 3 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The agent is extensible with SKILL.md-based skills, MetaSKILLs (a safe Python subset, optional extra install), MCP tool servers, custom commands in ~/.config/swival/commands/ invoked with !name, and a configurable review loop with LLM-as-judge or external reviewer scripts. -- evidence: [README.md#L320-L323](https://github.com/Swival/swival/blob/fabd2fbc43e3851f3a377b544ce75b03bfcff1d3/README.md#L320-L323), [README.md#L307-L312](https://github.com/Swival/swival/blob/fabd2fbc43e3851f3a377b544ce75b03bfcff1d3/README.md#L307-L312), [README.md#L236-L239](https://github.com/Swival/swival/blob/fabd2fbc43e3851f3a377b544ce75b03bfcff1d3/README.md#L236-L239)
- design-choices (1 claim(s)):
  - [observation/documented] Context management targets small models: graduated compaction, persistent thinking notes, and a todo checklist survive context resets, per the README's design description. -- evidence: [README.md#L213-L217](https://github.com/Swival/swival/blob/fabd2fbc43e3851f3a377b544ce75b03bfcff1d3/README.md#L213-L217)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (6 claim(s)):
  - [observation/documented] Swival is a CLI coding agent; running it with a task argument starts an autonomous tool loop until it produces an answer, and stdout carries only the final answer with diagnostics on stderr. -- evidence: [README.md#L317-L318](https://github.com/Swival/swival/blob/fabd2fbc43e3851f3a377b544ce75b03bfcff1d3/README.md#L317-L318), [README.md#L13-L25](https://github.com/Swival/swival/blob/fabd2fbc43e3851f3a377b544ce75b03bfcff1d3/README.md#L13-L25), [README.md#L7-L11](https://github.com/Swival/swival/blob/fabd2fbc43e3851f3a377b544ce75b03bfcff1d3/README.md#L7-L11)
  - [observation/documented] The CLI supports providers including LM Studio, llama.cpp, HuggingFace, OpenRouter, Google Gemini, GEAP/Vertex AI, ChatGPT Plus/Pro, AWS Bedrock, Apple Foundation Models (experimental), generic OpenAI-compatible servers, and external commands, selected via flags like --provider and --model. -- evidence: [README.md#L219-L234](https://github.com/Swival/swival/blob/fabd2fbc43e3851f3a377b544ce75b03bfcff1d3/README.md#L219-L234), [README.md#L31-L43](https://github.com/Swival/swival/blob/fabd2fbc43e3851f3a377b544ce75b03bfcff1d3/README.md#L31-L43), [README.md#L13-L25](https://github.com/Swival/swival/blob/fabd2fbc43e3851f3a377b544ce75b03bfcff1d3/README.md#L13-L25)
- memory-state (1 claim(s)):
  - [observation/documented] Cross-session memory stores notes in a local memory file and retrieves relevant entries per conversation using BM25 ranking; interrupted sessions save state to disk and resume in the same directory. -- evidence: [README.md#L260-L263](https://github.com/Swival/swival/blob/fabd2fbc43e3851f3a377b544ce75b03bfcff1d3/README.md#L260-L263), [README.md#L254-L258](https://github.com/Swival/swival/blob/fabd2fbc43e3851f3a377b544ce75b03bfcff1d3/README.md#L254-L258)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
  - [observation/documented] With --encrypt-secrets enabled, the agent detects API keys and credential tokens in LLM messages, encrypts them before they leave the machine, and decrypts locally on response so tools still work. -- evidence: [README.md#L247-L252](https://github.com/Swival/swival/blob/fabd2fbc43e3851f3a377b544ce75b03bfcff1d3/README.md#L247-L252)
- evaluation (1 claim(s)):
  - [observation/documented] Passing --report report.json writes a machine-readable evaluation report with per-call LLM timing, tool success/failure counts, compaction events, and guardrail interventions for comparing models and settings. -- evidence: [README.md#L241-L245](https://github.com/Swival/swival/blob/fabd2fbc43e3851f3a377b544ce75b03bfcff1d3/README.md#L241-L245)
- dependencies (1 claim(s)):
  - [observation/documented] Swival is pure Python with no framework, requires Python 3.13+, and is installable via uv tool install or Homebrew. -- evidence: [README.md#L61-L63](https://github.com/Swival/swival/blob/fabd2fbc43e3851f3a377b544ce75b03bfcff1d3/README.md#L61-L63), [README.md#L314-L315](https://github.com/Swival/swival/blob/fabd2fbc43e3851f3a377b544ce75b03bfcff1d3/README.md#L314-L315), [README.md#L13-L25](https://github.com/Swival/swival/blob/fabd2fbc43e3851f3a377b544ce75b03bfcff1d3/README.md#L13-L25), [README.md#L53-L59](https://github.com/Swival/swival/blob/fabd2fbc43e3851f3a377b544ce75b03bfcff1d3/README.md#L53-L59), [README.md#L67-L70](https://github.com/Swival/swival/blob/fabd2fbc43e3851f3a377b544ce75b03bfcff1d3/README.md#L67-L70)
- limitations: unknown (no source-linked claim submitted for this facet)
More evidence: [full detail](swival.detail.md)

Metadata and full claim list: [full detail](swival.detail.md)
Human notes ([notes](swival.notes.md), never overwritten by build)

[Back to map index](../../index.md)
