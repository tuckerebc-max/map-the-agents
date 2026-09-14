# vercel-labs/deepsec -- full detail

[Back to orientation](deepsec.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/vercel-labs/deepsec/23a69227e3380e6b44a7ebd93c52e023c59f17c3/83b78ffadd29c0d1.json](../../../wiki/dossiers/vercel-labs/deepsec/23a69227e3380e6b44a7ebd93c52e023c59f17c3/83b78ffadd29c0d1.json)

## specifications (1 claim(s))

- [observation/documented] deepsec is an agent-powered vulnerability scanner that runs in the user's own infrastructure and is optimized for on-demand review of all code in large existing repositories. -- evidence: [README.md#L3-L4](https://github.com/vercel-labs/deepsec/blob/23a69227e3380e6b44a7ebd93c52e023c59f17c3/README.md#L3-L4) (`clm_5351b712cea0ec0447ec8a87642522e69f09ec3ab43f435e88448376e24c5907`)

## components (5 claim(s))

- [observation/documented] The scan stage globs the project root, applies regex matchers to every matched file, and writes candidate matches into per-file FileRecords without any AI usage. -- evidence: [docs/architecture.md#L86-L91](https://github.com/vercel-labs/deepsec/blob/23a69227e3380e6b44a7ebd93c52e023c59f17c3/docs/architecture.md#L86-L91) (`clm_0cd68a7deeb0d5589eca6e9ef4c41a8e2a0198956fe916baf77a719274b74867`)
- [observation/documented] The process stage batches pending files, sends each batch to a configured AI agent backend with the system prompt and INFO.md, and parses JSON responses into findings stored on FileRecords. -- evidence: [docs/architecture.md#L99-L106](https://github.com/vercel-labs/deepsec/blob/23a69227e3380e6b44a7ebd93c52e023c59f17c3/docs/architecture.md#L99-L106) (`clm_7777d76bbabddc6e65eb53320a473bee7ba741f52299d0e907174cbed290f855`)
- [observation/documented] Three agent backends are supported for process: codex (default, via @openai/codex-sdk), claude (via @anthropic-ai/claude-agent-sdk), and pi (via @earendil-works/pi-coding-agent), each with a documented default model. -- evidence: [docs/architecture.md#L108-L108](https://github.com/vercel-labs/deepsec/blob/23a69227e3380e6b44a7ebd93c52e023c59f17c3/docs/architecture.md#L108-L108), [docs/architecture.md#L110-L114](https://github.com/vercel-labs/deepsec/blob/23a69227e3380e6b44a7ebd93c52e023c59f17c3/docs/architecture.md#L110-L114) (`clm_10c58a31819b721241fcc455430122a92831b302f6f55b8013bba0f8ecb9433e`)
- [observation/documented] The architecture doc describes five plugin extension points in packages/core/src/plugin.ts: matchers, notifiers, and agents are additive, while ownership, people, and executor are single-slot with last-write-wins ordering. -- evidence: [docs/architecture.md#L157-L158](https://github.com/vercel-labs/deepsec/blob/23a69227e3380e6b44a7ebd93c52e023c59f17c3/docs/architecture.md#L157-L158), [docs/architecture.md#L160-L165](https://github.com/vercel-labs/deepsec/blob/23a69227e3380e6b44a7ebd93c52e023c59f17c3/docs/architecture.md#L160-L165), [docs/configuration.md#L128-L129](https://github.com/vercel-labs/deepsec/blob/23a69227e3380e6b44a7ebd93c52e023c59f17c3/docs/configuration.md#L128-L129) (`clm_868d5db5ede5f73973baeac3c2fe9c0c8e2f0710ef309b7606f0f58b6ae7e8ff`)
- [observation/documented] The setup coordinator uses a read-only agent to produce INFO.md and a structured surface inventory, evaluates scan coverage, generates data-only matcher specs validated for regex safety and slug collisions, and gates paid processing until coverage passes. -- evidence: [docs/architecture.md#L67-L79](https://github.com/vercel-labs/deepsec/blob/23a69227e3380e6b44a7ebd93c52e023c59f17c3/docs/architecture.md#L67-L79) (`clm_6ee99b1a49d13d324d18b0292ba5406d2d903686c0e73c9e10d61f23ac85d278`)

## design-choices (1 claim(s))

- [observation/documented] The unit of work is a source file rather than a finding, which the architecture doc says makes per-file atomic locking and idempotent merges natural. -- evidence: [docs/architecture.md#L184-L186](https://github.com/vercel-labs/deepsec/blob/23a69227e3380e6b44a7ebd93c52e023c59f17c3/docs/architecture.md#L184-L186) (`clm_bb5b194cf2f2df691e327770bca86bd9eaa7e2c15fe808a947e6585cdbac2611`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The CLI exposes subcommands including scan, process, process --diff, triage, revalidate, enrich, report, export, metrics, status, and sandbox for running any command on Vercel Sandbox microVMs. -- evidence: [README.md#L120-L132](https://github.com/vercel-labs/deepsec/blob/23a69227e3380e6b44a7ebd93c52e023c59f17c3/README.md#L120-L132) (`clm_4515bc54b8dea6324ec52352965a33d705d16f5b71fc42048f809b5d9dcbd3be`)
- [observation/documented] Configuration lives in deepsec.config.ts (or .mjs/.js/.cjs) resolved from the current directory walking upward, declaring projects, plugins, matcher filters, default agent/model/thinking level, AI route, and dataDir. -- evidence: [docs/configuration.md#L6-L7](https://github.com/vercel-labs/deepsec/blob/23a69227e3380e6b44a7ebd93c52e023c59f17c3/docs/configuration.md#L6-L7), [docs/configuration.md#L29-L38](https://github.com/vercel-labs/deepsec/blob/23a69227e3380e6b44a7ebd93c52e023c59f17c3/docs/configuration.md#L29-L38) (`clm_9805870812e23e8c45bc01b85f098cb82d63934be157bd09d42560b814462a54`)

## memory-state (2 claim(s))

- [observation/documented] On-disk state is append-only: re-scans merge new candidates, re-processing appends to analysisHistory and merges findings, and revalidation annotates findings with verdicts without overwriting or deleting anything. -- evidence: [docs/data-layout.md#L88-L91](https://github.com/vercel-labs/deepsec/blob/23a69227e3380e6b44a7ebd93c52e023c59f17c3/docs/data-layout.md#L88-L91), [docs/architecture.md#L58-L61](https://github.com/vercel-labs/deepsec/blob/23a69227e3380e6b44a7ebd93c52e023c59f17c3/docs/architecture.md#L58-L61) (`clm_c1cb44e3925745ed552930bc70b4e219fd30ee62dabc58da7de0d9bf2bfb1b0a`)
- [observation/documented] Each FileRecord tracks candidates, findings, an append-only analysisHistory, gitInfo, a lifecycle status (pending/processing/analyzed/error), and a lockedByRunId field used for atomic file claiming. -- evidence: [docs/data-layout.md#L98-L110](https://github.com/vercel-labs/deepsec/blob/23a69227e3380e6b44a7ebd93c52e023c59f17c3/docs/data-layout.md#L98-L110) (`clm_464516511c0919624e784e1287d95cab321c0ff3b445638529795cef84d4a7c6`)

## orchestration (3 claim(s))

- [observation/documented] The processor claims files atomically via lockedByRunId so multiple workers can run in parallel; concurrency and batch size flags control how many files are in flight. -- evidence: [docs/architecture.md#L120-L123](https://github.com/vercel-labs/deepsec/blob/23a69227e3380e6b44a7ebd93c52e023c59f17c3/docs/architecture.md#L120-L123) (`clm_3a44982f7830f0ddfd911d65ad3ee8c631bb4b12577bfd9a9ec30d95bf42a145`)
- [observation/documented] For large codebases, work fans out across worker machines in parallel, and interrupted or errored runs can be re-run to resume, skipping already-analyzed files. -- evidence: [README.md#L8-L11](https://github.com/vercel-labs/deepsec/blob/23a69227e3380e6b44a7ebd93c52e023c59f17c3/README.md#L8-L11) (`clm_cf77ee141d897b14cc35dd32e20cbd72396bd21915c0650cb9c4a8b573b60d40`)
- [observation/documented] Large monorepos can optionally fan work across Vercel Sandbox microVMs; the local working tree is tarballed and uploaded (excluding .git), and model credentials stay host-side and are injected only at the egress host. -- evidence: [README.md#L102-L105](https://github.com/vercel-labs/deepsec/blob/23a69227e3380e6b44a7ebd93c52e023c59f17c3/README.md#L102-L105), [README.md#L96-L96](https://github.com/vercel-labs/deepsec/blob/23a69227e3380e6b44a7ebd93c52e023c59f17c3/README.md#L96-L96) (`clm_9f355c8aff5522ff4e5fff4d92c2cdf6af4521e831cb6e1ae00c01db6135e1ae`)

## tools-permissions (1 claim(s))

- [observation/documented] The security model treats deepsec like a coding agent with full shell access on its host environment; in sandbox mode, agent API keys are injected outside the sandbox and worker egress is limited to coding-agent hosts. -- evidence: [README.md#L109-L111](https://github.com/vercel-labs/deepsec/blob/23a69227e3380e6b44a7ebd93c52e023c59f17c3/README.md#L109-L111), [README.md#L115-L116](https://github.com/vercel-labs/deepsec/blob/23a69227e3380e6b44a7ebd93c52e023c59f17c3/README.md#L115-L116) (`clm_b2dfed48c617a9f5d12e5edd6b4643f2bcadeb989857841d6c018705cfcd7d0d`)

## evaluation (1 claim(s))

- [observation/documented] The revalidate stage re-checks findings for false positives using git history and, per the docs, empirically reduces the false-positive rate by 50% or more on most repos. -- evidence: [docs/architecture.md#L135-L135](https://github.com/vercel-labs/deepsec/blob/23a69227e3380e6b44a7ebd93c52e023c59f17c3/docs/architecture.md#L135-L135), [docs/architecture.md#L127-L133](https://github.com/vercel-labs/deepsec/blob/23a69227e3380e6b44a7ebd93c52e023c59f17c3/docs/architecture.md#L127-L133) (`clm_8ce0fb86a485d89e06007e71557f92699c8ad62d668c1ffa60ca24fbaf5ecc43`)

## dependencies (2 claim(s))

- [observation/documented] By default model calls route through Vercel AI Gateway; users can instead bring their own OpenAI, Anthropic, or custom HTTPS provider key via --model-auth direct with --ai-provider and --ai-api-key-env. -- evidence: [README.md#L79-L87](https://github.com/vercel-labs/deepsec/blob/23a69227e3380e6b44a7ebd93c52e023c59f17c3/README.md#L79-L87) (`clm_b37ec0fefb68564ecfa35c738009ab786ebd3dad642e86daf6f01dc594b706e8`)
- [observation/documented] Only the name of the environment variable holding the model key is stored, never the key value itself; setup-state evidence likewise contains no credential values. -- evidence: [README.md#L79-L87](https://github.com/vercel-labs/deepsec/blob/23a69227e3380e6b44a7ebd93c52e023c59f17c3/README.md#L79-L87), [docs/data-layout.md#L25-L28](https://github.com/vercel-labs/deepsec/blob/23a69227e3380e6b44a7ebd93c52e023c59f17c3/docs/data-layout.md#L25-L28) (`clm_b6bed49895eecebc40b35a02a6ad4fc03946a9346b3a4d1fc1919a1ddbba76ec`)

## limitations (2 claim(s))

- [observation/documented] Because it uses top models at maximum thinking levels by default, scans of large codebases can cost thousands to tens of thousands of dollars, per the README's own cost warning. -- evidence: [README.md#L6-L6](https://github.com/vercel-labs/deepsec/blob/23a69227e3380e6b44a7ebd93c52e023c59f17c3/README.md#L6-L6) (`clm_41663151cac87722586eb3112a3d9ca5d0244b2c5ce391fef28f9e27db391c62`)
- [observation/documented] The README warns of prompt-injection risk from external dependencies or vendored code even though the tool is designed to run on trusted source code. -- evidence: [README.md#L109-L111](https://github.com/vercel-labs/deepsec/blob/23a69227e3380e6b44a7ebd93c52e023c59f17c3/README.md#L109-L111) (`clm_d1e35c69c040e76a282f80e6fb2785a1dc796ff0e0cafbf8609435a4aaa46688`)

## relevance (1 claim(s))

- [observation/documented] deepsec targets teams wanting deep, long-running vulnerability review of large existing codebases, with per-finding triage (~1 cent per finding) and revalidation priced comparably to the AI process stage. -- evidence: [docs/faq.md#L63-L63](https://github.com/vercel-labs/deepsec/blob/23a69227e3380e6b44a7ebd93c52e023c59f17c3/docs/faq.md#L63-L63), [README.md#L3-L4](https://github.com/vercel-labs/deepsec/blob/23a69227e3380e6b44a7ebd93c52e023c59f17c3/README.md#L3-L4) (`clm_b1249a365f93e8b24fc9c9eb9018cf0fec5f9eec118efbabafb3169fab884ae6`)

