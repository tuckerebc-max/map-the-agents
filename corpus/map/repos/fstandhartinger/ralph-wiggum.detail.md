# fstandhartinger/ralph-wiggum -- full detail

[Back to orientation](ralph-wiggum.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/fstandhartinger/ralph-wiggum/3f15f0fb83b8c2e0ac8d11abdae0e83ab8204981/e715ed74bb1d3916.json](../../../wiki/dossiers/fstandhartinger/ralph-wiggum/3f15f0fb83b8c2e0ac8d11abdae0e83ab8204981/e715ed74bb1d3916.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (3 claim(s))

- [observation/documented] Completion is gated on a magic phrase: the agent outputs <promise>DONE</promise> only when acceptance criteria are verified, tests pass, and changes are committed and pushed; the loop retries otherwise. -- evidence: [README.md#L83-L83](https://github.com/fstandhartinger/ralph-wiggum/blob/3f15f0fb83b8c2e0ac8d11abdae0e83ab8204981/README.md#L83-L83), [README.md#L282-L282](https://github.com/fstandhartinger/ralph-wiggum/blob/3f15f0fb83b8c2e0ac8d11abdae0e83ab8204981/README.md#L282-L282), [README.md#L78-L81](https://github.com/fstandhartinger/ralph-wiggum/blob/3f15f0fb83b8c2e0ac8d11abdae0e83ab8204981/README.md#L78-L81) (`clm_ba1df09cb4c97ce73f242c6f0d3831f8fd2238a929e80e0972de2c9b79a238f1`)
- [observation/documented] Specs are expected to carry specific, testable acceptance criteria, and tests, lints, and builds act as backpressure that the agent must satisfy before signaling completion. -- evidence: [README.md#L279-L279](https://github.com/fstandhartinger/ralph-wiggum/blob/3f15f0fb83b8c2e0ac8d11abdae0e83ab8204981/README.md#L279-L279), [README.md#L148-L148](https://github.com/fstandhartinger/ralph-wiggum/blob/3f15f0fb83b8c2e0ac8d11abdae0e83ab8204981/README.md#L148-L148), [README.md#L143-L146](https://github.com/fstandhartinger/ralph-wiggum/blob/3f15f0fb83b8c2e0ac8d11abdae0e83ab8204981/README.md#L143-L146) (`clm_d6ca370b2b0720d4b47dda5815e42bf09a64bc6c8ef1b11e068f53d53099e626`)
- [observation/documented] Each spec tracks an attempt count as an NR_OF_TRIES comment; after 10 attempts without completion a spec is flagged as stuck and should be split into smaller specs. -- evidence: [README.md#L185-L185](https://github.com/fstandhartinger/ralph-wiggum/blob/3f15f0fb83b8c2e0ac8d11abdae0e83ab8204981/README.md#L185-L185), [README.md#L193-L196](https://github.com/fstandhartinger/ralph-wiggum/blob/3f15f0fb83b8c2e0ac8d11abdae0e83ab8204981/README.md#L193-L196) (`clm_92e51fa9f1505abca14ac91957c2d6af977a6a7b04997b81dc7cacca8a86cd97`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: AGENTS.md and CLAUDE.md instruct contributing agents to read .specify/memory/constitution.md on every session as the single source of all project instructions, including workflow configuration and autonomy settings. -- evidence: [AGENTS.md#L3-L3](https://github.com/fstandhartinger/ralph-wiggum/blob/3f15f0fb83b8c2e0ac8d11abdae0e83ab8204981/AGENTS.md#L3-L3), [AGENTS.md#L13-L13](https://github.com/fstandhartinger/ralph-wiggum/blob/3f15f0fb83b8c2e0ac8d11abdae0e83ab8204981/AGENTS.md#L13-L13), [AGENTS.md#L5-L11](https://github.com/fstandhartinger/ralph-wiggum/blob/3f15f0fb83b8c2e0ac8d11abdae0e83ab8204981/AGENTS.md#L5-L11), [CLAUDE.md#L3-L3](https://github.com/fstandhartinger/ralph-wiggum/blob/3f15f0fb83b8c2e0ac8d11abdae0e83ab8204981/CLAUDE.md#L3-L3), [CLAUDE.md#L5-L5](https://github.com/fstandhartinger/ralph-wiggum/blob/3f15f0fb83b8c2e0ac8d11abdae0e83ab8204981/CLAUDE.md#L5-L5) (`clm_28ccb4c02b0b51060976382a98a7bf1f9c520c4575c19df06abac47eb5cc4bc8`)
- [observation/documented] Repository development practice: agent instructions define context detection between Ralph-loop mode (implement specs, output the DONE promise) and interactive chat mode (guide the user, create specs). -- evidence: [AGENTS.md#L20-L22](https://github.com/fstandhartinger/ralph-wiggum/blob/3f15f0fb83b8c2e0ac8d11abdae0e83ab8204981/AGENTS.md#L20-L22), [AGENTS.md#L31-L31](https://github.com/fstandhartinger/ralph-wiggum/blob/3f15f0fb83b8c2e0ac8d11abdae0e83ab8204981/AGENTS.md#L31-L31), [AGENTS.md#L24-L24](https://github.com/fstandhartinger/ralph-wiggum/blob/3f15f0fb83b8c2e0ac8d11abdae0e83ab8204981/AGENTS.md#L24-L24), [CLAUDE.md#L7-L7](https://github.com/fstandhartinger/ralph-wiggum/blob/3f15f0fb83b8c2e0ac8d11abdae0e83ab8204981/CLAUDE.md#L7-L7), [AGENTS.md#L27-L29](https://github.com/fstandhartinger/ralph-wiggum/blob/3f15f0fb83b8c2e0ac8d11abdae0e83ab8204981/AGENTS.md#L27-L29) (`clm_6404b50af2024321701aa65060e58ca8e6bd70939ed11164ed6626fb0282a790`)

## skills-patterns (1 claim(s))

- [observation/documented] The repo follows the Agent Skills specification and can be installed via Vercel add-skill, OpenSkills, or Skillset, and is advertised as working with Claude Code, Cursor, Codex, Windsurf, Amp, and OpenCode. -- evidence: [README.md#L311-L311](https://github.com/fstandhartinger/ralph-wiggum/blob/3f15f0fb83b8c2e0ac8d11abdae0e83ab8204981/README.md#L311-L311), [README.md#L303-L303](https://github.com/fstandhartinger/ralph-wiggum/blob/3f15f0fb83b8c2e0ac8d11abdae0e83ab8204981/README.md#L303-L303), [README.md#L305-L309](https://github.com/fstandhartinger/ralph-wiggum/blob/3f15f0fb83b8c2e0ac8d11abdae0e83ab8204981/README.md#L305-L309) (`clm_3f9a6bce0346428987b51aad7688ebbc8a095abb4f8e9692e697b477a6012454`)

## interfaces (2 claim(s))

- [observation/documented] The product is driven by shell scripts: ralph-loop.sh (default build mode) and an optional 'plan' mode invoked as ralph-loop.sh plan, with matching PowerShell .ps1 variants. -- evidence: [README.md#L94-L95](https://github.com/fstandhartinger/ralph-wiggum/blob/3f15f0fb83b8c2e0ac8d11abdae0e83ab8204981/README.md#L94-L95), [README.md#L89-L92](https://github.com/fstandhartinger/ralph-wiggum/blob/3f15f0fb83b8c2e0ac8d11abdae0e83ab8204981/README.md#L89-L92) (`clm_c8dae0f491917aabb4b0b0f8b0ad0550810fe64a1742919014dae28be3df35d1`)
- [observation/documented] Build mode can take an iteration-count argument, e.g. ralph-loop.sh 20 for a maximum of 20 iterations, or run unlimited by default. -- evidence: [README.md#L160-L163](https://github.com/fstandhartinger/ralph-wiggum/blob/3f15f0fb83b8c2e0ac8d11abdae0e83ab8204981/README.md#L160-L163) (`clm_679b873b4faed71c7713b5ca64686ecf1c1612b3ff32e459e6d0e8dbce97fccf`)

## memory-state (2 claim(s))

- [observation/documented] State persists on disk between loops: IMPLEMENTATION_PLAN.md is read to pick tasks and updated with progress, while each iteration starts with a fresh context window. -- evidence: [README.md#L276-L276](https://github.com/fstandhartinger/ralph-wiggum/blob/3f15f0fb83b8c2e0ac8d11abdae0e83ab8204981/README.md#L276-L276), [README.md#L273-L273](https://github.com/fstandhartinger/ralph-wiggum/blob/3f15f0fb83b8c2e0ac8d11abdae0e83ab8204981/README.md#L273-L273), [README.md#L37-L41](https://github.com/fstandhartinger/ralph-wiggum/blob/3f15f0fb83b8c2e0ac8d11abdae0e83ab8204981/README.md#L37-L41) (`clm_806b0ce8ea54bd68c16e2646dd8bd37bfe7fdde8ae2614d55fc88ae69a2f6f65`)
- [observation/documented] A constitution file at .specify/memory/constitution.md is described as the single source of truth for agent behavior, with optional features configured there rather than in scripts. -- evidence: [README.md#L245-L264](https://github.com/fstandhartinger/ralph-wiggum/blob/3f15f0fb83b8c2e0ac8d11abdae0e83ab8204981/README.md#L245-L264), [README.md#L266-L266](https://github.com/fstandhartinger/ralph-wiggum/blob/3f15f0fb83b8c2e0ac8d11abdae0e83ab8204981/README.md#L266-L266) (`clm_f8d1071f814782656569037bd4722f66f8ef289e741e6686ff5e94f5250d4287`)

## orchestration (1 claim(s))

- [observation/documented] The tool runs an iterative loop: each iteration orients from specs, picks one task, implements and tests it, verifies criteria, commits and pushes, then repeats until a DONE marker appears. -- evidence: [README.md#L33-L33](https://github.com/fstandhartinger/ralph-wiggum/blob/3f15f0fb83b8c2e0ac8d11abdae0e83ab8204981/README.md#L33-L33), [README.md#L165-L171](https://github.com/fstandhartinger/ralph-wiggum/blob/3f15f0fb83b8c2e0ac8d11abdae0e83ab8204981/README.md#L165-L171), [README.md#L49-L74](https://github.com/fstandhartinger/ralph-wiggum/blob/3f15f0fb83b8c2e0ac8d11abdae0e83ab8204981/README.md#L49-L74) (`clm_5cfef2c437f4a1984835c7ec3cc3c7e6664fe1f52cda09c69bc12793a4fdb842`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## limitations (1 claim(s))

- [observation/documented] The README warns the tool grants AI agents significant autonomy over the codebase and system, advising users to review all changes and run in isolated environments when possible. -- evidence: [README.md#L7-L7](https://github.com/fstandhartinger/ralph-wiggum/blob/3f15f0fb83b8c2e0ac8d11abdae0e83ab8204981/README.md#L7-L7) (`clm_60a4e65bc90653f61abc493742e4517f8465be9bd87d52a3ddd3f360cee4a86b`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

