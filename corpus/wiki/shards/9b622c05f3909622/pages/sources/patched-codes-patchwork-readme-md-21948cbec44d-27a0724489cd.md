---
access: public
aliases: []
claim_ids:
- clm_1bbaba8205ee9df325123990282e47b1a15eb3e5527976716f1c00364c56160f
- clm_507a34e5525d06859c2507d4f1deaee89f176d0a63b70e3be9c8035475eb795d
- clm_686d0ae78a78b7abfa03495ae02af2d265d48d1fa0bd948217215401a41acff4
- clm_72b06c24e0f4a56797a3f1bd8e0e1589b98d7c34e9000f89a1c1714bd239a5fa
- clm_75f6254c08b372942de2c68bb5b36429cb3889e0702246025a87d606ae2d89fc
- clm_802ca562c52decf5f6155c4b3b52df561ea956d672a7b2205962c5aec10351fe
- clm_bcfb9b614523b974f2dc868d667ecd693f46fa6660ac174d75cde8ed6334078c
- clm_eb9b3d058152902a155c12a496f1b71be8082f6ae154e12501d250edcf0aa543
- clm_f3c7c5b3e09dce8e228ddd65d370a6c1f9e3aaf2ad8139393c5482b1f24fc103
- clm_fabbbf3f4b19050237a43e34da3c6ffe92e35dba3c9f299ca5e1ec2c4331fb3e
- clm_fd5514cb5bb578c53202434fd7f5d4a9fd1f940ecfd2d9489b350c8335be030b
maturity: draft
page_id: pg_65ce2fe2258d557190b427a0724489cd
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_40d8d0bdab2757c6bb5b492295d90375
title: patched-codes/patchwork/README.md @ 21948cbec44d
updated_at: '2026-09-14T02:30:21Z'
---

# patched-codes/patchwork/README.md @ 21948cbec44d

<!-- rcw:begin owner=source:src_40d8d0bdab2757c6bb5b492295d90375 block=evidence -->
- Optional pip dependency groups exist: 'security' (semgrep, depscan) required for AutoFix and DependencyUpgrade, 'rag' (chromadb) required for ResolveIssue, 'notifications' for notification steps, and 'all' which installs everything. [@claim:clm_1bbaba8205ee9df325123990282e47b1a15eb3e5527976716f1c00364c56160f]
- Patchwork appears relevant to security automation use cases, since its AutoFix patchflow patches vulnerabilities identified by Semgrep scans and DependencyUpgrade updates dependencies from vulnerable to fixed versions. [@claim:clm_507a34e5525d06859c2507d4f1deaee89f176d0a63b70e3be9c8035475eb795d]
- Repository development practice: contributions for new patchflows, steps, or the core framework are welcomed, with separate instruction documents for creating patchflows and steps, plus a HuggingChat assistant to help author them. [@claim:clm_686d0ae78a78b7abfa03495ae02af2d265d48d1fa0bd948217215401a41acff4]
- Patchflow configuration can be supplied via a --config flag pointing to a directory of patchflow defaults or to a config.yml file specifying keys such as openai_api_key, client_base_url, and model. [@claim:clm_72b06c24e0f4a56797a3f1bd8e0e1589b98d7c34e9000f89a1c1714bd239a5fa]
- Predefined patchflows include GenerateDocstring, AutoFix, PRReview, GenerateREADME, DependencyUpgrade, and ResolveIssue, each linked to its own directory in the repository. [@claim:clm_75f6254c08b372942de2c68bb5b36429cb3889e0702246025a87d606ae2d89fc]
- Installing patchwork-cli without any dependency group installs a core set of dependencies sufficient to run the GenerateDocstring, PRReview, and GenerateREADME patchflows. [@claim:clm_802ca562c52decf5f6155c4b3b52df561ea956d672a7b2205962c5aec10351fe]
- Patchwork supports any OpenAI-compatible endpoint, enabling models from providers like Groq, Together AI, or Hugging Face, and local models via llama.cpp, ollama, vllm, or tgi. [@claim:clm_bcfb9b614523b974f2dc868d667ecd693f46fa6660ac174d75cde8ed6334078c]
- Patchwork is licensed under AGPL-3.0 terms, while the separate patchwork template repository for creating and sharing custom patchflows and steps is licensed under Apache-2.0. [@claim:clm_eb9b3d058152902a155c12a496f1b71be8082f6ae154e12501d250edcf0aa543]
- Patchwork is built from three key components: reusable atomic steps (e.g., create PR, commit changes, call an LLM), customizable prompt templates, and patchflows that combine steps and prompts into automations. [@claim:clm_f3c7c5b3e09dce8e228ddd65d370a6c1f9e3aaf2ad8139393c5482b1f24fc103]
- The CLI runs patchflows with the syntax 'patchwork <PatchFlow> <?Arguments>'; arguments override patchflow attributes as key=value pairs, and valueless keys are treated as boolean True flags. [@claim:clm_fabbbf3f4b19050237a43e34da3c6ffe92e35dba3c9f299ca5e1ec2c4331fb3e]
- Prompt templates use {{}} placeholder variables replaced at each run with data from steps or inputs; each patchflow ships with an optimized default template that users can override via prompt_template_file. [@claim:clm_fd5514cb5bb578c53202434fd7f5d4a9fd1f940ecfd2d9489b350c8335be030b]
<!-- rcw:end owner=source:src_40d8d0bdab2757c6bb5b492295d90375 block=evidence -->

## Researcher notes

