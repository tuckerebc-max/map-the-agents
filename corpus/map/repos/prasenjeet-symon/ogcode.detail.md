# prasenjeet-symon/ogcode -- full detail

[Back to orientation](ogcode.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/prasenjeet-symon/ogcode/e76eaf72178d3451626b70daf1dbe8c4230b2bbb/15cde5cc5ac46f99.json](../../../wiki/dossiers/prasenjeet-symon/ogcode/e76eaf72178d3451626b70daf1dbe8c4230b2bbb/15cde5cc5ac46f99.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (2 claim(s))

- [observation/documented] Ogcode is described as a single Go binary with an embedded SolidJS web UI that runs locally, positioned as browser-native, self-hosted, and model-agnostic. -- evidence: [README.md#L125-L125](https://github.com/prasenjeet-symon/ogcode/blob/e76eaf72178d3451626b70daf1dbe8c4230b2bbb/README.md#L125-L125), [README.md#L127-L127](https://github.com/prasenjeet-symon/ogcode/blob/e76eaf72178d3451626b70daf1dbe8c4230b2bbb/README.md#L127-L127) (`clm_f695b974c4c5d93522680b1b6f877e87e719b29a5b9a827af3845763c3e6a17c`)
- [observation/documented] The breakdown agent enforces a file-ownership rule so parallel tasks never edit the same files, and dependency chains are strictly linear with cycles rejected before execution. -- evidence: [README.md#L106-L109](https://github.com/prasenjeet-symon/ogcode/blob/e76eaf72178d3451626b70daf1dbe8c4230b2bbb/README.md#L106-L109) (`clm_cc4d64b81a3769e7ff6c4001ea6bc26890961e9e46752d9dac3ab8a2563be5bd`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (1 claim(s))

- [observation/documented] Skills are SKILL.md files whose names and descriptions appear in the prompt; the full body is loaded via a skill tool only when a task matches. -- evidence: [README.md#L459-L459](https://github.com/prasenjeet-symon/ogcode/blob/e76eaf72178d3451626b70daf1dbe8c4230b2bbb/README.md#L459-L459), [README.md#L461-L461](https://github.com/prasenjeet-symon/ogcode/blob/e76eaf72178d3451626b70daf1dbe8c4230b2bbb/README.md#L461-L461) (`clm_505827ab5ea1c8887601377dc4da79b091f72e6bcac3d0ca0bde5bcad6ec8d2f`)

## interfaces (3 claim(s))

- [observation/documented] A file_map tool uses tree-sitter to outline declarations with line ranges; reading a file over 200 lines without a range returns the map instead of full contents. -- evidence: [README.md#L242-L249](https://github.com/prasenjeet-symon/ogcode/blob/e76eaf72178d3451626b70daf1dbe8c4230b2bbb/README.md#L242-L249), [README.md#L271-L271](https://github.com/prasenjeet-symon/ogcode/blob/e76eaf72178d3451626b70daf1dbe8c4230b2bbb/README.md#L271-L271), [README.md#L288-L288](https://github.com/prasenjeet-symon/ogcode/blob/e76eaf72178d3451626b70daf1dbe8c4230b2bbb/README.md#L288-L288) (`clm_472c0be01f5bd9f01a31d4217e80a0ce568f78cedff89eb20df3773f69be2bd6`)
- [observation/documented] Ten tree-sitter grammars cover Go, TypeScript/JS/TSX, PHP, Python, Rust, Swift, Java, C#, and Dart, with a heuristic fallback scanner for other file types. -- evidence: [README.md#L338-L338](https://github.com/prasenjeet-symon/ogcode/blob/e76eaf72178d3451626b70daf1dbe8c4230b2bbb/README.md#L338-L338), [README.md#L299-L299](https://github.com/prasenjeet-symon/ogcode/blob/e76eaf72178d3451626b70daf1dbe8c4230b2bbb/README.md#L299-L299), [README.md#L301-L312](https://github.com/prasenjeet-symon/ogcode/blob/e76eaf72178d3451626b70daf1dbe8c4230b2bbb/README.md#L301-L312) (`clm_405e8bfd426ffbf404fd7572f7b141f3b343a50070653ce8fc336c2453eb4218`)
- [observation/documented] Configuration layers CLI flag > environment variable > config file > provider auto-detect, supporting Anthropic, OpenAI, OpenRouter, and Ollama via env vars and optional JSON config files. -- evidence: [README.md#L405-L405](https://github.com/prasenjeet-symon/ogcode/blob/e76eaf72178d3451626b70daf1dbe8c4230b2bbb/README.md#L405-L405), [README.md#L453-L453](https://github.com/prasenjeet-symon/ogcode/blob/e76eaf72178d3451626b70daf1dbe8c4230b2bbb/README.md#L453-L453), [README.md#L411-L416](https://github.com/prasenjeet-symon/ogcode/blob/e76eaf72178d3451626b70daf1dbe8c4230b2bbb/README.md#L411-L416) (`clm_76094fe45afbb093411ac22c1d98d5d8e1700135ed0c32aa3efde839216f1a46`)

## memory-state (2 claim(s))

- [observation/documented] The README claims Agentic Session Memory recalls only task-relevant facts from a persistent knowledge graph per turn instead of replaying the full transcript, keeping per-turn prompt size flat. -- evidence: [README.md#L40-L40](https://github.com/prasenjeet-symon/ogcode/blob/e76eaf72178d3451626b70daf1dbe8c4230b2bbb/README.md#L40-L40), [README.md#L62-L62](https://github.com/prasenjeet-symon/ogcode/blob/e76eaf72178d3451626b70daf1dbe8c4230b2bbb/README.md#L62-L62) (`clm_0f4382dabd79d66905e287e397364e408d54dc1be79a5c1fe9e959fd7b34ce0b`)
- [observation/documented] A knowledge graph structured as Topic → Concept → Fact is said to persist across sessions as semantic memory of the codebase. -- evidence: [README.md#L155-L169](https://github.com/prasenjeet-symon/ogcode/blob/e76eaf72178d3451626b70daf1dbe8c4230b2bbb/README.md#L155-L169) (`clm_54542cfc94f3e49ee223333424415c484741de372b8afb9228a4ae81bc70b8b9`)

## orchestration (2 claim(s))

- [observation/documented] Plan Mode breaks a locked plan into tasks with effort estimates (S/M/L/XL), complexity scores, and a dependency graph, shown on a visual Kanban board before execution. -- evidence: [README.md#L95-L100](https://github.com/prasenjeet-symon/ogcode/blob/e76eaf72178d3451626b70daf1dbe8c4230b2bbb/README.md#L95-L100), [README.md#L82-L93](https://github.com/prasenjeet-symon/ogcode/blob/e76eaf72178d3451626b70daf1dbe8c4230b2bbb/README.md#L82-L93) (`clm_125fa3b06e8dc9b4e6048947771e1d7926bf2d22a17a77b907be45af71e95423`)
- [observation/documented] Each task runs in its own git worktree and isolated agent session; independent tasks execute in parallel, and finished tasks auto-commit, push, and open PRs via the gh CLI idempotently. -- evidence: [README.md#L95-L100](https://github.com/prasenjeet-symon/ogcode/blob/e76eaf72178d3451626b70daf1dbe8c4230b2bbb/README.md#L95-L100), [README.md#L115-L119](https://github.com/prasenjeet-symon/ogcode/blob/e76eaf72178d3451626b70daf1dbe8c4230b2bbb/README.md#L115-L119) (`clm_de7aa1fc67b50c9907acc5d8d4b38bb5d8333e15f88cb6a7fd3ae482582d2865`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (1 claim(s))

- [observation/documented] The README reports session-level token savings of 68–76% versus full-replay at 50–1000 message lengths, attributing accuracy gains to curated context; these are self-reported figures. -- evidence: [README.md#L253-L253](https://github.com/prasenjeet-symon/ogcode/blob/e76eaf72178d3451626b70daf1dbe8c4230b2bbb/README.md#L253-L253), [README.md#L255-L259](https://github.com/prasenjeet-symon/ogcode/blob/e76eaf72178d3451626b70daf1dbe8c4230b2bbb/README.md#L255-L259) (`clm_f357e737691894ed2370e5c4eaba872aa0185b2fb2fcf5e0253a21dff7bb089a`)

## dependencies (1 claim(s))

- [observation/documented] The Swift tree-sitter grammar is vendored into the repository rather than required via go.mod, and the Dart grammar is pinned to a commit pseudo-version because it lacks tagged releases. -- evidence: [README.md#L336-L336](https://github.com/prasenjeet-symon/ogcode/blob/e76eaf72178d3451626b70daf1dbe8c4230b2bbb/README.md#L336-L336), [README.md#L324-L324](https://github.com/prasenjeet-symon/ogcode/blob/e76eaf72178d3451626b70daf1dbe8c4230b2bbb/README.md#L324-L324) (`clm_930cb2b45360f9b94807d9dcb896507d3d82e54028041b147a5b11e246cd716b`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

