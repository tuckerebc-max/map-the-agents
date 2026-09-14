---
access: public
aliases: []
claim_ids:
- clm_07be4d77d6df7cdbf7e16516b36ea11732c96e02572ce632f9da338f01417380
- clm_0b823cb54ca3e16b3bc83d065b8a0b69569b469f57e00bb763aa81520ba0c97d
- clm_43e6a44524b7999ec69c6d1db772b7d4218d73c0c963af9c71d73aab299ba7b2
- clm_7d53517883f87e7e9e6ee152531f4f1d1daabcdc0b641fc3592e3057630dafb3
- clm_8e36d303fb7c3b7f02885e59915a461e7de307cfd6239f856b89aa63e80b906a
- clm_bc394e17d63d26b10dcec08cac4001456b5f19e3fcb1c1561f02e943025dd2fe
- clm_c341709600308201865df64c31a5134c6de266aded16baee1cdd5b230a20ab34
maturity: draft
page_id: pg_0ead2e0cd83b586c9b4879dd054bde79
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_352b0e355cbd54268718831d36e39e0e
title: yc-software/qm/docs/deploy-directory.md @ 361a6c0095dc
updated_at: '2026-09-14T03:24:57Z'
---

# yc-software/qm/docs/deploy-directory.md @ 361a6c0095dc

<!-- rcw:begin owner=source:src_352b0e355cbd54268718831d36e39e0e block=evidence -->
- The sandbox.egress contract clause is VALIDATED-ONLY: qm check emits wildcard/host warnings, but runtime enforcement of egress is explicitly absent. [@claim:clm_07be4d77d6df7cdbf7e16516b36ea11732c96e02572ce632f9da338f01417380]
- The deployment config root requires contract: 1, orgId, publicUrl, target, and a services list including core; target is docker, fly, or aws, and unknown contract majors fail closed. [@claim:clm_0b823cb54ca3e16b3bc83d065b8a0b69569b469f57e00bb763aa81520ba0c97d]
- Deployments depend on the @yc-software/qm package; the deployment directory's package.json pins the engine at the exact scaffolding version so the directory records which CLI interprets it. [@claim:clm_43e6a44524b7999ec69c6d1db772b7d4218d73c0c963af9c71d73aab299ba7b2]
- Repository development practice: the normal deployment gate order is check, doctor, plan, up --yes, then check --live, with infra build-image preceding plan on AWS MicroVM sandboxes. [@claim:clm_7d53517883f87e7e9e6ee152531f4f1d1daabcdc0b641fc3592e3057630dafb3]
- Published apps receive AGENT_API_URL and AGENT_CREDENTIAL_TOKEN and call $AGENT_API_URL/v1/credentials/broker with the token in x-agent-capability, authorizing as the immutable publisher rather than the viewing person. [@claim:clm_8e36d303fb7c3b7f02885e59915a461e7de307cfd6239f856b89aa63e80b906a]
- The security screen proxy contract specifies HTTPS POSTs with a JSON body carrying text, hook (user_input or tool_response), and chunk metadata; providers return score and threshold in 0..1 plus an optional primary_outcome label. [@claim:clm_bc394e17d63d26b10dcec08cac4001456b5f19e3fcb1c1561f02e943025dd2fe]
- Contract v1 defines a committed, portable deployment directory whose sole interpreter is the qm CLI, which validates the same inputs it uses to render containers, task definitions, secret routing, and the agent-computer layer. [@claim:clm_c341709600308201865df64c31a5134c6de266aded16baee1cdd5b230a20ab34]
<!-- rcw:end owner=source:src_352b0e355cbd54268718831d36e39e0e block=evidence -->

## Researcher notes

