---
access: public
aliases: []
claim_ids:
- clm_0ae662a46b21eab9245fb2812159d268190ef2c8c1db1bf48ff875b359490756
- clm_1099654794c6eea5d9cde50bc7321254a9cd8302496c5da94d7cba3849c53752
- clm_310275175c08ec391624e5e55960d7e3bd01afe08009dc60debcbe1df68f534a
- clm_50fcd673989fdddb93625ad1a28efe99c2b4bc31e64122d28c774d638bfd504c
- clm_72a8c1f7689632e9ce04b446bfe238777e5fc2f82e756f19f061df714c8cbd70
- clm_77148b411b4da0daa393e82964d948e18c9da30aa00ab5e782baac530a3c433e
- clm_79045bfc980a19397cbb57414993fee68a8dc3c38164ee897da41a368c9e7d31
- clm_de969f704188b66dd746ba6381675ba1115903f4d5f997a56ca84ff4d91de802
maturity: draft
page_id: pg_3a01f87f5696524299c0a89e3cfc329d
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_c6dca1f4dafa573b93b4bc2d33154982
title: josephsenior/Grinta-Coding-Agent/docs/ARCHITECTURE.md @ 918df240e0a5
updated_at: '2026-09-14T02:08:06Z'
---

# josephsenior/Grinta-Coding-Agent/docs/ARCHITECTURE.md @ 918df240e0a5

<!-- rcw:begin owner=source:src_c6dca1f4dafa573b93b4bc2d33154982 block=evidence -->
- Errors are classified as recoverable or terminal; recoverable errors retry with backoff, while terminal errors emit an error observation and transition to an ERROR state. Public lifecycle states include RUNNING, RETRYING, RATE_LIMITED, FINISHED, and others. [@claim:clm_0ae662a46b21eab9245fb2812159d268190ef2c8c1db1bf48ff875b359490756]
- The architecture has four layers: interface (launcher, TUI, non-interactive runner), orchestration (planning, retries, finish validation), execution (local commands, files, tools), and durability (event stream and persisted state). [@claim:clm_1099654794c6eea5d9cde50bc7321254a9cd8302496c5da94d7cba3849c53752]
- CLI subcommands include grinta init, grinta doctor, grinta sessions list/show/export/prune, and flags such as --project, --model, --theme, --minimal, --accessible, and --cleanup-storage. [@claim:clm_310275175c08ec391624e5e55960d7e3bd01afe08009dc60debcbe1df68f534a]
- A SessionOrchestrator coordinates focused services (retry, circuit breaker, stuck detection, task validation, state transitions) and runs actions through a middleware pipeline where safety checks execute first and telemetry last. [@claim:clm_50fcd673989fdddb93625ad1a28efe99c2b4bc31e64122d28c774d638bfd504c]
- The runtime targets Python 3.12 or 3.13, supports Linux, Windows, macOS, and WSL2, and the package metadata reports version 1.0.0. [@claim:clm_72a8c1f7689632e9ce04b446bfe238777e5fc2f82e756f19f061df714c8cbd70]
- The sandboxed_local execution profile adds OS-native process-scoped isolation (bwrap, AppContainer, sandbox-exec) for supported non-interactive subprocess commands, but interactive PTY sessions stay outside that boundary and it is not a VM or host isolation. [@claim:clm_77148b411b4da0daa393e82964d948e18c9da30aa00ab5e782baac530a3c433e]
- The product offers a Textual terminal UI for TTY stdin and a non-interactive runner for piped input where each input line is one turn, plus slash commands like /mode, /model, /checkpoint, and /resume. [@claim:clm_79045bfc980a19397cbb57414993fee68a8dc3c38164ee897da41a368c9e7d31]
- Sessions, event history, and checkpoints persist locally; workspace checkpoints use the standalone ShadowGit package writing content-addressed snapshots to a private object store without touching the user's .git. [@claim:clm_de969f704188b66dd746ba6381675ba1115903f4d5f997a56ca84ff4d91de802]
<!-- rcw:end owner=source:src_c6dca1f4dafa573b93b4bc2d33154982 block=evidence -->

## Researcher notes

