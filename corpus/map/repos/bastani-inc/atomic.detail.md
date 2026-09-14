# bastani-inc/atomic -- full detail

[Back to orientation](atomic.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/bastani-inc/atomic/ca64fa07885f0a1ef2d04a99f4e682de082a9341/cc096d4fbf9ff28b.json](../../../wiki/dossiers/bastani-inc/atomic/ca64fa07885f0a1ef2d04a99f4e682de082a9341/cc096d4fbf9ff28b.json)

## specifications (1 claim(s))

- [observation/documented] Workflows are authored as TypeScript workflow({...}) definitions whose stage dependencies must form a directed acyclic graph; cyclic graphs are unsupported, and loop/repair iterations must create distinct tracked work per iteration. -- evidence: [README.md#L898-L898](https://github.com/bastani-inc/atomic/blob/ca64fa07885f0a1ef2d04a99f4e682de082a9341/README.md#L898-L898), [README.md#L958-L958](https://github.com/bastani-inc/atomic/blob/ca64fa07885f0a1ef2d04a99f4e682de082a9341/README.md#L958-L958) (`clm_c6de7e1d48e5a0b82ad01433fe0a14b228ae2cee14bd2f607cafe5a17e4e34cb`)

## components (1 claim(s))

- [observation/documented] Atomic ships three top-level building blocks: workflows, skills, and specialized subagents, with nine bundled subagent definitions such as worker, debugger, and codebase-analyzer. -- evidence: [README.md#L954-L954](https://github.com/bastani-inc/atomic/blob/ca64fa07885f0a1ef2d04a99f4e682de082a9341/README.md#L954-L954), [README.md#L996-L1006](https://github.com/bastani-inc/atomic/blob/ca64fa07885f0a1ef2d04a99f4e682de082a9341/README.md#L996-L1006), [README.md#L994-L994](https://github.com/bastani-inc/atomic/blob/ca64fa07885f0a1ef2d04a99f4e682de082a9341/README.md#L994-L994) (`clm_754d00b01ed591828812e41971dfb6f30ace674d7ad6e0e7691abc9118ef4d82`)

## design-choices (1 claim(s))

- [observation/documented] The terminal UI uses a Catppuccin Mocha role-mapped palette with Catppuccin Blue as the sole accent, status colors mapped one-to-one to orchestrator session statuses, and Unicode-only iconography with no emoji. -- evidence: [DESIGN.md#L125-L132](https://github.com/bastani-inc/atomic/blob/ca64fa07885f0a1ef2d04a99f4e682de082a9341/DESIGN.md#L125-L132), [DESIGN.md#L139-L139](https://github.com/bastani-inc/atomic/blob/ca64fa07885f0a1ef2d04a99f4e682de082a9341/DESIGN.md#L139-L139), [DESIGN.md#L166-L166](https://github.com/bastani-inc/atomic/blob/ca64fa07885f0a1ef2d04a99f4e682de082a9341/DESIGN.md#L166-L166) (`clm_3b8355bc5017ac70fa08cf5c29fe3b69fc3c4030b40832ab0d959edf0f488e8e`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (1 claim(s))

- [observation/documented] Atomic implements the Agent Skills standard and can use configured Claude Code or Codex skill directories without rewriting them; skills can be auto-selected from descriptions or invoked with /skill:<name>. -- evidence: [README.md#L974-L974](https://github.com/bastani-inc/atomic/blob/ca64fa07885f0a1ef2d04a99f4e682de082a9341/README.md#L974-L974), [README.md#L351-L351](https://github.com/bastani-inc/atomic/blob/ca64fa07885f0a1ef2d04a99f4e682de082a9341/README.md#L351-L351) (`clm_1aa62b3f9bf573abec8aaa02356bec1f8463366f73aac39a829e198d15b6c490`)

## interfaces (2 claim(s))

- [observation/documented] The CLI exposes workflow management commands including /workflow list, inputs, status, connect, quit, and resume; quitting pauses a run so it can resume later. -- evidence: [README.md#L970-L970](https://github.com/bastani-inc/atomic/blob/ca64fa07885f0a1ef2d04a99f4e682de082a9341/README.md#L970-L970) (`clm_55718a22ece9d6a122c394ad39ed3fdc21cdd4afca19a238bc2dde8da0525145`)
- [observation/documented] Non-interactive use is supported via atomic -p "<prompt>", which prints the response and exits; provider credentials are stored in ~/.atomic/agent/auth.json with owner-only permissions where the platform supports them. -- evidence: [README.md#L334-L334](https://github.com/bastani-inc/atomic/blob/ca64fa07885f0a1ef2d04a99f4e682de082a9341/README.md#L334-L334) (`clm_7f35ecc6278348c7f94936dc04ee74c2e91852fbd716819ceb6918d9e18075db`)

## memory-state (1 claim(s))

- [observation/documented] Workflows persist artifacts such as plans, logs, transcripts, reviewer notes, check output, and summaries; research commonly lives in research/ and specs in specs/. -- evidence: [README.md#L1047-L1047](https://github.com/bastani-inc/atomic/blob/ca64fa07885f0a1ef2d04a99f4e682de082a9341/README.md#L1047-L1047) (`clm_414978fb23471071bb022d4cf608c86ee6867ee13e6ad9a60d81d0ca52c71f69`)

## orchestration (1 claim(s))

- [observation/documented] Stages can prompt an agent, run tools, call MCP servers, save artifacts, branch, retry, run in parallel, or pause for approval; specialized subagents handle focused work while a parent agent or workflow controls the larger task. -- evidence: [README.md#L894-L894](https://github.com/bastani-inc/atomic/blob/ca64fa07885f0a1ef2d04a99f4e682de082a9341/README.md#L894-L894), [README.md#L904-L904](https://github.com/bastani-inc/atomic/blob/ca64fa07885f0a1ef2d04a99f4e682de082a9341/README.md#L904-L904) (`clm_4f8d76953140fdfd7d146670d8c5e9dd2a9c28a6595be59bc45bb0036bcc6a23`)

## tools-permissions (1 claim(s))

- [observation/documented] Atomic has no built-in sandbox or command-level shell permission gate; tools and extensions run with the user's permissions, and the README recommends running autonomous work in a devcontainer, VM, or remote machine. -- evidence: [README.md#L338-L338](https://github.com/bastani-inc/atomic/blob/ca64fa07885f0a1ef2d04a99f4e682de082a9341/README.md#L338-L338) (`clm_e4867eaf18a8eb7ef33839806768004447c1628fc545d196f5445953c2c808d4`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] Package installation requires Node.js 22.19 or newer plus npm, pnpm, Yarn, or Bun (Bun 1.4.2+ for Bun installs); a self-contained release archive path needs no Node.js or package manager. -- evidence: [README.md#L289-L289](https://github.com/bastani-inc/atomic/blob/ca64fa07885f0a1ef2d04a99f4e682de082a9341/README.md#L289-L289), [README.md#L263-L265](https://github.com/bastani-inc/atomic/blob/ca64fa07885f0a1ef2d04a99f4e682de082a9341/README.md#L263-L265) (`clm_8b6d78c7883d39f4daaed1ea64c035cbcc03b56b98af96984f64eee318396bd2`)
- [observation/documented] Atomic is a fork of Pi and works with providers, tools, MCP servers, skills, and extensions from an existing Pi stack; it connects to model providers directly rather than wrapping other coding tools. -- evidence: [README.md#L896-L896](https://github.com/bastani-inc/atomic/blob/ca64fa07885f0a1ef2d04a99f4e682de082a9341/README.md#L896-L896), [README.md#L1027-L1027](https://github.com/bastani-inc/atomic/blob/ca64fa07885f0a1ef2d04a99f4e682de082a9341/README.md#L1027-L1027) (`clm_3ed2955cbcbfe13de480288197471e8a07f4f1b57883a3b3367d18588f7f5676`)

## limitations (1 claim(s))

- [observation/documented] The Linux musl release archives bundle their C++ runtime and run on stock Alpine, but Android and Termux are unsupported; provider availability depends on credentials, subscription, region, and the provider catalog. -- evidence: [README.md#L309-L309](https://github.com/bastani-inc/atomic/blob/ca64fa07885f0a1ef2d04a99f4e682de082a9341/README.md#L309-L309), [README.md#L230-L230](https://github.com/bastani-inc/atomic/blob/ca64fa07885f0a1ef2d04a99f4e682de082a9341/README.md#L230-L230) (`clm_4ae536c8d4bfc6d3685b31f4c3e160a2720366ec7111e1f4906e8089e5fe2a13`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

