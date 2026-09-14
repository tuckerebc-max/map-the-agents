---
access: public
aliases: []
claim_ids:
- clm_21bcf4ec6d99827d6cc427fcbe821fefc06ff85f931d7ca018065f7ca40a9173
- clm_3cced06c7f668f2b0f0390a590ce4801bd68a187f4ad2e5dc57de66f03774dc1
- clm_632bea2423d1c83f8de31755260d4da72e9db51225a57dec581c0e1e7ac23330
- clm_6722ca9a4503e8da86de84d6c4fb2cb0f3f50c9690a92fca3f352b422c374fdc
- clm_6a20a6de2f79815591eb74c0197bc0ed37078855cf33ec492ab6fa37bcd9382e
- clm_716833d4b1537dab00f86cfb1764f13d54581aed86f384bc781595fc1b9a8727
- clm_7e0680100f3993f23071f16f3890eab718e31ca70b9dc01015d27ff26813b1b0
- clm_d0ba634522f37ab024d8e9e5d7d8dc6b73299a4817392db6862c88ffdc5bf36c
- clm_d58b51a625f9387cadaee2583fe719821051e98f6e17166bf76b499279253cf7
- clm_ec67fd4b090e8fa5fbcf3e8e84a541fd305328395e2b4e7bc51572c2050a0fad
maturity: draft
page_id: pg_1dcf8733542c58459c2e28c997a00f03
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_f7af68416c0c53beb65224294d6d7d69
title: GSA-TTS/agentic-coding-quickstart/docs/BACKEND_GUIDE.md @ e0b9a3b60d87
updated_at: '2026-09-14T03:54:37Z'
---

# GSA-TTS/agentic-coding-quickstart/docs/BACKEND_GUIDE.md @ e0b9a3b60d87

<!-- rcw:begin owner=source:src_f7af68416c0c53beb65224294d6d7d69 block=evidence -->
- msb cannot mount symlinked host paths (failing with 'Not a directory'), so acq canonicalizes workspaces; macOS $TMPDIR paths under /var fail unless resolved to /private/var. [@claim:clm_21bcf4ec6d99827d6cc427fcbe821fefc06ff85f931d7ca018065f7ca40a9173]
- Backend selection is exposed via `acq backend set <name>`, a per-invocation `--backend` flag, and the `ACQ_BACKEND` environment variable. [@claim:clm_3cced06c7f668f2b0f0390a590ce4801bd68a187f4ad2e5dc57de66f03774dc1]
- A backend-neutral custom base image can be set with `--image` or `ACQ_IMAGE`; precedence is flag > env > backend-specific variable, and an explicitly set `ACQ_MSB_IMAGE` wins over the neutral knob with a notice. [@claim:clm_632bea2423d1c83f8de31755260d4da72e9db51225a57dec581c0e1e7ac23330]
- Although microsandbox has a snapshot CLI, acq does not surface it, so `ACQ_BACKEND_SUPPORTS_SNAPSHOTS=0` reflects what acq exposes rather than msb's capability. [@claim:clm_6722ca9a4503e8da86de84d6c4fb2cb0f3f50c9690a92fca3f352b422c374fdc]
- The sbx backend requires the sbx CLI >= 0.38.0 (for the v2 kit grammar) plus a Docker account, while the msb backend requires msb >= 0.6.8 and host virtualization (KVM, Apple Silicon HVF, or Windows WHP). [@claim:clm_6a20a6de2f79815591eb74c0197bc0ed37078855cf33ec492ab6fa37bcd9382e]
- acq supports two shipped isolation backends: msb (microsandbox, a lightweight open-source microVM runtime, the default) and sbx (Docker Sandboxes), with a Podman-based 'ppp' backend listed as in development. [@claim:clm_716833d4b1537dab00f86cfb1764f13d54581aed86f384bc781595fc1b9a8727]
- On sbx 0.38, `sbx kit add` cannot apply startup-bearing kits to a live sandbox, so the built-in kit bundle can only be extended by recreating the sandbox; msb is unaffected. [@claim:clm_7e0680100f3993f23071f16f3890eab718e31ca70b9dc01015d27ff26813b1b0]
- Secrets are injected at runtime via a proxy/host-env binding (e.g. `--secret USAI_API_KEY@api.gsa.usai.gov`), so real secret values never enter the guest VM or container. [@claim:clm_d0ba634522f37ab024d8e9e5d7d8dc6b73299a4817392db6862c88ffdc5bf36c]
- Network egress is selected by a backend-neutral tier variable `ACQ_NETWORK_TIER` (strict, balanced, open; default balanced); strict and balanced are deny-by-default with allowlists, and `open` requires an explicit confirmation variable. [@claim:clm_d58b51a625f9387cadaee2583fe719821051e98f6e17166bf76b499279253cf7]
- The msb backend defaults sandboxes to 4 GiB RAM and 2 vCPUs (overriding msb's 512 MiB/1 vCPU, which OOM-kills Node TUI agents), tunable via ACQ_MSB_MEMORY/ACQ_MSB_CPUS. [@claim:clm_ec67fd4b090e8fa5fbcf3e8e84a541fd305328395e2b4e7bc51572c2050a0fad]
<!-- rcw:end owner=source:src_f7af68416c0c53beb65224294d6d7d69 block=evidence -->

## Researcher notes

