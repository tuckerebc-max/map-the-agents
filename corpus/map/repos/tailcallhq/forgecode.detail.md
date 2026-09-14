# tailcallhq/forgecode -- full detail

[Back to orientation](forgecode.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/tailcallhq/forgecode/6ed5d37b6b45a2b6220877fd9aec5ba4c4b7f3c0/495877cd934128c0.json](../../../wiki/dossiers/tailcallhq/forgecode/6ed5d37b6b45a2b6220877fd9aec5ba4c4b7f3c0/495877cd934128c0.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] Forge ships three built-in agents: `forge` (implementation, modifies files), `sage` (read-only research), and `muse` (planning, writes plans to `plans/`). -- evidence: [README.md#L245-L249](https://github.com/tailcallhq/forgecode/blob/6ed5d37b6b45a2b6220877fd9aec5ba4c4b7f3c0/README.md#L245-L249), [README.md#L243-L243](https://github.com/tailcallhq/forgecode/blob/6ed5d37b6b45a2b6220877fd9aec5ba4c4b7f3c0/README.md#L243-L243) (`clm_63c6684620c3edef5abc70c6d274ba1986b5399718bce932487eb6db38171d88`)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: the README badges indicate a CI workflow (ci.yml), GitHub releases, a Discord community, and CLA assistant for contributions. -- evidence: [README.md#L6-L9](https://github.com/tailcallhq/forgecode/blob/6ed5d37b6b45a2b6220877fd9aec5ba4c4b7f3c0/README.md#L6-L9) (`clm_f51e814cd487576af7026d87efe3a88626c600c4f1e7c25d2b9731539f82e14a`)

## skills-patterns (2 claim(s))

- [observation/documented] Three built-in skills ship with Forge: create-skill, execute-plan, and github-pr-description; skills are reusable workflows the AI can invoke as tools. -- evidence: [README.md#L338-L340](https://github.com/tailcallhq/forgecode/blob/6ed5d37b6b45a2b6220877fd9aec5ba4c4b7f3c0/README.md#L338-L340), [README.md#L336-L336](https://github.com/tailcallhq/forgecode/blob/6ed5d37b6b45a2b6220877fd9aec5ba4c4b7f3c0/README.md#L336-L336) (`clm_e459e4540b6c1b7673d9cd35c10a7007344344a46d64b9128540fb56b4cde3cd`)
- [observation/documented] Custom skills are SKILL.md files with YAML front-matter, resolved with precedence: project-local `.forge/skills/` over global `~/forge/skills/` over built-in skills embedded in the binary. -- evidence: [README.md#L346-L350](https://github.com/tailcallhq/forgecode/blob/6ed5d37b6b45a2b6220877fd9aec5ba4c4b7f3c0/README.md#L346-L350), [README.md#L352-L352](https://github.com/tailcallhq/forgecode/blob/6ed5d37b6b45a2b6220877fd9aec5ba4c4b7f3c0/README.md#L352-L352), [README.md#L344-L344](https://github.com/tailcallhq/forgecode/blob/6ed5d37b6b45a2b6220877fd9aec5ba4c4b7f3c0/README.md#L344-L344) (`clm_84ce517c7889f3d9cf0a500e21f71aecd229b6006c6fd5343e52e5447bc02871`)

## interfaces (3 claim(s))

- [observation/documented] Forge offers three usage modes: an interactive terminal UI launched by running `forge` with no arguments, a one-shot CLI mode via `-p`/`--prompt`, and a ZSH plugin mode using `:` prefix commands. -- evidence: [README.md#L216-L216](https://github.com/tailcallhq/forgecode/blob/6ed5d37b6b45a2b6220877fd9aec5ba4c4b7f3c0/README.md#L216-L216), [README.md#L201-L201](https://github.com/tailcallhq/forgecode/blob/6ed5d37b6b45a2b6220877fd9aec5ba4c4b7f3c0/README.md#L201-L201), [README.md#L182-L182](https://github.com/tailcallhq/forgecode/blob/6ed5d37b6b45a2b6220877fd9aec5ba4c4b7f3c0/README.md#L182-L182), [README.md#L186-L186](https://github.com/tailcallhq/forgecode/blob/6ed5d37b6b45a2b6220877fd9aec5ba4c4b7f3c0/README.md#L186-L186) (`clm_f0140789189621e9dab2dfccadbf5d4a1209ebe1553fe60507177cab63b2c6ac`)
- [observation/documented] CLI options include `-p` for direct prompts, `--agent` to pick an agent, `-C` to change directory, `--sandbox` to create an isolated git worktree plus branch, and `--conversation-id` to resume a conversation. -- evidence: [README.md#L415-L426](https://github.com/tailcallhq/forgecode/blob/6ed5d37b6b45a2b6220877fd9aec5ba4c4b7f3c0/README.md#L415-L426) (`clm_afeb94b0df1aaac24101f533caf2bc09e5af06555cf2eb163958e01a2edd0beb`)
- [observation/documented] Semantic search indexes the codebase via `:sync`/`forge workspace sync`, sending file content to a workspace server defaulting to https://api.forgecode.dev, overridable with FORGE_WORKSPACE_SERVER_URL. -- evidence: [README.md#L364-L369](https://github.com/tailcallhq/forgecode/blob/6ed5d37b6b45a2b6220877fd9aec5ba4c4b7f3c0/README.md#L364-L369), [README.md#L463-L466](https://github.com/tailcallhq/forgecode/blob/6ed5d37b6b45a2b6220877fd9aec5ba4c4b7f3c0/README.md#L463-L466), [README.md#L371-L371](https://github.com/tailcallhq/forgecode/blob/6ed5d37b6b45a2b6220877fd9aec5ba4c4b7f3c0/README.md#L371-L371) (`clm_20b964b3e76d851fb1fcfd85f488979d80bbc95875c5100470954859e7f0b5c4`)

## memory-state (2 claim(s))

- [observation/documented] Forge saves every conversation and provides commands to list, resume, clone, rename, delete, dump as JSON/HTML, compact, and retry conversations, including toggling to the previous one. -- evidence: [README.md#L432-L443](https://github.com/tailcallhq/forgecode/blob/6ed5d37b6b45a2b6220877fd9aec5ba4c4b7f3c0/README.md#L432-L443), [README.md#L273-L273](https://github.com/tailcallhq/forgecode/blob/6ed5d37b6b45a2b6220877fd9aec5ba4c4b7f3c0/README.md#L273-L273), [README.md#L275-L290](https://github.com/tailcallhq/forgecode/blob/6ed5d37b6b45a2b6220877fd9aec5ba4c4b7f3c0/README.md#L275-L290) (`clm_c074c1b4f134270e88d652bcfae3a779a97701e4cb973ec36939ba7c6f604e9a`)
- [observation/documented] An AGENTS.md file in the project root or `~/forge/AGENTS.md` gives agents persistent instructions, and Forge reads it automatically at the start of every conversation. -- evidence: [README.md#L356-L356](https://github.com/tailcallhq/forgecode/blob/6ed5d37b6b45a2b6220877fd9aec5ba4c4b7f3c0/README.md#L356-L356) (`clm_760767ae7361238213423d8c9fd3c539ed9b1a52e4fc3a22044246be1411e5ac`)

## orchestration (1 claim(s))

- [observation/documented] Forge supports MCP servers with subcommands to list, import, show, remove, and reload configured servers. -- evidence: [README.md#L469-L473](https://github.com/tailcallhq/forgecode/blob/6ed5d37b6b45a2b6220877fd9aec5ba4c4b7f3c0/README.md#L469-L473) (`clm_fc0973587d6198a66c2aeda157be7951f1ee1152bc0e23260669bccfc289624d`)

## tools-permissions (1 claim(s))

- [observation/documented] The README describes a restricted shell mode that limits file system access and prevents unintended changes as part of Forge's security design. -- evidence: [README.md#L170-L174](https://github.com/tailcallhq/forgecode/blob/6ed5d37b6b45a2b6220877fd9aec5ba4c4b7f3c0/README.md#L170-L174) (`clm_3861d5a22a6c88efa87845a0c544d50f002718a8d5ae5a3efc908de55bb17ec4`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Using `.env` files for provider configuration is deprecated and slated for removal; environment-variable credentials are still supported for backward compatibility and are auto-migrated to file-based storage on first run. -- evidence: [README.md#L515-L515](https://github.com/tailcallhq/forgecode/blob/6ed5d37b6b45a2b6220877fd9aec5ba4c4b7f3c0/README.md#L515-L515), [README.md#L513-L513](https://github.com/tailcallhq/forgecode/blob/6ed5d37b6b45a2b6220877fd9aec5ba4c4b7f3c0/README.md#L513-L513) (`clm_b80e64f38b5b5ecf24bc6dba76d973d572993c34900d0492430db8fd6338bc78`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

