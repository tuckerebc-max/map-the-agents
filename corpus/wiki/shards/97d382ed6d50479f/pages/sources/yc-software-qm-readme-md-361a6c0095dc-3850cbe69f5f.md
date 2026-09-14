---
access: public
aliases: []
claim_ids:
- clm_0d76cf275a7ab00269188349f6ed6b173d09fa3946a2a3c36026c0c450792ba6
- clm_1d5847e861a37f4714dd5d00d846e7b7da4cd4e41e6f7fa42521b4556afb6dac
- clm_29aa8bc90c4bf89f650bd770b65d2349abdf5faa8c416e6bf36e6e42e4c38eac
- clm_2d3163258b3cb69d281475a7278c4258dc53f6d95f2bd230ba8cca327ec5cafe
- clm_43e6a44524b7999ec69c6d1db772b7d4218d73c0c963af9c71d73aab299ba7b2
- clm_5c836b847b7e0f4edbd516f67e78bbcaa02aea4a7251d2238130b83df29470eb
- clm_5e0d041a5aa6b71618416834fe147649eb2775be6a8cabd03377f5bc14518709
- clm_8408746c8d3f5d30f6274d9328670bc6678f2b5d2655b0a91a5389df213a2c69
- clm_8947e8289a18c308863022fa4ba22b2954b24763433d2e5e7c71e68cb1e387de
- clm_c773afaf2ffa741e5aa121747236680e3d16a014ecd9c10f95180112a860bc8c
- clm_eb912c2843273e979dd2af371249a486799ed49a714c7ecdb915181ae3d13305
maturity: draft
page_id: pg_f0d0986791c05cc9969c3850cbe69f5f
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_aa7699a5d8a05d50b92ea81e54e642c3
title: yc-software/qm/README.md @ 361a6c0095dc
updated_at: '2026-09-14T03:24:57Z'
---

# yc-software/qm/README.md @ 361a6c0095dc

<!-- rcw:begin owner=source:src_aa7699a5d8a05d50b92ea81e54e642c3 block=evidence -->
- Without DATABASE_URL and SESSION_STORE=postgres, sessions live in process memory and vanish on restart; Postgres otherwise holds user data, session history, and durable state. [@claim:clm_0d76cf275a7ab00269188349f6ed6b173d09fa3946a2a3c36026c0c450792ba6]
- The core runs TypeScript directly on Node with Fastify for HTTP; the Slack plugin uses Bolt, and the web UI builds with Vite and renders with Lit. [@claim:clm_1d5847e861a37f4714dd5d00d846e7b7da4cd4e41e6f7fa42521b4556afb6dac]
- Repository development practice: contributions are accepted as human-written text, not code — contributors describe changes informally in a .txt or .md file under adrs/, and maintainers handle implementation; vulnerabilities are reported privately. [@claim:clm_29aa8bc90c4bf89f650bd770b65d2349abdf5faa8c416e6bf36e6e42e4c38eac]
- Each person and each room gets its own scoped memory, files, keychain view, permissions, crons, web apps, and durable sandbox, so employees work independently while collaborating in channels and projects. [@claim:clm_2d3163258b3cb69d281475a7278c4258dc53f6d95f2bd230ba8cca327ec5cafe]
- Deployments depend on the @yc-software/qm package; the deployment directory's package.json pins the engine at the exact scaffolding version so the directory records which CLI interprets it. [@claim:clm_43e6a44524b7999ec69c6d1db772b7d4218d73c0c963af9c71d73aab299ba7b2]
- Every turn runs through a central core that can use various models and harnesses; the agent has a small fixed tool surface, including execute, which runs commands in the scope's own durable isolated sandbox. [@claim:clm_5c836b847b7e0f4edbd516f67e78bbcaa02aea4a7251d2238130b83df29470eb]
- QM targets startups wanting a company-wide agent: employees get isolated workspaces, collaborate in Slack channels and projects, and the same identity and configuration carries between Slack and the web app. [@claim:clm_5e0d041a5aa6b71618416834fe147649eb2775be6a8cabd03377f5bc14518709]
- In Open sharing posture, included memories are loaded into the prompt in full with source-scope labels and are searchable, with no relevance ranking applied; the candidate window is 100 recent sessions and 200 files. [@claim:clm_8408746c8d3f5d30f6274d9328670bc6678f2b5d2655b0a91a5389df213a2c69]
- A predeclared command policy with approval rules and hard denials for destructive operations like recursive deletes applies in every posture, including Dangerous. [@claim:clm_8947e8289a18c308863022fa4ba22b2954b24763433d2e5e7c71e68cb1e387de]
- Orgs pick one security posture — Strict (human approval per tool call), Auto (default; classifier screens provenance-labelled external data), or Dangerous (no screening or pauses) — and narrower scopes can only tighten it. [@claim:clm_c773afaf2ffa741e5aa121747236680e3d16a014ecd9c10f95180112a860bc8c]
- The core is generic: org-specific config, tools, skills, sandbox image, and infrastructure live in a deployment directory, and every substrate (harness, session store, sandbox, memory) sits behind an interface. [@claim:clm_eb912c2843273e979dd2af371249a486799ed49a714c7ecdb915181ae3d13305]
<!-- rcw:end owner=source:src_aa7699a5d8a05d50b92ea81e54e642c3 block=evidence -->

## Researcher notes

