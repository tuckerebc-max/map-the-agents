# lostintangent/conduit-release -- full detail

[Back to orientation](conduit-release.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/lostintangent/conduit-release/25766dcc59eebdb74059f90ad1df38838e58c865/19d04ef84883ae74.json](../../../wiki/dossiers/lostintangent/conduit-release/25766dcc59eebdb74059f90ad1df38838e58c865/19d04ef84883ae74.json)

## specifications (1 claim(s))

- [observation/documented] Conduit is described as a workspace manager for parallelizing coding tasks with agents across local and cloud compute, organizing work as flexible tabs of terminals, editors, and browsers. -- evidence: [README.md#L3-L3](https://github.com/lostintangent/conduit-release/blob/25766dcc59eebdb74059f90ad1df38838e58c865/README.md#L3-L3) (`clm_07294b9bfc7a157d7b7983bc3941a0218078700df3215ccb3713b9eb2ca58e7a`)

## components (2 claim(s))

- [observation/documented] Editor panes provide a file explorer and text editor with real-time git status, diffs, and stage/commit/push/pull actions, plus an integrated markdown preview. -- evidence: [README.md#L74-L74](https://github.com/lostintangent/conduit-release/blob/25766dcc59eebdb74059f90ad1df38838e58c865/README.md#L74-L74), [README.md#L70-L70](https://github.com/lostintangent/conduit-release/blob/25766dcc59eebdb74059f90ad1df38838e58c865/README.md#L70-L70) (`clm_13fb206a4b1a2d28abdcc0f39bd194333ca778bc2fb04e7e42a54205bbd1987b`)
- [observation/documented] Clicking a URL in a terminal opens a browser pane for navigating, testing, debugging, and favoriting web pages without leaving the app. -- evidence: [README.md#L80-L80](https://github.com/lostintangent/conduit-release/blob/25766dcc59eebdb74059f90ad1df38838e58c865/README.md#L80-L80) (`clm_987d6c36310179eb30c9de532e5c2ed99fde3d78ac82c1fc38f63f2cb1bd2043`)

## design-choices (1 claim(s))

- [observation/documented] The project's stated assumptions include supporting multiple coding agents with a learn-once experience, staying close to the metal, treating terminals as central, and emphasizing composability and personalization with smart defaults. -- evidence: [README.md#L130-L130](https://github.com/lostintangent/conduit-release/blob/25766dcc59eebdb74059f90ad1df38838e58c865/README.md#L130-L130), [README.md#L128-L128](https://github.com/lostintangent/conduit-release/blob/25766dcc59eebdb74059f90ad1df38838e58c865/README.md#L128-L128), [README.md#L132-L132](https://github.com/lostintangent/conduit-release/blob/25766dcc59eebdb74059f90ad1df38838e58c865/README.md#L132-L132), [README.md#L134-L134](https://github.com/lostintangent/conduit-release/blob/25766dcc59eebdb74059f90ad1df38838e58c865/README.md#L134-L134) (`clm_43aea20bc35442810522c008b1a5a0b3dec4d7cfa264b2bc39789ec61ea64282`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (4 claim(s))

- [observation/documented] Tabs support a resizable, collapsible, clonable grid of terminal, editor, and browser panes, and tabs can be locked to prevent accidental changes. -- evidence: [README.md#L18-L18](https://github.com/lostintangent/conduit-release/blob/25766dcc59eebdb74059f90ad1df38838e58c865/README.md#L18-L18), [README.md#L22-L22](https://github.com/lostintangent/conduit-release/blob/25766dcc59eebdb74059f90ad1df38838e58c865/README.md#L22-L22) (`clm_c735300e8d16be4bcdc83eebabe897673176ac5e959cd9f3c58150a5edd0894e`)
- [observation/documented] A `conduit` CLI lets users and coding agents design, interact with, and automate the dev environment, including terminals and browsers. -- evidence: [README.md#L96-L96](https://github.com/lostintangent/conduit-release/blob/25766dcc59eebdb74059f90ad1df38838e58c865/README.md#L96-L96) (`clm_5d16145fa958fe55207c130b48a720261f7410ab055da1085e41154c878c0891`)
- [observation/documented] Coding agents can be defined and configured, then recalled via a slash command from any terminal. -- evidence: [README.md#L38-L38](https://github.com/lostintangent/conduit-release/blob/25766dcc59eebdb74059f90ad1df38838e58c865/README.md#L38-L38) (`clm_a0567c9c2fc662a908c1fadaeb54e05d74d485e9cbd0a24fa8f82033f34cdbc7`)
- [observation/documented] Multiple terminal panes can be synchronized so typing steers them all at once; a command palette (cmd+shift+p) offers global commands including quick terminals with an MRU list. -- evidence: [README.md#L102-L102](https://github.com/lostintangent/conduit-release/blob/25766dcc59eebdb74059f90ad1df38838e58c865/README.md#L102-L102), [README.md#L120-L120](https://github.com/lostintangent/conduit-release/blob/25766dcc59eebdb74059f90ad1df38838e58c865/README.md#L120-L120) (`clm_f74c91c30d52a3f82f4c3274810a077424220d1f3dc6bb053dbcd47251bab8fe`)

## memory-state (1 claim(s))

- [observation/documented] Workspaces let users save and restore sets of tabs to move between projects easily. -- evidence: [README.md#L108-L108](https://github.com/lostintangent/conduit-release/blob/25766dcc59eebdb74059f90ad1df38838e58c865/README.md#L108-L108) (`clm_47ebc4fc9afe1c4048f450517e4a09e96c25c33a39743b00e4bfa34e816c64de`)

## orchestration (2 claim(s))

- [observation/documented] Users can create isolated agent sandboxes by splitting terminals or duplicating tabs, with automatic git worktree management. -- evidence: [README.md#L26-L26](https://github.com/lostintangent/conduit-release/blob/25766dcc59eebdb74059f90ad1df38838e58c865/README.md#L26-L26) (`clm_47ce09b5cdcfce06eaba2f30f2ef46765d1278dd5d85342d44dfe123ff666365`)
- [observation/documented] Cloud terminals can be spun up and mixed with local terminals to parallelize tasks further. -- evidence: [README.md#L32-L32](https://github.com/lostintangent/conduit-release/blob/25766dcc59eebdb74059f90ad1df38838e58c865/README.md#L32-L32) (`clm_95242b21ac0c971ef2c24a1328c2bb2e49e43b5b214529bb7f1c6887ee40a98e`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The latest release is distributed as a Conduit.dmg download and is currently macOS-only. -- evidence: [README.md#L9-L12](https://github.com/lostintangent/conduit-release/blob/25766dcc59eebdb74059f90ad1df38838e58c865/README.md#L9-L12) (`clm_a6aaaf366b8a0c71055a129766b4af55aba7560991c71389b482c445cf61174f`)

## limitations (1 claim(s))

- [observation/documented] The README frames the project as an exploration meant to be fun, questioning whether these primitives will suffice as coding agents grow more powerful. -- evidence: [README.md#L5-L5](https://github.com/lostintangent/conduit-release/blob/25766dcc59eebdb74059f90ad1df38838e58c865/README.md#L5-L5) (`clm_9345792f5e8b44e9789407a2070d9249283c2d31d3e282dd5316fd0b67db637b`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

