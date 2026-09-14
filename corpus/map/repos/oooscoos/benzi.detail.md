# oooscoos/benzi -- full detail

[Back to orientation](benzi.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/oooscoos/benzi/d9c7a3e63df77e16ef9618edc3a0d95b08758056/69afc1120b591d6f.json](../../../wiki/dossiers/oooscoos/benzi/d9c7a3e63df77e16ef9618edc3a0d95b08758056/69afc1120b591d6f.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] A runtime tracer hooks every call during execution and overlays observed behavior back onto the static map; a separate markup engine indexes HTML/CSS/DOM-JS including frontend embedded in Python strings. -- evidence: [README.md#L148-L154](https://github.com/oooscoos/Benzi/blob/d9c7a3e63df77e16ef9618edc3a0d95b08758056/README.md#L148-L154) (`clm_8a40ccbd8d795b49dc352b92bef37fe6849453221580e18684295a9648af8f1a`)

## design-choices (2 claim(s))

- [observation/documented] Benzi parses every project file with a tree-sitter-based compiler into a queryable map of symbols, call edges, references, and inheritance before answering questions. -- evidence: [README.md#L34-L34](https://github.com/oooscoos/Benzi/blob/d9c7a3e63df77e16ef9618edc3a0d95b08758056/README.md#L34-L34), [README.md#L36-L36](https://github.com/oooscoos/Benzi/blob/d9c7a3e63df77e16ef9618edc3a0d95b08758056/README.md#L36-L36) (`clm_4fa935151a36c536fc076b198fa44878e8f837a6733ab14f15f83aee37edac5a`)
- [observation/documented] The index distinguishes proven edges (with evidence), ambiguous calls (full candidate lists kept), and runtime traces; unresolved calls are classified rather than silently dropped. -- evidence: [README.md#L148-L154](https://github.com/oooscoos/Benzi/blob/d9c7a3e63df77e16ef9618edc3a0d95b08758056/README.md#L148-L154) (`clm_923c828a6f724954742b410a10c08e973eec6d16e782642e7996cae13bffbb74`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] Benzi is available as a browser demo (read-only, any public GitHub repo) and as a VS Code extension with edit access; there is no headless or CLI mode yet. -- evidence: [README.md#L168-L169](https://github.com/oooscoos/Benzi/blob/d9c7a3e63df77e16ef9618edc3a0d95b08758056/README.md#L168-L169), [README.md#L171-L171](https://github.com/oooscoos/Benzi/blob/d9c7a3e63df77e16ef9618edc3a0d95b08758056/README.md#L171-L171) (`clm_e73f74de04b51ff8b4812e523848ddc96891b8e2525c65e5ffdf9571fab9e3a3`)

## memory-state (1 claim(s))

- [observation/documented] Durable per-repo facts persist across restarts, so learned conventions are not re-derived each session. -- evidence: [README.md#L148-L154](https://github.com/oooscoos/Benzi/blob/d9c7a3e63df77e16ef9618edc3a0d95b08758056/README.md#L148-L154) (`clm_d2036f108d0d212b3105b4a9f1c16632b19a6e364662b1b96e03f6ef2ada86c2`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (2 claim(s))

- [observation/documented] The agent exposes 35+ tools; a sample of 16 includes get_callers, call_tree, trace_path, backflow, profile, skim_source, rollback_edit, and upgrade_to_pro. -- evidence: [README.md#L85-L85](https://github.com/oooscoos/Benzi/blob/d9c7a3e63df77e16ef9618edc3a0d95b08758056/README.md#L85-L85), [README.md#L87-L104](https://github.com/oooscoos/Benzi/blob/d9c7a3e63df77e16ef9618edc3a0d95b08758056/README.md#L87-L104) (`clm_ccd64849fbb044bff936a20f20010f801c1510cad2591c1ca8533b0ffd5be5e2`)
- [observation/documented] Every write passes syntax and semantic gates against the real language parser, and a broken parse auto-reverts the edit. -- evidence: [README.md#L108-L111](https://github.com/oooscoos/Benzi/blob/d9c7a3e63df77e16ef9618edc3a0d95b08758056/README.md#L108-L111) (`clm_1a23c614b449d4d7ea594f5b9c4901b3dae306223e81acfbd5f9654287f1a9bf`)

## evaluation (2 claim(s))

- [observation/documented] The README reports that a SWE-bench Verified run on DeepSeek v4-flash resolved 391/500 (78.2%) at $37.33 total, graded by the official harness in per-instance Docker containers with GitHub/PyPI network access blocked. -- evidence: [README.md#L54-L54](https://github.com/oooscoos/Benzi/blob/d9c7a3e63df77e16ef9618edc3a0d95b08758056/README.md#L54-L54), [README.md#L56-L64](https://github.com/oooscoos/Benzi/blob/d9c7a3e63df77e16ef9618edc3a0d95b08758056/README.md#L56-L64) (`clm_2645dabe9069d9a47af04ff9a4b5d947712ccec8ab0c7b55981dfa536c477978`)
- [observation/documented] A 24-bug cross-harness comparison reports Benzi reading the fewest source lines (9,125 with Sonnet vs 20,704 for Claude Code) and roughly a cent per bug on DeepSeek, while Claude Code is said to reach $0.18 per step on harder bugs. -- evidence: [README.md#L117-L122](https://github.com/oooscoos/Benzi/blob/d9c7a3e63df77e16ef9618edc3a0d95b08758056/README.md#L117-L122), [README.md#L115-L115](https://github.com/oooscoos/Benzi/blob/d9c7a3e63df77e16ef9618edc3a0d95b08758056/README.md#L115-L115), [README.md#L142-L142](https://github.com/oooscoos/Benzi/blob/d9c7a3e63df77e16ef9618edc3a0d95b08758056/README.md#L142-L142) (`clm_b369d52b3d01f40d769868025080a644495ca673efca8cbd0c057038ab74b1d9`)

## dependencies (1 claim(s))

- [observation/documented] Tree-sitter is described as the only real dependency, with each of ten supported languages implemented as a grammar plugin. -- evidence: [README.md#L160-L160](https://github.com/oooscoos/Benzi/blob/d9c7a3e63df77e16ef9618edc3a0d95b08758056/README.md#L160-L160) (`clm_b645e3c0662ca2a5a9fdf5ddcf4c9b7e0430bd63ddc001e63e480e2054670003`)

## limitations (1 claim(s))

- [observation/documented] Analysis depth varies by language: Python is deepest and the only language with runtime traces; execution is local-only and the agent does not browse the web. -- evidence: [README.md#L162-L162](https://github.com/oooscoos/Benzi/blob/d9c7a3e63df77e16ef9618edc3a0d95b08758056/README.md#L162-L162) (`clm_09d62ac76346861c5250c09f4c03e51ac290af54e49b8f3e48e5fef49a12104a`)

## relevance (1 claim(s))

- [inference/documented] The project appears to be actively developed and free to use, with a live demo site, benchmark report, and VS Code Marketplace listing referenced from the README. -- evidence: [README.md#L40-L50](https://github.com/oooscoos/Benzi/blob/d9c7a3e63df77e16ef9618edc3a0d95b08758056/README.md#L40-L50), [README.md#L14-L14](https://github.com/oooscoos/Benzi/blob/d9c7a3e63df77e16ef9618edc3a0d95b08758056/README.md#L14-L14), [README.md#L16-L22](https://github.com/oooscoos/Benzi/blob/d9c7a3e63df77e16ef9618edc3a0d95b08758056/README.md#L16-L22) (`clm_f813c95272131e65c53f23b495196cc0d6309405c333b362afa41acc979f6f1c`)

Superseded claim IDs (kept as history): clm_06c3a6f60a6dbc20ca3c0b51c17b304eb008beb02514c7f9d692fd2d3d258fc8, clm_0f34b585a879ab919c2158c6a479cc5f2e3743ceee0840a45b89b232677043fd

