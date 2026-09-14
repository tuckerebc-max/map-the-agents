---
access: public
aliases: []
claim_ids:
- clm_0aa15f91de65f9a4a0283e228222a6a6085ea58190f629f31252d36354ad6705
- clm_4cba4d61c7cab4183db4a426cf077a295d62053dc39e9c7486404156654908d0
- clm_4ec93f51f3fff03d767e5ab8c2c220793c558fca188c7371baa5a781582532f0
- clm_69cbe6716c0766ea6576fa5ed1999d7e0360ce1276bb90d1306adc3f0e5407f0
- clm_704562de095554cee05ed8067fe7ea5af0d6ed250d7a096af5a5f3236bf0e1aa
- clm_adeeb605b7b7af5f3439a22e78bfadb5ebab10ebb5e42dc00f51121b3c2229a0
- clm_ba6d7aaaa8e6abb012e9eb6ae4f9509f1bc7f7a9666a1d878980c413bc04afec
- clm_d3f16010a2041766834c627211c9075da55bd05b24a639d1a6181c99d4600a7b
- clm_d45860bf6b4dd484ff5fe0a8cec7a9199e670a55ff053a0bbaec68b7f1e9c827
- clm_d73e2863b6dd21ba914bcd4cc8b7fe4078ca9398f44c6f64076f7ae2316b9e4b
maturity: draft
page_id: pg_e480b3a7cf5c5a3683dfcfd8f47b9c9b
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_1162b68a53e85fb1a2f8ebc4568629c0
title: NVIDIA-NeMo/Speech/README.md @ ca3f93a516ff
updated_at: '2026-09-14T04:13:16Z'
---

# NVIDIA-NeMo/Speech/README.md @ ca3f93a516ff

<!-- rcw:begin owner=source:src_1162b68a53e85fb1a2f8ebc4568629c0 block=evidence -->
- The package installs over an existing Python/PyTorch/CUDA environment without replacing it, e.g. via pip or uv pip with the 'nemo-toolkit[asr,tts]' extras, and cu12/cu13 extras plus a PyTorch wheel index for pinned CUDA builds. [@claim:clm_0aa15f91de65f9a4a0283e228222a6a6085ea58190f629f31252d36354ad6705]
- Repository development practice: the recommended source install uses uv sync with extras from the committed uv.lock, with optional --group test for the test suite and --group docs for documentation builds. [@claim:clm_4cba4d61c7cab4183db4a426cf077a295d62053dc39e9c7486404156654908d0]
- The actively tested stack (Python 3.13 with PyTorch 2.11/CUDA 12.9 or PyTorch 2.12/CUDA 13.2, pinned in uv.lock and shipped in the container) is stated as convenient but not a hard requirement. [@claim:clm_4ec93f51f3fff03d767e5ab8c2c220793c558fca188c7371baa5a781582532f0]
- Repository development practice: the README badges indicate a CodeQL GitHub Actions workflow on main and black as the enforced code style; contributors are directed to CONTRIBUTING.md for the contribution process. [@claim:clm_69cbe6716c0766ea6576fa5ed1999d7e0360ce1276bb90d1306adc3f0e5407f0]
- NeMo Speech 3.0 is available as release v3.0.0 and in the 26.07.00 NeMo Speech NGC container; the last pre-split NeMo release was v2.7.3. [@claim:clm_704562de095554cee05ed8067fe7ea5af0d6ed250d7a096af5a5f3236bf0e1aa]
- Docker usage is documented: the prebuilt 26.07.00 NGC image can be pulled and run with --gpus all, or built from docker/Dockerfile with build args GPU_TARGET (h100plus default, a100) and BASE_IMAGE. [@claim:clm_adeeb605b7b7af5f3439a22e78bfadb5ebab10ebb5e42dc00f51121b3c2229a0]
- NeMo Speech is licensed under the Apache License 2.0. [@claim:clm_ba6d7aaaa8e6abb012e9eb6ae4f9509f1bc7f7a9666a1d878980c413bc04afec]
- The project targets researchers and PyTorch developers building speech models, covering automatic speech recognition, text-to-speech, and Speech LLMs, with pre-trained checkpoints for reuse. [@claim:clm_d3f16010a2041766834c627211c9075da55bd05b24a639d1a6181c99d4600a7b]
- The SpeechLM2/Automodel backend runs without compiled dependencies but can optionally use accelerated backends (Transformer Engine, FlashAttention, Mamba, grouped-GEMM/MoE, DeepEP) from the 'compiled' or 'compiled-a100' extras built by the Dockerfile. [@claim:clm_d45860bf6b4dd484ff5fe0a8cec7a9199e670a55ff053a0bbaec68b7f1e9c827]
- Minimum requirements are Python 3.12+, PyTorch 2.7+ (CPU or CUDA), and an NVIDIA GPU with CUDA, which is required for training and recommended for inference. [@claim:clm_d73e2863b6dd21ba914bcd4cc8b7fe4078ca9398f44c6f64076f7ae2316b9e4b]
<!-- rcw:end owner=source:src_1162b68a53e85fb1a2f8ebc4568629c0 block=evidence -->

## Researcher notes

