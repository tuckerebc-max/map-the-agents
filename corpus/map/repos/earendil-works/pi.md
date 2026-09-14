# earendil-works/pi

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 71dca871bc80 @ 03b32de110df5c1d

## Summary (orientation draft, not independently verified)

The repository is a monorepo for the Pi agent harness, containing a coding-agent CLI, agent runtime, multi-provider LLM API, TUI library, telemetry package, and chord composition runtime. Evidence covers its permission model, security trust boundary, supply-chain and contribution practices, and a detailed TUI alternate-screen layout plan. Evidence coverage: 152 of 291 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (complete): 5 of 5 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The repository is a monorepo whose packages include a coding-agent CLI, an agent runtime with tool calling and state management, a multi-provider LLM API, a TUI library, a telemetry package, and a chord application-composition runtime. -- evidence: [README.md#L17-L19](https://github.com/earendil-works/pi/blob/71dca871bc80b6bc97be37f0ca3189399d651fff/README.md#L17-L19), [README.md#L28-L35](https://github.com/earendil-works/pi/blob/71dca871bc80b6bc97be37f0ca3189399d651fff/README.md#L28-L35)
- design-choices (3 claim(s)):
  - [observation/documented] The TUI plan introduces a constrained alternate-screen layout so the coding-agent transcript scrolls while pending messages, status, editor, and footer stay fixed at the bottom; main-screen mode keeps terminal-owned scrolling. -- evidence: [tui-plan.md#L28-L28](https://github.com/earendil-works/pi/blob/71dca871bc80b6bc97be37f0ca3189399d651fff/tui-plan.md#L28-L28), [tui-plan.md#L5-L5](https://github.com/earendil-works/pi/blob/71dca871bc80b6bc97be37f0ca3189399d651fff/tui-plan.md#L5-L5), [tui-plan.md#L54-L70](https://github.com/earendil-works/pi/blob/71dca871bc80b6bc97be37f0ca3189399d651fff/tui-plan.md#L54-L70)
  - [observation/documented] The internal layout tree is rebuilt per requested render as a transient frame snapshot, while the public component tree stays long-lived and stateful; leaf render caches in Markdown, Text, Image, and Box are reused. -- evidence: [tui-plan.md#L368-L372](https://github.com/earendil-works/pi/blob/71dca871bc80b6bc97be37f0ca3189399d651fff/tui-plan.md#L368-L372), [tui-plan.md#L323-L323](https://github.com/earendil-works/pi/blob/71dca871bc80b6bc97be37f0ca3189399d651fff/tui-plan.md#L323-L323), [tui-plan.md#L343-L343](https://github.com/earendil-works/pi/blob/71dca871bc80b6bc97be37f0ca3189399d651fff/tui-plan.md#L343-L343), [tui-plan.md#L334-L334](https://github.com/earendil-works/pi/blob/71dca871bc80b6bc97be37f0ca3189399d651fff/tui-plan.md#L334-L334)
- workflows (3 claim(s)):
  - [observation/documented] Repository development practice: new contributors' issues and PRs are auto-closed by default and reviewed daily by maintainers, per CONTRIBUTING.md. -- evidence: [README.md#L11-L11](https://github.com/earendil-works/pi/blob/71dca871bc80b6bc97be37f0ca3189399d651fff/README.md#L11-L11)
  - [observation/documented] Repository development practice: development uses npm install --ignore-scripts, npm run build/check, ./test.sh (skipping LLM-dependent tests without API keys), and ./pi-test.sh to run pi from sources. -- evidence: [README.md#L55-L62](https://github.com/earendil-works/pi/blob/71dca871bc80b6bc97be37f0ca3189399d651fff/README.md#L55-L62)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The planned public layout primitives are VStack, HStack, and ScrollView, with stack entries configured via basis, grow, shrink, minSize, maxSize, and a viewport-dependent visible predicate. -- evidence: [tui-plan.md#L11-L24](https://github.com/earendil-works/pi/blob/71dca871bc80b6bc97be37f0ca3189399d651fff/tui-plan.md#L11-L24), [tui-plan.md#L120-L134](https://github.com/earendil-works/pi/blob/71dca871bc80b6bc97be37f0ca3189399d651fff/tui-plan.md#L120-L134)
  - [observation/documented] Constrained layout is exposed via a ViewportTUI capability interface with setLayoutRoot; TuiAltScreen implements it while TuiMainScreen does not, and a type guard checks the capability rather than using instanceof. -- evidence: [tui-plan.md#L263-L263](https://github.com/earendil-works/pi/blob/71dca871bc80b6bc97be37f0ca3189399d651fff/tui-plan.md#L263-L263), [tui-plan.md#L253-L256](https://github.com/earendil-works/pi/blob/71dca871bc80b6bc97be37f0ca3189399d651fff/tui-plan.md#L253-L256), [tui-plan.md#L261-L261](https://github.com/earendil-works/pi/blob/71dca871bc80b6bc97be37f0ca3189399d651fff/tui-plan.md#L261-L261)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
  - [observation/documented] Pi ships without a built-in permission system for filesystem, process, network, or credential access; by default it runs with the permissions of the launching user and process. -- evidence: [README.md#L41-L41](https://github.com/earendil-works/pi/blob/71dca871bc80b6bc97be37f0ca3189399d651fff/README.md#L41-L41)
More evidence: [full detail](pi.detail.md)

Metadata and full claim list: [full detail](pi.detail.md)
Human notes ([notes](pi.notes.md), never overwritten by build)

[Back to map index](../../index.md)
