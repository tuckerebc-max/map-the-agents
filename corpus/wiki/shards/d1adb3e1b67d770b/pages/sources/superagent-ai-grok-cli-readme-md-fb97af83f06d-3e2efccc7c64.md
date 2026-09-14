---
access: public
aliases: []
claim_ids:
- clm_03829a4f3259cf090343119f6ccc36de4346e472ebe32899a8c0cdce55a8e2f9
- clm_06e3f87ab4cfbb15482aa1a7e4428ba0404b412939af7feec403441a6b643dee
- clm_0aa93efb84d3bf0fa4dfed75245f69da5d7283d3e2222d541d46879e2e9b0fa4
- clm_2fe4d29e3e097ed3063fbc08ddd6b6089157047a84bd0299b414f710f0da48e6
- clm_43d4ab2ca7cca9133f6b1336c5f7bec116c65db73f6ffb10d352e89e0fa29002
- clm_59ac30e9da55799033c86a6b84113b6ffaf04133479b294c6db16b3c107de8e7
- clm_5b55ebd2e3523c0ed4f8a89e25e7d7b4c68ff97c5f2b654efcf0840d0b2e89d8
- clm_6df113290d79359c52fe6f4d5675c654ec59ba34655f844ab79bc110b228973d
- clm_720eadb3d73bff0c01e74aff78010d7cfb6f96e61e5d1eced3b77b3aa8ad18d3
- clm_772592f622254d3f4d5f65a72eeb45a5afec243c0df5f6bc01aa05c8bbb1dff9
- clm_8dd8f3b871e79ebd3edf1dafa5c326d4a5f07da3101c0a21288d8c2b8d4bc3a4
- clm_95fdb205625ec2c164299ab0a7129d382c7d6c533b3618ba11aabd1a47ccd2a1
- clm_983d49c4d23c0e452aa3a1b851fb0c8216284d5325f60094bf0b319aa7efc534
- clm_b3ed30d868d173884f8d1bb456f80f6f165ff808c942fb7593d486db908b0f74
- clm_c50665aa9b9eba0243af54593c33f130f0370d9e3ec11bb79190f1e9afcc7b78
- clm_c78e122b4b492ec65e39bd9ee0129cfe52b00171e12e9f7fb97026009a7dda36
- clm_dc26bcb2246c560dccc8b066609a697f31df1ee359b5792679e3a7c158872ae2
maturity: draft
page_id: pg_e5da6ade06fa5108b7b53e2efccc7c64
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_8c0f030103a05f6a8219658194ab69bd
title: superagent-ai/grok-cli/README.md @ fb97af83f06d
updated_at: '2026-09-14T03:16:02Z'
---

# superagent-ai/grok-cli/README.md @ fb97af83f06d

<!-- rcw:begin owner=source:src_8c0f030103a05f6a8219658194ab69bd block=evidence -->
- Supported hook events include PreToolUse, PostToolUse, PostToolUseFailure, UserPromptSubmit, SessionStart/End, Stop, SubagentStart/Stop, TaskCreated/Completed, PreCompact/PostCompact, Notification, InstructionsLoaded, and CwdChanged. [@claim:clm_03829a4f3259cf090343119f6ccc36de4346e472ebe32899a8c0cdce55a8e2f9]
- Telegram remote control pairs a bot via /pair with a 6-character code; long polling lives in the CLI process, which must keep running, and a headless 'grok telegram-bridge' flow exists. [@claim:clm_06e3f87ab4cfbb15482aa1a7e4428ba0404b412939af7feec403441a6b643dee]
- Telegram voice notes are transcribed via xAI's Grok Speech-to-Text endpoint (/v1/stt), which replaced whisper.cpp and removed local whisper-cli, ffmpeg, and model-download requirements. [@claim:clm_0aa93efb84d3bf0fa4dfed75245f69da5d7283d3e2222d541d46879e2e9b0fa4]
- A built-in computer sub-agent backed by agent-desktop performs host desktop automation on macOS via a snapshot-refs-action-snapshot workflow with tools like computer_snapshot, computer_click, computer_type, and computer_scroll; screenshots default to .grok/computer/. [@claim:clm_2fe4d29e3e097ed3063fbc08ddd6b6089157047a84bd0299b414f710f0da48e6]
- Built-in tools include search_x and search_web for live X/web search and generate_image/generate_video for media generation, with generated files saved locally under .grok/generated-media/ by default. [@claim:clm_43d4ab2ca7cca9133f6b1336c5f7bec116c65db73f6ffb10d352e89e0fa29002]
- The tool is built with TypeScript and Bun with an OpenTUI terminal UI, installs via a curl install script or 'bun add -g grok-dev', and the computer sub-agent depends on the agent-desktop package. [@claim:clm_59ac30e9da55799033c86a6b84113b6ffaf04133479b294c6db16b3c107de8e7]
- Sessions can be resumed with 'grok --session latest' or 'grok -s <session-id>' (also in interactive mode), and /compact in the TUI compresses accumulated conversation history. [@claim:clm_5b55ebd2e3523c0ed4f8a89e25e7d7b4c68ff97c5f2b654efcf0840d0b2e89d8]
- Sub-agents are on by default: foreground task delegation (e.g. explore, general, computer) plus background delegate for read-only deep dives. [@claim:clm_6df113290d79359c52fe6f4d5675c654ec59ba34655f844ab79bc110b228973d]
- The CLI supports headless runs via --prompt with options such as --directory, --max-tool-rounds, --format json, --batch-api, and --verify, plus session resume via --session latest or -s <session-id>. [@claim:clm_720eadb3d73bff0c01e74aff78010d7cfb6f96e61e5d1eced3b77b3aa8ad18d3]
- With --format json, headless output becomes a newline-delimited JSON event stream of semantic step-level events such as step_start, text, tool_use, step_finish, and error. [@claim:clm_772592f622254d3f4d5f65a72eeb45a5afec243c0df5f6bc01aa05c8bbb1dff9]
- Hooks run shell commands at agent lifecycle events; they receive JSON on stdin, may return JSON on stdout, and exit code 2 blocks the action while 0 means success and other codes are non-blocking errors. [@claim:clm_8dd8f3b871e79ebd3edf1dafa5c326d4a5f07da3101c0a21288d8c2b8d4bc3a4]
- Sandbox mode requires macOS 14+ on Apple Silicon and is unavailable on Intel Macs or Linux, per the troubleshooting section. [@claim:clm_95fdb205625ec2c164299ab0a7129d382c7d6c533b3618ba11aabd1a47ccd2a1]
- AGENTS.md instruction files are merged from the git root down to the working directory, with AGENTS.override.md taking precedence per directory when present. [@claim:clm_983d49c4d23c0e452aa3a1b851fb0c8216284d5325f60094bf0b319aa7efc534]
- Shell commands can run inside a Shuru microVM sandbox (--sandbox or /sandbox) isolating host filesystem and network; network is off by default with --allow-net/--allow-host controls, plus port forwards, resource limits, checkpoints, and secret injection. [@claim:clm_b3ed30d868d173884f8d1bb456f80f6f165ff808c942fb7593d486db908b0f74]
- The project is community-built, open-source, MIT-licensed, and explicitly not affiliated with or endorsed by xAI Corp, using the publicly available Grok API. [@claim:clm_c50665aa9b9eba0243af54593c33f130f0370d9e3ec11bb79190f1e9afcc7b78]
- Custom sub-agents can be defined in user settings with name, model, and instruction; the names general, explore, vision, verify, and computer are reserved for built-in sub-agents. [@claim:clm_c78e122b4b492ec65e39bd9ee0129cfe52b00171e12e9f7fb97026009a7dda36]
- No agent-performance benchmark or scored eval harness appears in the provided evidence; the --verify command produces build/run verification reports with screenshots and video, which is a runtime feature rather than a scored evaluation. [@claim:clm_dc26bcb2246c560dccc8b066609a697f31df1ee359b5792679e3a7c158872ae2]
<!-- rcw:end owner=source:src_8c0f030103a05f6a8219658194ab69bd block=evidence -->

## Researcher notes

