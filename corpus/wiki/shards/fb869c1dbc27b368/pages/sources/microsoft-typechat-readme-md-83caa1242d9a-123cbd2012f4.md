---
access: public
aliases: []
claim_ids:
- clm_05c69a67ddc6f59acf6925fecd08da692e8e4509a1e112e765fd4df62a0289be
- clm_1e965e0095096478658bda15e03ee67bae21f69fe50f67ebd798df3e44983e30
- clm_3b39565381a90c73d1973b5d86ba82d4504246e11cbc9f91e7da9121b5824cdc
- clm_3f97560752a84efde2f19f2f57b465a5a28565a0cd5af09a7c7fbc3754326c52
- clm_532b10bde929022cee04542b26cdb8863958e14e4f4147c9deb75815d8c8a783
- clm_833b73fc6fcb8c19819e08dd75a0cea1cff58094a461d768b704cb27450210ba
- clm_95141e5104f1d5ceb2589152e36b25d1a42396038a93da37f965079cb19d7f0e
- clm_a1ab767e14284b8f7931aaf04f85dc87163584baa15c8e8bf2c3a3fa599e97b6
- clm_e110ca5bc9af171f6664a5f13c876e8ff70e185056b53c30c00ec9d6f873b2bb
maturity: draft
page_id: pg_339434601392578ca2a1123cbd2012f4
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_aed61469778d5f4da9cea1dc23c8db47
title: microsoft/TypeChat/README.md @ 83caa1242d9a
updated_at: '2026-09-14T04:09:15Z'
---

# microsoft/TypeChat/README.md @ 83caa1242d9a

<!-- rcw:begin owner=source:src_aed61469778d5f4da9cea1dc23c8db47 block=evidence -->
- Repository development practice: the project adopts the Microsoft Open Source Code of Conduct, with questions directed to opencode@microsoft.com. [@claim:clm_05c69a67ddc6f59acf6925fecd08da692e8e4509a1e112e765fd4df62a0289be]
- Repository development practice: contributions require agreeing to a Contributor License Agreement, with a CLA bot decorating pull requests to determine status. [@claim:clm_1e965e0095096478658bda15e03ee67bae21f69fe50f67ebd798df3e44983e30]
- After validation, TypeChat summarizes the resulting instance succinctly without using an LLM to confirm alignment with user intent. [@claim:clm_3b39565381a90c73d1973b5d86ba82d4504246e11cbc9f91e7da9121b5824cdc]
- Developers define types representing supported intents, from simple sentiment classification to complex schemas like shopping carts or music apps. [@claim:clm_3f97560752a84efde2f19f2f57b465a5a28565a0cd5af09a7c7fbc3754326c52]
- TypeChat is a library for building natural language interfaces using types, replacing prompt engineering with schema engineering. [@claim:clm_532b10bde929022cee04542b26cdb8863958e14e4f4147c9deb75815d8c8a783]
- TypeChat's pipeline: builds an LLM prompt from the types, validates the response against the schema, and repairs invalid output through further model interaction. [@claim:clm_833b73fc6fcb8c19819e08dd75a0cea1cff58094a461d768b704cb27450210ba]
- The TypeScript/JavaScript package is installed via npm install typechat; Python and C#/.NET variants exist, with .NET hosted in a separate TypeChat.net repository. [@claim:clm_95141e5104f1d5ceb2589152e36b25d1a42396038a93da37f965079cb19d7f0e]
- Example projects live under typescript/examples and can be run locally or in a GitHub Codespace; documentation is hosted at microsoft.github.io/TypeChat. [@claim:clm_a1ab767e14284b8f7931aaf04f85dc87163584baa15c8e8bf2c3a3fa599e97b6]
- Schemas can be extended by adding types to a discriminated union, and made hierarchical via a meta-schema that selects sub-schemas from user input. [@claim:clm_e110ca5bc9af171f6664a5f13c876e8ff70e185056b53c30c00ec9d6f873b2bb]
<!-- rcw:end owner=source:src_aed61469778d5f4da9cea1dc23c8db47 block=evidence -->

## Researcher notes

