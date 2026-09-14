---
access: public
aliases: []
claim_ids:
- clm_396041a641794214f945b7487fc15568d7f2fbaba9f8d8cb2414e95ec75585e1
- clm_5ac28aad81a5ae6cfe17a91db831a4ac7d2ed9a3e3c3399ae4f4e0ff794fdd89
- clm_60910a6d43a6c3bf0a3b78620a2f083192a2f3c9ab4ee2d91e81752d002e9516
- clm_a571a048c660e12740a4e21bea33f2f7d58b575d9984f971272ff9a0f46a15e4
- clm_e293afa843ba3217a57240a49c50f36ab825309a151c5e2327a4a597a426bb44
- clm_fac63becd8b56d8a01633b936fbf73e6d433f4fa8295809020f0cda8b533c1e8
- clm_fef015d078f924049fc7899d222735f8afbefb677c830d03c13eff7ab6f26ca1
maturity: draft
page_id: pg_253fb7512d345c6ebd8aee62964dd689
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_0c30b6d7b0005bf9a831c3290ce0af2a
title: microsoft/TaskWeaver/README.md @ d44ddef23f90
updated_at: '2026-09-14T04:09:13Z'
---

# microsoft/TaskWeaver/README.md @ d44ddef23f90

<!-- rcw:begin owner=source:src_0c30b6d7b0005bf9a831c3290ce0af2a block=evidence -->
- LLM configuration is provided in a taskweaver_config.json file, e.g. llm.api_key and llm.model for OpenAI, with other LLMs and advanced configurations supported per the docs. [@claim:clm_396041a641794214f945b7487fc15568d7f2fbaba9f8d8cb2414e95ec75585e1]
- TaskWeaver is described as a code-first agent framework for planning and executing data analytics tasks, interpreting user requests as code snippets and coordinating plugin functions in a stateful manner. [@claim:clm_5ac28aad81a5ae6cfe17a91db831a4ac7d2ed9a3e3c3399ae4f4e0ff794fdd89]
- Unlike frameworks that track only chat history, TaskWeaver preserves both chat history and code execution history including in-memory data, which it says helps with complex data like high-dimensional tables. [@claim:clm_60910a6d43a6c3bf0a3b78620a2f083192a2f3c9ab4ee2d91e81752d002e9516]
- The project requires Python 3.10 or 3.11 per its README badge and states Python >= 3.10 is required for installation. [@claim:clm_a571a048c660e12740a4e21bea33f2f7d58b575d9984f971272ff9a0f46a15e4]
- TaskWeaver can be used via a CLI (python -m taskweaver -p ./project/), a Web UI for demos, or imported as a library into existing projects. [@claim:clm_e293afa843ba3217a57240a49c50f36ab825309a151c5e2327a4a597a426bb44]
- Repository development practice: installation from source involves cloning the repo and running pip install -r requirements.txt; earlier versions can be installed from release tags via pip install git+https://github.com/microsoft/TaskWeaver@<TAG>. [@claim:clm_fac63becd8b56d8a01633b936fbf73e6d433f4fa8295809020f0cda8b533c1e8]
- The sql_pull_data example plugin is implemented on top of Langchain and requires installing langchain and tabulate; the forecasting example requires yfinance and statsmodels. [@claim:clm_fef015d078f924049fc7899d222735f8afbefb677c830d03c13eff7ab6f26ca1]
<!-- rcw:end owner=source:src_0c30b6d7b0005bf9a831c3290ce0af2a block=evidence -->

## Researcher notes

