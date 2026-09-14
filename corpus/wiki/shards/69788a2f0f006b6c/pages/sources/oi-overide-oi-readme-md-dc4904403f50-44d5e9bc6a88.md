---
access: public
aliases: []
claim_ids:
- clm_32d8af85e889ba4c4564e690dc7cf86c385cf2e44fda396e23ddabea443e60c1
- clm_545f4f0e73a83c5743c95c2c82960e10c152c18bc335e98819dc6222cb507b2a
- clm_587b6f5abbdd13896e8e632c2aa0fcdb74ee0afeb0f95efd919a4041bdd9f078
- clm_83abf6fa2c88f84dab847835b8fe2b085873857643ccaba2aceb6f5c52aae768
- clm_86653f1ed09282b8eeb5c6a0cabe77ff8e9bd95be1f87e07b2002e76648e1e60
- clm_8d8f3ad8b839d85fcf56aae9baf20cd797cbbbc8cdb454fe554a0df6fc7f1318
- clm_da2dae9f8bd5e5c0e408a983c76ea2208987c55178141389c64caf78eb185bc2
- clm_dae48075a944e114291f56249ed071876c9bcb21fbc10a8f6256d34cbaa2535a
- clm_de89e95e4705755ee9ee3c6a057f0863c6eb9aa899aa8557dc8225e3ed19e27b
- clm_e72a944b1989230029106dbb170929e6bbadb306ff9b5fdc8e87142002b0163a
maturity: draft
page_id: pg_a013588036505f9681c144d5e9bc6a88
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_6091829f7e815a32ac1bcadc9ba77b6d
title: oi-overide/oi/README.md @ dc4904403f50
updated_at: '2026-09-14T02:25:00Z'
---

# oi-overide/oi/README.md @ dc4904403f50

<!-- rcw:begin owner=source:src_6091829f7e815a32ac1bcadc9ba77b6d block=evidence -->
- Repository development practice: contributors branch from `dev`, merge PRs through `staging` to `main`, and create a changeset (patch/minor/major) before submitting a feature-branch PR. [@claim:clm_32d8af85e889ba4c4564e690dc7cf86c385cf2e44fda396e23ddabea443e60c1]
- Repository development practice: local development uses a hot-reloading watcher (`npm run dev` / `pnpm dev`) that rebuilds on source changes, and `npm run build` plus `npm link` to test the production CLI. [@claim:clm_545f4f0e73a83c5743c95c2c82960e10c152c18bc335e98819dc6222cb507b2a]
- Repository development practice: a GitHub Actions pipeline runs on PRs and pushes to `main` (pnpm install, lint, build, release PRs), and a publish workflow publishes to npm and syncs back to `staging`. [@claim:clm_587b6f5abbdd13896e8e632c2aa0fcdb74ee0afeb0f95efd919a4041bdd9f078]
- The tool is designed to be IDE-agnostic, working with any IDE or text editor rather than integrating with a specific one. [@claim:clm_83abf6fa2c88f84dab847835b8fe2b085873857643ccaba2aceb6f5c52aae768]
- A live file-monitoring component continuously watches project files for code-generation prompts and is started with `overide start`. [@claim:clm_86653f1ed09282b8eeb5c6a0cabe77ff8e9bd95be1f87e07b2002e76648e1e60]
- Code generation uses the OpenAI API; a changelog entry states all other platform support was removed, leaving OpenAI as the sole provider. [@claim:clm_8d8f3ad8b839d85fcf56aae9baf20cd797cbbbc8cdb454fe554a0df6fc7f1318]
- Projects are configured via an `oi-config.json` file holding a project name and an ignore list such as `node_modules` and `*.test.js`. [@claim:clm_da2dae9f8bd5e5c0e408a983c76ea2208987c55178141389c64caf78eb185bc2]
- Features listed under 'Future Plans (v2.0)' — local-parser context management, unified-diff insertion, multi-file edits, and script execution — appear not yet shipped in this version. [@claim:clm_dae48075a944e114291f56249ed071876c9bcb21fbc10a8f6256d34cbaa2535a]
- Users place prompts between `//>` and `<//` markers in source files; generated code is shown with an accept-changes (y/n) prompt. [@claim:clm_de89e95e4705755ee9ee3c6a057f0863c6eb9aa899aa8557dc8225e3ed19e27b]
- The project is licensed under GNU GPL-2.0 and uses changesets for version management and npm publishing. [@claim:clm_e72a944b1989230029106dbb170929e6bbadb306ff9b5fdc8e87142002b0163a]
<!-- rcw:end owner=source:src_6091829f7e815a32ac1bcadc9ba77b6d block=evidence -->

## Researcher notes

