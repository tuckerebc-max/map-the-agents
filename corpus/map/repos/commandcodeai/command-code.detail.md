# commandcodeai/command-code -- full detail

[Back to orientation](command-code.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/commandcodeai/command-code/5c8f1b48c9d6704210cb3f9a476fdcffe5093e9a/5960e9e356d6db47.json](../../../wiki/dossiers/commandcodeai/command-code/5c8f1b48c9d6704210cb3f9a476fdcffe5093e9a/5960e9e356d6db47.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The README describes a model called `taste-1` as the core of the product's taste architecture, which it says learns from the user and grows with them. -- evidence: [readme.md#L61-L61](https://github.com/CommandCodeAI/command-code/blob/5c8f1b48c9d6704210cb3f9a476fdcffe5093e9a/readme.md#L61-L61), [readme.md#L33-L36](https://github.com/CommandCodeAI/command-code/blob/5c8f1b48c9d6704210cb3f9a476fdcffe5093e9a/readme.md#L33-L36) (`clm_24dcbcbee0c12da42c957262f707352c027c7396f5b97dbcf240ae48b137acf6`)

## design-choices (2 claim(s))

- [observation/documented] The taste system is designed to treat every accept, reject, and edit as a signal that shapes a per-user taste profile. -- evidence: [readme.md#L33-L36](https://github.com/CommandCodeAI/command-code/blob/5c8f1b48c9d6704210cb3f9a476fdcffe5093e9a/readme.md#L33-L36) (`clm_145836d0beb30ca5569c3981c915713a2a8ca1fb00a7baf035bc00654046f8b2`)
- [observation/documented] Taste rules are designed to be shareable across a team via `npx taste push/pull`, with the README stating that rules decay while taste compounds. -- evidence: [readme.md#L33-L36](https://github.com/CommandCodeAI/command-code/blob/5c8f1b48c9d6704210cb3f9a476fdcffe5093e9a/readme.md#L33-L36) (`clm_213984ff31c39f425659fcedf28a2d87a39721b2a5c175a981d972d28dc8ae7f`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (1 claim(s))

- [inference/documented] The docs site advertises workflow recipes pairing concrete scenarios with prompts and expected outcomes, suggesting a curated usage-pattern library, though only the link is in evidence. -- evidence: [readme.md#L75-L75](https://github.com/CommandCodeAI/command-code/blob/5c8f1b48c9d6704210cb3f9a476fdcffe5093e9a/readme.md#L75-L75), [readme.md#L73-L73](https://github.com/CommandCodeAI/command-code/blob/5c8f1b48c9d6704210cb3f9a476fdcffe5093e9a/readme.md#L73-L73) (`clm_510c3efe689bfbecbc6cd41ec8fe39e9ed787ec21b8edb9b5f880657259966cc`)

## interfaces (3 claim(s))

- [observation/documented] The product runs as a CLI: it is installed globally via npm and started inside a project with the `cmd` command. -- evidence: [readme.md#L50-L53](https://github.com/CommandCodeAI/command-code/blob/5c8f1b48c9d6704210cb3f9a476fdcffe5093e9a/readme.md#L50-L53), [readme.md#L44-L46](https://github.com/CommandCodeAI/command-code/blob/5c8f1b48c9d6704210cb3f9a476fdcffe5093e9a/readme.md#L44-L46) (`clm_92d93707395d57482d26ea74abe6e78e22599b50543652e6292255078a21521e`)
- [observation/documented] Interactive sessions support typed prefixes: `/` opens a command menu, `!` enters Bash mode, and `@` triggers file-path mention autocomplete. -- evidence: [readme.md#L67-L67](https://github.com/CommandCodeAI/command-code/blob/5c8f1b48c9d6704210cb3f9a476fdcffe5093e9a/readme.md#L67-L67) (`clm_f043110ee059a9ebdfcf68b8ee6300de8d7f94706f72ed48205b039949353c3b`)
- [observation/documented] A `/feedback` slash command is documented for reporting issues from within the tool, alongside GitHub issues as an alternative channel. -- evidence: [readme.md#L89-L92](https://github.com/CommandCodeAI/command-code/blob/5c8f1b48c9d6704210cb3f9a476fdcffe5093e9a/readme.md#L89-L92) (`clm_34ae20392277f257008de74af2b8f58f37eee3067997cb9be87d382573626574`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The tool is distributed as the npm package `command-code`, installed with `npm i -g command-code`. -- evidence: [readme.md#L11-L15](https://github.com/CommandCodeAI/command-code/blob/5c8f1b48c9d6704210cb3f9a476fdcffe5093e9a/readme.md#L11-L15), [readme.md#L44-L46](https://github.com/CommandCodeAI/command-code/blob/5c8f1b48c9d6704210cb3f9a476fdcffe5093e9a/readme.md#L44-L46) (`clm_45e5d22019fdd444a92e0dcb68aa9ea0fd2a14026c039ecd8364160c0fd97fc2`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (1 claim(s))

- [observation/documented] The project is a coding agent positioned as building full-stack projects, fixing bugs, writing tests, and refactoring while adapting to the user's coding style. -- evidence: [readme.md#L7-L9](https://github.com/CommandCodeAI/command-code/blob/5c8f1b48c9d6704210cb3f9a476fdcffe5093e9a/readme.md#L7-L9) (`clm_6fbb0121b7a8f435cf25d02d7b43de1b6b6e060cc973ba6f9bec9ddc7db98863`)

