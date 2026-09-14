# jigjoy-ai/baro -- full detail

[Back to orientation](baro.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/jigjoy-ai/baro/f9a610774532fdde578b656dd838766e1173c4fc/a7f091ec4bf6f132.json](../../../wiki/dossiers/jigjoy-ai/baro/f9a610774532fdde578b656dd838766e1173c4fc/a7f091ec4bf6f132.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (1 claim(s))

- [observation/documented] The architecture is described as a Rust TUI host plus a TypeScript orchestrator whose bounded contexts communicate over the Mozaik event bus, with machine gates in front of every merge. -- evidence: [README.md#L80-L80](https://github.com/jigjoy-ai/baro/blob/f9a610774532fdde578b656dd838766e1173c4fc/README.md#L80-L80) (`clm_ac7cfaff3f1e8029288f36cb28451ce63f696ff44703e632c0749bbe48f91958`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: the experiment guide instructs preparing a clean git repo with an unexecuted prd.json whose stories have concrete acceptance criteria and test commands, and installing workspace dependencies with npm install before running trials. -- evidence: [docs/collective-experiment.md#L143-L143](https://github.com/jigjoy-ai/baro/blob/f9a610774532fdde578b656dd838766e1173c4fc/docs/collective-experiment.md#L143-L143), [docs/collective-experiment.md#L179-L182](https://github.com/jigjoy-ai/baro/blob/f9a610774532fdde578b656dd838766e1173c4fc/docs/collective-experiment.md#L179-L182) (`clm_0e5d29b6dedc005b653821275afa67ebd02afd880a6eb405e5eb7a196615fc8c`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The product is installed globally via npm as baro-ai and is invoked as `baro "<goal>"` inside a repository, opening a TUI where intake asks questions, the user confirms the plan, and the run proceeds. -- evidence: [README.md#L27-L30](https://github.com/jigjoy-ai/baro/blob/f9a610774532fdde578b656dd838766e1173c4fc/README.md#L27-L30), [README.md#L32-L32](https://github.com/jigjoy-ai/baro/blob/f9a610774532fdde578b656dd838766e1173c4fc/README.md#L32-L32), [README.md#L18-L20](https://github.com/jigjoy-ai/baro/blob/f9a610774532fdde578b656dd838766e1173c4fc/README.md#L18-L20) (`clm_e6110d9ddb9d49432414558bbe8d4a4dc45ee554c44e9406e2bd440c0298a359`)
- [observation/documented] CLI commands include headless detached runs printing a run id, `watch` and `logs` for following runs, `runs`/`stop` for listing and stopping, `--resume` (never re-plans), `--continue` (always re-plans), `--doctor`, `login`, and `connect`. -- evidence: [README.md#L46-L58](https://github.com/jigjoy-ai/baro/blob/f9a610774532fdde578b656dd838766e1173c4fc/README.md#L46-L58), [README.md#L36-L42](https://github.com/jigjoy-ai/baro/blob/f9a610774532fdde578b656dd838766e1173c4fc/README.md#L36-L42) (`clm_a3e7704c988709fe7a6c2df6530d7718a051a5dbe007aee06cf28061a80d8ca2`)
- [observation/documented] Flags include backend selection (--llm claude|codex|openai|opencode|pi|hybrid|jigjoy), model override, effort level, parallel agent count, execution mode, --quick, --local-only, per-command shell budget, custom OpenAI base URL, and per-tier backend mapping. -- evidence: [README.md#L62-L73](https://github.com/jigjoy-ai/baro/blob/f9a610774532fdde578b656dd838766e1173c4fc/README.md#L62-L73) (`clm_92d2d411d0709701e7fd56b0da87655c88254493c97f754d78e2ff67f56fa2c1`)

## memory-state (1 claim(s))

- [observation/documented] Proposal IDs act as idempotency keys: exact re-delivery returns the remembered decision without reapplying, reuse with different content is rejected, and applied decisions can be restored from the PRD's runtimeGraph metadata when a host resumes the same runId. -- evidence: [docs/collective-experiment.md#L75-L87](https://github.com/jigjoy-ai/baro/blob/f9a610774532fdde578b656dd838766e1173c4fc/docs/collective-experiment.md#L75-L87) (`clm_baf49f898612c0d1607a2c499df6a0570704e54eef91703f124b0acef7b75aee`)

## orchestration (4 claim(s))

- [observation/documented] Goals are compiled by an architect into machine-checkable invariants before coding, split into a DAG of stories built in parallel across isolated git worktrees, with runtime replanning able to add and rewire stories mid-run and failed gates spawning remediation stories. -- evidence: [README.md#L8-L11](https://github.com/jigjoy-ai/baro/blob/f9a610774532fdde578b656dd838766e1173c4fc/README.md#L8-L11), [README.md#L82-L91](https://github.com/jigjoy-ai/baro/blob/f9a610774532fdde578b656dd838766e1173c4fc/README.md#L82-L91) (`clm_cf08c9b4122ad876d30561aec0b4db4e355bcdc6c8d41d32d4170ff510a8fd1e`)
- [observation/documented] Collective coordination is the CLI default; a legacy Conductor mode (one owner of DAG levels, retries, completion) can be selected with `--coordination legacy` for A/B comparison. -- evidence: [docs/collective-experiment.md#L7-L7](https://github.com/jigjoy-ai/baro/blob/f9a610774532fdde578b656dd838766e1173c4fc/docs/collective-experiment.md#L7-L7), [docs/collective-experiment.md#L5-L5](https://github.com/jigjoy-ai/baro/blob/f9a610774532fdde578b656dd838766e1173c4fc/docs/collective-experiment.md#L5-L5) (`clm_51bb064a0be450abf3833e9edcf1095eeac19fcfd26d96861f34fe203ab43cfe`)
- [observation/documented] In collective mode, workers publish credential-free capabilities and bids, a broker grants a correlated lease to a deterministic winner, and with the Critic enabled a story passes only after the acceptance verdict plus StoryMerged, not merely when the model process exits. -- evidence: [docs/collective-experiment.md#L7-L7](https://github.com/jigjoy-ai/baro/blob/f9a610774532fdde578b656dd838766e1173c4fc/docs/collective-experiment.md#L7-L7) (`clm_ae96de8fd332dcf0913d4e9163301ad6f790682478413c91bb7fb89f6c980274`)
- [observation/documented] The runtime is distributed but not leaderless: the Board serializes scheduling and durable graph commits while separate participants own goal meaning, route selection, lease granting, quality evaluation, merging, and verification. -- evidence: [docs/collective-runtime.md#L151-L156](https://github.com/jigjoy-ai/baro/blob/f9a610774532fdde578b656dd838766e1173c4fc/docs/collective-runtime.md#L151-L156) (`clm_630a3eb1b0633aa3bc1604d67ebf3a855db38c1a79fa35bfc09e1a9b75b7e73c`)

## tools-permissions (2 claim(s))

- [observation/documented] Runtime replan proposals carry run/story/lease/generation and a graphVersion; invalid, stale, cyclic, unauthorized, over-budget or non-durable candidates get a correlated rejection and are never shown as applied just because a model requested them. -- evidence: [docs/collective-experiment.md#L29-L37](https://github.com/jigjoy-ai/baro/blob/f9a610774532fdde578b656dd838766e1173c4fc/docs/collective-experiment.md#L29-L37) (`clm_6e0cee3d0ef9fb48d2a64af69932471fa3a2d75b324d2a606248af898c4b840f`)
- [observation/documented] The DialogueAgent is text-only with no codebase tools; it may send a bounded targeted message and one add-only delegation proposal of at most two stories, with no authority over removal, rewiring, priority, retries, model, route, lease, or merging. -- evidence: [docs/collective-experiment.md#L206-L216](https://github.com/jigjoy-ai/baro/blob/f9a610774532fdde578b656dd838766e1173c4fc/docs/collective-experiment.md#L206-L216), [docs/collective-experiment.md#L39-L46](https://github.com/jigjoy-ai/baro/blob/f9a610774532fdde578b656dd838766e1173c4fc/docs/collective-experiment.md#L39-L46) (`clm_d8d4ea05c10b8183558cf2b2dc435321fb6e914764821698ba41093323fa6efb`)

## evaluation (2 claim(s))

- [observation/documented] Merges are blocked behind fail-closed gates: declared tests, build-before-commit, an evidence critic judging captured command output, and write-surface ownership; the human reviews a PR the gates already accepted. -- evidence: [README.md#L8-L11](https://github.com/jigjoy-ai/baro/blob/f9a610774532fdde578b656dd838766e1173c4fc/README.md#L8-L11), [README.md#L82-L91](https://github.com/jigjoy-ai/baro/blob/f9a610774532fdde578b656dd838766e1173c4fc/README.md#L82-L91) (`clm_1a78f2e24d029f64423c450abc8fb39f316d40b40233281a4d59ed951fb7e376`)
- [observation/documented] A paired A/B harness (ab-run.ts) compares legacy vs collective coordination on identical PRD bytes across isolated clones, alternating arm order, hashing verify inputs, and producing per-trial artifacts including diff.patch, metrics.json, and audit logs. -- evidence: [docs/collective-experiment.md#L328-L347](https://github.com/jigjoy-ai/baro/blob/f9a610774532fdde578b656dd838766e1173c4fc/docs/collective-experiment.md#L328-L347), [docs/collective-experiment.md#L369-L380](https://github.com/jigjoy-ai/baro/blob/f9a610774532fdde578b656dd838766e1173c4fc/docs/collective-experiment.md#L369-L380), [docs/collective-experiment.md#L359-L359](https://github.com/jigjoy-ai/baro/blob/f9a610774532fdde578b656dd838766e1173c4fc/docs/collective-experiment.md#L359-L359), [docs/collective-experiment.md#L162-L169](https://github.com/jigjoy-ai/baro/blob/f9a610774532fdde578b656dd838766e1173c4fc/docs/collective-experiment.md#L162-L169), [docs/collective-experiment.md#L361-L361](https://github.com/jigjoy-ai/baro/blob/f9a610774532fdde578b656dd838766e1173c4fc/docs/collective-experiment.md#L361-L361) (`clm_aad8c4d7e94fad5ffbc9d4e4979621a34a4ed639df0fb167335c949fc0a86df1`)

## dependencies (1 claim(s))

- [observation/documented] The tool requires Node 20+, git, and at least one LLM backend: the claude CLI (default), codex, or any OpenAI-compatible endpoint; `baro --doctor` checks the setup. -- evidence: [README.md#L22-L23](https://github.com/jigjoy-ai/baro/blob/f9a610774532fdde578b656dd838766e1173c4fc/README.md#L22-L23) (`clm_766911624b7300063f436a3c324000b42f9c0aee1fb1362034b1a4ca01d22eb9`)

## limitations (4 claim(s))

- [observation/documented] The docs state Baro lacks a trusted per-story CandidateVerifier that executes new deterministic commands in the active worktree, so genuinely missing or fully stale command evidence stays inconclusive after bounded rechecks. -- evidence: [docs/collective-runtime.md#L47-L53](https://github.com/jigjoy-ai/baro/blob/f9a610774532fdde578b656dd838766e1173c4fc/docs/collective-runtime.md#L47-L53) (`clm_bb94c90bc24882cf73f385ce667a79ed9663f7f19767f5a5e236628239cba494`)
- [observation/documented] Codex, OpenCode, and Pi workers are one-shot CLI processes that cannot consume corrective messages after exit; failed verdicts for those backends require a separate recovery execution rather than in-process revision. -- evidence: [docs/collective-experiment.md#L315-L322](https://github.com/jigjoy-ai/baro/blob/f9a610774532fdde578b656dd838766e1173c4fc/docs/collective-experiment.md#L315-L322), [docs/collective-runtime.md#L21-L28](https://github.com/jigjoy-ai/baro/blob/f9a610774532fdde578b656dd838766e1173c4fc/docs/collective-runtime.md#L21-L28) (`clm_3d6a7d0597e6ca15591c35cdbf4113cdb7106ddda2212e97034005af8fda2239`)
- [observation/documented] The public CLI does not yet expose process-level run resumption: a restart creates a new run identity, keeps the graph version as baseline, resets the discovery budget, and does not expose the old decision ledger. -- evidence: [docs/collective-experiment.md#L75-L87](https://github.com/jigjoy-ai/baro/blob/f9a610774532fdde578b656dd838766e1173c4fc/docs/collective-experiment.md#L75-L87) (`clm_9de5bb01170e5a33f41495cc23c00132ee1f87e71bca99c5775edf62c83a7fa6`)
- [observation/documented] `--local-only` disables pushes and PRs but is explicitly not an OS or network sandbox, since story agents can execute arbitrary shell commands; a hard no-push boundary requires removing git remotes. -- evidence: [README.md#L62-L73](https://github.com/jigjoy-ai/baro/blob/f9a610774532fdde578b656dd838766e1173c4fc/README.md#L62-L73), [docs/collective-experiment.md#L201-L202](https://github.com/jigjoy-ai/baro/blob/f9a610774532fdde578b656dd838766e1173c4fc/docs/collective-experiment.md#L201-L202) (`clm_105014d924b25e519cecc21d417b0d2de15a7cdb764de15ab0c6e84752a8697f`)

## relevance (1 claim(s))

- [observation/documented] A cloud option runs the same fleet on a hosted site with isolated sandboxes and provider keys, or users can attach their own machine as a cloud runner via `baro login` and `baro connect --install-service`. -- evidence: [README.md#L116-L119](https://github.com/jigjoy-ai/baro/blob/f9a610774532fdde578b656dd838766e1173c4fc/README.md#L116-L119) (`clm_31d494bd46599975f396e273b9c161237a5e8067e2bb73f2ce4cd14613a801eb`)

