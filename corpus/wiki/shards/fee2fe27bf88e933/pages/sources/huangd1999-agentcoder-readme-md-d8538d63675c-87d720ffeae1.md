---
access: public
aliases: []
claim_ids:
- clm_026c388a6cfaaa27139d753318104c6fae5ead1457fbb38a2c2bf15900aebc07
- clm_284070a83e09564b6e42041f2eb8c98e3a2da030488b8a9754a58fc49a5b0843
- clm_2f11c1c8f8f8a8a785bd81091710e8369689d3e6de1c56404fd55843744cd04d
- clm_3030facb7d9bf638d7b49be9b44400608dd4e490b6224cd2d56f1c2eae58810b
- clm_3f1c514d0b3fa75b44483abf057b981bcd836ccd2cf26766bcfc40edd8e00b01
- clm_a984b8679dfd25a98f0630720e927103217f8f80664791969211887568273126
- clm_e3d407d2626e6340a05d872938c80062b9768ea340e8e91bd0e8d53f6a49d62a
- clm_e5c8550fce86c7adf371cbb6154774307b874fdd9fa5bbe4b647947d6c7a0927
- clm_f7ea061b51274c450114992125839cc6e3c2fc9c390351683b7f12f600ed7f1a
- clm_ff2f9c04f54d2c8ee8cc2ff154021ee32f55c1ac77f304d0ec986bb4f455827e
maturity: draft
page_id: pg_e14fbe597c405c91bd4587d720ffeae1
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_83b5c28433aa557d9fdcce8ded1c7da9
title: huangd1999/AgentCoder/README.md @ d8538d63675c
updated_at: '2026-09-14T02:04:23Z'
---

# huangd1999/AgentCoder/README.md @ d8538d63675c

<!-- rcw:begin owner=source:src_83b5c28433aa557d9fdcce8ded1c7da9 block=evidence -->
- The installation instructions clone the THUDM/CodeGeeX repository, suggesting CodeGeeX is used as part of the setup, though its role is not stated in the evidence. [@claim:clm_026c388a6cfaaa27139d753318104c6fae5ead1457fbb38a2c2bf15900aebc07]
- The README describes a modular structure intended to allow easy integration with advanced models and future enhancements. [@claim:clm_284070a83e09564b6e42041f2eb8c98e3a2da030488b8a9754a58fc49a5b0843]
- The project is released under the MIT License and acknowledges AIOHUB for funding and support. [@claim:clm_2f11c1c8f8f8a8a785bd81091710e8369689d3e6de1c56404fd55843744cd04d]
- Script names referencing humaneval and mbpp suggest the framework targets the HumanEval and MBPP code generation benchmarks. [@claim:clm_3030facb7d9bf638d7b49be9b44400608dd4e490b6224cd2d56f1c2eae58810b]
- Installation involves cloning the repo (plus CodeGeeX), running pip install -r requirements.txt, and adding an API key to a .env file. [@claim:clm_3f1c514d0b3fa75b44483abf057b981bcd836ccd2cf26766bcfc40edd8e00b01]
- The test designer agent generates diverse, objective test cases independently of code generation, and the test executor runs them against generated code to feed refinement feedback. [@claim:clm_a984b8679dfd25a98f0630720e927103217f8f80664791969211887568273126]
- The project requires an OpenAI or similar third-party provider API key, configured in a .env file as OPENAI_API_KEY. [@claim:clm_e3d407d2626e6340a05d872938c80062b9768ea340e8e91bd0e8d53f6a49d62a]
- The framework comprises three specialized agents: a programmer agent, a test designer agent, and a test executor agent that collaborate in an iterative feedback loop. [@claim:clm_e5c8550fce86c7adf371cbb6154774307b874fdd9fa5bbe4b647947d6c7a0927]
- Usage is via per-benchmark scripts: programmer_[humaneval/mbpp].py, test_designer_[humaneval/mbpp].py, and test_executor_[humaneval/mbpp].py. [@claim:clm_f7ea061b51274c450114992125839cc6e3c2fc9c390351683b7f12f600ed7f1a]
- The README invites contributions via GitHub issues or pull requests. [@claim:clm_ff2f9c04f54d2c8ee8cc2ff154021ee32f55c1ac77f304d0ec986bb4f455827e]
<!-- rcw:end owner=source:src_83b5c28433aa557d9fdcce8ded1c7da9 block=evidence -->

## Researcher notes

