---
access: public
aliases: []
claim_ids:
- clm_22757dbdc65ec7c526af68ee4406f21c91fe0ee02db4950f0799913436079911
- clm_3c21d5a18011a11c22414a065f4dffae4da7dd26c46c1223b10a1f700c0ead63
- clm_3e7d4a05b3565367525b2c4769be0c67bb3b7538b958f961fd9f7aaa8183ee36
- clm_47fa4abba9d1c0b515ef01cc90c62f319663f0fba29dffe859c952c2760bf3be
- clm_5b69c1c73c9e93cec290ab254119960f0455db58a746f5c53b211ecdd8c5f57c
- clm_7dd718f1737cfa1fc13010b534ba5161f4e75ee5361229db968eeedd3b482d56
- clm_8e8b297f66679588a73bc51e21c7144919f7b28e91cd81e7937c77d729284d89
- clm_a0ecbb78afd35417b6e76252c23084651d223461b88c242e37daf64035ab9a84
- clm_b86f56d76785dd4533a77ac945c6ef48bfc9df226367060bf8b1e88ccd508516
- clm_d4593cf1bb68cd89008d24ffa0939979c7976f354c712dd2d890ee6844488755
maturity: draft
page_id: pg_aee7c8f12f0254d89811ab8871b2eee5
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_07338b95b48959f0b85c915869bf7cff
title: sagiyaacoby/TeamHero/README.md @ 25466cdbfbcf
updated_at: '2026-09-14T02:37:45Z'
---

# sagiyaacoby/TeamHero/README.md @ 25466cdbfbcf

<!-- rcw:begin owner=source:src_07338b95b48959f0b85c915869bf7cff block=evidence -->
- The project targets developers working with Claude Code who want structure around their agents, and it is a builder platform requiring comfort with CLI and Node.js. [@claim:clm_22757dbdc65ec7c526af68ee4406f21c91fe0ee02db4950f0799913436079911]
- Each agent is documented to have persistent short- and long-term memory that carries across sessions. [@claim:clm_3c21d5a18011a11c22414a065f4dffae4da7dd26c46c1223b10a1f700c0ead63]
- The platform includes a web dashboard for managing an agent team, a Command Center terminal for talking to an orchestrator agent, a task system with plans, versions, approvals and deliverable tracking, agent memory, a knowledge base, optional skills, and file-scope conflict prevention. [@claim:clm_3e7d4a05b3565367525b2c4769be0c67bb3b7538b958f961fd9f7aaa8183ee36]
- Prerequisites are Node.js 18+ and the Claude CLI, described as the AI backbone powering the agents; the Claude CLI is installed globally via npm. [@claim:clm_47fa4abba9d1c0b515ef01cc90c62f319663f0fba29dffe859c952c2760bf3be]
- After launching via launch.bat on Windows or bash launch.sh on Mac/Linux, the dashboard is served at http://localhost:3777. [@claim:clm_5b69c1c73c9e93cec290ab254119960f0455db58a746f5c53b211ecdd8c5f57c]
- Skills are optional integrations such as browser automation and GitHub; the changelog also mentions a skills UI separating curated from user-installed skills and a Vercel CLI skill in the catalog. [@claim:clm_7dd718f1737cfa1fc13010b534ba5161f4e75ee5361229db968eeedd3b482d56]
- The project is released under the MIT License, with TeamHero and Kapow noted as trademarks of Sagi Yaacoby. [@claim:clm_8e8b297f66679588a73bc51e21c7144919f7b28e91cd81e7937c77d729284d89]
- The project positions itself around managing agents rather than creating them, emphasizing plans before execution, tracked deliverables, conflict prevention, and a single source of truth for team state. [@claim:clm_a0ecbb78afd35417b6e76252c23084651d223461b88c242e37daf64035ab9a84]
- Repository development practice: contributions are welcome under guidelines in CONTRIBUTING.md, and a code of conduct adapted from the Contributor Covenant applies to issues, pull requests, and discussions, with violations reportable to conduct@myteamhero.com. [@claim:clm_b86f56d76785dd4533a77ac945c6ef48bfc9df226367060bf8b1e88ccd508516]
- Tasks follow a plan, review, execute, and deliver lifecycle, and every file an agent will touch is declared upfront so agents do not overwrite each other's work. [@claim:clm_d4593cf1bb68cd89008d24ffa0939979c7976f354c712dd2d890ee6844488755]
<!-- rcw:end owner=source:src_07338b95b48959f0b85c915869bf7cff block=evidence -->

## Researcher notes

