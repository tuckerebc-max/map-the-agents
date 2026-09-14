# superagent-ai/grok-cli -- full detail

[Back to orientation](grok-cli.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/superagent-ai/grok-cli/fb97af83f06dca873281d60168430f06c8de6324/d13dd57301adcd9f.json](../../../wiki/dossiers/superagent-ai/grok-cli/fb97af83f06dca873281d60168430f06c8de6324/d13dd57301adcd9f.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (3 claim(s))

- [observation/documented] Custom sub-agents can be defined in user settings with name, model, and instruction; the names general, explore, vision, verify, and computer are reserved for built-in sub-agents. -- evidence: [README.md#L238-L238](https://github.com/superagent-ai/grok-cli/blob/fb97af83f06dca873281d60168430f06c8de6324/README.md#L238-L238), [README.md#L226-L236](https://github.com/superagent-ai/grok-cli/blob/fb97af83f06dca873281d60168430f06c8de6324/README.md#L226-L236), [README.md#L224-L224](https://github.com/superagent-ai/grok-cli/blob/fb97af83f06dca873281d60168430f06c8de6324/README.md#L224-L224) (`clm_c78e122b4b492ec65e39bd9ee0129cfe52b00171e12e9f7fb97026009a7dda36`)
- [observation/documented] A built-in computer sub-agent backed by agent-desktop performs host desktop automation on macOS via a snapshot-refs-action-snapshot workflow with tools like computer_snapshot, computer_click, computer_type, and computer_scroll; screenshots default to .grok/computer/. -- evidence: [README.md#L114-L119](https://github.com/superagent-ai/grok-cli/blob/fb97af83f06dca873281d60168430f06c8de6324/README.md#L114-L119), [README.md#L103-L103](https://github.com/superagent-ai/grok-cli/blob/fb97af83f06dca873281d60168430f06c8de6324/README.md#L103-L103) (`clm_2fe4d29e3e097ed3063fbc08ddd6b6089157047a84bd0299b414f710f0da48e6`)
- [observation/documented] Built-in tools include search_x and search_web for live X/web search and generate_image/generate_video for media generation, with generated files saved locally under .grok/generated-media/ by default. -- evidence: [README.md#L165-L167](https://github.com/superagent-ai/grok-cli/blob/fb97af83f06dca873281d60168430f06c8de6324/README.md#L165-L167), [README.md#L174-L189](https://github.com/superagent-ai/grok-cli/blob/fb97af83f06dca873281d60168430f06c8de6324/README.md#L174-L189) (`clm_43d4ab2ca7cca9133f6b1336c5f7bec116c65db73f6ffb10d352e89e0fa29002`)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (6 claim(s))

- [observation/documented] The CLI supports headless runs via --prompt with options such as --directory, --max-tool-rounds, --format json, --batch-api, and --verify, plus session resume via --session latest or -s <session-id>. -- evidence: [README.md#L69-L76](https://github.com/superagent-ai/grok-cli/blob/fb97af83f06dca873281d60168430f06c8de6324/README.md#L69-L76), [README.md#L84-L87](https://github.com/superagent-ai/grok-cli/blob/fb97af83f06dca873281d60168430f06c8de6324/README.md#L84-L87) (`clm_720eadb3d73bff0c01e74aff78010d7cfb6f96e61e5d1eced3b77b3aa8ad18d3`)
- [observation/documented] With --format json, headless output becomes a newline-delimited JSON event stream of semantic step-level events such as step_start, text, tool_use, step_finish, and error. -- evidence: [README.md#L97-L99](https://github.com/superagent-ai/grok-cli/blob/fb97af83f06dca873281d60168430f06c8de6324/README.md#L97-L99) (`clm_772592f622254d3f4d5f65a72eeb45a5afec243c0df5f6bc01aa05c8bbb1dff9`)
- [observation/documented] Hooks run shell commands at agent lifecycle events; they receive JSON on stdin, may return JSON on stdout, and exit code 2 blocks the action while 0 means success and other codes are non-blocking errors. -- evidence: [README.md#L315-L315](https://github.com/superagent-ai/grok-cli/blob/fb97af83f06dca873281d60168430f06c8de6324/README.md#L315-L315), [README.md#L292-L292](https://github.com/superagent-ai/grok-cli/blob/fb97af83f06dca873281d60168430f06c8de6324/README.md#L292-L292) (`clm_8dd8f3b871e79ebd3edf1dafa5c326d4a5f07da3101c0a21288d8c2b8d4bc3a4`)
- [observation/documented] Supported hook events include PreToolUse, PostToolUse, PostToolUseFailure, UserPromptSubmit, SessionStart/End, Stop, SubagentStart/Stop, TaskCreated/Completed, PreCompact/PostCompact, Notification, InstructionsLoaded, and CwdChanged. -- evidence: [README.md#L317-L317](https://github.com/superagent-ai/grok-cli/blob/fb97af83f06dca873281d60168430f06c8de6324/README.md#L317-L317) (`clm_03829a4f3259cf090343119f6ccc36de4346e472ebe32899a8c0cdce55a8e2f9`)
- [observation/documented] AGENTS.md instruction files are merged from the git root down to the working directory, with AGENTS.override.md taking precedence per directory when present. -- evidence: [README.md#L323-L323](https://github.com/superagent-ai/grok-cli/blob/fb97af83f06dca873281d60168430f06c8de6324/README.md#L323-L323) (`clm_983d49c4d23c0e452aa3a1b851fb0c8216284d5325f60094bf0b319aa7efc534`)
- [observation/documented] Telegram remote control pairs a bot via /pair with a 6-character code; long polling lives in the CLI process, which must keep running, and a headless 'grok telegram-bridge' flow exists. -- evidence: [README.md#L246-L249](https://github.com/superagent-ai/grok-cli/blob/fb97af83f06dca873281d60168430f06c8de6324/README.md#L246-L249), [README.md#L428-L430](https://github.com/superagent-ai/grok-cli/blob/fb97af83f06dca873281d60168430f06c8de6324/README.md#L428-L430), [README.md#L282-L284](https://github.com/superagent-ai/grok-cli/blob/fb97af83f06dca873281d60168430f06c8de6324/README.md#L282-L284) (`clm_06e3f87ab4cfbb15482aa1a7e4428ba0404b412939af7feec403441a6b643dee`)

## memory-state (1 claim(s))

- [observation/documented] Sessions can be resumed with 'grok --session latest' or 'grok -s <session-id>' (also in interactive mode), and /compact in the TUI compresses accumulated conversation history. -- evidence: [README.md#L453-L454](https://github.com/superagent-ai/grok-cli/blob/fb97af83f06dca873281d60168430f06c8de6324/README.md#L453-L454), [README.md#L84-L87](https://github.com/superagent-ai/grok-cli/blob/fb97af83f06dca873281d60168430f06c8de6324/README.md#L84-L87), [README.md#L89-L89](https://github.com/superagent-ai/grok-cli/blob/fb97af83f06dca873281d60168430f06c8de6324/README.md#L89-L89) (`clm_5b55ebd2e3523c0ed4f8a89e25e7d7b4c68ff97c5f2b654efcf0840d0b2e89d8`)

## orchestration (1 claim(s))

- [observation/documented] Sub-agents are on by default: foreground task delegation (e.g. explore, general, computer) plus background delegate for read-only deep dives. -- evidence: [README.md#L11-L11](https://github.com/superagent-ai/grok-cli/blob/fb97af83f06dca873281d60168430f06c8de6324/README.md#L11-L11), [README.md#L174-L189](https://github.com/superagent-ai/grok-cli/blob/fb97af83f06dca873281d60168430f06c8de6324/README.md#L174-L189) (`clm_6df113290d79359c52fe6f4d5675c654ec59ba34655f844ab79bc110b228973d`)

## tools-permissions (1 claim(s))

- [observation/documented] Shell commands can run inside a Shuru microVM sandbox (--sandbox or /sandbox) isolating host filesystem and network; network is off by default with --allow-net/--allow-host controls, plus port forwards, resource limits, checkpoints, and secret injection. -- evidence: [README.md#L345-L349](https://github.com/superagent-ai/grok-cli/blob/fb97af83f06dca873281d60168430f06c8de6324/README.md#L345-L349), [README.md#L335-L335](https://github.com/superagent-ai/grok-cli/blob/fb97af83f06dca873281d60168430f06c8de6324/README.md#L335-L335), [README.md#L339-L339](https://github.com/superagent-ai/grok-cli/blob/fb97af83f06dca873281d60168430f06c8de6324/README.md#L339-L339) (`clm_b3ed30d868d173884f8d1bb456f80f6f165ff808c942fb7593d486db908b0f74`)

## evaluation (1 claim(s))

- [inference/documented] No agent-performance benchmark or scored eval harness appears in the provided evidence; the --verify command produces build/run verification reports with screenshots and video, which is a runtime feature rather than a scored evaluation. -- evidence: [README.md#L355-L355](https://github.com/superagent-ai/grok-cli/blob/fb97af83f06dca873281d60168430f06c8de6324/README.md#L355-L355), [README.md#L362-L362](https://github.com/superagent-ai/grok-cli/blob/fb97af83f06dca873281d60168430f06c8de6324/README.md#L362-L362) (`clm_dc26bcb2246c560dccc8b066609a697f31df1ee359b5792679e3a7c158872ae2`)

## dependencies (2 claim(s))

- [observation/documented] The tool is built with TypeScript and Bun with an OpenTUI terminal UI, installs via a curl install script or 'bun add -g grok-dev', and the computer sub-agent depends on the agent-desktop package. -- evidence: [README.md#L3-L7](https://github.com/superagent-ai/grok-cli/blob/fb97af83f06dca873281d60168430f06c8de6324/README.md#L3-L7), [README.md#L11-L11](https://github.com/superagent-ai/grok-cli/blob/fb97af83f06dca873281d60168430f06c8de6324/README.md#L11-L11), [README.md#L19-L21](https://github.com/superagent-ai/grok-cli/blob/fb97af83f06dca873281d60168430f06c8de6324/README.md#L19-L21), [README.md#L103-L103](https://github.com/superagent-ai/grok-cli/blob/fb97af83f06dca873281d60168430f06c8de6324/README.md#L103-L103), [README.md#L25-L27](https://github.com/superagent-ai/grok-cli/blob/fb97af83f06dca873281d60168430f06c8de6324/README.md#L25-L27) (`clm_59ac30e9da55799033c86a6b84113b6ffaf04133479b294c6db16b3c107de8e7`)
- [observation/documented] Telegram voice notes are transcribed via xAI's Grok Speech-to-Text endpoint (/v1/stt), which replaced whisper.cpp and removed local whisper-cli, ffmpeg, and model-download requirements. -- evidence: [CHANGELOG.md#L15-L17](https://github.com/superagent-ai/grok-cli/blob/fb97af83f06dca873281d60168430f06c8de6324/CHANGELOG.md#L15-L17), [README.md#L253-L253](https://github.com/superagent-ai/grok-cli/blob/fb97af83f06dca873281d60168430f06c8de6324/README.md#L253-L253) (`clm_0aa93efb84d3bf0fa4dfed75245f69da5d7283d3e2222d541d46879e2e9b0fa4`)

## limitations (1 claim(s))

- [observation/documented] Sandbox mode requires macOS 14+ on Apple Silicon and is unavailable on Intel Macs or Linux, per the troubleshooting section. -- evidence: [README.md#L439-L439](https://github.com/superagent-ai/grok-cli/blob/fb97af83f06dca873281d60168430f06c8de6324/README.md#L439-L439), [README.md#L441-L441](https://github.com/superagent-ai/grok-cli/blob/fb97af83f06dca873281d60168430f06c8de6324/README.md#L441-L441), [README.md#L337-L337](https://github.com/superagent-ai/grok-cli/blob/fb97af83f06dca873281d60168430f06c8de6324/README.md#L337-L337) (`clm_95fdb205625ec2c164299ab0a7129d382c7d6c533b3618ba11aabd1a47ccd2a1`)

## relevance (1 claim(s))

- [observation/documented] The project is community-built, open-source, MIT-licensed, and explicitly not affiliated with or endorsed by xAI Corp, using the publicly available Grok API. -- evidence: [README.md#L9-L9](https://github.com/superagent-ai/grok-cli/blob/fb97af83f06dca873281d60168430f06c8de6324/README.md#L9-L9), [README.md#L490-L490](https://github.com/superagent-ai/grok-cli/blob/fb97af83f06dca873281d60168430f06c8de6324/README.md#L490-L490), [README.md#L496-L496](https://github.com/superagent-ai/grok-cli/blob/fb97af83f06dca873281d60168430f06c8de6324/README.md#L496-L496) (`clm_c50665aa9b9eba0243af54593c33f130f0370d9e3ec11bb79190f1e9afcc7b78`)

