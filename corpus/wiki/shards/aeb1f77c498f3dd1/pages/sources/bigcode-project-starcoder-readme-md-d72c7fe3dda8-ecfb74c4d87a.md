---
access: public
aliases: []
claim_ids:
- clm_1d2c1d2f625f8a80fe5c0b61e4529b9051de031afc6a9988822f69f30d9d125a
- clm_461afc725f22b7f36ef8a4e4ba0d4e0e805507347f57f20844c7af18f5bd3608
- clm_5f88b744e01777170b4d260b247b221c106c292134f51666123a099b459a2caa
- clm_7adfa8cfe3e6cdecb65bd2b16eb7759f38583bda10dc503e187247aa598166f0
- clm_7c73342ec232b1b8bca5f104a1ef8449a3c7b3cbf7b2cd9d078e66f3beea6930
- clm_90c561487b46d1513df61631de4c28e9118d682b9322ad1734df9c773d18b15e
- clm_afb0a45dbe84d161653f10219ff980cdbec3d0b47496c2f92c04f0a6ad0b853d
- clm_c1bf9939ee2f17d1d8ef1a60b79cd683efb8ab0a4648275009473eba5dabe245
- clm_cbb3edc069e2e8e7e5eb0d555879a5f471e99845cddfc9c2af3a9a216882fd57
- clm_ebc25651e1d1ad21562e22a4c3b4b2cece456a8eacafdcbdf4c2d6c6a8884999
- clm_ecdaaa4bfa480dc442ee415b577c0719409c521f5d3601fc3fb19ff9e049aaea
maturity: draft
page_id: pg_f2c658ebd0815a93a98cecfb74c4d87a
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_5efec9194f9e5fcb988c783c33d840d5
title: bigcode-project/starcoder/README.md @ d72c7fe3dda8
updated_at: '2026-09-14T03:38:27Z'
---

# bigcode-project/starcoder/README.md @ d72c7fe3dda8

<!-- rcw:begin owner=source:src_5efec9194f9e5fcb988c783c33d840d5 block=evidence -->
- Evaluation of StarCoder and its derivatives is done with the external BigCode-Evaluation-Harness for Code LLMs. [@claim:clm_1d2c1d2f625f8a80fe5c0b61e4529b9051de031afc6a9988822f69f30d9d125a]
- Using the model requires accepting an agreement on hf.co/bigcode/starcoder and logging into the Hugging Face hub with huggingface-cli login. [@claim:clm_461afc725f22b7f36ef8a4e4ba0d4e0e805507347f57f20844c7af18f5bd3608]
- Repository development practice: setup involves installing libraries from requirements.txt via pip, and fine-tuning setup uses a conda environment with pytorch, transformers, peft, datasets, accelerate, huggingface_hub, bitsandbytes, and wandb. [@claim:clm_5f88b744e01777170b4d260b247b221c106c292134f51666123a099b459a2caa]
- The README shows serving via the text-generation-inference Docker image with --model-id bigcode/starcoder and --max-total-tokens 8192, using a BigCode-enabled Hugging Face token. [@claim:clm_7adfa8cfe3e6cdecb65bd2b16eb7759f38583bda10dc503e187247aa598166f0]
- In FP32 the model needs over 60GB of RAM; loading in FP16/BF16 takes about 30GB, and 8-bit loading under 20GB (reported footprint ~15.9GB). [@claim:clm_7c73342ec232b1b8bca5f104a1ef8449a3c7b3cbf7b2cd9d078e66f3beea6930]
- Repository development practice: fine-tuning is run with finetune/finetune.py using the stack-exchange-instruction dataset, streaming, seq_length 2048, cosine LR schedule, and related hyperparameters; a torch.distributed.launch variant supports multiple GPUs. [@claim:clm_90c561487b46d1513df61631de4c28e9118d682b9322ad1734df9c773d18b15e]
- The README shows the model can run on either GPU (cuda) or CPU, with the device selected in the loading example. [@claim:clm_afb0a45dbe84d161653f10219ff980cdbec3d0b47496c2f92c04f0a6ad0b853d]
- StarCoder is a language model trained on source code and natural-language text covering more than 80 programming languages, plus text from GitHub issues, commits, and notebooks. [@claim:clm_c1bf9939ee2f17d1d8ef1a60b79cd683efb8ab0a4648275009473eba5dabe245]
- A fine-tuned StarCoder chat assistant variant was announced in May 2023, with training code in the chat/ directory and a hosted playground. [@claim:clm_cbb3edc069e2e8e7e5eb0d555879a5f471e99845cddfc9c2af3a9a216882fd57]
- The model is served from the checkpoint bigcode/starcoder and can be used through Hugging Face transformers AutoModelForCausalLM/AutoTokenizer or a text-generation pipeline. [@claim:clm_ebc25651e1d1ad21562e22a4c3b4b2cece456a8eacafdcbdf4c2d6c6a8884999]
- Repository development practice: models trained with PEFT must have adapter layers merged into the base model via finetune/merge_peft_adapters.py before inference or evaluation, with an optional --push_to_hub flag. [@claim:clm_ecdaaa4bfa480dc442ee415b577c0719409c521f5d3601fc3fb19ff9e049aaea]
<!-- rcw:end owner=source:src_5efec9194f9e5fcb988c783c33d840d5 block=evidence -->

## Researcher notes

