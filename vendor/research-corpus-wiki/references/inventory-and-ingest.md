# Inventory and ingest

## Initialize and register

```bash
rcw init /workbench/research-wiki --sources /workbench/source-packages --profile mixed --access internal
rcw inventory /workbench/research-wiki
rcw metadata /workbench/research-wiki primary:study.md /workbench/study-metadata.json
rcw sync /workbench/research-wiki
```

These paths illustrate separate source/wiki boundaries; use actual workbench paths. Inventory classifies new, changed, unchanged, and blocked items. `duplicate_of` identifies byte-identical candidates; preserve them without counting them as independent evidence. `missing` identifies prior package paths no longer present. Do not silently delete their records.

Supported inputs: UTF-8 Markdown, plain text, HTML, and completed manifest packages. Unsupported binary files are listed as blocked. Route PDFs, scans, audio, and video through an extraction workflow that preserves original identifiers and locators; do not pretend a filename is extracted evidence.

A package is a directory containing `manifest.json`:

```json
{"complete":true,"files":[{"path":"report.md","metadata":{"title":"Research report","creator":"Research team","source_type":"synthesis_report","date":"2026-09-13","access":"internal"}}]}
```

The manifest owns its directory and avoids double-ingesting members. A false/missing completion flag, missing files, unsupported paths, duplicate members, and unknown manifest fields block the package. A manifest may also carry title, bibliography, and unresolved_items; preserve these upstream and use original_sources metadata for attributable originals.

## Prepare, extract, apply

Run `rcw ingest prepare WIKI INVENTORY_KEY`. Open the returned `packet_path`. It contains source metadata, exact slices, IDs, and a source/base fingerprint. Read the relevant slices before producing a proposal. Store the proposal outside source roots, normally beside the packet.

A minimal proposal has this shape. Replace the operation and slice identifiers with values actually returned by preparation:

```json
{"schema_version":"1.0","operation_id":"op_from_packet","claims":[{"key":"finding-1","text":"The reported improvement applies to the study sample.","slice_ids":["slc_from_packet"],"evidence_type":"empirical_result","scope":{"population":"study sample"}}],"entities":[],"relationships":[]}
```

The example identifiers are explanatory; only full returned IDs are valid. Run `rcw ingest apply WIKI OPERATION_ID PROPOSAL_JSON`. The apply command validates schema, IDs, source state, quotation permissions, access, and page integrity; writes through a rollback journal; and verifies source bytes again before completing.

Extract bounded propositions, not whole paragraphs. Preserve conditions, qualifications, units, outcomes, comparator, and time period. For a source that contains no eligible claims, submit an empty claims list and explain that choice in the review packet. Do not fabricate content to populate a page.

Entity proposals use `key`, `name`, `entity_type`, `claim_keys`, optional aliases and external_ids. They remain proposed identities. Relationship endpoints can refer to the proposal's claim/entity keys or an allowed returned ID. `claim_ids` on a relationship may use the same claim keys during ingestion. An evidence link is mandatory; do not use a visual association as proof of support.

## Reconcile and resume

After a successful apply, repeat preparation with the same source/proposal to check `changed: false`. Prepare a new operation for each apply attempt after the corpus changes. Never reuse a stale packet. `sync` is a deterministic queue command; the skill orchestrates its prepare/apply loop and checkpoints each package. It does not invoke a model or start hidden background work.

Changed source bytes create a source version and retain older records. A source page's stable owned block is replaced, while its handwritten notes are preserved. Existing cross-source pages that cite superseded claims are marked unverified and require delta analysis. Refresh them with both supporting and opposing current evidence.
