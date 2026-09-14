# bigcode-project/starcoder

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit d72c7fe3dda8 @ b1fb3b0e3d96ec5f

## Summary (orientation draft, not independently verified)

The repository documents StarCoder, a code-trained language model, with usage examples via Hugging Face transformers, fine-tuning instructions (including Stack Exchange instruction tuning with PEFT), memory requirements, and a pointer to the BigCode evaluation harness.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 10 facet(s); 3 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] StarCoder is a language model trained on source code and natural-language text covering more than 80 programming languages, plus text from GitHub issues, commits, and notebooks. -- evidence: [README.md#L6-L6](https://github.com/bigcode-project/starcoder/blob/d72c7fe3dda81d47ad9b851f9567393fb6b551b9/README.md#L6-L6)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (1 claim(s)):
  - [observation/documented] The README shows the model can run on either GPU (cuda) or CPU, with the device selected in the loading example. -- evidence: [README.md#L46-L47](https://github.com/bigcode-project/starcoder/blob/d72c7fe3dda81d47ad9b851f9567393fb6b551b9/README.md#L46-L47)
- workflows (3 claim(s)):
  - [observation/documented] Repository development practice: setup involves installing libraries from requirements.txt via pip, and fine-tuning setup uses a conda environment with pytorch, transformers, peft, datasets, accelerate, huggingface_hub, bitsandbytes, and wandb. -- evidence: [README.md#L36-L39](https://github.com/bigcode-project/starcoder/blob/d72c7fe3dda81d47ad9b851f9567393fb6b551b9/README.md#L36-L39), [README.md#L84-L98](https://github.com/bigcode-project/starcoder/blob/d72c7fe3dda81d47ad9b851f9567393fb6b551b9/README.md#L84-L98), [README.md#L106-L110](https://github.com/bigcode-project/starcoder/blob/d72c7fe3dda81d47ad9b851f9567393fb6b551b9/README.md#L106-L110), [README.md#L112-L129](https://github.com/bigcode-project/starcoder/blob/d72c7fe3dda81d47ad9b851f9567393fb6b551b9/README.md#L112-L129), [README.md#L104-L104](https://github.com/bigcode-project/starcoder/blob/d72c7fe3dda81d47ad9b851f9567393fb6b551b9/README.md#L104-L104)
  - [observation/documented] Repository development practice: fine-tuning is run with finetune/finetune.py using the stack-exchange-instruction dataset, streaming, seq_length 2048, cosine LR schedule, and related hyperparameters; a torch.distributed.launch variant supports multiple GPUs. -- evidence: [README.md#L138-L159](https://github.com/bigcode-project/starcoder/blob/d72c7fe3dda81d47ad9b851f9567393fb6b551b9/README.md#L138-L159), [README.md#L161-L181](https://github.com/bigcode-project/starcoder/blob/d72c7fe3dda81d47ad9b851f9567393fb6b551b9/README.md#L161-L181)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] The model is served from the checkpoint bigcode/starcoder and can be used through Hugging Face transformers AutoModelForCausalLM/AutoTokenizer or a text-generation pipeline. -- evidence: [README.md#L46-L47](https://github.com/bigcode-project/starcoder/blob/d72c7fe3dda81d47ad9b851f9567393fb6b551b9/README.md#L46-L47), [README.md#L56-L61](https://github.com/bigcode-project/starcoder/blob/d72c7fe3dda81d47ad9b851f9567393fb6b551b9/README.md#L56-L61), [README.md#L33-L33](https://github.com/bigcode-project/starcoder/blob/d72c7fe3dda81d47ad9b851f9567393fb6b551b9/README.md#L33-L33), [README.md#L66-L69](https://github.com/bigcode-project/starcoder/blob/d72c7fe3dda81d47ad9b851f9567393fb6b551b9/README.md#L66-L69)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (1 claim(s)):
  - [observation/documented] The README shows serving via the text-generation-inference Docker image with --model-id bigcode/starcoder and --max-total-tokens 8192, using a BigCode-enabled Hugging Face token. -- evidence: [README.md#L73-L76](https://github.com/bigcode-project/starcoder/blob/d72c7fe3dda81d47ad9b851f9567393fb6b551b9/README.md#L73-L76)
- tools-permissions (1 claim(s)):
  - [observation/documented] Using the model requires accepting an agreement on hf.co/bigcode/starcoder and logging into the Hugging Face hub with huggingface-cli login. -- evidence: [README.md#L14-L17](https://github.com/bigcode-project/starcoder/blob/d72c7fe3dda81d47ad9b851f9567393fb6b551b9/README.md#L14-L17)
- evaluation (1 claim(s)):
  - [observation/documented] Evaluation of StarCoder and its derivatives is done with the external BigCode-Evaluation-Harness for Code LLMs. -- evidence: [README.md#L197-L197](https://github.com/bigcode-project/starcoder/blob/d72c7fe3dda81d47ad9b851f9567393fb6b551b9/README.md#L197-L197)
- dependencies (1 claim(s)):
  - [observation/documented] requirements.txt pins tqdm 4.65.0, transformers 4.28.1, datasets 2.11.0, huggingface-hub 0.13.4, and accelerate 0.18.0. -- evidence: [requirements.txt#L1-L5](https://github.com/bigcode-project/starcoder/blob/d72c7fe3dda81d47ad9b851f9567393fb6b551b9/requirements.txt#L1-L5)
- limitations (1 claim(s)):
  - [observation/documented] In FP32 the model needs over 60GB of RAM; loading in FP16/BF16 takes about 30GB, and 8-bit loading under 20GB (reported footprint ~15.9GB). -- evidence: [README.md#L207-L213](https://github.com/bigcode-project/starcoder/blob/d72c7fe3dda81d47ad9b851f9567393fb6b551b9/README.md#L207-L213), [README.md#L200-L201](https://github.com/bigcode-project/starcoder/blob/d72c7fe3dda81d47ad9b851f9567393fb6b551b9/README.md#L200-L201)
- relevance (1 claim(s)):
  - [observation/documented] A fine-tuned StarCoder chat assistant variant was announced in May 2023, with training code in the chat/ directory and a hosted playground. -- evidence: [README.md#L10-L10](https://github.com/bigcode-project/starcoder/blob/d72c7fe3dda81d47ad9b851f9567393fb6b551b9/README.md#L10-L10)
More evidence: [full detail](starcoder.detail.md)

Metadata and full claim list: [full detail](starcoder.detail.md)
Human notes ([notes](starcoder.notes.md), never overwritten by build)

[Back to map index](../../index.md)
