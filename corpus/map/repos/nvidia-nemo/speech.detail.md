# nvidia-nemo/speech -- full detail

[Back to orientation](speech.md)

## Origins

- github-rename-resolution
- alltheagents.org-backing
- github-verified-rename

## Projects

- navy-yard
- Observatory

Full evidence record (JSON): [wiki/dossiers/nvidia-nemo/speech/ca3f93a516ff172e32951928aea6f96a977a7600/568b8afcf9714648.json](../../../wiki/dossiers/nvidia-nemo/speech/ca3f93a516ff172e32951928aea6f96a977a7600/568b8afcf9714648.json)

## specifications (3 claim(s))

- [observation/documented] NeMo Speech 3.0 is available as release v3.0.0 and in the 26.07.00 NeMo Speech NGC container; the last pre-split NeMo release was v2.7.3. -- evidence: [README.md#L15-L19](https://github.com/NVIDIA-NeMo/Speech/blob/ca3f93a516ff172e32951928aea6f96a977a7600/README.md#L15-L19) (`clm_704562de095554cee05ed8067fe7ea5af0d6ed250d7a096af5a5f3236bf0e1aa`)
- [observation/documented] The project targets researchers and PyTorch developers building speech models, covering automatic speech recognition, text-to-speech, and Speech LLMs, with pre-trained checkpoints for reuse. -- evidence: [README.md#L46-L48](https://github.com/NVIDIA-NeMo/Speech/blob/ca3f93a516ff172e32951928aea6f96a977a7600/README.md#L46-L48) (`clm_d3f16010a2041766834c627211c9075da55bd05b24a639d1a6181c99d4600a7b`)
- [observation/documented] NeMo Speech is licensed under the Apache License 2.0. -- evidence: [README.md#L137-L137](https://github.com/NVIDIA-NeMo/Speech/blob/ca3f93a516ff172e32951928aea6f96a977a7600/README.md#L137-L137) (`clm_ba6d7aaaa8e6abb012e9eb6ae4f9509f1bc7f7a9666a1d878980c413bc04afec`)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: the README badges indicate a CodeQL GitHub Actions workflow on main and black as the enforced code style; contributors are directed to CONTRIBUTING.md for the contribution process. -- evidence: [README.md#L1-L7](https://github.com/NVIDIA-NeMo/Speech/blob/ca3f93a516ff172e32951928aea6f96a977a7600/README.md#L1-L7), [README.md#L132-L133](https://github.com/NVIDIA-NeMo/Speech/blob/ca3f93a516ff172e32951928aea6f96a977a7600/README.md#L132-L133) (`clm_69cbe6716c0766ea6576fa5ed1999d7e0360ce1276bb90d1306adc3f0e5407f0`)
- [observation/documented] Repository development practice: the recommended source install uses uv sync with extras from the committed uv.lock, with optional --group test for the test suite and --group docs for documentation builds. -- evidence: [README.md#L78-L78](https://github.com/NVIDIA-NeMo/Speech/blob/ca3f93a516ff172e32951928aea6f96a977a7600/README.md#L78-L78), [README.md#L88-L88](https://github.com/NVIDIA-NeMo/Speech/blob/ca3f93a516ff172e32951928aea6f96a977a7600/README.md#L88-L88) (`clm_4cba4d61c7cab4183db4a426cf077a295d62053dc39e9c7486404156654908d0`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The ASR API exposes model classes such as EncDecCTCModel, EncDecRNNTModel and their BPE and prompt-aware variants, with documented members including transcribe, change_vocabulary, and data/optimization setup methods. -- evidence: [docs/source/asr/api.rst#L28-L30](https://github.com/NVIDIA-NeMo/Speech/blob/ca3f93a516ff172e32951928aea6f96a977a7600/docs/source/asr/api.rst#L28-L30), [docs/source/asr/api.rst#L18-L20](https://github.com/NVIDIA-NeMo/Speech/blob/ca3f93a516ff172e32951928aea6f96a977a7600/docs/source/asr/api.rst#L18-L20), [docs/source/asr/api.rst#L8-L10](https://github.com/NVIDIA-NeMo/Speech/blob/ca3f93a516ff172e32951928aea6f96a977a7600/docs/source/asr/api.rst#L8-L10), [docs/source/asr/api.rst#L33-L35](https://github.com/NVIDIA-NeMo/Speech/blob/ca3f93a516ff172e32951928aea6f96a977a7600/docs/source/asr/api.rst#L33-L35) (`clm_ad0cd75eec987c9ed5ec4dd74c9c810ce8d60813c935ef062ffdb949d47e2fd9`)
- [observation/documented] Docker usage is documented: the prebuilt 26.07.00 NGC image can be pulled and run with --gpus all, or built from docker/Dockerfile with build args GPU_TARGET (h100plus default, a100) and BASE_IMAGE. -- evidence: [README.md#L111-L111](https://github.com/NVIDIA-NeMo/Speech/blob/ca3f93a516ff172e32951928aea6f96a977a7600/README.md#L111-L111), [README.md#L97-L100](https://github.com/NVIDIA-NeMo/Speech/blob/ca3f93a516ff172e32951928aea6f96a977a7600/README.md#L97-L100), [README.md#L104-L109](https://github.com/NVIDIA-NeMo/Speech/blob/ca3f93a516ff172e32951928aea6f96a977a7600/README.md#L104-L109) (`clm_adeeb605b7b7af5f3439a22e78bfadb5ebab10ebb5e42dc00f51121b3c2229a0`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (4 claim(s))

- [observation/documented] Minimum requirements are Python 3.12+, PyTorch 2.7+ (CPU or CUDA), and an NVIDIA GPU with CUDA, which is required for training and recommended for inference. -- evidence: [README.md#L57-L59](https://github.com/NVIDIA-NeMo/Speech/blob/ca3f93a516ff172e32951928aea6f96a977a7600/README.md#L57-L59) (`clm_d73e2863b6dd21ba914bcd4cc8b7fe4078ca9398f44c6f64076f7ae2316b9e4b`)
- [observation/documented] The actively tested stack (Python 3.13 with PyTorch 2.11/CUDA 12.9 or PyTorch 2.12/CUDA 13.2, pinned in uv.lock and shipped in the container) is stated as convenient but not a hard requirement. -- evidence: [README.md#L61-L61](https://github.com/NVIDIA-NeMo/Speech/blob/ca3f93a516ff172e32951928aea6f96a977a7600/README.md#L61-L61) (`clm_4ec93f51f3fff03d767e5ab8c2c220793c558fca188c7371baa5a781582532f0`)
- [observation/documented] The package installs over an existing Python/PyTorch/CUDA environment without replacing it, e.g. via pip or uv pip with the 'nemo-toolkit[asr,tts]' extras, and cu12/cu13 extras plus a PyTorch wheel index for pinned CUDA builds. -- evidence: [README.md#L125-L128](https://github.com/NVIDIA-NeMo/Speech/blob/ca3f93a516ff172e32951928aea6f96a977a7600/README.md#L125-L128), [README.md#L115-L115](https://github.com/NVIDIA-NeMo/Speech/blob/ca3f93a516ff172e32951928aea6f96a977a7600/README.md#L115-L115), [README.md#L117-L119](https://github.com/NVIDIA-NeMo/Speech/blob/ca3f93a516ff172e32951928aea6f96a977a7600/README.md#L117-L119) (`clm_0aa15f91de65f9a4a0283e228222a6a6085ea58190f629f31252d36354ad6705`)
- [observation/documented] The SpeechLM2/Automodel backend runs without compiled dependencies but can optionally use accelerated backends (Transformer Engine, FlashAttention, Mamba, grouped-GEMM/MoE, DeepEP) from the 'compiled' or 'compiled-a100' extras built by the Dockerfile. -- evidence: [README.md#L90-L90](https://github.com/NVIDIA-NeMo/Speech/blob/ca3f93a516ff172e32951928aea6f96a977a7600/README.md#L90-L90) (`clm_d45860bf6b4dd484ff5fe0a8cec7a9199e670a55ff053a0bbaec68b7f1e9c827`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

