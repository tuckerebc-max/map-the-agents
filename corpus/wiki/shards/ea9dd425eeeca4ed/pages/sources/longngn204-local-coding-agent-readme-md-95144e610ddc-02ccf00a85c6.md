---
access: public
aliases: []
claim_ids:
- clm_07e0271147c8c75f6824a20937b4c70c82c77cf3c5f074596abbac3fe8802acd
- clm_2d672b780cbd6dc2dfce77fb59f27ff545a3a5ab58ade77206ce54ee431258c8
- clm_35146fba8236a8e469ca6b2745b58a22746d95c2fa20eed48bcd94d1215741c4
- clm_437f2da30ba5cd49970f41a3ede7b033354b906c8fa17402c4d7c4eaca0f8057
- clm_4816bb6f39271ce632c9df6825326e4c2271d3181868f044e170fd734540184f
- clm_4aed66098a4dceab0d94a3238a002c95c66a500a0d4a01f9802c970f3f512325
- clm_64d622a49b09798748c876e8da5bd7862de3802f9dbf1c746d9383af55607964
- clm_7b1100b6207b80961552b6cafa826975ebaf8573009a1fc501124bbba1b1dc9b
- clm_89579bb0a3b7e75dfbf98f5c07f2a9fe61367af88859ad0add90cc312b958728
- clm_af807de68fb2f81d33ce10fe4db442f60accc29a0e124251de1729090c4cae7a
- clm_b6001a12496929674c33d85d51307cafcf0836a238c92edd75a8968d7841a6b7
- clm_fc73aadc7a904f5079a9bb70230080f4a80b0837598ad3805945390ca30dd5ad
- clm_fe9793973a4e6b5921fcdfd551c1e2ee7adb2aaf4c9203dc8075137b0c513aef
maturity: draft
page_id: pg_04cfdc9de28f5302b63e02ccf00a85c6
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_dd0ab0ca85d75acb8744477fe085cd7e
title: LongNgn204/local-coding-agent/README.md @ 95144e610ddc
updated_at: '2026-09-14T04:07:16Z'
---

# LongNgn204/local-coding-agent/README.md @ 95144e610ddc

<!-- rcw:begin owner=source:src_dd0ab0ca85d75acb8744477fe085cd7e block=evidence -->
- Since v4.4.3, default tool outputs are kept small (tighter read_file/run_command output, smaller read_many batch caps) to reduce ChatGPT Web lag, with per-call parameters like max_chars and head_lines to raise limits. [@claim:clm_07e0271147c8c75f6824a20937b4c70c82c77cf3c5f074596abbac3fe8802acd]
- An Electron tray app for Windows and macOS acts as a GUI supervisor for the same local server and tunnel, storing secrets with Windows DPAPI or macOS Keychain. [@claim:clm_2d672b780cbd6dc2dfce77fb59f27ff545a3a5ab58ade77206ce54ee431258c8]
- The agent cannot read or replace ChatGPT Web's internal context window; it only estimates MCP tool-traffic pressure, not actual token or context-window usage. [@claim:clm_35146fba8236a8e469ca6b2745b58a22746d95c2fa20eed48bcd94d1215741c4]
- The project turns a machine into a local MCP coding workspace for AI agents (Claude Code, Codex, Cursor, ChatGPT Web), licensed AGPL-3.0-or-later as a Community Edition; the latest stable release is v5.0.1. [@claim:clm_437f2da30ba5cd49970f41a3ede7b033354b906c8fa17402c4d7c4eaca0f8057]
- The project requires Node.js >= 18, and the proprietary tunnel client is user-supplied rather than bundled in releases. [@claim:clm_4816bb6f39271ce632c9df6825326e4c2271d3181868f044e170fd734540184f]
- A CLI (scripts/lca) offers install/setup/start lifecycle commands plus status, doctor, update, skills, open, stop, logs, and url subcommands. [@claim:clm_4aed66098a4dceab0d94a3238a002c95c66a500a0d4a01f9802c970f3f512325]
- compact_context stores a local structured checkpoint (goal, decisions, tasks, git state) under server/data/ with best-effort credential redaction, and resume_context loads it in a fresh chat. [@claim:clm_64d622a49b09798748c876e8da5bd7862de3802f9dbf1c746d9383af55607964]
- Repository development practice: server tests run from the server directory via npm run test:agent, test:pro, test:security, test:hardening, and npm run eval; the tray app builds with dotnet build. [@claim:clm_7b1100b6207b80961552b6cafa826975ebaf8573009a1fc501124bbba1b1dc9b]
- The product runs a local MCP server at http://127.0.0.1:8787/mcp, with a /healthz health endpoint and a dashboard at http://127.0.0.1:8790/ui. [@claim:clm_89579bb0a3b7e75dfbf98f5c07f2a9fe61367af88859ad0add90cc312b958728]
- Shipped helper scripts include local-coding-agent.mjs (prompt/setup-wizard/skills doctor), network-doctor.mjs, and support-report.mjs, which writes a redacted support-report.txt without keys or tokens. [@claim:clm_af807de68fb2f81d33ce10fe4db442f60accc29a0e124251de1729090c4cae7a]
- Recommended safety defaults are AGENT_MODE=safe, AGENT_POLICY=balanced, and DASHBOARD_PORT=8790; file tools are confined to configured workspace roots and risky actions require local approval under balanced policy. [@claim:clm_b6001a12496929674c33d85d51307cafcf0836a238c92edd75a8968d7841a6b7]
- The MCP tool surface includes workspace tools (workspace_info, workspace_snapshot, repo_map), file tools (read_file, write_file, apply_patch), search, command execution, git, and approval tools such as request_approval. [@claim:clm_fc73aadc7a904f5079a9bb70230080f4a80b0837598ad3805945390ca30dd5ad]
- The tool can run commands on the host and is explicitly not an OS sandbox; the README advises connecting only trusted workspaces and using a VM/container for untrusted repositories. [@claim:clm_fe9793973a4e6b5921fcdfd551c1e2ee7adb2aaf4c9203dc8075137b0c513aef]
<!-- rcw:end owner=source:src_dd0ab0ca85d75acb8744477fe085cd7e block=evidence -->

## Researcher notes

