# sonnhfit/sonagent

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 0bccfcbfee88 @ 2a013181a18ec69d

## Summary (orientation draft, not independently verified)

SonAgent is a Python-based autonomous LLM agent ('Digital Consciousness Backup Agent') with a multi-agent registry, per-agent skills, a SkillBuilder that generates and sandbox-tests new skills at runtime, CLI/Docker deployment, and timezone/API-key configuration. Evidence is documentation- and manifest-heavy; no source code slices are present.

## Source coverage

Source coverage (partial): 6 of 12 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 13 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

13 claim(s) across 10 facet(s); 3 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] The project describes itself as an autonomous 'Digital Consciousness Backup Agent' that uses LLMs to safeguard a user's digital presence, with self-editing source code capability. -- evidence: [README.MD#L9-L10](https://github.com/sonnhfit/SonAgent/blob/0bccfcbfee88d0c1cb76096b25f4c4e7cc3d8b58/README.MD#L9-L10)
- components (1 claim(s)):
  - [observation/documented] SkillBuilder consists of a SandboxExecutor that runs code with restricted imports/builtins and no file or network access, a SkillGenerator using templates, and a user-facing SkillBuilder skill with create_simple_skill, generate_skill, and test_skill_code methods. -- evidence: [docs/SKILL_BUILDER.md#L19-L23](https://github.com/sonnhfit/SonAgent/blob/0bccfcbfee88d0c1cb76096b25f4c4e7cc3d8b58/docs/SKILL_BUILDER.md#L19-L23), [docs/SKILL_BUILDER.md#L31-L38](https://github.com/sonnhfit/SonAgent/blob/0bccfcbfee88d0c1cb76096b25f4c4e7cc3d8b58/docs/SKILL_BUILDER.md#L31-L38), [docs/SKILL_BUILDER.md#L150-L154](https://github.com/sonnhfit/SonAgent/blob/0bccfcbfee88d0c1cb76096b25f4c4e7cc3d8b58/docs/SKILL_BUILDER.md#L150-L154), [docs/SKILL_BUILDER.md#L25-L29](https://github.com/sonnhfit/SonAgent/blob/0bccfcbfee88d0c1cb76096b25f4c4e7cc3d8b58/docs/SKILL_BUILDER.md#L25-L29)
- design-choices (2 claim(s)):
  - [observation/documented] The agent's stated design includes belief-based reasoning with LLMs, automatic belief acquisition over time, and learning from human feedback. -- evidence: [README.MD#L15-L15](https://github.com/sonnhfit/SonAgent/blob/0bccfcbfee88d0c1cb76096b25f4c4e7cc3d8b58/README.MD#L15-L15), [README.MD#L19-L19](https://github.com/sonnhfit/SonAgent/blob/0bccfcbfee88d0c1cb76096b25f4c4e7cc3d8b58/README.MD#L19-L19), [README.MD#L17-L17](https://github.com/sonnhfit/SonAgent/blob/0bccfcbfee88d0c1cb76096b25f4c4e7cc3d8b58/README.MD#L17-L17)
  - [observation/documented] Timezone is configurable via config.json or the SONAGENT_TIMEZONE environment variable, with priority env var > config file > default UTC, and any pytz-supported timezone string. -- evidence: [README.MD#L80-L80](https://github.com/sonnhfit/SonAgent/blob/0bccfcbfee88d0c1cb76096b25f4c4e7cc3d8b58/README.MD#L80-L80), [README.MD#L82-L82](https://github.com/sonnhfit/SonAgent/blob/0bccfcbfee88d0c1cb76096b25f4c4e7cc3d8b58/README.MD#L82-L82), [README.MD#L63-L71](https://github.com/sonnhfit/SonAgent/blob/0bccfcbfee88d0c1cb76096b25f4c4e7cc3d8b58/README.MD#L63-L71), [README.MD#L73-L75](https://github.com/sonnhfit/SonAgent/blob/0bccfcbfee88d0c1cb76096b25f4c4e7cc3d8b58/README.MD#L73-L75)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: dev tooling is pinned in requirements-dev.txt (pytest, ruff, mypy, pre-commit, coverage plugins), docs use Sphinx, and Docker images are built by CI to GitHub Container Registry with latest/dev/version/SHA tags. -- evidence: [requirements-dev.txt#L1-L10](https://github.com/sonnhfit/SonAgent/blob/0bccfcbfee88d0c1cb76096b25f4c4e7cc3d8b58/requirements-dev.txt#L1-L10), [README.MD#L147-L147](https://github.com/sonnhfit/SonAgent/blob/0bccfcbfee88d0c1cb76096b25f4c4e7cc3d8b58/README.MD#L147-L147), [README.MD#L149-L152](https://github.com/sonnhfit/SonAgent/blob/0bccfcbfee88d0c1cb76096b25f4c4e7cc3d8b58/README.MD#L149-L152), [docs/requirements.txt#L1-L2](https://github.com/sonnhfit/SonAgent/blob/0bccfcbfee88d0c1cb76096b25f4c4e7cc3d8b58/docs/requirements.txt#L1-L2)
- skills-patterns (2 claim(s)):
  - [observation/documented] Skills come in two types: Python classes inheriting from pydantic BaseModel, and markdown LLM instruction files; skills live in shared or per-agent directories under user_data/skills/. -- evidence: [docs/AGENT_SYSTEM.md#L110-L110](https://github.com/sonnhfit/SonAgent/blob/0bccfcbfee88d0c1cb76096b25f4c4e7cc3d8b58/docs/AGENT_SYSTEM.md#L110-L110), [docs/AGENT_SYSTEM.md#L131-L131](https://github.com/sonnhfit/SonAgent/blob/0bccfcbfee88d0c1cb76096b25f4c4e7cc3d8b58/docs/AGENT_SYSTEM.md#L131-L131), [docs/AGENT_SYSTEM.md#L115-L119](https://github.com/sonnhfit/SonAgent/blob/0bccfcbfee88d0c1cb76096b25f4c4e7cc3d8b58/docs/AGENT_SYSTEM.md#L115-L119), [docs/AGENT_SYSTEM.md#L74-L78](https://github.com/sonnhfit/SonAgent/blob/0bccfcbfee88d0c1cb76096b25f4c4e7cc3d8b58/docs/AGENT_SYSTEM.md#L74-L78)
  - [observation/documented] Standard starter skills (TextPrinter, WeatherAPISkill, HanoiWeatherChecker, SkillBuilder) are copied into user_data/skills/ on first run, and agent-specific starter skills are copied from sonagent/standard_skills/{agent_id}/ at startup. -- evidence: [README.MD#L45-L54](https://github.com/sonnhfit/SonAgent/blob/0bccfcbfee88d0c1cb76096b25f4c4e7cc3d8b58/README.MD#L45-L54), [docs/AGENT_SYSTEM.md#L152-L152](https://github.com/sonnhfit/SonAgent/blob/0bccfcbfee88d0c1cb76096b25f4c4e7cc3d8b58/docs/AGENT_SYSTEM.md#L152-L152), [docs/AGENT_SYSTEM.md#L179-L179](https://github.com/sonnhfit/SonAgent/blob/0bccfcbfee88d0c1cb76096b25f4c4e7cc3d8b58/docs/AGENT_SYSTEM.md#L179-L179)
- interfaces (2 claim(s)):
  - [observation/documented] MainAgent exposes a command-based process interface supporting commands such as create_task, list_tasks, get_task_status, and kill_task, with task priority determining execution order. -- evidence: [docs/AGENT_SYSTEM.md#L334-L334](https://github.com/sonnhfit/SonAgent/blob/0bccfcbfee88d0c1cb76096b25f4c4e7cc3d8b58/docs/AGENT_SYSTEM.md#L334-L334), [docs/AGENT_SYSTEM.md#L247-L251](https://github.com/sonnhfit/SonAgent/blob/0bccfcbfee88d0c1cb76096b25f4c4e7cc3d8b58/docs/AGENT_SYSTEM.md#L247-L251), [docs/AGENT_SYSTEM.md#L230-L235](https://github.com/sonnhfit/SonAgent/blob/0bccfcbfee88d0c1cb76096b25f4c4e7cc3d8b58/docs/AGENT_SYSTEM.md#L230-L235), [docs/AGENT_SYSTEM.md#L241-L244](https://github.com/sonnhfit/SonAgent/blob/0bccfcbfee88d0c1cb76096b25f4c4e7cc3d8b58/docs/AGENT_SYSTEM.md#L241-L244), [docs/AGENT_SYSTEM.md#L238-L238](https://github.com/sonnhfit/SonAgent/blob/0bccfcbfee88d0c1cb76096b25f4c4e7cc3d8b58/docs/AGENT_SYSTEM.md#L238-L238)
  - [observation/documented] The CLI is installed via pip and run with 'sonagent run' taking --config, --agentdb (SQLite), --memory-url, --user-data-dir, and --log-level options; 'sonagent init' creates the user_data folder. -- evidence: [README.MD#L32-L34](https://github.com/sonnhfit/SonAgent/blob/0bccfcbfee88d0c1cb76096b25f4c4e7cc3d8b58/README.MD#L32-L34), [README.MD#L38-L43](https://github.com/sonnhfit/SonAgent/blob/0bccfcbfee88d0c1cb76096b25f4c4e7cc3d8b58/README.MD#L38-L43), [README.MD#L56-L58](https://github.com/sonnhfit/SonAgent/blob/0bccfcbfee88d0c1cb76096b25f4c4e7cc3d8b58/README.MD#L56-L58), [README.MD#L45-L54](https://github.com/sonnhfit/SonAgent/blob/0bccfcbfee88d0c1cb76096b25f4c4e7cc3d8b58/README.MD#L45-L54)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (1 claim(s)):
More evidence: [full detail](sonagent.detail.md)

Metadata and full claim list: [full detail](sonagent.detail.md)
Human notes ([notes](sonagent.notes.md), never overwritten by build)

[Back to map index](../../index.md)
