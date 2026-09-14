# fission-ai/openspec -- full detail

[Back to orientation](openspec.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/fission-ai/openspec/9d4e5974e5c0d9a09b9c6c1e1eb0975e80ec4461/01249e4603bb0f5e.json](../../../wiki/dossiers/fission-ai/openspec/9d4e5974e5c0d9a09b9c6c1e1eb0975e80ec4461/01249e4603bb0f5e.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (3 claim(s))

- [observation/documented] Specs are plain Markdown with requirements and concrete scenarios and no special syntax to learn; each change gets its own folder containing proposal, specs, design, and tasks artifacts. -- evidence: [README.md#L82-L82](https://github.com/Fission-AI/OpenSpec/blob/9d4e5974e5c0d9a09b9c6c1e1eb0975e80ec4461/README.md#L82-L82), [README.md#L58-L64](https://github.com/Fission-AI/OpenSpec/blob/9d4e5974e5c0d9a09b9c6c1e1eb0975e80ec4461/README.md#L58-L64), [README.md#L190-L193](https://github.com/Fission-AI/OpenSpec/blob/9d4e5974e5c0d9a09b9c6c1e1eb0975e80ec4461/README.md#L190-L193) (`clm_ce515a991e4e4029df4ea6f024dcda4b6850f596c99728a2d58bae56500b3de3`)
- [observation/documented] The stated philosophy favors fluid, iterative workflows over rigid phase gates, targeting brownfield projects and scaling from personal projects to enterprises. -- evidence: [README.md#L28-L34](https://github.com/Fission-AI/OpenSpec/blob/9d4e5974e5c0d9a09b9c6c1e1eb0975e80ec4461/README.md#L28-L34), [README.md#L197-L197](https://github.com/Fission-AI/OpenSpec/blob/9d4e5974e5c0d9a09b9c6c1e1eb0975e80ec4461/README.md#L197-L197), [README.md#L190-L193](https://github.com/Fission-AI/OpenSpec/blob/9d4e5974e5c0d9a09b9c6c1e1eb0975e80ec4461/README.md#L190-L193) (`clm_0acdf504db33a39dd2384f698e4feedc45531e9fcdf3e6888e8303325132ed4e`)
- [observation/documented] OpenSpec collects anonymous telemetry limited to command names and version, disabled automatically in CI, with opt-out via config or OPENSPEC_TELEMETRY/DO_NOT_TRACK environment variables. -- evidence: [README.md#L238-L238](https://github.com/Fission-AI/OpenSpec/blob/9d4e5974e5c0d9a09b9c6c1e1eb0975e80ec4461/README.md#L238-L238), [README.md#L240-L242](https://github.com/Fission-AI/OpenSpec/blob/9d4e5974e5c0d9a09b9c6c1e1eb0975e80ec4461/README.md#L240-L242), [README.md#L236-L236](https://github.com/Fission-AI/OpenSpec/blob/9d4e5974e5c0d9a09b9c6c1e1eb0975e80ec4461/README.md#L236-L236) (`clm_aa6f12ede55e354d8e764ce322a96e3c372fbac0885147bd9a059d02d108c217`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: contributors should open a discussion or issue before a PR and link it; new features, significant refactors, and architectural changes require an OpenSpec change proposal first, with details in CONTRIBUTING.md. -- evidence: [README.md#L227-L227](https://github.com/Fission-AI/OpenSpec/blob/9d4e5974e5c0d9a09b9c6c1e1eb0975e80ec4461/README.md#L227-L227), [README.md#L229-L229](https://github.com/Fission-AI/OpenSpec/blob/9d4e5974e5c0d9a09b9c6c1e1eb0975e80ec4461/README.md#L229-L229) (`clm_c01d5b8f8615df92088917ac0bb275bff94f10ad9b83d655a874dcda3bcc4e1c`)
- [observation/documented] Repository development practice: install.md is an agent-facing setup prompt directing the installing agent to verify Node, install the CLI globally with user confirmation, run openspec init --tools, and report what init actually created. -- evidence: [install.md#L64-L64](https://github.com/Fission-AI/OpenSpec/blob/9d4e5974e5c0d9a09b9c6c1e1eb0975e80ec4461/install.md#L64-L64), [install.md#L5-L5](https://github.com/Fission-AI/OpenSpec/blob/9d4e5974e5c0d9a09b9c6c1e1eb0975e80ec4461/install.md#L5-L5), [install.md#L17-L21](https://github.com/Fission-AI/OpenSpec/blob/9d4e5974e5c0d9a09b9c6c1e1eb0975e80ec4461/install.md#L17-L21) (`clm_ac33c0f7ea1d148c315cbb9d2e9331a0a435acbf08e632d7cc9d657f2255fb0e`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] OpenSpec is driven from AI coding tools via slash commands such as /opsx:explore, /opsx:propose, /opsx:apply, and /opsx:archive, with tool-specific spellings like /opsx-propose (Cursor, Copilot), @opsx-propose (Amazon Q), or $openspec-propose (Codex). -- evidence: [README.md#L66-L72](https://github.com/Fission-AI/OpenSpec/blob/9d4e5974e5c0d9a09b9c6c1e1eb0975e80ec4461/README.md#L66-L72), [install.md#L66-L66](https://github.com/Fission-AI/OpenSpec/blob/9d4e5974e5c0d9a09b9c6c1e1eb0975e80ec4461/install.md#L66-L66), [README.md#L74-L77](https://github.com/Fission-AI/OpenSpec/blob/9d4e5974e5c0d9a09b9c6c1e1eb0975e80ec4461/README.md#L74-L77), [README.md#L58-L64](https://github.com/Fission-AI/OpenSpec/blob/9d4e5974e5c0d9a09b9c6c1e1eb0975e80ec4461/README.md#L58-L64), [README.md#L149-L149](https://github.com/Fission-AI/OpenSpec/blob/9d4e5974e5c0d9a09b9c6c1e1eb0975e80ec4461/README.md#L149-L149), [README.md#L49-L56](https://github.com/Fission-AI/OpenSpec/blob/9d4e5974e5c0d9a09b9c6c1e1eb0975e80ec4461/README.md#L49-L56) (`clm_d2da4b46c34912e686ae17ecf9bb610008b2ce226f9a8cc2d0929ac48159753d`)
- [observation/documented] The product ships a CLI installed globally via npm, pnpm, yarn, or bun (with a Nix option), with commands including openspec init, openspec update, and openspec config profile. -- evidence: [install.md#L33-L38](https://github.com/Fission-AI/OpenSpec/blob/9d4e5974e5c0d9a09b9c6c1e1eb0975e80ec4461/install.md#L33-L38), [README.md#L135-L138](https://github.com/Fission-AI/OpenSpec/blob/9d4e5974e5c0d9a09b9c6c1e1eb0975e80ec4461/README.md#L135-L138), [README.md#L129-L131](https://github.com/Fission-AI/OpenSpec/blob/9d4e5974e5c0d9a09b9c6c1e1eb0975e80ec4461/README.md#L129-L131), [README.md#L215-L217](https://github.com/Fission-AI/OpenSpec/blob/9d4e5974e5c0d9a09b9c6c1e1eb0975e80ec4461/README.md#L215-L217), [README.md#L147-L147](https://github.com/Fission-AI/OpenSpec/blob/9d4e5974e5c0d9a09b9c6c1e1eb0975e80ec4461/README.md#L147-L147), [README.md#L207-L209](https://github.com/Fission-AI/OpenSpec/blob/9d4e5974e5c0d9a09b9c6c1e1eb0975e80ec4461/README.md#L207-L209) (`clm_fdc4018060eb05485d101a2401b5a598f4f45a67d9b30d460d4e00466788ae4f`)
- [observation/documented] openspec init --tools <ids> generates per-tool skill and command files for the selected AI assistants, and the README claims support for 30+ tools. -- evidence: [install.md#L56-L56](https://github.com/Fission-AI/OpenSpec/blob/9d4e5974e5c0d9a09b9c6c1e1eb0975e80ec4461/install.md#L56-L56), [README.md#L147-L147](https://github.com/Fission-AI/OpenSpec/blob/9d4e5974e5c0d9a09b9c6c1e1eb0975e80ec4461/README.md#L147-L147), [README.md#L151-L154](https://github.com/Fission-AI/OpenSpec/blob/9d4e5974e5c0d9a09b9c6c1e1eb0975e80ec4461/README.md#L151-L154) (`clm_3b4e5e1b8a5d9e15f7fea2161dc93a640f16df865886cf8a28b0efb0f5ea6745`)

## memory-state (1 claim(s))

- [observation/documented] The product maintains an openspec/ directory separating openspec/specs/ (current truth) from openspec/changes/ (proposed updates), and archiving merges approved updates back into the specs. -- evidence: [README_OLD.md#L82-L86](https://github.com/Fission-AI/OpenSpec/blob/9d4e5974e5c0d9a09b9c6c1e1eb0975e80ec4461/README_OLD.md#L82-L86), [README.md#L74-L77](https://github.com/Fission-AI/OpenSpec/blob/9d4e5974e5c0d9a09b9c6c1e1eb0975e80ec4461/README.md#L74-L77), [README_OLD.md#L49-L52](https://github.com/Fission-AI/OpenSpec/blob/9d4e5974e5c0d9a09b9c6c1e1eb0975e80ec4461/README_OLD.md#L49-L52) (`clm_01d4d177b42d251d665b922cee4e393d5b167028351dcc4de1e8999d73ff63bf`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] OpenSpec requires Node.js 20.19.0 or higher, and the install prompt instructs checking node --version before installing. -- evidence: [install.md#L25-L25](https://github.com/Fission-AI/OpenSpec/blob/9d4e5974e5c0d9a09b9c6c1e1eb0975e80ec4461/install.md#L25-L25), [README.md#L125-L125](https://github.com/Fission-AI/OpenSpec/blob/9d4e5974e5c0d9a09b9c6c1e1eb0975e80ec4461/README.md#L125-L125) (`clm_fd0e3f2c1c9b0799904a331c0536f8db65804b63d3d453b723a73a994be40f3d`)

## limitations (2 claim(s))

- [observation/documented] An internal plan document records that archiving applies requirement-level replacements, so two changes touching the same requirement can silently drop scenarios with no warning or conflict indicator. -- evidence: [openspec-parallel-merge-plan.md#L4-L6](https://github.com/Fission-AI/OpenSpec/blob/9d4e5974e5c0d9a09b9c6c1e1eb0975e80ec4461/openspec-parallel-merge-plan.md#L4-L6), [openspec-parallel-merge-plan.md#L9-L13](https://github.com/Fission-AI/OpenSpec/blob/9d4e5974e5c0d9a09b9c6c1e1eb0975e80ec4461/openspec-parallel-merge-plan.md#L9-L13), [openspec-parallel-merge-plan.md#L16-L19](https://github.com/Fission-AI/OpenSpec/blob/9d4e5974e5c0d9a09b9c6c1e1eb0975e80ec4461/openspec-parallel-merge-plan.md#L16-L19) (`clm_8735d28797c6fc9a93d8bf276f856768ee7b83c870fb0ab1176d9bd966733b34`)
- [observation/documented] The same plan notes changes do not persist the requirement content they were authored against, so the archive step cannot detect divergence between the author's base and the live spec. -- evidence: [openspec-parallel-merge-plan.md#L4-L6](https://github.com/Fission-AI/OpenSpec/blob/9d4e5974e5c0d9a09b9c6c1e1eb0975e80ec4461/openspec-parallel-merge-plan.md#L4-L6), [openspec-parallel-merge-plan.md#L16-L19](https://github.com/Fission-AI/OpenSpec/blob/9d4e5974e5c0d9a09b9c6c1e1eb0975e80ec4461/openspec-parallel-merge-plan.md#L16-L19) (`clm_d54684e2f16387899f5f58a71ac766974e66698473e975b1f682f76169e47d39`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

