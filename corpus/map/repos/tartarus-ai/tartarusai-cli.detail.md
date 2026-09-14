# tartarus-ai/tartarusai-cli -- full detail

[Back to orientation](tartarusai-cli.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/tartarus-ai/tartarusai-cli/e708827a11df63efe686cbfb89b30df01fed8d57/36670dd6b96a642c.json](../../../wiki/dossiers/tartarus-ai/tartarusai-cli/e708827a11df63efe686cbfb89b30df01fed8d57/36670dd6b96a642c.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (3 claim(s))

- [observation/documented] The product is marketed as an uncensored coding agent with no policy filter, aimed at security research and edge-case automation that mainstream models reportedly refuse. -- evidence: [README.md#L29-L32](https://github.com/Tartarus-AI/tartarusai-cli/blob/e708827a11df63efe686cbfb89b30df01fed8d57/README.md#L29-L32), [README.md#L86-L90](https://github.com/Tartarus-AI/tartarusai-cli/blob/e708827a11df63efe686cbfb89b30df01fed8d57/README.md#L86-L90), [README.md#L7-L7](https://github.com/Tartarus-AI/tartarusai-cli/blob/e708827a11df63efe686cbfb89b30df01fed8d57/README.md#L7-L7) (`clm_c6f9abb1ae627f83809d280eada8d04f4d89e7f8424c3671cdc978114531349e`)
- [observation/documented] The README states stated boundaries: no weaponized payloads, spyware, DRM bypass, or license cracking; lab PoCs for patched public CVEs are in scope, attacking systems you don't own is not. -- evidence: [README.md#L103-L109](https://github.com/Tartarus-AI/tartarusai-cli/blob/e708827a11df63efe686cbfb89b30df01fed8d57/README.md#L103-L109) (`clm_3268dd22e065f8595afdbbbf8f5e4b587ae983a3d7950722366faa662d60e371`)
- [observation/documented] Advertised capabilities include a 256K context window, crypto-only billing, roughly 30 seconds from payment to activation, and a 14-day refund policy. -- evidence: [README.md#L86-L90](https://github.com/Tartarus-AI/tartarusai-cli/blob/e708827a11df63efe686cbfb89b30df01fed8d57/README.md#L86-L90) (`clm_99ba21905e6465ed3bd80e88a07a90a9f7c7018f3d2b6ca32cddb9cd1b4c2008`)

## workflows (6 claim(s))

- [observation/documented] Installation on macOS/Linux is via a curl-piped setup script that installs to ~/.local/bin and auto-detects OS and CPU, falling back to a baseline build on CPUs without AVX2. -- evidence: [README.md#L42-L44](https://github.com/Tartarus-AI/tartarusai-cli/blob/e708827a11df63efe686cbfb89b30df01fed8d57/README.md#L42-L44), [README.md#L46-L47](https://github.com/Tartarus-AI/tartarusai-cli/blob/e708827a11df63efe686cbfb89b30df01fed8d57/README.md#L46-L47), [README.md#L40-L40](https://github.com/Tartarus-AI/tartarusai-cli/blob/e708827a11df63efe686cbfb89b30df01fed8d57/README.md#L40-L40) (`clm_33e35aba6c96c57cebe421425a381db6ba2ea0b5cc0ab0cd1a2b117902db34d0`)
- [observation/documented] Windows users download a zip from the latest GitHub release and run tartarus.exe; separate release artifacts exist for linux-x64, linux-x64-baseline, darwin-arm64, and darwin-x64. -- evidence: [README.md#L57-L59](https://github.com/Tartarus-AI/tartarusai-cli/blob/e708827a11df63efe686cbfb89b30df01fed8d57/README.md#L57-L59), [README.md#L51-L55](https://github.com/Tartarus-AI/tartarusai-cli/blob/e708827a11df63efe686cbfb89b30df01fed8d57/README.md#L51-L55), [README.md#L49-L49](https://github.com/Tartarus-AI/tartarusai-cli/blob/e708827a11df63efe686cbfb89b30df01fed8d57/README.md#L49-L49) (`clm_deb736b876fc2a25a0d5f6624f7510864d92dfe4d84d550f694e79d3e861fdee`)
- [observation/documented] Quickstart: create an account and CLI token at dash.tartarusai.dev/account, run 'tartarus' in a project directory, and paste the API key on first launch, where it is validated and saved. -- evidence: [README.md#L63-L70](https://github.com/Tartarus-AI/tartarusai-cli/blob/e708827a11df63efe686cbfb89b30df01fed8d57/README.md#L63-L70) (`clm_7400b1f34b147139ac2c889e6131f3cc376a3a4b654a04f999ff17851f3fc834`)
- [observation/documented] SECURITY.md asks vulnerability reports by email with description, reproduction steps, and severity assessment, with PGP available on request for sensitive issues. -- evidence: [SECURITY.md#L10-L11](https://github.com/Tartarus-AI/tartarusai-cli/blob/e708827a11df63efe686cbfb89b30df01fed8d57/SECURITY.md#L10-L11), [SECURITY.md#L5-L8](https://github.com/Tartarus-AI/tartarusai-cli/blob/e708827a11df63efe686cbfb89b30df01fed8d57/SECURITY.md#L5-L8) (`clm_916980e6fe611d1229d8c8ff2664e33820ce392b7f6d9e207cfbe1e28c55b5ff`)
- [observation/documented] The disclosure policy targets acknowledgment within 72 hours, a triage plan within 7 days, and coordinated disclosure typically within 90 days or until a fix ships. -- evidence: [SECURITY.md#L13-L17](https://github.com/Tartarus-AI/tartarusai-cli/blob/e708827a11df63efe686cbfb89b30df01fed8d57/SECURITY.md#L13-L17) (`clm_ded369ad6eaad690da440c9c2b2dc57c68ef52286222f3e42bdacc85600ffa7e`)
- [observation/documented] Good-faith research within the stated scope gets safe harbor from legal action; there is no paid bounty, but credited researchers receive THANKS.md listing and a free annual Pro+ plan. -- evidence: [SECURITY.md#L39-L41](https://github.com/Tartarus-AI/tartarusai-cli/blob/e708827a11df63efe686cbfb89b30df01fed8d57/SECURITY.md#L39-L41), [SECURITY.md#L43-L44](https://github.com/Tartarus-AI/tartarusai-cli/blob/e708827a11df63efe686cbfb89b30df01fed8d57/SECURITY.md#L43-L44) (`clm_d04b63f460e3960f9055c2065cd3a21bf2a2ac844e4e90c62795346697d477e2`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] tartarusai-cli is a terminal client for TartarusAI, invoked as the 'tartarus' command, with a --help flag and docs hosted at dash.tartarusai.dev/docs. -- evidence: [README.md#L29-L32](https://github.com/Tartarus-AI/tartarusai-cli/blob/e708827a11df63efe686cbfb89b30df01fed8d57/README.md#L29-L32), [README.md#L72-L72](https://github.com/Tartarus-AI/tartarusai-cli/blob/e708827a11df63efe686cbfb89b30df01fed8d57/README.md#L72-L72), [README.md#L63-L70](https://github.com/Tartarus-AI/tartarusai-cli/blob/e708827a11df63efe686cbfb89b30df01fed8d57/README.md#L63-L70) (`clm_9eb9988def17469a3e1d598bcef584a5189f9bf0554c8a5cb60ecc42dd602351`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] The CLI ships as a single self-contained binary requiring no Python, pip, or Node runtime. -- evidence: [README.md#L38-L38](https://github.com/Tartarus-AI/tartarusai-cli/blob/e708827a11df63efe686cbfb89b30df01fed8d57/README.md#L38-L38) (`clm_1753787732615197f2ef03d35ea24c138b9a4a76cca505b0b2b290c2f4a0bc54`)
- [observation/documented] The project is MIT-licensed, with LICENSE and NOTICE files referenced for full attribution. -- evidence: [README.md#L120-L120](https://github.com/Tartarus-AI/tartarusai-cli/blob/e708827a11df63efe686cbfb89b30df01fed8d57/README.md#L120-L120), [README.md#L9-L11](https://github.com/Tartarus-AI/tartarusai-cli/blob/e708827a11df63efe686cbfb89b30df01fed8d57/README.md#L9-L11) (`clm_50d29438b0a390b917939868b1f4b0e89da37a5fe8132e659bc6ba2514a2edf9`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

