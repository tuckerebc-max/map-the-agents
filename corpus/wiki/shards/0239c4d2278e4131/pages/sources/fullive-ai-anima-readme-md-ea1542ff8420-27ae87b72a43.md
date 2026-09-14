---
access: public
aliases: []
claim_ids:
- clm_06c1ddab72c98cb7ae04d2a0a4338c012c93c39dd4bb96b75e90300769f9c015
- clm_0bfbc75d615a2cecf48f59390929509be33027166156568dcfb249a83a42a76e
- clm_2af37671bd9d163d8a0142d3b9265e01aa97d55f4257982f064e9826f6831d29
- clm_3925c94946030187bae7ab5c4896b19dd9292b98494c8f077ef30b82c49e9296
- clm_3a845cbbe42e0dbab1b9910a112b73e90d5b4b8825b52114fe6bae39db771b91
- clm_3cc0c015e1d3d540c24426639c96a0e46790fe4e6630f6827b1389e96558072e
- clm_4dd9ff3566948e4f7a033d05a2775970da5d48c66c8305cf750c4a48e8faa60a
- clm_9b51c7b503d41e58c67777bcd68227a0a910dc0444c3b5a01c2658667ccae212
- clm_9f7cebc7de082417d4e66dbf9851a0ded38ceeb64b50e8d3bc6fe47c09d7a1a9
- clm_c2a37ddc35ea3edae99c44735ac7b4ff4032d906d0b0f84365cbbbe71ca98a16
- clm_cc9846b5244a7ee7f2c545ee5cbd6d77e0a722dc20dc5273b0368db3654620a8
- clm_dcb6f79a76322ed93536504e7876c5d0492ef4b4c1679d92c37873c4674aca7d
maturity: draft
page_id: pg_204f072d322b5fb0a4d627ae87b72a43
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_6b0f225720f35491b2bcfe2b16b66859
title: Fullive-AI/Anima/README.md @ ea1542ff8420
updated_at: '2026-09-14T03:51:44Z'
---

# Fullive-AI/Anima/README.md @ ea1542ff8420

<!-- rcw:begin owner=source:src_6b0f225720f35491b2bcfe2b16b66859 block=evidence -->
- Built-in skills include light, humidifier, air_conditioner, air_purifier, speaker, coordinator, device_discovery, and skill_creator; custom skills can be added under skills/custom/. [@claim:clm_06c1ddab72c98cb7ae04d2a0a4338c012c93c39dd4bb96b75e90300769f9c015]
- Anima is described as an open-source Agent OS for intelligent hardware, aiming to give home devices perceptive, decision-making, learning, and extensible AI capabilities rather than being a device control panel. [@claim:clm_0bfbc75d615a2cecf48f59390929509be33027166156568dcfb249a83a42a76e]
- Extracted memories use a schema with claim_type categories (explicit/implicit preferences, routines, aliases, constraints, home context), positive/negative evidence, and status values candidate/confirmed/rejected/stale; only confirmed memory enters skill decisions by default. [@claim:clm_2af37671bd9d163d8a0142d3b9265e01aa97d55f4257982f064e9826f6831d29]
- The runtime chain is device discovery, sensor/event updates, a rules fast path for safety, an LLM slow path, command execution via adapters, memory/history writes, and dashboard visibility. [@claim:clm_3925c94946030187bae7ab5c4896b19dd9292b98494c8f077ef30b82c49e9296]
- The Brain is designed to decide within explicit skill boundaries, device capabilities, and safety rules rather than letting an LLM control devices freely. [@claim:clm_3a845cbbe42e0dbab1b9910a112b73e90d5b4b8825b52114fe6bae39db771b91]
- The backend exposes REST endpoints including /health, /api/devices, /api/chat, /api/environment, /api/scan, /api/memory, /api/settings, and Xiaomi QR login start/poll endpoints, with Swagger at localhost:8080/docs. [@claim:clm_3cc0c015e1d3d540c24426639c96a0e46790fe4e6630f6827b1389e96558072e]
- LLM integration is OpenAI-compatible, configured via ANIMA_LLM_API_KEY and optionally ANIMA_LLM_BASE_URL, supporting OpenAI, DeepSeek, Doubao, proxied Anthropic, and Ollama-compatible endpoints. [@claim:clm_4dd9ff3566948e4f7a033d05a2775970da5d48c66c8305cf750c4a48e8faa60a]
- The stack is Python 3.11-3.13 with FastAPI and LangGraph plus a React dashboard; Docker Compose is the recommended deployment, requiring only Docker Desktop or Docker Engine with the Compose plugin. [@claim:clm_9b51c7b503d41e58c67777bcd68227a0a910dc0444c3b5a01c2658667ccae212]
- The runtime comprises a Brain decision layer, device Skills, a layered Memory system, hardware Adapters, a FastAPI backend, and a React dashboard; core/main.py is the composition root and startup entrypoint. [@claim:clm_9f7cebc7de082417d4e66dbf9851a0ded38ceeb64b50e8d3bc6fe47c09d7a1a9]
- Skills are device domain-knowledge packages with a defined layout: SKILL.md metadata, references (knowledge, decide, learn prompts), and scripts/actions.py as the structured action execution entrypoint. [@claim:clm_c2a37ddc35ea3edae99c44735ac7b4ff4032d906d0b0f84365cbbbe71ca98a16]
- Memory is layered: L1 core identity loaded on every request, L2 a memory directory for the planner, and L3 detailed memories retrieved by device type and task before skill execution. [@claim:clm_cc9846b5244a7ee7f2c545ee5cbd6d77e0a722dc20dc5273b0368db3654620a8]
- MIoT command execution depends on each device's reachable local IP and token; Xiaomi Cloud login is mainly for discovery and token acquisition, not universal cloud remote control. [@claim:clm_dcb6f79a76322ed93536504e7876c5d0492ef4b4c1679d92c37873c4674aca7d]
<!-- rcw:end owner=source:src_6b0f225720f35491b2bcfe2b16b66859 block=evidence -->

## Researcher notes

