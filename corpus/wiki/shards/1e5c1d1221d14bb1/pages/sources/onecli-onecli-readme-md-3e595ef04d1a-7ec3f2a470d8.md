---
access: public
aliases: []
claim_ids:
- clm_1aafcecba604e3a6b3425e43d4e63cd4c4c1243a5eb977c0316f6985630d6282
- clm_6ca02f5aaf94f803bd4bf6f3575aeac290e2996dd83b1701b3738e7a52814922
- clm_78f7ed147a13da0000b6a127a2f4815f6d09a2646b96f43e3bb711526ee39989
- clm_9da261786b514d052e4c5b44818fc4aa5c68cd1cbac8420f9bbc3a0f702c68c6
- clm_a686b8a5402d83443b13188e2d5f894af99a4e81e00d6e52cea6a5c4169312a2
- clm_d4b8cc091be8782a24b9a52609eb9151e9d46fb8f72a10f4309ec48af2f0334d
- clm_e8ef9c3b9376c86d199a7a71036e552f4cb129bbd512f9f2a7bfc1d13d2c8645
- clm_ec7c6cbbd4514ccd5c2e08bdd3fda4e54437dac2e0f8798b02121dd4e734f8f5
- clm_ff863f7e4d7efd0d3989321d9308e4ac0d17862d80d28648d33af977834d0074
maturity: draft
page_id: pg_1d0d678458c759e0af3d7ec3f2a470d8
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_28895cf60b2456cd95948a7a066abde7
title: onecli/onecli/README.md @ 3e595ef04d1a
updated_at: '2026-09-14T02:25:50Z'
---

# onecli/onecli/README.md @ 3e595ef04d1a

<!-- rcw:begin owner=source:src_28895cf60b2456cd95948a7a066abde7 block=evidence -->
- Credentials are never given to agents: the gateway injects them per request, matching secrets by host and path pattern into headers or query parameters, and agents authenticate with access tokens via Proxy-Authorization headers. [@claim:clm_1aafcecba604e3a6b3425e43d4e63cd4c4c1243a5eb977c0316f6985630d6282]
- Agent memory is kept by the platform so it persists, and users can read and edit it at any time from the dashboard. [@claim:clm_6ca02f5aaf94f803bd4bf6f3575aeac290e2996dd83b1701b3738e7a52814922]
- Repository development practice: local setup is `mise install`, `pnpm install`, `pnpm dev`, which generates .env secrets, starts PostgreSQL, applies migrations, and runs web, api, gateway and runner; `pnpm check` is the pre-push and CI gate and `pnpm test` runs test suites. [@claim:clm_78f7ed147a13da0000b6a127a2f4815f6d09a2646b96f43e3bb711526ee39989]
- The runner starts, parks and reaps agent sandboxes, polls a work queue owned by the API server, and never touches the database directly. [@claim:clm_9da261786b514d052e4c5b44818fc4aa5c68cd1cbac8420f9bbc3a0f702c68c6]
- Each agent can have its own Slack app answering in channels and DMs under its own name; a DM shares the same conversation as the web dashboard, and gateway approvals appear as Slack cards with Approve/Deny buttons. [@claim:clm_a686b8a5402d83443b13188e2d5f894af99a4e81e00d6e52cea6a5c4169312a2]
- Agents run in isolated sandboxes whose only network egress is the gateway, so they can reach only granted resources; the runner is outbound-only with no inbound ports, enabling NAT'd hosts without ingress or tunnels. [@claim:clm_d4b8cc091be8782a24b9a52609eb9151e9d46fb8f72a10f4309ec48af2f0334d]
- Repository development practice: contributions require reading the Contributing Guide and Code of Conduct and are accepted under a Contributor License Agreement with ChartDB, Inc., signable via the CLA Assistant flow on a pull request. [@claim:clm_e8ef9c3b9376c86d199a7a71036e552f4cb129bbd512f9f2a7bfc1d13d2c8645]
- Licensing is Apache-2.0 except for `ee/` directories under the OneCLI Enterprise License, which is free for development, testing and evaluation but requires a subscription for production use. [@claim:clm_ec7c6cbbd4514ccd5c2e08bdd3fda4e54437dac2e0f8798b02121dd4e734f8f5]
- The platform comprises a Next.js web dashboard, an API server control plane owning the database and work queue, a Rust gateway, a runner, a sandbox supervisor, an SSH terminator, and a Slack channel adapter. [@claim:clm_ff863f7e4d7efd0d3989321d9308e4ac0d17862d80d28648d33af977834d0074]
<!-- rcw:end owner=source:src_28895cf60b2456cd95948a7a066abde7 block=evidence -->

## Researcher notes

