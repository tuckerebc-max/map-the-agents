---
access: public
aliases: []
claim_ids:
- clm_0707f126ddaecea3908de8cce39a5b9d9b743e28a547e1e5dde62cf52a7aa2fe
- clm_0e5c65a5f83a2f8f61e998d1dc8051d28918a78f9111e0b7711ba0aae5150e8c
- clm_139af722d641765e06102a34b79f07fcbd173fd9e1f336b8fe2cf4e055c645e9
- clm_4354df2c66fca2a8a051be85864e2fc8b18947e1e5550c73beedabeb8b226ee0
- clm_626a316d06dbb7623bb1e571087a3af8450e71dc2cc21e998b84bd7b3801d1a2
- clm_679ef622b467298283b7c8bb9e00843c131bb668c3c01447ac8d229363a45304
- clm_6f460a68f770910367b48ae7e4e9f815391d8b7a7b9b45bd3e2fa149886465d2
- clm_709d309b198df576f606e6af6f740b58aead3524c8d51bfaa114081ac1011434
- clm_8f51319fe06d48e12e29f488bae3973f72bbab7ae627bbfd60afe833ce4cb0c3
- clm_a96814219c2c3881607dc4a6d540fffa933bdb3c6484f45011dbcc4af020bc12
maturity: draft
page_id: pg_da8c95e7ddde5aa8aefe929e02aaa77b
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_f1ff546ea227596882f7f4dce678ca93
title: firetix/vibe-coding-penetration-tester/README.md @ 2625ff0bc570
updated_at: '2026-09-14T03:51:28Z'
---

# firetix/vibe-coding-penetration-tester/README.md @ 2625ff0bc570

<!-- rcw:begin owner=source:src_f1ff546ea227596882f7f4dce678ca93 block=evidence -->
- Optional hosted/billing endpoints include GET /api/entitlements, POST /api/billing/checkout, and POST /api/billing/webhook, plus a mock checkout route for local/test setups. [@claim:clm_0707f126ddaecea3908de8cce39a5b9d9b743e28a547e1e5dde62cf52a7aa2fe]
- The modular web app exposes session, scan, activity, logs, and report endpoints such as POST /api/scan/start, POST /api/scan/cancel, and GET /api/report/<report_id>. [@claim:clm_0e5c65a5f83a2f8f61e998d1dc8051d28918a78f9111e0b7711ba0aae5150e8c]
- The tool requires at least one LLM provider: an OpenAI API key, an Anthropic API key, or an Ollama server (default localhost:11434). [@claim:clm_139af722d641765e06102a34b79f07fcbd173fd9e1f336b8fe2cf4e055c645e9]
- The tool is restricted by its own notice to targets the user owns or has explicit authorization to test; unauthorized scanning may violate law and policy. [@claim:clm_4354df2c66fca2a8a051be85864e2fc8b18947e1e5550c73beedabeb8b226ee0]
- The repository includes a CLI entrypoint (main.py), modular Flask web API (run_web.py, web_api/), a legacy web_ui.py, agents/, tools/, and sample reports directories. [@claim:clm_626a316d06dbb7623bb1e571087a3af8450e71dc2cc21e998b84bd7b3801d1a2]
- Scanning is scope-aware with three scope modes: url, domain, and subdomain. [@claim:clm_679ef622b467298283b7c8bb9e00843c131bb668c3c01447ac8d229363a45304]
- The tool coordinates specialized security agents to discover and validate common web vulnerabilities and generates reproducible Markdown and JSON reports. [@claim:clm_6f460a68f770910367b48ae7e4e9f815391d8b7a7b9b45bd3e2fa149886465d2]
- Repository development practice: tests are run via ./run_tests.sh or focused pytest suites (unit, integration, API E2E, frontend E2E, Vercel preview) with markers defined in pytest.ini. [@claim:clm_709d309b198df576f606e6af6f740b58aead3524c8d51bfaa114081ac1011434]
- The CLI accepts --url (required), --model (default gpt-5.2), --provider (openai/anthropic/ollama), --scope, --output, --verbose, and --ollama-url options. [@claim:clm_8f51319fe06d48e12e29f488bae3973f72bbab7ae627bbfd60afe833ce4cb0c3]
- A multi-agent scan workflow covers discovery, planning, and vulnerability testing, with browser automation via Playwright for realistic interaction testing. [@claim:clm_a96814219c2c3881607dc4a6d540fffa933bdb3c6484f45011dbcc4af020bc12]
<!-- rcw:end owner=source:src_f1ff546ea227596882f7f4dce678ca93 block=evidence -->

## Researcher notes

