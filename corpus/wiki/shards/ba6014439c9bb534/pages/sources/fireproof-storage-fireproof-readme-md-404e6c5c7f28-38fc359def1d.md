---
access: public
aliases: []
claim_ids:
- clm_119b7bb1f416fe372d255c002a419b9af6d1ed480d039b0ababa51a610c9faac
- clm_2f902b0fd6a98ec86f0abaef60242d32fa8f29dc1b228af39210faf22387729a
- clm_46a82d223be21e55788ed57c6f4c899b259a13c84a467c9328ae7ecec14a1e7c
- clm_902843c54db66c07b075c91fe5ba530f52f83a62988468a56533c4f468284b50
- clm_927b24419fede3dac7c1521f78bea5292ed99546ad2d28e23d440a5b310d18f0
- clm_9814aad5aead847e6ee7c5677345fac4f62ac004bc22fad5491416df075a267c
- clm_9a2ee7315024daa014f5779c6cbe59f6fee2dafc6bdb4f446ed13269be0e916c
- clm_9fe52d417bff1dcbcaf9720854b2ae3a8116a656cab72e36cd4a974bc8176685
- clm_abba4dbd2bec5ec30d02ff0b5f4008ee7ef696c61afcfd60d861e7e3d65a6191
- clm_b839f6346e76d8e0d7ebb5b41f8e588a346c248e992edde377cab525b9631813
- clm_c72f93e36b498bea826406cf7c68fef14eadf50dd23ce6f10250ab718f87563c
- clm_dd7164f5b24b81119b7f59274ebab4720ba91eb8e002d733c49b2e097d024ad8
maturity: draft
page_id: pg_791e94407bec5c62b30538fc359def1d
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_41ebcae2d9675ab68d8bc923d54a526b
title: fireproof-storage/fireproof/README.md @ 404e6c5c7f28
updated_at: '2026-09-14T03:51:26Z'
---

# fireproof-storage/fireproof/README.md @ 404e6c5c7f28

<!-- rcw:begin owner=source:src_41ebcae2d9675ab68d8bc923d54a526b block=evidence -->
- Documents can embed files via a _files property, and an ImgFile React component loads and displays stored images with standard image-element props. [@claim:clm_119b7bb1f416fe372d255c002a419b9af6d1ed480d039b0ababa51a610c9faac]
- Repository development practice: the test suite runs with pnpm run test across projects, with pattern-based filtering, per-file React component tests, and FP_DEBUG env presets for vitest. [@claim:clm_2f902b0fd6a98ec86f0abaef60242d32fa8f29dc1b228af39210faf22387729a]
- The project claims multi-writer safety, CRDT-based real-time collaboration, encryption, and a small package size with no wasm, targeting browser, cloud, and edge environments. [@claim:clm_46a82d223be21e55788ed57c6f4c899b259a13c84a467c9328ae7ecec14a1e7c]
- Deno compatibility requires specific run flags, and the README notes tests are not currently run under Deno, marking Deno publishing as TODO. [@claim:clm_902843c54db66c07b075c91fe5ba530f52f83a62988468a56533c4f468284b50]
- The ledger enforces cryptographic causal consistency and integrity using a hash history, storing and replicating data as content-addressed encrypted blobs suitable for syncing via object storage. [@claim:clm_927b24419fede3dac7c1521f78bea5292ed99546ad2d28e23d440a5b310d18f0]
- Distribution is via npm packages use-fireproof (core plus React hooks) and @fireproof/core, also loadable from ESM.sh or a jsDelivr browser script tag exposing a global Fireproof. [@claim:clm_9814aad5aead847e6ee7c5677345fac4f62ac004bc22fad5491416df075a267c]
- React hooks useLiveQuery and useDocument are exposed through useFireproof, with useLiveQuery supporting options like descending order and a result limit. [@claim:clm_9a2ee7315024daa014f5779c6cbe59f6fee2dafc6bdb4f446ed13269be0e916c]
- Fireproof is described as a lightweight embedded document database with encrypted live sync, usable in any JavaScript environment via a unified API for React hooks and a standalone core API. [@claim:clm_9fe52d417bff1dcbcaf9720854b2ae3a8116a656cab72e36cd4a974bc8176685]
- Log output is controlled by the FP_DEBUG environment variable or logger.setDebug, and FP_FORMAT selects jsonice (multiline JSON), yaml, or json (singleline, the default). [@claim:clm_abba4dbd2bec5ec30d02ff0b5f4008ee7ef696c61afcfd60d861e7e3d65a6191]
- Repository development practice: a CI workflow badge links to ci.yaml on GitHub Actions, and docs are generated with pnpm run build:docs, which the README cautions pushes directly. [@claim:clm_b839f6346e76d8e0d7ebb5b41f8e588a346c248e992edde377cab525b9631813]
- By default the FP_STORAGE_URL can include extractKey=_deprecated_internal_api to bypass the key-extraction security check; a warning is emitted and more secure key management is only planned. [@claim:clm_c72f93e36b498bea826406cf7c68fef14eadf50dd23ce6f10250ab718f87563c]
- The core API exposes a document-database style interface (fireproof(name)) with put, get, subscribe, and query methods including range queries. [@claim:clm_dd7164f5b24b81119b7f59274ebab4720ba91eb8e002d733c49b2e097d024ad8]
<!-- rcw:end owner=source:src_41ebcae2d9675ab68d8bc923d54a526b block=evidence -->

## Researcher notes

