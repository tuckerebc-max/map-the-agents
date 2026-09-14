---
access: public
aliases: []
claim_ids:
- clm_071558c16704b69beb76ec1a08c70fa38f36b805ef6ad4b7ba0fa8fd3f522868
- clm_2f4c402a8e5c1923d93bf74efbacb495153f337be0f3c7b8de1b19a7117f2df1
- clm_2fff585020710d7406ed760f7c86cc9007800753b22df2a23012ad968405703e
- clm_3dbf03fe8521179ea30ae6f5fc5ea68aed3362dff5edb5715e872197c78758a4
- clm_3fd9fe8858c1a7c2d976926737af6f868e49c189168c912b6fddc2b8a0f6911d
- clm_4893d093bf2f90a9c9e5f96d99df2a07c223fce713b76a33f8c4b12259a5cde4
- clm_560511041b639262f4f7a2609df2aea9bf67e6421fd1e3dba2e52b4d5c23820c
- clm_5e278322dbe1d7cc5c9ee0209c572ea03d2abba295f077cd0bec1e13d1bf2e9e
- clm_65d36fabb29e4b69d0f39c346a42795b443b387ad70431ced823180071750a00
- clm_669f94fde187ef1bfc843da0287eb170cb4f28f90ac137a3808b729ab4933e44
- clm_996b16acb118e360d89ceb8f9d6b06f54661d4c4bda93b036087d4ef15349983
- clm_9bca59aaef9dda3cb03fb80a24b5c2b9ca02ab4f6e71ecc001b9062d82edfbab
- clm_b524f36ccafbc131b67667ca765ee36a70daded93acbf635f18c46846f0ac336
- clm_cf9a04e4acfa918fe6dab69646adcae7e416d3758471b2d6c729d4e45776132b
- clm_d481da6377de0ceb60333aa636616de6c813308e87c7a1bc2edd8dcb23bb6e5a
- clm_d9ebf410eb576b2cf9854f99e6ab5fb2e71868921d45ecacbe2d871f02ec27b4
- clm_e9afe460191ff3a8cc5d9cddf1161249151647fc60b07a9929371054cf869021
maturity: draft
page_id: pg_beba02caad835a22b914db0922f22b73
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_78068da0b2245abaac887b61e1391cf2
title: missuo/herdrm/README.md @ baca2c2bcc85
updated_at: '2026-09-14T02:20:03Z'
---

# missuo/herdrm/README.md @ baca2c2bcc85

<!-- rcw:begin owner=source:src_78068da0b2245abaac887b61e1391cf2 block=evidence -->
- Repository development practice: contributors build with `make build`/`make run` and run HerdrKit integration tests via `make kit-test`, which needs a running local herdr; PRs are expected to pass these locally since there is no CI gate yet. [@claim:clm_071558c16704b69beb76ec1a08c70fa38f36b805ef6ad4b7ba0fa8fd3f522868]
- Remote pastes stream over SSH into a self-pruning cache with 7-day retention and a 50 MB cap, pasting the remote path into the agent. [@claim:clm_2f4c402a8e5c1923d93bf74efbacb495153f337be0f3c7b8de1b19a7117f2df1]
- Repository development practice: pushing a v* tag triggers release automation that builds, notarizes, Sparkle-signs, and publishes a release, and CI fails if CHANGELOG.md lacks a matching version section. [@claim:clm_2fff585020710d7406ed760f7c86cc9007800753b22df2a23012ad968405703e]
- Remote device access requires OpenSSH, Tailscale SSH 1.98.0+, or a Keychain-stored password per the requirements section. [@claim:clm_3dbf03fe8521179ea30ae6f5fc5ea68aed3362dff5edb5715e872197c78758a4]
- Repository development practice: bug reports should include macOS version, herdr --version, and repro steps; feature ideas beyond small PRs need an issue first. [@claim:clm_3fd9fe8858c1a7c2d976926737af6f868e49c189168c912b6fddc2b8a0f6911d]
- herdrm requires macOS 14 or later, a local herdr installation (which herdrm will start if not running), and herdr on remote machines. [@claim:clm_4893d093bf2f90a9c9e5f96d99df2a07c223fce713b76a33f8c4b12259a5cde4]
- The app depends on Sparkle for auto-updates, is signed and notarized, and ships as a universal Apple Silicon/Intel binary. [@claim:clm_560511041b639262f4f7a2609df2aea9bf67e6421fd1e3dba2e52b4d5c23820c]
- The architecture has three layers: the herdr daemon owning PTYs, the HerdrKit transport/domain Swift package, and the Sources/HerdrM SwiftUI shell. [@claim:clm_5e278322dbe1d7cc5c9ee0209c572ea03d2abba295f077cd0bec1e13d1bf2e9e]
- Credits include libghostty-spm for the Ghostty Metal terminal engine, the herdr.tailcat plugin, Heeler for domain/transport patterns, and waku as a sidebar design reference. [@claim:clm_65d36fabb29e4b69d0f39c346a42795b443b387ad70431ced823180071750a00]
- A two-pane file manager browses local and SSH files side by side with transfers supporting progress, cancellation, and Replace/Keep Both conflict handling. [@claim:clm_669f94fde187ef1bfc843da0287eb170cb4f28f90ac137a3808b729ab4933e44]
- herdrm is relevant to teams running coding agents (Claude Code, Codex, Gemini, Grok, OpenCode) across multiple machines who want a native GUI console instead of living in a terminal multiplexer. [@claim:clm_996b16acb118e360d89ceb8f9d6b06f54661d4c4bda93b036087d4ef15349983]
- herdrm is built in SwiftUI as a native Mac app with no Electron or browser engine, positioned as fast and lightweight. [@claim:clm_9bca59aaef9dda3cb03fb80a24b5c2b9ca02ab4f6e71ecc001b9062d82edfbab]
- The project is explicitly early stage without full test coverage, and users are told to expect bugs. [@claim:clm_b524f36ccafbc131b67667ca765ee36a70daded93acbf635f18c46846f0ac336]
- herdrm attaches to agent or shell PTYs via `herdr agent attach` and `herdr terminal attach`, grabbing keyboard focus on jump. [@claim:clm_cf9a04e4acfa918fe6dab69646adcae7e416d3758471b2d6c729d4e45776132b]
- Keyboard shortcuts include ⌘N for a new agent, ⌘T for a new terminal, ⇧⌘N for a new space, and ⌘K for cross-device search. [@claim:clm_d481da6377de0ceb60333aa636616de6c813308e87c7a1bc2edd8dcb23bb6e5a]
- HerdrKit ships as an independently testable Swift package covering socket-RPC, SSH tunneling, and device storage. [@claim:clm_d9ebf410eb576b2cf9854f99e6ab5fb2e71868921d45ecacbe2d871f02ec27b4]
- SSH targets accept user@host, user@host:port, ssh:// URIs, and ~/.ssh/config aliases, with auth falling back from OpenSSH keys to Tailscale SSH to a Keychain password. [@claim:clm_e9afe460191ff3a8cc5d9cddf1161249151647fc60b07a9929371054cf869021]
<!-- rcw:end owner=source:src_78068da0b2245abaac887b61e1391cf2 block=evidence -->

## Researcher notes

