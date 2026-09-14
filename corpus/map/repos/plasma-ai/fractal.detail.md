# plasma-ai/fractal -- full detail

[Back to orientation](fractal.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/plasma-ai/fractal/18793200c0d7e8cdb2db369ea3abe5647a1e15e4/448057f9da1ad062.json](../../../wiki/dossiers/plasma-ai/fractal/18793200c0d7e8cdb2db369ea3abe5647a1e15e4/448057f9da1ad062.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (2 claim(s))

- [observation/documented] Agent loops arrange into a tree of git worktrees: a node iterates toward a goal and spawns child nodes for separable subtasks, so the tree grows to fit the problem rather than following a fixed plan. -- evidence: [README.md#L13-L19](https://github.com/plasma-ai/fractal/blob/18793200c0d7e8cdb2db369ea3abe5647a1e15e4/README.md#L13-L19), [README.md#L101-L105](https://github.com/plasma-ai/fractal/blob/18793200c0d7e8cdb2db369ea3abe5647a1e15e4/README.md#L101-L105) (`clm_ca8d630fc8b0ba34f6e1291385fabc70f4b6bd1706ab8de0fb0a8a679efef197`)
- [observation/documented] Each loop is bounded by hard caps on iterations, depth, children, cost, and time, and an operator can steer or stop it at any point. -- evidence: [README.md#L13-L19](https://github.com/plasma-ai/fractal/blob/18793200c0d7e8cdb2db369ea3abe5647a1e15e4/README.md#L13-L19) (`clm_7353749749fe72459707aca87dcf12fcf1bb6fd4852ceb9398ad26fc5fe2b76f`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: the test suite runs with pytest and --doctest-modules, and integration tests create real git repositories and worktrees, session-scoped to avoid repeated node-init overhead. -- evidence: [AGENTS.md#L72-L74](https://github.com/plasma-ai/fractal/blob/18793200c0d7e8cdb2db369ea3abe5647a1e15e4/AGENTS.md#L72-L74), [README.md#L206-L207](https://github.com/plasma-ai/fractal/blob/18793200c0d7e8cdb2db369ea3abe5647a1e15e4/README.md#L206-L207), [README.md#L202-L204](https://github.com/plasma-ai/fractal/blob/18793200c0d7e8cdb2db369ea3abe5647a1e15e4/README.md#L202-L204) (`clm_636240a2f69e93500e7e4b8ac2d65f1f31b0d95b4afa7fd55c0737bdabf90a55`)
- [observation/documented] Repository development practice: pull requests should branch from and target 'dev' rather than 'main', which advances only at releases; setup uses install.sh or uv sync with pre-commit hooks. -- evidence: [README.md#L176-L178](https://github.com/plasma-ai/fractal/blob/18793200c0d7e8cdb2db369ea3abe5647a1e15e4/README.md#L176-L178), [README.md#L229-L230](https://github.com/plasma-ai/fractal/blob/18793200c0d7e8cdb2db369ea3abe5647a1e15e4/README.md#L229-L230), [README.md#L213-L215](https://github.com/plasma-ai/fractal/blob/18793200c0d7e8cdb2db369ea3abe5647a1e15e4/README.md#L213-L215), [README.md#L184-L186](https://github.com/plasma-ai/fractal/blob/18793200c0d7e8cdb2db369ea3abe5647a1e15e4/README.md#L184-L186) (`clm_67119f3542a0adba768ff8a080c6c85d931708962c7b17ba3befcde6bc9afece`)

## skills-patterns (1 claim(s))

- [observation/documented] The fractal skill can be installed via plugin marketplace for Claude Code and Codex, or via 'fractal install', which copies or symlinks skills into ~/.claude/skills and ~/.agents/skills. -- evidence: [README.md#L84-L86](https://github.com/plasma-ai/fractal/blob/18793200c0d7e8cdb2db369ea3abe5647a1e15e4/README.md#L84-L86), [README.md#L80-L81](https://github.com/plasma-ai/fractal/blob/18793200c0d7e8cdb2db369ea3abe5647a1e15e4/README.md#L80-L81), [README.md#L75-L76](https://github.com/plasma-ai/fractal/blob/18793200c0d7e8cdb2db369ea3abe5647a1e15e4/README.md#L75-L76), [README.md#L92-L94](https://github.com/plasma-ai/fractal/blob/18793200c0d7e8cdb2db369ea3abe5647a1e15e4/README.md#L92-L94), [README.md#L88-L90](https://github.com/plasma-ai/fractal/blob/18793200c0d7e8cdb2db369ea3abe5647a1e15e4/README.md#L88-L90) (`clm_d37ffad7aee44c8cc1ccf58e09bc7ab4d59413fea5ed4948e551f8dee681a5e2`)

## interfaces (3 claim(s))

- [observation/documented] Five agent backends are supported — Claude Code, Codex, Grok Build, OpenCode, and Oh My Pi — selected per node with --agent, with OpenRouter routing available via --provider=openrouter or native model ids. -- evidence: [README.md#L107-L112](https://github.com/plasma-ai/fractal/blob/18793200c0d7e8cdb2db369ea3abe5647a1e15e4/README.md#L107-L112) (`clm_fbda7301173f5d07e230dd79c0f3eec4e0177d2bf7b5d88132926368e900fd47`)
- [observation/documented] The /fractal skill takes a plain-language directive, distills NODE.md instructions and a parameter table, asks for anything it could not infer, and launches the node in a tmux session once approved. -- evidence: [README.md#L114-L116](https://github.com/plasma-ai/fractal/blob/18793200c0d7e8cdb2db369ea3abe5647a1e15e4/README.md#L114-L116), [README.md#L118-L124](https://github.com/plasma-ai/fractal/blob/18793200c0d7e8cdb2db369ea3abe5647a1e15e4/README.md#L118-L124) (`clm_3ec9812806f4f85adeb4fe3c3f68d995c04650e714826ddaaa4ec1107eec2921`)
- [observation/documented] The fractal CLI exposes commands such as 'fractal open' to launch the dashboard from a project root (requires an initialized fractal), with a --light flag for light terminal color schemes. -- evidence: [README.md#L70-L71](https://github.com/plasma-ai/fractal/blob/18793200c0d7e8cdb2db369ea3abe5647a1e15e4/README.md#L70-L71) (`clm_17fd4c65296c6d73ffa4e5be34e760b87a1e82383e0fc43bf5346128bf0e8e0c`)

## memory-state (1 claim(s))

- [observation/documented] All state — runs, iterations, steps, costs, and signals — is tracked in a local SQLite database that can be interacted with live in a terminal UI. -- evidence: [README.md#L13-L19](https://github.com/plasma-ai/fractal/blob/18793200c0d7e8cdb2db369ea3abe5647a1e15e4/README.md#L13-L19), [README.md#L101-L105](https://github.com/plasma-ai/fractal/blob/18793200c0d7e8cdb2db369ea3abe5647a1e15e4/README.md#L101-L105) (`clm_aac1b603c26d0a704e01a646184d33f08e271fdab997e7b1ea52410684c2a583`)

## orchestration (1 claim(s))

- [observation/documented] 'node stop' waits for the in-flight agent to complete rather than tearing the running seat, and cascades over the target's entire subtree children-first; 'node kill' remains the immediate path and can reap booting spawns. -- evidence: [CHANGELOG.md#L420-L423](https://github.com/plasma-ai/fractal/blob/18793200c0d7e8cdb2db369ea3abe5647a1e15e4/CHANGELOG.md#L420-L423), [CHANGELOG.md#L414-L418](https://github.com/plasma-ai/fractal/blob/18793200c0d7e8cdb2db369ea3abe5647a1e15e4/CHANGELOG.md#L414-L418) (`clm_2731eef859ee02b9120860244c4b1c0c7465d362958a6a9d12dc6c8c50b6f958`)

## tools-permissions (1 claim(s))

- [observation/documented] Nodes run their agents without permission prompts by default: seeded configs disable approval gates (e.g. Claude bypassPermissions, Codex danger-full-access), and the per-node worktree isolates only the branch, not the filesystem or network. -- evidence: [README.md#L23-L32](https://github.com/plasma-ai/fractal/blob/18793200c0d7e8cdb2db369ea3abe5647a1e15e4/README.md#L23-L32) (`clm_38064d19540729b12ea6de440cab3b14ab349a21c6cab3023d586669bb17a657`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The package installs from PyPI as plasma-fractal (or via the fractal pointer dist); pipx/uv tool installs additionally require installing plasma-wiki, which a plain pip install pulls automatically. -- evidence: [README.md#L57-L59](https://github.com/plasma-ai/fractal/blob/18793200c0d7e8cdb2db369ea3abe5647a1e15e4/README.md#L57-L59), [CHANGELOG.md#L484-L485](https://github.com/plasma-ai/fractal/blob/18793200c0d7e8cdb2db369ea3abe5647a1e15e4/CHANGELOG.md#L484-L485), [README.md#L61-L65](https://github.com/plasma-ai/fractal/blob/18793200c0d7e8cdb2db369ea3abe5647a1e15e4/README.md#L61-L65), [README.md#L51-L53](https://github.com/plasma-ai/fractal/blob/18793200c0d7e8cdb2db369ea3abe5647a1e15e4/README.md#L51-L53) (`clm_05af5b814a1cbf5c2e845cc41e492577d47cae6367f9d8b4ff8c798e534f746a`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

