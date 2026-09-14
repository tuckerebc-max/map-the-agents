---
access: public
aliases: []
claim_ids:
- clm_0796b574aa6f62adf45f6e30089f41e2ac23bac3cc5c8af30df4fb4d157c5623
- clm_0dfb3000c6bce7b9f4e983f460679c1aaa4107d3f595df810ec086aa159562e0
- clm_1cf27595c5566683e6ec00f65671a5e091abfea36982c20dac59f54a8c5bfcfb
- clm_4c613ada48f3bb0afd4be8f9e0c88789e7cb61016be21813a3cc1825208a9b6e
- clm_8f96e7e793fad84452f741e87c2de3ea7568e9ac4623487ecda4e1de36eee36e
- clm_9475ffb2e42d460f17b245b53b7db8b5611fcc8546307e95910439ba5c34e2b5
- clm_9daa50338107ff699ba6e9127d46b042e5a2625eec6f34e4b2afd4bdcbde98d1
- clm_9effc15bd611862f9b34dc1caad046decaf2d1c8fc0ac9d394b01279358cace3
- clm_dabfbb500c8ff207d94cff8e8fdcbaabf277c7ee441354e8ee0ca8679698b68e
maturity: draft
page_id: pg_f106447d768c531e9cafb0c9601e57eb
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_ca7384f550775d82b359b3ed9fb67ee6
title: 101dotxyz/GPTeam/README.md @ a216364ea2db
updated_at: '2026-09-14T03:28:23Z'
---

# 101dotxyz/GPTeam/README.md @ a216364ea2db

<!-- rcw:begin owner=source:src_ca7384f550775d82b359b3ed9fb67ee6 block=evidence -->
- Repository development practice: contributors are asked to fork the repository, create a branch, implement changes, and submit a pull request, which maintainers will review with feedback. [@claim:clm_0796b574aa6f62adf45f6e30089f41e2ac23bac3cc5c8af30df4fb4d157c5623]
- While the world runs, each agent's current state is written to a text file in the agents/ folder, letting users observe what agents are doing. [@claim:clm_0dfb3000c6bce7b9f4e983f460679c1aaa4107d3f595df810ec086aa159562e0]
- GPTeam uses GPT-4 to create multiple agents that collaborate to achieve predefined goals, aiming to explore GPT models' potential for multi-agent productivity and communication. [@claim:clm_1cf27595c5566683e6ec00f65671a5e091abfea36982c20dac59f54a8c5bfcfb]
- The project requires an OpenAI API key in .env; supplying keys for optional services enables additional tools, and the project is managed with Poetry. [@claim:clm_4c613ada48f3bb0afd4be8f9e0c88789e7cb61016be21813a3cc1825208a9b6e]
- The world is configured via a config.json file listing available agents and locations; after editing it, users reset the database and relaunch the world. [@claim:clm_8f96e7e793fad84452f741e87c2de3ea7568e9ac4623487ecda4e1de36eee36e]
- A --turbo flag runs all LLM calls with gpt3.5-turbo for lower cost, at the cost of worse results; a --claude flag uses claude-v1 and claude-v1-instant for some calls. [@claim:clm_9475ffb2e42d460f17b245b53b7db8b5611fcc8546307e95910439ba5c34e2b5]
- Agents move around the world, perform tasks in different locations depending on their activity and other agents' positions, and can speak to each other and collaborate on tasks in parallel. [@claim:clm_9daa50338107ff699ba6e9127d46b042e5a2625eec6f34e4b2afd4bdcbde98d1]
- Each agent has its own memory and uses communication as a tool; agent memory and reflection are inspired by a cited research paper (arXiv 2304.03442). [@claim:clm_9effc15bd611862f9b34dc1caad046decaf2d1c8fc0ac9d394b01279358cace3]
- The project is licensed under the MIT license. [@claim:clm_dabfbb500c8ff207d94cff8e8fdcbaabf277c7ee441354e8ee0ca8679698b68e]
<!-- rcw:end owner=source:src_ca7384f550775d82b359b3ed9fb67ee6 block=evidence -->

## Researcher notes

