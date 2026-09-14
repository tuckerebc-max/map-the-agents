---
access: public
aliases: []
claim_ids:
- clm_06405e215164ce2eee204a8d34f104f9b82000b7701f5826b40c433434640fe2
- clm_06600a8f74483dae422fb5578d4dc1450ebbdf8a05eadbb5f6e71f8721df90af
- clm_4d874d5587c55ca25a693d0243d4edcef81a613a208b86b6e9e0b6316c58389e
- clm_a8c01500d523ac607337e643fad125b019d32962c5bcaa878c04d8433394b6d0
maturity: draft
page_id: pg_2f34849cac0b5a13ac691a5304eb4b39
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_08c70c6c1b715325bb5eba7f37f1f832
title: sonnhfit/SonAgent/docs/AGENT_SYSTEM.md @ 0bccfcbfee88
updated_at: '2026-09-14T02:42:06Z'
---

# sonnhfit/SonAgent/docs/AGENT_SYSTEM.md @ 0bccfcbfee88

<!-- rcw:begin owner=source:src_08c70c6c1b715325bb5eba7f37f1f832 block=evidence -->
- A multi-agent architecture includes a central AgentRegistry for registration, status tracking, and inter-agent message passing, plus a MainAgent coordinator that creates, assigns, and monitors tasks for sub-agents. [@claim:clm_06405e215164ce2eee204a8d34f104f9b82000b7701f5826b40c433434640fe2]
- Standard starter skills (TextPrinter, WeatherAPISkill, HanoiWeatherChecker, SkillBuilder) are copied into user_data/skills/ on first run, and agent-specific starter skills are copied from sonagent/standard_skills/{agent_id}/ at startup. [@claim:clm_06600a8f74483dae422fb5578d4dc1450ebbdf8a05eadbb5f6e71f8721df90af]
- MainAgent exposes a command-based process interface supporting commands such as create_task, list_tasks, get_task_status, and kill_task, with task priority determining execution order. [@claim:clm_4d874d5587c55ca25a693d0243d4edcef81a613a208b86b6e9e0b6316c58389e]
- Skills come in two types: Python classes inheriting from pydantic BaseModel, and markdown LLM instruction files; skills live in shared or per-agent directories under user_data/skills/. [@claim:clm_a8c01500d523ac607337e643fad125b019d32962c5bcaa878c04d8433394b6d0]
<!-- rcw:end owner=source:src_08c70c6c1b715325bb5eba7f37f1f832 block=evidence -->

## Researcher notes

