# Audit, recovery, and GitHub review

`rcw audit WIKI --level working` validates schemas, references, locators, quotation flags, access inheritance, generated page content, frontmatter, ownership markers, and supersession. `--level pr` also scans canonical files for common credential patterns. The release level runs the same corpus checks; the package's CI adds tests, property checks, type/lint checks, schema consistency, and demonstrations. A corpus audit alone does not prove production readiness.

A valid old source locator whose original bytes were replaced is a historical warning; an unavailable current source is an error. Unknown record fields, altered excerpts, missing referenced IDs, lower-access derived records, malformed markers, and unregistered text in a generated block are errors. Alias collisions and unverified/disputed material remain review warnings.

## Review packet

Run `rcw review-packet WIKI` and save its JSON to an appropriate private review artifact. It includes corpus counts, operation output paths, audit evidence, open gaps, unverified claims, and access counts. The packet can reveal restricted questions and identifiers; keep it at the corpus's access level.

Write a concise PR description from the actual packet: sources added/changed, page blocks changed, claims introduced or superseded, disagreements/gaps, access decisions, audit result, and preview location. Use the connected GitHub tools or authenticated git/gh available in the workbench. Respect existing authorization for uploads and draft PRs; do not make the researcher approve each reversible operation again. Follow actual repository instructions and branch protections. Never automatically merge, change repository visibility, or publish a restricted preview.

## Recovery

Mutating apply operations acquire an exclusive local lock. Proposal work happens before this lock, so interrupted model calls do not hold the corpus indefinitely. The packet records a canonical base digest, preventing an old proposal from overwriting changes from another operation. Across clones, GitHub review/merge rules remain the concurrency control.

On `RCW_LEASE_ACTIVE`, identify the holder and wait for that operation or investigate its failure. `rcw recover WIKI` refuses a live process, another host's uncertain lock, and any target with a third-party change. For a confirmed crashed transaction, it restores journaled prior bytes. No source bytes are restored or moved by this command.

| Error | Action |
|---|---|
| RCW_METADATA_REQUIRED / RCW_PACKAGE_BLOCKED | Inspect the inventory reason; register documented metadata or complete extraction upstream |
| RCW_PROPOSAL_OUT_OF_SCOPE | Correct the proposal using IDs from its current packet |
| RCW_SOURCE_MUTATED / RCW_BASE_DIVERGED | Preserve the attempted proposal as context, then prepare anew |
| RCW_MARKER_CONFLICT / RCW_PAGE_CONTENT_DRIFT | Review and repair the affected page on a branch; do not rewrite unrelated content |
| RCW_ACCESS_DOWNGRADE | Produce an independently reviewed redaction; do not downgrade the source record |
| RCW_CONSENT_QUOTE / RCW_QUOTE_LIMIT | Paraphrase within the actual permission and retain locator/citation |
| RCW_OUTPUT_EDITED / RCW_OUTPUT_NOT_EMPTY | Use a new output directory; preserve the existing user's files |

The CLI uses JSON errors and exits 3 for kernel failures; normal CLI usage errors exit 2. Inspect the stable error code for recovery decisions rather than parsing prose.
