---
access: public
aliases: []
claim_ids:
- clm_09d62ac76346861c5250c09f4c03e51ac290af54e49b8f3e48e5fef49a12104a
- clm_1a23c614b449d4d7ea594f5b9c4901b3dae306223e81acfbd5f9654287f1a9bf
- clm_2645dabe9069d9a47af04ff9a4b5d947712ccec8ab0c7b55981dfa536c477978
- clm_4fa935151a36c536fc076b198fa44878e8f837a6733ab14f15f83aee37edac5a
- clm_8a40ccbd8d795b49dc352b92bef37fe6849453221580e18684295a9648af8f1a
- clm_923c828a6f724954742b410a10c08e973eec6d16e782642e7996cae13bffbb74
- clm_b369d52b3d01f40d769868025080a644495ca673efca8cbd0c057038ab74b1d9
- clm_b645e3c0662ca2a5a9fdf5ddcf4c9b7e0430bd63ddc001e63e480e2054670003
- clm_ccd64849fbb044bff936a20f20010f801c1510cad2591c1ca8533b0ffd5be5e2
- clm_d2036f108d0d212b3105b4a9f1c16632b19a6e364662b1b96e03f6ef2ada86c2
- clm_e73f74de04b51ff8b4812e523848ddc96891b8e2525c65e5ffdf9571fab9e3a3
- clm_f813c95272131e65c53f23b495196cc0d6309405c333b362afa41acc979f6f1c
maturity: draft
page_id: pg_e6a2c8a7cc3f5561b1bd2bdbbcb9955d
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_65d758f211325188919ceb047cf9c1a2
title: oooscoos/Benzi/README.md @ d9c7a3e63df7
updated_at: '2026-09-14T04:57:32Z'
---

# oooscoos/Benzi/README.md @ d9c7a3e63df7

<!-- rcw:begin owner=source:src_65d758f211325188919ceb047cf9c1a2 block=evidence -->
- Analysis depth varies by language: Python is deepest and the only language with runtime traces; execution is local-only and the agent does not browse the web. [@claim:clm_09d62ac76346861c5250c09f4c03e51ac290af54e49b8f3e48e5fef49a12104a]
- Every write passes syntax and semantic gates against the real language parser, and a broken parse auto-reverts the edit. [@claim:clm_1a23c614b449d4d7ea594f5b9c4901b3dae306223e81acfbd5f9654287f1a9bf]
- The README reports that a SWE-bench Verified run on DeepSeek v4-flash resolved 391/500 (78.2%) at $37.33 total, graded by the official harness in per-instance Docker containers with GitHub/PyPI network access blocked. [@claim:clm_2645dabe9069d9a47af04ff9a4b5d947712ccec8ab0c7b55981dfa536c477978]
- Benzi parses every project file with a tree-sitter-based compiler into a queryable map of symbols, call edges, references, and inheritance before answering questions. [@claim:clm_4fa935151a36c536fc076b198fa44878e8f837a6733ab14f15f83aee37edac5a]
- A runtime tracer hooks every call during execution and overlays observed behavior back onto the static map; a separate markup engine indexes HTML/CSS/DOM-JS including frontend embedded in Python strings. [@claim:clm_8a40ccbd8d795b49dc352b92bef37fe6849453221580e18684295a9648af8f1a]
- The index distinguishes proven edges (with evidence), ambiguous calls (full candidate lists kept), and runtime traces; unresolved calls are classified rather than silently dropped. [@claim:clm_923c828a6f724954742b410a10c08e973eec6d16e782642e7996cae13bffbb74]
- A 24-bug cross-harness comparison reports Benzi reading the fewest source lines (9,125 with Sonnet vs 20,704 for Claude Code) and roughly a cent per bug on DeepSeek, while Claude Code is said to reach $0.18 per step on harder bugs. [@claim:clm_b369d52b3d01f40d769868025080a644495ca673efca8cbd0c057038ab74b1d9]
- Tree-sitter is described as the only real dependency, with each of ten supported languages implemented as a grammar plugin. [@claim:clm_b645e3c0662ca2a5a9fdf5ddcf4c9b7e0430bd63ddc001e63e480e2054670003]
- The agent exposes 35+ tools; a sample of 16 includes get_callers, call_tree, trace_path, backflow, profile, skim_source, rollback_edit, and upgrade_to_pro. [@claim:clm_ccd64849fbb044bff936a20f20010f801c1510cad2591c1ca8533b0ffd5be5e2]
- Durable per-repo facts persist across restarts, so learned conventions are not re-derived each session. [@claim:clm_d2036f108d0d212b3105b4a9f1c16632b19a6e364662b1b96e03f6ef2ada86c2]
- Benzi is available as a browser demo (read-only, any public GitHub repo) and as a VS Code extension with edit access; there is no headless or CLI mode yet. [@claim:clm_e73f74de04b51ff8b4812e523848ddc96891b8e2525c65e5ffdf9571fab9e3a3]
- The project appears to be actively developed and free to use, with a live demo site, benchmark report, and VS Code Marketplace listing referenced from the README. [@claim:clm_f813c95272131e65c53f23b495196cc0d6309405c333b362afa41acc979f6f1c]
<!-- rcw:end owner=source:src_65d758f211325188919ceb047cf9c1a2 block=evidence -->

## Researcher notes

