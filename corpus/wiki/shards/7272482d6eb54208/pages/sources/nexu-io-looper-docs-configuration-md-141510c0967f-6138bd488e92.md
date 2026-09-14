---
access: public
aliases: []
claim_ids:
- clm_0d2754ddca67e98ab8cda0456f6e501d6e1d106083c97a0ab10ec10b4670a440
- clm_1687f9c1480f50ea69278c56d1a9b58ef63133317f19e4d809b7e42904df59d1
- clm_17067f6373093d983efed565d17754e67050c5091ab0cc4b6e16fca260ca3019
- clm_1e441d515b435f94340b7859f8a56ff8fbcb537bfc7ac9c8434bec7c56c4449c
- clm_208db7d532595cb122787bfd6b96a785211c6eb94c9170911b515036b4889b2f
- clm_292680c748d1670ac28aedd0052e62a9252e6e7b529916779274ea66cf7725fc
- clm_2aefc41857077948a65f55d692d4ebb99d8100cdcff298bf5ab8303319b50160
- clm_2b03def758431262b11849f0b9fd44e81d202d45fd90289d0a7f511fdeac6c2a
- clm_327ad4891c627340c019af77f775f723eacfd176f6940e049e4f7fd82c39998f
- clm_33510f04398d5d87c84278c34c84610ac97b305ae4ddb872591ac0bde9100669
- clm_36f1b8280eb229a3852db6aae30e72fd77f6a1a97830b20f0fde2ad64bab7037
- clm_4a1e274932f1f34c6611ee3c7b3981617ec65ffb3b8b077282c7b4eda835c8a3
- clm_6b6c4a321b979c0cb0da0fbb70e84b2e5af98bb216ff8996428d1242fdd49fe9
- clm_743410e6ed68dd8f74cc248988a8f74bb66e6881ceb1d81a53341d4c7d6a78b1
- clm_9eca3f56534053d98aeb81b6b10d9e4c6da2ded81c0f5d87ea8ccad425b9cdb8
- clm_a98d9ad9568075703fc5df839fbbc186c6033cf0ea83a896f5251f97ffadb501
- clm_bf75fce2a2d98a741554c33acc4f95d5b3a9fec770b625e46b46505bceb24acf
- clm_e449e277691a622dc235dda0ce8d9a23c16ebb6e121905066a90dc264947b632
maturity: draft
page_id: pg_b609df8fb3875972a6f26138bd488e92
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_f4c2257a910c5ff99710c169e15bbb10
title: nexu-io/looper/docs/configuration.md @ 141510c0967f
updated_at: '2026-09-14T02:21:52Z'
---

# nexu-io/looper/docs/configuration.md @ 141510c0967f

<!-- rcw:begin owner=source:src_f4c2257a910c5ff99710c169e15bbb10 block=evidence -->
- In routed mode, loopernet centralizes webhook ingress and Node wakeups but must not mutate GitHub on its own; the Coordinator writes coarse GitHub authority first and the exact target label last, with polling retained as fallback and drift recovery. [@claim:clm_0d2754ddca67e98ab8cda0456f6e501d6e1d106083c97a0ab10ec10b4670a440]
- The webhook forwarder lock uses OS file locking and is not designed for NFS-style shared filesystems; the documentation advises keeping the runtime directory on a local filesystem. [@claim:clm_1687f9c1480f50ea69278c56d1a9b58ef63133317f19e4d809b7e42904df59d1]
- Looper is distributed as a GitHub Release Go binary and supports multiple agent vendor CLIs identified in config, including grok-build (invoked as grok), pi, and omp (Oh My Pi), alongside codex and claude-code shown in examples. [@claim:clm_17067f6373093d983efed565d17754e67050c5091ab0cc4b6e16fca260ca3019]
- For fresh unattended Grok Build runs, Looper supplies --always-approve and --sandbox off by default; configured agent arguments override these, so operators may choose a stricter --sandbox, and non-plain output formats can break result-marker parsing. [@claim:clm_1e441d515b435f94340b7859f8a56ff8fbcb537bfc7ac9c8434bec7c56c4449c]
- looper daemon install places a managed daemon binary at ~/.looper/bin/looperd; daemon start writes a pid file and lifecycle diagnostics under ~/.looper, and the CLI looks up the daemon there before $PATH. [@claim:clm_208db7d532595cb122787bfd6b96a785211c6eb94c9170911b515036b4889b2f]
- Agents read repository data through a host CLI exposed as LOOPER_HOST_CLI with subcommands such as host whoami, host api, host threads, and host git; these commands require the execution's private socket and cannot select another account or repository. [@claim:clm_292680c748d1670ac28aedd0052e62a9252e6e7b529916779274ea66cf7725fc]
- Webhook support has two delivery modes: gh-forward (default), where Looper runs gh webhook forward per repo and receives deliveries on the daemon route /webhook/forward, and tunnel, where Looper creates per-repo GitHub webhooks and the user supplies a tunnel to 127.0.0.1:<listenPort>. [@claim:clm_2aefc41857077948a65f55d692d4ebb99d8100cdcff298bf5ab8303319b50160]
- Grok Build, Pi, and Oh My Pi support is fresh-run only: daemon native resume and interactive takeover via looper resume are unsupported, and retries use a fresh checkpoint prompt. [@claim:clm_2b03def758431262b11849f0b9fd44e81d202d45fd90289d0a7f511fdeac6c2a]
- In-flight runs keep the immutable config snapshot and durable per-run agent snapshot they started with; resume/retry lineages copy the predecessor's agent_snapshot_json rather than re-resolving live config, and Looper never sends an old vendor's native session ID to a different CLI. [@claim:clm_327ad4891c627340c019af77f775f723eacfd176f6940e049e4f7fd82c39998f]
- Per coding role, agent identity overlays global agent.vendor/model, then the role's selected profile, then role-inline vendor/model, with inline winning per field; a role is runnable only when the overlay leaves a non-empty vendor. [@claim:clm_33510f04398d5d87c84278c34c84610ac97b305ae4ddb872591ac0bde9100669]
- Repository development practice: a separate sandbox-e2e CI workflow runs on main and manual dispatch using a repository variable and secret for a GitHub App, mints an installation token via actions/create-github-app-token, and cleans up temporary issues, PRs, and branches afterward. [@claim:clm_36f1b8280eb229a3852db6aae30e72fd77f6a1a97830b20f0fde2ad64bab7037]
- looperd loads configuration in layers: built-in defaults, config file, environment variables, then CLI flags; later layers override earlier ones, objects merge deeply, arrays are replaced as a whole, and omitted fields keep the previous layer's value. [@claim:clm_4a1e274932f1f34c6611ee3c7b3981617ec65ffb3b8b077282c7b4eda835c8a3]
- [[projects]] entries are a declarative startup import: the daemon validates and transactionally imports them into SQLite and builds the runtime Project Catalog exclusively from active database records; config import never removes API-managed projects, and reusing an API-managed ID fails startup. [@claim:clm_6b6c4a321b979c0cb0da0fbb70e84b2e5af98bb216ff8996428d1242fdd49fe9]
- Hosting tokens, private-key references, and personal GitHub/SSH authentication are stripped from agent environments after overrides merge; credential-bearing Git/GitHub CLI commands have a four-minute ceiling, and this is a credential/command-routing boundary rather than an OS sandbox. [@claim:clm_743410e6ed68dd8f74cc248988a8f74bb66e6881ceb1d81a53341d4c7d6a78b1]
- Projects have two network modes: off (local-only, looper:target:* labels ignored) and routed, where multi-Node operation is coordinated through loopernet and exactly one looper:target:<node_name> label is the exact-Node authority. [@claim:clm_9eca3f56534053d98aeb81b6b10d9e4c6da2ded81c0f5d87ea8ccad425b9cdb8]
- looperd watches the config file and atomically publishes a candidate only when every changed effective field is hot-safe per an explicit allowlist; invalid or restart-bound-containing candidates are rejected as a whole, leaving the last-known-good snapshot active with diagnostics at /dashboard/config. [@claim:clm_a98d9ad9568075703fc5df839fbbc186c6033cf0ea83a896f5251f97ffadb501]
- The daemon exposes a dashboard config editor at /dashboard/config and a PATCH /api/v1/config endpoint; every patch must submit the revision of the file generation that produced the published values, and when token auth is unset the endpoint accepts only loopback peer/Host requests and rejects proxy-forwarding headers. [@claim:clm_bf75fce2a2d98a741554c33acc4f95d5b3a9fec770b625e46b46505bceb24acf]
- Model suggestions are served via GET /api/v1/agent/models?vendor=..., combining a built-in per-vendor static list with an optional best-effort probe of the local vendor CLI; the catalog is advisory only, not an allowlist, and arbitrary model IDs remain valid. [@claim:clm_e449e277691a622dc235dda0ce8d9a23c16ebb6e121905066a90dc264947b632]
<!-- rcw:end owner=source:src_f4c2257a910c5ff99710c169e15bbb10 block=evidence -->

## Researcher notes

