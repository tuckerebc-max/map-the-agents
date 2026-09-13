# Analyze and ask

## Analyze

Run `rcw analyze prepare WIKI --scope changed --access restricted --limit 200`. Choose an access ceiling authorized for the current researcher. Open the returned packet. The default scope selects claims not yet covered by current analysis pages; `--scope full` starts a bounded full-corpus pass. If `remaining_claims` is nonzero, do not describe the packet as exhaustive.

Use `schemas/v1/analysis-proposal.schema.json`. Propose pages of type concept, finding, debate, or theme. Each page has a stable key, title, and assertions. Each assertion contains text, supporting claim_ids, and optional opposing_claim_ids. Propose relationships and gaps separately.

Judge convergence only after checking shared original-source lineage. A statute and a commentary repeating that statute are not independent legal authorities. A finding from one sample does not contradict a result from a different sample merely because their numbers differ. A recommendation is not a measured effect. Record scope mismatches and qualifications explicitly.

A gap requires question, reason, claim_ids when available, and optionally suggested_source. A relationship requires subject, predicate, object, claim_ids, and rationale. Supported predicates are listed in the schema; arbitrary graph labels are rejected. Apply with `rcw analyze apply WIKI OPERATION_ID PROPOSAL_JSON` and review the resulting pages.

## Ask

Run `rcw ask prepare WIKI "QUESTION" --access internal --limit 40`. Retrieval is lexical SQLite FTS5, with a bounded set of claims and reopened original slices. The wiki and index guide retrieval; answer from the slice text and its profile/lineage metadata. If retrieval misses a known synonym, prepare a focused second question/search and disclose the search boundary. Never claim complete corpus coverage merely because the packet is nonempty.

Use `schemas/v1/answer-proposal.schema.json` with status, assertions, limitations, schema_version, and the returned operation_id. Status must be:

- answered: accessible original evidence supports the bounded answer;
- partially_answered: some parts or original authorities are missing;
- conflicted: material accessible evidence disagrees;
- insufficient_evidence: no supported answer can be given.

Every substantive assertion requires claim IDs. A refusal has no assertions and states the evidence gap in limitations. Limitations describe evidence boundaries; do not hide new factual assertions there. Unverified or disputed claims require a qualified status and explicit limitations. Keep opposing evidence visible and identify the scope of any apparent contradiction.

Complete with `rcw ask complete WIKI OPERATION_ID PROPOSAL_JSON`. The returned Markdown links to the HTML renderer's evidence cards. Give the user the underlying source title and locator as well when no rendered site exists. Add `--file-answer` only when filing the answer is requested: supported assertions become an answer page; a refusal becomes a gap. The command does not conduct external research.

## Evidence review

The kernel proves reference validity, accessible source bytes, bounded quotation overlap, and access inheritance. It does not prove the proposition is entailed, that a causal design is valid, or that the evidence generalizes. Those are explicit agent/reviewer judgments. Preserve uncertainty instead of promoting mechanically checked material to approved.
