---
access: public
aliases: []
claim_ids:
- clm_00cbf53e041ad2c71b479f6488fec4ed06893a8265f5fcf04ca144c5f5b21ae9
- clm_3afe4e2d8e5f35702c43bfb93eb313da7292f0f5e44c24c3472943235e12920e
- clm_3f36762e7d8348e18228f2171001b9db21066ccd1d541a977a2c644024229496
- clm_545233f2a39450e38275aa1ab70ae63eb6ae5a08a72dfa6c055b1c3dbb503b81
- clm_5c4af4511258de7e8f440e7db44946b6f056676b2c3c540d2591b1de525d9a4c
- clm_95a6942bf56ea442fda37fc0594b27def9d7ad04396ad166022ac7b97a3a9d18
- clm_994851ec715d13bd3c17e01cb8f590fa504145cccfc2362879a238a9127a0f32
- clm_a5d89c1cde16839702308dc926c5836aadccf59c9976fa17934353a8ad57849f
- clm_add6e19d55c26b3f7c801e06a31a1216fd1970c21d0aee6985264a8504c42436
- clm_bf1e31097c7f7ac3c7459e853ab82e050333204a269aca69483544a69153f16b
- clm_c8d038ec93fd1091ae882d8b70dc3c15e88e282dd939741e8dd21543680279ba
- clm_cf1a8d962204e8374ea03d3b2a881622201ee68dd81a27d8b812d4cdeae5c923
maturity: draft
page_id: pg_97a2e60f05b6576495f54f60de47f337
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_d8ec9606c4bf54bdb578c4e50ad21c00
title: Pythagora-io/gpt-pilot/README.md @ 9b763fdaf002
updated_at: '2026-09-14T02:32:47Z'
---

# Pythagora-io/gpt-pilot/README.md @ 9b763fdaf002

<!-- rcw:begin owner=source:src_d8ec9606c4bf54bdb578c4e50ad21c00 block=evidence -->
- GPT Pilot codes the app step by step with the developer in the loop, debugging issues as they arise, in contrast to similar tools that output an entire codebase at once. [@claim:clm_00cbf53e041ad2c71b479f6488fec4ed06893a8265f5fcf04ca144c5f5b21ae9]
- GPT Pilot filters code shown to the LLM so each conversation contains only code relevant to the current task rather than the entire codebase, aiming to work at any scale. [@claim:clm_3afe4e2d8e5f35702c43bfb93eb313da7292f0f5e44c24c3472943235e12920e]
- Generated code is stored in a workspace folder named after the app name entered at startup; config.json (copied from example-config.json) holds LLM provider keys/endpoints and optional fs.ignore_paths. [@claim:clm_3f36762e7d8348e18228f2171001b9db21066ccd1d541a977a2c644024229496]
- GPT Pilot is the core technology for the Pythagora VS Code extension, positioned as an AI developer that can write full features, debug them, and ask for review. [@claim:clm_545233f2a39450e38275aa1ab70ae63eb6ae5a08a72dfa6c055b1c3dbb503b81]
- SQLite is the default database; PostgreSQL support requires additionally installing asyncpg and psycopg2 and setting db.url to a postgresql+asyncpg:// URL in config.json. [@claim:clm_5c4af4511258de7e8f440e7db44946b6f056676b2c3c540d2591b1de525d9a4c]
- The repository is no longer actively maintained, which the notice says is why the malicious commit went unnoticed; the notice and file removals are a security cleanup, not a resumption of development. [@claim:clm_95a6942bf56ea442fda37fc0594b27def9d7ad04396ad166022ac7b97a3a9d18]
- A credential-stealing supply-chain worm was hidden in core/telemetry/ from August 2025 until 11 June 2026; users who cloned and ran GPT Pilot from source in that window are told to rotate credentials. [@claim:clm_994851ec715d13bd3c17e01cb8f590fa504145cccfc2362879a238a9127a0f32]
- Documented warnings state that resuming from a specific step deletes all progress after that step, and that deleting a project cannot be undone. [@claim:clm_a5d89c1cde16839702308dc926c5836aadccf59c9976fa17934353a8ad57849f]
- The malicious commit added a hidden loader (core/telemetry/_hooks.py) wired via core/telemetry/__init__.py that downloaded the Bun runtime to execute an obfuscated payload (core/telemetry/_runtime.bin) harvesting cloud/AWS keys, GitHub and npm tokens, and SSH keys. [@claim:clm_add6e19d55c26b3f7c801e06a31a1216fd1970c21d0aee6985264a8504c42436]
- The Architect agent checks whether the app's technologies are installed on the machine and installs them if not. [@claim:clm_bf1e31097c7f7ac3c7459e853ab82e050333204a269aca69483544a69153f16b]
- The app-building pipeline uses named agents including Specification Writer, Architect, Tech Lead, Developer, Code Monkey, Reviewer, Troubleshooter, Debugger, and Technical Writer. [@claim:clm_c8d038ec93fd1091ae882d8b70dc3c15e88e282dd939741e8dd21543680279ba]
- The CLI supports listing projects (--list), resuming a project or a specific step (--project <app_id> [--step <step>]), deleting a project (--delete <app_id>), and --help for all options. [@claim:clm_cf1a8d962204e8374ea03d3b2a881622201ee68dd81a27d8b812d4cdeae5c923]
<!-- rcw:end owner=source:src_d8ec9606c4bf54bdb578c4e50ad21c00 block=evidence -->

## Researcher notes

