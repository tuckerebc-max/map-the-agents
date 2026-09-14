# lnxpy/hey -- full detail

[Back to orientation](hey.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/lnxpy/hey/9b1b2ab680a4f4ed6b62aa7c2ea62f71b7d403dc/f65bf68cccf6626a.json](../../../wiki/dossiers/lnxpy/hey/9b1b2ab680a4f4ed6b62aa7c2ea62f71b7d403dc/f65bf68cccf6626a.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (1 claim(s))

- [observation/documented] Configuration parameters include service URL, model (default gpt-3.5-turbo), a system prompt, code-block theme, loading text and spinner, and a never_style option to disable output styling for copying. -- evidence: [README.md#L98-L101](https://github.com/lnxpy/hey/blob/9b1b2ab680a4f4ed6b62aa7c2ea62f71b7d403dc/README.md#L98-L101), [README.md#L78-L81](https://github.com/lnxpy/hey/blob/9b1b2ab680a4f4ed6b62aa7c2ea62f71b7d403dc/README.md#L78-L81), [README.md#L89-L90](https://github.com/lnxpy/hey/blob/9b1b2ab680a4f4ed6b62aa7c2ea62f71b7d403dc/README.md#L89-L90), [README.md#L86-L87](https://github.com/lnxpy/hey/blob/9b1b2ab680a4f4ed6b62aa7c2ea62f71b7d403dc/README.md#L86-L87), [README.md#L92-L93](https://github.com/lnxpy/hey/blob/9b1b2ab680a4f4ed6b62aa7c2ea62f71b7d403dc/README.md#L92-L93), [README.md#L83-L84](https://github.com/lnxpy/hey/blob/9b1b2ab680a4f4ed6b62aa7c2ea62f71b7d403dc/README.md#L83-L84), [README.md#L95-L96](https://github.com/lnxpy/hey/blob/9b1b2ab680a4f4ed6b62aa7c2ea62f71b7d403dc/README.md#L95-L96) (`clm_333378e7c8a28c44c6a94f39c4bc55565bac508cf29fc7a1b0dbfcf190ef531d`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: the dev requirements file includes pytest and coverage>=7.2.5, indicating a Python test setup for contributors. -- evidence: [requirements-dev.txt#L1-L2](https://github.com/lnxpy/hey/blob/9b1b2ab680a4f4ed6b62aa7c2ea62f71b7d403dc/requirements-dev.txt#L1-L2) (`clm_a9020f53eb9610f020f168c2d819b8c49efb6c531eb8455d8f19efc0952ce01d`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (5 claim(s))

- [observation/documented] Hey is a CLI-based AI assistant powered by LLMs, and users can choose which LLM service it connects to. -- evidence: [README.md#L9-L9](https://github.com/lnxpy/hey/blob/9b1b2ab680a4f4ed6b62aa7c2ea62f71b7d403dc/README.md#L9-L9) (`clm_7df8aa6129c53f1d4841613d15f3cf72d417f0c6262aeddfe4f18ca0b4db50d2`)
- [observation/documented] Running bare `hey` opens the default $EDITOR for composing longer questions; if unset, it falls back to vim on Unix-like systems and notepad on Windows. -- evidence: [README.md#L59-L59](https://github.com/lnxpy/hey/blob/9b1b2ab680a4f4ed6b62aa7c2ea62f71b7d403dc/README.md#L59-L59), [README.md#L54-L57](https://github.com/lnxpy/hey/blob/9b1b2ab680a4f4ed6b62aa7c2ea62f71b7d403dc/README.md#L54-L57) (`clm_e8b6b692ae46bef69eb47814217476045a01a632b8ed057a4a791f9db254830b`)
- [observation/documented] The CLI provides an `ask` sub-command for quick questions, e.g. `hey ask "..."`, and `--help` to list commands and sub-commands. -- evidence: [README.md#L46-L46](https://github.com/lnxpy/hey/blob/9b1b2ab680a4f4ed6b62aa7c2ea62f71b7d403dc/README.md#L46-L46), [README.md#L38-L38](https://github.com/lnxpy/hey/blob/9b1b2ab680a4f4ed6b62aa7c2ea62f71b7d403dc/README.md#L38-L38), [README.md#L48-L50](https://github.com/lnxpy/hey/blob/9b1b2ab680a4f4ed6b62aa7c2ea62f71b7d403dc/README.md#L48-L50) (`clm_7b5ccd553c40fc7bba18d94f85e3c4e845f37cb9482763baf41a1e42e800c593`)
- [observation/documented] A `hey auth` command sets the LLM service token after installation. -- evidence: [README.md#L32-L35](https://github.com/lnxpy/hey/blob/9b1b2ab680a4f4ed6b62aa7c2ea62f71b7d403dc/README.md#L32-L35), [README.md#L30-L30](https://github.com/lnxpy/hey/blob/9b1b2ab680a4f4ed6b62aa7c2ea62f71b7d403dc/README.md#L30-L30) (`clm_16fa087c47745e91a803a9d6535e1fbaa7e70826303e4b12a999419ee1e28586`)
- [observation/documented] Configuration is managed via `hey config create` to generate a base config file and `hey config edit` to view and edit it. -- evidence: [README.md#L62-L62](https://github.com/lnxpy/hey/blob/9b1b2ab680a4f4ed6b62aa7c2ea62f71b7d403dc/README.md#L62-L62), [README.md#L66-L68](https://github.com/lnxpy/hey/blob/9b1b2ab680a4f4ed6b62aa7c2ea62f71b7d403dc/README.md#L66-L68), [README.md#L72-L74](https://github.com/lnxpy/hey/blob/9b1b2ab680a4f4ed6b62aa7c2ea62f71b7d403dc/README.md#L72-L74) (`clm_0105fcfcb789980bfd314e0a1e4a176dd9003de8ebea043a7fd7f76f0d53f9ca`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (3 claim(s))

- [observation/documented] The package is installable from PyPI as hey-mindsdb, or directly from the GitHub repository via pip. -- evidence: [README.md#L20-L22](https://github.com/lnxpy/hey/blob/9b1b2ab680a4f4ed6b62aa7c2ea62f71b7d403dc/README.md#L20-L22), [README.md#L25-L27](https://github.com/lnxpy/hey/blob/9b1b2ab680a4f4ed6b62aa7c2ea62f71b7d403dc/README.md#L25-L27) (`clm_9f19a86280dc393eb4e4e237733611ab2d8b5a400bd855785a325acf8255da43`)
- [observation/documented] The tool requires pip and Python 3.8 or newer on the user's machine. -- evidence: [README.md#L15-L15](https://github.com/lnxpy/hey/blob/9b1b2ab680a4f4ed6b62aa7c2ea62f71b7d403dc/README.md#L15-L15) (`clm_bb0d8b5375f0971e262fb58b4faf497d70d400793eb8d39f91e00b04244693bb`)
- [inference/documented] The loading spinner feature appears to rely on the Rich library, since the config comment points users to `python -m rich.spinner` for the full spinner list. -- evidence: [README.md#L95-L96](https://github.com/lnxpy/hey/blob/9b1b2ab680a4f4ed6b62aa7c2ea62f71b7d403dc/README.md#L95-L96) (`clm_72ba22218f6adefa5aa6e43927134351a579d4e6971a5150baaa9d92b36e2b40`)

## limitations (1 claim(s))

- [observation/documented] The README recommends free tokens from mdb.ai but notes users are not limited to it and can point Hey at any other LLM service. -- evidence: [README.md#L11-L12](https://github.com/lnxpy/hey/blob/9b1b2ab680a4f4ed6b62aa7c2ea62f71b7d403dc/README.md#L11-L12) (`clm_2348926268771b6b5835090c70c036e89764e800a95d7690d65ec6f7083676c3`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

