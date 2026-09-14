# 101dotxyz/gpteam

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit a216364ea2db @ 10cf6cc6e085a03c

## Summary (orientation draft, not independently verified)

GPTeam is a GPT-4-based multi-agent simulation where agents with memory collaborate on tasks in a configurable world, with optional Discord integration and alternative LLM backends. Evidence is mostly README/DISCORD.md documentation; no code slices are present.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] GPTeam uses GPT-4 to create multiple agents that collaborate to achieve predefined goals, aiming to explore GPT models' potential for multi-agent productivity and communication. -- evidence: [README.md#L21-L21](https://github.com/101dotxyz/GPTeam/blob/a216364ea2dbb208e6501468c5e5b791594cc3d5/README.md#L21-L21)
- components (1 claim(s)):
  - [observation/documented] Each agent has its own memory and uses communication as a tool; agent memory and reflection are inspired by a cited research paper (arXiv 2304.03442). -- evidence: [README.md#L43-L43](https://github.com/101dotxyz/GPTeam/blob/a216364ea2dbb208e6501468c5e5b791594cc3d5/README.md#L43-L43)
- design-choices (1 claim(s)):
  - [observation/documented] A --turbo flag runs all LLM calls with gpt3.5-turbo for lower cost, at the cost of worse results; a --claude flag uses claude-v1 and claude-v1-instant for some calls. -- evidence: [README.md#L37-L37](https://github.com/101dotxyz/GPTeam/blob/a216364ea2dbb208e6501468c5e5b791594cc3d5/README.md#L37-L37), [README.md#L63-L63](https://github.com/101dotxyz/GPTeam/blob/a216364ea2dbb208e6501468c5e5b791594cc3d5/README.md#L63-L63)
- workflows (2 claim(s)):
  - [observation/documented] Discord setup requires channel IDs per location in .env as <LOCATION_NAME>_CHANNEL_ID and bot tokens as <BOT_FIRST_NAME>_DISCORD_TOKEN, with the announcer bot needing Message Content Intent enabled. -- evidence: [DISCORD.md#L11-L22](https://github.com/101dotxyz/GPTeam/blob/a216364ea2dbb208e6501468c5e5b791594cc3d5/DISCORD.md#L11-L22), [DISCORD.md#L33-L49](https://github.com/101dotxyz/GPTeam/blob/a216364ea2dbb208e6501468c5e5b791594cc3d5/DISCORD.md#L33-L49)
  - [observation/documented] Repository development practice: contributors are asked to fork the repository, create a branch, implement changes, and submit a pull request, which maintainers will review with feedback. -- evidence: [README.md#L73-L76](https://github.com/101dotxyz/GPTeam/blob/a216364ea2dbb208e6501468c5e5b791594cc3d5/README.md#L73-L76), [README.md#L78-L78](https://github.com/101dotxyz/GPTeam/blob/a216364ea2dbb208e6501468c5e5b791594cc3d5/README.md#L78-L78)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The world is configured via a config.json file listing available agents and locations; after editing it, users reset the database and relaunch the world. -- evidence: [README.md#L53-L55](https://github.com/101dotxyz/GPTeam/blob/a216364ea2dbb208e6501468c5e5b791594cc3d5/README.md#L53-L55)
  - [observation/documented] While the world runs, each agent's current state is written to a text file in the agents/ folder, letting users observe what agents are doing. -- evidence: [README.md#L47-L47](https://github.com/101dotxyz/GPTeam/blob/a216364ea2dbb208e6501468c5e5b791594cc3d5/README.md#L47-L47)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (1 claim(s)):
  - [observation/documented] Agents move around the world, perform tasks in different locations depending on their activity and other agents' positions, and can speak to each other and collaborate on tasks in parallel. -- evidence: [README.md#L43-L43](https://github.com/101dotxyz/GPTeam/blob/a216364ea2dbb208e6501468c5e5b791594cc3d5/README.md#L43-L43)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
  - [observation/documented] The project requires an OpenAI API key in .env; supplying keys for optional services enables additional tools, and the project is managed with Poetry. -- evidence: [README.md#L31-L35](https://github.com/101dotxyz/GPTeam/blob/a216364ea2dbb208e6501468c5e5b791594cc3d5/README.md#L31-L35)
  - [observation/documented] The project is licensed under the MIT license. -- evidence: [README.md#L82-L82](https://github.com/101dotxyz/GPTeam/blob/a216364ea2dbb208e6501468c5e5b791594cc3d5/README.md#L82-L82)
- limitations (1 claim(s)):
More evidence: [full detail](gpteam.detail.md)

Metadata and full claim list: [full detail](gpteam.detail.md)
Human notes ([notes](gpteam.notes.md), never overwritten by build)

[Back to map index](../../index.md)
