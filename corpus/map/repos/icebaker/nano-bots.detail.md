# icebaker/nano-bots -- full detail

[Back to orientation](nano-bots.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/icebaker/nano-bots/2bbc92857aa4ca8db5b0af75e96243d2d6ceae62/797c7851bb478ba8.json](../../../wiki/dossiers/icebaker/nano-bots/2bbc92857aa4ca8db5b0af75e96243d2d6ceae62/797c7851bb478ba8.json)

## specifications (3 claim(s))

- [observation/documented] The repository hosts Nano Bots' Cartridges, which are YAML files that require a separate implementation to run. -- evidence: [README.md#L22-L22](https://github.com/icebaker/nano-bots/blob/2bbc92857aa4ca8db5b0af75e96243d2d6ceae62/README.md#L22-L22), [README.md#L6-L6](https://github.com/icebaker/nano-bots/blob/2bbc92857aa4ca8db5b0af75e96243d2d6ceae62/README.md#L6-L6), [README.md#L18-L18](https://github.com/icebaker/nano-bots/blob/2bbc92857aa4ca8db5b0af75e96243d2d6ceae62/README.md#L18-L18) (`clm_be88594ecb6d256e77aa535a2d6a0684f60387e1780eb4d758d05ebe723e3bc8`)
- [observation/documented] Cartridges may include a `miscellaneous.marketplace` section with `tags` (clean-URL style) and `samples` entries specifying interface type and inputs. -- evidence: [README.md#L62-L74](https://github.com/icebaker/nano-bots/blob/2bbc92857aa4ca8db5b0af75e96243d2d6ceae62/README.md#L62-L74), [README.md#L76-L76](https://github.com/icebaker/nano-bots/blob/2bbc92857aa4ca8db5b0af75e96243d2d6ceae62/README.md#L76-L76), [README.md#L60-L60](https://github.com/icebaker/nano-bots/blob/2bbc92857aa4ca8db5b0af75e96243d2d6ceae62/README.md#L60-L60) (`clm_8fa03a2ef3df44dc020571c5e824da75aa5af20a0625c45d6d43320cfc5ed9a0`)
- [observation/documented] Marketplace sample outputs cannot be authored; they are auto-generated, with each input potentially producing up to five distinct outputs, to ensure intellectual honesty. -- evidence: [README.md#L78-L78](https://github.com/icebaker/nano-bots/blob/2bbc92857aa4ca8db5b0af75e96243d2d6ceae62/README.md#L78-L78) (`clm_0358f7208b37f35b4b2c2dc52e2eb0e9ec2efc298b72d5aaeeb6513523ebb8c0`)

## components (1 claim(s))

- [observation/documented] Listed implementations include a Ruby CLI, a Clinic live editor, a Nano Bots API with a public endpoint, and Sublime Text and VS Code extensions. -- evidence: [README.md#L24-L29](https://github.com/icebaker/nano-bots/blob/2bbc92857aa4ca8db5b0af75e96243d2d6ceae62/README.md#L24-L29) (`clm_ac0c2f8925aaeed30358a4d3b2e628443322d100ba9fdb924781f2c064143318`)

## design-choices (1 claim(s))

- [observation/documented] The project recommends authors publish cartridges under permissive licenses (CC0-1.0 preferred, any SPDX-known license allowed) given unresolved questions about prompt licensing. -- evidence: [README.md#L104-L104](https://github.com/icebaker/nano-bots/blob/2bbc92857aa4ca8db5b0af75e96243d2d6ceae62/README.md#L104-L104), [README.md#L88-L88](https://github.com/icebaker/nano-bots/blob/2bbc92857aa4ca8db5b0af75e96243d2d6ceae62/README.md#L88-L88), [README.md#L90-L90](https://github.com/icebaker/nano-bots/blob/2bbc92857aa4ca8db5b0af75e96243d2d6ceae62/README.md#L90-L90) (`clm_95cd47396e54bc8a7451ea63ca24f07e6412361971b9051398f80cecaeda58ea`)

## workflows (4 claim(s))

- [observation/documented] Repository development practice: contributors share Cartridges via pull request, creating a folder named `@your-nickname` under `/cartridges` with a `profile.yml` describing the author. -- evidence: [README.md#L45-L45](https://github.com/icebaker/nano-bots/blob/2bbc92857aa4ca8db5b0af75e96243d2d6ceae62/README.md#L45-L45), [README.md#L47-L54](https://github.com/icebaker/nano-bots/blob/2bbc92857aa4ca8db5b0af75e96243d2d6ceae62/README.md#L47-L54) (`clm_f4be21367e82f5a823f128b2e5a362a05be6dfa898ee852e7b29544f2828e00b`)
- [observation/documented] Repository development practice: each user folder is tied to the contributor's GitHub username and only accepts pull requests from that user. -- evidence: [README.md#L56-L56](https://github.com/icebaker/nano-bots/blob/2bbc92857aa4ca8db5b0af75e96243d2d6ceae62/README.md#L56-L56) (`clm_c35d887b3559dc4429407dcb8ba1b31ba8f4baecb2e73bd8619585645b54e751`)
- [observation/documented] Repository development practice: cartridges go in a `/cartridges` subfolder as YAML files; a recursive search finds them regardless of internal directory structure. -- evidence: [README.md#L58-L58](https://github.com/icebaker/nano-bots/blob/2bbc92857aa4ca8db5b0af75e96243d2d6ceae62/README.md#L58-L58) (`clm_0c1c2fb61df6f062faea9465357efe991e6bd74faeff2b65247609a36a45ae3a`)
- [observation/documented] Repository development practice: the README recommends studying existing cartridges in the repo and their nbots.io pages as a learning path, and points to the official spec documentation for creating cartridges. -- evidence: [README.md#L33-L33](https://github.com/icebaker/nano-bots/blob/2bbc92857aa4ca8db5b0af75e96243d2d6ceae62/README.md#L33-L33), [README.md#L80-L80](https://github.com/icebaker/nano-bots/blob/2bbc92857aa4ca8db5b0af75e96243d2d6ceae62/README.md#L80-L80) (`clm_f4b2980acc287e4aa4fa03752919b29801bf8e46f8033e8b1d3cca54f89643e2`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] Cartridges can be used by downloading the YAML file or copying its contents into a local YAML file, then running it with an implementation. -- evidence: [README.md#L18-L18](https://github.com/icebaker/nano-bots/blob/2bbc92857aa4ca8db5b0af75e96243d2d6ceae62/README.md#L18-L18) (`clm_a52685c907d49e825bc98da5a2f1834b090b33505e3dad4f02a1f7f9d4e1b260`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Running a Cartridge requires an external implementation; the repository itself does not provide one. -- evidence: [README.md#L22-L22](https://github.com/icebaker/nano-bots/blob/2bbc92857aa4ca8db5b0af75e96243d2d6ceae62/README.md#L22-L22), [README.md#L18-L18](https://github.com/icebaker/nano-bots/blob/2bbc92857aa4ca8db5b0af75e96243d2d6ceae62/README.md#L18-L18) (`clm_107c202059fb396e87b7af0312ce1fd4f01f6b9f3b993d89c7fd10b80088877d`)

## limitations (1 claim(s))

- [observation/documented] The licensing section states it is uncertain whether its licensing approach is practical or enforceable, and that it should be seen as a statement of intention, not a guarantee. -- evidence: [README.md#L106-L106](https://github.com/icebaker/nano-bots/blob/2bbc92857aa4ca8db5b0af75e96243d2d6ceae62/README.md#L106-L106) (`clm_2b851d1538021a759fa45c10be76264010901326734e2a3170ab62a2aa930842`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

