# letstri/druk -- full detail

[Back to orientation](druk.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/letstri/druk/0027143d76ae68d2b7aeba87168a0f9e7142176c/b4006ea39e978a75.json](../../../wiki/dossiers/letstri/druk/0027143d76ae68d2b7aeba87168a0f9e7142176c/b4006ea39e978a75.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The app is a Solid application rendered to the terminal by OpenTUI, which supplies layout, text buffer, undo/redo, mouse hit-testing and the tree-sitter worker; the repo is the wiring around it. -- evidence: [ARCHITECTURE.md#L3-L6](https://github.com/letstri/druk/blob/0027143d76ae68d2b7aeba87168a0f9e7142176c/ARCHITECTURE.md#L3-L6) (`clm_6e2bc898058983798aa8946eb6f71cdcfab870b15b58d1820581a43bad0cf843`)

## design-choices (2 claim(s))

- [observation/documented] Extensions are JSON manifests, never code: installing one executes nothing, and manifests are read at startup with reload available via 'r' in the extensions panel. -- evidence: [README.md#L417-L422](https://github.com/letstri/druk/blob/0027143d76ae68d2b7aeba87168a0f9e7142176c/README.md#L417-L422), [ARCHITECTURE.md#L286-L291](https://github.com/letstri/druk/blob/0027143d76ae68d2b7aeba87168a0f9e7142176c/ARCHITECTURE.md#L286-L291) (`clm_cc6dfd0780483a2792d13ae3b92ad8c3e0d78e4390d6f2d0638042a3de825313`)
- [observation/documented] Settings live in two layers: a global config.json rewritten whole and a per-project .druk/settings.json of overrides that wins after merging. -- evidence: [ARCHITECTURE.md#L373-L380](https://github.com/letstri/druk/blob/0027143d76ae68d2b7aeba87168a0f9e7142176c/ARCHITECTURE.md#L373-L380) (`clm_53db1ddb3fbd397fc41e84bc33f89088fe682ca065ceb7d7586c89e18e455c3a`)

## workflows (3 claim(s))

- [observation/documented] Repository development practice: the extension market is a folder in this repo served raw from main, so a merged pull request makes an extension installable immediately; contributing one is a JSON file plus a PR. -- evidence: [ARCHITECTURE.md#L318-L322](https://github.com/letstri/druk/blob/0027143d76ae68d2b7aeba87168a0f9e7142176c/ARCHITECTURE.md#L318-L322), [README.md#L289-L292](https://github.com/letstri/druk/blob/0027143d76ae68d2b7aeba87168a0f9e7142176c/README.md#L289-L292), [README.md#L339-L340](https://github.com/letstri/druk/blob/0027143d76ae68d2b7aeba87168a0f9e7142176c/README.md#L339-L340) (`clm_1ea97589fc09cc3c9a5e2a5a8c20af49bddfd7f15319a0ec5b417763f9138c6a`)
- [observation/documented] Repository development practice: a boundary test fails the suite if ui/ or feature folders import from app/, enforcing one-way dependency direction. -- evidence: [ARCHITECTURE.md#L143-L153](https://github.com/letstri/druk/blob/0027143d76ae68d2b7aeba87168a0f9e7142176c/ARCHITECTURE.md#L143-L153) (`clm_917a7ec2031df2d25e238e9f3bd9fc3697cbae2f55d77be1dc75a59512c3db1b`)
- [observation/documented] Repository development practice: highlight queries should be compiled against their grammar and asserted in test/languages.test.ts, since bad queries fail silently. -- evidence: [ARCHITECTURE.md#L203-L206](https://github.com/letstri/druk/blob/0027143d76ae68d2b7aeba87168a0f9e7142176c/ARCHITECTURE.md#L203-L206) (`clm_3824115687f4cc94ace7178046d3b164211a05fda3dee54eac83d040d7f65454`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] Druk is a terminal code editor offering a file tree, tabs, search, PDF viewing, git marks, and syntax highlighting for 30+ languages, usable with keyboard and mouse. -- evidence: [README.md#L3-L4](https://github.com/letstri/druk/blob/0027143d76ae68d2b7aeba87168a0f9e7142176c/README.md#L3-L4) (`clm_8dc27333aac07ad2c116b035c8650fac1b25dada335761b672f954fcb83055ad`)
- [observation/documented] The CLI accepts a directory, a file, or a file with line/column (e.g. src/main.ts:42:7); npx and bunx work without installing. -- evidence: [README.md#L58-L64](https://github.com/letstri/druk/blob/0027143d76ae68d2b7aeba87168a0f9e7142176c/README.md#L58-L64), [README.md#L66-L66](https://github.com/letstri/druk/blob/0027143d76ae68d2b7aeba87168a0f9e7142176c/README.md#L66-L66) (`clm_78058d77cacd79537172b9114aa5000b5b02b9d1115ee8c2a5f3ae0b85be173d`)
- [observation/documented] F1 opens a command palette containing every feature; Ctrl+P fuzzy-opens files and Ctrl+K shows a transient strip of keys valid in the current pane. -- evidence: [README.md#L76-L92](https://github.com/letstri/druk/blob/0027143d76ae68d2b7aeba87168a0f9e7142176c/README.md#L76-L92) (`clm_f979a6de9d96a60ed4746574451b6ceec5c65d75edb7bbe051ae4453a384f7cc`)

## memory-state (2 claim(s))

- [observation/documented] Review notes persist in review.json beside the config, keyed by project, so an external agent can read and append answers while druk is open; answers reference a parent note id. -- evidence: [README.md#L241-L246](https://github.com/letstri/druk/blob/0027143d76ae68d2b7aeba87168a0f9e7142176c/README.md#L241-L246), [README.md#L224-L227](https://github.com/letstri/druk/blob/0027143d76ae68d2b7aeba87168a0f9e7142176c/README.md#L224-L227) (`clm_71bf604e8412f63257947af3bb028e4cb5bde25fefcc561b7c7b51fecfd94384`)
- [observation/documented] Druk remembers each project's open tabs, active file and expanded folders and restores them on the next open of that directory. -- evidence: [README.md#L278-L279](https://github.com/letstri/druk/blob/0027143d76ae68d2b7aeba87168a0f9e7142176c/README.md#L278-L279) (`clm_b90d760fdf0b3054128d8003b3c8ece1f9d565365349e3c54a489998cc968502`)

## orchestration (1 claim(s))

- [observation/documented] A filetype may have several language servers and all run concurrently; diagnostics are kept per sender and merged, while feature requests go to each ready server in turn with the first real answer winning. -- evidence: [ARCHITECTURE.md#L264-L272](https://github.com/letstri/druk/blob/0027143d76ae68d2b7aeba87168a0f9e7142176c/ARCHITECTURE.md#L264-L272) (`clm_5ecc33fbadd124697e74a982b0fe802ac7e9e0a3ee0dba791d70824c97974b5e`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Druk ships as one self-contained executable requiring no Node or Bun, distributed via install script, Homebrew, npm/bun launchers, .deb/.rpm, and release binaries for macOS, Linux and Windows. -- evidence: [README.md#L22-L24](https://github.com/letstri/druk/blob/0027143d76ae68d2b7aeba87168a0f9e7142176c/README.md#L22-L24), [README.md#L18-L20](https://github.com/letstri/druk/blob/0027143d76ae68d2b7aeba87168a0f9e7142176c/README.md#L18-L20), [README.md#L10-L10](https://github.com/letstri/druk/blob/0027143d76ae68d2b7aeba87168a0f9e7142176c/README.md#L10-L10), [README.md#L12-L14](https://github.com/letstri/druk/blob/0027143d76ae68d2b7aeba87168a0f9e7142176c/README.md#L12-L14), [README.md#L26-L28](https://github.com/letstri/druk/blob/0027143d76ae68d2b7aeba87168a0f9e7142176c/README.md#L26-L28), [README.md#L34-L35](https://github.com/letstri/druk/blob/0027143d76ae68d2b7aeba87168a0f9e7142176c/README.md#L34-L35), [README.md#L30-L32](https://github.com/letstri/druk/blob/0027143d76ae68d2b7aeba87168a0f9e7142176c/README.md#L30-L32) (`clm_a430b203a9162023bd6c5e191de86b6fd4f1e136a7ce1b514478476405b5235a`)

## limitations (1 claim(s))

- [observation/documented] PDF tabs are read-only, and corrupt, encrypted or unsupported PDFs stay closable while showing why they could not be rendered. -- evidence: [README.md#L151-L155](https://github.com/letstri/druk/blob/0027143d76ae68d2b7aeba87168a0f9e7142176c/README.md#L151-L155) (`clm_8b08e78c02254e2eec7ead41eacacce3e6faf9399a33fac7f0a8ca69a655e38f`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

