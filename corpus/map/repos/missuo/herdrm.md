# missuo/herdrm

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit baca2c2bcc85 @ a6dc06822f9ab0ee

## Summary (orientation draft, not independently verified)

herdrm is a native macOS (and iOS) SwiftUI console for the herdr coding-agent runtime, providing multi-device SSH/Tailcat device management, live PTY terminal attach, file transfer, search, and notifications. Evidence is README/CHANGELOG documentation plus contributor instructions; no source code slices are present.

## Source coverage

Source coverage (partial): 3 of 4 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 20 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

20 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (2 claim(s)):
  - [observation/documented] herdrm requires macOS 14 or later, a local herdr installation (which herdrm will start if not running), and herdr on remote machines. -- evidence: [README.md#L134-L137](https://github.com/missuo/herdrm/blob/baca2c2bcc85bd3a38f9a5a04db15fe8956a8d54/README.md#L134-L137)
  - [observation/documented] Remote device access requires OpenSSH, Tailscale SSH 1.98.0+, or a Keychain-stored password per the requirements section. -- evidence: [README.md#L134-L137](https://github.com/missuo/herdrm/blob/baca2c2bcc85bd3a38f9a5a04db15fe8956a8d54/README.md#L134-L137)
- components (3 claim(s)):
  - [observation/documented] The architecture has three layers: the herdr daemon owning PTYs, the HerdrKit transport/domain Swift package, and the Sources/HerdrM SwiftUI shell. -- evidence: [README.md#L161-L168](https://github.com/missuo/herdrm/blob/baca2c2bcc85bd3a38f9a5a04db15fe8956a8d54/README.md#L161-L168), [README.md#L170-L175](https://github.com/missuo/herdrm/blob/baca2c2bcc85bd3a38f9a5a04db15fe8956a8d54/README.md#L170-L175)
  - [observation/documented] HerdrKit ships as an independently testable Swift package covering socket-RPC, SSH tunneling, and device storage. -- evidence: [README.md#L170-L175](https://github.com/missuo/herdrm/blob/baca2c2bcc85bd3a38f9a5a04db15fe8956a8d54/README.md#L170-L175), [README.md#L106-L110](https://github.com/missuo/herdrm/blob/baca2c2bcc85bd3a38f9a5a04db15fe8956a8d54/README.md#L106-L110)
- design-choices (2 claim(s)):
  - [observation/documented] herdrm is built in SwiftUI as a native Mac app with no Electron or browser engine, positioned as fast and lightweight. -- evidence: [README.md#L121-L130](https://github.com/missuo/herdrm/blob/baca2c2bcc85bd3a38f9a5a04db15fe8956a8d54/README.md#L121-L130)
  - [observation/documented] The embedded terminal renders via libghostty (Metal) rather than SwiftTerm, with herdrm layering light-mode color adaptation, readline chords, and agent-aware paste on top. -- evidence: [CHANGELOG.md#L44-L58](https://github.com/missuo/herdrm/blob/baca2c2bcc85bd3a38f9a5a04db15fe8956a8d54/CHANGELOG.md#L44-L58)
- workflows (3 claim(s)):
  - [observation/documented] Repository development practice: contributors build with `make build`/`make run` and run HerdrKit integration tests via `make kit-test`, which needs a running local herdr; PRs are expected to pass these locally since there is no CI gate yet. -- evidence: [README.md#L190-L194](https://github.com/missuo/herdrm/blob/baca2c2bcc85bd3a38f9a5a04db15fe8956a8d54/README.md#L190-L194), [README.md#L179-L184](https://github.com/missuo/herdrm/blob/baca2c2bcc85bd3a38f9a5a04db15fe8956a8d54/README.md#L179-L184)
  - [observation/documented] Repository development practice: pushing a v* tag triggers release automation that builds, notarizes, Sparkle-signs, and publishes a release, and CI fails if CHANGELOG.md lacks a matching version section. -- evidence: [README.md#L190-L194](https://github.com/missuo/herdrm/blob/baca2c2bcc85bd3a38f9a5a04db15fe8956a8d54/README.md#L190-L194), [CHANGELOG.md#L3-L6](https://github.com/missuo/herdrm/blob/baca2c2bcc85bd3a38f9a5a04db15fe8956a8d54/CHANGELOG.md#L3-L6), [CLAUDE.md#L51-L62](https://github.com/missuo/herdrm/blob/baca2c2bcc85bd3a38f9a5a04db15fe8956a8d54/CLAUDE.md#L51-L62)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (4 claim(s)):
  - [observation/documented] herdrm attaches to agent or shell PTYs via `herdr agent attach` and `herdr terminal attach`, grabbing keyboard focus on jump. -- evidence: [README.md#L80-L91](https://github.com/missuo/herdrm/blob/baca2c2bcc85bd3a38f9a5a04db15fe8956a8d54/README.md#L80-L91)
  - [observation/documented] Keyboard shortcuts include ⌘N for a new agent, ⌘T for a new terminal, ⇧⌘N for a new space, and ⌘K for cross-device search. -- evidence: [README.md#L94-L103](https://github.com/missuo/herdrm/blob/baca2c2bcc85bd3a38f9a5a04db15fe8956a8d54/README.md#L94-L103), [README.md#L68-L77](https://github.com/missuo/herdrm/blob/baca2c2bcc85bd3a38f9a5a04db15fe8956a8d54/README.md#L68-L77)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
More evidence: [full detail](herdrm.detail.md)

Metadata and full claim list: [full detail](herdrm.detail.md)
Human notes ([notes](herdrm.notes.md), never overwritten by build)

[Back to map index](../../index.md)
