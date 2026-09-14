# funador/claude-code-merge-queue -- full detail

[Back to orientation](claude-code-merge-queue.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/funador/claude-code-merge-queue/f77757479cab8031774495c4207647709199a954/52448af2613d1623.json](../../../wiki/dossiers/funador/claude-code-merge-queue/f77757479cab8031774495c4207647709199a954/52448af2613d1623.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (2 claim(s))

- [observation/documented] Configuration lives in a single .mjs file with fields for branchPrefix, worktreeSuffix, portBase, integration/production branches, protectedBranches, regenerableFiles, symlinks, buildOutputDirs, checkCommand, and checksRequired. -- evidence: [README.md#L47-L61](https://github.com/funador/claude-code-merge-queue/blob/f77757479cab8031774495c4207647709199a954/README.md#L47-L61), [README.md#L43-L45](https://github.com/funador/claude-code-merge-queue/blob/f77757479cab8031774495c4207647709199a954/README.md#L43-L45) (`clm_42f2d40aa060954133b2e3a998c95b76bbdce66389ca7c174fe7a3fd5c269496`)
- [observation/documented] Malformed configuration fails loudly at command load time, listing every problem (empty branch names, negative port, identical integration and production branches) rather than failing later. -- evidence: [README.md#L63-L66](https://github.com/funador/claude-code-merge-queue/blob/f77757479cab8031774495c4207647709199a954/README.md#L63-L66) (`clm_28477543ca06e8381941057e161dc27365868ec2e470d09ddbd2cbc6c7dca687`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The CLI exposes commands including hook worktree-create, build-lock, land, sync, promote, preview, port, and prune, each documented with its purpose. -- evidence: [README.md#L81-L90](https://github.com/funador/claude-code-merge-queue/blob/f77757479cab8031774495c4207647709199a954/README.md#L81-L90) (`clm_8d67d2cf16386f40107a22d686416c754a008965e48b8fda88689273b9406e20`)
- [observation/documented] An init command writes a config file, CLAUDE.md instructions, a .claude/settings.json hook wiring, Husky pre-push hook if present, and package.json scripts like land, sync, promote, preview. -- evidence: [README.md#L23-L26](https://github.com/funador/claude-code-merge-queue/blob/f77757479cab8031774495c4207647709199a954/README.md#L23-L26), [README.md#L101-L113](https://github.com/funador/claude-code-merge-queue/blob/f77757479cab8031774495c4207647709199a954/README.md#L101-L113) (`clm_8299b266e0a3b8e291f6c1407e0593361a9d20231bb3a408f730ac0c3d2818fa`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (2 claim(s))

- [observation/documented] The land command rebases and pushes a lane onto the integration branch through a FIFO queue so two lanes are never mid-push simultaneously; agents can run it themselves. -- evidence: [README.md#L81-L90](https://github.com/funador/claude-code-merge-queue/blob/f77757479cab8031774495c4207647709199a954/README.md#L81-L90) (`clm_f2cf10b8af9e939498d56fef386700b3262b8296964bbd4623851d0cfc138052`)
- [observation/documented] A WorktreeCreate hook plugs the tool's numbered lanes into Claude Code's native worktree creation, and build-lock serializes builds machine-wide across lanes. -- evidence: [README.md#L81-L90](https://github.com/funador/claude-code-merge-queue/blob/f77757479cab8031774495c4207647709199a954/README.md#L81-L90) (`clm_a0e10b4bc82e4c5175ff39eb3517c93b07f8522741993a31ef5d8eaf0c99e35b`)

## tools-permissions (2 claim(s))

- [observation/documented] A pre-push hook rejects direct git pushes to the integration branch and runs checkCommand before allowing a landing; with no checkCommand configured, every push fails by default. -- evidence: [README.md#L92-L97](https://github.com/funador/claude-code-merge-queue/blob/f77757479cab8031774495c4207647709199a954/README.md#L92-L97) (`clm_2c5447b7d4a3e98ce7f3a6aa9204b70692432ad4db6f735acf6e9f83daa08132`)
- [observation/documented] Blocked pushes can be bypassed via a single environment variable (CLAUDE_CODE_MERGE_QUEUE_EMERGENCY_PUSH=1), which the README notes is a convention, not a guarantee against an adversarial agent. -- evidence: [README.md#L125-L126](https://github.com/funador/claude-code-merge-queue/blob/f77757479cab8031774495c4207647709199a954/README.md#L125-L126), [README.md#L117-L119](https://github.com/funador/claude-code-merge-queue/blob/f77757479cab8031774495c4207647709199a954/README.md#L117-L119), [README.md#L121-L123](https://github.com/funador/claude-code-merge-queue/blob/f77757479cab8031774495c4207647709199a954/README.md#L121-L123) (`clm_edd6b3f90e66cb6c5fa9c17134462523f5cb276206ecf7c83712140f24a87903`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] README badges indicate TypeScript 5.x, Node >=18, MIT license, and zero runtime dependencies; the package is published on npm as claude-code-merge-queue. -- evidence: [README.md#L5-L13](https://github.com/funador/claude-code-merge-queue/blob/f77757479cab8031774495c4207647709199a954/README.md#L5-L13) (`clm_62b445cae0724ccc6faf14d5ae3d3c2e55c19b7814a2d0128a95f2eb25523b2a`)

## limitations (3 claim(s))

- [observation/documented] No human review occurs before landing; checkCommand passing is the only gate, and the tool cannot distinguish a real test suite from a trivially passing command. -- evidence: [README.md#L130-L147](https://github.com/funador/claude-code-merge-queue/blob/f77757479cab8031774495c4207647709199a954/README.md#L130-L147) (`clm_eede019b57cccd75d2bc8473b64439d724ba912b6367947fdb9dd131c21374bf`)
- [observation/documented] The queue is single-machine: the FIFO lock lives in local temp storage, so concurrent landings from two machines only get git's ordinary non-fast-forward rejection. -- evidence: [README.md#L130-L147](https://github.com/funador/claude-code-merge-queue/blob/f77757479cab8031774495c4207647709199a954/README.md#L130-L147) (`clm_6f657d7ee898b7731a68c0198890d613ca0c504c9b7f9dd5dea2be7c5ee40f24`)
- [observation/documented] Locks are crash-safe via PID liveness rather than timeouts, and a slow checkCommand caps throughput since the FIFO lock is held for its entire duration. -- evidence: [README.md#L130-L147](https://github.com/funador/claude-code-merge-queue/blob/f77757479cab8031774495c4207647709199a954/README.md#L130-L147) (`clm_3570e6f71bd9beea564a6a38c32ea12780b5d02d3657cd2e4ad253528b637b26`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

