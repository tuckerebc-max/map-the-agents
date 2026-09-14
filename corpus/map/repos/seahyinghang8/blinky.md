# seahyinghang8/blinky

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit f7a61326e723 @ d1be42b9542d8f68

## Summary (orientation draft, not independently verified)

Selected evidence records: Blinky is an open-source AI debugging agent for VSCode that uses LLMs to identify and fix backend code errors, inspired by SWE-agent. The agent leverages the VSCode API, the Language Server Protocol, and print statement debugging to triangulate bugs in real-world backend systems.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Blinky is an open-source AI debugging agent for VSCode that uses LLMs to identify and fix backend code errors, inspired by SWE-agent. -- evidence: [README.md#L14-L14](https://github.com/seahyinghang8/blinky/blob/f7a61326e72348c8cb3e50896095675c2ed98039/README.md#L14-L14), [README.md#L5-L10](https://github.com/seahyinghang8/blinky/blob/f7a61326e72348c8cb3e50896095675c2ed98039/README.md#L5-L10)
- components (1 claim(s)):
  - [observation/documented] The agent leverages the VSCode API, the Language Server Protocol, and print statement debugging to triangulate bugs in real-world backend systems. -- evidence: [README.md#L16-L16](https://github.com/seahyinghang8/blinky/blob/f7a61326e72348c8cb3e50896095675c2ed98039/README.md#L16-L16)
- design-choices (2 claim(s)):
  - [observation/documented] File editing uses a match-and-replace technique where the agent regenerates the original text with line numbers, which the README says helps catch hallucinations and bad indentation. -- evidence: [README.md#L74-L74](https://github.com/seahyinghang8/blinky/blob/f7a61326e72348c8cb3e50896095675c2ed98039/README.md#L74-L74), [README.md#L68-L68](https://github.com/seahyinghang8/blinky/blob/f7a61326e72348c8cb3e50896095675c2ed98039/README.md#L68-L68)
  - [observation/documented] The core agent loop was ported from SWE-agent, and the extension embeds it in VSCode so developers can give feedback mid-run. -- evidence: [README.md#L62-L62](https://github.com/seahyinghang8/blinky/blob/f7a61326e72348c8cb3e50896095675c2ed98039/README.md#L62-L62), [README.md#L66-L66](https://github.com/seahyinghang8/blinky/blob/f7a61326e72348c8cb3e50896095675c2ed98039/README.md#L66-L66)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributors can run `npm run install:all` and press F5 (Debug: Start Debugging) for local extension development, and prompts are edited in src/config/default.yaml before rebuilding. -- evidence: [README.md#L114-L114](https://github.com/seahyinghang8/blinky/blob/f7a61326e72348c8cb3e50896095675c2ed98039/README.md#L114-L114), [README.md#L94-L94](https://github.com/seahyinghang8/blinky/blob/f7a61326e72348c8cb3e50896095675c2ed98039/README.md#L94-L94)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] Users interact through a VSCode chat interface (ghost icon in the sidebar) where they describe the bug and optionally specify repro steps before starting the agent. -- evidence: [README.md#L22-L30](https://github.com/seahyinghang8/blinky/blob/f7a61326e72348c8cb3e50896095675c2ed98039/README.md#L22-L30)
  - [observation/documented] Users can configure a custom 'Build Ready Text' pattern via Advanced Settings under Specify Repro Steps, used by the verifier to detect when a build step completes. -- evidence: [README.md#L86-L90](https://github.com/seahyinghang8/blinky/blob/f7a61326e72348c8cb3e50896095675c2ed98039/README.md#L86-L90)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (1 claim(s)):
  - [observation/documented] User feedback given while the agent runs is incorporated into its subsequent step, and after completion the user can accept or reject the proposed changes. -- evidence: [README.md#L35-L36](https://github.com/seahyinghang8/blinky/blob/f7a61326e72348c8cb3e50896095675c2ed98039/README.md#L35-L36), [README.md#L32-L33](https://github.com/seahyinghang8/blinky/blob/f7a61326e72348c8cb3e50896095675c2ed98039/README.md#L32-L33)
- tools-permissions (2 claim(s)):
  - [observation/documented] The agent's tool set includes LSP-based navigation tools GoToDefinition and GetAllReferences, plus GetFilesRelevantToEndpoint for navigating backend systems. -- evidence: [README.md#L64-L64](https://github.com/seahyinghang8/blinky/blob/f7a61326e72348c8cb3e50896095675c2ed98039/README.md#L64-L64)
  - [observation/documented] A Verify tool runs the user-specified repro steps; the agent iteratively debugs until the repro test passes and uses execution feedback from its print statements. -- evidence: [README.md#L78-L78](https://github.com/seahyinghang8/blinky/blob/f7a61326e72348c8cb3e50896095675c2ed98039/README.md#L78-L78)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
More evidence: [full detail](blinky.detail.md)

Metadata and full claim list: [full detail](blinky.detail.md)
Human notes ([notes](blinky.notes.md), never overwritten by build)

[Back to map index](../../index.md)
