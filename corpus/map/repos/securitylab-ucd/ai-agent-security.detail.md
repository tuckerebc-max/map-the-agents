# securitylab-ucd/ai-agent-security -- full detail

[Back to orientation](ai-agent-security.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/securitylab-ucd/ai-agent-security/0726a3d2acc1caada53302420b3050d6fe30427d/c035044634a6fb0e.json](../../../wiki/dossiers/securitylab-ucd/ai-agent-security/0726a3d2acc1caada53302420b3050d6fe30427d/c035044634a6fb0e.json)

## specifications (1 claim(s))

- [observation/documented] The repository holds source code for the encryption-defense demos presented in the paper 'Security of AI Agents'; sandbox defense and evaluation code lives in a separate AgentBench fork. -- evidence: [README.md#L2-L4](https://github.com/SecurityLab-UCD/ai-agent-security/blob/0726a3d2acc1caada53302420b3050d6fe30427d/README.md#L2-L4) (`clm_2c5e692eee0daab06957447367d6576be4cc3fe312dc2ac9d0e0ddf170ab9329`)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (1 claim(s))

- [observation/documented] Demo prompts are phrased as 'number' rather than 'SSN' or 'social security number' to avoid triggering alignment; users can request digit groups such as the first three or last four digits. -- evidence: [README.md#L40-L40](https://github.com/SecurityLab-UCD/ai-agent-security/blob/0726a3d2acc1caada53302420b3050d6fe30427d/README.md#L40-L40), [README.md#L38-L38](https://github.com/SecurityLab-UCD/ai-agent-security/blob/0726a3d2acc1caada53302420b3050d6fe30427d/README.md#L38-L38) (`clm_d6ffae61d23efbe51e66f5a9dcfd9deb7756af95e57d9a376bc2a7e9b7125552`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: setup involves sourcing env.sh from the repo root so Python can find the project's modules, installing dependencies via pip from requirements.txt, and generating homomorphic-encryption data with HE_data.py. -- evidence: [README.md#L20-L24](https://github.com/SecurityLab-UCD/ai-agent-security/blob/0726a3d2acc1caada53302420b3050d6fe30427d/README.md#L20-L24), [README.md#L15-L18](https://github.com/SecurityLab-UCD/ai-agent-security/blob/0726a3d2acc1caada53302420b3050d6fe30427d/README.md#L15-L18), [README.md#L10-L13](https://github.com/SecurityLab-UCD/ai-agent-security/blob/0726a3d2acc1caada53302420b3050d6fe30427d/README.md#L10-L13) (`clm_0badc85af3f321ddc521abe2a60a34261fb4b0557c3484506128f36b0789b33b`)
- [observation/documented] Repository development practice: tests are executed with 'pytest tests/*' after generating ciphertext files via HE_data.py. -- evidence: [README.md#L53-L54](https://github.com/SecurityLab-UCD/ai-agent-security/blob/0726a3d2acc1caada53302420b3050d6fe30427d/README.md#L53-L54), [README.md#L56-L56](https://github.com/SecurityLab-UCD/ai-agent-security/blob/0726a3d2acc1caada53302420b3050d6fe30427d/README.md#L56-L56), [README.md#L59-L60](https://github.com/SecurityLab-UCD/ai-agent-security/blob/0726a3d2acc1caada53302420b3050d6fe30427d/README.md#L59-L60) (`clm_7973253d3e189c0fcb30bc65d07da6c16364e570c4d2e6e6a32ff466d52f94fb`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The SSN agent demo is run as a CLI: python agents/ssn_agent.py with --model, --user_id, --ssns_path, and --secretkeys_path arguments. -- evidence: [README.md#L33-L36](https://github.com/SecurityLab-UCD/ai-agent-security/blob/0726a3d2acc1caada53302420b3050d6fe30427d/README.md#L33-L36) (`clm_127cfd58a56a3aeede02c4b4ec2c677e0b6981b6740badde6427e9c736a3c065`)
- [observation/documented] The homomorphic-encryption agent demo is run via python agents/HE_agent.py with a --model argument, and prompts must specify 'sum' or 'product' for postprocessing reasons. -- evidence: [README.md#L43-L47](https://github.com/SecurityLab-UCD/ai-agent-security/blob/0726a3d2acc1caada53302420b3050d6fe30427d/README.md#L43-L47) (`clm_f856132cafa923d5c70a54335ce520f9e25981d05dfdd843453d9643571e4d25`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (3 claim(s))

- [observation/documented] The project requires Python 3.8 or above. -- evidence: [README.md#L7-L7](https://github.com/SecurityLab-UCD/ai-agent-security/blob/0726a3d2acc1caada53302420b3050d6fe30427d/README.md#L7-L7) (`clm_6768499d5cc4a591c8cd7ca1394ad078e77bbc2a21178809c0632604971081b7`)
- [observation/documented] Pinned dependencies include langchain 0.1.16, langchain-openai 0.1.6, pyffx 0.3.0, and a git-installed py-fhe library; test dependencies are hypothesis 6.100.1 and pytest 8.1.1. -- evidence: [requirements.txt#L6-L7](https://github.com/SecurityLab-UCD/ai-agent-security/blob/0726a3d2acc1caada53302420b3050d6fe30427d/requirements.txt#L6-L7), [requirements.txt#L1-L4](https://github.com/SecurityLab-UCD/ai-agent-security/blob/0726a3d2acc1caada53302420b3050d6fe30427d/requirements.txt#L1-L4) (`clm_291426203a35c05d66fbffcdc507d199e961a8fbf1e3b8e70cd9ecf3c42b24c3`)
- [observation/documented] Running agents that use OpenAI LLMs for reasoning requires setting the OPENAI_API_KEY environment variable beforehand. -- evidence: [README.md#L27-L30](https://github.com/SecurityLab-UCD/ai-agent-security/blob/0726a3d2acc1caada53302420b3050d6fe30427d/README.md#L27-L30) (`clm_9784971201c07f452508fb0fbc288ff74e955215f309def072c977f308281582`)

## limitations (2 claim(s))

- [observation/documented] The default encryptor cannot handle numbers greater than 400, so calculation results must stay within 0 to 400 inclusive; the limit is configurable in HE_data/HE_data.py. -- evidence: [README.md#L43-L47](https://github.com/SecurityLab-UCD/ai-agent-security/blob/0726a3d2acc1caada53302420b3050d6fe30427d/README.md#L43-L47) (`clm_2d969264323ee9a1a59a71c7adfbfc02cbe87bc3aba00cd37c799b2ec87d8b42`)
- [observation/documented] A known bug in the HE demo: the LLM indexes the wrong item unless the first index written in the prompt is 0. -- evidence: [README.md#L49-L50](https://github.com/SecurityLab-UCD/ai-agent-security/blob/0726a3d2acc1caada53302420b3050d6fe30427d/README.md#L49-L50) (`clm_d63e3035be929502c9550d488610ffbb12c5033071fd83f35c43c04deb2197d8`)

## relevance (1 claim(s))

- [observation/documented] The work is associated with a RAIE 2025 workshop paper by He, Wang, Rong, Cheng, and Chen, with a DOI linking to arXiv 2406.08689. -- evidence: [README.md#L64-L73](https://github.com/SecurityLab-UCD/ai-agent-security/blob/0726a3d2acc1caada53302420b3050d6fe30427d/README.md#L64-L73) (`clm_8b13d7cb25e229ffcc0b5ba5586d4e7f4e34be83e615f8e1c4bc0e2ae4a2d577`)

