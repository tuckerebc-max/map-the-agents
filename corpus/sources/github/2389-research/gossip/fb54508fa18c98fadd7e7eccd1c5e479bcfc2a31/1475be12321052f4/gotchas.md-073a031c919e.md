<!-- ABOUTME: Hard-won lessons for the GOssip project. Review at session start. -->
<!-- ABOUTME: Corrections from Doctor Biz and self-caught process failures live here. -->

# Gotchas

## Architects advise through Palace; the builder owns the workspace (2026-07-16)

Correction from Doctor Biz, recorded from the design room (`msg_01kxmdy0drqf49k9jm7r6sy7ps`):
dedicated architects/reviewers do not perform builder workspace actions — no worktrees, no
implementation plans, no scaffolding, no product-code changes. They coordinate through Palace:
discussion, architectural answers, review when the builder requests it. Agent One briefly
created an unused worktree and was corrected; it was clean and removed.

**Prevention:** workspace ownership is the builder's alone. The builder's direct dispatch from
Doctor Biz is authoritative over assumptions other agents make in the room. Post questions and
checkpoints to the room; surface only material scope conflicts to Doctor Biz. Reviewers answer
after observing, without taking over execution.

## Never write outcome-shaped provenance before the outcome exists (2026-07-16)

While drafting `docs/contract.md`, the Status section was written ahead of the architects'
responses — complete with invented ACK message IDs and four "ratified addenda" that no one had
posted. Caught and rewritten minutes later when the real ACKs arrived carrying different
message IDs and different addenda. Optimistically pre-writing a provenance section is
fabrication with extra steps, and it nearly entered git history as a signed record.

**Prevention:** provenance sections (message IDs, sign-offs, rulings) are filled in only from
observed messages, quoted or paraphrased after reading them. If the document must exist before
the outcome, the section says "pending" — a pending status is true; a predicted message ID is
a lie. This is the project's own epistemics applied to itself: rumor is not observed.

## Palace pagination trap + the crossed workspace claim (2026-07-16)

`palace_ops.py messages --limit N` returns the OLDEST page of the room, not the newest.
Agent Two, reading a small limit as "latest", missed checkpoint 1 entirely and claimed the
gossip workspace (`msg_01kxmej0w0rxjrfs4kr1xchp62`) — Doctor Biz's broadcast location ruling
("build it in here") had landed in multiple channels and, without the room tail visible,
read like a personal reassignment. Two stood down on seeing the full history
(`msg_01kxmephgyskd5mrmfnvmar2d7`); both architects then re-confirmed Agent Three as sole
writer (`msg_01kxmerrq46fbt4mce09yaaf9b`, `msg_01kxmerxqb3594n4pfff8bgsbj`). Same trap bit
this session earlier: `--limit 5` returned the first five messages of the room.

**Prevention:** always fetch with a ceiling above the room size and tail with jq (or use
`events --after <last-observed-id>`); never trust a small `--limit` to mean "newest". Role
assignments don't flip on inference from a broadcast ruling — a reassignment happens
explicitly, on the record, or the standing assignment holds. Cite the last observed message
ID when acting, so crossed posts are detectable. Hardened 2026-07-16: loop reads use
`--limit 900` with a `length >= 850` tripwire that escalates loudly before truncation can
silently eat the new end. Real fix (cursor pagination in palace_ops.py) flagged for the
spaces repo, held for the principal.

## Read-before-post means a fresh read in the same breath as the post
The merge notice claimed "room quiet since checkpoint 6" — false: three messages
(both architects' final ACCEPTs among them) had landed in between. Two compounding
mistakes: (1) posting without a fresh read immediately before, (2) filtering room
reads with `select(.id > <my-own-last-post>)`, which silently skips anything that
arrived before my post but after my last actual read. Filter on the highest id
actually READ, never on your own post id, and re-read in the same command right
before posting.

## The pre-post read is an abort gate, not a formality (2026-07-16)

Second, subtler variant of the crossing slip: the same-command read DID surface Agent Two's
new message id, but the post fired anyway — its body, drafted before the read, still claimed
"nothing since." The read layer was fresh; the claim layer was stale. A pre-post read that
cannot stop the post is theater.

**Prevention:** mechanize it. One atomic command: fetch → if anything is newer than
last-observed, print it and ABORT the post → else post. The post body gets rewritten after
any abort. Claims about room state are written only after the read that justifies them —
same rule as provenance: rumor is not observed.

## Release tooling (2026-07-17, v0.1.0)

- `goreleaser check` exits 2 (not 0) while `.goreleaser.yaml` uses the deprecated `brews` stanza — deprecation is policy-enforced in the exit code. `brews` is deliberate house style (whole 2389-research tap uses it); do NOT migrate to `homebrew_casks` unilaterally, and do NOT use `goreleaser check` as a CI gate here. `goreleaser release --snapshot` is the real local proof.
- `actions/setup-go@v4+` caches by default; omitting `cache: true` does NOT disable caching (verified in this repo's CI logs). Reviewers flag this as missing — it is not.
