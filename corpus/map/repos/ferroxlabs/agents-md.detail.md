# ferroxlabs/agents-md -- full detail

[Back to orientation](agents-md.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/ferroxlabs/agents-md/90c7198cfa97ff1868f0600952098fee7fc86ef9/b15adb8e01836996.json](../../../wiki/dossiers/ferroxlabs/agents-md/90c7198cfa97ff1868f0600952098fee7fc86ef9/b15adb8e01836996.json)

## specifications (1 claim(s))

- [observation/documented] The repository's product is a single drop-in AGENTS.md file of operating instructions intended to be placed at any project's root and read by coding agents, released under the MIT license. -- evidence: [README.md#L119-L119](https://github.com/FerroxLabs/agents-md/blob/90c7198cfa97ff1868f0600952098fee7fc86ef9/README.md#L119-L119), [README.md#L7-L7](https://github.com/FerroxLabs/agents-md/blob/90c7198cfa97ff1868f0600952098fee7fc86ef9/README.md#L7-L7), [README.md#L5-L5](https://github.com/FerroxLabs/agents-md/blob/90c7198cfa97ff1868f0600952098fee7fc86ef9/README.md#L5-L5) (`clm_f52edcde04ee5121417c3e2b8676f5ee687af8d4e7cc712a7cf27605aa14b57f`)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (2 claim(s))

- [observation/documented] The file is deliberately kept tight (about 200 lines per the README, with under 300 suggested as a ceiling) so rules stay loaded, and sections 0-9 are meant to be left untouched by users. -- evidence: [README.md#L83-L83](https://github.com/FerroxLabs/agents-md/blob/90c7198cfa97ff1868f0600952098fee7fc86ef9/README.md#L83-L83), [AGENTS.md#L145-L145](https://github.com/FerroxLabs/agents-md/blob/90c7198cfa97ff1868f0600952098fee7fc86ef9/AGENTS.md#L145-L145), [README.md#L64-L71](https://github.com/FerroxLabs/agents-md/blob/90c7198cfa97ff1868f0600952098fee7fc86ef9/README.md#L64-L71) (`clm_0bee21d4c1a943d8e5fbcc5658fdd0212ac01c21488daaef1438c899e02730bd`)
- [observation/documented] The template synthesizes Karpathy's four principles on LLM coding failure modes, Boris Cherny's Claude Code workflow with reactive pruning, Anthropic's Claude Code best practices, community anti-sycophancy patterns, and the AGENTS.md standard. -- evidence: [README.md#L109-L113](https://github.com/FerroxLabs/agents-md/blob/90c7198cfa97ff1868f0600952098fee7fc86ef9/README.md#L109-L113), [AGENTS.md#L198-L204](https://github.com/FerroxLabs/agents-md/blob/90c7198cfa97ff1868f0600952098fee7fc86ef9/AGENTS.md#L198-L204) (`clm_4243351e15a8bc1abd623b66bd802be5cd708309686b2b476efb2b4504546421`)

## workflows (8 claim(s))

- [observation/documented] Installation is documented two ways: an agent-driven prompt that fetches the raw file, symlinks CLAUDE.md/GEMINI.md, and fills section 10 from the codebase, or a manual curl download of AGENTS.md. -- evidence: [README.md#L21-L27](https://github.com/FerroxLabs/agents-md/blob/90c7198cfa97ff1868f0600952098fee7fc86ef9/README.md#L21-L27), [README.md#L33-L35](https://github.com/FerroxLabs/agents-md/blob/90c7198cfa97ff1868f0600952098fee7fc86ef9/README.md#L33-L35) (`clm_b03094605754634cbd5a9c8f3d31c24f479d59399aa00d693440ca7806571e80`)
- [observation/documented] Repository development practice: the file's non-negotiables instruct agents to skip flattery, disagree with false premises, never fabricate facts, ask when a task has two plausible interpretations, and touch only lines traceable to the request. -- evidence: [AGENTS.md#L20-L24](https://github.com/FerroxLabs/agents-md/blob/90c7198cfa97ff1868f0600952098fee7fc86ef9/AGENTS.md#L20-L24) (`clm_dcdab43fcde10abb8bf3cd76130e0661d64ff11dca3dadd60949e56a23bd5485`)
- [observation/documented] Repository development practice: agents are told to define verifiable success criteria, write and run verification (tests, scripts, benchmarks) before claiming success, and fix causes rather than tests when verification fails. -- evidence: [AGENTS.md#L82-L85](https://github.com/FerroxLabs/agents-md/blob/90c7198cfa97ff1868f0600952098fee7fc86ef9/AGENTS.md#L82-L85) (`clm_16b7239792ace71aa86a18151a929db30e7d4d535451977ce169a695f8e9ed24`)
- [observation/documented] Repository development practice: the file directs agents to run existing test suites, linters, and type checkers rather than guessing, and to prefer CLI tools like gh, aws, gcloud, and kubectl when available. -- evidence: [AGENTS.md#L91-L96](https://github.com/FerroxLabs/agents-md/blob/90c7198cfa97ff1868f0600952098fee7fc86ef9/AGENTS.md#L91-L96) (`clm_efa85ec34864250470d8d2f8e636b36df18f26f59a9004c4181caa744991f45d`)
- [observation/documented] Repository development practice: section 10 (Project context) is a per-project template with TODO placeholders for stack, build/test/lint commands, layout, and forbidden areas, to be filled only with what can be verified from the codebase. -- evidence: [AGENTS.md#L171-L173](https://github.com/FerroxLabs/agents-md/blob/90c7198cfa97ff1868f0600952098fee7fc86ef9/AGENTS.md#L171-L173), [AGENTS.md#L151-L151](https://github.com/FerroxLabs/agents-md/blob/90c7198cfa97ff1868f0600952098fee7fc86ef9/AGENTS.md#L151-L151), [AGENTS.md#L160-L166](https://github.com/FerroxLabs/agents-md/blob/90c7198cfa97ff1868f0600952098fee7fc86ef9/AGENTS.md#L160-L166) (`clm_2312944799fde20b13aa5b6a7c2a71b47f08b3d266fb2c738423f29da5581db6`)
- [observation/documented] Repository development practice: section 11 (Project Learnings) starts empty and the agent is instructed to append one concrete rule each time the user corrects its approach, tightening or removing lines as issues disappear. -- evidence: [AGENTS.md#L190-L190](https://github.com/FerroxLabs/agents-md/blob/90c7198cfa97ff1868f0600952098fee7fc86ef9/AGENTS.md#L190-L190), [AGENTS.md#L188-L188](https://github.com/FerroxLabs/agents-md/blob/90c7198cfa97ff1868f0600952098fee7fc86ef9/AGENTS.md#L188-L188) (`clm_ebb4dc71f53b8b459f5faeaa027884ba31bddbc8ac15120f32e0320ff6946f32`)
- [observation/documented] For large codebases the README suggests sharding via Claude Code @-imports or .claude/rules with path frontmatter, or Cursor .cursor/rules with path scoping, while keeping a single AGENTS.md for other tools. -- evidence: [README.md#L91-L93](https://github.com/FerroxLabs/agents-md/blob/90c7198cfa97ff1868f0600952098fee7fc86ef9/README.md#L91-L93) (`clm_9a0eae13936832cddff66283d9eb1e742adbfb8671bed378fe71c1b61969250c`)
- [observation/documented] Repository development practice: the file includes a self-improvement loop instructing agents to diagnose mistakes as missing versus ignored rules, add or tighten rules accordingly, and prune lines every few weeks. -- evidence: [AGENTS.md#L140-L143](https://github.com/FerroxLabs/agents-md/blob/90c7198cfa97ff1868f0600952098fee7fc86ef9/AGENTS.md#L140-L143) (`clm_743324725155d54211d041a10efa7cf7cc762b3c8be84eb83ccb89002e0cd93d`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] The file targets the AGENTS.md open standard: tools like Codex, Cursor, Aider, Windsurf, Copilot, and Devin read it natively, while Claude Code and Gemini CLI require CLAUDE.md and GEMINI.md symlinks (or copies) pointing to it. -- evidence: [README.md#L39-L39](https://github.com/FerroxLabs/agents-md/blob/90c7198cfa97ff1868f0600952098fee7fc86ef9/README.md#L39-L39), [README.md#L37-L37](https://github.com/FerroxLabs/agents-md/blob/90c7198cfa97ff1868f0600952098fee7fc86ef9/README.md#L37-L37), [README.md#L101-L101](https://github.com/FerroxLabs/agents-md/blob/90c7198cfa97ff1868f0600952098fee7fc86ef9/README.md#L101-L101) (`clm_32434882651e7d69c01f8d46d31da00678ebb686836f8314bd5d788eff5fc964`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

