# fullive-ai/anima

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit ea1542ff8420 @ 5a37690defbc92d2

## Summary (orientation draft, not independently verified)

Anima is an open-source Agent OS for intelligent hardware: a Python/FastAPI backend with a LangGraph Brain, device Skills, layered file-based memory, MIoT adapters, and a React polling dashboard, currently supporting Xiaomi/Mi Home devices. AGENT.md and ARCHITECTURE_GUARDRAILS.md provide contributor-facing architecture and testing guidance. Evidence coverage: 166 of 400 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 14 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 15 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

15 claim(s) across 10 facet(s); 3 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Anima is described as an open-source Agent OS for intelligent hardware, aiming to give home devices perceptive, decision-making, learning, and extensible AI capabilities rather than being a device control panel. -- evidence: [README.md#L20-L20](https://github.com/Fullive-AI/Anima/blob/ea1542ff8420d37089926d558ff0d6cc2174eac8/README.md#L20-L20), [README.md#L1-L5](https://github.com/Fullive-AI/Anima/blob/ea1542ff8420d37089926d558ff0d6cc2174eac8/README.md#L1-L5)
- components (2 claim(s)):
  - [observation/documented] The runtime comprises a Brain decision layer, device Skills, a layered Memory system, hardware Adapters, a FastAPI backend, and a React dashboard; core/main.py is the composition root and startup entrypoint. -- evidence: [AGENT.md#L51-L51](https://github.com/Fullive-AI/Anima/blob/ea1542ff8420d37089926d558ff0d6cc2174eac8/AGENT.md#L51-L51), [README.md#L321-L344](https://github.com/Fullive-AI/Anima/blob/ea1542ff8420d37089926d558ff0d6cc2174eac8/README.md#L321-L344), [README.md#L34-L38](https://github.com/Fullive-AI/Anima/blob/ea1542ff8420d37089926d558ff0d6cc2174eac8/README.md#L34-L38), [AGENT.md#L55-L64](https://github.com/Fullive-AI/Anima/blob/ea1542ff8420d37089926d558ff0d6cc2174eac8/AGENT.md#L55-L64)
  - [observation/documented] Per AGENT.md, the implemented system is a single-process Python backend under core/ with file-based memory in data/memory and a polling-based frontend refresh. -- evidence: [AGENT.md#L30-L37](https://github.com/Fullive-AI/Anima/blob/ea1542ff8420d37089926d558ff0d6cc2174eac8/AGENT.md#L30-L37)
- design-choices (1 claim(s)):
  - [observation/documented] The Brain is designed to decide within explicit skill boundaries, device capabilities, and safety rules rather than letting an LLM control devices freely. -- evidence: [README.md#L115-L115](https://github.com/Fullive-AI/Anima/blob/ea1542ff8420d37089926d558ff0d6cc2174eac8/README.md#L115-L115)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: AGENT.md and ARCHITECTURE_GUARDRAILS.md target coding agents contributing to the repo, defining module ownership boundaries, change heuristics, and testing expectations such as running tests under tests/ before considering work complete. -- evidence: [AGENT.md#L279-L279](https://github.com/Fullive-AI/Anima/blob/ea1542ff8420d37089926d558ff0d6cc2174eac8/AGENT.md#L279-L279), [AGENT.md#L226-L226](https://github.com/Fullive-AI/Anima/blob/ea1542ff8420d37089926d558ff0d6cc2174eac8/AGENT.md#L226-L226), [AGENT.md#L281-L283](https://github.com/Fullive-AI/Anima/blob/ea1542ff8420d37089926d558ff0d6cc2174eac8/AGENT.md#L281-L283), [AGENT.md#L3-L3](https://github.com/Fullive-AI/Anima/blob/ea1542ff8420d37089926d558ff0d6cc2174eac8/AGENT.md#L3-L3)
- skills-patterns (2 claim(s)):
  - [observation/documented] Skills are device domain-knowledge packages with a defined layout: SKILL.md metadata, references (knowledge, decide, learn prompts), and scripts/actions.py as the structured action execution entrypoint. -- evidence: [README.md#L121-L129](https://github.com/Fullive-AI/Anima/blob/ea1542ff8420d37089926d558ff0d6cc2174eac8/README.md#L121-L129), [README.md#L119-L119](https://github.com/Fullive-AI/Anima/blob/ea1542ff8420d37089926d558ff0d6cc2174eac8/README.md#L119-L119)
  - [observation/documented] Built-in skills include light, humidifier, air_conditioner, air_purifier, speaker, coordinator, device_discovery, and skill_creator; custom skills can be added under skills/custom/. -- evidence: [README.md#L144-L144](https://github.com/Fullive-AI/Anima/blob/ea1542ff8420d37089926d558ff0d6cc2174eac8/README.md#L144-L144), [README.md#L133-L142](https://github.com/Fullive-AI/Anima/blob/ea1542ff8420d37089926d558ff0d6cc2174eac8/README.md#L133-L142)
- interfaces (2 claim(s)):
  - [observation/documented] The backend exposes REST endpoints including /health, /api/devices, /api/chat, /api/environment, /api/scan, /api/memory, /api/settings, and Xiaomi QR login start/poll endpoints, with Swagger at localhost:8080/docs. -- evidence: [README.md#L354-L369](https://github.com/Fullive-AI/Anima/blob/ea1542ff8420d37089926d558ff0d6cc2174eac8/README.md#L354-L369), [README.md#L373-L375](https://github.com/Fullive-AI/Anima/blob/ea1542ff8420d37089926d558ff0d6cc2174eac8/README.md#L373-L375)
  - [observation/documented] LLM integration is OpenAI-compatible, configured via ANIMA_LLM_API_KEY and optionally ANIMA_LLM_BASE_URL, supporting OpenAI, DeepSeek, Doubao, proxied Anthropic, and Ollama-compatible endpoints. -- evidence: [README.md#L286-L286](https://github.com/Fullive-AI/Anima/blob/ea1542ff8420d37089926d558ff0d6cc2174eac8/README.md#L286-L286), [README.md#L84-L84](https://github.com/Fullive-AI/Anima/blob/ea1542ff8420d37089926d558ff0d6cc2174eac8/README.md#L84-L84)
- memory-state (2 claim(s)):
More evidence: [full detail](anima.detail.md)

Metadata and full claim list: [full detail](anima.detail.md)
Human notes ([notes](anima.notes.md), never overwritten by build)

[Back to map index](../../index.md)
