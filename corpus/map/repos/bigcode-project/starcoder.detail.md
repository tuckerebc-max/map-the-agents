# bigcode-project/starcoder -- full detail

[Back to orientation](starcoder.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/bigcode-project/starcoder/d72c7fe3dda81d47ad9b851f9567393fb6b551b9/b1fb3b0e3d96ec5f.json](../../../wiki/dossiers/bigcode-project/starcoder/d72c7fe3dda81d47ad9b851f9567393fb6b551b9/b1fb3b0e3d96ec5f.json)

## specifications (1 claim(s))

- [observation/documented] StarCoder is a language model trained on source code and natural-language text covering more than 80 programming languages, plus text from GitHub issues, commits, and notebooks. -- evidence: [README.md#L6-L6](https://github.com/bigcode-project/starcoder/blob/d72c7fe3dda81d47ad9b851f9567393fb6b551b9/README.md#L6-L6) (`clm_c1bf9939ee2f17d1d8ef1a60b79cd683efb8ab0a4648275009473eba5dabe245`)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (1 claim(s))

- [observation/documented] The README shows the model can run on either GPU (cuda) or CPU, with the device selected in the loading example. -- evidence: [README.md#L46-L47](https://github.com/bigcode-project/starcoder/blob/d72c7fe3dda81d47ad9b851f9567393fb6b551b9/README.md#L46-L47) (`clm_afb0a45dbe84d161653f10219ff980cdbec3d0b47496c2f92c04f0a6ad0b853d`)

## workflows (3 claim(s))

- [observation/documented] Repository development practice: setup involves installing libraries from requirements.txt via pip, and fine-tuning setup uses a conda environment with pytorch, transformers, peft, datasets, accelerate, huggingface_hub, bitsandbytes, and wandb. -- evidence: [README.md#L36-L39](https://github.com/bigcode-project/starcoder/blob/d72c7fe3dda81d47ad9b851f9567393fb6b551b9/README.md#L36-L39), [README.md#L84-L98](https://github.com/bigcode-project/starcoder/blob/d72c7fe3dda81d47ad9b851f9567393fb6b551b9/README.md#L84-L98), [README.md#L106-L110](https://github.com/bigcode-project/starcoder/blob/d72c7fe3dda81d47ad9b851f9567393fb6b551b9/README.md#L106-L110), [README.md#L112-L129](https://github.com/bigcode-project/starcoder/blob/d72c7fe3dda81d47ad9b851f9567393fb6b551b9/README.md#L112-L129), [README.md#L104-L104](https://github.com/bigcode-project/starcoder/blob/d72c7fe3dda81d47ad9b851f9567393fb6b551b9/README.md#L104-L104) (`clm_5f88b744e01777170b4d260b247b221c106c292134f51666123a099b459a2caa`)
- [observation/documented] Repository development practice: fine-tuning is run with finetune/finetune.py using the stack-exchange-instruction dataset, streaming, seq_length 2048, cosine LR schedule, and related hyperparameters; a torch.distributed.launch variant supports multiple GPUs. -- evidence: [README.md#L138-L159](https://github.com/bigcode-project/starcoder/blob/d72c7fe3dda81d47ad9b851f9567393fb6b551b9/README.md#L138-L159), [README.md#L161-L181](https://github.com/bigcode-project/starcoder/blob/d72c7fe3dda81d47ad9b851f9567393fb6b551b9/README.md#L161-L181) (`clm_90c561487b46d1513df61631de4c28e9118d682b9322ad1734df9c773d18b15e`)
- [observation/documented] Repository development practice: models trained with PEFT must have adapter layers merged into the base model via finetune/merge_peft_adapters.py before inference or evaluation, with an optional --push_to_hub flag. -- evidence: [README.md#L188-L190](https://github.com/bigcode-project/starcoder/blob/d72c7fe3dda81d47ad9b851f9567393fb6b551b9/README.md#L188-L190), [README.md#L192-L194](https://github.com/bigcode-project/starcoder/blob/d72c7fe3dda81d47ad9b851f9567393fb6b551b9/README.md#L192-L194), [README.md#L183-L185](https://github.com/bigcode-project/starcoder/blob/d72c7fe3dda81d47ad9b851f9567393fb6b551b9/README.md#L183-L185) (`clm_ecdaaa4bfa480dc442ee415b577c0719409c521f5d3601fc3fb19ff9e049aaea`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] The model is served from the checkpoint bigcode/starcoder and can be used through Hugging Face transformers AutoModelForCausalLM/AutoTokenizer or a text-generation pipeline. -- evidence: [README.md#L46-L47](https://github.com/bigcode-project/starcoder/blob/d72c7fe3dda81d47ad9b851f9567393fb6b551b9/README.md#L46-L47), [README.md#L56-L61](https://github.com/bigcode-project/starcoder/blob/d72c7fe3dda81d47ad9b851f9567393fb6b551b9/README.md#L56-L61), [README.md#L33-L33](https://github.com/bigcode-project/starcoder/blob/d72c7fe3dda81d47ad9b851f9567393fb6b551b9/README.md#L33-L33), [README.md#L66-L69](https://github.com/bigcode-project/starcoder/blob/d72c7fe3dda81d47ad9b851f9567393fb6b551b9/README.md#L66-L69) (`clm_ebc25651e1d1ad21562e22a4c3b4b2cece456a8eacafdcbdf4c2d6c6a8884999`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (1 claim(s))

- [observation/documented] The README shows serving via the text-generation-inference Docker image with --model-id bigcode/starcoder and --max-total-tokens 8192, using a BigCode-enabled Hugging Face token. -- evidence: [README.md#L73-L76](https://github.com/bigcode-project/starcoder/blob/d72c7fe3dda81d47ad9b851f9567393fb6b551b9/README.md#L73-L76) (`clm_7adfa8cfe3e6cdecb65bd2b16eb7759f38583bda10dc503e187247aa598166f0`)

## tools-permissions (1 claim(s))

- [observation/documented] Using the model requires accepting an agreement on hf.co/bigcode/starcoder and logging into the Hugging Face hub with huggingface-cli login. -- evidence: [README.md#L14-L17](https://github.com/bigcode-project/starcoder/blob/d72c7fe3dda81d47ad9b851f9567393fb6b551b9/README.md#L14-L17) (`clm_461afc725f22b7f36ef8a4e4ba0d4e0e805507347f57f20844c7af18f5bd3608`)

## evaluation (1 claim(s))

- [observation/documented] Evaluation of StarCoder and its derivatives is done with the external BigCode-Evaluation-Harness for Code LLMs. -- evidence: [README.md#L197-L197](https://github.com/bigcode-project/starcoder/blob/d72c7fe3dda81d47ad9b851f9567393fb6b551b9/README.md#L197-L197) (`clm_1d2c1d2f625f8a80fe5c0b61e4529b9051de031afc6a9988822f69f30d9d125a`)

## dependencies (1 claim(s))

- [observation/documented] requirements.txt pins tqdm 4.65.0, transformers 4.28.1, datasets 2.11.0, huggingface-hub 0.13.4, and accelerate 0.18.0. -- evidence: [requirements.txt#L1-L5](https://github.com/bigcode-project/starcoder/blob/d72c7fe3dda81d47ad9b851f9567393fb6b551b9/requirements.txt#L1-L5) (`clm_0c990d84763c647cbe3ca34f76826b97e385ee13e45e812872722ebcedc632c9`)

## limitations (1 claim(s))

- [observation/documented] In FP32 the model needs over 60GB of RAM; loading in FP16/BF16 takes about 30GB, and 8-bit loading under 20GB (reported footprint ~15.9GB). -- evidence: [README.md#L207-L213](https://github.com/bigcode-project/starcoder/blob/d72c7fe3dda81d47ad9b851f9567393fb6b551b9/README.md#L207-L213), [README.md#L200-L201](https://github.com/bigcode-project/starcoder/blob/d72c7fe3dda81d47ad9b851f9567393fb6b551b9/README.md#L200-L201) (`clm_7c73342ec232b1b8bca5f104a1ef8449a3c7b3cbf7b2cd9d078e66f3beea6930`)

## relevance (1 claim(s))

- [observation/documented] A fine-tuned StarCoder chat assistant variant was announced in May 2023, with training code in the chat/ directory and a hosted playground. -- evidence: [README.md#L10-L10](https://github.com/bigcode-project/starcoder/blob/d72c7fe3dda81d47ad9b851f9567393fb6b551b9/README.md#L10-L10) (`clm_cbb3edc069e2e8e7e5eb0d555879a5f471e99845cddfc9c2af3a9a216882fd57`)

