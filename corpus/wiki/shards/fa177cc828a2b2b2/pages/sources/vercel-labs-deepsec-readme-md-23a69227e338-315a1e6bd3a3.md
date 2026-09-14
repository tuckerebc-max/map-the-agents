---
access: public
aliases: []
claim_ids:
- clm_41663151cac87722586eb3112a3d9ca5d0244b2c5ce391fef28f9e27db391c62
- clm_4515bc54b8dea6324ec52352965a33d705d16f5b71fc42048f809b5d9dcbd3be
- clm_5351b712cea0ec0447ec8a87642522e69f09ec3ab43f435e88448376e24c5907
- clm_9f355c8aff5522ff4e5fff4d92c2cdf6af4521e831cb6e1ae00c01db6135e1ae
- clm_b1249a365f93e8b24fc9c9eb9018cf0fec5f9eec118efbabafb3169fab884ae6
- clm_b2dfed48c617a9f5d12e5edd6b4643f2bcadeb989857841d6c018705cfcd7d0d
- clm_b37ec0fefb68564ecfa35c738009ab786ebd3dad642e86daf6f01dc594b706e8
- clm_b6bed49895eecebc40b35a02a6ad4fc03946a9346b3a4d1fc1919a1ddbba76ec
- clm_cf77ee141d897b14cc35dd32e20cbd72396bd21915c0650cb9c4a8b573b60d40
- clm_d1e35c69c040e76a282f80e6fb2785a1dc796ff0e0cafbf8609435a4aaa46688
maturity: draft
page_id: pg_c4d59b694483528392b7315a1e6bd3a3
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_ad7fe86ac0ca5d07be8665481b82df3a
title: vercel-labs/deepsec/README.md @ 23a69227e338
updated_at: '2026-09-14T04:30:27Z'
---

# vercel-labs/deepsec/README.md @ 23a69227e338

<!-- rcw:begin owner=source:src_ad7fe86ac0ca5d07be8665481b82df3a block=evidence -->
- Because it uses top models at maximum thinking levels by default, scans of large codebases can cost thousands to tens of thousands of dollars, per the README's own cost warning. [@claim:clm_41663151cac87722586eb3112a3d9ca5d0244b2c5ce391fef28f9e27db391c62]
- The CLI exposes subcommands including scan, process, process --diff, triage, revalidate, enrich, report, export, metrics, status, and sandbox for running any command on Vercel Sandbox microVMs. [@claim:clm_4515bc54b8dea6324ec52352965a33d705d16f5b71fc42048f809b5d9dcbd3be]
- deepsec is an agent-powered vulnerability scanner that runs in the user's own infrastructure and is optimized for on-demand review of all code in large existing repositories. [@claim:clm_5351b712cea0ec0447ec8a87642522e69f09ec3ab43f435e88448376e24c5907]
- Large monorepos can optionally fan work across Vercel Sandbox microVMs; the local working tree is tarballed and uploaded (excluding .git), and model credentials stay host-side and are injected only at the egress host. [@claim:clm_9f355c8aff5522ff4e5fff4d92c2cdf6af4521e831cb6e1ae00c01db6135e1ae]
- deepsec targets teams wanting deep, long-running vulnerability review of large existing codebases, with per-finding triage (~1 cent per finding) and revalidation priced comparably to the AI process stage. [@claim:clm_b1249a365f93e8b24fc9c9eb9018cf0fec5f9eec118efbabafb3169fab884ae6]
- The security model treats deepsec like a coding agent with full shell access on its host environment; in sandbox mode, agent API keys are injected outside the sandbox and worker egress is limited to coding-agent hosts. [@claim:clm_b2dfed48c617a9f5d12e5edd6b4643f2bcadeb989857841d6c018705cfcd7d0d]
- By default model calls route through Vercel AI Gateway; users can instead bring their own OpenAI, Anthropic, or custom HTTPS provider key via --model-auth direct with --ai-provider and --ai-api-key-env. [@claim:clm_b37ec0fefb68564ecfa35c738009ab786ebd3dad642e86daf6f01dc594b706e8]
- Only the name of the environment variable holding the model key is stored, never the key value itself; setup-state evidence likewise contains no credential values. [@claim:clm_b6bed49895eecebc40b35a02a6ad4fc03946a9346b3a4d1fc1919a1ddbba76ec]
- For large codebases, work fans out across worker machines in parallel, and interrupted or errored runs can be re-run to resume, skipping already-analyzed files. [@claim:clm_cf77ee141d897b14cc35dd32e20cbd72396bd21915c0650cb9c4a8b573b60d40]
- The README warns of prompt-injection risk from external dependencies or vendored code even though the tool is designed to run on trusted source code. [@claim:clm_d1e35c69c040e76a282f80e6fb2785a1dc796ff0e0cafbf8609435a4aaa46688]
<!-- rcw:end owner=source:src_ad7fe86ac0ca5d07be8665481b82df3a block=evidence -->

## Researcher notes

