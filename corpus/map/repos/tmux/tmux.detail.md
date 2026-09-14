# tmux/tmux -- full detail

[Back to orientation](tmux.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/tmux/tmux/e880cf63e0a9fe095d7c5d313761520fb1a8653c/8337bf233b789259.json](../../../wiki/dossiers/tmux/tmux/e880cf63e0a9fe095d7c5d313761520fb1a8653c/8337bf233b789259.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (9 claim(s))

- [observation/documented] Repository development practice: security issues are reported by email to nicholas.marriott@gmail.com per SECURITY.md. -- evidence: [SECURITY.md#L1-L1](https://github.com/tmux/tmux/blob/e880cf63e0a9fe095d7c5d313761520fb1a8653c/SECURITY.md#L1-L1) (`clm_6971708f0f82f801bb8f6910b6ed8650bb7ad0ccfb91bde49be79de8c62b65c7`)
- [observation/documented] Repository development practice: tmux portable is maintained from two repositories — the portable repo (portability layer, autotools build files, regression tests, docs) and the tmux-openbsd-cutover repo holding OpenBSD tmux history. -- evidence: [SYNCING.md#L3-L3](https://github.com/tmux/tmux/blob/e880cf63e0a9fe095d7c5d313761520fb1a8653c/SYNCING.md#L3-L3), [SYNCING.md#L5-L10](https://github.com/tmux/tmux/blob/e880cf63e0a9fe095d7c5d313761520fb1a8653c/SYNCING.md#L5-L10) (`clm_abaf41c91a4195f72f30d51363a9feb9a6902999967da1567841af94b676a9ec`)
- [observation/documented] Repository development practice: an update automation filters OpenBSD's usr.bin/tmux/ into an openbsd-git branch, cherry-picks new commits onto cutover master, then merges cutover master into portable master. -- evidence: [SYNCING.md#L19-L22](https://github.com/tmux/tmux/blob/e880cf63e0a9fe095d7c5d313761520fb1a8653c/SYNCING.md#L19-L22) (`clm_ffe31cf9f6457fcf780241967a4e36e44e9507fef73317e0951bf56ba9418e6a`)
- [observation/documented] Repository development practice: the cutover repository has three branches — master (consumed by portable, tmux source only), openbsd-git (raw filtered OpenBSD history), and an orphan automation branch holding the GitHub Actions workflow so workflow files are not merged into portable. -- evidence: [SYNCING.md#L50-L55](https://github.com/tmux/tmux/blob/e880cf63e0a9fe095d7c5d313761520fb1a8653c/SYNCING.md#L50-L55) (`clm_27c5fd616a6bb78ce44e987b77dd2849d5a1d674de895175f8fe837439961dd3`)
- [observation/documented] Repository development practice: the normal sync runs via a GitHub Actions workflow that blobless-clones OpenBSD src, filters usr.bin/tmux/, updates openbsd-git, cherry-picks onto cutover master, merges into portable master, and pushes. -- evidence: [SYNCING.md#L85-L90](https://github.com/tmux/tmux/blob/e880cf63e0a9fe095d7c5d313761520fb1a8653c/SYNCING.md#L85-L90), [SYNCING.md#L82-L83](https://github.com/tmux/tmux/blob/e880cf63e0a9fe095d7c5d313761520fb1a8653c/SYNCING.md#L82-L83) (`clm_b3c06bca6452961bc73c755ac617d5677c0fdba160034ac05b905170e618c5aa`)
- [observation/documented] Repository development practice: if the automated merge into portable fails, maintainers merge locally with --no-ff --log, resolve conflicts by deciding whether portable or OpenBSD owns each file, then push and rerun the workflow. -- evidence: [SYNCING.md#L164-L165](https://github.com/tmux/tmux/blob/e880cf63e0a9fe095d7c5d313761520fb1a8653c/SYNCING.md#L164-L165), [SYNCING.md#L99-L100](https://github.com/tmux/tmux/blob/e880cf63e0a9fe095d7c5d313761520fb1a8653c/SYNCING.md#L99-L100), [SYNCING.md#L121-L123](https://github.com/tmux/tmux/blob/e880cf63e0a9fe095d7c5d313761520fb1a8653c/SYNCING.md#L121-L123), [SYNCING.md#L125-L125](https://github.com/tmux/tmux/blob/e880cf63e0a9fe095d7c5d313761520fb1a8653c/SYNCING.md#L125-L125) (`clm_9da3ebf2dc5c7b4247249dc256fdba2993dab45209210e763aa8fd4a939069c2`)
- [observation/documented] Repository development practice: manual cutover updates cherry-pick the origin/openbsd-git..openbsd-git range onto cutover master and push both branches; workflow files must stay off cutover master. -- evidence: [SYNCING.md#L169-L171](https://github.com/tmux/tmux/blob/e880cf63e0a9fe095d7c5d313761520fb1a8653c/SYNCING.md#L169-L171), [SYNCING.md#L184-L189](https://github.com/tmux/tmux/blob/e880cf63e0a9fe095d7c5d313761520fb1a8653c/SYNCING.md#L184-L189), [SYNCING.md#L191-L192](https://github.com/tmux/tmux/blob/e880cf63e0a9fe095d7c5d313761520fb1a8653c/SYNCING.md#L191-L192) (`clm_8d952bf274531ce9f46fcc62b8f7da2493203d2cf1108fff0fbc9ee5f316681f`)
- [observation/documented] Repository development practice: much of tmux's compat/ code comes from OpenBSD libraries such as imsg, so maintainers are advised to periodically check OpenBSD libutil changes and sync relevant files into compat/. -- evidence: [SYNCING.md#L196-L199](https://github.com/tmux/tmux/blob/e880cf63e0a9fe095d7c5d313761520fb1a8653c/SYNCING.md#L196-L199) (`clm_e867879afd43104d0451c4171b89a378eff0933180e32bca3c879a68a7871040`)
- [observation/documented] Repository development practice: the release process updates README and CHANGES, bumps the version in configure.ac, tags (e.g. git tag -a 2.X), builds a tarball with make dist, uploads it to a GitHub release, and updates the tmux.github.io RELEASE version. -- evidence: [SYNCING.md#L229-L234](https://github.com/tmux/tmux/blob/e880cf63e0a9fe095d7c5d313761520fb1a8653c/SYNCING.md#L229-L234), [SYNCING.md#L210-L212](https://github.com/tmux/tmux/blob/e880cf63e0a9fe095d7c5d313761520fb1a8653c/SYNCING.md#L210-L212), [SYNCING.md#L222-L223](https://github.com/tmux/tmux/blob/e880cf63e0a9fe095d7c5d313761520fb1a8653c/SYNCING.md#L222-L223), [SYNCING.md#L203-L208](https://github.com/tmux/tmux/blob/e880cf63e0a9fe095d7c5d313761520fb1a8653c/SYNCING.md#L203-L208) (`clm_92518f96d15259b252a258bc8fb5945243c130ed4f3068e35bc29c05c4af6bbb`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

