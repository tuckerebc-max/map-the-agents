# wrongstack/wrongstack -- full detail

[Back to orientation](wrongstack.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/wrongstack/wrongstack/fdbf2c0268c63bbcb6975010f8bbaf92ab13e479/c8dee8173236ea4b.json](../../../wiki/dossiers/wrongstack/wrongstack/fdbf2c0268c63bbcb6975010f8bbaf92ab13e479/c8dee8173236ea4b.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The pnpm workspace reportedly contains 29 packages and two applications, with foundation packages persistence, kanban, and core, plus runtime, providers, tools, and user-surface packages. -- evidence: [docs/architecture.md#L50-L52](https://github.com/WrongStack/WrongStack/blob/fdbf2c0268c63bbcb6975010f8bbaf92ab13e479/docs/architecture.md#L50-L52), [docs/architecture.md#L54-L62](https://github.com/WrongStack/WrongStack/blob/fdbf2c0268c63bbcb6975010f8bbaf92ab13e479/docs/architecture.md#L54-L62) (`clm_178b637578644b0417467dcd1e86e1583787964770d4a60c7f8ce6c7fbf9c481`)

## design-choices (1 claim(s))

- [observation/documented] The kernel is described as four primitives — Container, Pipeline, EventBus, RunController — with extension points in registries and services bound through the Container. -- evidence: [docs/architecture.md#L88-L92](https://github.com/WrongStack/WrongStack/blob/fdbf2c0268c63bbcb6975010f8bbaf92ab13e479/docs/architecture.md#L88-L92), [README.md#L524-L527](https://github.com/WrongStack/WrongStack/blob/fdbf2c0268c63bbcb6975010f8bbaf92ab13e479/README.md#L524-L527), [README.md#L510-L520](https://github.com/WrongStack/WrongStack/blob/fdbf2c0268c63bbcb6975010f8bbaf92ab13e479/README.md#L510-L520), [README.md#L155-L165](https://github.com/WrongStack/WrongStack/blob/fdbf2c0268c63bbcb6975010f8bbaf92ab13e479/README.md#L155-L165) (`clm_0b7f8c828e6c72e4572b81b9ff45544d11fdf4d4672858519187ce2cec128475`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: release verification uses pnpm release:check with 18 gates, root Vitest coverage thresholds are set (>=76% lines, >=75% functions, >=66% branches), and package-boundary rules are enforced by a dedicated architecture test. -- evidence: [README.md#L563-L568](https://github.com/WrongStack/WrongStack/blob/fdbf2c0268c63bbcb6975010f8bbaf92ab13e479/README.md#L563-L568), [docs/architecture.md#L64-L70](https://github.com/WrongStack/WrongStack/blob/fdbf2c0268c63bbcb6975010f8bbaf92ab13e479/docs/architecture.md#L64-L70) (`clm_b2c4784c44b87e58c723a87a7066d1dfe3d800b73949ca453d3040f5f24b93bd`)
- [observation/documented] Repository development practice: pnpm release:fast skips only the audit and instrumented-coverage gates that CI covers, and the release matrix verifies the packed providers package installs with npm 10. -- evidence: [README.md#L50-L66](https://github.com/WrongStack/WrongStack/blob/fdbf2c0268c63bbcb6975010f8bbaf92ab13e479/README.md#L50-L66) (`clm_9e8fd75ac6b39c23376b3569621e763a6256ae39f386f0248f0abd34194e7167`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] The product offers six launch surfaces: a readline REPL, an Ink TUI behind --tui, a WebUI, SimpleUI, an Electron Desktop shell, and a cross-machine HQ dashboard. -- evidence: [README.md#L285-L289](https://github.com/WrongStack/WrongStack/blob/fdbf2c0268c63bbcb6975010f8bbaf92ab13e479/README.md#L285-L289), [README.md#L273-L280](https://github.com/WrongStack/WrongStack/blob/fdbf2c0268c63bbcb6975010f8bbaf92ab13e479/README.md#L273-L280), [README.md#L96-L144](https://github.com/WrongStack/WrongStack/blob/fdbf2c0268c63bbcb6975010f8bbaf92ab13e479/README.md#L96-L144) (`clm_d6e4cdf5f33b9cae66c30a2b682ab2d2a96090bfd10983dfb94e39f8b2d1cd79`)

## memory-state (1 claim(s))

- [observation/documented] SAGE is project-local long-term memory backed by SQLite/FTS5 under .wrongstack/memories/, with typed knowledge, anchors to files/symbols/commands/commits, a knowledge graph, and auto-injection into context each turn. -- evidence: [README.md#L355-L362](https://github.com/WrongStack/WrongStack/blob/fdbf2c0268c63bbcb6975010f8bbaf92ab13e479/README.md#L355-L362), [README.md#L96-L144](https://github.com/WrongStack/WrongStack/blob/fdbf2c0268c63bbcb6975010f8bbaf92ab13e479/README.md#L96-L144), [README.md#L364-L368](https://github.com/WrongStack/WrongStack/blob/fdbf2c0268c63bbcb6975010f8bbaf92ab13e479/README.md#L364-L368) (`clm_5a41a6a7ca5b89e8afc9cb1e587155e92d021febb56d34644e00c261e2e2fec4`)

## orchestration (1 claim(s))

- [observation/documented] A Director-led specialist fleet fans out subagents, each isolated with its own budget and JSONL transcript, coordinated over a project-wide mailbox with typed messages and live presence. -- evidence: [README.md#L322-L325](https://github.com/WrongStack/WrongStack/blob/fdbf2c0268c63bbcb6975010f8bbaf92ab13e479/README.md#L322-L325), [README.md#L343-L351](https://github.com/WrongStack/WrongStack/blob/fdbf2c0268c63bbcb6975010f8bbaf92ab13e479/README.md#L343-L351), [README.md#L96-L144](https://github.com/WrongStack/WrongStack/blob/fdbf2c0268c63bbcb6975010f8bbaf92ab13e479/README.md#L96-L144) (`clm_3da31d32a5706a942ff6bee114483550d0a3272dd070bac941e6cf413967ad22`)

## tools-permissions (2 claim(s))

- [observation/documented] Every tool call passes a permission policy; project-root containment cannot be overridden by YOLO, absolute denies remain enforced, and destructive shell actions stay confirmable unless destructive YOLO is explicitly enabled. -- evidence: [docs/architecture.md#L140-L144](https://github.com/WrongStack/WrongStack/blob/fdbf2c0268c63bbcb6975010f8bbaf92ab13e479/docs/architecture.md#L140-L144), [README.md#L481-L483](https://github.com/WrongStack/WrongStack/blob/fdbf2c0268c63bbcb6975010f8bbaf92ab13e479/README.md#L481-L483), [README.md#L155-L165](https://github.com/WrongStack/WrongStack/blob/fdbf2c0268c63bbcb6975010f8bbaf92ab13e479/README.md#L155-L165) (`clm_257aeee85c267b770ac61cd8de75b161eab843b918df61e03490cfb92591335b`)
- [observation/documented] Tools declare a JSON-schema input plus permission/risk/mutation profile, and the ToolExecutor evaluates permission before execution with sequential, parallel, and smart scheduling. -- evidence: [docs/architecture.md#L127-L131](https://github.com/WrongStack/WrongStack/blob/fdbf2c0268c63bbcb6975010f8bbaf92ab13e479/docs/architecture.md#L127-L131) (`clm_aaaf3643238f70ad111c89386316e1f04e21520704536c0578975d028eb0128f`)

## evaluation (1 claim(s))

- [observation/documented] The @wrongstack/bench package is described as a benchmark harness covering Aider polyglot and SWE-bench Verified. -- evidence: [README.md#L535-L557](https://github.com/WrongStack/WrongStack/blob/fdbf2c0268c63bbcb6975010f8bbaf92ab13e479/README.md#L535-L557) (`clm_f0378279ef38c0c12b39967a1709aaa13781c1f69fbe25c584ac0215fb3240ea`)

## dependencies (2 claim(s))

- [observation/documented] The project requires Node.js >= 22.19.0 with pnpm (recommended) or npm, or Bun >= 1.3.10 as an alternative runtime; it is ESM-only with no CommonJS bundles. -- evidence: [README.md#L563-L568](https://github.com/WrongStack/WrongStack/blob/fdbf2c0268c63bbcb6975010f8bbaf92ab13e479/README.md#L563-L568), [README.md#L175-L176](https://github.com/WrongStack/WrongStack/blob/fdbf2c0268c63bbcb6975010f8bbaf92ab13e479/README.md#L175-L176) (`clm_bc84cf2441ef9b2710134c276d45208a21858275d524fac2592fa7de9744be3a`)
- [observation/documented] Providers span multiple wire families including native Anthropic, OpenAI, Google, OpenAI-compatible, and OAuth adapters, with a catalog fetched from models.dev and one-command Ollama/vLLM/LM Studio local presets. -- evidence: [docs/architecture.md#L133-L138](https://github.com/WrongStack/WrongStack/blob/fdbf2c0268c63bbcb6975010f8bbaf92ab13e479/docs/architecture.md#L133-L138), [README.md#L411-L416](https://github.com/WrongStack/WrongStack/blob/fdbf2c0268c63bbcb6975010f8bbaf92ab13e479/README.md#L411-L416), [README.md#L25-L32](https://github.com/WrongStack/WrongStack/blob/fdbf2c0268c63bbcb6975010f8bbaf92ab13e479/README.md#L25-L32), [README.md#L406-L409](https://github.com/WrongStack/WrongStack/blob/fdbf2c0268c63bbcb6975010f8bbaf92ab13e479/README.md#L406-L409) (`clm_fc3f6747e01874ea79dbda4991632607ddc3d7b348ba8d54909f805b65c6783f`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

