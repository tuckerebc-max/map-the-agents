---
access: public
aliases: []
claim_ids:
- clm_3b4e5e1b8a5d9e15f7fea2161dc93a640f16df865886cf8a28b0efb0f5ea6745
- clm_ac33c0f7ea1d148c315cbb9d2e9331a0a435acbf08e632d7cc9d657f2255fb0e
- clm_d2da4b46c34912e686ae17ecf9bb610008b2ce226f9a8cc2d0929ac48159753d
- clm_fd0e3f2c1c9b0799904a331c0536f8db65804b63d3d453b723a73a994be40f3d
- clm_fdc4018060eb05485d101a2401b5a598f4f45a67d9b30d460d4e00466788ae4f
maturity: draft
page_id: pg_04b8f80b6dcc53d7ae578c951801b3d5
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_787b91bb9f8252e08622199f5d764a33
title: Fission-AI/OpenSpec/install.md @ 9d4e5974e5c0
updated_at: '2026-09-14T03:51:47Z'
---

# Fission-AI/OpenSpec/install.md @ 9d4e5974e5c0

<!-- rcw:begin owner=source:src_787b91bb9f8252e08622199f5d764a33 block=evidence -->
- openspec init --tools <ids> generates per-tool skill and command files for the selected AI assistants, and the README claims support for 30+ tools. [@claim:clm_3b4e5e1b8a5d9e15f7fea2161dc93a640f16df865886cf8a28b0efb0f5ea6745]
- Repository development practice: install.md is an agent-facing setup prompt directing the installing agent to verify Node, install the CLI globally with user confirmation, run openspec init --tools, and report what init actually created. [@claim:clm_ac33c0f7ea1d148c315cbb9d2e9331a0a435acbf08e632d7cc9d657f2255fb0e]
- OpenSpec is driven from AI coding tools via slash commands such as /opsx:explore, /opsx:propose, /opsx:apply, and /opsx:archive, with tool-specific spellings like /opsx-propose (Cursor, Copilot), @opsx-propose (Amazon Q), or $openspec-propose (Codex). [@claim:clm_d2da4b46c34912e686ae17ecf9bb610008b2ce226f9a8cc2d0929ac48159753d]
- OpenSpec requires Node.js 20.19.0 or higher, and the install prompt instructs checking node --version before installing. [@claim:clm_fd0e3f2c1c9b0799904a331c0536f8db65804b63d3d453b723a73a994be40f3d]
- The product ships a CLI installed globally via npm, pnpm, yarn, or bun (with a Nix option), with commands including openspec init, openspec update, and openspec config profile. [@claim:clm_fdc4018060eb05485d101a2401b5a598f4f45a67d9b30d460d4e00466788ae4f]
<!-- rcw:end owner=source:src_787b91bb9f8252e08622199f5d764a33 block=evidence -->

## Researcher notes

