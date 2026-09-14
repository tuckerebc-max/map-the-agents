# sagiyaacoby/teamhero -- full detail

[Back to orientation](teamhero.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/sagiyaacoby/teamhero/25466cdbfbcf44577d78a287077aaa3a92071036/d87a745d3ec5f54b.json](../../../wiki/dossiers/sagiyaacoby/teamhero/25466cdbfbcf44577d78a287077aaa3a92071036/d87a745d3ec5f54b.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The platform includes a web dashboard for managing an agent team, a Command Center terminal for talking to an orchestrator agent, a task system with plans, versions, approvals and deliverable tracking, agent memory, a knowledge base, optional skills, and file-scope conflict prevention. -- evidence: [README.md#L23-L29](https://github.com/sagiyaacoby/TeamHero/blob/25466cdbfbcf44577d78a287077aaa3a92071036/README.md#L23-L29) (`clm_3e7d4a05b3565367525b2c4769be0c67bb3b7538b958f961fd9f7aaa8183ee36`)

## design-choices (1 claim(s))

- [observation/documented] The project positions itself around managing agents rather than creating them, emphasizing plans before execution, tracked deliverables, conflict prevention, and a single source of truth for team state. -- evidence: [README.md#L35-L35](https://github.com/sagiyaacoby/TeamHero/blob/25466cdbfbcf44577d78a287077aaa3a92071036/README.md#L35-L35) (`clm_a0ecbb78afd35417b6e76252c23084651d223461b88c242e37daf64035ab9a84`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributions are welcome under guidelines in CONTRIBUTING.md, and a code of conduct adapted from the Contributor Covenant applies to issues, pull requests, and discussions, with violations reportable to conduct@myteamhero.com. -- evidence: [README.md#L86-L86](https://github.com/sagiyaacoby/TeamHero/blob/25466cdbfbcf44577d78a287077aaa3a92071036/README.md#L86-L86), [CODE_OF_CONDUCT.md#L34-L34](https://github.com/sagiyaacoby/TeamHero/blob/25466cdbfbcf44577d78a287077aaa3a92071036/CODE_OF_CONDUCT.md#L34-L34), [CODE_OF_CONDUCT.md#L28-L28](https://github.com/sagiyaacoby/TeamHero/blob/25466cdbfbcf44577d78a287077aaa3a92071036/CODE_OF_CONDUCT.md#L28-L28), [CODE_OF_CONDUCT.md#L24-L24](https://github.com/sagiyaacoby/TeamHero/blob/25466cdbfbcf44577d78a287077aaa3a92071036/CODE_OF_CONDUCT.md#L24-L24) (`clm_b86f56d76785dd4533a77ac945c6ef48bfc9df226367060bf8b1e88ccd508516`)

## skills-patterns (1 claim(s))

- [observation/documented] Skills are optional integrations such as browser automation and GitHub; the changelog also mentions a skills UI separating curated from user-installed skills and a Vercel CLI skill in the catalog. -- evidence: [CHANGELOG.md#L65-L74](https://github.com/sagiyaacoby/TeamHero/blob/25466cdbfbcf44577d78a287077aaa3a92071036/CHANGELOG.md#L65-L74), [README.md#L23-L29](https://github.com/sagiyaacoby/TeamHero/blob/25466cdbfbcf44577d78a287077aaa3a92071036/README.md#L23-L29) (`clm_7dd718f1737cfa1fc13010b534ba5161f4e75ee5361229db968eeedd3b482d56`)

## interfaces (2 claim(s))

- [observation/documented] After launching via launch.bat on Windows or bash launch.sh on Mac/Linux, the dashboard is served at http://localhost:3777. -- evidence: [README.md#L75-L78](https://github.com/sagiyaacoby/TeamHero/blob/25466cdbfbcf44577d78a287077aaa3a92071036/README.md#L75-L78), [README.md#L80-L80](https://github.com/sagiyaacoby/TeamHero/blob/25466cdbfbcf44577d78a287077aaa3a92071036/README.md#L80-L80), [README.md#L70-L73](https://github.com/sagiyaacoby/TeamHero/blob/25466cdbfbcf44577d78a287077aaa3a92071036/README.md#L70-L73) (`clm_5b69c1c73c9e93cec290ab254119960f0455db58a746f5c53b211ecdd8c5f57c`)
- [observation/documented] The task lifecycle uses statuses including planning, pending_approval, working, done, and closed, with simplified transition actions (Accept, Improve, Hold, Cancel) and a done-to-closed auto-lifecycle on a 2-day timer. -- evidence: [CHANGELOG.md#L65-L74](https://github.com/sagiyaacoby/TeamHero/blob/25466cdbfbcf44577d78a287077aaa3a92071036/CHANGELOG.md#L65-L74) (`clm_d100b75e8a5618dad61497b6a184e564733b6b1251eca9e64ba7bc28790cdc47`)

## memory-state (1 claim(s))

- [observation/documented] Each agent is documented to have persistent short- and long-term memory that carries across sessions. -- evidence: [CHANGELOG.md#L116-L119](https://github.com/sagiyaacoby/TeamHero/blob/25466cdbfbcf44577d78a287077aaa3a92071036/CHANGELOG.md#L116-L119), [README.md#L23-L29](https://github.com/sagiyaacoby/TeamHero/blob/25466cdbfbcf44577d78a287077aaa3a92071036/README.md#L23-L29) (`clm_3c21d5a18011a11c22414a065f4dffae4da7dd26c46c1223b10a1f700c0ead63`)

## orchestration (2 claim(s))

- [observation/documented] Tasks follow a plan, review, execute, and deliver lifecycle, and every file an agent will touch is declared upfront so agents do not overwrite each other's work. -- evidence: [README.md#L37-L37](https://github.com/sagiyaacoby/TeamHero/blob/25466cdbfbcf44577d78a287077aaa3a92071036/README.md#L37-L37) (`clm_d4593cf1bb68cd89008d24ffa0939979c7976f354c712dd2d890ee6844488755`)
- [observation/documented] The changelog documents autopilot scheduling with recurring and one-time timed tasks, smart model routing for cost-efficient execution, and dependency auto-triggering so tasks start when their dependencies complete. -- evidence: [CHANGELOG.md#L42-L44](https://github.com/sagiyaacoby/TeamHero/blob/25466cdbfbcf44577d78a287077aaa3a92071036/CHANGELOG.md#L42-L44) (`clm_12f3ed7c8a55fb41f385c9789a098368223e1040f5d341b3b3c16d337c0be9a4`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] Prerequisites are Node.js 18+ and the Claude CLI, described as the AI backbone powering the agents; the Claude CLI is installed globally via npm. -- evidence: [README.md#L56-L58](https://github.com/sagiyaacoby/TeamHero/blob/25466cdbfbcf44577d78a287077aaa3a92071036/README.md#L56-L58), [README.md#L53-L54](https://github.com/sagiyaacoby/TeamHero/blob/25466cdbfbcf44577d78a287077aaa3a92071036/README.md#L53-L54) (`clm_47fa4abba9d1c0b515ef01cc90c62f319663f0fba29dffe859c952c2760bf3be`)
- [observation/documented] Vendor libraries including xterm, marked, and qrcode are bundled to support CDN-free offline operation. -- evidence: [CHANGELOG.md#L28-L28](https://github.com/sagiyaacoby/TeamHero/blob/25466cdbfbcf44577d78a287077aaa3a92071036/CHANGELOG.md#L28-L28), [CHANGELOG.md#L17-L21](https://github.com/sagiyaacoby/TeamHero/blob/25466cdbfbcf44577d78a287077aaa3a92071036/CHANGELOG.md#L17-L21) (`clm_ae6003dcbe7bdd4155217d67e860761b5bdf928f817ffa4190aa48f1f4cbf052`)

## limitations (1 claim(s))

- [observation/documented] The project is released under the MIT License, with TeamHero and Kapow noted as trademarks of Sagi Yaacoby. -- evidence: [README.md#L92-L92](https://github.com/sagiyaacoby/TeamHero/blob/25466cdbfbcf44577d78a287077aaa3a92071036/README.md#L92-L92), [README.md#L94-L94](https://github.com/sagiyaacoby/TeamHero/blob/25466cdbfbcf44577d78a287077aaa3a92071036/README.md#L94-L94) (`clm_8e8b297f66679588a73bc51e21c7144919f7b28e91cd81e7937c77d729284d89`)

## relevance (1 claim(s))

- [observation/documented] The project targets developers working with Claude Code who want structure around their agents, and it is a builder platform requiring comfort with CLI and Node.js. -- evidence: [README.md#L43-L43](https://github.com/sagiyaacoby/TeamHero/blob/25466cdbfbcf44577d78a287077aaa3a92071036/README.md#L43-L43), [README.md#L45-L45](https://github.com/sagiyaacoby/TeamHero/blob/25466cdbfbcf44577d78a287077aaa3a92071036/README.md#L45-L45) (`clm_22757dbdc65ec7c526af68ee4406f21c91fe0ee02db4950f0799913436079911`)

