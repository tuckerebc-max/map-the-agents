# norvialabs/forge

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 8a1c5e85ec5c @ d8ce37fcadf8e938

## Summary (orientation draft, not independently verified)

Forge is an open-source Rust terminal coding environment (alpha) combining agent sessions, editing, shell, and sandboxed tool execution in one TUI, with durable SQLite journals, child-agent orchestration, and OS-enforced sandboxing with proxy-controlled network egress. All prior claims were verified against the cited slices except the design-system hue-invariant claim, which was revised to only what its cited slice states. Evidence coverage: 130 of 315 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 9 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 20 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

20 claim(s) across 10 facet(s); 3 facet(s) unknown.

- specifications (2 claim(s)):
  - [observation/documented] Forge is an open-source terminal coding environment for working with AI agents, combining agent conversations, file explorer, Vim-style editing, shell, diffs, approvals, and multiple durable sessions in one keyboard-driven TUI. -- evidence: [README.md#L13-L16](https://github.com/NorviaLabs/forge/blob/8a1c5e85ec5cd0dce38ba64a205d212c822488d2/README.md#L13-L16)
  - [observation/documented] The project describes itself as alpha software and advises reviewing every approval prompt and using it first in a disposable or backed-up repository. -- evidence: [README.md#L23-L24](https://github.com/NorviaLabs/forge/blob/8a1c5e85ec5cd0dce38ba64a205d212c822488d2/README.md#L23-L24)
- components (1 claim(s)):
  - [observation/documented] Forge is a Rust workspace whose main crates include forge-cli (entry point), forge-tui (terminal interface), forge-core (agent loop and session lifecycle), forge-model, forge-connect, forge-tools, and forge-durable (SQLite journals). -- evidence: [README.md#L597-L603](https://github.com/NorviaLabs/forge/blob/8a1c5e85ec5cd0dce38ba64a205d212c822488d2/README.md#L597-L603), [README.md#L595-L595](https://github.com/NorviaLabs/forge/blob/8a1c5e85ec5cd0dce38ba64a205d212c822488d2/README.md#L595-L595)
- design-choices (2 claim(s)):
  - [observation/documented] Colours are semantic tokens defined per theme rather than fixed hex values, and the design system names ACCENT_STATUS_MIN_HUE_DISTANCE as its single hardest rule, asserted over built-in themes in tests. -- evidence: [FORGE-DESIGN.md#L208-L208](https://github.com/NorviaLabs/forge/blob/8a1c5e85ec5cd0dce38ba64a205d212c822488d2/FORGE-DESIGN.md#L208-L208), [FORGE-DESIGN.md#L171-L171](https://github.com/NorviaLabs/forge/blob/8a1c5e85ec5cd0dce38ba64a205d212c822488d2/FORGE-DESIGN.md#L171-L171)
  - [observation/documented] Core UX invariants include exactly one effective keyboard owner at a time, colour never being the sole state indicator, approvals and failures outranking routine activity, and refusing to render below an enforced minimum of 80x18. -- evidence: [FORGE-DESIGN.md#L157-L167](https://github.com/NorviaLabs/forge/blob/8a1c5e85ec5cd0dce38ba64a205d212c822488d2/FORGE-DESIGN.md#L157-L167)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributors are told to run cargo fmt --check, cargo clippy with -D warnings, and cargo test --workspace before submitting a change, with further guidance in CONTRIBUTING.md. -- evidence: [README.md#L607-L611](https://github.com/NorviaLabs/forge/blob/8a1c5e85ec5cd0dce38ba64a205d212c822488d2/README.md#L607-L611), [README.md#L605-L605](https://github.com/NorviaLabs/forge/blob/8a1c5e85ec5cd0dce38ba64a205d212c822488d2/README.md#L605-L605), [README.md#L613-L613](https://github.com/NorviaLabs/forge/blob/8a1c5e85ec5cd0dce38ba64a205d212c822488d2/README.md#L613-L613)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (4 claim(s)):
  - [observation/documented] The TUI exposes in-app slash commands such as /connect, /model, /resume, /continue, /fork, /compact, /terminal, /theme, /effort, /thinking, /status, and /quit. -- evidence: [README.md#L173-L192](https://github.com/NorviaLabs/forge/blob/8a1c5e85ec5cd0dce38ba64a205d212c822488d2/README.md#L173-L192)
  - [observation/documented] Documented CLI forms include bare `forge`, `forge --continue`, `forge --resume [<session-id>]`, and `forge --fork <session-id>`; the default workspace is the current directory, overridable via FORGE_WORKSPACE. -- evidence: [README.md#L194-L196](https://github.com/NorviaLabs/forge/blob/8a1c5e85ec5cd0dce38ba64a205d212c822488d2/README.md#L194-L196), [README.md#L560-L566](https://github.com/NorviaLabs/forge/blob/8a1c5e85ec5cd0dce38ba64a205d212c822488d2/README.md#L560-L566), [README.md#L114-L115](https://github.com/NorviaLabs/forge/blob/8a1c5e85ec5cd0dce38ba64a205d212c822488d2/README.md#L114-L115), [README.md#L548-L550](https://github.com/NorviaLabs/forge/blob/8a1c5e85ec5cd0dce38ba64a205d212c822488d2/README.md#L548-L550), [README.md#L552-L553](https://github.com/NorviaLabs/forge/blob/8a1c5e85ec5cd0dce38ba64a205d212c822488d2/README.md#L552-L553), [README.md#L555-L558](https://github.com/NorviaLabs/forge/blob/8a1c5e85ec5cd0dce38ba64a205d212c822488d2/README.md#L555-L558), [README.md#L110-L112](https://github.com/NorviaLabs/forge/blob/8a1c5e85ec5cd0dce38ba64a205d212c822488d2/README.md#L110-L112)
- memory-state (1 claim(s)):
More evidence: [full detail](forge.detail.md)

Metadata and full claim list: [full detail](forge.detail.md)
Human notes ([notes](forge.notes.md), never overwritten by build)

[Back to map index](../../index.md)
