# nvidia-nemo/speech

Status: distilled - Freshness: current
Catalog classes: agent-sdk
Origins: github-rename-resolution, alltheagents.org-backing, github-verified-rename - Projects: navy-yard, Observatory
Formerly: nvidia/nemo (github id 200722670).
Latest snapshot: commit ca3f93a516ff @ 568b8afcf9714648

## Summary (orientation draft, not independently verified)

Selected evidence records: NeMo Speech 3.0 is available as release v3.0.0 and in the 26.07.00 NeMo Speech NGC container; the last pre-split NeMo release was v2.7.3. The project targets researchers and PyTorch developers building speech models, covering automatic speech recognition, text-to-speech, and Speech LLMs, with pre-trained checkpoints for reuse.

## Source coverage

Source coverage (partial): 6 of 111 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 4 facet(s); 9 facet(s) unknown.

- specifications (3 claim(s)):
  - [observation/documented] NeMo Speech 3.0 is available as release v3.0.0 and in the 26.07.00 NeMo Speech NGC container; the last pre-split NeMo release was v2.7.3. -- evidence: [README.md#L15-L19](https://github.com/NVIDIA-NeMo/Speech/blob/ca3f93a516ff172e32951928aea6f96a977a7600/README.md#L15-L19)
  - [observation/documented] The project targets researchers and PyTorch developers building speech models, covering automatic speech recognition, text-to-speech, and Speech LLMs, with pre-trained checkpoints for reuse. -- evidence: [README.md#L46-L48](https://github.com/NVIDIA-NeMo/Speech/blob/ca3f93a516ff172e32951928aea6f96a977a7600/README.md#L46-L48)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: the README badges indicate a CodeQL GitHub Actions workflow on main and black as the enforced code style; contributors are directed to CONTRIBUTING.md for the contribution process. -- evidence: [README.md#L1-L7](https://github.com/NVIDIA-NeMo/Speech/blob/ca3f93a516ff172e32951928aea6f96a977a7600/README.md#L1-L7), [README.md#L132-L133](https://github.com/NVIDIA-NeMo/Speech/blob/ca3f93a516ff172e32951928aea6f96a977a7600/README.md#L132-L133)
  - [observation/documented] Repository development practice: the recommended source install uses uv sync with extras from the committed uv.lock, with optional --group test for the test suite and --group docs for documentation builds. -- evidence: [README.md#L78-L78](https://github.com/NVIDIA-NeMo/Speech/blob/ca3f93a516ff172e32951928aea6f96a977a7600/README.md#L78-L78), [README.md#L88-L88](https://github.com/NVIDIA-NeMo/Speech/blob/ca3f93a516ff172e32951928aea6f96a977a7600/README.md#L88-L88)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The ASR API exposes model classes such as EncDecCTCModel, EncDecRNNTModel and their BPE and prompt-aware variants, with documented members including transcribe, change_vocabulary, and data/optimization setup methods. -- evidence: [docs/source/asr/api.rst#L28-L30](https://github.com/NVIDIA-NeMo/Speech/blob/ca3f93a516ff172e32951928aea6f96a977a7600/docs/source/asr/api.rst#L28-L30), [docs/source/asr/api.rst#L18-L20](https://github.com/NVIDIA-NeMo/Speech/blob/ca3f93a516ff172e32951928aea6f96a977a7600/docs/source/asr/api.rst#L18-L20), [docs/source/asr/api.rst#L8-L10](https://github.com/NVIDIA-NeMo/Speech/blob/ca3f93a516ff172e32951928aea6f96a977a7600/docs/source/asr/api.rst#L8-L10), [docs/source/asr/api.rst#L33-L35](https://github.com/NVIDIA-NeMo/Speech/blob/ca3f93a516ff172e32951928aea6f96a977a7600/docs/source/asr/api.rst#L33-L35)
  - [observation/documented] Docker usage is documented: the prebuilt 26.07.00 NGC image can be pulled and run with --gpus all, or built from docker/Dockerfile with build args GPU_TARGET (h100plus default, a100) and BASE_IMAGE. -- evidence: [README.md#L111-L111](https://github.com/NVIDIA-NeMo/Speech/blob/ca3f93a516ff172e32951928aea6f96a977a7600/README.md#L111-L111), [README.md#L97-L100](https://github.com/NVIDIA-NeMo/Speech/blob/ca3f93a516ff172e32951928aea6f96a977a7600/README.md#L97-L100), [README.md#L104-L109](https://github.com/NVIDIA-NeMo/Speech/blob/ca3f93a516ff172e32951928aea6f96a977a7600/README.md#L104-L109)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (4 claim(s)):
  - [observation/documented] Minimum requirements are Python 3.12+, PyTorch 2.7+ (CPU or CUDA), and an NVIDIA GPU with CUDA, which is required for training and recommended for inference. -- evidence: [README.md#L57-L59](https://github.com/NVIDIA-NeMo/Speech/blob/ca3f93a516ff172e32951928aea6f96a977a7600/README.md#L57-L59)
More evidence: [full detail](speech.detail.md)

Metadata and full claim list: [full detail](speech.detail.md)
Human notes ([notes](speech.notes.md), never overwritten by build)

[Back to map index](../../index.md)
