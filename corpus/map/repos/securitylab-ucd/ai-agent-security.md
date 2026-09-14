# securitylab-ucd/ai-agent-security

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 0726a3d2acc1 @ c035044634a6fb0e

## Summary (orientation draft, not independently verified)

The repository contains demo source code for the encryption defense from the paper 'Security of AI Agents', with sandbox defense and evaluation code in a separate AgentBench fork. Evidence covers two agent demos (SSN and homomorphic encryption), their CLI interfaces, pinned dependencies, setup/test instructions, and documented limitations.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] The repository holds source code for the encryption-defense demos presented in the paper 'Security of AI Agents'; sandbox defense and evaluation code lives in a separate AgentBench fork. -- evidence: [README.md#L2-L4](https://github.com/SecurityLab-UCD/ai-agent-security/blob/0726a3d2acc1caada53302420b3050d6fe30427d/README.md#L2-L4)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (1 claim(s)):
  - [observation/documented] Demo prompts are phrased as 'number' rather than 'SSN' or 'social security number' to avoid triggering alignment; users can request digit groups such as the first three or last four digits. -- evidence: [README.md#L40-L40](https://github.com/SecurityLab-UCD/ai-agent-security/blob/0726a3d2acc1caada53302420b3050d6fe30427d/README.md#L40-L40), [README.md#L38-L38](https://github.com/SecurityLab-UCD/ai-agent-security/blob/0726a3d2acc1caada53302420b3050d6fe30427d/README.md#L38-L38)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: setup involves sourcing env.sh from the repo root so Python can find the project's modules, installing dependencies via pip from requirements.txt, and generating homomorphic-encryption data with HE_data.py. -- evidence: [README.md#L20-L24](https://github.com/SecurityLab-UCD/ai-agent-security/blob/0726a3d2acc1caada53302420b3050d6fe30427d/README.md#L20-L24), [README.md#L15-L18](https://github.com/SecurityLab-UCD/ai-agent-security/blob/0726a3d2acc1caada53302420b3050d6fe30427d/README.md#L15-L18), [README.md#L10-L13](https://github.com/SecurityLab-UCD/ai-agent-security/blob/0726a3d2acc1caada53302420b3050d6fe30427d/README.md#L10-L13)
  - [observation/documented] Repository development practice: tests are executed with 'pytest tests/*' after generating ciphertext files via HE_data.py. -- evidence: [README.md#L53-L54](https://github.com/SecurityLab-UCD/ai-agent-security/blob/0726a3d2acc1caada53302420b3050d6fe30427d/README.md#L53-L54), [README.md#L56-L56](https://github.com/SecurityLab-UCD/ai-agent-security/blob/0726a3d2acc1caada53302420b3050d6fe30427d/README.md#L56-L56), [README.md#L59-L60](https://github.com/SecurityLab-UCD/ai-agent-security/blob/0726a3d2acc1caada53302420b3050d6fe30427d/README.md#L59-L60)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The SSN agent demo is run as a CLI: python agents/ssn_agent.py with --model, --user_id, --ssns_path, and --secretkeys_path arguments. -- evidence: [README.md#L33-L36](https://github.com/SecurityLab-UCD/ai-agent-security/blob/0726a3d2acc1caada53302420b3050d6fe30427d/README.md#L33-L36)
  - [observation/documented] The homomorphic-encryption agent demo is run via python agents/HE_agent.py with a --model argument, and prompts must specify 'sum' or 'product' for postprocessing reasons. -- evidence: [README.md#L43-L47](https://github.com/SecurityLab-UCD/ai-agent-security/blob/0726a3d2acc1caada53302420b3050d6fe30427d/README.md#L43-L47)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (3 claim(s)):
  - [observation/documented] The project requires Python 3.8 or above. -- evidence: [README.md#L7-L7](https://github.com/SecurityLab-UCD/ai-agent-security/blob/0726a3d2acc1caada53302420b3050d6fe30427d/README.md#L7-L7)
  - [observation/documented] Pinned dependencies include langchain 0.1.16, langchain-openai 0.1.6, pyffx 0.3.0, and a git-installed py-fhe library; test dependencies are hypothesis 6.100.1 and pytest 8.1.1. -- evidence: [requirements.txt#L6-L7](https://github.com/SecurityLab-UCD/ai-agent-security/blob/0726a3d2acc1caada53302420b3050d6fe30427d/requirements.txt#L6-L7), [requirements.txt#L1-L4](https://github.com/SecurityLab-UCD/ai-agent-security/blob/0726a3d2acc1caada53302420b3050d6fe30427d/requirements.txt#L1-L4)
- limitations (2 claim(s)):
  - [observation/documented] The default encryptor cannot handle numbers greater than 400, so calculation results must stay within 0 to 400 inclusive; the limit is configurable in HE_data/HE_data.py. -- evidence: [README.md#L43-L47](https://github.com/SecurityLab-UCD/ai-agent-security/blob/0726a3d2acc1caada53302420b3050d6fe30427d/README.md#L43-L47)
More evidence: [full detail](ai-agent-security.detail.md)

Metadata and full claim list: [full detail](ai-agent-security.detail.md)
Human notes ([notes](ai-agent-security.notes.md), never overwritten by build)

[Back to map index](../../index.md)
