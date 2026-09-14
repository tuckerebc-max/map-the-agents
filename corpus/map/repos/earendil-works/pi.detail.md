# earendil-works/pi -- full detail

[Back to orientation](pi.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/earendil-works/pi/71dca871bc80b6bc97be37f0ca3189399d651fff/03b32de110df5c1d.json](../../../wiki/dossiers/earendil-works/pi/71dca871bc80b6bc97be37f0ca3189399d651fff/03b32de110df5c1d.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The repository is a monorepo whose packages include a coding-agent CLI, an agent runtime with tool calling and state management, a multi-provider LLM API, a TUI library, a telemetry package, and a chord application-composition runtime. -- evidence: [README.md#L17-L19](https://github.com/earendil-works/pi/blob/71dca871bc80b6bc97be37f0ca3189399d651fff/README.md#L17-L19), [README.md#L28-L35](https://github.com/earendil-works/pi/blob/71dca871bc80b6bc97be37f0ca3189399d651fff/README.md#L28-L35) (`clm_34bf24e120dc7f0549c6077e12267dd135a1d69b0fc7d66da1b2b35cd55d2d18`)

## design-choices (3 claim(s))

- [observation/documented] The TUI plan introduces a constrained alternate-screen layout so the coding-agent transcript scrolls while pending messages, status, editor, and footer stay fixed at the bottom; main-screen mode keeps terminal-owned scrolling. -- evidence: [tui-plan.md#L28-L28](https://github.com/earendil-works/pi/blob/71dca871bc80b6bc97be37f0ca3189399d651fff/tui-plan.md#L28-L28), [tui-plan.md#L5-L5](https://github.com/earendil-works/pi/blob/71dca871bc80b6bc97be37f0ca3189399d651fff/tui-plan.md#L5-L5), [tui-plan.md#L54-L70](https://github.com/earendil-works/pi/blob/71dca871bc80b6bc97be37f0ca3189399d651fff/tui-plan.md#L54-L70) (`clm_1c11ef75f4016822545696a3233d63e6a0b281534636937351726d5b84750c16`)
- [observation/documented] The internal layout tree is rebuilt per requested render as a transient frame snapshot, while the public component tree stays long-lived and stateful; leaf render caches in Markdown, Text, Image, and Box are reused. -- evidence: [tui-plan.md#L368-L372](https://github.com/earendil-works/pi/blob/71dca871bc80b6bc97be37f0ca3189399d651fff/tui-plan.md#L368-L372), [tui-plan.md#L323-L323](https://github.com/earendil-works/pi/blob/71dca871bc80b6bc97be37f0ca3189399d651fff/tui-plan.md#L323-L323), [tui-plan.md#L343-L343](https://github.com/earendil-works/pi/blob/71dca871bc80b6bc97be37f0ca3189399d651fff/tui-plan.md#L343-L343), [tui-plan.md#L334-L334](https://github.com/earendil-works/pi/blob/71dca871bc80b6bc97be37f0ca3189399d651fff/tui-plan.md#L334-L334) (`clm_9af5d3b81bedbed1dc88fb2cd0215eeb02332706642b51ed199c353349e289e9`)
- [observation/documented] Wheel events are hit-tested against the committed frame and routed from the deepest box upward, with overscroll chaining or containment, falling back to the primary scroll view; keyboard scrolling actions remain always available. -- evidence: [tui-plan.md#L517-L517](https://github.com/earendil-works/pi/blob/71dca871bc80b6bc97be37f0ca3189399d651fff/tui-plan.md#L517-L517), [tui-plan.md#L552-L552](https://github.com/earendil-works/pi/blob/71dca871bc80b6bc97be37f0ca3189399d651fff/tui-plan.md#L552-L552), [tui-plan.md#L528-L534](https://github.com/earendil-works/pi/blob/71dca871bc80b6bc97be37f0ca3189399d651fff/tui-plan.md#L528-L534) (`clm_7c84f0ded688464371f8545f706e76d5503c3655bd69ce36499ab24ddd991517`)

## workflows (3 claim(s))

- [observation/documented] Repository development practice: new contributors' issues and PRs are auto-closed by default and reviewed daily by maintainers, per CONTRIBUTING.md. -- evidence: [README.md#L11-L11](https://github.com/earendil-works/pi/blob/71dca871bc80b6bc97be37f0ca3189399d651fff/README.md#L11-L11) (`clm_20e24f06a0c4e72163e81c6327f59e640e68a8aa53d801a78838ce84b8529497`)
- [observation/documented] Repository development practice: development uses npm install --ignore-scripts, npm run build/check, ./test.sh (skipping LLM-dependent tests without API keys), and ./pi-test.sh to run pi from sources. -- evidence: [README.md#L55-L62](https://github.com/earendil-works/pi/blob/71dca871bc80b6bc97be37f0ca3189399d651fff/README.md#L55-L62) (`clm_1d57dcc7d3c0acc23dd46e1a7cbc70352c24b0eda74deec655337016955093c0`)
- [observation/documented] Repository development practice: npm dependency changes are treated as reviewed code changes, with CI installing via npm ci --ignore-scripts and a scheduled workflow running npm audit and signature checks. -- evidence: [README.md#L79-L79](https://github.com/earendil-works/pi/blob/71dca871bc80b6bc97be37f0ca3189399d651fff/README.md#L79-L79), [README.md#L81-L89](https://github.com/earendil-works/pi/blob/71dca871bc80b6bc97be37f0ca3189399d651fff/README.md#L81-L89) (`clm_fc57dc33369d45c5a0700ddf421df8311cd3c2c25b630888c303049e9d973ec1`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The planned public layout primitives are VStack, HStack, and ScrollView, with stack entries configured via basis, grow, shrink, minSize, maxSize, and a viewport-dependent visible predicate. -- evidence: [tui-plan.md#L11-L24](https://github.com/earendil-works/pi/blob/71dca871bc80b6bc97be37f0ca3189399d651fff/tui-plan.md#L11-L24), [tui-plan.md#L120-L134](https://github.com/earendil-works/pi/blob/71dca871bc80b6bc97be37f0ca3189399d651fff/tui-plan.md#L120-L134) (`clm_9858867453dde331039c980dac0b872b0f3117f15797ef68e9e470c2b7aa5d34`)
- [observation/documented] Constrained layout is exposed via a ViewportTUI capability interface with setLayoutRoot; TuiAltScreen implements it while TuiMainScreen does not, and a type guard checks the capability rather than using instanceof. -- evidence: [tui-plan.md#L263-L263](https://github.com/earendil-works/pi/blob/71dca871bc80b6bc97be37f0ca3189399d651fff/tui-plan.md#L263-L263), [tui-plan.md#L253-L256](https://github.com/earendil-works/pi/blob/71dca871bc80b6bc97be37f0ca3189399d651fff/tui-plan.md#L253-L256), [tui-plan.md#L261-L261](https://github.com/earendil-works/pi/blob/71dca871bc80b6bc97be37f0ca3189399d651fff/tui-plan.md#L261-L261) (`clm_0b02da203fcd2e0a243c4e30deaa795e79d4d8b59f5dfcea7e8a999bc22b8eff`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] Pi ships without a built-in permission system for filesystem, process, network, or credential access; by default it runs with the permissions of the launching user and process. -- evidence: [README.md#L41-L41](https://github.com/earendil-works/pi/blob/71dca871bc80b6bc97be37f0ca3189399d651fff/README.md#L41-L41) (`clm_5e55f3ee68c05787ef0368a9169f7df34aade2cdbd50369082d28d476404f066`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Direct external dependencies are pinned to exact versions, .npmrc sets save-exact and min-release-age=2, and the published CLI package carries a shrinkwrap file pinning transitive dependencies. -- evidence: [README.md#L81-L89](https://github.com/earendil-works/pi/blob/71dca871bc80b6bc97be37f0ca3189399d651fff/README.md#L81-L89) (`clm_3a5f6427ae410dc49efd65eecbe5d3a2903c060e330fb19dbd728850d8a939de`)

## limitations (1 claim(s))

- [observation/documented] The security policy states the coding agent intentionally has no sandbox, and prompt injection via files like AGENTS.md or code comments cannot be protected against, so users must trust extensions, skills, and repositories. -- evidence: [SECURITY.md#L50-L68](https://github.com/earendil-works/pi/blob/71dca871bc80b6bc97be37f0ca3189399d651fff/SECURITY.md#L50-L68), [SECURITY.md#L19-L22](https://github.com/earendil-works/pi/blob/71dca871bc80b6bc97be37f0ca3189399d651fff/SECURITY.md#L19-L22) (`clm_6fef1c235e06d3c3eae528698a9d75046e075b63f9c35a1d47b58111921ec569`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

