# paoloanzn/microcodex -- full detail

[Back to orientation](microcodex.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/paoloanzn/microcodex/2d88e4f57552a91a98c9018ae76101148f5002c7/35b0dd63d72e3d03.json](../../../wiki/dossiers/paoloanzn/microcodex/2d88e4f57552a91a98c9018ae76101148f5002c7/35b0dd63d72e3d03.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] MicroCodex is described as an ultra-lightweight coding agent that runs locally in the terminal and is written in C++23. -- evidence: [README.md#L1-L7](https://github.com/paoloanzn/microcodex/blob/2d88e4f57552a91a98c9018ae76101148f5002c7/README.md#L1-L7) (`clm_d783119fdc45814c405ba90a1796dc801ee3dcc358ade78e035eff3bafdf1d24`)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (4 claim(s))

- [observation/documented] Installation is via a curl-piped install script (with `MICROCODEX_RELEASE` selecting a specific release) or by downloading a platform archive from GitHub Releases. -- evidence: [README.md#L43-L45](https://github.com/paoloanzn/microcodex/blob/2d88e4f57552a91a98c9018ae76101148f5002c7/README.md#L43-L45), [README.md#L23-L24](https://github.com/paoloanzn/microcodex/blob/2d88e4f57552a91a98c9018ae76101148f5002c7/README.md#L23-L24), [README.md#L17-L19](https://github.com/paoloanzn/microcodex/blob/2d88e4f57552a91a98c9018ae76101148f5002c7/README.md#L17-L19), [README.md#L41-L41](https://github.com/paoloanzn/microcodex/blob/2d88e4f57552a91a98c9018ae76101148f5002c7/README.md#L41-L41) (`clm_6d2a08efa679accbe146a3243a301e0f555d07b72559ea8478ee75038ac8f9c4`)
- [observation/documented] Repository development practice: contributors build with a C++23 compiler, make, libcurl and OpenSSL dev files, run `make` and `make test`, and should keep PRs to one logical change with tests passing and no warnings. -- evidence: [CONTRIBUTING.md#L31-L35](https://github.com/paoloanzn/microcodex/blob/2d88e4f57552a91a98c9018ae76101148f5002c7/CONTRIBUTING.md#L31-L35), [CONTRIBUTING.md#L37-L40](https://github.com/paoloanzn/microcodex/blob/2d88e4f57552a91a98c9018ae76101148f5002c7/CONTRIBUTING.md#L37-L40), [CONTRIBUTING.md#L46-L51](https://github.com/paoloanzn/microcodex/blob/2d88e4f57552a91a98c9018ae76101148f5002c7/CONTRIBUTING.md#L46-L51), [CONTRIBUTING.md#L19-L19](https://github.com/paoloanzn/microcodex/blob/2d88e4f57552a91a98c9018ae76101148f5002c7/CONTRIBUTING.md#L19-L19) (`clm_ff6c8461d7d81a1b31595b9e17a5becf3b39f2fad5b3e9b6c31e118ed52ed07f`)
- [observation/documented] Repository development practice: bug reports should include reproduction steps, expected vs actual behavior, OS and compiler version, and must never contain credentials or tokens. -- evidence: [CONTRIBUTING.md#L15-L15](https://github.com/paoloanzn/microcodex/blob/2d88e4f57552a91a98c9018ae76101148f5002c7/CONTRIBUTING.md#L15-L15), [CONTRIBUTING.md#L7-L7](https://github.com/paoloanzn/microcodex/blob/2d88e4f57552a91a98c9018ae76101148f5002c7/CONTRIBUTING.md#L7-L7), [CONTRIBUTING.md#L9-L13](https://github.com/paoloanzn/microcodex/blob/2d88e4f57552a91a98c9018ae76101148f5002c7/CONTRIBUTING.md#L9-L13) (`clm_288afd6b7ce5fe7b1dfe9a23b95d8bf084c8ba7f81500cc47b44489156f3157b`)
- [observation/documented] Repository development practice: contributors are warned not to submit unreviewed AI-generated PR descriptions or diffs and remain responsible for validating their submissions. -- evidence: [CONTRIBUTING.md#L53-L54](https://github.com/paoloanzn/microcodex/blob/2d88e4f57552a91a98c9018ae76101148f5002c7/CONTRIBUTING.md#L53-L54) (`clm_ebad30167bd4811b9cc00f034200442687eccdefa277ca2ee6010644fa70b90d`)

## skills-patterns (1 claim(s))

- [observation/documented] Skills are discovered under `$CODEX_HOME/skills` (default `~/.codex/skills`); each needs a `SKILL.md` with YAML frontmatter name and description, and the full skill is read only when its metadata matches the task. -- evidence: [README.md#L68-L73](https://github.com/paoloanzn/microcodex/blob/2d88e4f57552a91a98c9018ae76101148f5002c7/README.md#L68-L73) (`clm_a80d3c7460f983b1f820ed26f27f962f064c2f8c11f4218fc7c8687b5ed4a81c`)

## interfaces (2 claim(s))

- [observation/documented] The product provides one-shot prompts, an interactive terminal UI, local coding tools, durable conversations, and automatic context compaction. -- evidence: [README.md#L1-L7](https://github.com/paoloanzn/microcodex/blob/2d88e4f57552a91a98c9018ae76101148f5002c7/README.md#L1-L7) (`clm_476350f166687f7b70dff4932bf3d832b541dcf75ce08797e7620e1c21d693b1`)
- [observation/documented] Users sign in with `microcodex login` (a `--device-auth` option exists for remote or headless machines) and can run interactively or pass a one-shot prompt as an argument. -- evidence: [README.md#L49-L49](https://github.com/paoloanzn/microcodex/blob/2d88e4f57552a91a98c9018ae76101148f5002c7/README.md#L49-L49), [README.md#L53-L56](https://github.com/paoloanzn/microcodex/blob/2d88e4f57552a91a98c9018ae76101148f5002c7/README.md#L53-L56) (`clm_55199b7ae7bf7b3dc8ef0f368410b4187016dc07503fcc734137ea9c8df8bf7b`)

## memory-state (1 claim(s))

- [observation/documented] OAuth credentials from login are stored under `$CODEX_HOME`, or `~/.codex` when that variable is unset. -- evidence: [README.md#L49-L49](https://github.com/paoloanzn/microcodex/blob/2d88e4f57552a91a98c9018ae76101148f5002c7/README.md#L49-L49) (`clm_814b5eff35a095df5a6df22fcac21d114de019fe310cabc542827004c887126b`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] The agent is not a sandbox: before running the user's shell it applies a lexical denylist (e.g. `rm -rf`, `git reset --hard`, shutdown commands); other commands and file operations run with the process's own permissions. -- evidence: [README.md#L58-L64](https://github.com/paoloanzn/microcodex/blob/2d88e4f57552a91a98c9018ae76101148f5002c7/README.md#L58-L64) (`clm_2c5a4bb56f1348950c2f8fe10bc20b679ce23821e6f65b0d82ef20c4fddcedcc`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Linux requires the libcurl and OpenSSL runtime libraries, and prebuilt binaries are published for macOS and Linux on arm64 and x86_64. -- evidence: [README.md#L39-L39](https://github.com/paoloanzn/microcodex/blob/2d88e4f57552a91a98c9018ae76101148f5002c7/README.md#L39-L39), [README.md#L28-L33](https://github.com/paoloanzn/microcodex/blob/2d88e4f57552a91a98c9018ae76101148f5002c7/README.md#L28-L33) (`clm_d639afff502118d2d83cba42a52c2925f46745400f888d15e7de03211be245a1`)

## limitations (1 claim(s))

- [observation/documented] Documented known issues include unimplemented MCP support, inability to copy text from the terminal during use, and a bash safety gate that may miss indirect or unrecognized destructive commands. -- evidence: [README.md#L89-L92](https://github.com/paoloanzn/microcodex/blob/2d88e4f57552a91a98c9018ae76101148f5002c7/README.md#L89-L92) (`clm_f6c9da148f3d567b09251d5165f15d2c3809c54f9073e0e310a869a28ccc225e`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

