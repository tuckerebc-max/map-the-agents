# 2389-research/claude-plugins -- full detail

[Back to orientation](claude-plugins.md)

## Origins

- alltheagents.org-site-pages

## Projects

- Observatory

Full evidence record (JSON): [wiki/dossiers/2389-research/claude-plugins/017d34612ebffc73eb74415aa0984d57072f5a62/bb0f6c55bd4c81bf.json](../../../wiki/dossiers/2389-research/claude-plugins/017d34612ebffc73eb74415aa0984d57072f5a62/bb0f6c55bd4c81bf.json)

## specifications (1 claim(s))

- [observation/documented] The repository is a marketplace of 28 plugins and MCP servers for Claude Code covering parallel exploration, iterative refinement, binary reverse engineering, and structured decision-making. -- evidence: [README.md#L6-L6](https://github.com/2389-research/claude-plugins/blob/017d34612ebffc73eb74415aa0984d57072f5a62/README.md#L6-L6) (`clm_6958916bfa90d723cf5f585a5c3c6b0fe08bcc8f6e2211dfec689a95f558e77c`)

## components (2 claim(s))

- [observation/documented] The catalog includes plugins such as simmer (iterative refinement with investigation-first judges), test-kitchen (parallel implementation exploration), thrifty (tiered Sonnet/Haiku delegation), and binary-re (ELF reverse engineering). -- evidence: [README.md#L42-L51](https://github.com/2389-research/claude-plugins/blob/017d34612ebffc73eb74415aa0984d57072f5a62/README.md#L42-L51), [README.md#L55-L64](https://github.com/2389-research/claude-plugins/blob/017d34612ebffc73eb74415aa0984d57072f5a62/README.md#L55-L64), [docs/index.md#L35-L42](https://github.com/2389-research/claude-plugins/blob/017d34612ebffc73eb74415aa0984d57072f5a62/docs/index.md#L35-L42) (`clm_e774cb2c29cd89db77b6cabfb3c6b2e48ad61363f1387f8db0c26747d047eb6f`)
- [observation/documented] The marketplace lists four MCP servers: agent-drugs, socialmedia, journal, and slack-mcp, providing behavior modification, social media, journaling, and Slack integration. -- evidence: [README.md#L84-L89](https://github.com/2389-research/claude-plugins/blob/017d34612ebffc73eb74415aa0984d57072f5a62/README.md#L84-L89) (`clm_dd771ce5f8d5eb61eb1233ea25f693cd3a7a5d71b273abd19b54b2649f5d15c1`)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (4 claim(s))

- [observation/documented] Repository development practice: adding a plugin requires creating a repo under 2389-research/, adding a marketplace.json entry, running 'npm run generate', then committing and pushing. -- evidence: [README.md#L93-L96](https://github.com/2389-research/claude-plugins/blob/017d34612ebffc73eb74415aa0984d57072f5a62/README.md#L93-L96) (`clm_9781279ae74a51310e0d834cc581a3d0c107d9dcc5512a4b1796c01c81674eac`)
- [observation/documented] Repository development practice: after modifying a skill, contributors copy it into ~/.claude/skills/, test manually against tests/integration scenarios, and verify auto-detection, TodoWrite checklists, and step ordering. -- evidence: [docs/DEVELOPMENT.md#L78-L81](https://github.com/2389-research/claude-plugins/blob/017d34612ebffc73eb74415aa0984d57072f5a62/docs/DEVELOPMENT.md#L78-L81), [docs/DEVELOPMENT.md#L87-L87](https://github.com/2389-research/claude-plugins/blob/017d34612ebffc73eb74415aa0984d57072f5a62/docs/DEVELOPMENT.md#L87-L87), [docs/DEVELOPMENT.md#L89-L93](https://github.com/2389-research/claude-plugins/blob/017d34612ebffc73eb74415aa0984d57072f5a62/docs/DEVELOPMENT.md#L89-L93) (`clm_cbad277d11aa5beb31b33f70cedd99d942b51f055853150bf9894e34b7e5c41c`)
- [observation/documented] Repository development practice: a manual testing checklist covers auto-detection, sub-skill routing, TodoWrite checklists, correct tool use (Read, Edit, Write, Grep), and output format. -- evidence: [docs/DEVELOPMENT.md#L304-L312](https://github.com/2389-research/claude-plugins/blob/017d34612ebffc73eb74415aa0984d57072f5a62/docs/DEVELOPMENT.md#L304-L312) (`clm_1276ffb54e4b6331b803d996ab074d2565f301e8cbf03d0f3c2592d4fc0abd83`)
- [observation/documented] Repository development practice: skill authoring guidance requires granular TodoWrite items (2-5 minutes each), complete runnable code examples, and exact file paths rather than vague references. -- evidence: [docs/DEVELOPMENT.md#L271-L271](https://github.com/2389-research/claude-plugins/blob/017d34612ebffc73eb74415aa0984d57072f5a62/docs/DEVELOPMENT.md#L271-L271), [docs/DEVELOPMENT.md#L263-L267](https://github.com/2389-research/claude-plugins/blob/017d34612ebffc73eb74415aa0984d57072f5a62/docs/DEVELOPMENT.md#L263-L267), [docs/DEVELOPMENT.md#L285-L285](https://github.com/2389-research/claude-plugins/blob/017d34612ebffc73eb74415aa0984d57072f5a62/docs/DEVELOPMENT.md#L285-L285), [docs/DEVELOPMENT.md#L337-L341](https://github.com/2389-research/claude-plugins/blob/017d34612ebffc73eb74415aa0984d57072f5a62/docs/DEVELOPMENT.md#L337-L341) (`clm_9afb7575a6f2604fac857d102c0d280dd985a9605f32b3feaca1c1ecae041022`)

## skills-patterns (4 claim(s))

- [observation/documented] Skills are defined in SKILL.md markdown files with YAML frontmatter containing a name and a description used for auto-detection. -- evidence: [docs/DEVELOPMENT.md#L56-L60](https://github.com/2389-research/claude-plugins/blob/017d34612ebffc73eb74415aa0984d57072f5a62/docs/DEVELOPMENT.md#L56-L60), [docs/DEVELOPMENT.md#L52-L52](https://github.com/2389-research/claude-plugins/blob/017d34612ebffc73eb74415aa0984d57072f5a62/docs/DEVELOPMENT.md#L52-L52) (`clm_5ffeacd238e9e66ec3ac2078cc8f66e39d8f483f8ea73120274975deb9275860`)
- [observation/documented] The css-development and firebase-development plugins use a main orchestrator SKILL.md plus sub-skill directories (e.g., create-component, validate, refactor; project-setup, add-feature, debug). -- evidence: [docs/DEVELOPMENT.md#L7-L46](https://github.com/2389-research/claude-plugins/blob/017d34612ebffc73eb74415aa0984d57072f5a62/docs/DEVELOPMENT.md#L7-L46) (`clm_c2083a220943671988732b903870f908fc87a3a9ca3faeb6e857176ad30bbb22`)
- [observation/documented] All Firebase patterns are centralized in the main firebase-development SKILL.md (1323 lines), and sub-skills reference them via '@firebase-development/pattern-name' syntax. -- evidence: [docs/DEVELOPMENT.md#L159-L159](https://github.com/2389-research/claude-plugins/blob/017d34612ebffc73eb74415aa0984d57072f5a62/docs/DEVELOPMENT.md#L159-L159) (`clm_d4e0b0b632a3adb7cc9c1085183f87f44e2bea3ea8f7506840d0b3eb4d5b9d09`)
- [observation/documented] Key CSS patterns include semantic class naming, Tailwind composition with @apply, dark mode by default, and static plus component-rendering test coverage. -- evidence: [docs/DEVELOPMENT.md#L144-L148](https://github.com/2389-research/claude-plugins/blob/017d34612ebffc73eb74415aa0984d57072f5a62/docs/DEVELOPMENT.md#L144-L148) (`clm_f93c4b67dac4fbe0eb8cd8f9c8d4bf5c1d0d7c42b988e07a7fdad30c40b83110`)

## interfaces (2 claim(s))

- [observation/documented] Plugins can be installed in any agent (Claude Code, Cursor, Codex) via vercel-labs/skills using 'npx skills add 2389-research/<plugin>'. -- evidence: [README.md#L14-L14](https://github.com/2389-research/claude-plugins/blob/017d34612ebffc73eb74415aa0984d57072f5a62/README.md#L14-L14), [README.md#L16-L18](https://github.com/2389-research/claude-plugins/blob/017d34612ebffc73eb74415aa0984d57072f5a62/README.md#L16-L18), [docs/index.md#L9-L11](https://github.com/2389-research/claude-plugins/blob/017d34612ebffc73eb74415aa0984d57072f5a62/docs/index.md#L9-L11) (`clm_30d3b35379f60d8f0917647627dcfc8073b0a1728cb175477537cf0a191f75df`)
- [observation/documented] Native Claude Code installation uses '/plugin marketplace add 2389-research/claude-plugins' followed by '/plugin install <plugin>@2389-research'. -- evidence: [README.md#L24-L26](https://github.com/2389-research/claude-plugins/blob/017d34612ebffc73eb74415aa0984d57072f5a62/README.md#L24-L26), [docs/llms.txt#L15-L18](https://github.com/2389-research/claude-plugins/blob/017d34612ebffc73eb74415aa0984d57072f5a62/docs/llms.txt#L15-L18) (`clm_a3bc70f454faed6412c3f84621b845dc5f4b8289c4991103006c79d7b7ee1867`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (1 claim(s))

- [inference/documented] The thrifty plugin is documented as benchmarked at roughly 64% lower cost than Opus at equal quality, suggesting some agent-performance evaluation exists, though no eval harness appears in the evidence. -- evidence: [docs/index.md#L48-L52](https://github.com/2389-research/claude-plugins/blob/017d34612ebffc73eb74415aa0984d57072f5a62/docs/index.md#L48-L52), [README.md#L42-L51](https://github.com/2389-research/claude-plugins/blob/017d34612ebffc73eb74415aa0984d57072f5a62/README.md#L42-L51) (`clm_060003b334feee4cddf876978ffc53b64a5dacca9898cd2aef0df35b2cddc67b`)

## dependencies (2 claim(s))

- [observation/documented] The binary-re plugin relies on radare2, Ghidra, GDB, and QEMU for hypothesis-driven ELF analysis across ARM64, ARMv7, and x86_64. -- evidence: [docs/index.md#L23-L29](https://github.com/2389-research/claude-plugins/blob/017d34612ebffc73eb74415aa0984d57072f5a62/docs/index.md#L23-L29), [docs/llms.txt#L24-L30](https://github.com/2389-research/claude-plugins/blob/017d34612ebffc73eb74415aa0984d57072f5a62/docs/llms.txt#L24-L30) (`clm_0eb584d15c32d9fff22c924f023a6f20b4292f4de364a71bdf55a90e8740cde6`)
- [observation/documented] The speed-run plugin uses a hosted LLM (Cerebras) for token-efficient parallel code generation, claiming about 60% token savings, and includes an MCP server. -- evidence: [docs/index.md#L23-L29](https://github.com/2389-research/claude-plugins/blob/017d34612ebffc73eb74415aa0984d57072f5a62/docs/index.md#L23-L29), [docs/llms.txt#L24-L30](https://github.com/2389-research/claude-plugins/blob/017d34612ebffc73eb74415aa0984d57072f5a62/docs/llms.txt#L24-L30) (`clm_b3edc6e7356fbf196323c375ff47fe6508351c9179b362c1d562d50b700d7cba`)

## limitations (1 claim(s))

- [observation/documented] The four MCP servers (journal, socialmedia, slack-mcp, agent-drugs) install via Claude Code only and ship no skills for npx. -- evidence: [README.md#L28-L28](https://github.com/2389-research/claude-plugins/blob/017d34612ebffc73eb74415aa0984d57072f5a62/README.md#L28-L28) (`clm_fd0894890cdff7c2bd4f24dffd90a58ddfb4d6e45efd76fd2db1a788a48bd8fb`)

## relevance (1 claim(s))

- [observation/documented] The marketplace is MIT-licensed, published by 2389 Research, browsable at 2389-research.github.io/claude-plugins, with contact email hello@2389.ai. -- evidence: [README.md#L106-L106](https://github.com/2389-research/claude-plugins/blob/017d34612ebffc73eb74415aa0984d57072f5a62/README.md#L106-L106), [README.md#L10-L10](https://github.com/2389-research/claude-plugins/blob/017d34612ebffc73eb74415aa0984d57072f5a62/README.md#L10-L10), [README.md#L110-L110](https://github.com/2389-research/claude-plugins/blob/017d34612ebffc73eb74415aa0984d57072f5a62/README.md#L110-L110) (`clm_b96ffcab46e1fec9c2749f3b96f41c7e2b26b4af0d2a2bf93cf6ee67d3a678fe`)

