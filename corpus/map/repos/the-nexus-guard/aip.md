# the-nexus-guard/aip

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 3d8c873139ea @ e93b0149ff82da41

## Summary (orientation draft, not independently verified)

Selected evidence records: AIP is organized into three layers: an identity layer (Ed25519 keypairs, DIDs, challenge-response), a trust layer (vouches, scopes, paths, revocation), and a communication layer (E2E encrypted messaging). The protocol is designed to be decentralized with no central registry, local-first so each agent keeps its own trust view, and auditable via signed 'isnad' trust chains.

## Source coverage

Source coverage (partial): 6 of 38 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] A draft 0xSKL integration spec (v0.1.0) defines an extended skill manifest with an AIP author block (DID, public key, Ed25519 signature over sha256 of name+version+content_hash+timestamp) and Cage execution policy based on author trust score. -- evidence: [docs/0xskl_integration_spec.md#L64-L84](https://github.com/The-Nexus-Guard/aip/blob/3d8c873139ea6d4db421a57886fcfccc35925fcf/docs/0xskl_integration_spec.md#L64-L84), [docs/0xskl_integration_spec.md#L3-L6](https://github.com/The-Nexus-Guard/aip/blob/3d8c873139ea6d4db421a57886fcfccc35925fcf/docs/0xskl_integration_spec.md#L3-L6), [docs/0xskl_integration_spec.md#L32-L58](https://github.com/The-Nexus-Guard/aip/blob/3d8c873139ea6d4db421a57886fcfccc35925fcf/docs/0xskl_integration_spec.md#L32-L58), [docs/0xskl_integration_spec.md#L88-L88](https://github.com/The-Nexus-Guard/aip/blob/3d8c873139ea6d4db421a57886fcfccc35925fcf/docs/0xskl_integration_spec.md#L88-L88)
- components (2 claim(s)):
  - [observation/documented] AIP is organized into three layers: an identity layer (Ed25519 keypairs, DIDs, challenge-response), a trust layer (vouches, scopes, paths, revocation), and a communication layer (E2E encrypted messaging). -- evidence: [README.md#L70-L74](https://github.com/The-Nexus-Guard/aip/blob/3d8c873139ea6d4db421a57886fcfccc35925fcf/README.md#L70-L74), [README.md#L62-L62](https://github.com/The-Nexus-Guard/aip/blob/3d8c873139ea6d4db421a57886fcfccc35925fcf/README.md#L62-L62), [README.md#L76-L80](https://github.com/The-Nexus-Guard/aip/blob/3d8c873139ea6d4db421a57886fcfccc35925fcf/README.md#L76-L80), [README.md#L64-L68](https://github.com/The-Nexus-Guard/aip/blob/3d8c873139ea6d4db421a57886fcfccc35925fcf/README.md#L64-L68)
  - [observation/documented] An identity middleware (AIPMiddleware) signs outgoing HTTP requests and verifies incoming ones, exposing trust-score-gated processing and peer discovery by minimum trust. -- evidence: [README.md#L201-L201](https://github.com/The-Nexus-Guard/aip/blob/3d8c873139ea6d4db421a57886fcfccc35925fcf/README.md#L201-L201), [README.md#L209-L210](https://github.com/The-Nexus-Guard/aip/blob/3d8c873139ea6d4db421a57886fcfccc35925fcf/README.md#L209-L210), [README.md#L204-L206](https://github.com/The-Nexus-Guard/aip/blob/3d8c873139ea6d4db421a57886fcfccc35925fcf/README.md#L204-L206), [README.md#L193-L193](https://github.com/The-Nexus-Guard/aip/blob/3d8c873139ea6d4db421a57886fcfccc35925fcf/README.md#L193-L193)
- design-choices (2 claim(s)):
  - [observation/documented] The protocol is designed to be decentralized with no central registry, local-first so each agent keeps its own trust view, and auditable via signed 'isnad' trust chains. -- evidence: [README.md#L84-L88](https://github.com/The-Nexus-Guard/aip/blob/3d8c873139ea6d4db421a57886fcfccc35925fcf/README.md#L84-L88), [README.md#L146-L146](https://github.com/The-Nexus-Guard/aip/blob/3d8c873139ea6d4db421a57886fcfccc35925fcf/README.md#L146-L146)
  - [observation/documented] Trust paths use decay scoring across hops (e.g., a documented example of 0.64 for two hops at 0.8 decay), and badges turn green 'Verified' at 3+ CODE_SIGNING vouches. -- evidence: [README.md#L371-L373](https://github.com/The-Nexus-Guard/aip/blob/3d8c873139ea6d4db421a57886fcfccc35925fcf/README.md#L371-L373), [README.md#L412-L416](https://github.com/The-Nexus-Guard/aip/blob/3d8c873139ea6d4db421a57886fcfccc35925fcf/README.md#L412-L416)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: the README points contributors to a Contributing Guide and GitHub Discussions for questions and ideas. -- evidence: [README.md#L682-L682](https://github.com/The-Nexus-Guard/aip/blob/3d8c873139ea6d4db421a57886fcfccc35925fcf/README.md#L682-L682), [README.md#L680-L680](https://github.com/The-Nexus-Guard/aip/blob/3d8c873139ea6d4db421a57886fcfccc35925fcf/README.md#L680-L680)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] A CLI named 'aip' exposes commands including init, register, verify, vouch, revoke, sign, message, messages, reply, rotate-key, trust-score, trust-graph, doctor, export, import, search, and cache. -- evidence: [README.md#L21-L24](https://github.com/The-Nexus-Guard/aip/blob/3d8c873139ea6d4db421a57886fcfccc35925fcf/README.md#L21-L24), [README.md#L441-L441](https://github.com/The-Nexus-Guard/aip/blob/3d8c873139ea6d4db421a57886fcfccc35925fcf/README.md#L441-L441), [README.md#L465-L495](https://github.com/The-Nexus-Guard/aip/blob/3d8c873139ea6d4db421a57886fcfccc35925fcf/README.md#L465-L495)
  - [observation/documented] Message signing uses the payload format sender_did|recipient_did|timestamp|encrypted_content; the older format without encrypted_content still works but is deprecated and slated for removal. -- evidence: [README.md#L338-L338](https://github.com/The-Nexus-Guard/aip/blob/3d8c873139ea6d4db421a57886fcfccc35925fcf/README.md#L338-L338), [README.md#L334-L336](https://github.com/The-Nexus-Guard/aip/blob/3d8c873139ea6d4db421a57886fcfccc35925fcf/README.md#L334-L336), [README.md#L332-L332](https://github.com/The-Nexus-Guard/aip/blob/3d8c873139ea6d4db421a57886fcfccc35925fcf/README.md#L332-L332)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
More evidence: [full detail](aip.detail.md)

Metadata and full claim list: [full detail](aip.detail.md)
Human notes ([notes](aip.notes.md), never overwritten by build)

[Back to map index](../../index.md)
