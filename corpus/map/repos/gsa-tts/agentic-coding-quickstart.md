# gsa-tts/agentic-coding-quickstart

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit e0b9a3b60d87 @ 1c3580d2ef2330cc

## Summary (orientation draft, not independently verified)

The repository ships `acq`, a CLI that runs AI coding agents (e.g. opencode) inside isolated sandboxes (msb microVM by default, Docker sbx optionally) with USAi gateway access, secret proxying, and tiered network egress. Evidence is documentation-only (README and backend guide); no code or evaluation results are present. Evidence coverage: 128 of 310 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 46 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 13 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

13 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] acq supports two shipped isolation backends: msb (microsandbox, a lightweight open-source microVM runtime, the default) and sbx (Docker Sandboxes), with a Podman-based 'ppp' backend listed as in development. -- evidence: [docs/BACKEND_GUIDE.md#L22-L26](https://github.com/GSA-TTS/agentic-coding-quickstart/blob/e0b9a3b60d878080094264b407b03fb830c48c4e/docs/BACKEND_GUIDE.md#L22-L26), [README.md#L8-L10](https://github.com/GSA-TTS/agentic-coding-quickstart/blob/e0b9a3b60d878080094264b407b03fb830c48c4e/README.md#L8-L10), [docs/BACKEND_GUIDE.md#L114-L117](https://github.com/GSA-TTS/agentic-coding-quickstart/blob/e0b9a3b60d878080094264b407b03fb830c48c4e/docs/BACKEND_GUIDE.md#L114-L117)
- design-choices (3 claim(s)):
  - [observation/documented] Secrets are injected at runtime via a proxy/host-env binding (e.g. `--secret USAI_API_KEY@api.gsa.usai.gov`), so real secret values never enter the guest VM or container. -- evidence: [README.md#L155-L156](https://github.com/GSA-TTS/agentic-coding-quickstart/blob/e0b9a3b60d878080094264b407b03fb830c48c4e/README.md#L155-L156), [README.md#L34-L37](https://github.com/GSA-TTS/agentic-coding-quickstart/blob/e0b9a3b60d878080094264b407b03fb830c48c4e/README.md#L34-L37), [docs/BACKEND_GUIDE.md#L130-L143](https://github.com/GSA-TTS/agentic-coding-quickstart/blob/e0b9a3b60d878080094264b407b03fb830c48c4e/docs/BACKEND_GUIDE.md#L130-L143), [docs/BACKEND_GUIDE.md#L45-L55](https://github.com/GSA-TTS/agentic-coding-quickstart/blob/e0b9a3b60d878080094264b407b03fb830c48c4e/docs/BACKEND_GUIDE.md#L45-L55)
  - [observation/documented] Network egress is selected by a backend-neutral tier variable `ACQ_NETWORK_TIER` (strict, balanced, open; default balanced); strict and balanced are deny-by-default with allowlists, and `open` requires an explicit confirmation variable. -- evidence: [docs/BACKEND_GUIDE.md#L255-L260](https://github.com/GSA-TTS/agentic-coding-quickstart/blob/e0b9a3b60d878080094264b407b03fb830c48c4e/docs/BACKEND_GUIDE.md#L255-L260), [docs/BACKEND_GUIDE.md#L262-L266](https://github.com/GSA-TTS/agentic-coding-quickstart/blob/e0b9a3b60d878080094264b407b03fb830c48c4e/docs/BACKEND_GUIDE.md#L262-L266), [docs/BACKEND_GUIDE.md#L287-L317](https://github.com/GSA-TTS/agentic-coding-quickstart/blob/e0b9a3b60d878080094264b407b03fb830c48c4e/docs/BACKEND_GUIDE.md#L287-L317)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns (1 claim(s)):
  - [observation/documented] The companion playbook provides agent skills following the agentskills.io standard (e.g. federal-security-controls-lookup, ato-package, code-review), symlinked into ~/.agents/skills when a sandbox launches so agents discover them automatically. -- evidence: [README.md#L231-L234](https://github.com/GSA-TTS/agentic-coding-quickstart/blob/e0b9a3b60d878080094264b407b03fb830c48c4e/README.md#L231-L234), [README.md#L225-L229](https://github.com/GSA-TTS/agentic-coding-quickstart/blob/e0b9a3b60d878080094264b407b03fb830c48c4e/README.md#L225-L229)
- interfaces (3 claim(s)):
  - [observation/documented] The product's entry point is the `acq` CLI, invoked e.g. as `acq run opencode ~/my-project`, which runs the agent in a sandbox configured for federal usage. -- evidence: [README.md#L6-L6](https://github.com/GSA-TTS/agentic-coding-quickstart/blob/e0b9a3b60d878080094264b407b03fb830c48c4e/README.md#L6-L6), [README.md#L133-L135](https://github.com/GSA-TTS/agentic-coding-quickstart/blob/e0b9a3b60d878080094264b407b03fb830c48c4e/README.md#L133-L135), [README.md#L8-L10](https://github.com/GSA-TTS/agentic-coding-quickstart/blob/e0b9a3b60d878080094264b407b03fb830c48c4e/README.md#L8-L10)
  - [observation/documented] Backend selection is exposed via `acq backend set <name>`, a per-invocation `--backend` flag, and the `ACQ_BACKEND` environment variable. -- evidence: [docs/BACKEND_GUIDE.md#L171-L172](https://github.com/GSA-TTS/agentic-coding-quickstart/blob/e0b9a3b60d878080094264b407b03fb830c48c4e/docs/BACKEND_GUIDE.md#L171-L172), [docs/BACKEND_GUIDE.md#L74-L74](https://github.com/GSA-TTS/agentic-coding-quickstart/blob/e0b9a3b60d878080094264b407b03fb830c48c4e/docs/BACKEND_GUIDE.md#L74-L74), [docs/BACKEND_GUIDE.md#L165-L165](https://github.com/GSA-TTS/agentic-coding-quickstart/blob/e0b9a3b60d878080094264b407b03fb830c48c4e/docs/BACKEND_GUIDE.md#L165-L165), [docs/BACKEND_GUIDE.md#L77-L77](https://github.com/GSA-TTS/agentic-coding-quickstart/blob/e0b9a3b60d878080094264b407b03fb830c48c4e/docs/BACKEND_GUIDE.md#L77-L77), [docs/BACKEND_GUIDE.md#L80-L81](https://github.com/GSA-TTS/agentic-coding-quickstart/blob/e0b9a3b60d878080094264b407b03fb830c48c4e/docs/BACKEND_GUIDE.md#L80-L81), [docs/BACKEND_GUIDE.md#L168-L168](https://github.com/GSA-TTS/agentic-coding-quickstart/blob/e0b9a3b60d878080094264b407b03fb830c48c4e/docs/BACKEND_GUIDE.md#L168-L168)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] The sbx backend requires the sbx CLI >= 0.38.0 (for the v2 kit grammar) plus a Docker account, while the msb backend requires msb >= 0.6.8 and host virtualization (KVM, Apple Silicon HVF, or Windows WHP). -- evidence: [docs/BACKEND_GUIDE.md#L147-L150](https://github.com/GSA-TTS/agentic-coding-quickstart/blob/e0b9a3b60d878080094264b407b03fb830c48c4e/docs/BACKEND_GUIDE.md#L147-L150), [docs/BACKEND_GUIDE.md#L59-L63](https://github.com/GSA-TTS/agentic-coding-quickstart/blob/e0b9a3b60d878080094264b407b03fb830c48c4e/docs/BACKEND_GUIDE.md#L59-L63)
- limitations (3 claim(s)):
More evidence: [full detail](agentic-coding-quickstart.detail.md)

Metadata and full claim list: [full detail](agentic-coding-quickstart.detail.md)
Human notes ([notes](agentic-coding-quickstart.notes.md), never overwritten by build)

[Back to map index](../../index.md)
