# Corpus contract

## Canonical layout

`wiki.yaml` defines a corpus ID, title, profile, default access, source roots, maximum input bytes, and quote limit. Paths are relative to this configuration. Source and wiki roots must be disjoint. `rcw.lock` records the skill, schema, Python version, and configuration digest. New corpora default to internal access.

`data/` holds JSONL tables: packages, sources, source_versions, slices, citations, claims, entities, relationships, pages, gaps, and operations. `pages/` contains typed Markdown with strict YAML frontmatter. `metadata/` contains optional metadata overrides keyed to source inventory keys. `state/manifest.json` records completed package digests. Accepted proposals live in `reports/proposals/`.

Keep these paths in Git. Ignore `build/`, `state/operations/` and `state/leases/`: the first is disposable output; the others may contain temporary restricted source text and recovery journals. Do not include a corpus's temporary packets in an issue, public PR, or skill release.

## Identity

Logical sources and pages use namespaced UUIDv5 identifiers. Known DOI, official ID, URI, or transcript ID determines a source's identity; otherwise the stable root ID and relative path do. Explicit metadata is necessary to retain identity through a source rename. Versions, slices, claims, relationships, packages, and gaps use SHA-256 content identities. Operations use random UUIDv4 identifiers. These are deliberate implementation choices; operation timestamps supply ordering.

Every domain record has a schema version, ID, access, review state, creation/update time, and operation provenance. No-op runs preserve all canonical bytes. The schema files are generated from the same Pydantic models the kernel uses, so proposals, records, and code share field names.

## Evidence

A source version identifies exact source bytes and metadata. A slice identifies a version, text digest, and locator. Markdown/text locators contain actual 1-based line bounds; HTML locators identify an ordinal block in deterministically sanitized text. An HTML block locator is not an original PDF page number. Preserve an original page/section reference in source metadata or extracted text when supplied.

The kernel reopens source text to validate locators and prepare answers. It retains historical records, not full copies of previous source bytes. Keep versioned originals in the upstream corpus. If an upstream file is replaced, old evidence records remain and the audit labels the unavailable old version; it never presents the replacement as the earlier evidence.

An extraction proposal contains `claims`, `entities`, and `relationships`. Claims cite supplied `slice_ids`; synthesis and answer assertions cite `claim_ids`. All fields are defined in `schemas/v1/`. Unknown fields and fabricated IDs fail validation. Use `scope` for population, jurisdiction, timeframe, setting, method, instrument status, and qualifiers.

## Review and access

Review states: extracted, mechanically_checked, human_reviewed, approved, disputed, superseded, unverified. The agent/kernel does not grant human-reviewed or approved status. A reviewer may make a documented record change on the review branch; validate that diff through the same audit. Access downgrades require a separately reviewed redaction product.

Access follows `public < internal < confidential < restricted`. Derived assertions inherit the maximum supporting class. A source's metadata access is its asserted classification, not proof of a hosting system's permissions. Store each corpus in a repository whose membership may access its most restrictive records. Metadata filtering does not make a public Git repository safe for confidential data.

## Machine-owned page blocks

The kernel encloses its evidence section in `rcw:begin`/`rcw:end` HTML comments with a stable owner. It fails on malformed, overlapping, duplicate, or missing blocks. Human notes outside the block survive reingestion byte-for-byte. Import human synthesis into an evidence proposal before including it in a published view.
