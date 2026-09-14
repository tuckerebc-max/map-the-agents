---
access: public
aliases: []
claim_ids:
- clm_020a496a591bcacc57dc87e0a3dcf7401640c6e3e1128853ba970b17fb82ebe7
- clm_16ad7ac3f1bb1bc1b0eee0e21bd983a2faa14e55e5129d60c20e2fb8c8e0e9ab
- clm_3545dc45d9b7ad479e2c620228964c63671d24e94377e6814db097a6c512f092
- clm_6aa395684bce4bc756bb56e6d7a535a88804a7a56c6b15f67ba6af213c1fdaae
- clm_77520a9f5f9f5181495cb44caca0365d9a205b40aa0f34d2ddbdac3e0bda989a
- clm_9eb24386eb08953c860267c104b348ed50e7cdcc328b18c4d47e2c62583b44f9
- clm_a5cf3e5c13cf84d1175817479e9b17a39f8dd35f9f3e5c88d179a86fe9697aa8
- clm_beb97569d494bc062e86ddd6ffe7a1bd7b1d273af53365716936762caac39830
- clm_c173eb70a76e93de12a84d0fb32d7f022d42b77c8f5facbfe3596e47887ddd20
- clm_daf1e6e7c86ca43435b0d4dea6aeef9eb60326b604f33b1f7698510de294f8e4
- clm_ebaacd428ce48ed5c86ba840771f868324e5ee616cb4c0486337f474da618095
- clm_ebfe153201e4121ed4c396c411725a8a6b69e32bf6b230a052ec0bb5ce5c779b
maturity: draft
page_id: pg_61342faa768c5083913316ef66fab25d
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_4529e061c00b5176944c21cbceb4a9b3
title: get-vix/vix/README.md @ 8e4262d6d1a8
updated_at: '2026-09-14T01:51:04Z'
---

# get-vix/vix/README.md @ 8e4262d6d1a8

<!-- rcw:begin owner=source:src_4529e061c00b5176944c21cbceb4a9b3 block=evidence -->
- Vix ships built-in provider support for Anthropic, OpenAI, OpenRouter, OrcaRouter, AWS Bedrock, Ollama, llama.cpp, and Lemonade, among others. [@claim:clm_020a496a591bcacc57dc87e0a3dcf7401640c6e3e1128853ba970b17fb82ebe7]
- Rather than limiting exploration, vix strips whitespace characters from file content via a virtual filesystem so the LLM works on minified code, reportedly reducing tokens by 20-50%. [@claim:clm_16ad7ac3f1bb1bc1b0eee0e21bd983a2faa14e55e5129d60c20e2fb8c8e0e9ab]
- The product consists of a daemon (vixd) and a client (vix); the daemon is started first, and multiple isolated vix instances can then be run. [@claim:clm_3545dc45d9b7ad479e2c620228964c63671d24e94377e6814db097a6c512f092]
- Vix is described as a fast, token-efficient AI coding agent whose stem agents maximize prompt-cache reuse across phases and whose Tree-sitter virtual filesystem lets it read and edit minified code, claimed to cut tokens 20-50%. [@claim:clm_6aa395684bce4bc756bb56e6d7a535a88804a7a56c6b15f67ba6af213c1fdaae]
- Users can define multi-phase agent pipelines in JSON with agent, bash, and tool steps, including templating, branching, parallelism, and history forking; custom workflows are configured in settings.json. [@claim:clm_77520a9f5f9f5181495cb44caca0365d9a205b40aa0f34d2ddbdac3e0bda989a]
- The stem-agent design uses a generic system prompt with per-phase instructions delivered as user messages, so the explore-phase history stays cached when the LLM is told to act as a planner. [@claim:clm_9eb24386eb08953c860267c104b348ed50e7cdcc328b18c4d47e2c62583b44f9]
- Vix advertises standard agent capabilities including skills, MCP servers, subagents, LSP-backed code intelligence, sandboxed execution, and multiple providers. [@claim:clm_a5cf3e5c13cf84d1175817479e9b17a39f8dd35f9f3e5c88d179a86fe9697aa8]
- Installation is via a curl-piped install script or Homebrew tap (get-vix/vix), and requires ANTHROPIC_API_KEY to be set in the environment. [@claim:clm_beb97569d494bc062e86ddd6ffe7a1bd7b1d273af53365716936762caac39830]
- The README reports a self-described non-scientific benchmark of vix plan mode against Claude Code on 7 real coding scenarios with the same prompt, measuring time and cost, with reproducible transcripts in a separate vix-eval repo; vix was faster and cheaper on almost all tasks. [@claim:clm_c173eb70a76e93de12a84d0fb32d7f022d42b77c8f5facbfe3596e47887ddd20]
- The benchmark summary notes vix lost on one task involving a 3,000+ line file, because minification only helped during exploration while execution fell back to regular read/edit tools. [@claim:clm_daf1e6e7c86ca43435b0d4dea6aeef9eb60326b604f33b1f7698510de294f8e4]
- The README warns that vix currently works only on macOS and Linux. [@claim:clm_ebaacd428ce48ed5c86ba840771f868324e5ee616cb4c0486337f474da618095]
- Providers are configured via a providers.json overlay in ~/.vix/ or ./.vix/ merged over an embedded base: same-id entries are field-patched, new ids appended, and models/credential_methods arrays replace wholesale. [@claim:clm_ebfe153201e4121ed4c396c411725a8a6b69e32bf6b230a052ec0bb5ce5c779b]
<!-- rcw:end owner=source:src_4529e061c00b5176944c21cbceb4a9b3 block=evidence -->

## Researcher notes

