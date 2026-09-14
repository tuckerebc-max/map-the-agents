---
access: public
aliases: []
claim_ids:
- clm_06ed315b3b97e872ac31522735a193e8d19dbd9df81305e6e6d5c8c4d957fb07
- clm_1b25ecc6dd2e55d52276bf21caa1ec9a480944b8d63ebddf8a61b87d3cf10745
- clm_3281b13f7cb96e2da3d15724ec7c8f0ca5330d27a1a8d8116aae15b0f6ab1a79
- clm_6cd6a43ac673c6ea9313d97ebd1a9fdb92a4ddae23f1260b40fbadc693c1e343
- clm_7cc592f3d8252fc87f9f8b6ca42f50632526d09d057485b66f198c61ed6baee1
- clm_901e94172194af794762b741fb1af4ede0b419ea88fd915ad4147016079f3684
- clm_aa9fa819bc9d7955bfb520d2fecf6c176a1a94763c819b0e6c1c7410310092f8
- clm_ccb1ebce4407b2beabb3505ddd2f72cbc660e483c5d3f109a191e06d715c85fd
- clm_ce09888fbf82b9c454d7b1a4716bc70a81765392471db529d048ac8f8cbccff6
- clm_d5faef4e2dbcc94a248da68394aada9779173c1b81dc6b68b23091bc5bd67590
- clm_f244573f3442504fcb4647ceab3f0448e2d4e919f034c107e864982566ce2297
- clm_f674de14d7e27e21f32aa0ca1acd98b70a7ec946151fb454b46f76eac8a02048
- clm_fc9612b2344883fa686cf9ee1a4bd918061a7ec5945e097518d2dcbdb639f9b8
maturity: draft
page_id: pg_2688cf9bc8025659abc8ebb4516a2851
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_aa55d0785078586587919ed330a39396
title: SquareWaveSystems/squarebox/README.md @ 8c1f97fcfb57
updated_at: '2026-09-14T04:23:14Z'
---

# SquareWaveSystems/squarebox/README.md @ 8c1f97fcfb57

<!-- rcw:begin owner=source:src_aa55d0785078586587919ed330a39396 block=evidence -->
- Prerequisites are Docker (primary, tested) or Podman (experimental), plus Git; the installer auto-detects the runtime and offers a one-line Docker install path for macOS, Linux, and Windows. [@claim:clm_06ed315b3b97e872ac31522735a193e8d19dbd9df81305e6e6d5c8c4d957fb07]
- The published image is multi-arch (amd64 + arm64), and the reviewed amd64 v1.1 candidate is roughly 900 MB in docker image ls, with optional components adding from ~7 MB (edit) to ~800 MB (.NET). [@claim:clm_1b25ecc6dd2e55d52276bf21caa1ec9a480944b8d63ebddf8a61b87d3cf10745]
- Per-user state (shell history, GitHub CLI auth, AI-assistant data, mise toolchains) lives in the squarebox-home named Docker volume that survives container replacement, while code lives on the host at the workspace bind mount. [@claim:clm_3281b13f7cb96e2da3d15724ec7c8f0ca5330d27a1a8d8116aae15b0f6ab1a79]
- Inside the container, sqrbx-setup re-runs the configuration wizard (sections git, github, ai, editors, tuis, multiplexers, sdks, shell), sqrbx-update manages tool updates, and sqrbx-help lists the sqrbx-* commands. [@claim:clm_6cd6a43ac673c6ea9313d97ebd1a9fdb92a4ddae23f1260b40fbadc693c1e343]
- The box defines opinionated aliases (ls→eza, cat→bat, git shorthands) and generates *-yolo aliases for selected AI tools that disable approval prompts; codex-yolo additionally disables Codex's sandbox. [@claim:clm_7cc592f3d8252fc87f9f8b6ca42f50632526d09d057485b66f198c61ed6baee1]
- Artifact installation is fail-closed: GitHub-hosted optional tools require an exact release tag, one exactly named asset, and a matching SHA-256 digest, failing before download or extraction on missing or malformed metadata. [@claim:clm_901e94172194af794762b741fb1af4ede0b419ea88fd915ad4147016079f3684]
- Installers accept flags --build, --edge, --adopt, --verbose and environment variables such as SQUAREBOX_DIR, SQUAREBOX_TAG, SQUAREBOX_RUNTIME, PUID/PGID, and non-interactive toolset selectors like SQUAREBOX_AI and SQUAREBOX_SDKS. [@claim:clm_aa9fa819bc9d7955bfb520d2fecf6c176a1a94763c819b0e6c1c7410310092f8]
- For persistent server use (Unraid/NAS/VPS), the README directs users to run the prebuilt image via the bundled docker-compose.yml with PUID/PGID set in .env, attaching with docker compose exec -u dev. [@claim:clm_ccb1ebce4407b2beabb3505ddd2f72cbc660e483c5d3f109a191e06d715c85fd]
- squarebox packages a terminal development environment—CLI tools, AI coding assistants, language SDKs, and shell aliases—into a single Docker container (Podman experimental), runnable on desktop, VPS, or Codespace. [@claim:clm_ce09888fbf82b9c454d7b1a4716bc70a81765392471db529d048ac8f8cbccff6]
- Podman support is explicitly experimental, with possible rough edges around volume mounts, SSH agent forwarding, and rebuild flows; the rootless adapter disables SELinux container separation. [@claim:clm_d5faef4e2dbcc94a248da68394aada9779173c1b81dc6b68b23091bc5bd67590]
- The image ships CLI tools including bat, delta, difftastic, eza, fd, fzf, gh, glow, jq, just, mise, nano, ripgrep, starship, and bubblewrap (used by the Codex CLI sandbox). [@claim:clm_f244573f3442504fcb4647ceab3f0448e2d4e919f034c107e864982566ce2297]
- Optional first-run selections include AI assistants (Claude Code, Copilot CLI, Gemini CLI, Codex CLI, opencode, Pi, Oh My Pi), editors (micro, edit, fresh, helix, nvim), TUI tools, and multiplexers (tmux, zellij, herdr). [@claim:clm_f674de14d7e27e21f32aa0ca1acd98b70a7ec946151fb454b46f76eac8a02048]
- SDKs are managed exclusively through mise, with selections written to ~/.config/mise/config.toml and shims wired into bash, zsh, and fish via mise activate. [@claim:clm_fc9612b2344883fa686cf9ee1a4bd918061a7ec5945e097518d2dcbdb639f9b8]
<!-- rcw:end owner=source:src_aa55d0785078586587919ed330a39396 block=evidence -->

## Researcher notes

