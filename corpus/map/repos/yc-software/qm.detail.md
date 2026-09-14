# yc-software/qm -- full detail

[Back to orientation](qm.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/yc-software/qm/361a6c0095dcd3d156aca91353f3ffba0bb8b69b/da4f0a633de29ba8.json](../../../wiki/dossiers/yc-software/qm/361a6c0095dcd3d156aca91353f3ffba0bb8b69b/da4f0a633de29ba8.json)

## specifications (2 claim(s))

- [observation/documented] Contract v1 defines a committed, portable deployment directory whose sole interpreter is the qm CLI, which validates the same inputs it uses to render containers, task definitions, secret routing, and the agent-computer layer. -- evidence: [docs/deploy-directory.md#L3-L3](https://github.com/yc-software/qm/blob/361a6c0095dcd3d156aca91353f3ffba0bb8b69b/docs/deploy-directory.md#L3-L3) (`clm_c341709600308201865df64c31a5134c6de266aded16baee1cdd5b230a20ab34`)
- [observation/documented] The deployment config root requires contract: 1, orgId, publicUrl, target, and a services list including core; target is docker, fly, or aws, and unknown contract majors fail closed. -- evidence: [docs/deploy-directory.md#L24-L24](https://github.com/yc-software/qm/blob/361a6c0095dcd3d156aca91353f3ffba0bb8b69b/docs/deploy-directory.md#L24-L24) (`clm_0b823cb54ca3e16b3bc83d065b8a0b69569b469f57e00bb763aa81520ba0c97d`)

## components (2 claim(s))

- [observation/documented] A deployment runs three application workloads: core, web-ui (chat plus admin under /admin), and portal, which is the public entry point and hosts the optional built-in auth broker; Slack stays in core. -- evidence: [docs/combined-services.md#L3-L3](https://github.com/yc-software/qm/blob/361a6c0095dcd3d156aca91353f3ffba0bb8b69b/docs/combined-services.md#L3-L3) (`clm_8681a067b467fd47e2bde2d6a36c3bb3bd0cb42ea0d43cb35de964aaecb31ff5`)
- [observation/documented] The core runs TypeScript directly on Node with Fastify for HTTP; the Slack plugin uses Bolt, and the web UI builds with Vite and renders with Lit. -- evidence: [README.md#L87-L88](https://github.com/yc-software/qm/blob/361a6c0095dcd3d156aca91353f3ffba0bb8b69b/README.md#L87-L88) (`clm_1d5847e861a37f4714dd5d00d846e7b7da4cd4e41e6f7fa42521b4556afb6dac`)

## design-choices (2 claim(s))

- [observation/documented] Each person and each room gets its own scoped memory, files, keychain view, permissions, crons, web apps, and durable sandbox, so employees work independently while collaborating in channels and projects. -- evidence: [README.md#L22-L23](https://github.com/yc-software/qm/blob/361a6c0095dcd3d156aca91353f3ffba0bb8b69b/README.md#L22-L23), [README.md#L17-L20](https://github.com/yc-software/qm/blob/361a6c0095dcd3d156aca91353f3ffba0bb8b69b/README.md#L17-L20) (`clm_2d3163258b3cb69d281475a7278c4258dc53f6d95f2bd230ba8cca327ec5cafe`)
- [observation/documented] The core is generic: org-specific config, tools, skills, sandbox image, and infrastructure live in a deployment directory, and every substrate (harness, session store, sandbox, memory) sits behind an interface. -- evidence: [README.md#L90-L94](https://github.com/yc-software/qm/blob/361a6c0095dcd3d156aca91353f3ffba0bb8b69b/README.md#L90-L94) (`clm_eb912c2843273e979dd2af371249a486799ed49a714c7ecdb915181ae3d13305`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: contributions are accepted as human-written text, not code — contributors describe changes informally in a .txt or .md file under adrs/, and maintainers handle implementation; vulnerabilities are reported privately. -- evidence: [README.md#L156-L160](https://github.com/yc-software/qm/blob/361a6c0095dcd3d156aca91353f3ffba0bb8b69b/README.md#L156-L160) (`clm_29aa8bc90c4bf89f650bd770b65d2349abdf5faa8c416e6bf36e6e42e4c38eac`)
- [observation/documented] Repository development practice: the normal deployment gate order is check, doctor, plan, up --yes, then check --live, with infra build-image preceding plan on AWS MicroVM sandboxes. -- evidence: [docs/deploy-directory.md#L122-L122](https://github.com/yc-software/qm/blob/361a6c0095dcd3d156aca91353f3ffba0bb8b69b/docs/deploy-directory.md#L122-L122) (`clm_7d53517883f87e7e9e6ee152531f4f1d1daabcdc0b641fc3592e3057630dafb3`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The security screen proxy contract specifies HTTPS POSTs with a JSON body carrying text, hook (user_input or tool_response), and chunk metadata; providers return score and threshold in 0..1 plus an optional primary_outcome label. -- evidence: [docs/deploy-directory.md#L34-L34](https://github.com/yc-software/qm/blob/361a6c0095dcd3d156aca91353f3ffba0bb8b69b/docs/deploy-directory.md#L34-L34), [docs/deploy-directory.md#L59-L59](https://github.com/yc-software/qm/blob/361a6c0095dcd3d156aca91353f3ffba0bb8b69b/docs/deploy-directory.md#L59-L59), [docs/deploy-directory.md#L61-L67](https://github.com/yc-software/qm/blob/361a6c0095dcd3d156aca91353f3ffba0bb8b69b/docs/deploy-directory.md#L61-L67), [docs/deploy-directory.md#L36-L57](https://github.com/yc-software/qm/blob/361a6c0095dcd3d156aca91353f3ffba0bb8b69b/docs/deploy-directory.md#L36-L57) (`clm_bc394e17d63d26b10dcec08cac4001456b5f19e3fcb1c1561f02e943025dd2fe`)
- [observation/documented] Published apps receive AGENT_API_URL and AGENT_CREDENTIAL_TOKEN and call $AGENT_API_URL/v1/credentials/broker with the token in x-agent-capability, authorizing as the immutable publisher rather than the viewing person. -- evidence: [docs/deploy-directory.md#L151-L157](https://github.com/yc-software/qm/blob/361a6c0095dcd3d156aca91353f3ffba0bb8b69b/docs/deploy-directory.md#L151-L157) (`clm_8e36d303fb7c3b7f02885e59915a461e7de307cfd6239f856b89aa63e80b906a`)

## memory-state (2 claim(s))

- [observation/documented] Without DATABASE_URL and SESSION_STORE=postgres, sessions live in process memory and vanish on restart; Postgres otherwise holds user data, session history, and durable state. -- evidence: [README.md#L70-L73](https://github.com/yc-software/qm/blob/361a6c0095dcd3d156aca91353f3ffba0bb8b69b/README.md#L70-L73), [README.md#L77-L85](https://github.com/yc-software/qm/blob/361a6c0095dcd3d156aca91353f3ffba0bb8b69b/README.md#L77-L85) (`clm_0d76cf275a7ab00269188349f6ed6b173d09fa3946a2a3c36026c0c450792ba6`)
- [observation/documented] In Open sharing posture, included memories are loaded into the prompt in full with source-scope labels and are searchable, with no relevance ranking applied; the candidate window is 100 recent sessions and 200 files. -- evidence: [README.md#L115-L124](https://github.com/yc-software/qm/blob/361a6c0095dcd3d156aca91353f3ffba0bb8b69b/README.md#L115-L124) (`clm_8408746c8d3f5d30f6274d9328670bc6678f2b5d2655b0a91a5389df213a2c69`)

## orchestration (1 claim(s))

- [observation/documented] Every turn runs through a central core that can use various models and harnesses; the agent has a small fixed tool surface, including execute, which runs commands in the scope's own durable isolated sandbox. -- evidence: [README.md#L77-L85](https://github.com/yc-software/qm/blob/361a6c0095dcd3d156aca91353f3ffba0bb8b69b/README.md#L77-L85) (`clm_5c836b847b7e0f4edbd516f67e78bbcaa02aea4a7251d2238130b83df29470eb`)

## tools-permissions (2 claim(s))

- [observation/documented] Orgs pick one security posture — Strict (human approval per tool call), Auto (default; classifier screens provenance-labelled external data), or Dangerous (no screening or pauses) — and narrower scopes can only tighten it. -- evidence: [README.md#L103-L108](https://github.com/yc-software/qm/blob/361a6c0095dcd3d156aca91353f3ffba0bb8b69b/README.md#L103-L108), [README.md#L98-L101](https://github.com/yc-software/qm/blob/361a6c0095dcd3d156aca91353f3ffba0bb8b69b/README.md#L98-L101) (`clm_c773afaf2ffa741e5aa121747236680e3d16a014ecd9c10f95180112a860bc8c`)
- [observation/documented] A predeclared command policy with approval rules and hard denials for destructive operations like recursive deletes applies in every posture, including Dangerous. -- evidence: [README.md#L110-L111](https://github.com/yc-software/qm/blob/361a6c0095dcd3d156aca91353f3ffba0bb8b69b/README.md#L110-L111) (`clm_8947e8289a18c308863022fa4ba22b2954b24763433d2e5e7c71e68cb1e387de`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Deployments depend on the @yc-software/qm package; the deployment directory's package.json pins the engine at the exact scaffolding version so the directory records which CLI interprets it. -- evidence: [README.md#L139-L139](https://github.com/yc-software/qm/blob/361a6c0095dcd3d156aca91353f3ffba0bb8b69b/README.md#L139-L139), [docs/deploy-directory.md#L7-L7](https://github.com/yc-software/qm/blob/361a6c0095dcd3d156aca91353f3ffba0bb8b69b/docs/deploy-directory.md#L7-L7) (`clm_43e6a44524b7999ec69c6d1db772b7d4218d73c0c963af9c71d73aab299ba7b2`)

## limitations (2 claim(s))

- [observation/documented] Admin model verification's small probe does not certify prices, maximum advertised context/output limits, image support, every reasoning level, or correct tool execution; admin-managed API models remain Pi-only in normal use. -- evidence: [docs/admin-model-verification.md#L15-L19](https://github.com/yc-software/qm/blob/361a6c0095dcd3d156aca91353f3ffba0bb8b69b/docs/admin-model-verification.md#L15-L19) (`clm_6284ad912d5f8d58ab3fc76e9db43e1121b25f194b38616f8471c51827bb3907`)
- [observation/documented] The sandbox.egress contract clause is VALIDATED-ONLY: qm check emits wildcard/host warnings, but runtime enforcement of egress is explicitly absent. -- evidence: [docs/deploy-directory.md#L132-L145](https://github.com/yc-software/qm/blob/361a6c0095dcd3d156aca91353f3ffba0bb8b69b/docs/deploy-directory.md#L132-L145), [docs/deploy-directory.md#L147-L147](https://github.com/yc-software/qm/blob/361a6c0095dcd3d156aca91353f3ffba0bb8b69b/docs/deploy-directory.md#L147-L147) (`clm_07be4d77d6df7cdbf7e16516b36ea11732c96e02572ce632f9da338f01417380`)

## relevance (1 claim(s))

- [observation/documented] QM targets startups wanting a company-wide agent: employees get isolated workspaces, collaborate in Slack channels and projects, and the same identity and configuration carries between Slack and the web app. -- evidence: [README.md#L31-L41](https://github.com/yc-software/qm/blob/361a6c0095dcd3d156aca91353f3ffba0bb8b69b/README.md#L31-L41), [README.md#L17-L20](https://github.com/yc-software/qm/blob/361a6c0095dcd3d156aca91353f3ffba0bb8b69b/README.md#L17-L20) (`clm_5e0d041a5aa6b71618416834fe147649eb2775be6a8cabd03377f5bc14518709`)

