---
access: public
aliases: []
claim_ids:
- clm_27c5fd616a6bb78ce44e987b77dd2849d5a1d674de895175f8fe837439961dd3
- clm_8d952bf274531ce9f46fcc62b8f7da2493203d2cf1108fff0fbc9ee5f316681f
- clm_92518f96d15259b252a258bc8fb5945243c130ed4f3068e35bc29c05c4af6bbb
- clm_9da3ebf2dc5c7b4247249dc256fdba2993dab45209210e763aa8fd4a939069c2
- clm_abaf41c91a4195f72f30d51363a9feb9a6902999967da1567841af94b676a9ec
- clm_b3c06bca6452961bc73c755ac617d5677c0fdba160034ac05b905170e618c5aa
- clm_e867879afd43104d0451c4171b89a378eff0933180e32bca3c879a68a7871040
- clm_ffe31cf9f6457fcf780241967a4e36e44e9507fef73317e0951bf56ba9418e6a
maturity: draft
page_id: pg_96d044035790531c9342eff4c194997b
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_c2047b91d510565c9fac6ccddddd7a04
title: tmux/tmux/SYNCING.md @ e880cf63e0a9
updated_at: '2026-09-14T04:26:40Z'
---

# tmux/tmux/SYNCING.md @ e880cf63e0a9

<!-- rcw:begin owner=source:src_c2047b91d510565c9fac6ccddddd7a04 block=evidence -->
- Repository development practice: the cutover repository has three branches — master (consumed by portable, tmux source only), openbsd-git (raw filtered OpenBSD history), and an orphan automation branch holding the GitHub Actions workflow so workflow files are not merged into portable. [@claim:clm_27c5fd616a6bb78ce44e987b77dd2849d5a1d674de895175f8fe837439961dd3]
- Repository development practice: manual cutover updates cherry-pick the origin/openbsd-git..openbsd-git range onto cutover master and push both branches; workflow files must stay off cutover master. [@claim:clm_8d952bf274531ce9f46fcc62b8f7da2493203d2cf1108fff0fbc9ee5f316681f]
- Repository development practice: the release process updates README and CHANGES, bumps the version in configure.ac, tags (e.g. git tag -a 2.X), builds a tarball with make dist, uploads it to a GitHub release, and updates the tmux.github.io RELEASE version. [@claim:clm_92518f96d15259b252a258bc8fb5945243c130ed4f3068e35bc29c05c4af6bbb]
- Repository development practice: if the automated merge into portable fails, maintainers merge locally with --no-ff --log, resolve conflicts by deciding whether portable or OpenBSD owns each file, then push and rerun the workflow. [@claim:clm_9da3ebf2dc5c7b4247249dc256fdba2993dab45209210e763aa8fd4a939069c2]
- Repository development practice: tmux portable is maintained from two repositories — the portable repo (portability layer, autotools build files, regression tests, docs) and the tmux-openbsd-cutover repo holding OpenBSD tmux history. [@claim:clm_abaf41c91a4195f72f30d51363a9feb9a6902999967da1567841af94b676a9ec]
- Repository development practice: the normal sync runs via a GitHub Actions workflow that blobless-clones OpenBSD src, filters usr.bin/tmux/, updates openbsd-git, cherry-picks onto cutover master, merges into portable master, and pushes. [@claim:clm_b3c06bca6452961bc73c755ac617d5677c0fdba160034ac05b905170e618c5aa]
- Repository development practice: much of tmux's compat/ code comes from OpenBSD libraries such as imsg, so maintainers are advised to periodically check OpenBSD libutil changes and sync relevant files into compat/. [@claim:clm_e867879afd43104d0451c4171b89a378eff0933180e32bca3c879a68a7871040]
- Repository development practice: an update automation filters OpenBSD's usr.bin/tmux/ into an openbsd-git branch, cherry-picks new commits onto cutover master, then merges cutover master into portable master. [@claim:clm_ffe31cf9f6457fcf780241967a4e36e44e9507fef73317e0951bf56ba9418e6a]
<!-- rcw:end owner=source:src_c2047b91d510565c9fac6ccddddd7a04 block=evidence -->

## Researcher notes

