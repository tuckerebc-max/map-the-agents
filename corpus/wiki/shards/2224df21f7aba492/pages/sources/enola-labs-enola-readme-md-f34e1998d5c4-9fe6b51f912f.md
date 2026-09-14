---
access: public
aliases: []
claim_ids:
- clm_12be7aae2975973d72f7e3158abfb3ec18b957082231bae78d7fd4913dd63900
- clm_13852f3c2da46286bcb81fc0a43532735ff05b758365dce8e93ef9fc3b23efe8
- clm_17ab7b4c5db75d06c2d0633b4b1556a4501c71674fda9031fb1b5f6bf2750457
- clm_30381593ac7bd0fe372d626ab85d94466bb8cc2a44ab9803156e2b25d6b35329
- clm_3abc2a8a413516a167aabdc54193d5aab26e3d7a57421fcd8a7febc94323827c
- clm_4036197ae948109e5e6509d36150809c5942d38b6720e970c93fdca589123429
- clm_4a37e51a604c5e223ed6909dfb7901109ace002c977661f5873a12a63de4d8eb
- clm_542cd0352f1b9b0c46c3f159e8d17856e6d2fe06721e4ffc471826c38e28ce1d
- clm_5a2f1a131fb798463a022fe9acde6cbd134976fa8cb43ff180e856cb224eb96f
- clm_65ae7c153485bac708252d00680e10c5267d22ed648d972211bafa6446dc65e7
- clm_65dddb94ae9f1f8264852000bc8570251295d5fab0a806088e5ac22dd0c748af
- clm_70441d945b106704853d1f6b588ac9f195990c2555d0f6a9c4be6421c38850ec
- clm_956ba2112f601871b425a5a32e040b1a049dd25f8f23105188bab4ceaee625a9
- clm_9f00cd44491716a4c0d31905d48cd028d4be5d145619c23e2d2757d24ab8cd73
- clm_bbe9ee0411bc8f0bb1f7adfe65dbdba7ca9ba39ce08d8686aaafa0c0fad4e949
- clm_c4e8dffc705d6d5d9604455e4e8c6b1c83098d5d5907292a740affe97ccd3051
- clm_c8269f58fafef5fb3e7ec45f72b80b0b501e8da1df970a13605ed65ca27f9214
- clm_f8ca93c57131625a6ae879718cf53c2cf256ec50b5dda62143862890d1e3d422
- clm_fc8bf2e743fb48171bbc4956e6a7b27b22154626741eaf0e03b66bee1c0199ba
maturity: draft
page_id: pg_257272b612b55a16ad8a9fe6b51f912f
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_1eced62061dc507897d6df530257edfe
title: enola-labs/enola/README.md @ f34e1998d5c4
updated_at: '2026-09-14T03:49:08Z'
---

# enola-labs/enola/README.md @ f34e1998d5c4

<!-- rcw:begin owner=source:src_1eced62061dc507897d6df530257edfe block=evidence -->
- A read-only local dashboard visualizes snapshots with findings, architectural changes, lifetime usage and diagnostics tabs, and shows the generation command when no snapshot exists. [@claim:clm_12be7aae2975973d72f7e3158abfb3ec18b957082231bae78d7fd4913dd63900]
- Most findings are advisory: across the benchmark corpus 96.3% could not fail a build under the default policy, and outlier thresholds are per-repository so a clean check means only that nothing new was introduced. [@claim:clm_13852f3c2da46286bcb81fc0a43532735ff05b758365dce8e93ef9fc3b23efe8]
- enola install --hooks writes instructions into agent-read files and adds hooks that grade each session; in opencode, which lacks such hooks, it installs a plugin that refuses the first grep/glob/list to surface the enola tool, bounded to two refusals. [@claim:clm_17ab7b4c5db75d06c2d0633b4b1556a4501c71674fda9031fb1b5f6bf2750457]
- By default no policy is set: all findings are reported, the run exits 0, and the output explicitly states that nothing was enforced. [@claim:clm_30381593ac7bd0fe372d626ab85d94466bb8cc2a44ab9803156e2b25d6b35329]
- The single binary is distributed via an install script, PyPI (enola-cli), Ruby gems, and package indexes, targeting Linux, macOS (amd64/arm64) and Windows without a Go toolchain or C compiler. [@claim:clm_3abc2a8a413516a167aabdc54193d5aab26e3d7a57421fcd8a7febc94323827c]
- enola check uses four exit codes: 0 for pass, 1 for a failing finding or spillover, 2 for a missing baseline or bad flag, and 3 for a baseline incomparable to the current code. [@claim:clm_4036197ae948109e5e6509d36150809c5942d38b6720e970c93fdca589123429]
- The install command previews every change and asks before writing, never creates shared files like AGENTS.md that did not already exist, and uninstall reverses everything byte-for-byte. [@claim:clm_4a37e51a604c5e223ed6909dfb7901109ace002c977661f5873a12a63de4d8eb]
- Cross-repo analysis joins clients and services into one graph, resolving route prefixes interprocedurally across files and packages, and enola coverage reports per service how many outbound calls could not be matched to a route. [@claim:clm_542cd0352f1b9b0c46c3f159e8d17856e6d2fe06721e4ffc471826c38e28ce1d]
- Enola exposes itself to coding agents as an MCP server launched via the command 'enola', with per-client setup for Claude Code, Copilot, Cursor, opencode and Codex. [@claim:clm_5a2f1a131fb798463a022fe9acde6cbd134976fa8cb43ff180e856cb224eb96f]
- Enola models only static structure and has no representation of runtime behavior such as timeouts, retry budgets, or message loss; the gate also grades only the delta, so pre-existing findings stay silent. [@claim:clm_65ae7c153485bac708252d00680e10c5267d22ed648d972211bafa6446dc65e7]
- Snapshots carry a receipt with enola's version, git ref, dirty-tree status, extractors used, and a sha256-based snapshot ID; baselines pinned by a different version or ignore rules are deemed incomparable until re-pinned. [@claim:clm_65dddb94ae9f1f8264852000bc8570251295d5fab0a806088e5ac22dd0c748af]
- Enola targets AI-assisted development where agents write code faster than humans can review, catching structural regressions like layer violations and scope spillover that builds and tests miss. [@claim:clm_70441d945b106704853d1f6b588ac9f195990c2555d0f6a9c4be6421c38850ec]
- Only cycles, intent, constraints and a declared layer order reach confidence 1.00; heuristic explainers are capped at 0.95, so gating on them requires lowering --min-confidence. [@claim:clm_956ba2112f601871b425a5a32e040b1a049dd25f8f23105188bab4ceaee625a9]
- Enola parses source with tree-sitter plus language-specific extractors, detecting 23 languages and formats automatically, with framework awareness for Go, Spring, Next.js, Angular, FastAPI, Django and others. [@claim:clm_9f00cd44491716a4c0d31905d48cd028d4be5d145619c23e2d2757d24ab8cd73]
- The tool computes its graph from parsed source with graph algorithms, using no language model, embeddings, upload, account, or license check. [@claim:clm_bbe9ee0411bc8f0bb1f7adfe65dbdba7ca9ba39ce08d8686aaafa0c0fad4e949]
- Enola maps a repository's structure before a change and compares it afterward, reporting only what that specific change introduced rather than pre-existing issues. [@claim:clm_c4e8dffc705d6d5d9604455e4e8c6b1c83098d5d5907292a740affe97ccd3051]
- The CLI includes commands such as enola --explain, baseline pin, check, doctor, dashboard, coverage, install --hooks, uninstall and upgrade, with flags like --fail-on, --min-confidence, --target and --max-spillover. [@claim:clm_c8269f58fafef5fb3e7ec45f72b80b0b501e8da1df970a13605ed65ca27f9214]
- Across 81 open-source repositories indexed three times each, all produced byte-identical snapshot IDs and fact files over 7.0 million facts with zero parse errors; warm re-index benchmarks include grafana at 7.5s and the Linux kernel at 52.6s. [@claim:clm_f8ca93c57131625a6ae879718cf53c2cf256ec50b5dda62143862890d1e3d422]
- Enola runs nineteen checks it calls explainers (e.g. layers, cycles, intent, god-class, hotspots, unused-routes, coverage) on every run; a policy flag decides which findings may set the exit code. [@claim:clm_fc8bf2e743fb48171bbc4956e6a7b27b22154626741eaf0e03b66bee1c0199ba]
<!-- rcw:end owner=source:src_1eced62061dc507897d6df530257edfe block=evidence -->

## Researcher notes

