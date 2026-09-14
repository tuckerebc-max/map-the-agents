# oi-overide/oi -- full detail

[Back to orientation](oi.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/oi-overide/oi/dc4904403f5013e31d436b03a5ea5f6d31201ef8/e9bfe679c94f5f47.json](../../../wiki/dossiers/oi-overide/oi/dc4904403f5013e31d436b03a5ea5f6d31201ef8/e9bfe679c94f5f47.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] A live file-monitoring component continuously watches project files for code-generation prompts and is started with `overide start`. -- evidence: [README.md#L25-L28](https://github.com/oi-overide/oi/blob/dc4904403f5013e31d436b03a5ea5f6d31201ef8/README.md#L25-L28), [README.md#L64-L66](https://github.com/oi-overide/oi/blob/dc4904403f5013e31d436b03a5ea5f6d31201ef8/README.md#L64-L66) (`clm_86653f1ed09282b8eeb5c6a0cabe77ff8e9bd95be1f87e07b2002e76648e1e60`)

## design-choices (1 claim(s))

- [observation/documented] The tool is designed to be IDE-agnostic, working with any IDE or text editor rather than integrating with a specific one. -- evidence: [README.md#L25-L28](https://github.com/oi-overide/oi/blob/dc4904403f5013e31d436b03a5ea5f6d31201ef8/README.md#L25-L28) (`clm_83abf6fa2c88f84dab847835b8fe2b085873857643ccaba2aceb6f5c52aae768`)

## workflows (3 claim(s))

- [observation/documented] Repository development practice: contributors branch from `dev`, merge PRs through `staging` to `main`, and create a changeset (patch/minor/major) before submitting a feature-branch PR. -- evidence: [README.md#L101-L107](https://github.com/oi-overide/oi/blob/dc4904403f5013e31d436b03a5ea5f6d31201ef8/README.md#L101-L107), [README.md#L117-L117](https://github.com/oi-overide/oi/blob/dc4904403f5013e31d436b03a5ea5f6d31201ef8/README.md#L117-L117), [README.md#L127-L129](https://github.com/oi-overide/oi/blob/dc4904403f5013e31d436b03a5ea5f6d31201ef8/README.md#L127-L129) (`clm_32d8af85e889ba4c4564e690dc7cf86c385cf2e44fda396e23ddabea443e60c1`)
- [observation/documented] Repository development practice: a GitHub Actions pipeline runs on PRs and pushes to `main` (pnpm install, lint, build, release PRs), and a publish workflow publishes to npm and syncs back to `staging`. -- evidence: [README.md#L214-L214](https://github.com/oi-overide/oi/blob/dc4904403f5013e31d436b03a5ea5f6d31201ef8/README.md#L214-L214), [README.md#L231-L233](https://github.com/oi-overide/oi/blob/dc4904403f5013e31d436b03a5ea5f6d31201ef8/README.md#L231-L233), [README.md#L218-L222](https://github.com/oi-overide/oi/blob/dc4904403f5013e31d436b03a5ea5f6d31201ef8/README.md#L218-L222) (`clm_587b6f5abbdd13896e8e632c2aa0fcdb74ee0afeb0f95efd919a4041bdd9f078`)
- [observation/documented] Repository development practice: local development uses a hot-reloading watcher (`npm run dev` / `pnpm dev`) that rebuilds on source changes, and `npm run build` plus `npm link` to test the production CLI. -- evidence: [README.md#L176-L178](https://github.com/oi-overide/oi/blob/dc4904403f5013e31d436b03a5ea5f6d31201ef8/README.md#L176-L178), [README.md#L149-L150](https://github.com/oi-overide/oi/blob/dc4904403f5013e31d436b03a5ea5f6d31201ef8/README.md#L149-L150), [README.md#L169-L172](https://github.com/oi-overide/oi/blob/dc4904403f5013e31d436b03a5ea5f6d31201ef8/README.md#L169-L172), [README.md#L163-L163](https://github.com/oi-overide/oi/blob/dc4904403f5013e31d436b03a5ea5f6d31201ef8/README.md#L163-L163) (`clm_545f4f0e73a83c5743c95c2c82960e10c152c18bc335e98819dc6222cb507b2a`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] Users place prompts between `//>` and `<//` markers in source files; generated code is shown with an accept-changes (y/n) prompt. -- evidence: [README.md#L72-L74](https://github.com/oi-overide/oi/blob/dc4904403f5013e31d436b03a5ea5f6d31201ef8/README.md#L72-L74), [README.md#L78-L84](https://github.com/oi-overide/oi/blob/dc4904403f5013e31d436b03a5ea5f6d31201ef8/README.md#L78-L84) (`clm_de89e95e4705755ee9ee3c6a057f0863c6eb9aa899aa8557dc8225e3ed19e27b`)
- [observation/documented] Projects are configured via an `oi-config.json` file holding a project name and an ignore list such as `node_modules` and `*.test.js`. -- evidence: [README.md#L90-L95](https://github.com/oi-overide/oi/blob/dc4904403f5013e31d436b03a5ea5f6d31201ef8/README.md#L90-L95), [README.md#L88-L88](https://github.com/oi-overide/oi/blob/dc4904403f5013e31d436b03a5ea5f6d31201ef8/README.md#L88-L88) (`clm_da2dae9f8bd5e5c0e408a983c76ea2208987c55178141389c64caf78eb185bc2`)
- [observation/documented] The `init` and `start` commands support a `--path` option so Overide can be initialized and started in any target directory. -- evidence: [CHANGELOG.md#L16-L16](https://github.com/oi-overide/oi/blob/dc4904403f5013e31d436b03a5ea5f6d31201ef8/CHANGELOG.md#L16-L16) (`clm_bc10933c106f7960c562102b0eb0335cfcf449db7e1e65944e636791370bcf3a`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] Code generation uses the OpenAI API; a changelog entry states all other platform support was removed, leaving OpenAI as the sole provider. -- evidence: [README.md#L25-L28](https://github.com/oi-overide/oi/blob/dc4904403f5013e31d436b03a5ea5f6d31201ef8/README.md#L25-L28), [CHANGELOG.md#L7-L7](https://github.com/oi-overide/oi/blob/dc4904403f5013e31d436b03a5ea5f6d31201ef8/CHANGELOG.md#L7-L7) (`clm_8d8f3ad8b839d85fcf56aae9baf20cd797cbbbc8cdb454fe554a0df6fc7f1318`)
- [observation/documented] The project is licensed under GNU GPL-2.0 and uses changesets for version management and npm publishing. -- evidence: [README.md#L133-L135](https://github.com/oi-overide/oi/blob/dc4904403f5013e31d436b03a5ea5f6d31201ef8/README.md#L133-L135), [README.md#L115-L115](https://github.com/oi-overide/oi/blob/dc4904403f5013e31d436b03a5ea5f6d31201ef8/README.md#L115-L115), [README.md#L248-L248](https://github.com/oi-overide/oi/blob/dc4904403f5013e31d436b03a5ea5f6d31201ef8/README.md#L248-L248) (`clm_e72a944b1989230029106dbb170929e6bbadb306ff9b5fdc8e87142002b0163a`)

## limitations (1 claim(s))

- [inference/documented] Features listed under 'Future Plans (v2.0)' — local-parser context management, unified-diff insertion, multi-file edits, and script execution — appear not yet shipped in this version. -- evidence: [README.md#L237-L240](https://github.com/oi-overide/oi/blob/dc4904403f5013e31d436b03a5ea5f6d31201ef8/README.md#L237-L240) (`clm_dae48075a944e114291f56249ed071876c9bcb21fbc10a8f6256d34cbaa2535a`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

