---
access: public
aliases: []
claim_ids:
- clm_046c0a6e0a5d1af08bca75e702ec3c4d2530bd60caf36c85d3923c6d290fa637
- clm_15fb0436c39a19e24c9b79c6ca7854bafdad0e0a00ce4dfa8616107cb93ca7b0
- clm_2ca5c2316937bebc9d8de3e618d020ba99a37b6f0cd8df11f414401fa12b84a4
- clm_68e7fb7b7505587796df7638005783276c414a28a66d1fe96aeddd71f4d52297
- clm_7644cf6ab4f2fb2a412be03388876cb38e50467171ca65774d399ed1cbc3163c
- clm_7a293a8c57aa685022deaf9f24fa830eb428202fe4fe364a16a5a80461a97b12
- clm_88a412ddd9a8647bc6d4fdf655a4d15e02e60f8cff9023c01594671f2934d6ec
- clm_8da806ec88a5b9b09e1e5656a1f9ace793ddcbd6334a34359f1c564f4cdea000
- clm_936ec1081078c657e68c24358c811c53f7dcf5a090f771b3ca47749d03454f8a
- clm_bbb648958a017c3fb6c6e1d341182e35773fb4152c576934ebdbe96781b05868
- clm_c4a4b12f1f15604ad78cf01360ce792e5c8a180bf0776089b8f03a3a1751e756
- clm_f02865e7349fae78db6de377cd6186055c5bd38c4e33153d8608c25c12a16416
- clm_f3d7ee020109e6940489f0bce0bf79b2b4412feb7a2c1631ff983d182da231f7
maturity: draft
page_id: pg_1fc19d5f911356babdea4f0a5ba159e0
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_bc2e5fda244d528ea96fecdc30fd33e8
title: coleam00/Linear-Coding-Agent-Harness/README.md @ c37dc0969930
updated_at: '2026-09-14T01:42:55Z'
---

# coleam00/Linear-Coding-Agent-Harness/README.md @ c37dc0969930

<!-- rcw:begin owner=source:src_bc2e5fda244d528ea96fecdc30fd33e8 block=evidence -->
- The runtime uses a defense-in-depth security model: OS-level sandboxing of bash commands, filesystem restrictions to the project directory, a bash command allowlist, and explicit MCP tool permissions. [@claim:clm_046c0a6e0a5d1af08bca75e702ec3c4d2530bd60caf36c85d3923c6d290fa637]
- The demo implements a two-agent pattern: an initializer agent that sets up the Linear project and issues, and a coding agent that implements them. [@claim:clm_15fb0436c39a19e24c9b79c6ca7854bafdad0e0a00ce4dfa8616107cb93ca7b0]
- The repository includes modules for agent session logic, Claude SDK/MCP client configuration, security validation, progress tracking, prompt loading, and Linear configuration constants, plus prompt files for both agent roles. [@claim:clm_2ca5c2316937bebc9d8de3e618d020ba99a37b6f0cd8df11f414401fa12b84a4]
- The initializer agent reads app_spec.txt, creates a Linear project, generates 50 detailed issues, creates a META issue for session tracking, and sets up project structure, init.sh, and git. [@claim:clm_68e7fb7b7505587796df7638005783276c414a28a66d1fe96aeddd71f4d52297]
- The project requires the Claude Code CLI installed globally via npm and Python dependencies from requirements.txt, which pins claude-code-sdk>=0.0.25. [@claim:clm_7644cf6ab4f2fb2a412be03388876cb38e50467171ca65774d399ed1cbc3163c]
- The entry point is autonomous_agent_demo.py, invoked with --project-dir, with optional --max-iterations (default unlimited) and --model (default claude-opus-4-5-20251101) flags. [@claim:clm_7a293a8c57aa685022deaf9f24fa830eb428202fe4fe364a16a5a80461a97b12]
- Generated projects contain a .linear_project.json marker file holding Linear project state, alongside the copied spec, init.sh, and .claude_settings.json security settings. [@claim:clm_88a412ddd9a8647bc6d4fdf655a4d15e02e60f8cff9023c01594671f2934d6ec]
- The coding agent appears to verify previously completed features and test new ones via Puppeteer browser automation, though no benchmark or success-rate metrics are documented. [@claim:clm_8da806ec88a5b9b09e1e5656a1f9ace793ddcbd6334a34359f1c564f4cdea000]
- All work tracking and inter-agent communication happens through Linear issues, comments, and status transitions rather than local text files. [@claim:clm_936ec1081078c657e68c24358c811c53f7dcf5a090f771b3ca47749d03454f8a]
- The coding agent queries Linear for the highest-priority Todo issue, claims it, implements and tests the feature, comments on the issue, marks it Done, and updates the META issue with a session summary. [@claim:clm_bbb648958a017c3fb6c6e1d341182e35773fb4152c576934ebdbe96781b05868]
- The bash allowlist permits only specific commands such as npm, node, and git, and is configurable via ALLOWED_COMMANDS in security.py. [@claim:clm_c4a4b12f1f15604ad78cf01360ce792e5c8a180bf0776089b8f03a3a1751e756]
- Two MCP servers are used: Linear over Streamable HTTP for issue/status/comment management, and Puppeteer over stdio for browser-based UI testing. [@claim:clm_f02865e7349fae78db6de377cd6186055c5bd38c4e33153d8608c25c12a16416]
- Two environment variables are required at runtime: CLAUDE_CODE_OAUTH_TOKEN (from claude setup-token) and LINEAR_API_KEY for MCP access. [@claim:clm_f3d7ee020109e6940489f0bce0bf79b2b4412feb7a2c1631ff983d182da231f7]
<!-- rcw:end owner=source:src_bc2e5fda244d528ea96fecdc30fd33e8 block=evidence -->

## Researcher notes

