# griddynamics/rosetta -- full detail

[Back to orientation](rosetta.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/griddynamics/rosetta/785054e925aa90a56b1221879584e341eac58f72/785672389caeb1f9.json](../../../wiki/dossiers/griddynamics/rosetta/785054e925aa90a56b1221879584e341eac58f72/785672389caeb1f9.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] Rosettify is a local CLI/MCP utility providing deterministic workflow execution with zero network calls; it includes plan management, specs management, an atomic write cycle with a backup chain, and sequential phase enforcement. -- evidence: [docs/ARCHITECTURE.md#L151-L158](https://github.com/griddynamics/rosetta/blob/785054e925aa90a56b1221879584e341eac58f72/docs/ARCHITECTURE.md#L151-L158), [docs/ARCHITECTURE.md#L143-L143](https://github.com/griddynamics/rosetta/blob/785054e925aa90a56b1221879584e341eac58f72/docs/ARCHITECTURE.md#L143-L143) (`clm_b8e736c78a091225ca6f5ec0caf31190ab3acb491641e0786abfcc237d32f060`)

## design-choices (2 claim(s))

- [observation/documented] Rosetta layers instructions at runtime — core, then organization, then project — with higher layers propagating to every project automatically, all authored in markdown and versioned in Git. -- evidence: [README.md#L102-L102](https://github.com/griddynamics/rosetta/blob/785054e925aa90a56b1221879584e341eac58f72/README.md#L102-L102), [README.md#L123-L123](https://github.com/griddynamics/rosetta/blob/785054e925aa90a56b1221879584e341eac58f72/README.md#L123-L123) (`clm_8eade8d12226e253020c6117624af82638cf535978585b125b1f0afac9857104`)
- [observation/documented] The architecture follows inversion of control: Rosetta does not see or process source code; it exposes guardrails and a menu of instructions, and the coding agent selects only what it needs. -- evidence: [docs/ARCHITECTURE.md#L72-L72](https://github.com/griddynamics/rosetta/blob/785054e925aa90a56b1221879584e341eac58f72/docs/ARCHITECTURE.md#L72-L72) (`clm_f7623ff1a657804b23de4140cfd0613403ef9063d2b6551373647c6fbb6130a1`)

## workflows (2 claim(s))

- [observation/documented] Rosetta ships named workflows including coding-flow, requirements-authoring-flow, security-flow, testgen/api-aqa/ui-aqa flows, and code-analysis-flow, each with defined phases, subagents, and HITL gates. -- evidence: [README.md#L49-L55](https://github.com/griddynamics/rosetta/blob/785054e925aa90a56b1221879584e341eac58f72/README.md#L49-L55), [README.md#L191-L191](https://github.com/griddynamics/rosetta/blob/785054e925aa90a56b1221879584e341eac58f72/README.md#L191-L191) (`clm_c374efadca4a55f60dd11be885721d7ab3de18810307d689ba084426a5ea9374`)
- [observation/documented] Repository development practice: contributors are directed to CONTRIBUTING.md for workflow and expectations, and the README notes Rosetta plugins are used to develop Rosetta itself. -- evidence: [README.md#L211-L211](https://github.com/griddynamics/rosetta/blob/785054e925aa90a56b1221879584e341eac58f72/README.md#L211-L211), [README.md#L213-L213](https://github.com/griddynamics/rosetta/blob/785054e925aa90a56b1221879584e341eac58f72/README.md#L213-L213) (`clm_6df9278939c44de68587a51f6d4f3e1e51da591d07473526e15f3d36075116b8`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] Rosetta defines typed command aliases (e.g. USE SKILL, APPLY PHASE, INVOKE SUBAGENT) that work across IDEs instead of calling MCP tools directly, for portability, decoupling, and authoring. -- evidence: [docs/ARCHITECTURE.md#L80-L80](https://github.com/griddynamics/rosetta/blob/785054e925aa90a56b1221879584e341eac58f72/docs/ARCHITECTURE.md#L80-L80), [docs/ARCHITECTURE.md#L82-L84](https://github.com/griddynamics/rosetta/blob/785054e925aa90a56b1221879584e341eac58f72/docs/ARCHITECTURE.md#L82-L84), [docs/ARCHITECTURE.md#L86-L100](https://github.com/griddynamics/rosetta/blob/785054e925aa90a56b1221879584e341eac58f72/docs/ARCHITECTURE.md#L86-L100) (`clm_cd44f61b7d1232ecee8acc0671a1f022c219fbc0d9fb2936a49ef67494275bca`)
- [observation/documented] The rosettify tool is published on npm and invoked via npx, or run as a local MCP server over stdio with a --mcp flag; it offers plan and specs subcommands operating on local JSON files. -- evidence: [docs/ARCHITECTURE.md#L151-L158](https://github.com/griddynamics/rosetta/blob/785054e925aa90a56b1221879584e341eac58f72/docs/ARCHITECTURE.md#L151-L158), [docs/ARCHITECTURE.md#L145-L145](https://github.com/griddynamics/rosetta/blob/785054e925aa90a56b1221879584e341eac58f72/docs/ARCHITECTURE.md#L145-L145) (`clm_e248fed1616b582fa63f6bcefac6f56e9cedade7d0bb0afbe22af57814afac4f`)

## memory-state (1 claim(s))

- [observation/documented] Rosetta instructs agents to maintain agents/MEMORY.md with root causes, actions tried, and lessons learned, and to write execution state (plans, specs, phase progress) to disk so failed sessions resume from checkpoints. -- evidence: [README.md#L199-L199](https://github.com/griddynamics/rosetta/blob/785054e925aa90a56b1221879584e341eac58f72/README.md#L199-L199), [README.md#L195-L195](https://github.com/griddynamics/rosetta/blob/785054e925aa90a56b1221879584e341eac58f72/README.md#L195-L195) (`clm_4eb01200602bd0e1f31189d1da89bd20e620773886f1a0a20ca864cefea21175`)

## orchestration (1 claim(s))

- [observation/documented] Rosetta workflows instruct the agent to delegate review to a separate subagent with a fresh context window that inspects the implementation against original specs, and to use a validator subagent with real execution evidence. -- evidence: [README.md#L187-L187](https://github.com/griddynamics/rosetta/blob/785054e925aa90a56b1221879584e341eac58f72/README.md#L187-L187), [README.md#L183-L183](https://github.com/griddynamics/rosetta/blob/785054e925aa90a56b1221879584e341eac58f72/README.md#L183-L183) (`clm_eef3808ac163ac4403de73bf68064633c76426344aeb8884abd6190b40ae485e`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (2 claim(s))

- [observation/documented] The curiocity harness drives coding-agent CLIs (Claude Code, Codex) through a real PTY, reads native on-disk transcripts, auto-answers agent questions via LLM, and scores runs with deterministic checks plus an LLM judge, gating CI on the aggregate. -- evidence: [docs/ARCHITECTURE.md#L172-L172](https://github.com/griddynamics/rosetta/blob/785054e925aa90a56b1221879584e341eac58f72/docs/ARCHITECTURE.md#L172-L172) (`clm_c6fe0744f03e81c52accf3c047284a1720707030b557ba38f6d1e5a3bb11ea92`)
- [observation/documented] rosettify-prompts is a dev-only prompt A/B/N benchmark against the Anthropic API, comparing tokens, cost, latency, and stability across concurrent conversation variants; it is not shipped to end users. -- evidence: [docs/ARCHITECTURE.md#L166-L166](https://github.com/griddynamics/rosetta/blob/785054e925aa90a56b1221879584e341eac58f72/docs/ARCHITECTURE.md#L166-L166) (`clm_801d1a7de3c9093fa3d5dc2857605f65e439d2856b962b96f5f81e603f76439d`)

## dependencies (1 claim(s))

- [observation/documented] The MCP server is built on FastMCP v3 with Streamable HTTP + OAuth 2.1 and STDIO transports, and the MCP pipeline involves Redis schema migrations and RAGFlow datasets. -- evidence: [docs/ARCHITECTURE.md#L66-L66](https://github.com/griddynamics/rosetta/blob/785054e925aa90a56b1221879584e341eac58f72/docs/ARCHITECTURE.md#L66-L66) (`clm_83cd58f2a34483b2f8c557ce05f0c1d819ec98f33ba11c394c355e8823c67526`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

