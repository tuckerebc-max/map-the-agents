# kommander/oc-plugin-vault-tec -- full detail

[Back to orientation](oc-plugin-vault-tec.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/kommander/oc-plugin-vault-tec/a0184713d03795e641d1aae9b6d66f1a76cd9afc/1506c8a77987616d.json](../../../wiki/dossiers/kommander/oc-plugin-vault-tec/a0184713d03795e641d1aae9b6d66f1a76cd9afc/1506c8a77987616d.json)

## specifications (1 claim(s))

- [observation/documented] The plugin is described as a Vault-Tec personality matrix that turns the coding terminal into a pre-War RobCo engineering assistant, including 122 vault experiment dossiers. -- evidence: [README.md#L3-L3](https://github.com/kommander/oc-plugin-vault-tec/blob/a0184713d03795e641d1aae9b6d66f1a76cd9afc/README.md#L3-L3) (`clm_0d008aa991c2abfdb3b99b03f39233ea63d33c1ca65d28c12a1677b337fe22a5`)

## components (3 claim(s))

- [observation/documented] Server-side options include enabled (default true), mode with append/replace values (default append), and an optional prompt override string. -- evidence: [README.md#L27-L29](https://github.com/kommander/oc-plugin-vault-tec/blob/a0184713d03795e641d1aae9b6d66f1a76cd9afc/README.md#L27-L29) (`clm_e7570c56aa9e53e5a04a003e03a71e8663424821fcd5091b3fe4563a6564296a`)
- [observation/documented] TUI options cover enabled, theme (default 'vault-tec'), set_theme, scanlines, vignette (default 0.75), sidebar, and tips, all defaulting to true except vignette. -- evidence: [README.md#L33-L39](https://github.com/kommander/oc-plugin-vault-tec/blob/a0184713d03795e641d1aae9b6d66f1a76cd9afc/README.md#L33-L39) (`clm_aceaac6d100fc055ca0e5ed17c17ecf670920c16cb2905e16eb7d6ba3c29a504`)
- [observation/documented] The prompt file opens with a RobCo TERMLINK boot sequence, initializes a 'personality matrix', and grants 'Overseer-level access' before defining the VT-OS/OPENCODE persona. -- evidence: [prompt.txt#L1-L7](https://github.com/kommander/oc-plugin-vault-tec/blob/a0184713d03795e641d1aae9b6d66f1a76cd9afc/prompt.txt#L1-L7), [prompt.txt#L17-L17](https://github.com/kommander/oc-plugin-vault-tec/blob/a0184713d03795e641d1aae9b6d66f1a76cd9afc/prompt.txt#L17-L17), [prompt.txt#L9-L11](https://github.com/kommander/oc-plugin-vault-tec/blob/a0184713d03795e641d1aae9b6d66f1a76cd9afc/prompt.txt#L9-L11) (`clm_b9a4fe41c81e14c3ea40e83bf2d885cbb3f62fcea113edbe8f2eca0848e3d83c`)

## design-choices (3 claim(s))

- [observation/documented] Operating parameters state that engineering competency always takes priority: Vault-Tec communication standards never supersede engineering accuracy, and the agent should use all available tools to complete tasks. -- evidence: [prompt.txt#L155-L160](https://github.com/kommander/oc-plugin-vault-tec/blob/a0184713d03795e641d1aae9b6d66f1a76cd9afc/prompt.txt#L155-L160), [prompt.txt#L181-L181](https://github.com/kommander/oc-plugin-vault-tec/blob/a0184713d03795e641d1aae9b6d66f1a76cd9afc/prompt.txt#L181-L181) (`clm_698db6ca4aa05b8567f814e692ebaafb55f40040dcccda35683509665013a77e`)
- [observation/documented] Responses should be formatted as terminal output with status lines like '[VT-OS] STATUS: OPERATIONAL', '>' prefixes, [WARNING]/[CAUTION] blocks, and terminal-style sign-offs. -- evidence: [prompt.txt#L162-L167](https://github.com/kommander/oc-plugin-vault-tec/blob/a0184713d03795e641d1aae9b6d66f1a76cd9afc/prompt.txt#L162-L167) (`clm_55bf603d66fa84527b4ba1f97d421194eae52d2258c15240043f9664be55efd7`)
- [observation/documented] The prompt imposes a hard no-emoji rule, requiring ASCII art and text symbols instead, framed as incompatible with RobCo CRT display hardware. -- evidence: [prompt.txt#L179-L179](https://github.com/kommander/oc-plugin-vault-tec/blob/a0184713d03795e641d1aae9b6d66f1a76cd9afc/prompt.txt#L179-L179), [prompt.txt#L171-L177](https://github.com/kommander/oc-plugin-vault-tec/blob/a0184713d03795e641d1aae9b6d66f1a76cd9afc/prompt.txt#L171-L177) (`clm_3710cb7dfaf3d8f630a0deaf9f419c0d5cda315c429366d7b392ece1c7d90b03`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (2 claim(s))

- [observation/documented] The prompt instructs the agent to speak as a pre-War Vault-Tec corporate terminal with 1950s atomic-age optimism, retro slogans, and themed jargon for bugs, errors, builds, tests, and deployments. -- evidence: [prompt.txt#L23-L39](https://github.com/kommander/oc-plugin-vault-tec/blob/a0184713d03795e641d1aae9b6d66f1a76cd9afc/prompt.txt#L23-L39) (`clm_bb70463f049c97f103553232f2cda80462b5e5a8334498a4626ced7cb91a5cad`)
- [observation/documented] The prompt embeds a large Fallout lore knowledge base: corporate history, Project Safehouse, vault architecture, notable vault experiments, UOS, Pip-Boy, key technologies, factions, and pre/post-war world history. -- evidence: [prompt.txt#L63-L95](https://github.com/kommander/oc-plugin-vault-tec/blob/a0184713d03795e641d1aae9b6d66f1a76cd9afc/prompt.txt#L63-L95), [prompt.txt#L98-L104](https://github.com/kommander/oc-plugin-vault-tec/blob/a0184713d03795e641d1aae9b6d66f1a76cd9afc/prompt.txt#L98-L104), [prompt.txt#L135-L145](https://github.com/kommander/oc-plugin-vault-tec/blob/a0184713d03795e641d1aae9b6d66f1a76cd9afc/prompt.txt#L135-L145), [prompt.txt#L110-L119](https://github.com/kommander/oc-plugin-vault-tec/blob/a0184713d03795e641d1aae9b6d66f1a76cd9afc/prompt.txt#L110-L119), [prompt.txt#L122-L132](https://github.com/kommander/oc-plugin-vault-tec/blob/a0184713d03795e641d1aae9b6d66f1a76cd9afc/prompt.txt#L122-L132), [prompt.txt#L45-L45](https://github.com/kommander/oc-plugin-vault-tec/blob/a0184713d03795e641d1aae9b6d66f1a76cd9afc/prompt.txt#L45-L45), [prompt.txt#L52-L52](https://github.com/kommander/oc-plugin-vault-tec/blob/a0184713d03795e641d1aae9b6d66f1a76cd9afc/prompt.txt#L52-L52) (`clm_f9e37049857ffda0d8fd8a0155dcb58465ba3b549fb5cafc42776b1c43545a34`)

## interfaces (2 claim(s))

- [observation/documented] Installation is supported via the CLI command 'opencode plugin oc-plugin-vault-tec' or through OpenCode's Ctrl+P 'Install Plugin' flow. -- evidence: [README.md#L17-L19](https://github.com/kommander/oc-plugin-vault-tec/blob/a0184713d03795e641d1aae9b6d66f1a76cd9afc/README.md#L17-L19), [README.md#L11-L13](https://github.com/kommander/oc-plugin-vault-tec/blob/a0184713d03795e641d1aae9b6d66f1a76cd9afc/README.md#L11-L13) (`clm_31d224b143cc978e4a1d4536bdc29f5da0f9b1f8a2823572f850b41f05adbed8`)
- [observation/documented] Plugin options are configured through the opencode.json and tui.json config files. -- evidence: [README.md#L23-L23](https://github.com/kommander/oc-plugin-vault-tec/blob/a0184713d03795e641d1aae9b6d66f1a76cd9afc/README.md#L23-L23) (`clm_996a79607239cd6e70a6bf7912e90ed66aed3d207d87dec675c7fadab9b22d36`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (1 claim(s))

- [inference/documented] The plugin appears aimed at developers using OpenCode who want a Fallout-themed assistant persona and retro terminal UI theming rather than new tooling capabilities. -- evidence: [README.md#L3-L3](https://github.com/kommander/oc-plugin-vault-tec/blob/a0184713d03795e641d1aae9b6d66f1a76cd9afc/README.md#L3-L3), [README.md#L33-L39](https://github.com/kommander/oc-plugin-vault-tec/blob/a0184713d03795e641d1aae9b6d66f1a76cd9afc/README.md#L33-L39) (`clm_5b9872d4a12dae2bd5df8ab87fa1414fbe82a17d400a9d18140828ebae8bad80`)

