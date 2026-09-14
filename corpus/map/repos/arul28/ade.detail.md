# arul28/ade -- full detail

[Back to orientation](ade.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/arul28/ade/4e14f9cdf0e4825445b343f95823ddbbe3029544/e54a9a8c96c9ab57.json](../../../wiki/dossiers/arul28/ade/4e14f9cdf0e4825445b343f95823ddbbe3029544/e54a9a8c96c9ab57.json)

## specifications (1 claim(s))

- [observation/documented] ADE runs Claude Code, Codex, Cursor, Factory Droid, and OpenCode in one workspace reachable from any machine, the web, or a mobile app, and is described as free. -- evidence: [README.md#L40-L40](https://github.com/arul28/ADE/blob/4e14f9cdf0e4825445b343f95823ddbbe3029544/README.md#L40-L40) (`clm_391a72e5e594caef77f2e63ad172d47e3c3ef1967208491db6d14a80506b64cb`)

## components (1 claim(s))

- [observation/documented] The repo contains apps/ade-cli (Brain, CLI, and ade code TUI), apps/desktop (Electron), apps/ios (SwiftUI), and apps/web (website and downloads). -- evidence: [README.md#L189-L195](https://github.com/arul28/ADE/blob/4e14f9cdf0e4825445b343f95823ddbbe3029544/README.md#L189-L195) (`clm_2c94e3b8ec1f9d816c000a00c64b432928f2615611fcfa1b78bed6a3a7562ba0`)

## design-choices (1 claim(s))

- [observation/documented] ADE is local-first: the Brain is the always-on process owning the project catalog, sync websocket, and authority to run things; project data lives in .ade/ per repo and machine state in ~/.ade. -- evidence: [README.md#L187-L187](https://github.com/arul28/ADE/blob/4e14f9cdf0e4825445b343f95823ddbbe3029544/README.md#L187-L187) (`clm_39fb79aa6e34a28abb3e1c9877d6af6cf773a596633261506314d3165df81380`)

## workflows (6 claim(s))

- [observation/documented] Repository development practice: AGENTS.md defines a five-stage dev loop (/context, /quality, /test, /ship plus utilities) implemented as agent skills under .agents/skills/, with /ship wrapping an autonomous PR-to-merge playbook. -- evidence: [AGENTS.md#L17-L17](https://github.com/arul28/ADE/blob/4e14f9cdf0e4825445b343f95823ddbbe3029544/AGENTS.md#L17-L17), [AGENTS.md#L19-L22](https://github.com/arul28/ADE/blob/4e14f9cdf0e4825445b343f95823ddbbe3029544/AGENTS.md#L19-L22), [AGENTS.md#L12-L15](https://github.com/arul28/ADE/blob/4e14f9cdf0e4825445b343f95823ddbbe3029544/AGENTS.md#L12-L15), [AGENTS.md#L26-L26](https://github.com/arul28/ADE/blob/4e14f9cdf0e4825445b343f95823ddbbe3029544/AGENTS.md#L26-L26) (`clm_371dbe999fffc43586ceb731c6e0f7127169cd9a15471601d1c40e20a4fbe90c`)
- [observation/documented] Repository development practice: validation uses desktop and CLI typecheck/test/build commands, with the large desktop suite sharded and the smallest relevant subset run first. -- evidence: [AGENTS.md#L79-L91](https://github.com/arul28/ADE/blob/4e14f9cdf0e4825445b343f95823ddbbe3029544/AGENTS.md#L79-L91), [README.md#L210-L210](https://github.com/arul28/ADE/blob/4e14f9cdf0e4825445b343f95823ddbbe3029544/README.md#L210-L210), [AGENTS.md#L138-L141](https://github.com/arul28/ADE/blob/4e14f9cdf0e4825445b343f95823ddbbe3029544/AGENTS.md#L138-L141) (`clm_e2d3c884f44e5bd60f5b2f4685dc485d194085cb4c761bfabb917e00970e6a09`)
- [observation/documented] Repository development practice: PRs require conventional-commit titles, a Problem/Cause/Change/Verification body, before/after images for UI changes, and one concern per PR. -- evidence: [AGENTS.md#L72-L75](https://github.com/arul28/ADE/blob/4e14f9cdf0e4825445b343f95823ddbbe3029544/AGENTS.md#L72-L75) (`clm_26a3cb98ff4cdd901a66252b198b2a330bcb13341a0b6ee95eb9e61acc711143`)
- [observation/documented] Repository development practice: releases are cut by tagging main with vX.Y.Z, triggering a workflow that publishes a draft GitHub Release; Windows builds are gated behind the ADE_WINDOWS_PUBLIC_RELEASE_ENABLED variable. -- evidence: [AGENTS.md#L130-L132](https://github.com/arul28/ADE/blob/4e14f9cdf0e4825445b343f95823ddbbe3029544/AGENTS.md#L130-L132) (`clm_86c97dce700ad06af87539ba3420dc4f7ce2ceae3803f6ed57a648725d74f707`)
- [observation/documented] Repository development practice: Node.js 22.x is required because node:sqlite is the primary database engine, and each app under apps/ has independent node_modules with no npm workspaces. -- evidence: [AGENTS.md#L138-L141](https://github.com/arul28/ADE/blob/4e14f9cdf0e4825445b343f95823ddbbe3029544/AGENTS.md#L138-L141) (`clm_43718c723c662d9363f9bac9c02387d673d9097229f989d4643de9a45f1c205d`)
- [observation/documented] Repository development practice: CLAUDE.md assigns Claude-specific model roles, designating one model as PM/coordinator that delegates implementation to Opus 5 subagents. -- evidence: [CLAUDE.md#L3-L3](https://github.com/arul28/ADE/blob/4e14f9cdf0e4825445b343f95823ddbbe3029544/CLAUDE.md#L3-L3), [CLAUDE.md#L5-L5](https://github.com/arul28/ADE/blob/4e14f9cdf0e4825445b343f95823ddbbe3029544/CLAUDE.md#L5-L5) (`clm_7d5f630cd576c60ceb970eb682533a265871f265386a62d220c502ec0b53c396`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The ade CLI offers subcommands such as desktop, brain status, code, lanes create, prs checks, and actions list, sharing the same binary that runs the Brain. -- evidence: [README.md#L174-L181](https://github.com/arul28/ADE/blob/4e14f9cdf0e4825445b343f95823ddbbe3029544/README.md#L174-L181), [README.md#L172-L172](https://github.com/arul28/ADE/blob/4e14f9cdf0e4825445b343f95823ddbbe3029544/README.md#L172-L172) (`clm_428422f5bf33b6035bd67118e332a58b18b1f8448fc011b768351955b1b021ce`)
- [observation/documented] ade connect links a machine to an ADE account, with flags --status --text, --headless for SSH device flow, and --no-login for local/LAN-only service setup. -- evidence: [README.md#L157-L157](https://github.com/arul28/ADE/blob/4e14f9cdf0e4825445b343f95823ddbbe3029544/README.md#L157-L157), [README.md#L161-L166](https://github.com/arul28/ADE/blob/4e14f9cdf0e4825445b343f95823ddbbe3029544/README.md#L161-L166) (`clm_51b6229c10720b1fa2bc44b7ab902b8ad05ad60aa405094e14644448b7a9e599`)
- [observation/documented] The installer supports overrides including ADE_VERSION, ADE_INSTALL_DIR, ADE_HOME, ADE_INSTALL_NO_PATH, and ADE_INSTALL_NO_PROMPT, and skips prompts when no terminal is attached. -- evidence: [README.md#L141-L141](https://github.com/arul28/ADE/blob/4e14f9cdf0e4825445b343f95823ddbbe3029544/README.md#L141-L141), [README.md#L139-L139](https://github.com/arul28/ADE/blob/4e14f9cdf0e4825445b343f95823ddbbe3029544/README.md#L139-L139) (`clm_702a2f27ac3b1c92b23ba7a3bb13943dec811f47852df38e914cc057f7afd860`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (1 claim(s))

- [observation/documented] Mobile connections prefer LAN, then Tailscale, falling back to ADE's own relay service; without an account, pairing is possible via QR/link, LAN/Tailscale scan, or SSH. -- evidence: [README.md#L151-L151](https://github.com/arul28/ADE/blob/4e14f9cdf0e4825445b343f95823ddbbe3029544/README.md#L151-L151) (`clm_b674c37448cbbdfc81ad60e44f7457796b14d5e5a754a210e102d627394e1c4a`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The project is licensed AGPL-3.0, while the @ade-dev/sdk and @ade-dev/chat-ui npm packages are MIT and an ADE Runtime Embedding Exception covers shipping the runtime binary. -- evidence: [README.md#L222-L222](https://github.com/arul28/ADE/blob/4e14f9cdf0e4825445b343f95823ddbbe3029544/README.md#L222-L222), [README.md#L224-L224](https://github.com/arul28/ADE/blob/4e14f9cdf0e4825445b343f95823ddbbe3029544/README.md#L224-L224) (`clm_012ba13d2f4d1fd053e2a4741a45e129204ae2293fcd2b9c4dd13c9dbf1aecc8`)

## limitations (1 claim(s))

- [observation/documented] There is no Linux desktop app yet; Linux can run only the Brain, and the Windows desktop app is beta with some macOS features unavailable and ARM64 unsupported. -- evidence: [README.md#L109-L109](https://github.com/arul28/ADE/blob/4e14f9cdf0e4825445b343f95823ddbbe3029544/README.md#L109-L109), [README.md#L127-L127](https://github.com/arul28/ADE/blob/4e14f9cdf0e4825445b343f95823ddbbe3029544/README.md#L127-L127), [README.md#L121-L121](https://github.com/arul28/ADE/blob/4e14f9cdf0e4825445b343f95823ddbbe3029544/README.md#L121-L121), [README.md#L119-L119](https://github.com/arul28/ADE/blob/4e14f9cdf0e4825445b343f95823ddbbe3029544/README.md#L119-L119) (`clm_319c7100f3669aad8b19cc32ec4f3bfb641c3040da6efacc725033c7c684e915`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

