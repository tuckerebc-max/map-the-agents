---
access: public
aliases: []
claim_ids:
- clm_1b411e740c29587653e1e47ee10b3e51e0e99040316f3c5d30859ec9660d64ab
- clm_1e888e5793ef069fda7d80fb09a9115ea1e56cf9bbbabaeb6b9f33568759e1cd
- clm_32d9e93b0cb1707578304da17f73f3c3439a4ac2a56abfbab4e50eb0b7775069
- clm_3ede4bc1da0046ce8e99979790b54a298b2c7298ee0dea1c49bd7a43c53a6b86
- clm_4bc7d8cde20e3290a1bae1b3b4be8cd1f14801b1e94a519b2d6249951337b17f
- clm_4f97b53d2f51f977de26991a9e1bc359183a0869db572842761dce2a52f43945
- clm_5319cd5775e33e39f41437c598d82fc38335d7ba72994d4ea51d9840bebbe807
- clm_534b4ba5084422dd71da7164911d0f4e89e7fb2b272d206ce841a1085c41ee3e
- clm_a0b821f97eb2361c55a28964cdd1a8d1d690e0168a0111412ef0a6bf76cb590b
- clm_efe5496ea728902481eab0ce66c642cb95f0e06c1145cc88c98a57cc71095a9a
- clm_f61b1def94c89f3ec072ba41225a556370a610a6fe0f357656368ff227d9e2eb
maturity: draft
page_id: pg_4cc32fcc478a5365b239046415a369c8
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_dfa363a3a5005eb29eb6c7601d873320
title: 2389-research/packnplay/docs/plans/2025-10-23-cage-implementation.md @ 5abeea291783
updated_at: '2026-09-14T03:29:32Z'
---

# 2389-research/packnplay/docs/plans/2025-10-23-cage-implementation.md @ 5abeea291783

<!-- rcw:begin owner=source:src_dfa363a3a5005eb29eb6c7601d873320 block=evidence -->
- The planned CLI exposes four subcommands: run (with path, worktree, no-worktree, env, and verbose flags), attach, stop, and list, with attach and stop accepting path and worktree flags. [@claim:clm_1b411e740c29587653e1e47ee10b3e51e0e99040316f3c5d30859ec9660d64ab]
- The plan specifies parsing .devcontainer/devcontainer.json for image, dockerFile, and remoteUser fields, defaulting remoteUser to devuser, and falling back to a default Ubuntu devcontainers image config when no devcontainer file exists. [@claim:clm_1e888e5793ef069fda7d80fb09a9115ea1e56cf9bbbabaeb6b9f33568759e1cd]
- Repository development practice: the plan follows a test-first workflow per task — write a failing test, implement, re-run go test to verify it passes, then commit. [@claim:clm_32d9e93b0cb1707578304da17f73f3c3439a4ac2a56abfbab4e50eb0b7775069]
- Repository development practice: the plan document instructs the implementing agent to use the superpowers:executing-plans sub-skill to implement the plan task-by-task. [@claim:clm_3ede4bc1da0046ce8e99979790b54a298b2c7298ee0dea1c49bd7a43c53a6b86]
- The planned tech stack is Go 1.21+, the cobra CLI framework, and the Docker and git CLIs invoked via shell. [@claim:clm_4bc7d8cde20e3290a1bae1b3b4be8cd1f14801b1e94a519b2d6249951337b17f]
- The evidence consists only of an implementation plan; the run, attach, stop, and list commands are specified with TODO placeholders, so actual implemented behavior at this commit is not evidenced by these slices. [@claim:clm_4f97b53d2f51f977de26991a9e1bc359183a0869db572842761dce2a52f43945]
- The plan's stated goal is to build packnplay, a CLI tool that launches commands such as Claude Code inside isolated Docker containers with automated worktree and dev container management. [@claim:clm_5319cd5775e33e39f41437c598d82fc38335d7ba72994d4ea51d9840bebbe807]
- The planned architecture is a single Go binary using cobra for the CLI that shells out to docker and git commands, uses idmap mounts for UID translation, and tracks container state via session-based Docker labels. [@claim:clm_534b4ba5084422dd71da7164911d0f4e89e7fb2b272d206ce841a1085c41ee3e]
- Planned worktree paths are computed as a sibling directory of the project named <project>-<sanitized-branch>, with branch names sanitized for filesystem safety. [@claim:clm_a0b821f97eb2361c55a28964cdd1a8d1d690e0168a0111412ef0a6bf76cb590b]
- Planned container naming combines a packnplay prefix, project name, and sanitized worktree name (slashes, spaces, and colons replaced with dashes), and containers carry managed-by, packnplay-project, and packnplay-worktree labels. [@claim:clm_efe5496ea728902481eab0ce66c642cb95f0e06c1145cc88c98a57cc71095a9a]
- The planned Docker client detects the container CLI by honoring a DOCKER_CMD environment variable override, then falling back to docker and then podman in PATH. [@claim:clm_f61b1def94c89f3ec072ba41225a556370a610a6fe0f357656368ff227d9e2eb]
<!-- rcw:end owner=source:src_dfa363a3a5005eb29eb6c7601d873320 block=evidence -->

## Researcher notes

