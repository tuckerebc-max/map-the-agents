# gsa-tts/agentic-coding-quickstart -- full detail

[Back to orientation](agentic-coding-quickstart.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/gsa-tts/agentic-coding-quickstart/e0b9a3b60d878080094264b407b03fb830c48c4e/1c3580d2ef2330cc.json](../../../wiki/dossiers/gsa-tts/agentic-coding-quickstart/e0b9a3b60d878080094264b407b03fb830c48c4e/1c3580d2ef2330cc.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] acq supports two shipped isolation backends: msb (microsandbox, a lightweight open-source microVM runtime, the default) and sbx (Docker Sandboxes), with a Podman-based 'ppp' backend listed as in development. -- evidence: [docs/BACKEND_GUIDE.md#L22-L26](https://github.com/GSA-TTS/agentic-coding-quickstart/blob/e0b9a3b60d878080094264b407b03fb830c48c4e/docs/BACKEND_GUIDE.md#L22-L26), [README.md#L8-L10](https://github.com/GSA-TTS/agentic-coding-quickstart/blob/e0b9a3b60d878080094264b407b03fb830c48c4e/README.md#L8-L10), [docs/BACKEND_GUIDE.md#L114-L117](https://github.com/GSA-TTS/agentic-coding-quickstart/blob/e0b9a3b60d878080094264b407b03fb830c48c4e/docs/BACKEND_GUIDE.md#L114-L117) (`clm_716833d4b1537dab00f86cfb1764f13d54581aed86f384bc781595fc1b9a8727`)

## design-choices (3 claim(s))

- [observation/documented] Secrets are injected at runtime via a proxy/host-env binding (e.g. `--secret USAI_API_KEY@api.gsa.usai.gov`), so real secret values never enter the guest VM or container. -- evidence: [README.md#L155-L156](https://github.com/GSA-TTS/agentic-coding-quickstart/blob/e0b9a3b60d878080094264b407b03fb830c48c4e/README.md#L155-L156), [README.md#L34-L37](https://github.com/GSA-TTS/agentic-coding-quickstart/blob/e0b9a3b60d878080094264b407b03fb830c48c4e/README.md#L34-L37), [docs/BACKEND_GUIDE.md#L130-L143](https://github.com/GSA-TTS/agentic-coding-quickstart/blob/e0b9a3b60d878080094264b407b03fb830c48c4e/docs/BACKEND_GUIDE.md#L130-L143), [docs/BACKEND_GUIDE.md#L45-L55](https://github.com/GSA-TTS/agentic-coding-quickstart/blob/e0b9a3b60d878080094264b407b03fb830c48c4e/docs/BACKEND_GUIDE.md#L45-L55) (`clm_d0ba634522f37ab024d8e9e5d7d8dc6b73299a4817392db6862c88ffdc5bf36c`)
- [observation/documented] Network egress is selected by a backend-neutral tier variable `ACQ_NETWORK_TIER` (strict, balanced, open; default balanced); strict and balanced are deny-by-default with allowlists, and `open` requires an explicit confirmation variable. -- evidence: [docs/BACKEND_GUIDE.md#L255-L260](https://github.com/GSA-TTS/agentic-coding-quickstart/blob/e0b9a3b60d878080094264b407b03fb830c48c4e/docs/BACKEND_GUIDE.md#L255-L260), [docs/BACKEND_GUIDE.md#L262-L266](https://github.com/GSA-TTS/agentic-coding-quickstart/blob/e0b9a3b60d878080094264b407b03fb830c48c4e/docs/BACKEND_GUIDE.md#L262-L266), [docs/BACKEND_GUIDE.md#L287-L317](https://github.com/GSA-TTS/agentic-coding-quickstart/blob/e0b9a3b60d878080094264b407b03fb830c48c4e/docs/BACKEND_GUIDE.md#L287-L317) (`clm_d58b51a625f9387cadaee2583fe719821051e98f6e17166bf76b499279253cf7`)
- [observation/documented] The msb backend defaults sandboxes to 4 GiB RAM and 2 vCPUs (overriding msb's 512 MiB/1 vCPU, which OOM-kills Node TUI agents), tunable via ACQ_MSB_MEMORY/ACQ_MSB_CPUS. -- evidence: [docs/BACKEND_GUIDE.md#L325-L333](https://github.com/GSA-TTS/agentic-coding-quickstart/blob/e0b9a3b60d878080094264b407b03fb830c48c4e/docs/BACKEND_GUIDE.md#L325-L333) (`clm_ec67fd4b090e8fa5fbcf3e8e84a541fd305328395e2b4e7bc51572c2050a0fad`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (1 claim(s))

- [observation/documented] The companion playbook provides agent skills following the agentskills.io standard (e.g. federal-security-controls-lookup, ato-package, code-review), symlinked into ~/.agents/skills when a sandbox launches so agents discover them automatically. -- evidence: [README.md#L231-L234](https://github.com/GSA-TTS/agentic-coding-quickstart/blob/e0b9a3b60d878080094264b407b03fb830c48c4e/README.md#L231-L234), [README.md#L225-L229](https://github.com/GSA-TTS/agentic-coding-quickstart/blob/e0b9a3b60d878080094264b407b03fb830c48c4e/README.md#L225-L229) (`clm_eaefae11f3ee353787874776163f43a32a7ef20b75c67b93c73163277bb12d99`)

## interfaces (3 claim(s))

- [observation/documented] The product's entry point is the `acq` CLI, invoked e.g. as `acq run opencode ~/my-project`, which runs the agent in a sandbox configured for federal usage. -- evidence: [README.md#L6-L6](https://github.com/GSA-TTS/agentic-coding-quickstart/blob/e0b9a3b60d878080094264b407b03fb830c48c4e/README.md#L6-L6), [README.md#L133-L135](https://github.com/GSA-TTS/agentic-coding-quickstart/blob/e0b9a3b60d878080094264b407b03fb830c48c4e/README.md#L133-L135), [README.md#L8-L10](https://github.com/GSA-TTS/agentic-coding-quickstart/blob/e0b9a3b60d878080094264b407b03fb830c48c4e/README.md#L8-L10) (`clm_48943dbfaf9facae9d6e09e77b8c14547c34dddc49d9c1ff44dad1ca2ba20608`)
- [observation/documented] Backend selection is exposed via `acq backend set <name>`, a per-invocation `--backend` flag, and the `ACQ_BACKEND` environment variable. -- evidence: [docs/BACKEND_GUIDE.md#L171-L172](https://github.com/GSA-TTS/agentic-coding-quickstart/blob/e0b9a3b60d878080094264b407b03fb830c48c4e/docs/BACKEND_GUIDE.md#L171-L172), [docs/BACKEND_GUIDE.md#L74-L74](https://github.com/GSA-TTS/agentic-coding-quickstart/blob/e0b9a3b60d878080094264b407b03fb830c48c4e/docs/BACKEND_GUIDE.md#L74-L74), [docs/BACKEND_GUIDE.md#L165-L165](https://github.com/GSA-TTS/agentic-coding-quickstart/blob/e0b9a3b60d878080094264b407b03fb830c48c4e/docs/BACKEND_GUIDE.md#L165-L165), [docs/BACKEND_GUIDE.md#L77-L77](https://github.com/GSA-TTS/agentic-coding-quickstart/blob/e0b9a3b60d878080094264b407b03fb830c48c4e/docs/BACKEND_GUIDE.md#L77-L77), [docs/BACKEND_GUIDE.md#L80-L81](https://github.com/GSA-TTS/agentic-coding-quickstart/blob/e0b9a3b60d878080094264b407b03fb830c48c4e/docs/BACKEND_GUIDE.md#L80-L81), [docs/BACKEND_GUIDE.md#L168-L168](https://github.com/GSA-TTS/agentic-coding-quickstart/blob/e0b9a3b60d878080094264b407b03fb830c48c4e/docs/BACKEND_GUIDE.md#L168-L168) (`clm_3cced06c7f668f2b0f0390a590ce4801bd68a187f4ad2e5dc57de66f03774dc1`)
- [observation/documented] A backend-neutral custom base image can be set with `--image` or `ACQ_IMAGE`; precedence is flag > env > backend-specific variable, and an explicitly set `ACQ_MSB_IMAGE` wins over the neutral knob with a notice. -- evidence: [docs/BACKEND_GUIDE.md#L440-L443](https://github.com/GSA-TTS/agentic-coding-quickstart/blob/e0b9a3b60d878080094264b407b03fb830c48c4e/docs/BACKEND_GUIDE.md#L440-L443), [docs/BACKEND_GUIDE.md#L430-L431](https://github.com/GSA-TTS/agentic-coding-quickstart/blob/e0b9a3b60d878080094264b407b03fb830c48c4e/docs/BACKEND_GUIDE.md#L430-L431), [docs/BACKEND_GUIDE.md#L422-L424](https://github.com/GSA-TTS/agentic-coding-quickstart/blob/e0b9a3b60d878080094264b407b03fb830c48c4e/docs/BACKEND_GUIDE.md#L422-L424) (`clm_632bea2423d1c83f8de31755260d4da72e9db51225a57dec581c0e1e7ac23330`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The sbx backend requires the sbx CLI >= 0.38.0 (for the v2 kit grammar) plus a Docker account, while the msb backend requires msb >= 0.6.8 and host virtualization (KVM, Apple Silicon HVF, or Windows WHP). -- evidence: [docs/BACKEND_GUIDE.md#L147-L150](https://github.com/GSA-TTS/agentic-coding-quickstart/blob/e0b9a3b60d878080094264b407b03fb830c48c4e/docs/BACKEND_GUIDE.md#L147-L150), [docs/BACKEND_GUIDE.md#L59-L63](https://github.com/GSA-TTS/agentic-coding-quickstart/blob/e0b9a3b60d878080094264b407b03fb830c48c4e/docs/BACKEND_GUIDE.md#L59-L63) (`clm_6a20a6de2f79815591eb74c0197bc0ed37078855cf33ec492ab6fa37bcd9382e`)

## limitations (3 claim(s))

- [observation/documented] On sbx 0.38, `sbx kit add` cannot apply startup-bearing kits to a live sandbox, so the built-in kit bundle can only be extended by recreating the sandbox; msb is unaffected. -- evidence: [docs/BACKEND_GUIDE.md#L94-L108](https://github.com/GSA-TTS/agentic-coding-quickstart/blob/e0b9a3b60d878080094264b407b03fb830c48c4e/docs/BACKEND_GUIDE.md#L94-L108), [docs/BACKEND_GUIDE.md#L45-L55](https://github.com/GSA-TTS/agentic-coding-quickstart/blob/e0b9a3b60d878080094264b407b03fb830c48c4e/docs/BACKEND_GUIDE.md#L45-L55) (`clm_7e0680100f3993f23071f16f3890eab718e31ca70b9dc01015d27ff26813b1b0`)
- [observation/documented] Although microsandbox has a snapshot CLI, acq does not surface it, so `ACQ_BACKEND_SUPPORTS_SNAPSHOTS=0` reflects what acq exposes rather than msb's capability. -- evidence: [docs/BACKEND_GUIDE.md#L130-L143](https://github.com/GSA-TTS/agentic-coding-quickstart/blob/e0b9a3b60d878080094264b407b03fb830c48c4e/docs/BACKEND_GUIDE.md#L130-L143), [docs/BACKEND_GUIDE.md#L85-L90](https://github.com/GSA-TTS/agentic-coding-quickstart/blob/e0b9a3b60d878080094264b407b03fb830c48c4e/docs/BACKEND_GUIDE.md#L85-L90) (`clm_6722ca9a4503e8da86de84d6c4fb2cb0f3f50c9690a92fca3f352b422c374fdc`)
- [observation/documented] msb cannot mount symlinked host paths (failing with 'Not a directory'), so acq canonicalizes workspaces; macOS $TMPDIR paths under /var fail unless resolved to /private/var. -- evidence: [docs/BACKEND_GUIDE.md#L356-L363](https://github.com/GSA-TTS/agentic-coding-quickstart/blob/e0b9a3b60d878080094264b407b03fb830c48c4e/docs/BACKEND_GUIDE.md#L356-L363) (`clm_21bcf4ec6d99827d6cc427fcbe821fefc06ff85f931d7ca018065f7ca40a9173`)

## relevance (1 claim(s))

- [observation/documented] The quickstart targets federal teams using AI coding agents, connecting them to USAi (GSA's LLM gateway at api.gsa.usai.gov), and is classified as a local development environment for Low/Moderate-impact work, not a production/hosted environment. -- evidence: [README.md#L3-L4](https://github.com/GSA-TTS/agentic-coding-quickstart/blob/e0b9a3b60d878080094264b407b03fb830c48c4e/README.md#L3-L4), [README.md#L248-L248](https://github.com/GSA-TTS/agentic-coding-quickstart/blob/e0b9a3b60d878080094264b407b03fb830c48c4e/README.md#L248-L248) (`clm_a4600bd06623848c727681178028fff7c21b85aef18643951c0cd1620d0e77eb`)

