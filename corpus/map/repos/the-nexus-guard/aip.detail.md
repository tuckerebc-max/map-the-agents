# the-nexus-guard/aip -- full detail

[Back to orientation](aip.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/the-nexus-guard/aip/3d8c873139ea6d4db421a57886fcfccc35925fcf/e93b0149ff82da41.json](../../../wiki/dossiers/the-nexus-guard/aip/3d8c873139ea6d4db421a57886fcfccc35925fcf/e93b0149ff82da41.json)

## specifications (1 claim(s))

- [observation/documented] A draft 0xSKL integration spec (v0.1.0) defines an extended skill manifest with an AIP author block (DID, public key, Ed25519 signature over sha256 of name+version+content_hash+timestamp) and Cage execution policy based on author trust score. -- evidence: [docs/0xskl_integration_spec.md#L64-L84](https://github.com/The-Nexus-Guard/aip/blob/3d8c873139ea6d4db421a57886fcfccc35925fcf/docs/0xskl_integration_spec.md#L64-L84), [docs/0xskl_integration_spec.md#L3-L6](https://github.com/The-Nexus-Guard/aip/blob/3d8c873139ea6d4db421a57886fcfccc35925fcf/docs/0xskl_integration_spec.md#L3-L6), [docs/0xskl_integration_spec.md#L32-L58](https://github.com/The-Nexus-Guard/aip/blob/3d8c873139ea6d4db421a57886fcfccc35925fcf/docs/0xskl_integration_spec.md#L32-L58), [docs/0xskl_integration_spec.md#L88-L88](https://github.com/The-Nexus-Guard/aip/blob/3d8c873139ea6d4db421a57886fcfccc35925fcf/docs/0xskl_integration_spec.md#L88-L88) (`clm_17892d27beda224b80f43bdf6a71bbc91c2167a3cf214628b81dec3494027395`)

## components (2 claim(s))

- [observation/documented] AIP is organized into three layers: an identity layer (Ed25519 keypairs, DIDs, challenge-response), a trust layer (vouches, scopes, paths, revocation), and a communication layer (E2E encrypted messaging). -- evidence: [README.md#L70-L74](https://github.com/The-Nexus-Guard/aip/blob/3d8c873139ea6d4db421a57886fcfccc35925fcf/README.md#L70-L74), [README.md#L62-L62](https://github.com/The-Nexus-Guard/aip/blob/3d8c873139ea6d4db421a57886fcfccc35925fcf/README.md#L62-L62), [README.md#L76-L80](https://github.com/The-Nexus-Guard/aip/blob/3d8c873139ea6d4db421a57886fcfccc35925fcf/README.md#L76-L80), [README.md#L64-L68](https://github.com/The-Nexus-Guard/aip/blob/3d8c873139ea6d4db421a57886fcfccc35925fcf/README.md#L64-L68) (`clm_f8d132b6b3202243fe667dc83b212702ae75f1ac3c533ef13766dde48ff432aa`)
- [observation/documented] An identity middleware (AIPMiddleware) signs outgoing HTTP requests and verifies incoming ones, exposing trust-score-gated processing and peer discovery by minimum trust. -- evidence: [README.md#L201-L201](https://github.com/The-Nexus-Guard/aip/blob/3d8c873139ea6d4db421a57886fcfccc35925fcf/README.md#L201-L201), [README.md#L209-L210](https://github.com/The-Nexus-Guard/aip/blob/3d8c873139ea6d4db421a57886fcfccc35925fcf/README.md#L209-L210), [README.md#L204-L206](https://github.com/The-Nexus-Guard/aip/blob/3d8c873139ea6d4db421a57886fcfccc35925fcf/README.md#L204-L206), [README.md#L193-L193](https://github.com/The-Nexus-Guard/aip/blob/3d8c873139ea6d4db421a57886fcfccc35925fcf/README.md#L193-L193) (`clm_c8161a12388fd119441499c2afc79faee98109dfed98008c618fd30f334addbe`)

## design-choices (2 claim(s))

- [observation/documented] The protocol is designed to be decentralized with no central registry, local-first so each agent keeps its own trust view, and auditable via signed 'isnad' trust chains. -- evidence: [README.md#L84-L88](https://github.com/The-Nexus-Guard/aip/blob/3d8c873139ea6d4db421a57886fcfccc35925fcf/README.md#L84-L88), [README.md#L146-L146](https://github.com/The-Nexus-Guard/aip/blob/3d8c873139ea6d4db421a57886fcfccc35925fcf/README.md#L146-L146) (`clm_69941c125971d2e5c56fd8abb934dd0c71702f1049b279f9d40d4f9878707724`)
- [observation/documented] Trust paths use decay scoring across hops (e.g., a documented example of 0.64 for two hops at 0.8 decay), and badges turn green 'Verified' at 3+ CODE_SIGNING vouches. -- evidence: [README.md#L371-L373](https://github.com/The-Nexus-Guard/aip/blob/3d8c873139ea6d4db421a57886fcfccc35925fcf/README.md#L371-L373), [README.md#L412-L416](https://github.com/The-Nexus-Guard/aip/blob/3d8c873139ea6d4db421a57886fcfccc35925fcf/README.md#L412-L416) (`clm_c7792ef0f183a74aa8ce2b5b8d55e63032db8e712c5919c3d0b2576a4cff8e02`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: the README points contributors to a Contributing Guide and GitHub Discussions for questions and ideas. -- evidence: [README.md#L682-L682](https://github.com/The-Nexus-Guard/aip/blob/3d8c873139ea6d4db421a57886fcfccc35925fcf/README.md#L682-L682), [README.md#L680-L680](https://github.com/The-Nexus-Guard/aip/blob/3d8c873139ea6d4db421a57886fcfccc35925fcf/README.md#L680-L680) (`clm_f99fa7e0d037e1fad8f722297072e61ca507bcc86627f8b0c7b9f99720b34b4a`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] A CLI named 'aip' exposes commands including init, register, verify, vouch, revoke, sign, message, messages, reply, rotate-key, trust-score, trust-graph, doctor, export, import, search, and cache. -- evidence: [README.md#L21-L24](https://github.com/The-Nexus-Guard/aip/blob/3d8c873139ea6d4db421a57886fcfccc35925fcf/README.md#L21-L24), [README.md#L441-L441](https://github.com/The-Nexus-Guard/aip/blob/3d8c873139ea6d4db421a57886fcfccc35925fcf/README.md#L441-L441), [README.md#L465-L495](https://github.com/The-Nexus-Guard/aip/blob/3d8c873139ea6d4db421a57886fcfccc35925fcf/README.md#L465-L495) (`clm_612a45aec8782e67978dbf64daa8d4cb5e87536f369ad477b92e75110922e0ef`)
- [observation/documented] Message signing uses the payload format sender_did|recipient_did|timestamp|encrypted_content; the older format without encrypted_content still works but is deprecated and slated for removal. -- evidence: [README.md#L338-L338](https://github.com/The-Nexus-Guard/aip/blob/3d8c873139ea6d4db421a57886fcfccc35925fcf/README.md#L338-L338), [README.md#L334-L336](https://github.com/The-Nexus-Guard/aip/blob/3d8c873139ea6d4db421a57886fcfccc35925fcf/README.md#L334-L336), [README.md#L332-L332](https://github.com/The-Nexus-Guard/aip/blob/3d8c873139ea6d4db421a57886fcfccc35925fcf/README.md#L332-L332) (`clm_ba7db7ae40652595d077e6138ae6ac1a97d039c1984ae8a81d7d2ea32bb8af37`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] A pure-Python implementation exists with zero dependencies; optional performance dependencies include cryptography or pynacl, and langchain-core is an optional dependency for framework tools. -- evidence: [README.md#L606-L606](https://github.com/The-Nexus-Guard/aip/blob/3d8c873139ea6d4db421a57886fcfccc35925fcf/README.md#L606-L606), [README.md#L84-L88](https://github.com/The-Nexus-Guard/aip/blob/3d8c873139ea6d4db421a57886fcfccc35925fcf/README.md#L84-L88), [README.md#L380-L383](https://github.com/The-Nexus-Guard/aip/blob/3d8c873139ea6d4db421a57886fcfccc35925fcf/README.md#L380-L383) (`clm_65b86f13998ec396cca9bb073d7e369a1f2960beddc417ed6699eaca8820a199`)

## limitations (1 claim(s))

- [observation/documented] The status checklist marks trust gossip protocol and reputation scoring as unchecked, indicating these are not yet implemented in v0.5.46. -- evidence: [README.md#L422-L422](https://github.com/The-Nexus-Guard/aip/blob/3d8c873139ea6d4db421a57886fcfccc35925fcf/README.md#L422-L422), [README.md#L424-L437](https://github.com/The-Nexus-Guard/aip/blob/3d8c873139ea6d4db421a57886fcfccc35925fcf/README.md#L424-L437) (`clm_d0a97f31febeb14bd0df7911e4774f70f7c7b41fe550626bd9992f08889f46d2`)

## relevance (1 claim(s))

- [observation/documented] AIP targets agent-to-agent security gaps: verifying who an agent is, deciding trustworthiness via vouch chains, signing skills for code provenance, and private messaging, including MCP and A2A protocol integrations. -- evidence: [README.md#L610-L610](https://github.com/The-Nexus-Guard/aip/blob/3d8c873139ea6d4db421a57886fcfccc35925fcf/README.md#L610-L610), [README.md#L9-L9](https://github.com/The-Nexus-Guard/aip/blob/3d8c873139ea6d4db421a57886fcfccc35925fcf/README.md#L9-L9), [README.md#L241-L241](https://github.com/The-Nexus-Guard/aip/blob/3d8c873139ea6d4db421a57886fcfccc35925fcf/README.md#L241-L241), [README.md#L11-L11](https://github.com/The-Nexus-Guard/aip/blob/3d8c873139ea6d4db421a57886fcfccc35925fcf/README.md#L11-L11), [README.md#L52-L58](https://github.com/The-Nexus-Guard/aip/blob/3d8c873139ea6d4db421a57886fcfccc35925fcf/README.md#L52-L58) (`clm_3715f251fceb5812b75246e44ef07b0f02bfd974d74f356d5ccfb1d01d6fbb00`)

