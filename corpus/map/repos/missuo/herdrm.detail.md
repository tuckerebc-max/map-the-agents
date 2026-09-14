# missuo/herdrm -- full detail

[Back to orientation](herdrm.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/missuo/herdrm/baca2c2bcc85bd3a38f9a5a04db15fe8956a8d54/a6dc06822f9ab0ee.json](../../../wiki/dossiers/missuo/herdrm/baca2c2bcc85bd3a38f9a5a04db15fe8956a8d54/a6dc06822f9ab0ee.json)

## specifications (2 claim(s))

- [observation/documented] herdrm requires macOS 14 or later, a local herdr installation (which herdrm will start if not running), and herdr on remote machines. -- evidence: [README.md#L134-L137](https://github.com/missuo/herdrm/blob/baca2c2bcc85bd3a38f9a5a04db15fe8956a8d54/README.md#L134-L137) (`clm_4893d093bf2f90a9c9e5f96d99df2a07c223fce713b76a33f8c4b12259a5cde4`)
- [observation/documented] Remote device access requires OpenSSH, Tailscale SSH 1.98.0+, or a Keychain-stored password per the requirements section. -- evidence: [README.md#L134-L137](https://github.com/missuo/herdrm/blob/baca2c2bcc85bd3a38f9a5a04db15fe8956a8d54/README.md#L134-L137) (`clm_3dbf03fe8521179ea30ae6f5fc5ea68aed3362dff5edb5715e872197c78758a4`)

## components (3 claim(s))

- [observation/documented] The architecture has three layers: the herdr daemon owning PTYs, the HerdrKit transport/domain Swift package, and the Sources/HerdrM SwiftUI shell. -- evidence: [README.md#L161-L168](https://github.com/missuo/herdrm/blob/baca2c2bcc85bd3a38f9a5a04db15fe8956a8d54/README.md#L161-L168), [README.md#L170-L175](https://github.com/missuo/herdrm/blob/baca2c2bcc85bd3a38f9a5a04db15fe8956a8d54/README.md#L170-L175) (`clm_5e278322dbe1d7cc5c9ee0209c572ea03d2abba295f077cd0bec1e13d1bf2e9e`)
- [observation/documented] HerdrKit ships as an independently testable Swift package covering socket-RPC, SSH tunneling, and device storage. -- evidence: [README.md#L170-L175](https://github.com/missuo/herdrm/blob/baca2c2bcc85bd3a38f9a5a04db15fe8956a8d54/README.md#L170-L175), [README.md#L106-L110](https://github.com/missuo/herdrm/blob/baca2c2bcc85bd3a38f9a5a04db15fe8956a8d54/README.md#L106-L110) (`clm_d9ebf410eb576b2cf9854f99e6ab5fb2e71868921d45ecacbe2d871f02ec27b4`)
- [observation/documented] A two-pane file manager browses local and SSH files side by side with transfers supporting progress, cancellation, and Replace/Keep Both conflict handling. -- evidence: [README.md#L94-L103](https://github.com/missuo/herdrm/blob/baca2c2bcc85bd3a38f9a5a04db15fe8956a8d54/README.md#L94-L103), [CHANGELOG.md#L148-L159](https://github.com/missuo/herdrm/blob/baca2c2bcc85bd3a38f9a5a04db15fe8956a8d54/CHANGELOG.md#L148-L159) (`clm_669f94fde187ef1bfc843da0287eb170cb4f28f90ac137a3808b729ab4933e44`)

## design-choices (2 claim(s))

- [observation/documented] herdrm is built in SwiftUI as a native Mac app with no Electron or browser engine, positioned as fast and lightweight. -- evidence: [README.md#L121-L130](https://github.com/missuo/herdrm/blob/baca2c2bcc85bd3a38f9a5a04db15fe8956a8d54/README.md#L121-L130) (`clm_9bca59aaef9dda3cb03fb80a24b5c2b9ca02ab4f6e71ecc001b9062d82edfbab`)
- [observation/documented] The embedded terminal renders via libghostty (Metal) rather than SwiftTerm, with herdrm layering light-mode color adaptation, readline chords, and agent-aware paste on top. -- evidence: [CHANGELOG.md#L44-L58](https://github.com/missuo/herdrm/blob/baca2c2bcc85bd3a38f9a5a04db15fe8956a8d54/CHANGELOG.md#L44-L58) (`clm_6af4d840972683d52c763ad52341452a3af85f677e3d54088169363b1486bad3`)

## workflows (3 claim(s))

- [observation/documented] Repository development practice: contributors build with `make build`/`make run` and run HerdrKit integration tests via `make kit-test`, which needs a running local herdr; PRs are expected to pass these locally since there is no CI gate yet. -- evidence: [README.md#L190-L194](https://github.com/missuo/herdrm/blob/baca2c2bcc85bd3a38f9a5a04db15fe8956a8d54/README.md#L190-L194), [README.md#L179-L184](https://github.com/missuo/herdrm/blob/baca2c2bcc85bd3a38f9a5a04db15fe8956a8d54/README.md#L179-L184) (`clm_071558c16704b69beb76ec1a08c70fa38f36b805ef6ad4b7ba0fa8fd3f522868`)
- [observation/documented] Repository development practice: pushing a v* tag triggers release automation that builds, notarizes, Sparkle-signs, and publishes a release, and CI fails if CHANGELOG.md lacks a matching version section. -- evidence: [README.md#L190-L194](https://github.com/missuo/herdrm/blob/baca2c2bcc85bd3a38f9a5a04db15fe8956a8d54/README.md#L190-L194), [CHANGELOG.md#L3-L6](https://github.com/missuo/herdrm/blob/baca2c2bcc85bd3a38f9a5a04db15fe8956a8d54/CHANGELOG.md#L3-L6), [CLAUDE.md#L51-L62](https://github.com/missuo/herdrm/blob/baca2c2bcc85bd3a38f9a5a04db15fe8956a8d54/CLAUDE.md#L51-L62) (`clm_2fff585020710d7406ed760f7c86cc9007800753b22df2a23012ad968405703e`)
- [observation/documented] Repository development practice: bug reports should include macOS version, herdr --version, and repro steps; feature ideas beyond small PRs need an issue first. -- evidence: [README.md#L190-L194](https://github.com/missuo/herdrm/blob/baca2c2bcc85bd3a38f9a5a04db15fe8956a8d54/README.md#L190-L194) (`clm_3fd9fe8858c1a7c2d976926737af6f868e49c189168c912b6fddc2b8a0f6911d`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (4 claim(s))

- [observation/documented] herdrm attaches to agent or shell PTYs via `herdr agent attach` and `herdr terminal attach`, grabbing keyboard focus on jump. -- evidence: [README.md#L80-L91](https://github.com/missuo/herdrm/blob/baca2c2bcc85bd3a38f9a5a04db15fe8956a8d54/README.md#L80-L91) (`clm_cf9a04e4acfa918fe6dab69646adcae7e416d3758471b2d6c729d4e45776132b`)
- [observation/documented] Keyboard shortcuts include ⌘N for a new agent, ⌘T for a new terminal, ⇧⌘N for a new space, and ⌘K for cross-device search. -- evidence: [README.md#L94-L103](https://github.com/missuo/herdrm/blob/baca2c2bcc85bd3a38f9a5a04db15fe8956a8d54/README.md#L94-L103), [README.md#L68-L77](https://github.com/missuo/herdrm/blob/baca2c2bcc85bd3a38f9a5a04db15fe8956a8d54/README.md#L68-L77) (`clm_d481da6377de0ceb60333aa636616de6c813308e87c7a1bc2edd8dcb23bb6e5a`)
- [observation/documented] SSH targets accept user@host, user@host:port, ssh:// URIs, and ~/.ssh/config aliases, with auth falling back from OpenSSH keys to Tailscale SSH to a Keychain password. -- evidence: [README.md#L57-L65](https://github.com/missuo/herdrm/blob/baca2c2bcc85bd3a38f9a5a04db15fe8956a8d54/README.md#L57-L65) (`clm_e9afe460191ff3a8cc5d9cddf1161249151647fc60b07a9929371054cf869021`)
- [observation/documented] Remote pastes stream over SSH into a self-pruning cache with 7-day retention and a 50 MB cap, pasting the remote path into the agent. -- evidence: [README.md#L94-L103](https://github.com/missuo/herdrm/blob/baca2c2bcc85bd3a38f9a5a04db15fe8956a8d54/README.md#L94-L103), [CHANGELOG.md#L337-L346](https://github.com/missuo/herdrm/blob/baca2c2bcc85bd3a38f9a5a04db15fe8956a8d54/CHANGELOG.md#L337-L346) (`clm_2f4c402a8e5c1923d93bf74efbacb495153f337be0f3c7b8de1b19a7117f2df1`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] The app depends on Sparkle for auto-updates, is signed and notarized, and ships as a universal Apple Silicon/Intel binary. -- evidence: [README.md#L146-L148](https://github.com/missuo/herdrm/blob/baca2c2bcc85bd3a38f9a5a04db15fe8956a8d54/README.md#L146-L148), [README.md#L106-L110](https://github.com/missuo/herdrm/blob/baca2c2bcc85bd3a38f9a5a04db15fe8956a8d54/README.md#L106-L110) (`clm_560511041b639262f4f7a2609df2aea9bf67e6421fd1e3dba2e52b4d5c23820c`)
- [observation/documented] Credits include libghostty-spm for the Ghostty Metal terminal engine, the herdr.tailcat plugin, Heeler for domain/transport patterns, and waku as a sidebar design reference. -- evidence: [README.md#L198-L208](https://github.com/missuo/herdrm/blob/baca2c2bcc85bd3a38f9a5a04db15fe8956a8d54/README.md#L198-L208) (`clm_65d36fabb29e4b69d0f39c346a42795b443b387ad70431ced823180071750a00`)

## limitations (3 claim(s))

- [observation/documented] The project is explicitly early stage without full test coverage, and users are told to expect bugs. -- evidence: [README.md#L218-L218](https://github.com/missuo/herdrm/blob/baca2c2bcc85bd3a38f9a5a04db15fe8956a8d54/README.md#L218-L218), [README.md#L15-L21](https://github.com/missuo/herdrm/blob/baca2c2bcc85bd3a38f9a5a04db15fe8956a8d54/README.md#L15-L21) (`clm_b524f36ccafbc131b67667ca765ee36a70daded93acbf635f18c46846f0ac336`)
- [observation/documented] Tailcat devices pay a roughly 1-2 second tunnel handshake per operation, and standalone shells and the Files workspace still require SSH rather than the tunnel. -- evidence: [CHANGELOG.md#L63-L81](https://github.com/missuo/herdrm/blob/baca2c2bcc85bd3a38f9a5a04db15fe8956a8d54/CHANGELOG.md#L63-L81) (`clm_36b1573bbb5562055b08b47ec95ed140bef84db21623a3eb4a1daec021d3b13f`)
- [observation/documented] On the iOS/iPadOS client, tailcat devices carry herdr's control plane (spaces, agents, prompting) but not a live terminal, which remains SSH-only. -- evidence: [CHANGELOG.md#L44-L58](https://github.com/missuo/herdrm/blob/baca2c2bcc85bd3a38f9a5a04db15fe8956a8d54/CHANGELOG.md#L44-L58) (`clm_d6368bdbca0fed50f8b2df2b2b17415c11f40750c5b762409516802cb8841933`)

## relevance (1 claim(s))

- [observation/documented] herdrm is relevant to teams running coding agents (Claude Code, Codex, Gemini, Grok, OpenCode) across multiple machines who want a native GUI console instead of living in a terminal multiplexer. -- evidence: [README.md#L116-L119](https://github.com/missuo/herdrm/blob/baca2c2bcc85bd3a38f9a5a04db15fe8956a8d54/README.md#L116-L119), [README.md#L9-L13](https://github.com/missuo/herdrm/blob/baca2c2bcc85bd3a38f9a5a04db15fe8956a8d54/README.md#L9-L13), [README.md#L121-L130](https://github.com/missuo/herdrm/blob/baca2c2bcc85bd3a38f9a5a04db15fe8956a8d54/README.md#L121-L130) (`clm_996b16acb118e360d89ceb8f9d6b06f54661d4c4bda93b036087d4ef15349983`)

