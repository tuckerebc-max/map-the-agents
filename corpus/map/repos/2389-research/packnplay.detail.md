# 2389-research/packnplay -- full detail

[Back to orientation](packnplay.md)

## Origins

- alltheagents.org-site-pages

## Projects

- Observatory

Full evidence record (JSON): [wiki/dossiers/2389-research/packnplay/5abeea29178330dec7ba09c035934fa9416e2945/233c35e9bb5fb7ff.json](../../../wiki/dossiers/2389-research/packnplay/5abeea29178330dec7ba09c035934fa9416e2945/233c35e9bb5fb7ff.json)

## specifications (1 claim(s))

- [observation/documented] The plan's stated goal is to build packnplay, a CLI tool that launches commands such as Claude Code inside isolated Docker containers with automated worktree and dev container management. -- evidence: [docs/plans/2025-10-23-cage-implementation.md#L5-L5](https://github.com/2389-research/packnplay/blob/5abeea29178330dec7ba09c035934fa9416e2945/docs/plans/2025-10-23-cage-implementation.md#L5-L5) (`clm_5319cd5775e33e39f41437c598d82fc38335d7ba72994d4ea51d9840bebbe807`)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (5 claim(s))

- [observation/documented] The planned architecture is a single Go binary using cobra for the CLI that shells out to docker and git commands, uses idmap mounts for UID translation, and tracks container state via session-based Docker labels. -- evidence: [docs/plans/2025-10-23-cage-implementation.md#L7-L7](https://github.com/2389-research/packnplay/blob/5abeea29178330dec7ba09c035934fa9416e2945/docs/plans/2025-10-23-cage-implementation.md#L7-L7) (`clm_534b4ba5084422dd71da7164911d0f4e89e7fb2b272d206ce841a1085c41ee3e`)
- [observation/documented] The planned Docker client detects the container CLI by honoring a DOCKER_CMD environment variable override, then falling back to docker and then podman in PATH. -- evidence: [docs/plans/2025-10-23-cage-implementation.md#L438-L439](https://github.com/2389-research/packnplay/blob/5abeea29178330dec7ba09c035934fa9416e2945/docs/plans/2025-10-23-cage-implementation.md#L438-L439), [docs/plans/2025-10-23-cage-implementation.md#L418-L426](https://github.com/2389-research/packnplay/blob/5abeea29178330dec7ba09c035934fa9416e2945/docs/plans/2025-10-23-cage-implementation.md#L418-L426), [docs/plans/2025-10-23-cage-implementation.md#L433-L436](https://github.com/2389-research/packnplay/blob/5abeea29178330dec7ba09c035934fa9416e2945/docs/plans/2025-10-23-cage-implementation.md#L433-L436), [docs/plans/2025-10-23-cage-implementation.md#L428-L431](https://github.com/2389-research/packnplay/blob/5abeea29178330dec7ba09c035934fa9416e2945/docs/plans/2025-10-23-cage-implementation.md#L428-L431) (`clm_f61b1def94c89f3ec072ba41225a556370a610a6fe0f357656368ff227d9e2eb`)
- [observation/documented] Planned container naming combines a packnplay prefix, project name, and sanitized worktree name (slashes, spaces, and colons replaced with dashes), and containers carry managed-by, packnplay-project, and packnplay-worktree labels. -- evidence: [docs/plans/2025-10-23-cage-implementation.md#L886-L891](https://github.com/2389-research/packnplay/blob/5abeea29178330dec7ba09c035934fa9416e2945/docs/plans/2025-10-23-cage-implementation.md#L886-L891), [docs/plans/2025-10-23-cage-implementation.md#L893-L900](https://github.com/2389-research/packnplay/blob/5abeea29178330dec7ba09c035934fa9416e2945/docs/plans/2025-10-23-cage-implementation.md#L893-L900), [docs/plans/2025-10-23-cage-implementation.md#L902-L909](https://github.com/2389-research/packnplay/blob/5abeea29178330dec7ba09c035934fa9416e2945/docs/plans/2025-10-23-cage-implementation.md#L902-L909) (`clm_efe5496ea728902481eab0ce66c642cb95f0e06c1145cc88c98a57cc71095a9a`)
- [observation/documented] The plan specifies parsing .devcontainer/devcontainer.json for image, dockerFile, and remoteUser fields, defaulting remoteUser to devuser, and falling back to a default Ubuntu devcontainers image config when no devcontainer file exists. -- evidence: [docs/plans/2025-10-23-cage-implementation.md#L739-L744](https://github.com/2389-research/packnplay/blob/5abeea29178330dec7ba09c035934fa9416e2945/docs/plans/2025-10-23-cage-implementation.md#L739-L744), [docs/plans/2025-10-23-cage-implementation.md#L773-L780](https://github.com/2389-research/packnplay/blob/5abeea29178330dec7ba09c035934fa9416e2945/docs/plans/2025-10-23-cage-implementation.md#L773-L780), [docs/plans/2025-10-23-cage-implementation.md#L765-L768](https://github.com/2389-research/packnplay/blob/5abeea29178330dec7ba09c035934fa9416e2945/docs/plans/2025-10-23-cage-implementation.md#L765-L768) (`clm_1e888e5793ef069fda7d80fb09a9115ea1e56cf9bbbabaeb6b9f33568759e1cd`)
- [observation/documented] Planned worktree paths are computed as a sibling directory of the project named <project>-<sanitized-branch>, with branch names sanitized for filesystem safety. -- evidence: [docs/plans/2025-10-23-cage-implementation.md#L574-L582](https://github.com/2389-research/packnplay/blob/5abeea29178330dec7ba09c035934fa9416e2945/docs/plans/2025-10-23-cage-implementation.md#L574-L582), [docs/plans/2025-10-23-cage-implementation.md#L565-L568](https://github.com/2389-research/packnplay/blob/5abeea29178330dec7ba09c035934fa9416e2945/docs/plans/2025-10-23-cage-implementation.md#L565-L568), [docs/plans/2025-10-23-cage-implementation.md#L570-L572](https://github.com/2389-research/packnplay/blob/5abeea29178330dec7ba09c035934fa9416e2945/docs/plans/2025-10-23-cage-implementation.md#L570-L572) (`clm_a0b821f97eb2361c55a28964cdd1a8d1d690e0168a0111412ef0a6bf76cb590b`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: the plan document instructs the implementing agent to use the superpowers:executing-plans sub-skill to implement the plan task-by-task. -- evidence: [docs/plans/2025-10-23-cage-implementation.md#L3-L3](https://github.com/2389-research/packnplay/blob/5abeea29178330dec7ba09c035934fa9416e2945/docs/plans/2025-10-23-cage-implementation.md#L3-L3) (`clm_3ede4bc1da0046ce8e99979790b54a298b2c7298ee0dea1c49bd7a43c53a6b86`)
- [observation/documented] Repository development practice: the plan follows a test-first workflow per task — write a failing test, implement, re-run go test to verify it passes, then commit. -- evidence: [docs/plans/2025-10-23-cage-implementation.md#L383-L383](https://github.com/2389-research/packnplay/blob/5abeea29178330dec7ba09c035934fa9416e2945/docs/plans/2025-10-23-cage-implementation.md#L383-L383), [docs/plans/2025-10-23-cage-implementation.md#L459-L459](https://github.com/2389-research/packnplay/blob/5abeea29178330dec7ba09c035934fa9416e2945/docs/plans/2025-10-23-cage-implementation.md#L459-L459), [docs/plans/2025-10-23-cage-implementation.md#L465-L465](https://github.com/2389-research/packnplay/blob/5abeea29178330dec7ba09c035934fa9416e2945/docs/plans/2025-10-23-cage-implementation.md#L465-L465), [docs/plans/2025-10-23-cage-implementation.md#L387-L387](https://github.com/2389-research/packnplay/blob/5abeea29178330dec7ba09c035934fa9416e2945/docs/plans/2025-10-23-cage-implementation.md#L387-L387), [docs/plans/2025-10-23-cage-implementation.md#L463-L463](https://github.com/2389-research/packnplay/blob/5abeea29178330dec7ba09c035934fa9416e2945/docs/plans/2025-10-23-cage-implementation.md#L463-L463), [docs/plans/2025-10-23-cage-implementation.md#L328-L328](https://github.com/2389-research/packnplay/blob/5abeea29178330dec7ba09c035934fa9416e2945/docs/plans/2025-10-23-cage-implementation.md#L328-L328) (`clm_32d9e93b0cb1707578304da17f73f3c3439a4ac2a56abfbab4e50eb0b7775069`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] The planned CLI exposes four subcommands: run (with path, worktree, no-worktree, env, and verbose flags), attach, stop, and list, with attach and stop accepting path and worktree flags. -- evidence: [docs/plans/2025-10-23-cage-implementation.md#L263-L271](https://github.com/2389-research/packnplay/blob/5abeea29178330dec7ba09c035934fa9416e2945/docs/plans/2025-10-23-cage-implementation.md#L263-L271), [docs/plans/2025-10-23-cage-implementation.md#L179-L185](https://github.com/2389-research/packnplay/blob/5abeea29178330dec7ba09c035934fa9416e2945/docs/plans/2025-10-23-cage-implementation.md#L179-L185), [docs/plans/2025-10-23-cage-implementation.md#L101-L108](https://github.com/2389-research/packnplay/blob/5abeea29178330dec7ba09c035934fa9416e2945/docs/plans/2025-10-23-cage-implementation.md#L101-L108), [docs/plans/2025-10-23-cage-implementation.md#L215-L218](https://github.com/2389-research/packnplay/blob/5abeea29178330dec7ba09c035934fa9416e2945/docs/plans/2025-10-23-cage-implementation.md#L215-L218), [docs/plans/2025-10-23-cage-implementation.md#L248-L251](https://github.com/2389-research/packnplay/blob/5abeea29178330dec7ba09c035934fa9416e2945/docs/plans/2025-10-23-cage-implementation.md#L248-L251) (`clm_1b411e740c29587653e1e47ee10b3e51e0e99040316f3c5d30859ec9660d64ab`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The planned tech stack is Go 1.21+, the cobra CLI framework, and the Docker and git CLIs invoked via shell. -- evidence: [docs/plans/2025-10-23-cage-implementation.md#L9-L9](https://github.com/2389-research/packnplay/blob/5abeea29178330dec7ba09c035934fa9416e2945/docs/plans/2025-10-23-cage-implementation.md#L9-L9) (`clm_4bc7d8cde20e3290a1bae1b3b4be8cd1f14801b1e94a519b2d6249951337b17f`)

## limitations (1 claim(s))

- [inference/documented] The evidence consists only of an implementation plan; the run, attach, stop, and list commands are specified with TODO placeholders, so actual implemented behavior at this commit is not evidenced by these slices. -- evidence: [docs/plans/2025-10-23-cage-implementation.md#L263-L271](https://github.com/2389-research/packnplay/blob/5abeea29178330dec7ba09c035934fa9416e2945/docs/plans/2025-10-23-cage-implementation.md#L263-L271), [docs/plans/2025-10-23-cage-implementation.md#L202-L210](https://github.com/2389-research/packnplay/blob/5abeea29178330dec7ba09c035934fa9416e2945/docs/plans/2025-10-23-cage-implementation.md#L202-L210), [docs/plans/2025-10-23-cage-implementation.md#L235-L243](https://github.com/2389-research/packnplay/blob/5abeea29178330dec7ba09c035934fa9416e2945/docs/plans/2025-10-23-cage-implementation.md#L235-L243), [docs/plans/2025-10-23-cage-implementation.md#L165-L174](https://github.com/2389-research/packnplay/blob/5abeea29178330dec7ba09c035934fa9416e2945/docs/plans/2025-10-23-cage-implementation.md#L165-L174) (`clm_4f97b53d2f51f977de26991a9e1bc359183a0869db572842761dce2a52f43945`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

