# arphanetx/monocle -- full detail

[Back to orientation](monocle.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/arphanetx/monocle/6a865d767a9623af4e72cd1c2b9e39e62db45105/82058386115fbb7c.json](../../../wiki/dossiers/arphanetx/monocle/6a865d767a9623af4e72cd1c2b9e39e62db45105/82058386115fbb7c.json)

## specifications (1 claim(s))

- [observation/documented] Monocle performs natural language searches against compiled binaries: given a binary and search criteria, it decompiles the binary and uses an in-built LLM to identify and score matching code areas. -- evidence: [README.md#L17-L20](https://github.com/arphanetx/Monocle/blob/6a865d767a9623af4e72cd1c2b9e39e62db45105/README.md#L17-L20) (`clm_d9a65cdee0dce8bb8766d2eebf840dd490af449d7a3619e47b930646aea73674`)

## components (1 claim(s))

- [observation/documented] Monocle uses Ghidra headless to enable decompilation of compiled binaries. -- evidence: [README.md#L17-L20](https://github.com/arphanetx/Monocle/blob/6a865d767a9623af4e72cd1c2b9e39e62db45105/README.md#L17-L20) (`clm_ddff4cbb116985b5467190e07fe5b6aa3b9374378898acdd604dc2ee4846d14f`)

## design-choices (1 claim(s))

- [observation/documented] Queries are written in plain text because the tool is backed by an LLM, allowing open-ended natural language questions about a binary without prior knowledge. -- evidence: [README.md#L17-L20](https://github.com/arphanetx/Monocle/blob/6a865d767a9623af4e72cd1c2b9e39e62db45105/README.md#L17-L20) (`clm_29c0e03f35f6202596b3f122d0d3627000ab90e800ff8811414cb9294a2f6e79`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: contributors should fork the repo, create a descriptively named branch, test changes, submit a pull request with a detailed description, and address maintainer feedback before merge. -- evidence: [README.md#L106-L111](https://github.com/arphanetx/Monocle/blob/6a865d767a9623af4e72cd1c2b9e39e62db45105/README.md#L106-L111), [README.md#L103-L104](https://github.com/arphanetx/Monocle/blob/6a865d767a9623af4e72cd1c2b9e39e62db45105/README.md#L103-L104) (`clm_5aca87cd9562f1eaa5f0b1116863031ef4a16b2a3dc71771837a4de3395d19db`)
- [observation/documented] Repository development practice: the project follows the Contributor Covenant Code of Conduct, and bugs or feature requests should be reported via GitHub issues with reproduction details. -- evidence: [README.md#L114-L114](https://github.com/arphanetx/Monocle/blob/6a865d767a9623af4e72cd1c2b9e39e62db45105/README.md#L114-L114), [README.md#L117-L117](https://github.com/arphanetx/Monocle/blob/6a865d767a9623af4e72cd1c2b9e39e62db45105/README.md#L117-L117) (`clm_74a640042a3d3ef04c5638fb83a484e5944b0efa7403ec445daa608944135269`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The CLI takes a binary path and a search target, e.g. monocle --binary <path-to-binary> --find <component-to-find> on Unix, with a monocle.exe variant on Windows. -- evidence: [README.md#L56-L63](https://github.com/arphanetx/Monocle/blob/6a865d767a9623af4e72cd1c2b9e39e62db45105/README.md#L56-L63) (`clm_86fd158e31385fa47535914e660eabd35e633436dd84543ffc0f100540885653`)
- [observation/documented] While processing, Monocle shows a live table sorted by score, listing each analyzed function with a 0-10 relevance score and an explanation; zero-scored functions get no explanation. -- evidence: [README.md#L65-L65](https://github.com/arphanetx/Monocle/blob/6a865d767a9623af4e72cd1c2b9e39e62db45105/README.md#L65-L65) (`clm_32bfd63c12fff0746c2b632a7355f98f0708c2ca567f4c156edde5fe9448abd7`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (3 claim(s))

- [observation/documented] The runtime model is Mistral-7B-Instruct-v0.2, an instruct fine-tuned Mistral-7B-v0.2 with 7.24B parameters, BF16 tensors, and a 32k context window. -- evidence: [README.md#L95-L100](https://github.com/arphanetx/Monocle/blob/6a865d767a9623af4e72cd1c2b9e39e62db45105/README.md#L95-L100), [README.md#L25-L25](https://github.com/arphanetx/Monocle/blob/6a865d767a9623af4e72cd1c2b9e39e62db45105/README.md#L25-L25) (`clm_ee074a789ea566314b7903a3be3089380c9ae6b8acf3de770f211e90ef4f7eb2`)
- [observation/documented] Monocle requires Nvidia CUDA for improved LLM performance, plus Ghidra installed with analyzeHeadless available in the environment. -- evidence: [README.md#L35-L35](https://github.com/arphanetx/Monocle/blob/6a865d767a9623af4e72cd1c2b9e39e62db45105/README.md#L35-L35), [README.md#L30-L33](https://github.com/arphanetx/Monocle/blob/6a865d767a9623af4e72cd1c2b9e39e62db45105/README.md#L30-L33) (`clm_bc2b1bcff517ed85c391ade1f7fc9b1bf0b0b95b72be32b6ab35331eabe28766`)
- [observation/documented] Python dependencies are listed in requirements.txt, including transformers[torch]>=4.28.1, torch>=1.13.1, bitsandbytes>=0.39.0, rich, and huggingface_hub. -- evidence: [README.md#L37-L37](https://github.com/arphanetx/Monocle/blob/6a865d767a9623af4e72cd1c2b9e39e62db45105/README.md#L37-L37), [requirements.txt#L1-L13](https://github.com/arphanetx/Monocle/blob/6a865d767a9623af4e72cd1c2b9e39e62db45105/requirements.txt#L1-L13) (`clm_5d90bcc44b72f1308fe99e13d7dc4869736365320d04a6b1a3d0f1745d4b3e47`)

## limitations (2 claim(s))

- [observation/documented] At least 16GB RAM and a dedicated Nvidia GPU with 4GB+ memory are recommended; lower-spec machines can run it but significantly slower. -- evidence: [README.md#L25-L25](https://github.com/arphanetx/Monocle/blob/6a865d767a9623af4e72cd1c2b9e39e62db45105/README.md#L25-L25) (`clm_7312beede696695ddd0b4316b693779358cd23e0bb3a5283967bf1cf21bdbca6`)
- [observation/documented] Monocle has been tested on Windows 11 and is expected, though not confirmed, to be compatible with Unix and other systems. -- evidence: [README.md#L27-L27](https://github.com/arphanetx/Monocle/blob/6a865d767a9623af4e72cd1c2b9e39e62db45105/README.md#L27-L27) (`clm_78c30067e7dceb7c479ebbff9c6024e17f63eb6cd17807bd119e51b40491252a`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

