# mvanhorn/agentcookie

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 57b53dfd9162 @ 14f23d6052e3cd81

## Summary (orientation draft, not independently verified)

Selected evidence records: On Linux the sink injects cookies directly into Chrome's in-memory store via the Chrome DevTools Protocol (Storage.setCookies) instead of rewriting Chrome's SQLite, and Chrome must be started with a remote-debugging port such as 9223. Cookies are sealed with AES-GCM using per-peer keys derived from an X25519 + HKDF pairing handshake in which the pairing code is mixed into the HKDF salt; key files are stored mode 0600.

## Source coverage

Source coverage (partial): 6 of 45 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 5 facet(s); 8 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The architecture doc lays out Go packages including cmd/agentcookie (cobra CLI), internal/cli, internal/chrome, internal/transport, internal/config, internal/pairing, internal/keystore, internal/protocol, and internal/cdp. -- evidence: [docs/architecture.md#L62-L72](https://github.com/mvanhorn/agentcookie/blob/57b53dfd916233777941de91c02a0312e9751603/docs/architecture.md#L62-L72)
- design-choices (5 claim(s)):
  - [observation/documented] On Linux the sink injects cookies directly into Chrome's in-memory store via the Chrome DevTools Protocol (Storage.setCookies) instead of rewriting Chrome's SQLite, and Chrome must be started with a remote-debugging port such as 9223. -- evidence: [docs/architecture.md#L51-L52](https://github.com/mvanhorn/agentcookie/blob/57b53dfd916233777941de91c02a0312e9751603/docs/architecture.md#L51-L52), [README.md#L59-L60](https://github.com/mvanhorn/agentcookie/blob/57b53dfd916233777941de91c02a0312e9751603/README.md#L59-L60), [README.md#L40-L57](https://github.com/mvanhorn/agentcookie/blob/57b53dfd916233777941de91c02a0312e9751603/README.md#L40-L57), [README.md#L62-L62](https://github.com/mvanhorn/agentcookie/blob/57b53dfd916233777941de91c02a0312e9751603/README.md#L62-L62)
  - [observation/documented] Cookies are sealed with AES-GCM using per-peer keys derived from an X25519 + HKDF pairing handshake in which the pairing code is mixed into the HKDF salt; key files are stored mode 0600. -- evidence: [docs/architecture.md#L108-L116](https://github.com/mvanhorn/agentcookie/blob/57b53dfd916233777941de91c02a0312e9751603/docs/architecture.md#L108-L116), [docs/architecture.md#L100-L104](https://github.com/mvanhorn/agentcookie/blob/57b53dfd916233777941de91c02a0312e9751603/docs/architecture.md#L100-L104), [docs/architecture.md#L62-L72](https://github.com/mvanhorn/agentcookie/blob/57b53dfd916233777941de91c02a0312e9751603/docs/architecture.md#L62-L72), [README.md#L32-L32](https://github.com/mvanhorn/agentcookie/blob/57b53dfd916233777941de91c02a0312e9751603/README.md#L32-L32)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: the README's working-today list cites 520+ unit tests across 26 packages, a repository test-suite figure rather than any agent-performance evaluation. -- evidence: [README.md#L317-L324](https://github.com/mvanhorn/agentcookie/blob/57b53dfd916233777941de91c02a0312e9751603/README.md#L317-L324)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces: unknown (no source-linked claim submitted for this facet)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] The product requires Tailscale and Chrome on both machines, and the Linux sink must bind a Tailscale 100.x address, refusing to start without the tailnet. -- evidence: [README.md#L104-L106](https://github.com/mvanhorn/agentcookie/blob/57b53dfd916233777941de91c02a0312e9751603/README.md#L104-L106), [docs/architecture.md#L51-L52](https://github.com/mvanhorn/agentcookie/blob/57b53dfd916233777941de91c02a0312e9751603/docs/architecture.md#L51-L52), [docs/consumption.md#L109-L110](https://github.com/mvanhorn/agentcookie/blob/57b53dfd916233777941de91c02a0312e9751603/docs/consumption.md#L109-L110)
- limitations (3 claim(s)):
  - [observation/documented] Chrome's DBSC binds Google/Workspace sessions to device keys, so copied cookies for such sites stop working within minutes; the documented workaround is signing the sink's Chrome into the same Google account locally. -- evidence: [README.md#L328-L335](https://github.com/mvanhorn/agentcookie/blob/57b53dfd916233777941de91c02a0312e9751603/README.md#L328-L335), [README.md#L309-L309](https://github.com/mvanhorn/agentcookie/blob/57b53dfd916233777941de91c02a0312e9751603/README.md#L309-L309), [README.md#L5-L5](https://github.com/mvanhorn/agentcookie/blob/57b53dfd916233777941de91c02a0312e9751603/README.md#L5-L5), [README.md#L305-L305](https://github.com/mvanhorn/agentcookie/blob/57b53dfd916233777941de91c02a0312e9751603/README.md#L305-L305)
  - [observation/documented] Documented limits include a plaintext-at-rest sidecar at ~/.agentcookie/cookies-plain.db, a loopback-only CDP port that same-user processes can read, no live key rotation (wizard re-run required), and unread Linux extra-profile Chrome SQLite. -- evidence: [README.md#L328-L335](https://github.com/mvanhorn/agentcookie/blob/57b53dfd916233777941de91c02a0312e9751603/README.md#L328-L335)
More evidence: [full detail](agentcookie.detail.md)

Metadata and full claim list: [full detail](agentcookie.detail.md)
Human notes ([notes](agentcookie.notes.md), never overwritten by build)

[Back to map index](../../index.md)
