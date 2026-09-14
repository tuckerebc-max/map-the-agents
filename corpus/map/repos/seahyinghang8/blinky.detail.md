# seahyinghang8/blinky -- full detail

[Back to orientation](blinky.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/seahyinghang8/blinky/f7a61326e72348c8cb3e50896095675c2ed98039/d1be42b9542d8f68.json](../../../wiki/dossiers/seahyinghang8/blinky/f7a61326e72348c8cb3e50896095675c2ed98039/d1be42b9542d8f68.json)

## specifications (1 claim(s))

- [observation/documented] Blinky is an open-source AI debugging agent for VSCode that uses LLMs to identify and fix backend code errors, inspired by SWE-agent. -- evidence: [README.md#L14-L14](https://github.com/seahyinghang8/blinky/blob/f7a61326e72348c8cb3e50896095675c2ed98039/README.md#L14-L14), [README.md#L5-L10](https://github.com/seahyinghang8/blinky/blob/f7a61326e72348c8cb3e50896095675c2ed98039/README.md#L5-L10) (`clm_c03401602f3efe4b5aa47169866f5035af5ceaddf90de6b21d7e78c692774bdb`)

## components (1 claim(s))

- [observation/documented] The agent leverages the VSCode API, the Language Server Protocol, and print statement debugging to triangulate bugs in real-world backend systems. -- evidence: [README.md#L16-L16](https://github.com/seahyinghang8/blinky/blob/f7a61326e72348c8cb3e50896095675c2ed98039/README.md#L16-L16) (`clm_fdd4c468589c0f5e9eff42ce185abf525ac5033509b7bb3525336959c77e5bee`)

## design-choices (2 claim(s))

- [observation/documented] File editing uses a match-and-replace technique where the agent regenerates the original text with line numbers, which the README says helps catch hallucinations and bad indentation. -- evidence: [README.md#L74-L74](https://github.com/seahyinghang8/blinky/blob/f7a61326e72348c8cb3e50896095675c2ed98039/README.md#L74-L74), [README.md#L68-L68](https://github.com/seahyinghang8/blinky/blob/f7a61326e72348c8cb3e50896095675c2ed98039/README.md#L68-L68) (`clm_59ff641efd91253dcc379f47fc6f81d5fe1c4cdb64f57a276d2cbde14b011d72`)
- [observation/documented] The core agent loop was ported from SWE-agent, and the extension embeds it in VSCode so developers can give feedback mid-run. -- evidence: [README.md#L62-L62](https://github.com/seahyinghang8/blinky/blob/f7a61326e72348c8cb3e50896095675c2ed98039/README.md#L62-L62), [README.md#L66-L66](https://github.com/seahyinghang8/blinky/blob/f7a61326e72348c8cb3e50896095675c2ed98039/README.md#L66-L66) (`clm_aa1a420b81d9c99d83801da8151cc8bd845ab6828840275eb504061f4bb6f980`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributors can run `npm run install:all` and press F5 (Debug: Start Debugging) for local extension development, and prompts are edited in src/config/default.yaml before rebuilding. -- evidence: [README.md#L114-L114](https://github.com/seahyinghang8/blinky/blob/f7a61326e72348c8cb3e50896095675c2ed98039/README.md#L114-L114), [README.md#L94-L94](https://github.com/seahyinghang8/blinky/blob/f7a61326e72348c8cb3e50896095675c2ed98039/README.md#L94-L94) (`clm_d1dded2f06fbeabe0c4f01a6905c45a241f42f783043c2cf638cddcf0c116098`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] Users interact through a VSCode chat interface (ghost icon in the sidebar) where they describe the bug and optionally specify repro steps before starting the agent. -- evidence: [README.md#L22-L30](https://github.com/seahyinghang8/blinky/blob/f7a61326e72348c8cb3e50896095675c2ed98039/README.md#L22-L30) (`clm_5a7c12c7943199fb22a78cbdc84a60c4be2c6f1e93433af0b6795ea3c7c1bdb8`)
- [observation/documented] Users can configure a custom 'Build Ready Text' pattern via Advanced Settings under Specify Repro Steps, used by the verifier to detect when a build step completes. -- evidence: [README.md#L86-L90](https://github.com/seahyinghang8/blinky/blob/f7a61326e72348c8cb3e50896095675c2ed98039/README.md#L86-L90) (`clm_328226f0af8ccfda90c12ccaeb893ce87a2776745045a97a973670284ea93a90`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (1 claim(s))

- [observation/documented] User feedback given while the agent runs is incorporated into its subsequent step, and after completion the user can accept or reject the proposed changes. -- evidence: [README.md#L35-L36](https://github.com/seahyinghang8/blinky/blob/f7a61326e72348c8cb3e50896095675c2ed98039/README.md#L35-L36), [README.md#L32-L33](https://github.com/seahyinghang8/blinky/blob/f7a61326e72348c8cb3e50896095675c2ed98039/README.md#L32-L33) (`clm_a11d6ee77adb30a487384e61082e83d0b9a7fe70455a7eb185dddcd4f7991ef1`)

## tools-permissions (2 claim(s))

- [observation/documented] The agent's tool set includes LSP-based navigation tools GoToDefinition and GetAllReferences, plus GetFilesRelevantToEndpoint for navigating backend systems. -- evidence: [README.md#L64-L64](https://github.com/seahyinghang8/blinky/blob/f7a61326e72348c8cb3e50896095675c2ed98039/README.md#L64-L64) (`clm_a29924d99170325e657ef9af5318a11c3ec9511c269c47df4fdb26178b5d0901`)
- [observation/documented] A Verify tool runs the user-specified repro steps; the agent iteratively debugs until the repro test passes and uses execution feedback from its print statements. -- evidence: [README.md#L78-L78](https://github.com/seahyinghang8/blinky/blob/f7a61326e72348c8cb3e50896095675c2ed98039/README.md#L78-L78) (`clm_c2fe49222c3b6ed5e1a4707b0da0d2b100b9325ed80c67b4fcc4e8e57606f26e`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] On first run the user is prompted for an OpenAI API key, which is stored locally in VSCode config for subsequent calls to OpenAI's server. -- evidence: [README.md#L20-L20](https://github.com/seahyinghang8/blinky/blob/f7a61326e72348c8cb3e50896095675c2ed98039/README.md#L20-L20) (`clm_cd6f3524cf536df7a18a2a209a6641189a90014a7245233c121ca8a8ae680647`)

## limitations (1 claim(s))

- [observation/documented] As of May 2024, per the README, SOTA LLMs struggle with large edits, motivating the match-and-replace editing approach; long builds are also cited as an unavoidable slowdown. -- evidence: [README.md#L86-L90](https://github.com/seahyinghang8/blinky/blob/f7a61326e72348c8cb3e50896095675c2ed98039/README.md#L86-L90), [README.md#L72-L72](https://github.com/seahyinghang8/blinky/blob/f7a61326e72348c8cb3e50896095675c2ed98039/README.md#L72-L72) (`clm_15f43c903d653b129f56f4a02a9ee5952827e071ddd556b1cba005519723ebd7`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

