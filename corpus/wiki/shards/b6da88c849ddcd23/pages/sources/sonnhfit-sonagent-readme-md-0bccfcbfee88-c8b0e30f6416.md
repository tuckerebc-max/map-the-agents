---
access: public
aliases: []
claim_ids:
- clm_06600a8f74483dae422fb5578d4dc1450ebbdf8a05eadbb5f6e71f8721df90af
- clm_3a98cc0826a69cb4b3afb3af77d1fdb3d766487393c6e111f4979764415da4f2
- clm_5ad149584e62ab0e18c56936144f65417ac08e36a804911d599caefebfbde68d
- clm_ba73c85060de8b39d8df65972d6e2c609b1903c5b1952d927a4613cb92f0b0b3
- clm_d68420b789dcb729d754beb23c7b8e45b49b4bcf05aa95c089a67d805ded3f49
- clm_de35cdd140713252a9bcadbff29f35112c4d980fad4deab5dc719422f9ca98ba
maturity: draft
page_id: pg_cf0e03bfa26355169f22c8b0e30f6416
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_309e8dd55d845735830d71163aa1da1c
title: sonnhfit/SonAgent/README.MD @ 0bccfcbfee88
updated_at: '2026-09-14T02:42:06Z'
---

# sonnhfit/SonAgent/README.MD @ 0bccfcbfee88

<!-- rcw:begin owner=source:src_309e8dd55d845735830d71163aa1da1c block=evidence -->
- Standard starter skills (TextPrinter, WeatherAPISkill, HanoiWeatherChecker, SkillBuilder) are copied into user_data/skills/ on first run, and agent-specific starter skills are copied from sonagent/standard_skills/{agent_id}/ at startup. [@claim:clm_06600a8f74483dae422fb5578d4dc1450ebbdf8a05eadbb5f6e71f8721df90af]
- The project describes itself as an autonomous 'Digital Consciousness Backup Agent' that uses LLMs to safeguard a user's digital presence, with self-editing source code capability. [@claim:clm_3a98cc0826a69cb4b3afb3af77d1fdb3d766487393c6e111f4979764415da4f2]
- The agent's stated design includes belief-based reasoning with LLMs, automatic belief acquisition over time, and learning from human feedback. [@claim:clm_5ad149584e62ab0e18c56936144f65417ac08e36a804911d599caefebfbde68d]
- The CLI is installed via pip and run with 'sonagent run' taking --config, --agentdb (SQLite), --memory-url, --user-data-dir, and --log-level options; 'sonagent init' creates the user_data folder. [@claim:clm_ba73c85060de8b39d8df65972d6e2c609b1903c5b1952d927a4613cb92f0b0b3]
- Repository development practice: dev tooling is pinned in requirements-dev.txt (pytest, ruff, mypy, pre-commit, coverage plugins), docs use Sphinx, and Docker images are built by CI to GitHub Container Registry with latest/dev/version/SHA tags. [@claim:clm_d68420b789dcb729d754beb23c7b8e45b49b4bcf05aa95c089a67d805ded3f49]
- Timezone is configurable via config.json or the SONAGENT_TIMEZONE environment variable, with priority env var > config file > default UTC, and any pytz-supported timezone string. [@claim:clm_de35cdd140713252a9bcadbff29f35112c4d980fad4deab5dc719422f9ca98ba]
<!-- rcw:end owner=source:src_309e8dd55d845735830d71163aa1da1c block=evidence -->

## Researcher notes

