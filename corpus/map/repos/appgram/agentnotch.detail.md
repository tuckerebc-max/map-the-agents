# appgram/agentnotch -- full detail

[Back to orientation](agentnotch.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/appgram/agentnotch/4139d6fd7b90a060b90b17ed20e0878b0641cc1a/e12631ac6603de96.json](../../../wiki/dossiers/appgram/agentnotch/4139d6fd7b90a060b90b17ed20e0878b0641cc1a/e12631ac6603de96.json)

## specifications (1 claim(s))

- [observation/documented] Requires macOS 14.0 (Sonoma) or later; on non-notch Macs the app falls back to the menu bar. -- evidence: [README.md#L114-L115](https://github.com/AppGram/agentnotch/blob/4139d6fd7b90a060b90b17ed20e0878b0641cc1a/README.md#L114-L115) (`clm_858c27e5d26e29cb26e3c4d4e3d6b4447c406d960950758b337e6c5540a1110f`)

## components (3 claim(s))

- [observation/documented] AgentNotch is a macOS menu bar app that lives in the Mac's notch and shows real-time telemetry from Claude Code and OpenAI Codex sessions. -- evidence: [README.md#L23-L23](https://github.com/AppGram/agentnotch/blob/4139d6fd7b90a060b90b17ed20e0878b0641cc1a/README.md#L23-L23) (`clm_93ad087c73b2e4ad0a0cd26fb337fca4c976d96032103c0c18a572db6bb38876`)
- [observation/documented] The app displays each tool call as it happens, including file reads, code edits, and shell commands. -- evidence: [README.md#L28-L28](https://github.com/AppGram/agentnotch/blob/4139d6fd7b90a060b90b17ed20e0878b0641cc1a/README.md#L28-L28) (`clm_a513571ac9ce6d547062ef3a2b07ce169155c377278a04ae9f70bc1c4480a311`)
- [observation/documented] It tracks input/output token usage and estimated costs in real time, and notifies the user when an assistant finishes a task. -- evidence: [README.md#L41-L41](https://github.com/AppGram/agentnotch/blob/4139d6fd7b90a060b90b17ed20e0878b0641cc1a/README.md#L41-L41), [README.md#L31-L31](https://github.com/AppGram/agentnotch/blob/4139d6fd7b90a060b90b17ed20e0878b0641cc1a/README.md#L31-L31) (`clm_817ed53aec442a58714f7809a1982bd928b90ae8b76ae159ec9985a691910376`)

## design-choices (3 claim(s))

- [observation/documented] Source-aware color coding distinguishes assistants: orange for Claude Code, blue for Codex, and light blue for unknown sources. -- evidence: [README.md#L34-L36](https://github.com/AppGram/agentnotch/blob/4139d6fd7b90a060b90b17ed20e0878b0641cc1a/README.md#L34-L36), [README.md#L38-L38](https://github.com/AppGram/agentnotch/blob/4139d6fd7b90a060b90b17ed20e0878b0641cc1a/README.md#L38-L38) (`clm_8a740c83509cc83ddad02d3cc4c7c93bf976ef69764cc9532c1807e8aa04c948`)
- [observation/documented] Display is configurable: token counts, cost estimates, source filtering (Claude/Codex), and the menu bar icon can be toggled. -- evidence: [README.md#L49-L52](https://github.com/AppGram/agentnotch/blob/4139d6fd7b90a060b90b17ed20e0878b0641cc1a/README.md#L49-L52) (`clm_ab84cdaf8beb71041bc73008cf0edf9a15af49b68c46d92ce04bdf6ce5db281e`)
- [observation/documented] The app runs entirely locally, sending no data anywhere; it only receives telemetry from local AI tools. -- evidence: [README.md#L119-L119](https://github.com/AppGram/agentnotch/blob/4139d6fd7b90a060b90b17ed20e0878b0641cc1a/README.md#L119-L119) (`clm_9204fe28077a4be0046b5a92615e3333a50b4c1a3b2ae648c3efb5b1c9a86113`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: the contributor guide documents a release process of building in Xcode, zipping the app, computing SHA256, updating the cask formula, and pushing to the homebrew-tap repo. -- evidence: [CLAUDE.md#L166-L172](https://github.com/AppGram/agentnotch/blob/4139d6fd7b90a060b90b17ed20e0878b0641cc1a/CLAUDE.md#L166-L172), [CLAUDE.md#L163-L163](https://github.com/AppGram/agentnotch/blob/4139d6fd7b90a060b90b17ed20e0878b0641cc1a/CLAUDE.md#L163-L163) (`clm_6aa72c9582f500a9436bcf8e842a8eb53754a1ba38094e5326c9c3d31a27d70f`)
- [observation/documented] Repository development practice: debug logging is wrapped in a debugLog() helper that only prints in DEBUG builds. -- evidence: [CLAUDE.md#L100-L108](https://github.com/AppGram/agentnotch/blob/4139d6fd7b90a060b90b17ed20e0878b0641cc1a/CLAUDE.md#L100-L108) (`clm_2812815787e0edf57f3642892676b028772f292269b68362c05397c36a956f55`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] AgentNotch listens for OTLP/HTTP on port 4318 by default and decodes OTLP logs (/v1/logs) and metrics (/v1/metrics). -- evidence: [README.md#L82-L82](https://github.com/AppGram/agentnotch/blob/4139d6fd7b90a060b90b17ed20e0878b0641cc1a/README.md#L82-L82) (`clm_c83d00eb55f0b673b43970a6c098112d6538d80890a19b311a9a38d7d4cb9b8b`)
- [observation/documented] Interaction model: the notch indicator expands on hover to show recent tool calls, and clicking opens a full view with token breakdown and settings. -- evidence: [README.md#L101-L104](https://github.com/AppGram/agentnotch/blob/4139d6fd7b90a060b90b17ed20e0878b0641cc1a/README.md#L101-L104), [README.md#L44-L46](https://github.com/AppGram/agentnotch/blob/4139d6fd7b90a060b90b17ed20e0878b0641cc1a/README.md#L44-L46) (`clm_9c4de1b06419279be53299c021ceabf2edfb1c31eff7aec211a835f19d8969ac`)

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

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

