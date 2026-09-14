# memorax-ai/memorax-code -- full detail

[Back to orientation](memorax-code.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/memorax-ai/memorax-code/1525c20fbcad8c688bfaf4bb54dc117876fd6a09/916cf8e021cf3d6f.json](../../../wiki/dossiers/memorax-ai/memorax-code/1525c20fbcad8c688bfaf4bb54dc117876fd6a09/916cf8e021cf3d6f.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (3 claim(s))

- [observation/documented] The system integrates seven coding clients with one local Backend, a capability-oriented modular monolith, surrounded by six client deployment adapters, a shared runtime source layer, and an npm assembly/CLI layer. -- evidence: [ARCHITECTURE.md#L28-L32](https://github.com/memorax-ai/memorax-code/blob/1525c20fbcad8c688bfaf4bb54dc117876fd6a09/ARCHITECTURE.md#L28-L32), [ARCHITECTURE.md#L36-L39](https://github.com/memorax-ai/memorax-code/blob/1525c20fbcad8c688bfaf4bb54dc117876fd6a09/ARCHITECTURE.md#L36-L39) (`clm_66c97585ac8a651a827302d786cec72fe60923a46c914bfe5b1e9d16e5d90c54`)
- [observation/documented] The Backend owns the local memory service, repository scope, trace, lifecycle, and update scheduling, but must not own model execution, provider credentials, or native transcript creation. -- evidence: [ARCHITECTURE.md#L126-L138](https://github.com/memorax-ai/memorax-code/blob/1525c20fbcad8c688bfaf4bb54dc117876fd6a09/ARCHITECTURE.md#L126-L138) (`clm_74376d914b1cfd1da92279991a398dc08c40b9d10f10db9e750b238ffd11797c`)
- [observation/documented] adapter-common is a shared source layer consumed by the Backend and all six adapters, providing connection primitives, credential storage, locks, and Hook transport; it is not an independently deployed service. -- evidence: [ARCHITECTURE.md#L140-L143](https://github.com/memorax-ai/memorax-code/blob/1525c20fbcad8c688bfaf4bb54dc117876fd6a09/ARCHITECTURE.md#L140-L143), [ARCHITECTURE.md#L126-L138](https://github.com/memorax-ai/memorax-code/blob/1525c20fbcad8c688bfaf4bb54dc117876fd6a09/ARCHITECTURE.md#L126-L138) (`clm_eaebe6aacefec997e47210a9018d2960f8b36aaeb3825a557027bbd36a4e9512`)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributors are directed to read CONTRIBUTING.md before making changes, and AGENTS.md defines working rules for coding agents, runtime/data invariants, and Git handoff requirements. -- evidence: [ARCHITECTURE.md#L9-L18](https://github.com/memorax-ai/memorax-code/blob/1525c20fbcad8c688bfaf4bb54dc117876fd6a09/ARCHITECTURE.md#L9-L18), [README.md#L356-L358](https://github.com/memorax-ai/memorax-code/blob/1525c20fbcad8c688bfaf4bb54dc117876fd6a09/README.md#L356-L358) (`clm_dedbb3ef52a30450ea7d4107a30759a1d7326e42ad2b0a8731b9af85351d99f2`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] Adapter Hooks and plugins communicate with the Backend via versioned, client-qualified local HTTP commands carrying JSON and token headers, with a request deadline and optional cancellation; the transport does not retry or start the Backend. -- evidence: [ARCHITECTURE.md#L147-L165](https://github.com/memorax-ai/memorax-code/blob/1525c20fbcad8c688bfaf4bb54dc117876fd6a09/ARCHITECTURE.md#L147-L165) (`clm_33c49998aa682dd0b060d2ac0b03789410322cce02f10502e48299c9b766fc10`)

## memory-state (3 claim(s))

- [observation/documented] Memory is divided into four categories: Coding Memory (engineering lessons), Repo Memory (repository knowledge), Personal Memory (user preferences), and Procedure Memory (reusable task steps). -- evidence: [README.md#L235-L240](https://github.com/memorax-ai/memorax-code/blob/1525c20fbcad8c688bfaf4bb54dc117876fd6a09/README.md#L235-L240) (`clm_00ef1fa849729e7a115af31d85fd43cd1fb0031427e120f1f4efca65a9467d02`)
- [observation/documented] Personal and Procedure Memory stay in the current repository under .repo_memory/; writes compare existing content so equivalent requests make no change and conflicts update or supersede entries. -- evidence: [README.md#L242-L250](https://github.com/memorax-ai/memorax-code/blob/1525c20fbcad8c688bfaf4bb54dc117876fd6a09/README.md#L242-L250) (`clm_6e76580d4a2d5f02c2872490438c8d5dd3af395e3f83599b0b98ede8ba8bf69b`)
- [observation/documented] Local trace capture is on by default for supported clients and retained traces under MEMORAX_CODE_HOME may include prompts, responses, recalled memory, reminder text, and local paths; it can be switched to metadata-only or disabled. -- evidence: [README.md#L272-L278](https://github.com/memorax-ai/memorax-code/blob/1525c20fbcad8c688bfaf4bb54dc117876fd6a09/README.md#L272-L278) (`clm_6a09ff5d063ad441a6116c83ff33e5750b49f3acfc6a16a9225f1e97e4c3b3e3`)

## orchestration (2 claim(s))

- [observation/documented] After setup, the managed Backend schedules a detached updater that locks, resolves a channel target, installs an exact published version via the package-replacement path, and reuses non-interactive setup reconciliation. -- evidence: [ARCHITECTURE.md#L262-L275](https://github.com/memorax-ai/memorax-code/blob/1525c20fbcad8c688bfaf4bb54dc117876fd6a09/ARCHITECTURE.md#L262-L275), [ARCHITECTURE.md#L301-L309](https://github.com/memorax-ai/memorax-code/blob/1525c20fbcad8c688bfaf4bb54dc117876fd6a09/ARCHITECTURE.md#L301-L309) (`clm_4db40c8d6b9342e787b37f5653b3f25f3dd0ce716d22e502bac1edf1c8baf3a6`)
- [observation/documented] Automatic Search on turn-start Hooks is disabled by default; the usual retrieval path is the client invoking memorax-cli through the shared Skill, while Hooks still provide identity, scope, and writeback coordination. -- evidence: [ARCHITECTURE.md#L383-L387](https://github.com/memorax-ai/memorax-code/blob/1525c20fbcad8c688bfaf4bb54dc117876fd6a09/ARCHITECTURE.md#L383-L387) (`clm_2799c9f6f086415b6b0a5f59ed65bdede1342f137fd7f8f58fdd0c7e1af1c0ae`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] The package requires Node.js 20 or newer (Node 24 LTS recommended), and DeepSeek Harness releases require Node ^22.19.0 || >=24.0.0 with pnpm on PATH; MemoraX Code does not install or update DSH. -- evidence: [README.md#L55-L56](https://github.com/memorax-ai/memorax-code/blob/1525c20fbcad8c688bfaf4bb54dc117876fd6a09/README.md#L55-L56), [README.md#L58-L61](https://github.com/memorax-ai/memorax-code/blob/1525c20fbcad8c688bfaf4bb54dc117876fd6a09/README.md#L58-L61) (`clm_e0814f36d299d52be5e1186498df052e916c8b65e0f2278c71a2e0600a0dbfa2`)
- [observation/documented] On Linux, guest credentials require /usr/bin/secret-tool from libsecret and an available Secret Service, and MemoraX search and writeback require network access. -- evidence: [README.md#L63-L66](https://github.com/memorax-ai/memorax-code/blob/1525c20fbcad8c688bfaf4bb54dc117876fd6a09/README.md#L63-L66) (`clm_dfdc7aa10d901b5177984db51d457bc54dda47d840c7823fcf94c64072fe85ea`)

## limitations (2 claim(s))

- [observation/documented] Trae can use the Skill for Repo Memory but does not currently expose a headless worker for automatic Repo Memory maintenance, and automatic quota reminders are not listed for DeepSeek Harness. -- evidence: [README.md#L254-L263](https://github.com/memorax-ai/memorax-code/blob/1525c20fbcad8c688bfaf4bb54dc117876fd6a09/README.md#L254-L263) (`clm_fc49aa3aba3966266d452b4e9afc40fb1dec4bea97059c7366292f6883a220ff`)
- [observation/documented] The MemoraX platform does not currently support attaching a Mark ID to an already-registered account, so guest users must obtain the Mark ID before registering to keep guest memory. -- evidence: [README.md#L139-L143](https://github.com/memorax-ai/memorax-code/blob/1525c20fbcad8c688bfaf4bb54dc117876fd6a09/README.md#L139-L143) (`clm_e496b6ef98a44ca543b57ba0e35e3d957a5960b25a0d668bc2bb8f7c576821f6`)

## relevance (1 claim(s))

- [observation/documented] The product targets the problem that new coding-agent sessions start without prior architecture knowledge, failed attempts, repository rules, or working preferences, providing a shared memory layer across supported clients. -- evidence: [README.md#L39-L41](https://github.com/memorax-ai/memorax-code/blob/1525c20fbcad8c688bfaf4bb54dc117876fd6a09/README.md#L39-L41), [README.md#L43-L47](https://github.com/memorax-ai/memorax-code/blob/1525c20fbcad8c688bfaf4bb54dc117876fd6a09/README.md#L43-L47) (`clm_240adc51d6340123da53373e82062821f0b3eac1fd436951d486d551c7b93822`)

