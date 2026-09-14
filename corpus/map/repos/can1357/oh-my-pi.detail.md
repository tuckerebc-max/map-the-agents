# can1357/oh-my-pi -- full detail

[Back to orientation](oh-my-pi.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/can1357/oh-my-pi/9b2a43514bfcfc0b9607ac9ac160115aec897f06/d28b45f95a242d11.json](../../../wiki/dossiers/can1357/oh-my-pi/9b2a43514bfcfc0b9607ac9ac160115aec897f06/d28b45f95a242d11.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] The native layer comprises six Rust crates (pi-natives, pi-shell, pi-ast, pi-iso, pi-voice, pi-walker) shipped as a platform-tagged N-API addon for six platforms. -- evidence: [README.md#L452-L453](https://github.com/can1357/oh-my-pi/blob/9b2a43514bfcfc0b9607ac9ac160115aec897f06/README.md#L452-L453), [README.md#L450-L450](https://github.com/can1357/oh-my-pi/blob/9b2a43514bfcfc0b9607ac9ac160115aec897f06/README.md#L450-L450) (`clm_ae2e101cc5cf9d3900dd4083d095d400562d049228b73ade627a45445b2c9111`)
- [observation/documented] pi-shell is an embedded bash engine (~38k lines) with persistent sessions and in-process coreutils dispatch; pi-walker is a parallel ignore-aware walker shared by grep, glob, workspace, and shell. -- evidence: [README.md#L457-L464](https://github.com/can1357/oh-my-pi/blob/9b2a43514bfcfc0b9607ac9ac160115aec897f06/README.md#L457-L464) (`clm_8ecb6194bc6413a757c8389aeb76265b7b074242072dc4457a34ed9532ad6d75`)

## design-choices (3 claim(s))

- [observation/documented] omp links search, shell, AST, and other native implementations in-process to avoid fork/exec on the hot path, and the same binary targets macOS, Linux, and Windows without WSL. -- evidence: [README.md#L450-L450](https://github.com/can1357/oh-my-pi/blob/9b2a43514bfcfc0b9607ac9ac160115aec897f06/README.md#L450-L450), [README.md#L199-L199](https://github.com/can1357/oh-my-pi/blob/9b2a43514bfcfc0b9607ac9ac160115aec897f06/README.md#L199-L199) (`clm_cd851648179be82a3e044b103d3701a8f9a688b5ace66973fc48ea18bc871566`)
- [observation/documented] Edits use hashline patches anchored by content hashes; stale anchors cause the patch to be rejected before applying, and the README reports 61% fewer output tokens for Grok 4 Fast. -- evidence: [README.md#L207-L207](https://github.com/can1357/oh-my-pi/blob/9b2a43514bfcfc0b9607ac9ac160115aec897f06/README.md#L207-L207) (`clm_840d8fc4de1b8917c836b2fd28787be38a7d7eb833e0be63b68523052bdcae70`)
- [observation/documented] Prompt-control keywords (ultrathink, orchestrate, workflowz) trigger only in prose, not inside code spans, fenced blocks, XML/HTML, identifiers, or paths. -- evidence: [README.md#L321-L321](https://github.com/can1357/oh-my-pi/blob/9b2a43514bfcfc0b9607ac9ac160115aec897f06/README.md#L321-L321), [README.md#L315-L315](https://github.com/can1357/oh-my-pi/blob/9b2a43514bfcfc0b9607ac9ac160115aec897f06/README.md#L315-L315) (`clm_40c1d3a8b89634dab75c6bec0972d8bca30f155a40495723ed9a124c92bbddbe`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: pull requests are temporarily open to everyone as a trial; a prior vouch requirement is lifted while open contributions are evaluated, and it may return. -- evidence: [README.md#L29-L33](https://github.com/can1357/oh-my-pi/blob/9b2a43514bfcfc0b9607ac9ac160115aec897f06/README.md#L29-L33) (`clm_4367f1946509544aa0fd04c44c5206c9c218e320a31c25aef5140d2066c8854e`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (6 claim(s))

- [observation/documented] omp offers four entry points sharing one engine: an interactive TUI, a one-shot prompt mode (omp -p), a Node SDK, and stdio-based RPC and ACP modes. -- evidence: [README.md#L496-L496](https://github.com/can1357/oh-my-pi/blob/9b2a43514bfcfc0b9607ac9ac160115aec897f06/README.md#L496-L496) (`clm_b80c01dd6cc3d0775f888ffcf455cde5913c7dd053e4a9b7c22de1f834beb6fd`)
- [observation/documented] The Node SDK package @oh-my-pi/pi-coding-agent exposes ModelRegistry, SessionManager, createAgentSession, and discoverAuthStorage, with typed session events. -- evidence: [README.md#L508-L508](https://github.com/can1357/oh-my-pi/blob/9b2a43514bfcfc0b9607ac9ac160115aec897f06/README.md#L508-L508), [README.md#L510-L510](https://github.com/can1357/oh-my-pi/blob/9b2a43514bfcfc0b9607ac9ac160115aec897f06/README.md#L510-L510) (`clm_ae0106579e5ddcaba3407106577f3608b0ba1548038d57f8769a8a14881a8f35`)
- [observation/documented] RPC mode uses NDJSON commands over stdio; an --mode rpc-ui variant emits tool cards, selectors, and dialogs as extension_ui_request frames the host must answer. -- evidence: [README.md#L536-L536](https://github.com/can1357/oh-my-pi/blob/9b2a43514bfcfc0b9607ac9ac160115aec897f06/README.md#L536-L536) (`clm_6b1f0400767bcbbbadd7d90a24a28d7a40ba46e86e99a8dedc4772b7ab467512`)
- [observation/documented] omp generates bash, zsh, and fish completion scripts from live command/flag metadata, with model names resolved against a bundled catalog and --resume against on-disk sessions. -- evidence: [README.md#L98-L98](https://github.com/can1357/oh-my-pi/blob/9b2a43514bfcfc0b9607ac9ac160115aec897f06/README.md#L98-L98) (`clm_eec9d895ee2f13a49b0229501a42bfc6eafcace6d3757b83c18bbca8cf183f7e`)
- [observation/documented] Sixteen internal URI schemes (pr://, issue://, agent://, skill://, ssh://, etc.) resolve inside filesystem-shaped tools, so read pr://1428 behaves like reading a local file. -- evidence: [README.md#L231-L231](https://github.com/can1357/oh-my-pi/blob/9b2a43514bfcfc0b9607ac9ac160115aec897f06/README.md#L231-L231) (`clm_5b81abc80410990b4518037e4e41f3441f97b6922b534cadf9d6132117b2e1eb`)
- [observation/documented] Merge conflicts are exposed as URLs: the agent writes @theirs, @ours, or @base to conflict://N (or conflict://* in bulk) to resolve files. -- evidence: [README.md#L235-L235](https://github.com/can1357/oh-my-pi/blob/9b2a43514bfcfc0b9607ac9ac160115aec897f06/README.md#L235-L235) (`clm_c044da9f68e41e95a4b63a2935fea182c84c86eedb54a0884f334aee2796c836`)

## memory-state (1 claim(s))

- [observation/documented] Memory tools include retain, recall, reflect, memory_edit, and learn (which can promote lessons into managed skills), with a selectable memory.backend (local, Hindsight, or Mnemopi) that is project-scoped by default. -- evidence: [README.md#L215-L215](https://github.com/can1357/oh-my-pi/blob/9b2a43514bfcfc0b9607ac9ac160115aec897f06/README.md#L215-L215), [README.md#L300-L307](https://github.com/can1357/oh-my-pi/blob/9b2a43514bfcfc0b9607ac9ac160115aec897f06/README.md#L300-L307) (`clm_c0f36714e932d1dd5d912a0c0d53e0539837ad92812874b43aeffb119f0ef2cd`)

## orchestration (2 claim(s))

- [observation/documented] The task tool fans out subagents in parallel, optionally workspace-isolated, returning schema-validated results; an Agent Hub (Alt+A) shows live transcripts and lets users steer or kill workers. -- evidence: [README.md#L165-L165](https://github.com/can1357/oh-my-pi/blob/9b2a43514bfcfc0b9607ac9ac160115aec897f06/README.md#L165-L165), [README.md#L284-L287](https://github.com/can1357/oh-my-pi/blob/9b2a43514bfcfc0b9607ac9ac160115aec897f06/README.md#L284-L287), [README.md#L171-L171](https://github.com/can1357/oh-my-pi/blob/9b2a43514bfcfc0b9607ac9ac160115aec897f06/README.md#L171-L171) (`clm_0a6b190aef29b7fadd7da775a97fc0792b70140befc026a5eb16993585bc340b`)
- [observation/documented] An 'advisor' role pairs a second model that reads every main-agent turn on its own context and injects inline notes ranging from asides to hard blockers. -- evidence: [README.md#L175-L175](https://github.com/can1357/oh-my-pi/blob/9b2a43514bfcfc0b9607ac9ac160115aec897f06/README.md#L175-L175) (`clm_f2a45a3db439c29d2a4c5d905ae501452b0c13f1a6d19aa64732c8559229f163`)

## tools-permissions (2 claim(s))

- [observation/documented] Over ACP, tool I/O routes through editor capabilities and writes are gated by session/request_permission; the edit and bash tools map to that permission route. -- evidence: [README.md#L550-L550](https://github.com/can1357/oh-my-pi/blob/9b2a43514bfcfc0b9607ac9ac160115aec897f06/README.md#L550-L550), [README.md#L552-L557](https://github.com/can1357/oh-my-pi/blob/9b2a43514bfcfc0b9607ac9ac160115aec897f06/README.md#L552-L557) (`clm_9bedc2bd79e446876d8fd0501d48f709d8026e6f556a690a0e03a373c22df680`)
- [observation/documented] The active tool set can be pinned via --tools; rarely used discoverable tools sit behind xd:// devices and run only when tools.xdev is enabled. -- evidence: [README.md#L259-L259](https://github.com/can1357/oh-my-pi/blob/9b2a43514bfcfc0b9607ac9ac160115aec897f06/README.md#L259-L259) (`clm_35116894a52e1cf07f7e7a21fa347cb48b3f62ec659cf65a43756f66c827538e`)

## evaluation (1 claim(s))

- [observation/documented] The README cites benchmark-style results for its edit format, e.g. Grok Code Fast 1 improving 6.7% to 68.3% and MiniMax pass rate roughly doubling versus str_replace, linking a blog post for details. -- evidence: [README.md#L115-L120](https://github.com/can1357/oh-my-pi/blob/9b2a43514bfcfc0b9607ac9ac160115aec897f06/README.md#L115-L120), [README.md#L127-L127](https://github.com/can1357/oh-my-pi/blob/9b2a43514bfcfc0b9607ac9ac160115aec897f06/README.md#L127-L127) (`clm_142c38dcbed80027eff517f0ad6ec48b7e1cbe14f2e918d53e26b73093f3eebd`)

## dependencies (2 claim(s))

- [observation/documented] web_search chains twenty-three providers, including keyless options (duckduckgo, startpage, browser-based google/ecosia/mojeek) and API-key or oauth-backed services, with site-aware extraction for code hosts, registries, and research sources. -- evidence: [README.md#L391-L391](https://github.com/can1357/oh-my-pi/blob/9b2a43514bfcfc0b9607ac9ac160115aec897f06/README.md#L391-L391), [README.md#L397-L422](https://github.com/can1357/oh-my-pi/blob/9b2a43514bfcfc0b9607ac9ac160115aec897f06/README.md#L397-L422), [README.md#L430-L434](https://github.com/can1357/oh-my-pi/blob/9b2a43514bfcfc0b9607ac9ac160115aec897f06/README.md#L430-L434) (`clm_c5d2042b9bf7f64583e06fb51be93083d51256e37e498d9abaf30c5560d1c9f8`)
- [observation/documented] Custom OpenAI-compatible providers can be declared in ~/.omp/agent/models.yml, and routing supports fallback chains, path-scoped model lists, and round-robin API-key rotation with per-credential backoff. -- evidence: [README.md#L382-L385](https://github.com/can1357/oh-my-pi/blob/9b2a43514bfcfc0b9607ac9ac160115aec897f06/README.md#L382-L385), [README.md#L356-L356](https://github.com/can1357/oh-my-pi/blob/9b2a43514bfcfc0b9607ac9ac160115aec897f06/README.md#L356-L356) (`clm_3502077017d53bb247549f202756d84e19a06c849b49ed3c50fac22fb3a15b1d`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

