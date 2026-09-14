---
access: public
aliases: []
claim_ids:
- clm_05af5b814a1cbf5c2e845cc41e492577d47cae6367f9d8b4ff8c798e534f746a
- clm_17fd4c65296c6d73ffa4e5be34e760b87a1e82383e0fc43bf5346128bf0e8e0c
- clm_38064d19540729b12ea6de440cab3b14ab349a21c6cab3023d586669bb17a657
- clm_3ec9812806f4f85adeb4fe3c3f68d995c04650e714826ddaaa4ec1107eec2921
- clm_636240a2f69e93500e7e4b8ac2d65f1f31b0d95b4afa7fd55c0737bdabf90a55
- clm_67119f3542a0adba768ff8a080c6c85d931708962c7b17ba3befcde6bc9afece
- clm_7353749749fe72459707aca87dcf12fcf1bb6fd4852ceb9398ad26fc5fe2b76f
- clm_aac1b603c26d0a704e01a646184d33f08e271fdab997e7b1ea52410684c2a583
- clm_ca8d630fc8b0ba34f6e1291385fabc70f4b6bd1706ab8de0fb0a8a679efef197
- clm_d37ffad7aee44c8cc1ccf58e09bc7ab4d59413fea5ed4948e551f8dee681a5e2
- clm_fbda7301173f5d07e230dd79c0f3eec4e0177d2bf7b5d88132926368e900fd47
maturity: draft
page_id: pg_49313d24b9c85bb3ae4244be68816e70
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_aa3a00d6d7ab5ff7b5801bbcc485ea9b
title: plasma-ai/fractal/README.md @ 18793200c0d7
updated_at: '2026-09-14T02:31:11Z'
---

# plasma-ai/fractal/README.md @ 18793200c0d7

<!-- rcw:begin owner=source:src_aa3a00d6d7ab5ff7b5801bbcc485ea9b block=evidence -->
- The package installs from PyPI as plasma-fractal (or via the fractal pointer dist); pipx/uv tool installs additionally require installing plasma-wiki, which a plain pip install pulls automatically. [@claim:clm_05af5b814a1cbf5c2e845cc41e492577d47cae6367f9d8b4ff8c798e534f746a]
- The fractal CLI exposes commands such as 'fractal open' to launch the dashboard from a project root (requires an initialized fractal), with a --light flag for light terminal color schemes. [@claim:clm_17fd4c65296c6d73ffa4e5be34e760b87a1e82383e0fc43bf5346128bf0e8e0c]
- Nodes run their agents without permission prompts by default: seeded configs disable approval gates (e.g. Claude bypassPermissions, Codex danger-full-access), and the per-node worktree isolates only the branch, not the filesystem or network. [@claim:clm_38064d19540729b12ea6de440cab3b14ab349a21c6cab3023d586669bb17a657]
- The /fractal skill takes a plain-language directive, distills NODE.md instructions and a parameter table, asks for anything it could not infer, and launches the node in a tmux session once approved. [@claim:clm_3ec9812806f4f85adeb4fe3c3f68d995c04650e714826ddaaa4ec1107eec2921]
- Repository development practice: the test suite runs with pytest and --doctest-modules, and integration tests create real git repositories and worktrees, session-scoped to avoid repeated node-init overhead. [@claim:clm_636240a2f69e93500e7e4b8ac2d65f1f31b0d95b4afa7fd55c0737bdabf90a55]
- Repository development practice: pull requests should branch from and target 'dev' rather than 'main', which advances only at releases; setup uses install.sh or uv sync with pre-commit hooks. [@claim:clm_67119f3542a0adba768ff8a080c6c85d931708962c7b17ba3befcde6bc9afece]
- Each loop is bounded by hard caps on iterations, depth, children, cost, and time, and an operator can steer or stop it at any point. [@claim:clm_7353749749fe72459707aca87dcf12fcf1bb6fd4852ceb9398ad26fc5fe2b76f]
- All state — runs, iterations, steps, costs, and signals — is tracked in a local SQLite database that can be interacted with live in a terminal UI. [@claim:clm_aac1b603c26d0a704e01a646184d33f08e271fdab997e7b1ea52410684c2a583]
- Agent loops arrange into a tree of git worktrees: a node iterates toward a goal and spawns child nodes for separable subtasks, so the tree grows to fit the problem rather than following a fixed plan. [@claim:clm_ca8d630fc8b0ba34f6e1291385fabc70f4b6bd1706ab8de0fb0a8a679efef197]
- The fractal skill can be installed via plugin marketplace for Claude Code and Codex, or via 'fractal install', which copies or symlinks skills into ~/.claude/skills and ~/.agents/skills. [@claim:clm_d37ffad7aee44c8cc1ccf58e09bc7ab4d59413fea5ed4948e551f8dee681a5e2]
- Five agent backends are supported — Claude Code, Codex, Grok Build, OpenCode, and Oh My Pi — selected per node with --agent, with OpenRouter routing available via --provider=openrouter or native model ids. [@claim:clm_fbda7301173f5d07e230dd79c0f3eec4e0177d2bf7b5d88132926368e900fd47]
<!-- rcw:end owner=source:src_aa3a00d6d7ab5ff7b5801bbcc485ea9b block=evidence -->

## Researcher notes

