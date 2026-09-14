# squarewavesystems/squarebox -- full detail

[Back to orientation](squarebox.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/squarewavesystems/squarebox/8c1f97fcfb571473ea85251e78e5f020017e6d4f/49d1143036d8e9ff.json](../../../wiki/dossiers/squarewavesystems/squarebox/8c1f97fcfb571473ea85251e78e5f020017e6d4f/49d1143036d8e9ff.json)

## specifications (1 claim(s))

- [observation/documented] squarebox packages a terminal development environment—CLI tools, AI coding assistants, language SDKs, and shell aliases—into a single Docker container (Podman experimental), runnable on desktop, VPS, or Codespace. -- evidence: [README.md#L8-L12](https://github.com/SquareWaveSystems/squarebox/blob/8c1f97fcfb571473ea85251e78e5f020017e6d4f/README.md#L8-L12) (`clm_ce09888fbf82b9c454d7b1a4716bc70a81765392471db529d048ac8f8cbccff6`)

## components (2 claim(s))

- [observation/documented] The image ships CLI tools including bat, delta, difftastic, eza, fd, fzf, gh, glow, jq, just, mise, nano, ripgrep, starship, and bubblewrap (used by the Codex CLI sandbox). -- evidence: [README.md#L222-L243](https://github.com/SquareWaveSystems/squarebox/blob/8c1f97fcfb571473ea85251e78e5f020017e6d4f/README.md#L222-L243) (`clm_f244573f3442504fcb4647ceab3f0448e2d4e919f034c107e864982566ce2297`)
- [observation/documented] Optional first-run selections include AI assistants (Claude Code, Copilot CLI, Gemini CLI, Codex CLI, opencode, Pi, Oh My Pi), editors (micro, edit, fresh, helix, nvim), TUI tools, and multiplexers (tmux, zellij, herdr). -- evidence: [README.md#L272-L278](https://github.com/SquareWaveSystems/squarebox/blob/8c1f97fcfb571473ea85251e78e5f020017e6d4f/README.md#L272-L278), [README.md#L297-L301](https://github.com/SquareWaveSystems/squarebox/blob/8c1f97fcfb571473ea85251e78e5f020017e6d4f/README.md#L297-L301), [README.md#L256-L265](https://github.com/SquareWaveSystems/squarebox/blob/8c1f97fcfb571473ea85251e78e5f020017e6d4f/README.md#L256-L265), [README.md#L286-L291](https://github.com/SquareWaveSystems/squarebox/blob/8c1f97fcfb571473ea85251e78e5f020017e6d4f/README.md#L286-L291) (`clm_f674de14d7e27e21f32aa0ca1acd98b70a7ec946151fb454b46f76eac8a02048`)

## design-choices (3 claim(s))

- [observation/documented] The box defines opinionated aliases (ls→eza, cat→bat, git shorthands) and generates *-yolo aliases for selected AI tools that disable approval prompts; codex-yolo additionally disables Codex's sandbox. -- evidence: [README.md#L371-L395](https://github.com/SquareWaveSystems/squarebox/blob/8c1f97fcfb571473ea85251e78e5f020017e6d4f/README.md#L371-L395), [README.md#L397-L400](https://github.com/SquareWaveSystems/squarebox/blob/8c1f97fcfb571473ea85251e78e5f020017e6d4f/README.md#L397-L400) (`clm_7cc592f3d8252fc87f9f8b6ca42f50632526d09d057485b66f198c61ed6baee1`)
- [observation/documented] SDKs are managed exclusively through mise, with selections written to ~/.config/mise/config.toml and shims wired into bash, zsh, and fish via mise activate. -- evidence: [README.md#L337-L340](https://github.com/SquareWaveSystems/squarebox/blob/8c1f97fcfb571473ea85251e78e5f020017e6d4f/README.md#L337-L340) (`clm_fc9612b2344883fa686cf9ee1a4bd918061a7ec5945e097518d2dcbdb639f9b8`)
- [observation/documented] Artifact installation is fail-closed: GitHub-hosted optional tools require an exact release tag, one exactly named asset, and a matching SHA-256 digest, failing before download or extraction on missing or malformed metadata. -- evidence: [docs/adr/0001-fail-closed-artifact-installation.md#L3-L15](https://github.com/SquareWaveSystems/squarebox/blob/8c1f97fcfb571473ea85251e78e5f020017e6d4f/docs/adr/0001-fail-closed-artifact-installation.md#L3-L15), [README.md#L535-L542](https://github.com/SquareWaveSystems/squarebox/blob/8c1f97fcfb571473ea85251e78e5f020017e6d4f/README.md#L535-L542) (`clm_901e94172194af794762b741fb1af4ede0b419ea88fd915ad4147016079f3684`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] Installers accept flags --build, --edge, --adopt, --verbose and environment variables such as SQUAREBOX_DIR, SQUAREBOX_TAG, SQUAREBOX_RUNTIME, PUID/PGID, and non-interactive toolset selectors like SQUAREBOX_AI and SQUAREBOX_SDKS. -- evidence: [README.md#L97-L107](https://github.com/SquareWaveSystems/squarebox/blob/8c1f97fcfb571473ea85251e78e5f020017e6d4f/README.md#L97-L107), [README.md#L94-L95](https://github.com/SquareWaveSystems/squarebox/blob/8c1f97fcfb571473ea85251e78e5f020017e6d4f/README.md#L94-L95), [README.md#L113-L120](https://github.com/SquareWaveSystems/squarebox/blob/8c1f97fcfb571473ea85251e78e5f020017e6d4f/README.md#L113-L120) (`clm_aa9fa819bc9d7955bfb520d2fecf6c176a1a94763c819b0e6c1c7410310092f8`)
- [observation/documented] Inside the container, sqrbx-setup re-runs the configuration wizard (sections git, github, ai, editors, tuis, multiplexers, sdks, shell), sqrbx-update manages tool updates, and sqrbx-help lists the sqrbx-* commands. -- evidence: [README.md#L362-L366](https://github.com/SquareWaveSystems/squarebox/blob/8c1f97fcfb571473ea85251e78e5f020017e6d4f/README.md#L362-L366), [README.md#L449-L449](https://github.com/SquareWaveSystems/squarebox/blob/8c1f97fcfb571473ea85251e78e5f020017e6d4f/README.md#L449-L449), [README.md#L353-L357](https://github.com/SquareWaveSystems/squarebox/blob/8c1f97fcfb571473ea85251e78e5f020017e6d4f/README.md#L353-L357) (`clm_6cd6a43ac673c6ea9313d97ebd1a9fdb92a4ddae23f1260b40fbadc693c1e343`)
- [observation/documented] The published image is multi-arch (amd64 + arm64), and the reviewed amd64 v1.1 candidate is roughly 900 MB in docker image ls, with optional components adding from ~7 MB (edit) to ~800 MB (.NET). -- evidence: [README.md#L506-L523](https://github.com/SquareWaveSystems/squarebox/blob/8c1f97fcfb571473ea85251e78e5f020017e6d4f/README.md#L506-L523), [README.md#L499-L502](https://github.com/SquareWaveSystems/squarebox/blob/8c1f97fcfb571473ea85251e78e5f020017e6d4f/README.md#L499-L502), [README.md#L206-L210](https://github.com/SquareWaveSystems/squarebox/blob/8c1f97fcfb571473ea85251e78e5f020017e6d4f/README.md#L206-L210) (`clm_1b25ecc6dd2e55d52276bf21caa1ec9a480944b8d63ebddf8a61b87d3cf10745`)

## memory-state (1 claim(s))

- [observation/documented] Per-user state (shell history, GitHub CLI auth, AI-assistant data, mise toolchains) lives in the squarebox-home named Docker volume that survives container replacement, while code lives on the host at the workspace bind mount. -- evidence: [README.md#L179-L186](https://github.com/SquareWaveSystems/squarebox/blob/8c1f97fcfb571473ea85251e78e5f020017e6d4f/README.md#L179-L186), [README.md#L206-L210](https://github.com/SquareWaveSystems/squarebox/blob/8c1f97fcfb571473ea85251e78e5f020017e6d4f/README.md#L206-L210) (`clm_3281b13f7cb96e2da3d15724ec7c8f0ca5330d27a1a8d8116aae15b0f6ab1a79`)

## orchestration (1 claim(s))

- [observation/documented] For persistent server use (Unraid/NAS/VPS), the README directs users to run the prebuilt image via the bundled docker-compose.yml with PUID/PGID set in .env, attaching with docker compose exec -u dev. -- evidence: [README.md#L196-L198](https://github.com/SquareWaveSystems/squarebox/blob/8c1f97fcfb571473ea85251e78e5f020017e6d4f/README.md#L196-L198), [README.md#L200-L204](https://github.com/SquareWaveSystems/squarebox/blob/8c1f97fcfb571473ea85251e78e5f020017e6d4f/README.md#L200-L204), [README.md#L191-L194](https://github.com/SquareWaveSystems/squarebox/blob/8c1f97fcfb571473ea85251e78e5f020017e6d4f/README.md#L191-L194) (`clm_ccb1ebce4407b2beabb3505ddd2f72cbc660e483c5d3f109a191e06d715c85fd`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Prerequisites are Docker (primary, tested) or Podman (experimental), plus Git; the installer auto-detects the runtime and offers a one-line Docker install path for macOS, Linux, and Windows. -- evidence: [README.md#L48-L48](https://github.com/SquareWaveSystems/squarebox/blob/8c1f97fcfb571473ea85251e78e5f020017e6d4f/README.md#L48-L48), [README.md#L44-L44](https://github.com/SquareWaveSystems/squarebox/blob/8c1f97fcfb571473ea85251e78e5f020017e6d4f/README.md#L44-L44), [README.md#L30-L32](https://github.com/SquareWaveSystems/squarebox/blob/8c1f97fcfb571473ea85251e78e5f020017e6d4f/README.md#L30-L32), [README.md#L54-L54](https://github.com/SquareWaveSystems/squarebox/blob/8c1f97fcfb571473ea85251e78e5f020017e6d4f/README.md#L54-L54), [README.md#L27-L28](https://github.com/SquareWaveSystems/squarebox/blob/8c1f97fcfb571473ea85251e78e5f020017e6d4f/README.md#L27-L28) (`clm_06ed315b3b97e872ac31522735a193e8d19dbd9df81305e6e6d5c8c4d957fb07`)

## limitations (2 claim(s))

- [observation/documented] Podman support is explicitly experimental, with possible rough edges around volume mounts, SSH agent forwarding, and rebuild flows; the rootless adapter disables SELinux container separation. -- evidence: [README.md#L34-L39](https://github.com/SquareWaveSystems/squarebox/blob/8c1f97fcfb571473ea85251e78e5f020017e6d4f/README.md#L34-L39) (`clm_d5faef4e2dbcc94a248da68394aada9779173c1b81dc6b68b23091bc5bd67590`)
- [observation/documented] The ADR notes its rollback guarantee is not crash atomicity—power loss during a multi-path commit can leave staged files needing inspection—and dpkg package operations fall outside the rollback guarantee. -- evidence: [docs/adr/0001-fail-closed-artifact-installation.md#L17-L24](https://github.com/SquareWaveSystems/squarebox/blob/8c1f97fcfb571473ea85251e78e5f020017e6d4f/docs/adr/0001-fail-closed-artifact-installation.md#L17-L24), [docs/adr/0001-fail-closed-artifact-installation.md#L31-L36](https://github.com/SquareWaveSystems/squarebox/blob/8c1f97fcfb571473ea85251e78e5f020017e6d4f/docs/adr/0001-fail-closed-artifact-installation.md#L31-L36) (`clm_02ebf76a05bd8cb850c17aa49a63d0f4f07f9da47fa51796d2542c48213fc273`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

