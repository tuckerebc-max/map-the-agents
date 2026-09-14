# paoloanzn/microcodex

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 2d88e4f57552 @ 35b0dd63d72e3d03

## Summary (orientation draft, not independently verified)

MicroCodex is a C++23 terminal coding agent with one-shot prompts, an interactive UI, local tools, durable conversations, and context compaction; evidence covers its CLI, login flow, skills discovery, shell denylist, install options, and documented limitations. Contributor guidance in CONTRIBUTING.md is repository development practice only.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] MicroCodex is described as an ultra-lightweight coding agent that runs locally in the terminal and is written in C++23. -- evidence: [README.md#L1-L7](https://github.com/paoloanzn/microcodex/blob/2d88e4f57552a91a98c9018ae76101148f5002c7/README.md#L1-L7)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows (4 claim(s)):
  - [observation/documented] Installation is via a curl-piped install script (with `MICROCODEX_RELEASE` selecting a specific release) or by downloading a platform archive from GitHub Releases. -- evidence: [README.md#L43-L45](https://github.com/paoloanzn/microcodex/blob/2d88e4f57552a91a98c9018ae76101148f5002c7/README.md#L43-L45), [README.md#L23-L24](https://github.com/paoloanzn/microcodex/blob/2d88e4f57552a91a98c9018ae76101148f5002c7/README.md#L23-L24), [README.md#L17-L19](https://github.com/paoloanzn/microcodex/blob/2d88e4f57552a91a98c9018ae76101148f5002c7/README.md#L17-L19), [README.md#L41-L41](https://github.com/paoloanzn/microcodex/blob/2d88e4f57552a91a98c9018ae76101148f5002c7/README.md#L41-L41)
  - [observation/documented] Repository development practice: contributors build with a C++23 compiler, make, libcurl and OpenSSL dev files, run `make` and `make test`, and should keep PRs to one logical change with tests passing and no warnings. -- evidence: [CONTRIBUTING.md#L31-L35](https://github.com/paoloanzn/microcodex/blob/2d88e4f57552a91a98c9018ae76101148f5002c7/CONTRIBUTING.md#L31-L35), [CONTRIBUTING.md#L37-L40](https://github.com/paoloanzn/microcodex/blob/2d88e4f57552a91a98c9018ae76101148f5002c7/CONTRIBUTING.md#L37-L40), [CONTRIBUTING.md#L46-L51](https://github.com/paoloanzn/microcodex/blob/2d88e4f57552a91a98c9018ae76101148f5002c7/CONTRIBUTING.md#L46-L51), [CONTRIBUTING.md#L19-L19](https://github.com/paoloanzn/microcodex/blob/2d88e4f57552a91a98c9018ae76101148f5002c7/CONTRIBUTING.md#L19-L19)
- skills-patterns (1 claim(s)):
  - [observation/documented] Skills are discovered under `$CODEX_HOME/skills` (default `~/.codex/skills`); each needs a `SKILL.md` with YAML frontmatter name and description, and the full skill is read only when its metadata matches the task. -- evidence: [README.md#L68-L73](https://github.com/paoloanzn/microcodex/blob/2d88e4f57552a91a98c9018ae76101148f5002c7/README.md#L68-L73)
- interfaces (2 claim(s)):
  - [observation/documented] The product provides one-shot prompts, an interactive terminal UI, local coding tools, durable conversations, and automatic context compaction. -- evidence: [README.md#L1-L7](https://github.com/paoloanzn/microcodex/blob/2d88e4f57552a91a98c9018ae76101148f5002c7/README.md#L1-L7)
  - [observation/documented] Users sign in with `microcodex login` (a `--device-auth` option exists for remote or headless machines) and can run interactively or pass a one-shot prompt as an argument. -- evidence: [README.md#L49-L49](https://github.com/paoloanzn/microcodex/blob/2d88e4f57552a91a98c9018ae76101148f5002c7/README.md#L49-L49), [README.md#L53-L56](https://github.com/paoloanzn/microcodex/blob/2d88e4f57552a91a98c9018ae76101148f5002c7/README.md#L53-L56)
- memory-state (1 claim(s)):
  - [observation/documented] OAuth credentials from login are stored under `$CODEX_HOME`, or `~/.codex` when that variable is unset. -- evidence: [README.md#L49-L49](https://github.com/paoloanzn/microcodex/blob/2d88e4f57552a91a98c9018ae76101148f5002c7/README.md#L49-L49)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
  - [observation/documented] The agent is not a sandbox: before running the user's shell it applies a lexical denylist (e.g. `rm -rf`, `git reset --hard`, shutdown commands); other commands and file operations run with the process's own permissions. -- evidence: [README.md#L58-L64](https://github.com/paoloanzn/microcodex/blob/2d88e4f57552a91a98c9018ae76101148f5002c7/README.md#L58-L64)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] Linux requires the libcurl and OpenSSL runtime libraries, and prebuilt binaries are published for macOS and Linux on arm64 and x86_64. -- evidence: [README.md#L39-L39](https://github.com/paoloanzn/microcodex/blob/2d88e4f57552a91a98c9018ae76101148f5002c7/README.md#L39-L39), [README.md#L28-L33](https://github.com/paoloanzn/microcodex/blob/2d88e4f57552a91a98c9018ae76101148f5002c7/README.md#L28-L33)
- limitations (1 claim(s)):
More evidence: [full detail](microcodex.detail.md)

Metadata and full claim list: [full detail](microcodex.detail.md)
Human notes ([notes](microcodex.notes.md), never overwritten by build)

[Back to map index](../../index.md)
