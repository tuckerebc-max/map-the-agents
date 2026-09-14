# harnesslab/claw-code-agent

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 167571da895b @ 76b0b0a684f15cec

## Summary (orientation draft, not independently verified)

README and parity-checklist evidence describe Claw Code Agent, a Python reimplementation of the Claude Code agent architecture that runs against OpenAI-compatible model servers with zero core dependencies, a tiered permission system, plugin/nested-agent runtimes, and session persistence. Evidence is documentation-only; no source code slices are present. Evidence coverage: 144 of 236 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 3 of 4 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 20 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

20 claim(s) across 11 facet(s); 2 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] The project is a Python reimplementation of the Claude Code npm agent architecture, intended to run with local open-source models via an OpenAI-compatible API server, and is marked alpha status. -- evidence: [README.md#L91-L91](https://github.com/HarnessLab/claw-code-agent/blob/167571da895b2a1a9e36ecfae2876984cef65e0d/README.md#L91-L91), [README.md#L11-L19](https://github.com/HarnessLab/claw-code-agent/blob/167571da895b2a1a9e36ecfae2876984cef65e0d/README.md#L11-L19), [README.md#L7-L9](https://github.com/HarnessLab/claw-code-agent/blob/167571da895b2a1a9e36ecfae2876984cef65e0d/README.md#L7-L9)
- components (1 claim(s)):
  - [observation/documented] The src/ tree includes modules for the agent loop (agent_runtime.py), tool execution (agent_tools.py), prompt assembly (agent_prompting.py), context building, session state, slash commands, nested-agent management, an OpenAI-compatible streaming client, and plugin runtime. -- evidence: [README.md#L223-L287](https://github.com/HarnessLab/claw-code-agent/blob/167571da895b2a1a9e36ecfae2876984cef65e0d/README.md#L223-L287)
- design-choices (2 claim(s)):
  - [observation/documented] Custom agent profiles are markdown files discovered from ./.claude/agents and ~/./.claude/agents, with project agents overriding user agents and user agents overriding built-ins on matching agent_type. -- evidence: [README.md#L607-L607](https://github.com/HarnessLab/claw-code-agent/blob/167571da895b2a1a9e36ecfae2876984cef65e0d/README.md#L607-L607), [README.md#L602-L602](https://github.com/HarnessLab/claw-code-agent/blob/167571da895b2a1a9e36ecfae2876984cef65e0d/README.md#L602-L602), [README.md#L604-L605](https://github.com/HarnessLab/claw-code-agent/blob/167571da895b2a1a9e36ecfae2876984cef65e0d/README.md#L604-L605)
  - [observation/documented] The runtime targets OpenAI-compatible chat-completions endpoints, so it can run against vLLM, Ollama, LiteLLM Proxy, or OpenRouter, configured via OPENAI_BASE_URL, OPENAI_API_KEY, and OPENAI_MODEL environment variables. -- evidence: [README.md#L402-L406](https://github.com/HarnessLab/claw-code-agent/blob/167571da895b2a1a9e36ecfae2876984cef65e0d/README.md#L402-L406), [README.md#L381-L381](https://github.com/HarnessLab/claw-code-agent/blob/167571da895b2a1a9e36ecfae2876984cef65e0d/README.md#L381-L381), [README.md#L327-L327](https://github.com/HarnessLab/claw-code-agent/blob/167571da895b2a1a9e36ecfae2876984cef65e0d/README.md#L327-L327), [README.md#L354-L354](https://github.com/HarnessLab/claw-code-agent/blob/167571da895b2a1a9e36ecfae2876984cef65e0d/README.md#L354-L354)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: the README instructs running the full test suite with 'python3 -m unittest discover -s tests -v', and points to TESTING_GUIDE.md for step-by-step feature verification commands. -- evidence: [README.md#L857-L859](https://github.com/HarnessLab/claw-code-agent/blob/167571da895b2a1a9e36ecfae2876984cef65e0d/README.md#L857-L859), [README.md#L855-L855](https://github.com/HarnessLab/claw-code-agent/blob/167571da895b2a1a9e36ecfae2876984cef65e0d/README.md#L855-L855), [README.md#L871-L871](https://github.com/HarnessLab/claw-code-agent/blob/167571da895b2a1a9e36ecfae2876984cef65e0d/README.md#L871-L871)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (4 claim(s)):
  - [observation/documented] The CLI exposes commands such as agent, agent-chat, agent-bg/agent-ps/agent-logs/agent-kill for background sessions, agent-resume, agent-prompt, token-budget, and agents-create/update/delete, plus utility commands like summary, manifest, commands, and tools. -- evidence: [README.md#L469-L487](https://github.com/HarnessLab/claw-code-agent/blob/167571da895b2a1a9e36ecfae2876984cef65e0d/README.md#L469-L487), [README.md#L660-L665](https://github.com/HarnessLab/claw-code-agent/blob/167571da895b2a1a9e36ecfae2876984cef65e0d/README.md#L660-L665)
  - [observation/documented] Slash commands are handled locally before the model loop and include /help, /context, /token-budget, /mcp, /search, /remote, /account, /config, /plan, and /tasks, some with aliases. -- evidence: [README.md#L553-L553](https://github.com/HarnessLab/claw-code-agent/blob/167571da895b2a1a9e36ecfae2876984cef65e0d/README.md#L553-L553), [README.md#L555-L589](https://github.com/HarnessLab/claw-code-agent/blob/167571da895b2a1a9e36ecfae2876984cef65e0d/README.md#L555-L589)
- memory-state (2 claim(s)):
  - [observation/documented] Each agent run automatically saves a resumable session under .port_sessions/agent, and agent-resume or agent-chat --resume-session-id continues from the saved transcript when run from the same directory. -- evidence: [README.md#L837-L841](https://github.com/HarnessLab/claw-code-agent/blob/167571da895b2a1a9e36ecfae2876984cef65e0d/README.md#L837-L841), [README.md#L820-L820](https://github.com/HarnessLab/claw-code-agent/blob/167571da895b2a1a9e36ecfae2876984cef65e0d/README.md#L820-L820), [README.md#L829-L833](https://github.com/HarnessLab/claw-code-agent/blob/167571da895b2a1a9e36ecfae2876984cef65e0d/README.md#L829-L833), [README.md#L849-L849](https://github.com/HarnessLab/claw-code-agent/blob/167571da895b2a1a9e36ecfae2876984cef65e0d/README.md#L849-L849)
  - [observation/documented] The runtime journals file edits with snapshot IDs and replays summaries on session resume, and performs context reduction via auto-snip, auto-compact, and reactive compaction on prompt-too-long errors. -- evidence: [README.md#L156-L205](https://github.com/HarnessLab/claw-code-agent/blob/167571da895b2a1a9e36ecfae2876984cef65e0d/README.md#L156-L205), [README.md#L27-L85](https://github.com/HarnessLab/claw-code-agent/blob/167571da895b2a1a9e36ecfae2876984cef65e0d/README.md#L27-L85)
More evidence: [full detail](claw-code-agent.detail.md)

Metadata and full claim list: [full detail](claw-code-agent.detail.md)
Human notes ([notes](claw-code-agent.notes.md), never overwritten by build)

[Back to map index](../../index.md)
