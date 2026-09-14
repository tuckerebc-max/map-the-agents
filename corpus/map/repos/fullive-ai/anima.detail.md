# fullive-ai/anima -- full detail

[Back to orientation](anima.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/fullive-ai/anima/ea1542ff8420d37089926d558ff0d6cc2174eac8/5a37690defbc92d2.json](../../../wiki/dossiers/fullive-ai/anima/ea1542ff8420d37089926d558ff0d6cc2174eac8/5a37690defbc92d2.json)

## specifications (1 claim(s))

- [observation/documented] Anima is described as an open-source Agent OS for intelligent hardware, aiming to give home devices perceptive, decision-making, learning, and extensible AI capabilities rather than being a device control panel. -- evidence: [README.md#L20-L20](https://github.com/Fullive-AI/Anima/blob/ea1542ff8420d37089926d558ff0d6cc2174eac8/README.md#L20-L20), [README.md#L1-L5](https://github.com/Fullive-AI/Anima/blob/ea1542ff8420d37089926d558ff0d6cc2174eac8/README.md#L1-L5) (`clm_0bfbc75d615a2cecf48f59390929509be33027166156568dcfb249a83a42a76e`)

## components (2 claim(s))

- [observation/documented] The runtime comprises a Brain decision layer, device Skills, a layered Memory system, hardware Adapters, a FastAPI backend, and a React dashboard; core/main.py is the composition root and startup entrypoint. -- evidence: [AGENT.md#L51-L51](https://github.com/Fullive-AI/Anima/blob/ea1542ff8420d37089926d558ff0d6cc2174eac8/AGENT.md#L51-L51), [README.md#L321-L344](https://github.com/Fullive-AI/Anima/blob/ea1542ff8420d37089926d558ff0d6cc2174eac8/README.md#L321-L344), [README.md#L34-L38](https://github.com/Fullive-AI/Anima/blob/ea1542ff8420d37089926d558ff0d6cc2174eac8/README.md#L34-L38), [AGENT.md#L55-L64](https://github.com/Fullive-AI/Anima/blob/ea1542ff8420d37089926d558ff0d6cc2174eac8/AGENT.md#L55-L64) (`clm_9f7cebc7de082417d4e66dbf9851a0ded38ceeb64b50e8d3bc6fe47c09d7a1a9`)
- [observation/documented] Per AGENT.md, the implemented system is a single-process Python backend under core/ with file-based memory in data/memory and a polling-based frontend refresh. -- evidence: [AGENT.md#L30-L37](https://github.com/Fullive-AI/Anima/blob/ea1542ff8420d37089926d558ff0d6cc2174eac8/AGENT.md#L30-L37) (`clm_e0d994ab5624ad8f9917691c96dba6bb59b93eb5e075f052efd887ed929297db`)

## design-choices (1 claim(s))

- [observation/documented] The Brain is designed to decide within explicit skill boundaries, device capabilities, and safety rules rather than letting an LLM control devices freely. -- evidence: [README.md#L115-L115](https://github.com/Fullive-AI/Anima/blob/ea1542ff8420d37089926d558ff0d6cc2174eac8/README.md#L115-L115) (`clm_3a845cbbe42e0dbab1b9910a112b73e90d5b4b8825b52114fe6bae39db771b91`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: AGENT.md and ARCHITECTURE_GUARDRAILS.md target coding agents contributing to the repo, defining module ownership boundaries, change heuristics, and testing expectations such as running tests under tests/ before considering work complete. -- evidence: [AGENT.md#L279-L279](https://github.com/Fullive-AI/Anima/blob/ea1542ff8420d37089926d558ff0d6cc2174eac8/AGENT.md#L279-L279), [AGENT.md#L226-L226](https://github.com/Fullive-AI/Anima/blob/ea1542ff8420d37089926d558ff0d6cc2174eac8/AGENT.md#L226-L226), [AGENT.md#L281-L283](https://github.com/Fullive-AI/Anima/blob/ea1542ff8420d37089926d558ff0d6cc2174eac8/AGENT.md#L281-L283), [AGENT.md#L3-L3](https://github.com/Fullive-AI/Anima/blob/ea1542ff8420d37089926d558ff0d6cc2174eac8/AGENT.md#L3-L3) (`clm_247e5c7fedb850fedcfd3756826acdf3774a04afad92b0cd48c6470bd61e3a78`)

## skills-patterns (2 claim(s))

- [observation/documented] Skills are device domain-knowledge packages with a defined layout: SKILL.md metadata, references (knowledge, decide, learn prompts), and scripts/actions.py as the structured action execution entrypoint. -- evidence: [README.md#L121-L129](https://github.com/Fullive-AI/Anima/blob/ea1542ff8420d37089926d558ff0d6cc2174eac8/README.md#L121-L129), [README.md#L119-L119](https://github.com/Fullive-AI/Anima/blob/ea1542ff8420d37089926d558ff0d6cc2174eac8/README.md#L119-L119) (`clm_c2a37ddc35ea3edae99c44735ac7b4ff4032d906d0b0f84365cbbbe71ca98a16`)
- [observation/documented] Built-in skills include light, humidifier, air_conditioner, air_purifier, speaker, coordinator, device_discovery, and skill_creator; custom skills can be added under skills/custom/. -- evidence: [README.md#L144-L144](https://github.com/Fullive-AI/Anima/blob/ea1542ff8420d37089926d558ff0d6cc2174eac8/README.md#L144-L144), [README.md#L133-L142](https://github.com/Fullive-AI/Anima/blob/ea1542ff8420d37089926d558ff0d6cc2174eac8/README.md#L133-L142) (`clm_06c1ddab72c98cb7ae04d2a0a4338c012c93c39dd4bb96b75e90300769f9c015`)

## interfaces (2 claim(s))

- [observation/documented] The backend exposes REST endpoints including /health, /api/devices, /api/chat, /api/environment, /api/scan, /api/memory, /api/settings, and Xiaomi QR login start/poll endpoints, with Swagger at localhost:8080/docs. -- evidence: [README.md#L354-L369](https://github.com/Fullive-AI/Anima/blob/ea1542ff8420d37089926d558ff0d6cc2174eac8/README.md#L354-L369), [README.md#L373-L375](https://github.com/Fullive-AI/Anima/blob/ea1542ff8420d37089926d558ff0d6cc2174eac8/README.md#L373-L375) (`clm_3cc0c015e1d3d540c24426639c96a0e46790fe4e6630f6827b1389e96558072e`)
- [observation/documented] LLM integration is OpenAI-compatible, configured via ANIMA_LLM_API_KEY and optionally ANIMA_LLM_BASE_URL, supporting OpenAI, DeepSeek, Doubao, proxied Anthropic, and Ollama-compatible endpoints. -- evidence: [README.md#L286-L286](https://github.com/Fullive-AI/Anima/blob/ea1542ff8420d37089926d558ff0d6cc2174eac8/README.md#L286-L286), [README.md#L84-L84](https://github.com/Fullive-AI/Anima/blob/ea1542ff8420d37089926d558ff0d6cc2174eac8/README.md#L84-L84) (`clm_4dd9ff3566948e4f7a033d05a2775970da5d48c66c8305cf750c4a48e8faa60a`)

## memory-state (2 claim(s))

- [observation/documented] Memory is layered: L1 core identity loaded on every request, L2 a memory directory for the planner, and L3 detailed memories retrieved by device type and task before skill execution. -- evidence: [README.md#L165-L167](https://github.com/Fullive-AI/Anima/blob/ea1542ff8420d37089926d558ff0d6cc2174eac8/README.md#L165-L167), [README.md#L158-L160](https://github.com/Fullive-AI/Anima/blob/ea1542ff8420d37089926d558ff0d6cc2174eac8/README.md#L158-L160), [README.md#L162-L163](https://github.com/Fullive-AI/Anima/blob/ea1542ff8420d37089926d558ff0d6cc2174eac8/README.md#L162-L163) (`clm_cc9846b5244a7ee7f2c545ee5cbd6d77e0a722dc20dc5273b0368db3654620a8`)
- [observation/documented] Extracted memories use a schema with claim_type categories (explicit/implicit preferences, routines, aliases, constraints, home context), positive/negative evidence, and status values candidate/confirmed/rejected/stale; only confirmed memory enters skill decisions by default. -- evidence: [README.md#L179-L185](https://github.com/Fullive-AI/Anima/blob/ea1542ff8420d37089926d558ff0d6cc2174eac8/README.md#L179-L185) (`clm_2af37671bd9d163d8a0142d3b9265e01aa97d55f4257982f064e9826f6831d29`)

## orchestration (1 claim(s))

- [observation/documented] The runtime chain is device discovery, sensor/event updates, a rules fast path for safety, an LLM slow path, command execution via adapters, memory/history writes, and dashboard visibility. -- evidence: [ARCHITECTURE_GUARDRAILS.md#L13-L13](https://github.com/Fullive-AI/Anima/blob/ea1542ff8420d37089926d558ff0d6cc2174eac8/ARCHITECTURE_GUARDRAILS.md#L13-L13), [README.md#L92-L92](https://github.com/Fullive-AI/Anima/blob/ea1542ff8420d37089926d558ff0d6cc2174eac8/README.md#L92-L92) (`clm_3925c94946030187bae7ab5c4896b19dd9292b98494c8f077ef30b82c49e9296`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The stack is Python 3.11-3.13 with FastAPI and LangGraph plus a React dashboard; Docker Compose is the recommended deployment, requiring only Docker Desktop or Docker Engine with the Compose plugin. -- evidence: [README.md#L10-L16](https://github.com/Fullive-AI/Anima/blob/ea1542ff8420d37089926d558ff0d6cc2174eac8/README.md#L10-L16), [README.md#L220-L220](https://github.com/Fullive-AI/Anima/blob/ea1542ff8420d37089926d558ff0d6cc2174eac8/README.md#L220-L220) (`clm_9b51c7b503d41e58c67777bcd68227a0a910dc0444c3b5a01c2658667ccae212`)

## limitations (2 claim(s))

- [observation/documented] MIoT command execution depends on each device's reachable local IP and token; Xiaomi Cloud login is mainly for discovery and token acquisition, not universal cloud remote control. -- evidence: [README.md#L200-L200](https://github.com/Fullive-AI/Anima/blob/ea1542ff8420d37089926d558ff0d6cc2174eac8/README.md#L200-L200) (`clm_dcb6f79a76322ed93536504e7876c5d0492ef4b4c1679d92c37873c4674aca7d`)
- [observation/documented] Per AGENT.md, MQTT is not the main production event path, the dashboard is polling-based rather than realtime, room modeling is weak, and chat is narrow task routing rather than a full assistant. -- evidence: [AGENT.md#L211-L212](https://github.com/Fullive-AI/Anima/blob/ea1542ff8420d37089926d558ff0d6cc2174eac8/AGENT.md#L211-L212), [AGENT.md#L205-L207](https://github.com/Fullive-AI/Anima/blob/ea1542ff8420d37089926d558ff0d6cc2174eac8/AGENT.md#L205-L207), [AGENT.md#L221-L222](https://github.com/Fullive-AI/Anima/blob/ea1542ff8420d37089926d558ff0d6cc2174eac8/AGENT.md#L221-L222), [AGENT.md#L216-L217](https://github.com/Fullive-AI/Anima/blob/ea1542ff8420d37089926d558ff0d6cc2174eac8/AGENT.md#L216-L217), [AGENT.md#L41-L45](https://github.com/Fullive-AI/Anima/blob/ea1542ff8420d37089926d558ff0d6cc2174eac8/AGENT.md#L41-L45) (`clm_78b9daea3331e0375dc183432c508859db32ba23556679864b75aa73a34b9cfd`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

