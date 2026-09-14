---
access: public
aliases: []
claim_ids:
- clm_0e4c68c55bc086e9e46ff6810ae365a3b7b08fb71cc454ad4734515ae4b16b4e
- clm_314e8e526daeb73cac57a3faa2e35a795b9a57ae5ccf9b4ba7444e69ade76c96
- clm_8752994f192f36c00576c975dd0610ff2150b9bc7aa07a4e448be047b11596a7
- clm_96cf7bbea9574367a22df3f9f87ee918392a2122c8322c91ab82c8c990096f1f
- clm_b9791d56140c2af904f104fcfccc03828779718c0bfc688a94a359169c36da58
maturity: draft
page_id: pg_ce2dcfb3628353bab1a829db943e7ef9
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_a1d4cc1b8c3b514fb295c028808325ee
title: microsoft/TaskWeaver/website/docs/code_execution.md @ d44ddef23f90
updated_at: '2026-09-14T04:09:13Z'
---

# microsoft/TaskWeaver/website/docs/code_execution.md @ d44ddef23f90

<!-- rcw:begin owner=source:src_a1d4cc1b8c3b514fb295c028808325ee block=evidence -->
- The execution mode is configured via the execution_service.kernel_mode parameter in taskweaver_config.json, with 'container' as the default value. [@claim:clm_0e4c68c55bc086e9e46ff6810ae365a3b7b08fb71cc454ad4734515ae4b16b4e]
- Container mode has documented limitations: slower startup, limited host access with only the session workspace directory mounted (files must be uploaded via /upload or the web upload button), and packages must be added to the Dockerfile and image rebuilt. [@claim:clm_314e8e526daeb73cac57a3faa2e35a795b9a57ae5ccf9b4ba7444e69ade76c96]
- Code execution supports 'local' and 'container' modes; container mode (the default) runs code in a Docker container for a more secure environment, while local mode runs code as a subprocess and could let malicious users or LLM-generated code harm the host. [@claim:clm_8752994f192f36c00576c975dd0610ff2150b9bc7aa07a4e448be047b11596a7]
- The default executor Docker image contains only dependencies from requirements.txt; users needing extra packages must modify the Dockerfile at TaskWeaver/docker/ces_container/Dockerfile and rebuild. [@claim:clm_96cf7bbea9574367a22df3f9f87ee918392a2122c8322c91ab82c8c990096f1f]
- Generated code is executed via a Jupyter Kernel, chosen as a well-established interactive computing tool supporting many languages. [@claim:clm_b9791d56140c2af904f104fcfccc03828779718c0bfc688a94a359169c36da58]
<!-- rcw:end owner=source:src_a1d4cc1b8c3b514fb295c028808325ee block=evidence -->

## Researcher notes

