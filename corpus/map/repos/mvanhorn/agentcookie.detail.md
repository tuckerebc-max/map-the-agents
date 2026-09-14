# mvanhorn/agentcookie -- full detail

[Back to orientation](agentcookie.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/mvanhorn/agentcookie/57b53dfd916233777941de91c02a0312e9751603/14f23d6052e3cd81.json](../../../wiki/dossiers/mvanhorn/agentcookie/57b53dfd916233777941de91c02a0312e9751603/14f23d6052e3cd81.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The architecture doc lays out Go packages including cmd/agentcookie (cobra CLI), internal/cli, internal/chrome, internal/transport, internal/config, internal/pairing, internal/keystore, internal/protocol, and internal/cdp. -- evidence: [docs/architecture.md#L62-L72](https://github.com/mvanhorn/agentcookie/blob/57b53dfd916233777941de91c02a0312e9751603/docs/architecture.md#L62-L72) (`clm_217080b97abe02d053cebc2bc97c0b61f0e170fc479bf358fb0fbb352db7e033`)

## design-choices (5 claim(s))

- [observation/documented] On Linux the sink injects cookies directly into Chrome's in-memory store via the Chrome DevTools Protocol (Storage.setCookies) instead of rewriting Chrome's SQLite, and Chrome must be started with a remote-debugging port such as 9223. -- evidence: [docs/architecture.md#L51-L52](https://github.com/mvanhorn/agentcookie/blob/57b53dfd916233777941de91c02a0312e9751603/docs/architecture.md#L51-L52), [README.md#L59-L60](https://github.com/mvanhorn/agentcookie/blob/57b53dfd916233777941de91c02a0312e9751603/README.md#L59-L60), [README.md#L40-L57](https://github.com/mvanhorn/agentcookie/blob/57b53dfd916233777941de91c02a0312e9751603/README.md#L40-L57), [README.md#L62-L62](https://github.com/mvanhorn/agentcookie/blob/57b53dfd916233777941de91c02a0312e9751603/README.md#L62-L62) (`clm_883b948f84a528007a60465948774ffebb85547487ba73c9af168c262550a91f`)
- [observation/documented] Cookies are sealed with AES-GCM using per-peer keys derived from an X25519 + HKDF pairing handshake in which the pairing code is mixed into the HKDF salt; key files are stored mode 0600. -- evidence: [docs/architecture.md#L108-L116](https://github.com/mvanhorn/agentcookie/blob/57b53dfd916233777941de91c02a0312e9751603/docs/architecture.md#L108-L116), [docs/architecture.md#L100-L104](https://github.com/mvanhorn/agentcookie/blob/57b53dfd916233777941de91c02a0312e9751603/docs/architecture.md#L100-L104), [docs/architecture.md#L62-L72](https://github.com/mvanhorn/agentcookie/blob/57b53dfd916233777941de91c02a0312e9751603/docs/architecture.md#L62-L72), [README.md#L32-L32](https://github.com/mvanhorn/agentcookie/blob/57b53dfd916233777941de91c02a0312e9751603/README.md#L32-L32) (`clm_91834bd6d42db94bc7be4e4c04a3ffd9aa54c988570999df7e25a41d21e6b36b`)
- [observation/documented] The sync protocol carries a versioned SyncEnvelope with a monotonic Sequence; the sink rejects wrong keys with 401, version mismatches with 400, and replays via an in-memory SequenceTracker with 409. -- evidence: [docs/architecture.md#L89-L96](https://github.com/mvanhorn/agentcookie/blob/57b53dfd916233777941de91c02a0312e9751603/docs/architecture.md#L89-L96), [docs/architecture.md#L108-L116](https://github.com/mvanhorn/agentcookie/blob/57b53dfd916233777941de91c02a0312e9751603/docs/architecture.md#L108-L116), [docs/architecture.md#L76-L85](https://github.com/mvanhorn/agentcookie/blob/57b53dfd916233777941de91c02a0312e9751603/docs/architecture.md#L76-L85) (`clm_856e0652a55416bf71836e48d841e20d891b59ab0ea81d7d9fa4afa804896462`)
- [observation/documented] On Linux, a missing blocklist.yaml or omitted policy field means the sink ships nothing (allowlist-empty) as a security default; sync-all requires an explicit blocklist policy with an empty domains list, described as an operator choice rather than the code default. -- evidence: [README.md#L246-L246](https://github.com/mvanhorn/agentcookie/blob/57b53dfd916233777941de91c02a0312e9751603/README.md#L246-L246), [README.md#L236-L236](https://github.com/mvanhorn/agentcookie/blob/57b53dfd916233777941de91c02a0312e9751603/README.md#L236-L236), [docs/architecture.md#L54-L58](https://github.com/mvanhorn/agentcookie/blob/57b53dfd916233777941de91c02a0312e9751603/docs/architecture.md#L54-L58), [docs/consumption.md#L165-L166](https://github.com/mvanhorn/agentcookie/blob/57b53dfd916233777941de91c02a0312e9751603/docs/consumption.md#L165-L166) (`clm_bdbef00468a7bee0142a460ce108d9509a632462ac71580b6fcee6f34f3ba592`)
- [observation/documented] One source can fan out to multiple sinks, reading and filtering cookies once then sealing and POSTing to each sink with that sink's own paired key; an unreachable sink fails in isolation, and every sink receives the full cookie and secret set. -- evidence: [README.md#L301-L301](https://github.com/mvanhorn/agentcookie/blob/57b53dfd916233777941de91c02a0312e9751603/README.md#L301-L301), [README.md#L277-L277](https://github.com/mvanhorn/agentcookie/blob/57b53dfd916233777941de91c02a0312e9751603/README.md#L277-L277) (`clm_a4ebb241bef483db16875c3200ded1bc1161a8e5fda6c40278524e8292397151`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: the README's working-today list cites 520+ unit tests across 26 packages, a repository test-suite figure rather than any agent-performance evaluation. -- evidence: [README.md#L317-L324](https://github.com/mvanhorn/agentcookie/blob/57b53dfd916233777941de91c02a0312e9751603/README.md#L317-L324) (`clm_8d6fc2d31418ac32fc0e08e547f64d2584594935ea06f01db111b7b5f0cddc09`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The product requires Tailscale and Chrome on both machines, and the Linux sink must bind a Tailscale 100.x address, refusing to start without the tailnet. -- evidence: [README.md#L104-L106](https://github.com/mvanhorn/agentcookie/blob/57b53dfd916233777941de91c02a0312e9751603/README.md#L104-L106), [docs/architecture.md#L51-L52](https://github.com/mvanhorn/agentcookie/blob/57b53dfd916233777941de91c02a0312e9751603/docs/architecture.md#L51-L52), [docs/consumption.md#L109-L110](https://github.com/mvanhorn/agentcookie/blob/57b53dfd916233777941de91c02a0312e9751603/docs/consumption.md#L109-L110) (`clm_64e50074d85103060014dfd2e404f3e16bc8ddc9960953cf5e4abbb269b2dbcc`)

## limitations (3 claim(s))

- [observation/documented] Chrome's DBSC binds Google/Workspace sessions to device keys, so copied cookies for such sites stop working within minutes; the documented workaround is signing the sink's Chrome into the same Google account locally. -- evidence: [README.md#L328-L335](https://github.com/mvanhorn/agentcookie/blob/57b53dfd916233777941de91c02a0312e9751603/README.md#L328-L335), [README.md#L309-L309](https://github.com/mvanhorn/agentcookie/blob/57b53dfd916233777941de91c02a0312e9751603/README.md#L309-L309), [README.md#L5-L5](https://github.com/mvanhorn/agentcookie/blob/57b53dfd916233777941de91c02a0312e9751603/README.md#L5-L5), [README.md#L305-L305](https://github.com/mvanhorn/agentcookie/blob/57b53dfd916233777941de91c02a0312e9751603/README.md#L305-L305) (`clm_6e5b51b9f28b3198359239f7bf0607ffac6d2ad00667c36b734e911c0270ef58`)
- [observation/documented] Documented limits include a plaintext-at-rest sidecar at ~/.agentcookie/cookies-plain.db, a loopback-only CDP port that same-user processes can read, no live key rotation (wizard re-run required), and unread Linux extra-profile Chrome SQLite. -- evidence: [README.md#L328-L335](https://github.com/mvanhorn/agentcookie/blob/57b53dfd916233777941de91c02a0312e9751603/README.md#L328-L335) (`clm_7256e87791e180d626c0c934abb3abb1ec3b4dc5357f284109e1efaad611ee31`)
- [observation/documented] A recorded 2026-05-19 dry run of the closed-beta installer on a clean Mac mini concluded it was not ready for the first invite, citing blockers including broken tarball extraction, missing --code/--pair-url passthrough, and a key-file hostname mismatch that silently broke syncing. -- evidence: [docs/dry-run-2026-05-19.md#L26-L26](https://github.com/mvanhorn/agentcookie/blob/57b53dfd916233777941de91c02a0312e9751603/docs/dry-run-2026-05-19.md#L26-L26), [docs/dry-run-2026-05-19.md#L32-L32](https://github.com/mvanhorn/agentcookie/blob/57b53dfd916233777941de91c02a0312e9751603/docs/dry-run-2026-05-19.md#L32-L32), [docs/dry-run-2026-05-19.md#L20-L20](https://github.com/mvanhorn/agentcookie/blob/57b53dfd916233777941de91c02a0312e9751603/docs/dry-run-2026-05-19.md#L20-L20), [docs/dry-run-2026-05-19.md#L28-L28](https://github.com/mvanhorn/agentcookie/blob/57b53dfd916233777941de91c02a0312e9751603/docs/dry-run-2026-05-19.md#L28-L28) (`clm_3bdfe49a653f7efc4f6a54cba39d3e4fecc418e0f7d60b0923ac74172adbea4a`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

