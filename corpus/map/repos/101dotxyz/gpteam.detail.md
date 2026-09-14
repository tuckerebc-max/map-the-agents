# 101dotxyz/gpteam -- full detail

[Back to orientation](gpteam.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/101dotxyz/gpteam/a216364ea2dbb208e6501468c5e5b791594cc3d5/10cf6cc6e085a03c.json](../../../wiki/dossiers/101dotxyz/gpteam/a216364ea2dbb208e6501468c5e5b791594cc3d5/10cf6cc6e085a03c.json)

## specifications (1 claim(s))

- [observation/documented] GPTeam uses GPT-4 to create multiple agents that collaborate to achieve predefined goals, aiming to explore GPT models' potential for multi-agent productivity and communication. -- evidence: [README.md#L21-L21](https://github.com/101dotxyz/GPTeam/blob/a216364ea2dbb208e6501468c5e5b791594cc3d5/README.md#L21-L21) (`clm_1cf27595c5566683e6ec00f65671a5e091abfea36982c20dac59f54a8c5bfcfb`)

## components (1 claim(s))

- [observation/documented] Each agent has its own memory and uses communication as a tool; agent memory and reflection are inspired by a cited research paper (arXiv 2304.03442). -- evidence: [README.md#L43-L43](https://github.com/101dotxyz/GPTeam/blob/a216364ea2dbb208e6501468c5e5b791594cc3d5/README.md#L43-L43) (`clm_9effc15bd611862f9b34dc1caad046decaf2d1c8fc0ac9d394b01279358cace3`)

## design-choices (1 claim(s))

- [observation/documented] A --turbo flag runs all LLM calls with gpt3.5-turbo for lower cost, at the cost of worse results; a --claude flag uses claude-v1 and claude-v1-instant for some calls. -- evidence: [README.md#L37-L37](https://github.com/101dotxyz/GPTeam/blob/a216364ea2dbb208e6501468c5e5b791594cc3d5/README.md#L37-L37), [README.md#L63-L63](https://github.com/101dotxyz/GPTeam/blob/a216364ea2dbb208e6501468c5e5b791594cc3d5/README.md#L63-L63) (`clm_9475ffb2e42d460f17b245b53b7db8b5611fcc8546307e95910439ba5c34e2b5`)

## workflows (2 claim(s))

- [observation/documented] Discord setup requires channel IDs per location in .env as <LOCATION_NAME>_CHANNEL_ID and bot tokens as <BOT_FIRST_NAME>_DISCORD_TOKEN, with the announcer bot needing Message Content Intent enabled. -- evidence: [DISCORD.md#L11-L22](https://github.com/101dotxyz/GPTeam/blob/a216364ea2dbb208e6501468c5e5b791594cc3d5/DISCORD.md#L11-L22), [DISCORD.md#L33-L49](https://github.com/101dotxyz/GPTeam/blob/a216364ea2dbb208e6501468c5e5b791594cc3d5/DISCORD.md#L33-L49) (`clm_3a0733c8f0467b61f304c90ef7e1da85b21811d5c0f521d09ca2b5429858a6d5`)
- [observation/documented] Repository development practice: contributors are asked to fork the repository, create a branch, implement changes, and submit a pull request, which maintainers will review with feedback. -- evidence: [README.md#L73-L76](https://github.com/101dotxyz/GPTeam/blob/a216364ea2dbb208e6501468c5e5b791594cc3d5/README.md#L73-L76), [README.md#L78-L78](https://github.com/101dotxyz/GPTeam/blob/a216364ea2dbb208e6501468c5e5b791594cc3d5/README.md#L78-L78) (`clm_0796b574aa6f62adf45f6e30089f41e2ac23bac3cc5c8af30df4fb4d157c5623`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The world is configured via a config.json file listing available agents and locations; after editing it, users reset the database and relaunch the world. -- evidence: [README.md#L53-L55](https://github.com/101dotxyz/GPTeam/blob/a216364ea2dbb208e6501468c5e5b791594cc3d5/README.md#L53-L55) (`clm_8f96e7e793fad84452f741e87c2de3ea7568e9ac4623487ecda4e1de36eee36e`)
- [observation/documented] While the world runs, each agent's current state is written to a text file in the agents/ folder, letting users observe what agents are doing. -- evidence: [README.md#L47-L47](https://github.com/101dotxyz/GPTeam/blob/a216364ea2dbb208e6501468c5e5b791594cc3d5/README.md#L47-L47) (`clm_0dfb3000c6bce7b9f4e983f460679c1aaa4107d3f595df810ec086aa159562e0`)
- [observation/documented] In the Discord integration, each world maps to a Discord guild, each location to a channel, each agent to a separate bot application, plus an announcer bot that announces agent movement between rooms. -- evidence: [DISCORD.md#L3-L8](https://github.com/101dotxyz/GPTeam/blob/a216364ea2dbb208e6501468c5e5b791594cc3d5/DISCORD.md#L3-L8) (`clm_5e73729f5f75557f071987b963f5d208d9f4cab32f3c0329281a5417ec006634`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (1 claim(s))

- [observation/documented] Agents move around the world, perform tasks in different locations depending on their activity and other agents' positions, and can speak to each other and collaborate on tasks in parallel. -- evidence: [README.md#L43-L43](https://github.com/101dotxyz/GPTeam/blob/a216364ea2dbb208e6501468c5e5b791594cc3d5/README.md#L43-L43) (`clm_9daa50338107ff699ba6e9127d46b042e5a2625eec6f34e4b2afd4bdcbde98d1`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] The project requires an OpenAI API key in .env; supplying keys for optional services enables additional tools, and the project is managed with Poetry. -- evidence: [README.md#L31-L35](https://github.com/101dotxyz/GPTeam/blob/a216364ea2dbb208e6501468c5e5b791594cc3d5/README.md#L31-L35) (`clm_4c613ada48f3bb0afd4be8f9e0c88789e7cb61016be21813a3cc1825208a9b6e`)
- [observation/documented] The project is licensed under the MIT license. -- evidence: [README.md#L82-L82](https://github.com/101dotxyz/GPTeam/blob/a216364ea2dbb208e6501468c5e5b791594cc3d5/README.md#L82-L82) (`clm_dabfbb500c8ff207d94cff8e8fdcbaabf277c7ee441354e8ee0ca8679698b68e`)

## limitations (1 claim(s))

- [observation/documented] The Discord bot configuration guide is described as basic, and running the Discord bots in production is stated to be at the user's own risk with permissions to be optimized as needed. -- evidence: [DISCORD.md#L25-L27](https://github.com/101dotxyz/GPTeam/blob/a216364ea2dbb208e6501468c5e5b791594cc3d5/DISCORD.md#L25-L27) (`clm_0f30224cd5a009b77255ff4acd4cf574d153af37c74d0a7324aa97232b3c6dfc`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

