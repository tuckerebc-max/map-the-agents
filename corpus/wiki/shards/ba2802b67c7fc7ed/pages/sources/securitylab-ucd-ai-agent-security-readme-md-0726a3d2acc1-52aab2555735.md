---
access: public
aliases: []
claim_ids:
- clm_0badc85af3f321ddc521abe2a60a34261fb4b0557c3484506128f36b0789b33b
- clm_127cfd58a56a3aeede02c4b4ec2c677e0b6981b6740badde6427e9c736a3c065
- clm_2c5e692eee0daab06957447367d6576be4cc3fe312dc2ac9d0e0ddf170ab9329
- clm_2d969264323ee9a1a59a71c7adfbfc02cbe87bc3aba00cd37c799b2ec87d8b42
- clm_6768499d5cc4a591c8cd7ca1394ad078e77bbc2a21178809c0632604971081b7
- clm_7973253d3e189c0fcb30bc65d07da6c16364e570c4d2e6e6a32ff466d52f94fb
- clm_8b13d7cb25e229ffcc0b5ba5586d4e7f4e34be83e615f8e1c4bc0e2ae4a2d577
- clm_9784971201c07f452508fb0fbc288ff74e955215f309def072c977f308281582
- clm_d63e3035be929502c9550d488610ffbb12c5033071fd83f35c43c04deb2197d8
- clm_d6ffae61d23efbe51e66f5a9dcfd9deb7756af95e57d9a376bc2a7e9b7125552
- clm_f856132cafa923d5c70a54335ce520f9e25981d05dfdd843453d9643571e4d25
maturity: draft
page_id: pg_7e5a5fe786485630a42152aab2555735
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_4105a096beea5ebba680bb4fc6c9248d
title: SecurityLab-UCD/ai-agent-security/README.md @ 0726a3d2acc1
updated_at: '2026-09-14T04:20:52Z'
---

# SecurityLab-UCD/ai-agent-security/README.md @ 0726a3d2acc1

<!-- rcw:begin owner=source:src_4105a096beea5ebba680bb4fc6c9248d block=evidence -->
- Repository development practice: setup involves sourcing env.sh from the repo root so Python can find the project's modules, installing dependencies via pip from requirements.txt, and generating homomorphic-encryption data with HE_data.py. [@claim:clm_0badc85af3f321ddc521abe2a60a34261fb4b0557c3484506128f36b0789b33b]
- The SSN agent demo is run as a CLI: python agents/ssn_agent.py with --model, --user_id, --ssns_path, and --secretkeys_path arguments. [@claim:clm_127cfd58a56a3aeede02c4b4ec2c677e0b6981b6740badde6427e9c736a3c065]
- The repository holds source code for the encryption-defense demos presented in the paper 'Security of AI Agents'; sandbox defense and evaluation code lives in a separate AgentBench fork. [@claim:clm_2c5e692eee0daab06957447367d6576be4cc3fe312dc2ac9d0e0ddf170ab9329]
- The default encryptor cannot handle numbers greater than 400, so calculation results must stay within 0 to 400 inclusive; the limit is configurable in HE_data/HE_data.py. [@claim:clm_2d969264323ee9a1a59a71c7adfbfc02cbe87bc3aba00cd37c799b2ec87d8b42]
- The project requires Python 3.8 or above. [@claim:clm_6768499d5cc4a591c8cd7ca1394ad078e77bbc2a21178809c0632604971081b7]
- Repository development practice: tests are executed with 'pytest tests/*' after generating ciphertext files via HE_data.py. [@claim:clm_7973253d3e189c0fcb30bc65d07da6c16364e570c4d2e6e6a32ff466d52f94fb]
- The work is associated with a RAIE 2025 workshop paper by He, Wang, Rong, Cheng, and Chen, with a DOI linking to arXiv 2406.08689. [@claim:clm_8b13d7cb25e229ffcc0b5ba5586d4e7f4e34be83e615f8e1c4bc0e2ae4a2d577]
- Running agents that use OpenAI LLMs for reasoning requires setting the OPENAI_API_KEY environment variable beforehand. [@claim:clm_9784971201c07f452508fb0fbc288ff74e955215f309def072c977f308281582]
- A known bug in the HE demo: the LLM indexes the wrong item unless the first index written in the prompt is 0. [@claim:clm_d63e3035be929502c9550d488610ffbb12c5033071fd83f35c43c04deb2197d8]
- Demo prompts are phrased as 'number' rather than 'SSN' or 'social security number' to avoid triggering alignment; users can request digit groups such as the first three or last four digits. [@claim:clm_d6ffae61d23efbe51e66f5a9dcfd9deb7756af95e57d9a376bc2a7e9b7125552]
- The homomorphic-encryption agent demo is run via python agents/HE_agent.py with a --model argument, and prompts must specify 'sum' or 'product' for postprocessing reasons. [@claim:clm_f856132cafa923d5c70a54335ce520f9e25981d05dfdd843453d9643571e4d25]
<!-- rcw:end owner=source:src_4105a096beea5ebba680bb4fc6c9248d block=evidence -->

## Researcher notes

