# longngn204/local-coding-agent -- full detail

[Back to orientation](local-coding-agent.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/longngn204/local-coding-agent/95144e610ddcc3bb5a879117803907c008b1a88e/0ba6128836bbd797.json](../../../wiki/dossiers/longngn204/local-coding-agent/95144e610ddcc3bb5a879117803907c008b1a88e/0ba6128836bbd797.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] An Electron tray app for Windows and macOS acts as a GUI supervisor for the same local server and tunnel, storing secrets with Windows DPAPI or macOS Keychain. -- evidence: [README.md#L245-L246](https://github.com/LongNgn204/local-coding-agent/blob/95144e610ddcc3bb5a879117803907c008b1a88e/README.md#L245-L246) (`clm_2d672b780cbd6dc2dfce77fb59f27ff545a3a5ab58ade77206ce54ee431258c8`)
- [observation/documented] Shipped helper scripts include local-coding-agent.mjs (prompt/setup-wizard/skills doctor), network-doctor.mjs, and support-report.mjs, which writes a redacted support-report.txt without keys or tokens. -- evidence: [README.md#L73-L81](https://github.com/LongNgn204/local-coding-agent/blob/95144e610ddcc3bb5a879117803907c008b1a88e/README.md#L73-L81), [README.md#L291-L293](https://github.com/LongNgn204/local-coding-agent/blob/95144e610ddcc3bb5a879117803907c008b1a88e/README.md#L291-L293), [README.md#L306-L309](https://github.com/LongNgn204/local-coding-agent/blob/95144e610ddcc3bb5a879117803907c008b1a88e/README.md#L306-L309), [README.md#L311-L314](https://github.com/LongNgn204/local-coding-agent/blob/95144e610ddcc3bb5a879117803907c008b1a88e/README.md#L311-L314) (`clm_af807de68fb2f81d33ce10fe4db442f60accc29a0e124251de1729090c4cae7a`)

## design-choices (2 claim(s))

- [observation/documented] Recommended safety defaults are AGENT_MODE=safe, AGENT_POLICY=balanced, and DASHBOARD_PORT=8790; file tools are confined to configured workspace roots and risky actions require local approval under balanced policy. -- evidence: [README.md#L397-L403](https://github.com/LongNgn204/local-coding-agent/blob/95144e610ddcc3bb5a879117803907c008b1a88e/README.md#L397-L403), [README.md#L389-L393](https://github.com/LongNgn204/local-coding-agent/blob/95144e610ddcc3bb5a879117803907c008b1a88e/README.md#L389-L393) (`clm_b6001a12496929674c33d85d51307cafcf0836a238c92edd75a8968d7841a6b7`)
- [observation/documented] Since v4.4.3, default tool outputs are kept small (tighter read_file/run_command output, smaller read_many batch caps) to reduce ChatGPT Web lag, with per-call parameters like max_chars and head_lines to raise limits. -- evidence: [README.md#L318-L320](https://github.com/LongNgn204/local-coding-agent/blob/95144e610ddcc3bb5a879117803907c008b1a88e/README.md#L318-L320), [README.md#L322-L331](https://github.com/LongNgn204/local-coding-agent/blob/95144e610ddcc3bb5a879117803907c008b1a88e/README.md#L322-L331) (`clm_07e0271147c8c75f6824a20937b4c70c82c77cf3c5f074596abbac3fe8802acd`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: server tests run from the server directory via npm run test:agent, test:pro, test:security, test:hardening, and npm run eval; the tray app builds with dotnet build. -- evidence: [README.md#L434-L437](https://github.com/LongNgn204/local-coding-agent/blob/95144e610ddcc3bb5a879117803907c008b1a88e/README.md#L434-L437), [README.md#L423-L430](https://github.com/LongNgn204/local-coding-agent/blob/95144e610ddcc3bb5a879117803907c008b1a88e/README.md#L423-L430) (`clm_7b1100b6207b80961552b6cafa826975ebaf8573009a1fc501124bbba1b1dc9b`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The product runs a local MCP server at http://127.0.0.1:8787/mcp, with a /healthz health endpoint and a dashboard at http://127.0.0.1:8790/ui. -- evidence: [README.md#L97-L98](https://github.com/LongNgn204/local-coding-agent/blob/95144e610ddcc3bb5a879117803907c008b1a88e/README.md#L97-L98), [README.md#L407-L417](https://github.com/LongNgn204/local-coding-agent/blob/95144e610ddcc3bb5a879117803907c008b1a88e/README.md#L407-L417), [README.md#L280-L281](https://github.com/LongNgn204/local-coding-agent/blob/95144e610ddcc3bb5a879117803907c008b1a88e/README.md#L280-L281) (`clm_89579bb0a3b7e75dfbf98f5c07f2a9fe61367af88859ad0add90cc312b958728`)
- [observation/documented] The MCP tool surface includes workspace tools (workspace_info, workspace_snapshot, repo_map), file tools (read_file, write_file, apply_patch), search, command execution, git, and approval tools such as request_approval. -- evidence: [README.md#L364-L376](https://github.com/LongNgn204/local-coding-agent/blob/95144e610ddcc3bb5a879117803907c008b1a88e/README.md#L364-L376) (`clm_fc73aadc7a904f5079a9bb70230080f4a80b0837598ad3805945390ca30dd5ad`)
- [observation/documented] A CLI (scripts/lca) offers install/setup/start lifecycle commands plus status, doctor, update, skills, open, stop, logs, and url subcommands. -- evidence: [README.md#L232-L241](https://github.com/LongNgn204/local-coding-agent/blob/95144e610ddcc3bb5a879117803907c008b1a88e/README.md#L232-L241), [README.md#L206-L212](https://github.com/LongNgn204/local-coding-agent/blob/95144e610ddcc3bb5a879117803907c008b1a88e/README.md#L206-L212) (`clm_4aed66098a4dceab0d94a3238a002c95c66a500a0d4a01f9802c970f3f512325`)

## memory-state (1 claim(s))

- [observation/documented] compact_context stores a local structured checkpoint (goal, decisions, tasks, git state) under server/data/ with best-effort credential redaction, and resume_context loads it in a fresh chat. -- evidence: [README.md#L356-L360](https://github.com/LongNgn204/local-coding-agent/blob/95144e610ddcc3bb5a879117803907c008b1a88e/README.md#L356-L360), [README.md#L342-L347](https://github.com/LongNgn204/local-coding-agent/blob/95144e610ddcc3bb5a879117803907c008b1a88e/README.md#L342-L347) (`clm_64d622a49b09798748c876e8da5bd7862de3802f9dbf1c746d9383af55607964`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The project requires Node.js >= 18, and the proprietary tunnel client is user-supplied rather than bundled in releases. -- evidence: [README.md#L10-L18](https://github.com/LongNgn204/local-coding-agent/blob/95144e610ddcc3bb5a879117803907c008b1a88e/README.md#L10-L18), [README.md#L47-L54](https://github.com/LongNgn204/local-coding-agent/blob/95144e610ddcc3bb5a879117803907c008b1a88e/README.md#L47-L54) (`clm_4816bb6f39271ce632c9df6825326e4c2271d3181868f044e170fd734540184f`)

## limitations (2 claim(s))

- [observation/documented] The tool can run commands on the host and is explicitly not an OS sandbox; the README advises connecting only trusted workspaces and using a VM/container for untrusted repositories. -- evidence: [README.md#L397-L403](https://github.com/LongNgn204/local-coding-agent/blob/95144e610ddcc3bb5a879117803907c008b1a88e/README.md#L397-L403), [README.md#L37-L38](https://github.com/LongNgn204/local-coding-agent/blob/95144e610ddcc3bb5a879117803907c008b1a88e/README.md#L37-L38) (`clm_fe9793973a4e6b5921fcdfd551c1e2ee7adb2aaf4c9203dc8075137b0c513aef`)
- [observation/documented] The agent cannot read or replace ChatGPT Web's internal context window; it only estimates MCP tool-traffic pressure, not actual token or context-window usage. -- evidence: [README.md#L339-L340](https://github.com/LongNgn204/local-coding-agent/blob/95144e610ddcc3bb5a879117803907c008b1a88e/README.md#L339-L340), [README.md#L356-L360](https://github.com/LongNgn204/local-coding-agent/blob/95144e610ddcc3bb5a879117803907c008b1a88e/README.md#L356-L360) (`clm_35146fba8236a8e469ca6b2745b58a22746d95c2fa20eed48bcd94d1215741c4`)

## relevance (1 claim(s))

- [observation/documented] The project turns a machine into a local MCP coding workspace for AI agents (Claude Code, Codex, Cursor, ChatGPT Web), licensed AGPL-3.0-or-later as a Community Edition; the latest stable release is v5.0.1. -- evidence: [README.md#L7-L8](https://github.com/LongNgn204/local-coding-agent/blob/95144e610ddcc3bb5a879117803907c008b1a88e/README.md#L7-L8), [README.md#L20-L25](https://github.com/LongNgn204/local-coding-agent/blob/95144e610ddcc3bb5a879117803907c008b1a88e/README.md#L20-L25), [README.md#L40-L43](https://github.com/LongNgn204/local-coding-agent/blob/95144e610ddcc3bb5a879117803907c008b1a88e/README.md#L40-L43), [README.md#L441-L443](https://github.com/LongNgn204/local-coding-agent/blob/95144e610ddcc3bb5a879117803907c008b1a88e/README.md#L441-L443) (`clm_437f2da30ba5cd49970f41a3ede7b033354b906c8fa17402c4d7c4eaca0f8057`)

