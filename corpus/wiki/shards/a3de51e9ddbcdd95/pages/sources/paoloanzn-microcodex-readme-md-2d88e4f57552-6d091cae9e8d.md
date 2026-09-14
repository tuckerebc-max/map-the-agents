---
access: public
aliases: []
claim_ids:
- clm_2c5a4bb56f1348950c2f8fe10bc20b679ce23821e6f65b0d82ef20c4fddcedcc
- clm_476350f166687f7b70dff4932bf3d832b541dcf75ce08797e7620e1c21d693b1
- clm_55199b7ae7bf7b3dc8ef0f368410b4187016dc07503fcc734137ea9c8df8bf7b
- clm_6d2a08efa679accbe146a3243a301e0f555d07b72559ea8478ee75038ac8f9c4
- clm_814b5eff35a095df5a6df22fcac21d114de019fe310cabc542827004c887126b
- clm_a80d3c7460f983b1f820ed26f27f962f064c2f8c11f4218fc7c8687b5ed4a81c
- clm_d639afff502118d2d83cba42a52c2925f46745400f888d15e7de03211be245a1
- clm_d783119fdc45814c405ba90a1796dc801ee3dcc358ade78e035eff3bafdf1d24
- clm_f6c9da148f3d567b09251d5165f15d2c3809c54f9073e0e310a869a28ccc225e
maturity: draft
page_id: pg_2a4c29b97ee15d94af3b6d091cae9e8d
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_49444f9139f952da91f5c98fc1682d84
title: paoloanzn/microcodex/README.md @ 2d88e4f57552
updated_at: '2026-09-14T02:28:51Z'
---

# paoloanzn/microcodex/README.md @ 2d88e4f57552

<!-- rcw:begin owner=source:src_49444f9139f952da91f5c98fc1682d84 block=evidence -->
- The agent is not a sandbox: before running the user's shell it applies a lexical denylist (e.g. `rm -rf`, `git reset --hard`, shutdown commands); other commands and file operations run with the process's own permissions. [@claim:clm_2c5a4bb56f1348950c2f8fe10bc20b679ce23821e6f65b0d82ef20c4fddcedcc]
- The product provides one-shot prompts, an interactive terminal UI, local coding tools, durable conversations, and automatic context compaction. [@claim:clm_476350f166687f7b70dff4932bf3d832b541dcf75ce08797e7620e1c21d693b1]
- Users sign in with `microcodex login` (a `--device-auth` option exists for remote or headless machines) and can run interactively or pass a one-shot prompt as an argument. [@claim:clm_55199b7ae7bf7b3dc8ef0f368410b4187016dc07503fcc734137ea9c8df8bf7b]
- Installation is via a curl-piped install script (with `MICROCODEX_RELEASE` selecting a specific release) or by downloading a platform archive from GitHub Releases. [@claim:clm_6d2a08efa679accbe146a3243a301e0f555d07b72559ea8478ee75038ac8f9c4]
- OAuth credentials from login are stored under `$CODEX_HOME`, or `~/.codex` when that variable is unset. [@claim:clm_814b5eff35a095df5a6df22fcac21d114de019fe310cabc542827004c887126b]
- Skills are discovered under `$CODEX_HOME/skills` (default `~/.codex/skills`); each needs a `SKILL.md` with YAML frontmatter name and description, and the full skill is read only when its metadata matches the task. [@claim:clm_a80d3c7460f983b1f820ed26f27f962f064c2f8c11f4218fc7c8687b5ed4a81c]
- Linux requires the libcurl and OpenSSL runtime libraries, and prebuilt binaries are published for macOS and Linux on arm64 and x86_64. [@claim:clm_d639afff502118d2d83cba42a52c2925f46745400f888d15e7de03211be245a1]
- MicroCodex is described as an ultra-lightweight coding agent that runs locally in the terminal and is written in C++23. [@claim:clm_d783119fdc45814c405ba90a1796dc801ee3dcc358ade78e035eff3bafdf1d24]
- Documented known issues include unimplemented MCP support, inability to copy text from the terminal during use, and a bash safety gate that may miss indirect or unrecognized destructive commands. [@claim:clm_f6c9da148f3d567b09251d5165f15d2c3809c54f9073e0e310a869a28ccc225e]
<!-- rcw:end owner=source:src_49444f9139f952da91f5c98fc1682d84 block=evidence -->

## Researcher notes

