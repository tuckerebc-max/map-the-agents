# nexu-io/looper -- full detail

[Back to orientation](looper.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/nexu-io/looper/141510c0967f1b9888a07cbbe8ccadb07ff879f8/3ca8b4de5320199a.json](../../../wiki/dossiers/nexu-io/looper/141510c0967f1b9888a07cbbe8ccadb07ff879f8/3ca8b4de5320199a.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] looper daemon install places a managed daemon binary at ~/.looper/bin/looperd; daemon start writes a pid file and lifecycle diagnostics under ~/.looper, and the CLI looks up the daemon there before $PATH. -- evidence: [docs/configuration.md#L9-L13](https://github.com/nexu-io/looper/blob/141510c0967f1b9888a07cbbe8ccadb07ff879f8/docs/configuration.md#L9-L13), [docs/configuration.md#L15-L15](https://github.com/nexu-io/looper/blob/141510c0967f1b9888a07cbbe8ccadb07ff879f8/docs/configuration.md#L15-L15) (`clm_208db7d532595cb122787bfd6b96a785211c6eb94c9170911b515036b4889b2f`)
- [observation/documented] Webhook support has two delivery modes: gh-forward (default), where Looper runs gh webhook forward per repo and receives deliveries on the daemon route /webhook/forward, and tunnel, where Looper creates per-repo GitHub webhooks and the user supplies a tunnel to 127.0.0.1:<listenPort>. -- evidence: [docs/configuration.md#L47-L48](https://github.com/nexu-io/looper/blob/141510c0967f1b9888a07cbbe8ccadb07ff879f8/docs/configuration.md#L47-L48), [docs/configuration.md#L75-L80](https://github.com/nexu-io/looper/blob/141510c0967f1b9888a07cbbe8ccadb07ff879f8/docs/configuration.md#L75-L80), [docs/configuration.md#L45-L45](https://github.com/nexu-io/looper/blob/141510c0967f1b9888a07cbbe8ccadb07ff879f8/docs/configuration.md#L45-L45) (`clm_2aefc41857077948a65f55d692d4ebb99d8100cdcff298bf5ab8303319b50160`)

## design-choices (4 claim(s))

- [observation/documented] looperd loads configuration in layers: built-in defaults, config file, environment variables, then CLI flags; later layers override earlier ones, objects merge deeply, arrays are replaced as a whole, and omitted fields keep the previous layer's value. -- evidence: [docs/configuration.md#L84-L84](https://github.com/nexu-io/looper/blob/141510c0967f1b9888a07cbbe8ccadb07ff879f8/docs/configuration.md#L84-L84), [docs/configuration.md#L86-L89](https://github.com/nexu-io/looper/blob/141510c0967f1b9888a07cbbe8ccadb07ff879f8/docs/configuration.md#L86-L89), [docs/configuration.md#L91-L91](https://github.com/nexu-io/looper/blob/141510c0967f1b9888a07cbbe8ccadb07ff879f8/docs/configuration.md#L91-L91) (`clm_4a1e274932f1f34c6611ee3c7b3981617ec65ffb3b8b077282c7b4eda835c8a3`)
- [observation/documented] looperd watches the config file and atomically publishes a candidate only when every changed effective field is hot-safe per an explicit allowlist; invalid or restart-bound-containing candidates are rejected as a whole, leaving the last-known-good snapshot active with diagnostics at /dashboard/config. -- evidence: [docs/configuration.md#L97-L97](https://github.com/nexu-io/looper/blob/141510c0967f1b9888a07cbbe8ccadb07ff879f8/docs/configuration.md#L97-L97), [docs/configuration.md#L95-L95](https://github.com/nexu-io/looper/blob/141510c0967f1b9888a07cbbe8ccadb07ff879f8/docs/configuration.md#L95-L95) (`clm_a98d9ad9568075703fc5df839fbbc186c6033cf0ea83a896f5251f97ffadb501`)
- [observation/documented] [[projects]] entries are a declarative startup import: the daemon validates and transactionally imports them into SQLite and builds the runtime Project Catalog exclusively from active database records; config import never removes API-managed projects, and reusing an API-managed ID fails startup. -- evidence: [docs/configuration.md#L202-L206](https://github.com/nexu-io/looper/blob/141510c0967f1b9888a07cbbe8ccadb07ff879f8/docs/configuration.md#L202-L206), [docs/configuration.md#L200-L200](https://github.com/nexu-io/looper/blob/141510c0967f1b9888a07cbbe8ccadb07ff879f8/docs/configuration.md#L200-L200) (`clm_6b6c4a321b979c0cb0da0fbb70e84b2e5af98bb216ff8996428d1242fdd49fe9`)
- [observation/documented] Per coding role, agent identity overlays global agent.vendor/model, then the role's selected profile, then role-inline vendor/model, with inline winning per field; a role is runnable only when the overlay leaves a non-empty vendor. -- evidence: [docs/configuration.md#L262-L262](https://github.com/nexu-io/looper/blob/141510c0967f1b9888a07cbbe8ccadb07ff879f8/docs/configuration.md#L262-L262), [docs/configuration.md#L268-L268](https://github.com/nexu-io/looper/blob/141510c0967f1b9888a07cbbe8ccadb07ff879f8/docs/configuration.md#L268-L268), [docs/configuration.md#L264-L266](https://github.com/nexu-io/looper/blob/141510c0967f1b9888a07cbbe8ccadb07ff879f8/docs/configuration.md#L264-L266) (`clm_33510f04398d5d87c84278c34c84610ac97b305ae4ddb872591ac0bde9100669`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: a separate sandbox-e2e CI workflow runs on main and manual dispatch using a repository variable and secret for a GitHub App, mints an installation token via actions/create-github-app-token, and cleans up temporary issues, PRs, and branches afterward. -- evidence: [docs/configuration.md#L595-L602](https://github.com/nexu-io/looper/blob/141510c0967f1b9888a07cbbe8ccadb07ff879f8/docs/configuration.md#L595-L602), [docs/configuration.md#L574-L582](https://github.com/nexu-io/looper/blob/141510c0967f1b9888a07cbbe8ccadb07ff879f8/docs/configuration.md#L574-L582) (`clm_36f1b8280eb229a3852db6aae30e72fd77f6a1a97830b20f0fde2ad64bab7037`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The daemon exposes a dashboard config editor at /dashboard/config and a PATCH /api/v1/config endpoint; every patch must submit the revision of the file generation that produced the published values, and when token auth is unset the endpoint accepts only loopback peer/Host requests and rejects proxy-forwarding headers. -- evidence: [docs/configuration.md#L119-L119](https://github.com/nexu-io/looper/blob/141510c0967f1b9888a07cbbe8ccadb07ff879f8/docs/configuration.md#L119-L119), [docs/configuration.md#L121-L121](https://github.com/nexu-io/looper/blob/141510c0967f1b9888a07cbbe8ccadb07ff879f8/docs/configuration.md#L121-L121) (`clm_bf75fce2a2d98a741554c33acc4f95d5b3a9fec770b625e46b46505bceb24acf`)
- [observation/documented] Model suggestions are served via GET /api/v1/agent/models?vendor=..., combining a built-in per-vendor static list with an optional best-effort probe of the local vendor CLI; the catalog is advisory only, not an allowlist, and arbitrary model IDs remain valid. -- evidence: [docs/configuration.md#L284-L284](https://github.com/nexu-io/looper/blob/141510c0967f1b9888a07cbbe8ccadb07ff879f8/docs/configuration.md#L284-L284), [docs/configuration.md#L282-L282](https://github.com/nexu-io/looper/blob/141510c0967f1b9888a07cbbe8ccadb07ff879f8/docs/configuration.md#L282-L282) (`clm_e449e277691a622dc235dda0ce8d9a23c16ebb6e121905066a90dc264947b632`)
- [observation/documented] Agents read repository data through a host CLI exposed as LOOPER_HOST_CLI with subcommands such as host whoami, host api, host threads, and host git; these commands require the execution's private socket and cannot select another account or repository. -- evidence: [docs/configuration.md#L551-L556](https://github.com/nexu-io/looper/blob/141510c0967f1b9888a07cbbe8ccadb07ff879f8/docs/configuration.md#L551-L556), [docs/configuration.md#L542-L549](https://github.com/nexu-io/looper/blob/141510c0967f1b9888a07cbbe8ccadb07ff879f8/docs/configuration.md#L542-L549), [docs/configuration.md#L528-L540](https://github.com/nexu-io/looper/blob/141510c0967f1b9888a07cbbe8ccadb07ff879f8/docs/configuration.md#L528-L540) (`clm_292680c748d1670ac28aedd0052e62a9252e6e7b529916779274ea66cf7725fc`)

## memory-state (1 claim(s))

- [observation/documented] In-flight runs keep the immutable config snapshot and durable per-run agent snapshot they started with; resume/retry lineages copy the predecessor's agent_snapshot_json rather than re-resolving live config, and Looper never sends an old vendor's native session ID to a different CLI. -- evidence: [docs/configuration.md#L296-L298](https://github.com/nexu-io/looper/blob/141510c0967f1b9888a07cbbe8ccadb07ff879f8/docs/configuration.md#L296-L298), [docs/configuration.md#L113-L113](https://github.com/nexu-io/looper/blob/141510c0967f1b9888a07cbbe8ccadb07ff879f8/docs/configuration.md#L113-L113), [docs/configuration.md#L111-L111](https://github.com/nexu-io/looper/blob/141510c0967f1b9888a07cbbe8ccadb07ff879f8/docs/configuration.md#L111-L111) (`clm_327ad4891c627340c019af77f775f723eacfd176f6940e049e4f7fd82c39998f`)

## orchestration (2 claim(s))

- [observation/documented] Projects have two network modes: off (local-only, looper:target:* labels ignored) and routed, where multi-Node operation is coordinated through loopernet and exactly one looper:target:<node_name> label is the exact-Node authority. -- evidence: [docs/configuration.md#L21-L21](https://github.com/nexu-io/looper/blob/141510c0967f1b9888a07cbbe8ccadb07ff879f8/docs/configuration.md#L21-L21), [docs/configuration.md#L23-L24](https://github.com/nexu-io/looper/blob/141510c0967f1b9888a07cbbe8ccadb07ff879f8/docs/configuration.md#L23-L24), [docs/configuration.md#L28-L30](https://github.com/nexu-io/looper/blob/141510c0967f1b9888a07cbbe8ccadb07ff879f8/docs/configuration.md#L28-L30) (`clm_9eca3f56534053d98aeb81b6b10d9e4c6da2ded81c0f5d87ea8ccad425b9cdb8`)
- [observation/documented] In routed mode, loopernet centralizes webhook ingress and Node wakeups but must not mutate GitHub on its own; the Coordinator writes coarse GitHub authority first and the exact target label last, with polling retained as fallback and drift recovery. -- evidence: [docs/configuration.md#L34-L37](https://github.com/nexu-io/looper/blob/141510c0967f1b9888a07cbbe8ccadb07ff879f8/docs/configuration.md#L34-L37) (`clm_0d2754ddca67e98ab8cda0456f6e501d6e1d106083c97a0ab10ec10b4670a440`)

## tools-permissions (2 claim(s))

- [observation/documented] For fresh unattended Grok Build runs, Looper supplies --always-approve and --sandbox off by default; configured agent arguments override these, so operators may choose a stricter --sandbox, and non-plain output formats can break result-marker parsing. -- evidence: [docs/configuration.md#L369-L369](https://github.com/nexu-io/looper/blob/141510c0967f1b9888a07cbbe8ccadb07ff879f8/docs/configuration.md#L369-L369) (`clm_1e441d515b435f94340b7859f8a56ff8fbcb537bfc7ac9c8434bec7c56c4449c`)
- [observation/documented] Hosting tokens, private-key references, and personal GitHub/SSH authentication are stripped from agent environments after overrides merge; credential-bearing Git/GitHub CLI commands have a four-minute ceiling, and this is a credential/command-routing boundary rather than an OS sandbox. -- evidence: [docs/configuration.md#L558-L562](https://github.com/nexu-io/looper/blob/141510c0967f1b9888a07cbbe8ccadb07ff879f8/docs/configuration.md#L558-L562), [docs/configuration.md#L528-L540](https://github.com/nexu-io/looper/blob/141510c0967f1b9888a07cbbe8ccadb07ff879f8/docs/configuration.md#L528-L540) (`clm_743410e6ed68dd8f74cc248988a8f74bb66e6881ceb1d81a53341d4c7d6a78b1`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Looper is distributed as a GitHub Release Go binary and supports multiple agent vendor CLIs identified in config, including grok-build (invoked as grok), pi, and omp (Oh My Pi), alongside codex and claude-code shown in examples. -- evidence: [docs/configuration.md#L314-L316](https://github.com/nexu-io/looper/blob/141510c0967f1b9888a07cbbe8ccadb07ff879f8/docs/configuration.md#L314-L316), [docs/configuration.md#L390-L390](https://github.com/nexu-io/looper/blob/141510c0967f1b9888a07cbbe8ccadb07ff879f8/docs/configuration.md#L390-L390), [docs/configuration.md#L375-L375](https://github.com/nexu-io/looper/blob/141510c0967f1b9888a07cbbe8ccadb07ff879f8/docs/configuration.md#L375-L375), [docs/configuration.md#L9-L13](https://github.com/nexu-io/looper/blob/141510c0967f1b9888a07cbbe8ccadb07ff879f8/docs/configuration.md#L9-L13), [docs/configuration.md#L304-L307](https://github.com/nexu-io/looper/blob/141510c0967f1b9888a07cbbe8ccadb07ff879f8/docs/configuration.md#L304-L307), [docs/configuration.md#L360-L360](https://github.com/nexu-io/looper/blob/141510c0967f1b9888a07cbbe8ccadb07ff879f8/docs/configuration.md#L360-L360) (`clm_17067f6373093d983efed565d17754e67050c5091ab0cc4b6e16fca260ca3019`)

## limitations (2 claim(s))

- [observation/documented] Grok Build, Pi, and Oh My Pi support is fresh-run only: daemon native resume and interactive takeover via looper resume are unsupported, and retries use a fresh checkpoint prompt. -- evidence: [docs/configuration.md#L401-L401](https://github.com/nexu-io/looper/blob/141510c0967f1b9888a07cbbe8ccadb07ff879f8/docs/configuration.md#L401-L401), [docs/configuration.md#L386-L386](https://github.com/nexu-io/looper/blob/141510c0967f1b9888a07cbbe8ccadb07ff879f8/docs/configuration.md#L386-L386), [docs/configuration.md#L371-L371](https://github.com/nexu-io/looper/blob/141510c0967f1b9888a07cbbe8ccadb07ff879f8/docs/configuration.md#L371-L371) (`clm_2b03def758431262b11849f0b9fd44e81d202d45fd90289d0a7f511fdeac6c2a`)
- [observation/documented] The webhook forwarder lock uses OS file locking and is not designed for NFS-style shared filesystems; the documentation advises keeping the runtime directory on a local filesystem. -- evidence: [docs/configuration.md#L17-L17](https://github.com/nexu-io/looper/blob/141510c0967f1b9888a07cbbe8ccadb07ff879f8/docs/configuration.md#L17-L17) (`clm_1687f9c1480f50ea69278c56d1a9b58ef63133317f19e4d809b7e42904df59d1`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

