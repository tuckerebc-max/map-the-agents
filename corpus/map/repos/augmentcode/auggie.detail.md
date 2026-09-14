# augmentcode/auggie -- full detail

[Back to orientation](auggie.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/augmentcode/auggie/9cc3ead419db9486ad44e6e4bba30ecd6784ccff/ba3e31b0ac8fb359.json](../../../wiki/dossiers/augmentcode/auggie/9cc3ead419db9486ad44e6e4bba30ecd6784ccff/ba3e31b0ac8fb359.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] A daemon component validates the host's Git version at startup, can be configured with a custom worktree directory, and can auto-discover git workspaces under a non-git container. -- evidence: [CHANGELOG.md#L107-L114](https://github.com/augmentcode/auggie/blob/9cc3ead419db9486ad44e6e4bba30ecd6784ccff/CHANGELOG.md#L107-L114), [CHANGELOG.md#L91-L91](https://github.com/augmentcode/auggie/blob/9cc3ead419db9486ad44e6e4bba30ecd6784ccff/CHANGELOG.md#L91-L91), [CHANGELOG.md#L6-L14](https://github.com/augmentcode/auggie/blob/9cc3ead419db9486ad44e6e4bba30ecd6784ccff/CHANGELOG.md#L6-L14) (`clm_d71617e3f795f34ccb86dd6208675be90f559a79dc77ad5160b3a265a8bb893c`)

## design-choices (1 claim(s))

- [observation/documented] Plan mode saves plans to ~/.augment/plans/ and enforces strict read-only access; tool permissions default to denylist mode to prevent accidental lockout from all tools. -- evidence: [CHANGELOG.md#L369-L378](https://github.com/augmentcode/auggie/blob/9cc3ead419db9486ad44e6e4bba30ecd6784ccff/CHANGELOG.md#L369-L378), [CHANGELOG.md#L342-L351](https://github.com/augmentcode/auggie/blob/9cc3ead419db9486ad44e6e4bba30ecd6784ccff/CHANGELOG.md#L342-L351) (`clm_58d20415375e64cb610aa1b53b4e56e4c228313ae5bec0d479504f87b0ce759e`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (1 claim(s))

- [observation/documented] The CLI loads specialized domain knowledge from SKILL.md files following the agentskills.io specification, and a /skills command shows loaded skills with approximate token usage. -- evidence: [CHANGELOG.md#L482-L484](https://github.com/augmentcode/auggie/blob/9cc3ead419db9486ad44e6e4bba30ecd6784ccff/CHANGELOG.md#L482-L484) (`clm_94ca75d86417463177ef4a34c85bc07c8d0c0b3a0ea56249c1944e73ac6fbd68`)

## interfaces (4 claim(s))

- [observation/documented] The CLI supports a login command, running with an optional initial prompt, a --print mode that runs once and writes to stdout (suited to CI), and --quiet to return only final output. -- evidence: [README.md#L22-L24](https://github.com/augmentcode/auggie/blob/9cc3ead419db9486ad44e6e4bba30ecd6784ccff/README.md#L22-L24), [README.md#L28-L31](https://github.com/augmentcode/auggie/blob/9cc3ead419db9486ad44e6e4bba30ecd6784ccff/README.md#L28-L31), [README.md#L33-L34](https://github.com/augmentcode/auggie/blob/9cc3ead419db9486ad44e6e4bba30ecd6784ccff/README.md#L33-L34) (`clm_56a8f23a947aba7418594f7fc74e95c7c415ea60f30e203d72a36e159dc97cca`)
- [observation/documented] Reusable prompts stored as markdown files with frontmatter under .augment/commands/ become slash commands such as /code-review. -- evidence: [README.md#L38-L38](https://github.com/augmentcode/auggie/blob/9cc3ead419db9486ad44e6e4bba30ecd6784ccff/README.md#L38-L38), [README.md#L42-L51](https://github.com/augmentcode/auggie/blob/9cc3ead419db9486ad44e6e4bba30ecd6784ccff/README.md#L42-L51) (`clm_2ed87cb117ae99144b71053e3d29e88836c947f4a30d6b653d8d3042ba2ed023`)
- [observation/documented] The CLI offers an MCP mode with --mcp-auto-workspace for on-the-fly workspace indexing, and an --acp flag for Agent Communication Protocol support. -- evidence: [CHANGELOG.md#L608-L612](https://github.com/augmentcode/auggie/blob/9cc3ead419db9486ad44e6e4bba30ecd6784ccff/CHANGELOG.md#L608-L612), [CHANGELOG.md#L508-L508](https://github.com/augmentcode/auggie/blob/9cc3ead419db9486ad44e6e4bba30ecd6784ccff/CHANGELOG.md#L508-L508) (`clm_cc0c65842f21631d8f769f8ca75851e105ce80d00e54ab0f31089ad845f60876`)
- [observation/documented] Cloud subcommands include auggie cloud project, tunnel open/close/list, analytics, trigger enable/disable, and vfs get-url for compact durable VFS file links. -- evidence: [CHANGELOG.md#L101-L104](https://github.com/augmentcode/auggie/blob/9cc3ead419db9486ad44e6e4bba30ecd6784ccff/CHANGELOG.md#L101-L104), [CHANGELOG.md#L51-L52](https://github.com/augmentcode/auggie/blob/9cc3ead419db9486ad44e6e4bba30ecd6784ccff/CHANGELOG.md#L51-L52), [CHANGELOG.md#L86-L88](https://github.com/augmentcode/auggie/blob/9cc3ead419db9486ad44e6e4bba30ecd6784ccff/CHANGELOG.md#L86-L88) (`clm_c891153b0c25cb92a2f474de5614be017e0705a0ac305c7b3205ebf296df91f8`)

## memory-state (1 claim(s))

- [observation/documented] Agent progress is saved incrementally after each LLM exchange to prevent loss on crashes, and queued messages persist in the session file across CLI restarts. -- evidence: [CHANGELOG.md#L395-L404](https://github.com/augmentcode/auggie/blob/9cc3ead419db9486ad44e6e4bba30ecd6784ccff/CHANGELOG.md#L395-L404) (`clm_02e32fea2e996a32228eb0bf65db22e99f799edd501d165da965f8fabce5198b`)

## orchestration (1 claim(s))

- [observation/documented] The agent supports built-in sub-agents including explore, auggie-guide, and a general-purpose sub-agent, and the agent loop executes independent tools in parallel. -- evidence: [CHANGELOG.md#L148-L148](https://github.com/augmentcode/auggie/blob/9cc3ead419db9486ad44e6e4bba30ecd6784ccff/CHANGELOG.md#L148-L148), [CHANGELOG.md#L22-L26](https://github.com/augmentcode/auggie/blob/9cc3ead419db9486ad44e6e4bba30ecd6784ccff/CHANGELOG.md#L22-L26), [CHANGELOG.md#L127-L129](https://github.com/augmentcode/auggie/blob/9cc3ead419db9486ad44e6e4bba30ecd6784ccff/CHANGELOG.md#L127-L129), [CHANGELOG.md#L342-L351](https://github.com/augmentcode/auggie/blob/9cc3ead419db9486ad44e6e4bba30ecd6784ccff/CHANGELOG.md#L342-L351) (`clm_bb6aa4baa53ac2950e632601244021ec28b30ae1d2cb06680ff81f5887ab8632`)

## tools-permissions (1 claim(s))

- [observation/documented] Saving files to sensitive paths requires approval, and denying a tool permission request provides clearer feedback, indicating a runtime permission model over tool use. -- evidence: [CHANGELOG.md#L297-L301](https://github.com/augmentcode/auggie/blob/9cc3ead419db9486ad44e6e4bba30ecd6784ccff/CHANGELOG.md#L297-L301), [CHANGELOG.md#L36-L38](https://github.com/augmentcode/auggie/blob/9cc3ead419db9486ad44e6e4bba30ecd6784ccff/CHANGELOG.md#L36-L38) (`clm_2f372183f531ae80ac14210c4882198c2e0686f17edf150642195ab6378eb226`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The package is published as @augmentcode/auggie on npm and requires Node.js 22 or later. -- evidence: [README.md#L3-L3](https://github.com/augmentcode/auggie/blob/9cc3ead419db9486ad44e6e4bba30ecd6784ccff/README.md#L3-L3), [README.md#L16-L18](https://github.com/augmentcode/auggie/blob/9cc3ead419db9486ad44e6e4bba30ecd6784ccff/README.md#L16-L18), [README.md#L14-L14](https://github.com/augmentcode/auggie/blob/9cc3ead419db9486ad44e6e4bba30ecd6784ccff/README.md#L14-L14) (`clm_59a1db976d28485a16da54a9172dc5f2610d0bf8fb4a5d5a14c5fea51e132728`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (1 claim(s))

- [observation/documented] Auggie is described as Augment's agentic coding CLI that runs in a terminal, analyzing code, making safe edits, and automating routine tasks via natural language. -- evidence: [README.md#L5-L5](https://github.com/augmentcode/auggie/blob/9cc3ead419db9486ad44e6e4bba30ecd6784ccff/README.md#L5-L5) (`clm_3c2c4447623f72b7be2d09f70bec4eac5a37ea50553995e54235d14286076702`)

