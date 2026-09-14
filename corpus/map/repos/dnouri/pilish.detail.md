# dnouri/pilish -- full detail

[Back to orientation](pilish.md)

## Origins

- github-verified-rename
- alltheagents.org-backing

## Projects

- Observatory

Full evidence record (JSON): [wiki/dossiers/dnouri/pilish/894d1e7be124ecbdfcb203d9c22b627b61620ace/5f45544ad87d0a76.json](../../../wiki/dossiers/dnouri/pilish/894d1e7be124ecbdfcb203d9c22b627b61620ace/5f45544ad87d0a76.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (12 claim(s))

- [observation/documented] Repository development practice: the guide describes Pilish as an Emacs frontend for the pi coding agent with a two-window UI (markdown chat buffer plus prompt composition buffer) communicating with the pi CLI via JSON-over-stdio RPC. -- evidence: [AGENTS.md#L3-L5](https://github.com/dnouri/pilish/blob/894d1e7be124ecbdfcb203d9c22b627b61620ace/AGENTS.md#L3-L5) (`clm_87f7085f1094786deaf287d46a1249ac226d434677b7b819b217ba98bbf14418`)
- [observation/documented] Repository development practice: the guide documents ten production source modules forming an acyclic dependency DAG, plus an optional Evil integration module, with the internal require edges listed explicitly. -- evidence: [AGENTS.md#L9-L10](https://github.com/dnouri/pilish/blob/894d1e7be124ecbdfcb203d9c22b627b61620ace/AGENTS.md#L9-L10), [AGENTS.md#L12-L22](https://github.com/dnouri/pilish/blob/894d1e7be124ecbdfcb203d9c22b627b61620ace/AGENTS.md#L12-L22), [AGENTS.md#L24-L25](https://github.com/dnouri/pilish/blob/894d1e7be124ecbdfcb203d9c22b627b61620ace/AGENTS.md#L24-L25) (`clm_28421fa6da09a31cbe2b05288a7aa76b211a3f595b480e0e68d9b8d947555665`)
- [observation/documented] Repository development practice: per the guide, menu and UI only declare browser entry points without requiring browse, and the top-level load order makes those commands available without introducing a cycle. -- evidence: [AGENTS.md#L27-L31](https://github.com/dnouri/pilish/blob/894d1e7be124ecbdfcb203d9c22b627b61620ace/AGENTS.md#L27-L31) (`clm_9ec99a665a8697f62c813dae9afd546c9391d571e3a8592492a6423f143178e0`)
- [observation/documented] Repository development practice: the guide lists md-ts-mode (a tree-sitter markdown major mode used by chat buffers) as an external package dependency, noting loading pilish must not globally claim unrelated Markdown files. -- evidence: [AGENTS.md#L33-L33](https://github.com/dnouri/pilish/blob/894d1e7be124ecbdfcb203d9c22b627b61620ace/AGENTS.md#L33-L33), [AGENTS.md#L35-L36](https://github.com/dnouri/pilish/blob/894d1e7be124ecbdfcb203d9c22b627b61620ace/AGENTS.md#L35-L36) (`clm_c1d545b0241e4d54b790efb955844cb27508ad645341d0d9429659b097a06392`)
- [observation/documented] Repository development practice: the guide states shared session state lives in ui.el, that menu.el and input.el are siblings requiring neither the other, and that cross-module state mutations use accessor functions like --set-process defined in ui.el. -- evidence: [AGENTS.md#L38-L40](https://github.com/dnouri/pilish/blob/894d1e7be124ecbdfcb203d9c22b627b61620ace/AGENTS.md#L38-L40), [AGENTS.md#L42-L44](https://github.com/dnouri/pilish/blob/894d1e7be124ecbdfcb203d9c22b627b61620ace/AGENTS.md#L42-L44) (`clm_f38a9621519a66cdd96ba8240e0bdd3db6058a71bbde74facbb29beafdfd2d11`)
- [observation/documented] Repository development practice: the guide maps each source file to a purpose, e.g. pilish-core.el for JSON parsing, line buffering, RPC request correlation and process protocol, and pilish-browse.el for magit-section session/tree browsers with disk session discovery. -- evidence: [AGENTS.md#L61-L73](https://github.com/dnouri/pilish/blob/894d1e7be124ecbdfcb203d9c22b627b61620ace/AGENTS.md#L61-L73) (`clm_05fb22cc556cb12e8958a6e87ce59c7774e5917e3b11ef4b0eaac3b19242370e`)
- [observation/documented] Repository development practice: tests are run with 'make test', per-module targets such as make test-core and make test-browse, integration targets (fake/real), and ERT regexp SELECTOR filtering; VERBOSE=1 yields full raw ERT output. -- evidence: [AGENTS.md#L161-L166](https://github.com/dnouri/pilish/blob/894d1e7be124ecbdfcb203d9c22b627b61620ace/AGENTS.md#L161-L166), [AGENTS.md#L148-L154](https://github.com/dnouri/pilish/blob/894d1e7be124ecbdfcb203d9c22b627b61620ace/AGENTS.md#L148-L154), [AGENTS.md#L141-L146](https://github.com/dnouri/pilish/blob/894d1e7be124ecbdfcb203d9c22b627b61620ace/AGENTS.md#L141-L146), [AGENTS.md#L129-L139](https://github.com/dnouri/pilish/blob/894d1e7be124ecbdfcb203d9c22b627b61620ace/AGENTS.md#L129-L139), [AGENTS.md#L124-L127](https://github.com/dnouri/pilish/blob/894d1e7be124ecbdfcb203d9c22b627b61620ace/AGENTS.md#L124-L127) (`clm_fbd3bab31071cd6e948e7cca76424c999ceea8a861b5ffab1acba54b364893c0`)
- [observation/documented] Repository development practice: benchmark make targets cover table rendering, reload/resume, tool-update storm, and deferred agent_end cooling lanes, with GUI (xvfb) lanes primary and batch lanes as quick sanity checks; correctness errors, not timing thresholds, fail the runs. -- evidence: [AGENTS.md#L188-L206](https://github.com/dnouri/pilish/blob/894d1e7be124ecbdfcb203d9c22b627b61620ace/AGENTS.md#L188-L206), [AGENTS.md#L174-L186](https://github.com/dnouri/pilish/blob/894d1e7be124ecbdfcb203d9c22b627b61620ace/AGENTS.md#L174-L186) (`clm_e3c0e0162f482a101b7d3f22f3df67752623c1cee27f833fac7e1f5a294f4657`)
- [observation/documented] Repository development practice: linting uses make lint (checkdoc plus package-lint), make check-parens, and make check (byte-compile, lint, all tests) which equals the pre-commit hook; the hook runs scripts/check.sh and can be skipped with --no-verify. -- evidence: [AGENTS.md#L225-L226](https://github.com/dnouri/pilish/blob/894d1e7be124ecbdfcb203d9c22b627b61620ace/AGENTS.md#L225-L226), [AGENTS.md#L210-L216](https://github.com/dnouri/pilish/blob/894d1e7be124ecbdfcb203d9c22b627b61620ace/AGENTS.md#L210-L216), [AGENTS.md#L228-L228](https://github.com/dnouri/pilish/blob/894d1e7be124ecbdfcb203d9c22b627b61620ace/AGENTS.md#L228-L228) (`clm_5b0700c8e9b8756733618e91ed08d358ca8d99aa44d1addf04f9e4472fb033a0`)
- [observation/documented] Repository development practice: 'make test' auto-installs the Emacs package dependencies transient, magit-section, and md-ts-mode on first run, caching via a .deps-stamp file, with 'make clean' forcing reinstall. -- evidence: [AGENTS.md#L220-L221](https://github.com/dnouri/pilish/blob/894d1e7be124ecbdfcb203d9c22b627b61620ace/AGENTS.md#L220-L221) (`clm_f1f3fbf24bdad8f81c2fbf77e84a0e1dfb2180724ce4ef76a7d69350e980572f`)
- [observation/documented] Repository development practice: the guide prescribes tmux-based spike scripts under gitignored ./tmp/ for reproducing visual bugs, including required boilerplate, -Q launch caveats, and buffer naming patterns like *pilish-chat:<dir>*. -- evidence: [AGENTS.md#L263-L270](https://github.com/dnouri/pilish/blob/894d1e7be124ecbdfcb203d9c22b627b61620ace/AGENTS.md#L263-L270), [AGENTS.md#L232-L233](https://github.com/dnouri/pilish/blob/894d1e7be124ecbdfcb203d9c22b627b61620ace/AGENTS.md#L232-L233), [AGENTS.md#L235-L243](https://github.com/dnouri/pilish/blob/894d1e7be124ecbdfcb203d9c22b627b61620ace/AGENTS.md#L235-L243) (`clm_630f48d9e8f43abfb053307e5de7db27c22753338d8c71355b0e28e6393690ca`)
- [observation/documented] Repository development practice: conventions include the pilish- prefix for public symbols, pilish-- for internal ones, pilish-test-<description> test names, git add of specific files rather than -A, and consulting the pi CLI (TypeScript) source as the RPC protocol reference. -- evidence: [AGENTS.md#L312-L314](https://github.com/dnouri/pilish/blob/894d1e7be124ecbdfcb203d9c22b627b61620ace/AGENTS.md#L312-L314), [AGENTS.md#L318-L321](https://github.com/dnouri/pilish/blob/894d1e7be124ecbdfcb203d9c22b627b61620ace/AGENTS.md#L318-L321), [AGENTS.md#L274-L276](https://github.com/dnouri/pilish/blob/894d1e7be124ecbdfcb203d9c22b627b61620ace/AGENTS.md#L274-L276) (`clm_621d9b1aed1153e5e33616ce943e744a94616a5bf15edea4a435ab6a4c1786c4`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

