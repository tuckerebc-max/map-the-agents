# Source profiles

Use `schemas/v1/source-metadata.schema.json` for exact fields. A file's sidecar is `file.md.source.json`; a package member can embed the same metadata; `rcw metadata` can register it inside the wiki. Do not write a sidecar into an established read-only source root.

Required common fields: title, creator, source_type. Supply date when known, access, identifiers, and original URL. Missing dates remain null. Use a descriptive label only when the source lacks a title and label it as such in research notes.

| Profile | Record and check |
|---|---|
| Scholarly | source_type scholarly_article/book/report; DOI when actually present, venue, methodology, population, reported outcomes and uncertainty |
| Policy/legal | source_type legislation/regulation/guidance; jurisdiction, legal_status, status_date, provision; legislation and regulation require all four |
| Organizational | source_type organizational_record; organization, role, attribution, verified_date; attribute statements to the named office or source |
| Interview/session | source_type interview/session; confidential or restricted access; granted consent with separate quote, paraphrase, identify, publish booleans |
| General | Explicit type and attribution; distinguish factual context from recommendations and methods |
| Mixed | Apply the relevant source rules separately to each member; retain distinct evidence types in synthesis |

The selected corpus profile guides the researcher. Runtime requirements follow `source_type` so a mixed corpus receives the same source-level checks.

## Legal materials

Preserve whether an instrument is introduced, pending, enacted, effective, amended, stayed, withdrawn, or expired. Do not label a bill as law. Do not invent a DOI for legislation. Citation export preserves legal source types and jurisdiction. A source's historical status is not a current-law determination; new status requires a dated original source.

## Generated research packages

Use `synthesis_report` for model-generated reports. `original_sources` may list reported title, identifier, and locator; this records attribution, not verified access. The kernel marks claims from these reports `original_missing` and creates gaps. Add the original evidence as a separate source, re-extract its claims, and cite those original slices in the next synthesis. A report repeating the same original is not independent corroboration.

## Interview consent

Example when only internal paraphrase is permitted:

```json
{"title":"Participant P01 interview","creator":"Participant P01","date":"2026-08-26","source_type":"interview","access":"confidential","identifiers":{"transcript_id":"P01-20260826"},"consent":{"state":"granted","quote":false,"paraphrase":true,"identify":false,"publish":false}}
```

Missing, pending, or denied consent blocks ingest. Do not infer permission from file access. Use a pseudonym before ingest when identification is prohibited. The tool screens substantial verbatim overlap; it cannot determine whether a paraphrase remains identifying. The researcher must make that judgment.
