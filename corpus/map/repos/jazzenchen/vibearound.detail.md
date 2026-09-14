# jazzenchen/vibearound -- full detail

[Back to orientation](vibearound.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/jazzenchen/vibearound/1654259bbb0e247b52352fa7b53221b75458e34c/7297fd70b15bc22e.json](../../../wiki/dossiers/jazzenchen/vibearound/1654259bbb0e247b52352fa7b53221b75458e34c/7297fd70b15bc22e.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (3 claim(s))

- [observation/documented] The API bridge (va-ai-api-bridge, VAAAB) translates between OpenAI Responses, OpenAI Chat Completions, Anthropic Messages, and Gemini Generate Content shapes using profile-scoped local routes and model aliases. -- evidence: [README.md#L87-L95](https://github.com/jazzenchen/VibeAround/blob/1654259bbb0e247b52352fa7b53221b75458e34c/README.md#L87-L95), [README.md#L112-L114](https://github.com/jazzenchen/VibeAround/blob/1654259bbb0e247b52352fa7b53221b75458e34c/README.md#L112-L114), [README.md#L97-L97](https://github.com/jazzenchen/VibeAround/blob/1654259bbb0e247b52352fa7b53221b75458e34c/README.md#L97-L97) (`clm_012c0acfa2d2a96a4252f3a420c3a5701412800d38a2728bb3732cc779864c41`)
- [observation/documented] Host-side web search runs through the standalone va-search-tool project, supporting Exa, Tavily, Grok/xAI, and Brave Search, and can run as a stdio plugin, CLI, or local /v1/search HTTP service. -- evidence: [README.md#L124-L124](https://github.com/jazzenchen/VibeAround/blob/1654259bbb0e247b52352fa7b53221b75458e34c/README.md#L124-L124), [README.md#L120-L120](https://github.com/jazzenchen/VibeAround/blob/1654259bbb0e247b52352fa7b53221b75458e34c/README.md#L120-L120), [README.md#L126-L130](https://github.com/jazzenchen/VibeAround/blob/1654259bbb0e247b52352fa7b53221b75458e34c/README.md#L126-L130) (`clm_4277b283b2830d281f1096d668fce2a8bedc8a3fd91cc6f63a79bd63ba7de077`)
- [observation/documented] IM integrations are built with the VibeAround Channel SDK as plugins handling platform transport (Feishu/Lark, Telegram, Slack, Discord, DingTalk, WeCom, QQ Bot, WeChat) while the SDK manages agent/session lifecycle and command bridging. -- evidence: [README.md#L165-L165](https://github.com/jazzenchen/VibeAround/blob/1654259bbb0e247b52352fa7b53221b75458e34c/README.md#L165-L165), [README.md#L161-L161](https://github.com/jazzenchen/VibeAround/blob/1654259bbb0e247b52352fa7b53221b75458e34c/README.md#L161-L161), [README.md#L305-L314](https://github.com/jazzenchen/VibeAround/blob/1654259bbb0e247b52352fa7b53221b75458e34c/README.md#L305-L314) (`clm_3e7c4f4819808ba56df8bc32963baecd7558ef189931b8fe5cb1f671703f8de7`)

## design-choices (2 claim(s))

- [observation/documented] The security model keeps execution local: the daemon listens on loopback unless a tunnel is enabled, dashboard APIs require a local auth token, tunnel owner surfaces require browser pairing, and Share links use six-digit access codes expiring after 10 minutes. -- evidence: [README.md#L323-L330](https://github.com/jazzenchen/VibeAround/blob/1654259bbb0e247b52352fa7b53221b75458e34c/README.md#L323-L330) (`clm_d007ac86fd541e6bf091960ba118303641590190959b5fdb95e03954131732f2`)
- [observation/documented] Server Share previews are a page-preview transport forwarding authenticated GET/HEAD paths only; writes, protocol upgrades, service workers, WebSockets, and HMR are unsupported, and /va/*, owner pages, chat, and review controls are excluded. -- evidence: [README.md#L323-L330](https://github.com/jazzenchen/VibeAround/blob/1654259bbb0e247b52352fa7b53221b75458e34c/README.md#L323-L330), [README.md#L253-L256](https://github.com/jazzenchen/VibeAround/blob/1654259bbb0e247b52352fa7b53221b75458e34c/README.md#L253-L256) (`clm_4614a57c5fc3f4de609d2bf9e5dda24021f8ebf4a65f4304d68174871b94802d`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: local development is done from the src directory with bun install, bun run prebuild, and bun run dev; Windows and Linux packages are built by GitHub Actions. -- evidence: [README.md#L357-L357](https://github.com/jazzenchen/VibeAround/blob/1654259bbb0e247b52352fa7b53221b75458e34c/README.md#L357-L357), [README.md#L379-L384](https://github.com/jazzenchen/VibeAround/blob/1654259bbb0e247b52352fa7b53221b75458e34c/README.md#L379-L384) (`clm_2dd820c1f9e0798d752514abbf8224cd36a220bb28ac358548c8599fe0b5fc2b`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] VibeAround exposes local agents as OpenAI/Anthropic-compatible endpoints under /local-agent/{agent_id}/{profile_id}/..., including responses, chat completions, messages, and models routes, with an x-vibearound-cwd header for workspace selection. -- evidence: [README.md#L142-L147](https://github.com/jazzenchen/VibeAround/blob/1654259bbb0e247b52352fa7b53221b75458e34c/README.md#L142-L147), [README.md#L136-L136](https://github.com/jazzenchen/VibeAround/blob/1654259bbb0e247b52352fa7b53221b75458e34c/README.md#L136-L136), [README.md#L149-L153](https://github.com/jazzenchen/VibeAround/blob/1654259bbb0e247b52352fa7b53221b75458e34c/README.md#L149-L153) (`clm_4af59fd8250cf3cd5165b25ff64deb3fbb31090423739bd5352d7e29fe15a9f4`)
- [observation/documented] The npm CLI installs both `va` and `vibearound` commands, with subcommands such as `va serve`, `va tui`, and `va launch --profile ...`. -- evidence: [README.md#L367-L371](https://github.com/jazzenchen/VibeAround/blob/1654259bbb0e247b52352fa7b53221b75458e34c/README.md#L367-L371), [README.md#L361-L361](https://github.com/jazzenchen/VibeAround/blob/1654259bbb0e247b52352fa7b53221b75458e34c/README.md#L361-L361) (`clm_d37d3c9227166aca512eeb4fdd7bb408d648d3437f52db5961a421061337069d`)
- [observation/documented] The local server listens on port 12358 by default with the dashboard at http://127.0.0.1:12358/va/, and data is stored in ~/.vibearound/, overridable via VIBEAROUND_DATA_DIR. -- evidence: [docs/README.md#L83-L87](https://github.com/jazzenchen/VibeAround/blob/1654259bbb0e247b52352fa7b53221b75458e34c/docs/README.md#L83-L87), [README.md#L373-L373](https://github.com/jazzenchen/VibeAround/blob/1654259bbb0e247b52352fa7b53221b75458e34c/README.md#L373-L373) (`clm_b519fff47466e5e7b2829c1da464f5873473f04abcd8d0add3d0cdf911122523`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (1 claim(s))

- [observation/documented] Sessions can be handed off via a generated /pickup command pasted into any connected IM channel, resuming the same agent session independent of the originating channel, with slash commands like /switch, /session, and /workspace for control. -- evidence: [README.md#L159-L159](https://github.com/jazzenchen/VibeAround/blob/1654259bbb0e247b52352fa7b53221b75458e34c/README.md#L159-L159), [README.md#L182-L194](https://github.com/jazzenchen/VibeAround/blob/1654259bbb0e247b52352fa7b53221b75458e34c/README.md#L182-L194), [README.md#L171-L177](https://github.com/jazzenchen/VibeAround/blob/1654259bbb0e247b52352fa7b53221b75458e34c/README.md#L171-L177) (`clm_0e238cfd7abd52ed56936e0081f15cc43d3398cd1c2b1bc97b779fea2f641e42`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Building locally requires Rust 1.82+, Bun 1.3+, and Node.js 24 LTS recommended, plus Xcode command line tools on macOS and WebKitGTK/Tauri system dependencies on Linux. -- evidence: [README.md#L386-L386](https://github.com/jazzenchen/VibeAround/blob/1654259bbb0e247b52352fa7b53221b75458e34c/README.md#L386-L386) (`clm_173e5d9bfd5e9b2b785b79069ef09e0f98091665da2122b16cef022d8b2d7134`)

## limitations (2 claim(s))

- [observation/documented] Per the README's own comparison table, IM file attachments are send-only (receiving files from IM is not currently supported), and scheduling and rich IM commands are listed as not currently supported. -- evidence: [README.md#L182-L194](https://github.com/jazzenchen/VibeAround/blob/1654259bbb0e247b52352fa7b53221b75458e34c/README.md#L182-L194) (`clm_9b3850621dc3e61110879e77ac50da4bae18d8e0efde61c9f2f3d641d6872b19`)
- [observation/documented] The macOS desktop package is currently Apple Silicon only, while Windows and Linux builds are produced by GitHub Actions. -- evidence: [README.md#L357-L357](https://github.com/jazzenchen/VibeAround/blob/1654259bbb0e247b52352fa7b53221b75458e34c/README.md#L357-L357) (`clm_e86f8916ad0e7baa3048f7db44dae71a9b65297770ceab9dbb67358fbad93df5`)

## relevance (1 claim(s))

- [observation/documented] VibeAround targets developers who use AI coding agents (Claude Code, Codex CLI, Gemini CLI, Pi, OpenCode, desktop variants) and want one local hub for launching, API bridging, remote messaging, and browser-based session continuation. -- evidence: [README.md#L40-L40](https://github.com/jazzenchen/VibeAround/blob/1654259bbb0e247b52352fa7b53221b75458e34c/README.md#L40-L40), [README.md#L28-L34](https://github.com/jazzenchen/VibeAround/blob/1654259bbb0e247b52352fa7b53221b75458e34c/README.md#L28-L34), [README.md#L216-L216](https://github.com/jazzenchen/VibeAround/blob/1654259bbb0e247b52352fa7b53221b75458e34c/README.md#L216-L216) (`clm_62766b376ed05a92eb9f9fc43f0742bfcb9a8eaaded50dfada6aa0e9dd94e7d7`)

