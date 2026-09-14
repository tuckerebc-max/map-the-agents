# plandex-ai/plandex -- full detail

[Back to orientation](plandex.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/plandex-ai/plandex/e2d772072efadbe41d2946d97d79be55532dbab5/99984345a25cc48d.json](../../../wiki/dossiers/plandex-ai/plandex/e2d772072efadbe41d2946d97d79be55532dbab5/99984345a25cc48d.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] Project maps and syntax validation are built on tree-sitter, with support for 30+ languages. -- evidence: [README.md#L97-L97](https://github.com/plandex-ai/plandex/blob/e2d772072efadbe41d2946d97d79be55532dbab5/README.md#L97-L97) (`clm_21e8d7e9844ea960732432c4c7a95e753138d318e2dc8c5a9b50fe14804a1e64`)

## design-choices (3 claim(s))

- [observation/documented] AI-generated changes are kept in a cumulative diff review sandbox separate from project files until applied, with controlled command execution so changes can be rolled back and debugged. -- evidence: [README.md#L83-L83](https://github.com/plandex-ai/plandex/blob/e2d772072efadbe41d2946d97d79be55532dbab5/README.md#L83-L83) (`clm_3c0fada2bfb9670067c86594af6a32fa6abb56b0359b721ff8c523a627a18603`)
- [observation/documented] The tool handles up to 2M tokens of context directly (~100k per file) and can index directories of 20M+ tokens using tree-sitter project maps, loading only what each step needs. -- evidence: [README.md#L81-L81](https://github.com/plandex-ai/plandex/blob/e2d772072efadbe41d2946d97d79be55532dbab5/README.md#L81-L81), [README.md#L93-L93](https://github.com/plandex-ai/plandex/blob/e2d772072efadbe41d2946d97d79be55532dbab5/README.md#L93-L93) (`clm_4a67f0a93f8e4e3036478f701100eced0d136a9376641035ea7313f002827c66`)
- [observation/documented] Every plan update gets full-fledged version control, including branches for exploring multiple paths or comparing models, plus git integration with commit message generation and optional automatic commits. -- evidence: [README.md#L115-L115](https://github.com/plandex-ai/plandex/blob/e2d772072efadbe41d2946d97d79be55532dbab5/README.md#L115-L115), [README.md#L117-L117](https://github.com/plandex-ai/plandex/blob/e2d772072efadbe41d2946d97d79be55532dbab5/README.md#L117-L117) (`clm_fc25f4102f3fbd28d5c4237eb1eb71f8e4f6dc8895ec0b77e5aee5f5bbc6e3f6`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (5 claim(s))

- [observation/documented] Plandex is a terminal-based AI coding tool offering both a REPL (started with `plandex` or `pdx`) and a CLI for scripting and piping data into context. -- evidence: [README.md#L121-L121](https://github.com/plandex-ai/plandex/blob/e2d772072efadbe41d2946d97d79be55532dbab5/README.md#L121-L121), [README.md#L190-L190](https://github.com/plandex-ai/plandex/blob/e2d772072efadbe41d2946d97d79be55532dbab5/README.md#L190-L190), [README.md#L198-L200](https://github.com/plandex-ai/plandex/blob/e2d772072efadbe41d2946d97d79be55532dbab5/README.md#L198-L200), [README.md#L81-L81](https://github.com/plandex-ai/plandex/blob/e2d772072efadbe41d2946d97d79be55532dbab5/README.md#L81-L81), [README.md#L123-L123](https://github.com/plandex-ai/plandex/blob/e2d772072efadbe41d2946d97d79be55532dbab5/README.md#L123-L123) (`clm_ffae015681636e8aa38d4602296b922966e150148b50991081396eab813a5e1a`)
- [observation/documented] A configuration system exposes settings such as auto-mode (none/basic/plus/semi/full, default semi), auto-apply (default false), auto-commit (default true), and can-exec, viewable via `plandex config` and modifiable via `plandex set-config`. -- evidence: [docs/docs/core-concepts/configuration.md#L31-L33](https://github.com/plandex-ai/plandex/blob/e2d772072efadbe41d2946d97d79be55532dbab5/docs/docs/core-concepts/configuration.md#L31-L33), [docs/docs/core-concepts/configuration.md#L62-L65](https://github.com/plandex-ai/plandex/blob/e2d772072efadbe41d2946d97d79be55532dbab5/docs/docs/core-concepts/configuration.md#L62-L65), [docs/docs/core-concepts/configuration.md#L8-L8](https://github.com/plandex-ai/plandex/blob/e2d772072efadbe41d2946d97d79be55532dbab5/docs/docs/core-concepts/configuration.md#L8-L8), [docs/docs/core-concepts/configuration.md#L53-L58](https://github.com/plandex-ai/plandex/blob/e2d772072efadbe41d2946d97d79be55532dbab5/docs/docs/core-concepts/configuration.md#L53-L58), [docs/docs/core-concepts/configuration.md#L12-L15](https://github.com/plandex-ai/plandex/blob/e2d772072efadbe41d2946d97d79be55532dbab5/docs/docs/core-concepts/configuration.md#L12-L15), [docs/docs/core-concepts/configuration.md#L37-L41](https://github.com/plandex-ai/plandex/blob/e2d772072efadbe41d2946d97d79be55532dbab5/docs/docs/core-concepts/configuration.md#L37-L41), [docs/docs/core-concepts/configuration.md#L19-L23](https://github.com/plandex-ai/plandex/blob/e2d772072efadbe41d2946d97d79be55532dbab5/docs/docs/core-concepts/configuration.md#L19-L23) (`clm_6a086cd409e0028981f53b19b913e05320e0c0744bad51cd51c77780f2642491`)
- [observation/documented] Many settings can be overridden per command with CLI flags (e.g. `plandex tell "..." --apply --auto-exec --debug`); these overrides apply only to that execution and don't change saved configuration. -- evidence: [docs/docs/core-concepts/configuration.md#L93-L93](https://github.com/plandex-ai/plandex/blob/e2d772072efadbe41d2946d97d79be55532dbab5/docs/docs/core-concepts/configuration.md#L93-L93), [docs/docs/core-concepts/configuration.md#L90-L91](https://github.com/plandex-ai/plandex/blob/e2d772072efadbe41d2946d97d79be55532dbab5/docs/docs/core-concepts/configuration.md#L90-L91), [docs/docs/core-concepts/configuration.md#L86-L86](https://github.com/plandex-ai/plandex/blob/e2d772072efadbe41d2946d97d79be55532dbab5/docs/docs/core-concepts/configuration.md#L86-L86) (`clm_a4dab8ccca225a306afd16200f6182a7f6991eed0e647fa88149a3ad0adcc8be`)
- [observation/documented] REPL commands include \config, \set-config, and \set-auto, with `default` variants that modify configuration for new plans. -- evidence: [docs/docs/core-concepts/configuration.md#L99-L106](https://github.com/plandex-ai/plandex/blob/e2d772072efadbe41d2946d97d79be55532dbab5/docs/docs/core-concepts/configuration.md#L99-L106) (`clm_176f67fd9004173cce1bc12057277e21cb88ea57d94dae65638c3310360400e0`)
- [observation/documented] Installation is a one-line, zero-dependency script (`curl -sL https://plandex.ai/install.sh | bash`), and Plandex can use a Claude Pro/Max subscription for Anthropic models, offered at first run. -- evidence: [README.md#L172-L172](https://github.com/plandex-ai/plandex/blob/e2d772072efadbe41d2946d97d79be55532dbab5/README.md#L172-L172), [README.md#L145-L147](https://github.com/plandex-ai/plandex/blob/e2d772072efadbe41d2946d97d79be55532dbab5/README.md#L145-L147), [README.md#L125-L125](https://github.com/plandex-ai/plandex/blob/e2d772072efadbe41d2946d97d79be55532dbab5/README.md#L125-L125) (`clm_4f11e11cde4ff9d452c519eb8e994dbfd432847afed02f82975a9cf3af0e70af`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Plandex supports models from Anthropic, OpenAI, Google, and open-source providers, with curated model packs trading off capability, cost, and speed; context caching is used for OpenAI, Anthropic, and Google models. -- evidence: [README.md#L99-L99](https://github.com/plandex-ai/plandex/blob/e2d772072efadbe41d2946d97d79be55532dbab5/README.md#L99-L99), [README.md#L85-L85](https://github.com/plandex-ai/plandex/blob/e2d772072efadbe41d2946d97d79be55532dbab5/README.md#L85-L85), [README.md#L111-L111](https://github.com/plandex-ai/plandex/blob/e2d772072efadbe41d2946d97d79be55532dbab5/README.md#L111-L111) (`clm_c35a717ca3fcd490df195dd1633307764d8e998ccf9fe70ca34b0ad040a6f727`)

## limitations (2 claim(s))

- [observation/documented] On Windows, Plandex works only in the WSL shell; it does not work in the Windows CMD prompt or PowerShell. -- evidence: [README.md#L149-L149](https://github.com/plandex-ai/plandex/blob/e2d772072efadbe41d2946d97d79be55532dbab5/README.md#L149-L149) (`clm_ae15e35f7f1917e14cfb45244c31139a49720356186108ddee4804587cf9316e`)
- [observation/documented] Plandex Cloud is winding down as of 10/3/2025 and is no longer accepting new users; self-hosted/local mode with Docker and your own provider API keys is the documented alternative. -- evidence: [README.md#L155-L158](https://github.com/plandex-ai/plandex/blob/e2d772072efadbe41d2946d97d79be55532dbab5/README.md#L155-L158) (`clm_11d8896912c85ad2551d4ad021a0b389d066e33a31e2cfe24c6f2962e632d723`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

