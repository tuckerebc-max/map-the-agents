# prime-radiant-inc/evener -- full detail

[Back to orientation](evener.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/prime-radiant-inc/evener/ea6649c17c5db8e55c29c03bbe103eeef4a0d538/afd5117241fc1a76.json](../../../wiki/dossiers/prime-radiant-inc/evener/ea6649c17c5db8e55c29c03bbe103eeef4a0d538/afd5117241fc1a76.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (2 claim(s))

- [observation/documented] The repo is a multi-module Go monorepo (llm, agent, auth libraries plus the app) where binaries couple only via the appwire and hubapi wire contracts, never by importing each other's code; libraries may never import app code. -- evidence: [docs/architecture.md#L33-L37](https://github.com/prime-radiant-inc/evener/blob/ea6649c17c5db8e55c29c03bbe103eeef4a0d538/docs/architecture.md#L33-L37), [docs/architecture.md#L15-L20](https://github.com/prime-radiant-inc/evener/blob/ea6649c17c5db8e55c29c03bbe103eeef4a0d538/docs/architecture.md#L15-L20), [docs/architecture.md#L39-L41](https://github.com/prime-radiant-inc/evener/blob/ea6649c17c5db8e55c29c03bbe103eeef4a0d538/docs/architecture.md#L39-L41), [docs/architecture.md#L11-L13](https://github.com/prime-radiant-inc/evener/blob/ea6649c17c5db8e55c29c03bbe103eeef4a0d538/docs/architecture.md#L11-L13), [docs/architecture.md#L30-L31](https://github.com/prime-radiant-inc/evener/blob/ea6649c17c5db8e55c29c03bbe103eeef4a0d538/docs/architecture.md#L30-L31), [docs/architecture.md#L78-L84](https://github.com/prime-radiant-inc/evener/blob/ea6649c17c5db8e55c29c03bbe103eeef4a0d538/docs/architecture.md#L78-L84) (`clm_654a61ee0e3f88d56d50d7683e80dfb08c545707cc4f5461c1f617566d80b523`)
- [observation/documented] A repeated-call breaker keys a per-session ledger on tool name plus a hash of raw argument bytes: the third consecutive same-class failure is refused before dispatch, and a repetition trigger nudges on byte-identical result bodies without refusing, so communicate is never blocked. -- evidence: [docs/architecture.md#L221-L228](https://github.com/prime-radiant-inc/evener/blob/ea6649c17c5db8e55c29c03bbe103eeef4a0d538/docs/architecture.md#L221-L228), [docs/architecture.md#L202-L219](https://github.com/prime-radiant-inc/evener/blob/ea6649c17c5db8e55c29c03bbe103eeef4a0d538/docs/architecture.md#L202-L219) (`clm_d45761b153f2cb18e5ce95b0921689ea546962d172285ce75e3bf1e4b11ece37`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: build and install from source with make build / build-hub / build-llmcall / make install, run `make help` for targets, and note that vet/test-race/lint gates iterate over every module since a root-only `go test ./...` skips the library suites in a workspace. -- evidence: [README.md#L389-L391](https://github.com/prime-radiant-inc/evener/blob/ea6649c17c5db8e55c29c03bbe103eeef4a0d538/README.md#L389-L391), [docs/architecture.md#L66-L74](https://github.com/prime-radiant-inc/evener/blob/ea6649c17c5db8e55c29c03bbe103eeef4a0d538/docs/architecture.md#L66-L74), [README.md#L40-L42](https://github.com/prime-radiant-inc/evener/blob/ea6649c17c5db8e55c29c03bbe103eeef4a0d538/README.md#L40-L42), [README.md#L154-L156](https://github.com/prime-radiant-inc/evener/blob/ea6649c17c5db8e55c29c03bbe103eeef4a0d538/README.md#L154-L156), [README.md#L121-L122](https://github.com/prime-radiant-inc/evener/blob/ea6649c17c5db8e55c29c03bbe103eeef4a0d538/README.md#L121-L122), [README.md#L13-L23](https://github.com/prime-radiant-inc/evener/blob/ea6649c17c5db8e55c29c03bbe103eeef4a0d538/README.md#L13-L23) (`clm_fd113fa0049fb22d4d7566d7b5ddd91056bc950ef0eb8e3c0dd08c6b0731c9cc`)

## skills-patterns (1 claim(s))

- [observation/documented] Standalone user skills in the config skills directory are discovered automatically, extra skill paths can be added via skills_dirs in launch.toml or CLI flags, and user-global slash commands are read from a commands directory when present. -- evidence: [README.md#L60-L69](https://github.com/prime-radiant-inc/evener/blob/ea6649c17c5db8e55c29c03bbe103eeef4a0d538/README.md#L60-L69), [README.md#L71-L88](https://github.com/prime-radiant-inc/evener/blob/ea6649c17c5db8e55c29c03bbe103eeef4a0d538/README.md#L71-L88) (`clm_ed65f4826fbd15098381a2412f26f5aa61cef47dbefcd72465100213b9177e7c`)

## interfaces (3 claim(s))

- [observation/documented] The product ships three binaries: `evener` (non-interactive CLI engine), `evener hub` (browser-based orchestrator for many concurrent sessions), and `evener tui` (terminal dashboard), plus a one-shot `llmcall` client. -- evidence: [README.md#L150-L150](https://github.com/prime-radiant-inc/evener/blob/ea6649c17c5db8e55c29c03bbe103eeef4a0d538/README.md#L150-L150), [docs/architecture.md#L11-L13](https://github.com/prime-radiant-inc/evener/blob/ea6649c17c5db8e55c29c03bbe103eeef4a0d538/docs/architecture.md#L11-L13), [README.md#L379-L379](https://github.com/prime-radiant-inc/evener/blob/ea6649c17c5db8e55c29c03bbe103eeef4a0d538/README.md#L379-L379), [README.md#L3-L8](https://github.com/prime-radiant-inc/evener/blob/ea6649c17c5db8e55c29c03bbe103eeef4a0d538/README.md#L3-L8), [README.md#L116-L117](https://github.com/prime-radiant-inc/evener/blob/ea6649c17c5db8e55c29c03bbe103eeef4a0d538/README.md#L116-L117), [README.md#L209-L211](https://github.com/prime-radiant-inc/evener/blob/ea6649c17c5db8e55c29c03bbe103eeef4a0d538/README.md#L209-L211) (`clm_e39ec22e5226f349325ada2f2245bd79363453b103fb8cfbca64dc15b890d8ad`)
- [observation/documented] The hub listens on 127.0.0.1:9180, prints a one-time auth URL that sets an authorizing browser cookie, and offers a /new session page, /credentials page, fork-from-message, /aside side threads, transparent resume, and Ctrl/⌘K search. -- evidence: [README.md#L98-L99](https://github.com/prime-radiant-inc/evener/blob/ea6649c17c5db8e55c29c03bbe103eeef4a0d538/README.md#L98-L99), [README.md#L101-L103](https://github.com/prime-radiant-inc/evener/blob/ea6649c17c5db8e55c29c03bbe103eeef4a0d538/README.md#L101-L103), [README.md#L126-L136](https://github.com/prime-radiant-inc/evener/blob/ea6649c17c5db8e55c29c03bbe103eeef4a0d538/README.md#L126-L136), [README.md#L105-L112](https://github.com/prime-radiant-inc/evener/blob/ea6649c17c5db8e55c29c03bbe103eeef4a0d538/README.md#L105-L112) (`clm_754b04d96a8d39a7ee420c1d88bdff1477f7f20ff5887e454e41608f0171b21b`)
- [observation/documented] The TUI connects to the hub at 127.0.0.1:9180 by default, auto-starts a missing local hub (unless --no-auto-start-hub), and supports flags like --hub-addr, --hub-bin, --auth-token, --state-dir, and --debug. -- evidence: [README.md#L181-L184](https://github.com/prime-radiant-inc/evener/blob/ea6649c17c5db8e55c29c03bbe103eeef4a0d538/README.md#L181-L184), [README.md#L175-L177](https://github.com/prime-radiant-inc/evener/blob/ea6649c17c5db8e55c29c03bbe103eeef4a0d538/README.md#L175-L177), [README.md#L188-L196](https://github.com/prime-radiant-inc/evener/blob/ea6649c17c5db8e55c29c03bbe103eeef4a0d538/README.md#L188-L196), [README.md#L168-L171](https://github.com/prime-radiant-inc/evener/blob/ea6649c17c5db8e55c29c03bbe103eeef4a0d538/README.md#L168-L171) (`clm_3d355114fdce40a8f21bda6bcdc69d4727db0ad03fedca4475e55a14a576a809`)

## memory-state (1 claim(s))

- [observation/documented] Session state auto-saves under the XDG state directory per project after each assistant turn; project IDs derive from the canonical path so linked worktrees share a bucket while separate clones get distinct ones; sessions resume via --resume, --resume-last, or --resume-with. -- evidence: [README.md#L344-L346](https://github.com/prime-radiant-inc/evener/blob/ea6649c17c5db8e55c29c03bbe103eeef4a0d538/README.md#L344-L346), [README.md#L60-L69](https://github.com/prime-radiant-inc/evener/blob/ea6649c17c5db8e55c29c03bbe103eeef4a0d538/README.md#L60-L69), [README.md#L369-L369](https://github.com/prime-radiant-inc/evener/blob/ea6649c17c5db8e55c29c03bbe103eeef4a0d538/README.md#L369-L369), [README.md#L366-L366](https://github.com/prime-radiant-inc/evener/blob/ea6649c17c5db8e55c29c03bbe103eeef4a0d538/README.md#L366-L366), [README.md#L372-L373](https://github.com/prime-radiant-inc/evener/blob/ea6649c17c5db8e55c29c03bbe103eeef4a0d538/README.md#L372-L373), [README.md#L348-L350](https://github.com/prime-radiant-inc/evener/blob/ea6649c17c5db8e55c29c03bbe103eeef4a0d538/README.md#L348-L350) (`clm_e1c8cec03779524b7f3a45eeca9ec9d5e0cb7c932671b71e5f04114074e3e9ef`)

## orchestration (1 claim(s))

- [observation/documented] The hub spawns `evener` serve daemons as subprocesses and serves clients over AppWire; sessions can be forked at any user message or to a side thread via /aside, and subagents appear indented under their spawning session in the sidebar. -- evidence: [docs/architecture.md#L33-L37](https://github.com/prime-radiant-inc/evener/blob/ea6649c17c5db8e55c29c03bbe103eeef4a0d538/docs/architecture.md#L33-L37), [README.md#L126-L136](https://github.com/prime-radiant-inc/evener/blob/ea6649c17c5db8e55c29c03bbe103eeef4a0d538/README.md#L126-L136), [README.md#L116-L117](https://github.com/prime-radiant-inc/evener/blob/ea6649c17c5db8e55c29c03bbe103eeef4a0d538/README.md#L116-L117) (`clm_eab9a401a6711dd8f35704d5ba0b01c788c8aec110fa38cab10f7127fa452d14`)

## tools-permissions (1 claim(s))

- [observation/documented] A session's file, process, and network access can be confined with the `--sandbox` flag; sandbox denials can escalate to a human approval card, though breaker-parked calls carry no typed error and do not trigger that escalation. -- evidence: [docs/architecture.md#L230-L234](https://github.com/prime-radiant-inc/evener/blob/ea6649c17c5db8e55c29c03bbe103eeef4a0d538/docs/architecture.md#L230-L234), [ABOUT.md#L8-L8](https://github.com/prime-radiant-inc/evener/blob/ea6649c17c5db8e55c29c03bbe103eeef4a0d538/ABOUT.md#L8-L8), [README.md#L13-L23](https://github.com/prime-radiant-inc/evener/blob/ea6649c17c5db8e55c29c03bbe103eeef4a0d538/README.md#L13-L23) (`clm_05d6bdc3e5773285652d03c4ba217cb812ec8c5aba095d360f82cbead36ea600`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Evener uses the LLM's native tool-calling and supports many providers out of the box (OpenAI, Anthropic, Google, Ollama, Bedrock, Azure, and others), with additional providers addable via a providers.toml entry. -- evidence: [README.md#L237-L237](https://github.com/prime-radiant-inc/evener/blob/ea6649c17c5db8e55c29c03bbe103eeef4a0d538/README.md#L237-L237), [ABOUT.md#L11-L13](https://github.com/prime-radiant-inc/evener/blob/ea6649c17c5db8e55c29c03bbe103eeef4a0d538/ABOUT.md#L11-L13), [README.md#L13-L23](https://github.com/prime-radiant-inc/evener/blob/ea6649c17c5db8e55c29c03bbe103eeef4a0d538/README.md#L13-L23) (`clm_c51b98fc026589a199eae4382c2a44cb6fc82d1211e4a120f52915722e8fffca`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

