---
access: public
aliases: []
claim_ids:
- clm_50499ccadd3f65e0773aafd7f60e9b9dc11f1b682252625cc77d4b79198ad387
- clm_99a809caf63b9e8f81b7f6edefe661816d94d0266f692a25454a85bddb91d39a
- clm_9d96430b9f28b12a2c9e298dd30ec7ef676d2a933610f65f36d3a65735a062e0
- clm_b361640b802f545fec40091cf47135bd73bf41409d313f370b793747cf91f075
maturity: draft
page_id: pg_c2ac5563db4154b2b8cd4256c5be9661
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_b79279bb68605ebeb10af8b8bba2b103
title: AlanChen4/Summer-2024-SWE-Internships/requirements.txt @ 4dd027d006b3
updated_at: '2026-09-14T03:32:49Z'
---

# AlanChen4/Summer-2024-SWE-Internships/requirements.txt @ 4dd027d006b3

<!-- rcw:begin owner=source:src_b79279bb68605ebeb10af8b8bba2b103 block=evidence -->
- Type-stub packages (types-requests, types-urllib3) are pinned alongside mypy, supporting static type checking of requests-based code during development. [@claim:clm_50499ccadd3f65e0773aafd7f60e9b9dc11f1b682252625cc77d4b79198ad387]
- Repository development practice: requirements.txt includes pre-commit 3.3.3, black 23.3.0, and mypy 1.4.1, indicating the project uses pre-commit hooks with formatting and type checking in its development workflow. [@claim:clm_99a809caf63b9e8f81b7f6edefe661816d94d0266f692a25454a85bddb91d39a]
- The project pins exact dependency versions in requirements.txt, including requests 2.31.0, python-dotenv 1.0.0, and PyYAML 6.0. [@claim:clm_9d96430b9f28b12a2c9e298dd30ec7ef676d2a933610f65f36d3a65735a062e0]
- Repository development practice: the presence of nodeenv and virtualenv among pinned packages suggests the pre-commit setup may manage Node-based hooks and isolated environments for contributors. [@claim:clm_b361640b802f545fec40091cf47135bd73bf41409d313f370b793747cf91f075]
<!-- rcw:end owner=source:src_b79279bb68605ebeb10af8b8bba2b103 block=evidence -->

## Researcher notes

