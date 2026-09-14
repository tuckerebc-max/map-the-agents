---
access: public
aliases: []
claim_ids:
- clm_0a6b190aef29b7fadd7da775a97fc0792b70140befc026a5eb16993585bc340b
- clm_142c38dcbed80027eff517f0ad6ec48b7e1cbe14f2e918d53e26b73093f3eebd
- clm_3502077017d53bb247549f202756d84e19a06c849b49ed3c50fac22fb3a15b1d
- clm_35116894a52e1cf07f7e7a21fa347cb48b3f62ec659cf65a43756f66c827538e
- clm_40c1d3a8b89634dab75c6bec0972d8bca30f155a40495723ed9a124c92bbddbe
- clm_4367f1946509544aa0fd04c44c5206c9c218e320a31c25aef5140d2066c8854e
- clm_5b81abc80410990b4518037e4e41f3441f97b6922b534cadf9d6132117b2e1eb
- clm_6b1f0400767bcbbbadd7d90a24a28d7a40ba46e86e99a8dedc4772b7ab467512
- clm_840d8fc4de1b8917c836b2fd28787be38a7d7eb833e0be63b68523052bdcae70
- clm_8ecb6194bc6413a757c8389aeb76265b7b074242072dc4457a34ed9532ad6d75
- clm_9bedc2bd79e446876d8fd0501d48f709d8026e6f556a690a0e03a373c22df680
- clm_ae0106579e5ddcaba3407106577f3608b0ba1548038d57f8769a8a14881a8f35
- clm_ae2e101cc5cf9d3900dd4083d095d400562d049228b73ade627a45445b2c9111
- clm_b80c01dd6cc3d0775f888ffcf455cde5913c7dd053e4a9b7c22de1f834beb6fd
- clm_c044da9f68e41e95a4b63a2935fea182c84c86eedb54a0884f334aee2796c836
- clm_c0f36714e932d1dd5d912a0c0d53e0539837ad92812874b43aeffb119f0ef2cd
- clm_c5d2042b9bf7f64583e06fb51be93083d51256e37e498d9abaf30c5560d1c9f8
- clm_cd851648179be82a3e044b103d3701a8f9a688b5ace66973fc48ea18bc871566
- clm_eec9d895ee2f13a49b0229501a42bfc6eafcace6d3757b83c18bbca8cf183f7e
- clm_f2a45a3db439c29d2a4c5d905ae501452b0c13f1a6d19aa64732c8559229f163
maturity: draft
page_id: pg_1c2a4831f5fd5250b0dee2445dcb4c00
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_24f7c560c17f5486ac984c98d0eb28e3
title: can1357/oh-my-pi/README.md @ 9b2a43514bfc
updated_at: '2026-09-14T01:39:37Z'
---

# can1357/oh-my-pi/README.md @ 9b2a43514bfc

<!-- rcw:begin owner=source:src_24f7c560c17f5486ac984c98d0eb28e3 block=evidence -->
- The task tool fans out subagents in parallel, optionally workspace-isolated, returning schema-validated results; an Agent Hub (Alt+A) shows live transcripts and lets users steer or kill workers. [@claim:clm_0a6b190aef29b7fadd7da775a97fc0792b70140befc026a5eb16993585bc340b]
- The README cites benchmark-style results for its edit format, e.g. Grok Code Fast 1 improving 6.7% to 68.3% and MiniMax pass rate roughly doubling versus str_replace, linking a blog post for details. [@claim:clm_142c38dcbed80027eff517f0ad6ec48b7e1cbe14f2e918d53e26b73093f3eebd]
- Custom OpenAI-compatible providers can be declared in ~/.omp/agent/models.yml, and routing supports fallback chains, path-scoped model lists, and round-robin API-key rotation with per-credential backoff. [@claim:clm_3502077017d53bb247549f202756d84e19a06c849b49ed3c50fac22fb3a15b1d]
- The active tool set can be pinned via --tools; rarely used discoverable tools sit behind xd:// devices and run only when tools.xdev is enabled. [@claim:clm_35116894a52e1cf07f7e7a21fa347cb48b3f62ec659cf65a43756f66c827538e]
- Prompt-control keywords (ultrathink, orchestrate, workflowz) trigger only in prose, not inside code spans, fenced blocks, XML/HTML, identifiers, or paths. [@claim:clm_40c1d3a8b89634dab75c6bec0972d8bca30f155a40495723ed9a124c92bbddbe]
- Repository development practice: pull requests are temporarily open to everyone as a trial; a prior vouch requirement is lifted while open contributions are evaluated, and it may return. [@claim:clm_4367f1946509544aa0fd04c44c5206c9c218e320a31c25aef5140d2066c8854e]
- Sixteen internal URI schemes (pr://, issue://, agent://, skill://, ssh://, etc.) resolve inside filesystem-shaped tools, so read pr://1428 behaves like reading a local file. [@claim:clm_5b81abc80410990b4518037e4e41f3441f97b6922b534cadf9d6132117b2e1eb]
- RPC mode uses NDJSON commands over stdio; an --mode rpc-ui variant emits tool cards, selectors, and dialogs as extension_ui_request frames the host must answer. [@claim:clm_6b1f0400767bcbbbadd7d90a24a28d7a40ba46e86e99a8dedc4772b7ab467512]
- Edits use hashline patches anchored by content hashes; stale anchors cause the patch to be rejected before applying, and the README reports 61% fewer output tokens for Grok 4 Fast. [@claim:clm_840d8fc4de1b8917c836b2fd28787be38a7d7eb833e0be63b68523052bdcae70]
- pi-shell is an embedded bash engine (~38k lines) with persistent sessions and in-process coreutils dispatch; pi-walker is a parallel ignore-aware walker shared by grep, glob, workspace, and shell. [@claim:clm_8ecb6194bc6413a757c8389aeb76265b7b074242072dc4457a34ed9532ad6d75]
- Over ACP, tool I/O routes through editor capabilities and writes are gated by session/request_permission; the edit and bash tools map to that permission route. [@claim:clm_9bedc2bd79e446876d8fd0501d48f709d8026e6f556a690a0e03a373c22df680]
- The Node SDK package @oh-my-pi/pi-coding-agent exposes ModelRegistry, SessionManager, createAgentSession, and discoverAuthStorage, with typed session events. [@claim:clm_ae0106579e5ddcaba3407106577f3608b0ba1548038d57f8769a8a14881a8f35]
- The native layer comprises six Rust crates (pi-natives, pi-shell, pi-ast, pi-iso, pi-voice, pi-walker) shipped as a platform-tagged N-API addon for six platforms. [@claim:clm_ae2e101cc5cf9d3900dd4083d095d400562d049228b73ade627a45445b2c9111]
- omp offers four entry points sharing one engine: an interactive TUI, a one-shot prompt mode (omp -p), a Node SDK, and stdio-based RPC and ACP modes. [@claim:clm_b80c01dd6cc3d0775f888ffcf455cde5913c7dd053e4a9b7c22de1f834beb6fd]
- Merge conflicts are exposed as URLs: the agent writes @theirs, @ours, or @base to conflict://N (or conflict://* in bulk) to resolve files. [@claim:clm_c044da9f68e41e95a4b63a2935fea182c84c86eedb54a0884f334aee2796c836]
- Memory tools include retain, recall, reflect, memory_edit, and learn (which can promote lessons into managed skills), with a selectable memory.backend (local, Hindsight, or Mnemopi) that is project-scoped by default. [@claim:clm_c0f36714e932d1dd5d912a0c0d53e0539837ad92812874b43aeffb119f0ef2cd]
- web_search chains twenty-three providers, including keyless options (duckduckgo, startpage, browser-based google/ecosia/mojeek) and API-key or oauth-backed services, with site-aware extraction for code hosts, registries, and research sources. [@claim:clm_c5d2042b9bf7f64583e06fb51be93083d51256e37e498d9abaf30c5560d1c9f8]
- omp links search, shell, AST, and other native implementations in-process to avoid fork/exec on the hot path, and the same binary targets macOS, Linux, and Windows without WSL. [@claim:clm_cd851648179be82a3e044b103d3701a8f9a688b5ace66973fc48ea18bc871566]
- omp generates bash, zsh, and fish completion scripts from live command/flag metadata, with model names resolved against a bundled catalog and --resume against on-disk sessions. [@claim:clm_eec9d895ee2f13a49b0229501a42bfc6eafcace6d3757b83c18bbca8cf183f7e]
- An 'advisor' role pairs a second model that reads every main-agent turn on its own context and injects inline notes ranging from asides to hard blockers. [@claim:clm_f2a45a3db439c29d2a4c5d905ae501452b0c13f1a6d19aa64732c8559229f163]
<!-- rcw:end owner=source:src_24f7c560c17f5486ac984c98d0eb28e3 block=evidence -->

## Researcher notes

