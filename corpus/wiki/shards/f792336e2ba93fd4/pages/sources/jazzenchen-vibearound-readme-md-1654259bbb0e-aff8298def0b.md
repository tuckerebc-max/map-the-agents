---
access: public
aliases: []
claim_ids:
- clm_012c0acfa2d2a96a4252f3a420c3a5701412800d38a2728bb3732cc779864c41
- clm_0e238cfd7abd52ed56936e0081f15cc43d3398cd1c2b1bc97b779fea2f641e42
- clm_173e5d9bfd5e9b2b785b79069ef09e0f98091665da2122b16cef022d8b2d7134
- clm_2dd820c1f9e0798d752514abbf8224cd36a220bb28ac358548c8599fe0b5fc2b
- clm_3e7c4f4819808ba56df8bc32963baecd7558ef189931b8fe5cb1f671703f8de7
- clm_4277b283b2830d281f1096d668fce2a8bedc8a3fd91cc6f63a79bd63ba7de077
- clm_4614a57c5fc3f4de609d2bf9e5dda24021f8ebf4a65f4304d68174871b94802d
- clm_4af59fd8250cf3cd5165b25ff64deb3fbb31090423739bd5352d7e29fe15a9f4
- clm_62766b376ed05a92eb9f9fc43f0742bfcb9a8eaaded50dfada6aa0e9dd94e7d7
- clm_9b3850621dc3e61110879e77ac50da4bae18d8e0efde61c9f2f3d641d6872b19
- clm_b519fff47466e5e7b2829c1da464f5873473f04abcd8d0add3d0cdf911122523
- clm_d007ac86fd541e6bf091960ba118303641590190959b5fdb95e03954131732f2
- clm_d37d3c9227166aca512eeb4fdd7bb408d648d3437f52db5961a421061337069d
- clm_e86f8916ad0e7baa3048f7db44dae71a9b65297770ceab9dbb67358fbad93df5
maturity: draft
page_id: pg_314066a209605bd2ab04aff8298def0b
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_5e999787ca46511d963ca966bf7cfadc
title: jazzenchen/VibeAround/README.md @ 1654259bbb0e
updated_at: '2026-09-14T02:07:07Z'
---

# jazzenchen/VibeAround/README.md @ 1654259bbb0e

<!-- rcw:begin owner=source:src_5e999787ca46511d963ca966bf7cfadc block=evidence -->
- The API bridge (va-ai-api-bridge, VAAAB) translates between OpenAI Responses, OpenAI Chat Completions, Anthropic Messages, and Gemini Generate Content shapes using profile-scoped local routes and model aliases. [@claim:clm_012c0acfa2d2a96a4252f3a420c3a5701412800d38a2728bb3732cc779864c41]
- Sessions can be handed off via a generated /pickup command pasted into any connected IM channel, resuming the same agent session independent of the originating channel, with slash commands like /switch, /session, and /workspace for control. [@claim:clm_0e238cfd7abd52ed56936e0081f15cc43d3398cd1c2b1bc97b779fea2f641e42]
- Building locally requires Rust 1.82+, Bun 1.3+, and Node.js 24 LTS recommended, plus Xcode command line tools on macOS and WebKitGTK/Tauri system dependencies on Linux. [@claim:clm_173e5d9bfd5e9b2b785b79069ef09e0f98091665da2122b16cef022d8b2d7134]
- Repository development practice: local development is done from the src directory with bun install, bun run prebuild, and bun run dev; Windows and Linux packages are built by GitHub Actions. [@claim:clm_2dd820c1f9e0798d752514abbf8224cd36a220bb28ac358548c8599fe0b5fc2b]
- IM integrations are built with the VibeAround Channel SDK as plugins handling platform transport (Feishu/Lark, Telegram, Slack, Discord, DingTalk, WeCom, QQ Bot, WeChat) while the SDK manages agent/session lifecycle and command bridging. [@claim:clm_3e7c4f4819808ba56df8bc32963baecd7558ef189931b8fe5cb1f671703f8de7]
- Host-side web search runs through the standalone va-search-tool project, supporting Exa, Tavily, Grok/xAI, and Brave Search, and can run as a stdio plugin, CLI, or local /v1/search HTTP service. [@claim:clm_4277b283b2830d281f1096d668fce2a8bedc8a3fd91cc6f63a79bd63ba7de077]
- Server Share previews are a page-preview transport forwarding authenticated GET/HEAD paths only; writes, protocol upgrades, service workers, WebSockets, and HMR are unsupported, and /va/*, owner pages, chat, and review controls are excluded. [@claim:clm_4614a57c5fc3f4de609d2bf9e5dda24021f8ebf4a65f4304d68174871b94802d]
- VibeAround exposes local agents as OpenAI/Anthropic-compatible endpoints under /local-agent/{agent_id}/{profile_id}/..., including responses, chat completions, messages, and models routes, with an x-vibearound-cwd header for workspace selection. [@claim:clm_4af59fd8250cf3cd5165b25ff64deb3fbb31090423739bd5352d7e29fe15a9f4]
- VibeAround targets developers who use AI coding agents (Claude Code, Codex CLI, Gemini CLI, Pi, OpenCode, desktop variants) and want one local hub for launching, API bridging, remote messaging, and browser-based session continuation. [@claim:clm_62766b376ed05a92eb9f9fc43f0742bfcb9a8eaaded50dfada6aa0e9dd94e7d7]
- Per the README's own comparison table, IM file attachments are send-only (receiving files from IM is not currently supported), and scheduling and rich IM commands are listed as not currently supported. [@claim:clm_9b3850621dc3e61110879e77ac50da4bae18d8e0efde61c9f2f3d641d6872b19]
- The local server listens on port 12358 by default with the dashboard at http://127.0.0.1:12358/va/, and data is stored in ~/.vibearound/, overridable via VIBEAROUND_DATA_DIR. [@claim:clm_b519fff47466e5e7b2829c1da464f5873473f04abcd8d0add3d0cdf911122523]
- The security model keeps execution local: the daemon listens on loopback unless a tunnel is enabled, dashboard APIs require a local auth token, tunnel owner surfaces require browser pairing, and Share links use six-digit access codes expiring after 10 minutes. [@claim:clm_d007ac86fd541e6bf091960ba118303641590190959b5fdb95e03954131732f2]
- The npm CLI installs both `va` and `vibearound` commands, with subcommands such as `va serve`, `va tui`, and `va launch --profile ...`. [@claim:clm_d37d3c9227166aca512eeb4fdd7bb408d648d3437f52db5961a421061337069d]
- The macOS desktop package is currently Apple Silicon only, while Windows and Linux builds are produced by GitHub Actions. [@claim:clm_e86f8916ad0e7baa3048f7db44dae71a9b65297770ceab9dbb67358fbad93df5]
<!-- rcw:end owner=source:src_5e999787ca46511d963ca966bf7cfadc block=evidence -->

## Researcher notes

