---
access: public
aliases: []
claim_ids:
- clm_131d88c79568389693c0823e748ade39c45712cccc5971f6d61ea9a9c2a8e461
- clm_4866bb9642529f95ae4cca923fde2a3abbf83f0dd82cbe9761050a175f444f9b
- clm_a6fbf314d1e399f0be2495ec00624f3f82338299fa7a679e01bd9ae0c1d83aa5
- clm_acc13d43e32f438a4368464e6c7b3702c5b9f23e2bf13d94e75772d93b6a135b
- clm_baa1e7a57911f79245ef86de0c134645beb291a6dd3b7d096491a7807dbd84c4
maturity: draft
page_id: pg_4fcb65d85c14532f96e0c60babb00ceb
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_7a000dc988405f3fa1dacecdde66dacd
title: google-gemini/gemini-cli/docs/cli/sandbox.md @ 9c1b0a610534
updated_at: '2026-09-14T02:01:21Z'
---

# google-gemini/gemini-cli/docs/cli/sandbox.md @ 9c1b0a610534

<!-- rcw:begin owner=source:src_7a000dc988405f3fa1dacecdde66dacd block=evidence -->
- Tool-level sandboxing isolates individual tool executions such as shell_exec and write_file, and can be disabled via security.toolSandboxing=false in settings.json (restart required). [@claim:clm_131d88c79568389693c0823e748ade39c45712cccc5971f6d61ea9a9c2a8e461]
- LXC sandboxing is Linux-only and requires the container to already exist and be running, as Gemini does not create it automatically. [@claim:clm_4866bb9642529f95ae4cca923fde2a3abbf83f0dd82cbe9761050a175f444f9b]
- Sandboxing can be enabled via the -s/--sandbox flag, the GEMINI_SANDBOX env var, or settings.json, with providers including docker, podman, sandbox-exec, runsc, and lxc. [@claim:clm_a6fbf314d1e399f0be2495ec00624f3f82338299fa7a679e01bd9ae0c1d83aa5]
- CLI flags include --include-directories for multiple directories, -m for model selection, and -s for sandboxing. [@claim:clm_acc13d43e32f438a4368464e6c7b3702c5b9f23e2bf13d94e75772d93b6a135b]
- A sandbox expansion mechanism detects permission denials or proactively identified needs and shows a modal request; approval grants extended permissions for that specific run. [@claim:clm_baa1e7a57911f79245ef86de0c134645beb291a6dd3b7d096491a7807dbd84c4]
<!-- rcw:end owner=source:src_7a000dc988405f3fa1dacecdde66dacd block=evidence -->

## Researcher notes

