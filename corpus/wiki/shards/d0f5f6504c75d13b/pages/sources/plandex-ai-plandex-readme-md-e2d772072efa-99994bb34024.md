---
access: public
aliases: []
claim_ids:
- clm_11d8896912c85ad2551d4ad021a0b389d066e33a31e2cfe24c6f2962e632d723
- clm_21e8d7e9844ea960732432c4c7a95e753138d318e2dc8c5a9b50fe14804a1e64
- clm_3c0fada2bfb9670067c86594af6a32fa6abb56b0359b721ff8c523a627a18603
- clm_4a67f0a93f8e4e3036478f701100eced0d136a9376641035ea7313f002827c66
- clm_4f11e11cde4ff9d452c519eb8e994dbfd432847afed02f82975a9cf3af0e70af
- clm_ae15e35f7f1917e14cfb45244c31139a49720356186108ddee4804587cf9316e
- clm_c35a717ca3fcd490df195dd1633307764d8e998ccf9fe70ca34b0ad040a6f727
- clm_fc25f4102f3fbd28d5c4237eb1eb71f8e4f6dc8895ec0b77e5aee5f5bbc6e3f6
- clm_ffae015681636e8aa38d4602296b922966e150148b50991081396eab813a5e1a
maturity: draft
page_id: pg_4cd26d27a05056fb947a99994bb34024
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_119ec9a457025664a2b07868a7c46610
title: plandex-ai/plandex/README.md @ e2d772072efa
updated_at: '2026-09-14T03:11:52Z'
---

# plandex-ai/plandex/README.md @ e2d772072efa

<!-- rcw:begin owner=source:src_119ec9a457025664a2b07868a7c46610 block=evidence -->
- Plandex Cloud is winding down as of 10/3/2025 and is no longer accepting new users; self-hosted/local mode with Docker and your own provider API keys is the documented alternative. [@claim:clm_11d8896912c85ad2551d4ad021a0b389d066e33a31e2cfe24c6f2962e632d723]
- Project maps and syntax validation are built on tree-sitter, with support for 30+ languages. [@claim:clm_21e8d7e9844ea960732432c4c7a95e753138d318e2dc8c5a9b50fe14804a1e64]
- AI-generated changes are kept in a cumulative diff review sandbox separate from project files until applied, with controlled command execution so changes can be rolled back and debugged. [@claim:clm_3c0fada2bfb9670067c86594af6a32fa6abb56b0359b721ff8c523a627a18603]
- The tool handles up to 2M tokens of context directly (~100k per file) and can index directories of 20M+ tokens using tree-sitter project maps, loading only what each step needs. [@claim:clm_4a67f0a93f8e4e3036478f701100eced0d136a9376641035ea7313f002827c66]
- Installation is a one-line, zero-dependency script (`curl -sL https://plandex.ai/install.sh | bash`), and Plandex can use a Claude Pro/Max subscription for Anthropic models, offered at first run. [@claim:clm_4f11e11cde4ff9d452c519eb8e994dbfd432847afed02f82975a9cf3af0e70af]
- On Windows, Plandex works only in the WSL shell; it does not work in the Windows CMD prompt or PowerShell. [@claim:clm_ae15e35f7f1917e14cfb45244c31139a49720356186108ddee4804587cf9316e]
- Plandex supports models from Anthropic, OpenAI, Google, and open-source providers, with curated model packs trading off capability, cost, and speed; context caching is used for OpenAI, Anthropic, and Google models. [@claim:clm_c35a717ca3fcd490df195dd1633307764d8e998ccf9fe70ca34b0ad040a6f727]
- Every plan update gets full-fledged version control, including branches for exploring multiple paths or comparing models, plus git integration with commit message generation and optional automatic commits. [@claim:clm_fc25f4102f3fbd28d5c4237eb1eb71f8e4f6dc8895ec0b77e5aee5f5bbc6e3f6]
- Plandex is a terminal-based AI coding tool offering both a REPL (started with `plandex` or `pdx`) and a CLI for scripting and piping data into context. [@claim:clm_ffae015681636e8aa38d4602296b922966e150148b50991081396eab813a5e1a]
<!-- rcw:end owner=source:src_119ec9a457025664a2b07868a7c46610 block=evidence -->

## Researcher notes

