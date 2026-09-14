# talmetis-labs/aizen -- full detail

[Back to orientation](aizen.md)

## Origins

- github-rename-resolution
- alltheagents.org-backing
- github-verified-rename

## Projects

- navy-yard
- Observatory

Full evidence record (JSON): [wiki/dossiers/talmetis-labs/aizen/997bdd3bbba4222a9d67322a10f026146853e7be/861f8119c0413970.json](../../../wiki/dossiers/talmetis-labs/aizen/997bdd3bbba4222a9d67322a10f026146853e7be/861f8119c0413970.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] The sandbox code is organized under src/sandbox with modules for policy, capabilities, a single runner that builds sandboxed commands, audit logging, and per-platform backends (guarded, linux, windows, macos). -- evidence: [docs/SANDBOX.md#L55-L68](https://github.com/talmetis-labs/aizen/blob/997bdd3bbba4222a9d67322a10f026146853e7be/docs/SANDBOX.md#L55-L68) (`clm_85b8d7c10e6cdeff1f76449391c3adc777b5bb21bb6ba95008d87c03e8a9178b`)
- [observation/documented] v0.6.1 consolidated tools: multi_edit merged into file_edit (edits[] for atomic multi-edit), and four checkpoint tools collapsed into checkpoint (save/rewind/restore) and read-only checkpoint_view (diff/list). -- evidence: [release-notes-v0.6.1.md#L22-L23](https://github.com/talmetis-labs/aizen/blob/997bdd3bbba4222a9d67322a10f026146853e7be/release-notes-v0.6.1.md#L22-L23), [release-notes-v0.6.1.md#L16-L18](https://github.com/talmetis-labs/aizen/blob/997bdd3bbba4222a9d67322a10f026146853e7be/release-notes-v0.6.1.md#L16-L18) (`clm_05385f8d7a9cc631ed358706d5d7b0605b6d4c2f235b4036d0eddbf945489337`)

## design-choices (1 claim(s))

- [observation/documented] Aizen is documented as a single static binary (~34 MB, ~10 ms cold start claimed) requiring no Node, Python, Docker, or cloud account, targeting Windows, Linux, and macOS. -- evidence: [README.md#L87-L94](https://github.com/talmetis-labs/aizen/blob/997bdd3bbba4222a9d67322a10f026146853e7be/README.md#L87-L94), [README.md#L8-L8](https://github.com/talmetis-labs/aizen/blob/997bdd3bbba4222a9d67322a10f026146853e7be/README.md#L8-L8), [README.md#L19-L24](https://github.com/talmetis-labs/aizen/blob/997bdd3bbba4222a9d67322a10f026146853e7be/README.md#L19-L24) (`clm_38c61cce565629a074ed964da1c14ca3b000211d5a61d1b1ce1384b368e588e4`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributors sign a CLA once via a bot-comment flow with the exact sentence 'I have read the CLA Document and I hereby sign the CLA'; the CLA grants the maintainer commercial relicensing rights while the public project stays Apache-2.0. -- evidence: [CLA.md#L42-L45](https://github.com/talmetis-labs/aizen/blob/997bdd3bbba4222a9d67322a10f026146853e7be/CLA.md#L42-L45), [CLA.md#L100-L100](https://github.com/talmetis-labs/aizen/blob/997bdd3bbba4222a9d67322a10f026146853e7be/CLA.md#L100-L100), [CLA.md#L96-L98](https://github.com/talmetis-labs/aizen/blob/997bdd3bbba4222a9d67322a10f026146853e7be/CLA.md#L96-L98), [README.md#L123-L125](https://github.com/talmetis-labs/aizen/blob/997bdd3bbba4222a9d67322a10f026146853e7be/README.md#L123-L125) (`clm_8849efd66f1205586c9c2b171e884a4def0e1641644273156c58b9e36c22e55e`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] The agent accepts any OpenAI-style /chat/completions endpoint, including OpenAI, OpenRouter, local llama.cpp/vLLM, or an Anthropic gateway. -- evidence: [README.md#L87-L94](https://github.com/talmetis-labs/aizen/blob/997bdd3bbba4222a9d67322a10f026146853e7be/README.md#L87-L94), [README.md#L10-L11](https://github.com/talmetis-labs/aizen/blob/997bdd3bbba4222a9d67322a10f026146853e7be/README.md#L10-L11) (`clm_3af7ab718bcdc97d5b61b3ee2be67fce744197e4861011292aebe22c1f89bfbf`)

## memory-state (1 claim(s))

- [observation/documented] The agent is documented to keep an offline BM25-ranked memory that learns from reuse, plus a persona, a durable 'SOUL' identity, and skills it writes for itself after real work. -- evidence: [README.md#L87-L94](https://github.com/talmetis-labs/aizen/blob/997bdd3bbba4222a9d67322a10f026146853e7be/README.md#L87-L94) (`clm_8207e6c9419d8e63eb62d7cba4b27e1c2c5bb05ab922b6e5341db7eaccd769cb`)

## orchestration (1 claim(s))

- [observation/documented] A 'Pantheon' of seven capability-scoped sub-agents (argus, metis, daedalus, nemesis, themis, clio, mnemosyne) is fanned out via `aizen workflow`, which synthesizes one answer. -- evidence: [README.md#L108-L113](https://github.com/talmetis-labs/aizen/blob/997bdd3bbba4222a9d67322a10f026146853e7be/README.md#L108-L113) (`clm_7bc1e401d59be4d25fc94a0d810f93d5808a5f468b6e6dcb30c793f993ad1c77`)

## tools-permissions (3 claim(s))

- [observation/documented] The sandbox runs commands without inheriting API keys, denies network by default, and enforces filesystem policy via Landlock+seccomp on Linux and Seatbelt on macOS; Windows uses Job-Object containment and reports 'partial'. -- evidence: [README.md#L87-L94](https://github.com/talmetis-labs/aizen/blob/997bdd3bbba4222a9d67322a10f026146853e7be/README.md#L87-L94), [docs/SANDBOX.md#L101-L108](https://github.com/talmetis-labs/aizen/blob/997bdd3bbba4222a9d67322a10f026146853e7be/docs/SANDBOX.md#L101-L108) (`clm_6f5411b8c7a55f2cf10ddaf47c3f2a726f7e2e064f1c513f8c7aefbd6ddb9e6a`)
- [observation/documented] Sandbox modes are auto (default), strict, guarded, and off; strict refuses spawns rather than downgrading, and unattended runs fail closed unless sandbox.allow_guarded_fallback is true. -- evidence: [docs/SANDBOX.md#L85-L90](https://github.com/talmetis-labs/aizen/blob/997bdd3bbba4222a9d67322a10f026146853e7be/docs/SANDBOX.md#L85-L90) (`clm_5f074ab5b4c50963369dcd51fc8e9853f5571046eb318299442ed63cfdff038e`)
- [observation/documented] Approval (ask/smart/yolo plus a cmd_guard hard floor) is separate from the sandbox: even approved commands get no secrets, no network, and no out-of-workspace writes where kernel backends exist. -- evidence: [docs/SANDBOX.md#L41-L46](https://github.com/talmetis-labs/aizen/blob/997bdd3bbba4222a9d67322a10f026146853e7be/docs/SANDBOX.md#L41-L46) (`clm_3ebecac6d2c2ef8b24fdad97feae964bc5f1f9d5f2bb8fca855285e3a2a5899f`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## limitations (1 claim(s))

- [observation/documented] The sandbox explicitly does not protect against kernel exploits, an already-compromised user account or machine, secrets placed inside the workspace, or a human approving a harmful command. -- evidence: [docs/SANDBOX.md#L32-L35](https://github.com/talmetis-labs/aizen/blob/997bdd3bbba4222a9d67322a10f026146853e7be/docs/SANDBOX.md#L32-L35) (`clm_8e621931587e82991be770db96578a73805046d928f621a3aa1aca5ce56e4ee7`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

