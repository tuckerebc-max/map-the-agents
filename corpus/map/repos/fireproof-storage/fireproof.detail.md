# fireproof-storage/fireproof -- full detail

[Back to orientation](fireproof.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/fireproof-storage/fireproof/404e6c5c7f28109c103626c78da845eb95cabcfa/11291582979dda34.json](../../../wiki/dossiers/fireproof-storage/fireproof/404e6c5c7f28109c103626c78da845eb95cabcfa/11291582979dda34.json)

## specifications (2 claim(s))

- [observation/documented] Fireproof is described as a lightweight embedded document database with encrypted live sync, usable in any JavaScript environment via a unified API for React hooks and a standalone core API. -- evidence: [README.md#L10-L10](https://github.com/fireproof-storage/fireproof/blob/404e6c5c7f28109c103626c78da845eb95cabcfa/README.md#L10-L10) (`clm_9fe52d417bff1dcbcaf9720854b2ae3a8116a656cab72e36cd4a974bc8176685`)
- [observation/documented] From version 0.19 onward the database format is stated to be stable with no backward-compatibility breaks, though internal APIs changed between the 0.19 and 0.20 series. -- evidence: [CHANGELOG.md#L5-L7](https://github.com/fireproof-storage/fireproof/blob/404e6c5c7f28109c103626c78da845eb95cabcfa/CHANGELOG.md#L5-L7) (`clm_4df4c55fe6b47733f3208fd5ea5929f9553efab2a9311583bdcc1ec9a90d9975`)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (2 claim(s))

- [observation/documented] The ledger enforces cryptographic causal consistency and integrity using a hash history, storing and replicating data as content-addressed encrypted blobs suitable for syncing via object storage. -- evidence: [README.md#L21-L21](https://github.com/fireproof-storage/fireproof/blob/404e6c5c7f28109c103626c78da845eb95cabcfa/README.md#L21-L21) (`clm_927b24419fede3dac7c1521f78bea5292ed99546ad2d28e23d440a5b310d18f0`)
- [observation/documented] The project claims multi-writer safety, CRDT-based real-time collaboration, encryption, and a small package size with no wasm, targeting browser, cloud, and edge environments. -- evidence: [README.md#L147-L147](https://github.com/fireproof-storage/fireproof/blob/404e6c5c7f28109c103626c78da845eb95cabcfa/README.md#L147-L147), [README.md#L142-L145](https://github.com/fireproof-storage/fireproof/blob/404e6c5c7f28109c103626c78da845eb95cabcfa/README.md#L142-L145) (`clm_46a82d223be21e55788ed57c6f4c899b259a13c84a467c9328ae7ecec14a1e7c`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: the test suite runs with pnpm run test across projects, with pattern-based filtering, per-file React component tests, and FP_DEBUG env presets for vitest. -- evidence: [README.md#L210-L212](https://github.com/fireproof-storage/fireproof/blob/404e6c5c7f28109c103626c78da845eb95cabcfa/README.md#L210-L212), [README.md#L204-L206](https://github.com/fireproof-storage/fireproof/blob/404e6c5c7f28109c103626c78da845eb95cabcfa/README.md#L204-L206), [README.md#L181-L186](https://github.com/fireproof-storage/fireproof/blob/404e6c5c7f28109c103626c78da845eb95cabcfa/README.md#L181-L186), [README.md#L190-L190](https://github.com/fireproof-storage/fireproof/blob/404e6c5c7f28109c103626c78da845eb95cabcfa/README.md#L190-L190), [README.md#L198-L200](https://github.com/fireproof-storage/fireproof/blob/404e6c5c7f28109c103626c78da845eb95cabcfa/README.md#L198-L200), [README.md#L192-L194](https://github.com/fireproof-storage/fireproof/blob/404e6c5c7f28109c103626c78da845eb95cabcfa/README.md#L192-L194) (`clm_2f902b0fd6a98ec86f0abaef60242d32fa8f29dc1b228af39210faf22387729a`)
- [observation/documented] Repository development practice: a CI workflow badge links to ci.yaml on GitHub Actions, and docs are generated with pnpm run build:docs, which the README cautions pushes directly. -- evidence: [README.md#L251-L253](https://github.com/fireproof-storage/fireproof/blob/404e6c5c7f28109c103626c78da845eb95cabcfa/README.md#L251-L253), [README.md#L3-L8](https://github.com/fireproof-storage/fireproof/blob/404e6c5c7f28109c103626c78da845eb95cabcfa/README.md#L3-L8), [README.md#L249-L249](https://github.com/fireproof-storage/fireproof/blob/404e6c5c7f28109c103626c78da845eb95cabcfa/README.md#L249-L249) (`clm_b839f6346e76d8e0d7ebb5b41f8e588a346c248e992edde377cab525b9631813`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (5 claim(s))

- [observation/documented] React hooks useLiveQuery and useDocument are exposed through useFireproof, with useLiveQuery supporting options like descending order and a result limit. -- evidence: [README.md#L64-L65](https://github.com/fireproof-storage/fireproof/blob/404e6c5c7f28109c103626c78da845eb95cabcfa/README.md#L64-L65), [README.md#L58-L59](https://github.com/fireproof-storage/fireproof/blob/404e6c5c7f28109c103626c78da845eb95cabcfa/README.md#L58-L59), [README.md#L16-L19](https://github.com/fireproof-storage/fireproof/blob/404e6c5c7f28109c103626c78da845eb95cabcfa/README.md#L16-L19) (`clm_9a2ee7315024daa014f5779c6cbe59f6fee2dafc6bdb4f446ed13269be0e916c`)
- [observation/documented] The core API exposes a document-database style interface (fireproof(name)) with put, get, subscribe, and query methods including range queries. -- evidence: [README.md#L126-L126](https://github.com/fireproof-storage/fireproof/blob/404e6c5c7f28109c103626c78da845eb95cabcfa/README.md#L126-L126), [README.md#L133-L136](https://github.com/fireproof-storage/fireproof/blob/404e6c5c7f28109c103626c78da845eb95cabcfa/README.md#L133-L136), [README.md#L121-L122](https://github.com/fireproof-storage/fireproof/blob/404e6c5c7f28109c103626c78da845eb95cabcfa/README.md#L121-L122), [README.md#L128-L131](https://github.com/fireproof-storage/fireproof/blob/404e6c5c7f28109c103626c78da845eb95cabcfa/README.md#L128-L131), [README.md#L124-L124](https://github.com/fireproof-storage/fireproof/blob/404e6c5c7f28109c103626c78da845eb95cabcfa/README.md#L124-L124) (`clm_dd7164f5b24b81119b7f59274ebab4720ba91eb8e002d733c49b2e097d024ad8`)
- [observation/documented] Documents can embed files via a _files property, and an ImgFile React component loads and displays stored images with standard image-element props. -- evidence: [README.md#L89-L89](https://github.com/fireproof-storage/fireproof/blob/404e6c5c7f28109c103626c78da845eb95cabcfa/README.md#L89-L89), [README.md#L115-L115](https://github.com/fireproof-storage/fireproof/blob/404e6c5c7f28109c103626c78da845eb95cabcfa/README.md#L115-L115), [README.md#L91-L100](https://github.com/fireproof-storage/fireproof/blob/404e6c5c7f28109c103626c78da845eb95cabcfa/README.md#L91-L100) (`clm_119b7bb1f416fe372d255c002a419b9af6d1ed480d039b0ababa51a610c9faac`)
- [observation/documented] Log output is controlled by the FP_DEBUG environment variable or logger.setDebug, and FP_FORMAT selects jsonice (multiline JSON), yaml, or json (singleline, the default). -- evidence: [README.md#L222-L222](https://github.com/fireproof-storage/fireproof/blob/404e6c5c7f28109c103626c78da845eb95cabcfa/README.md#L222-L222), [README.md#L171-L173](https://github.com/fireproof-storage/fireproof/blob/404e6c5c7f28109c103626c78da845eb95cabcfa/README.md#L171-L173), [README.md#L224-L226](https://github.com/fireproof-storage/fireproof/blob/404e6c5c7f28109c103626c78da845eb95cabcfa/README.md#L224-L226), [README.md#L165-L165](https://github.com/fireproof-storage/fireproof/blob/404e6c5c7f28109c103626c78da845eb95cabcfa/README.md#L165-L165) (`clm_abba4dbd2bec5ec30d02ff0b5f4008ee7ef696c61afcfd60d861e7e3d65a6191`)
- [observation/documented] The 0.20 series changes the Gateway interface to pass semantic runtime objects instead of Uint8Arrays and Url, renames Database to Ledger with no functional change, replaces memfs with a memory:// URL scheme, and adds a GatewayInterceptor for logging, encryption, or compression. -- evidence: [CHANGELOG.md#L9-L32](https://github.com/fireproof-storage/fireproof/blob/404e6c5c7f28109c103626c78da845eb95cabcfa/CHANGELOG.md#L9-L32) (`clm_853f95f046657846674dd79451c0ab71264a5c331c03595fe56301e8157950bc`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Distribution is via npm packages use-fireproof (core plus React hooks) and @fireproof/core, also loadable from ESM.sh or a jsDelivr browser script tag exposing a global Fireproof. -- evidence: [README.md#L45-L47](https://github.com/fireproof-storage/fireproof/blob/404e6c5c7f28109c103626c78da845eb95cabcfa/README.md#L45-L47), [README.md#L25-L25](https://github.com/fireproof-storage/fireproof/blob/404e6c5c7f28109c103626c78da845eb95cabcfa/README.md#L25-L25), [README.md#L39-L41](https://github.com/fireproof-storage/fireproof/blob/404e6c5c7f28109c103626c78da845eb95cabcfa/README.md#L39-L41), [README.md#L27-L29](https://github.com/fireproof-storage/fireproof/blob/404e6c5c7f28109c103626c78da845eb95cabcfa/README.md#L27-L29), [README.md#L33-L35](https://github.com/fireproof-storage/fireproof/blob/404e6c5c7f28109c103626c78da845eb95cabcfa/README.md#L33-L35) (`clm_9814aad5aead847e6ee7c5677345fac4f62ac004bc22fad5491416df075a267c`)

## limitations (2 claim(s))

- [observation/documented] Deno compatibility requires specific run flags, and the README notes tests are not currently run under Deno, marking Deno publishing as TODO. -- evidence: [README.md#L238-L238](https://github.com/fireproof-storage/fireproof/blob/404e6c5c7f28109c103626c78da845eb95cabcfa/README.md#L238-L238), [README.md#L240-L241](https://github.com/fireproof-storage/fireproof/blob/404e6c5c7f28109c103626c78da845eb95cabcfa/README.md#L240-L241), [README.md#L243-L245](https://github.com/fireproof-storage/fireproof/blob/404e6c5c7f28109c103626c78da845eb95cabcfa/README.md#L243-L245), [README.md#L236-L236](https://github.com/fireproof-storage/fireproof/blob/404e6c5c7f28109c103626c78da845eb95cabcfa/README.md#L236-L236) (`clm_902843c54db66c07b075c91fe5ba530f52f83a62988468a56533c4f468284b50`)
- [observation/documented] By default the FP_STORAGE_URL can include extractKey=_deprecated_internal_api to bypass the key-extraction security check; a warning is emitted and more secure key management is only planned. -- evidence: [README.md#L230-L232](https://github.com/fireproof-storage/fireproof/blob/404e6c5c7f28109c103626c78da845eb95cabcfa/README.md#L230-L232) (`clm_c72f93e36b498bea826406cf7c68fef14eadf50dd23ce6f10250ab718f87563c`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

