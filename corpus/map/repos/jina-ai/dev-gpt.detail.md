# jina-ai/dev-gpt -- full detail

[Back to orientation](dev-gpt.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/jina-ai/dev-gpt/f6c151f93b02cc07fe6302e507927ea5f802a61e/065ec9400596f020.json](../../../wiki/dossiers/jina-ai/dev-gpt/f6c151f93b02cc07fe6302e507927ea5f802a61e/065ec9400596f020.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] For each strategy the generator produces microservice.py, test_microservice.py, requirements.txt, and a Dockerfile whose build also runs the tests. -- evidence: [README.md#L505-L517](https://github.com/jina-ai/dev-gpt/blob/f6c151f93b02cc07fe6302e507927ea5f802a61e/README.md#L505-L517) (`clm_e651c96b6ac8f9f80baa4703aafe8633dbcc081752a76433e266879463f0686d`)

## design-choices (2 claim(s))

- [observation/documented] The tool is framed as a virtual three-role team — Product Manager, Developer, and DevOps — that builds microservices from a natural-language description. -- evidence: [README.md#L9-L26](https://github.com/jina-ai/dev-gpt/blob/f6c151f93b02cc07fe6302e507927ea5f802a61e/README.md#L9-L26), [README.md#L28-L31](https://github.com/jina-ai/dev-gpt/blob/f6c151f93b02cc07fe6302e507927ea5f802a61e/README.md#L28-L31), [README.md#L57-L59](https://github.com/jina-ai/dev-gpt/blob/f6c151f93b02cc07fe6302e507927ea5f802a61e/README.md#L57-L59) (`clm_3f5d7ef2d0ea6424c4bf23b0bef8e4debbef750a5ecb4f2fe813ac7f6629f93c`)
- [observation/documented] The model choice is user-selectable between gpt-3.5-turbo and gpt-4, with gpt-3.5-turbo described as roughly 10x cheaper but less capable of complex microservices; default is the largest model the key can access. -- evidence: [README.md#L85-L95](https://github.com/jina-ai/dev-gpt/blob/f6c151f93b02cc07fe6302e507927ea5f802a61e/README.md#L85-L95) (`clm_ad205eb121e6f371542b12f04732a09cc7950edbb017482e3ec9e37a77ad618c`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributors are invited to open PRs or issues, and a checklist of next steps and nice-to-haves (e.g. verifying Windows/Linux support, adding tests, cleaning up duplicate code) is maintained in the README. -- evidence: [README.md#L524-L525](https://github.com/jina-ai/dev-gpt/blob/f6c151f93b02cc07fe6302e507927ea5f802a61e/README.md#L524-L525), [README.md#L527-L531](https://github.com/jina-ai/dev-gpt/blob/f6c151f93b02cc07fe6302e507927ea5f802a61e/README.md#L527-L531), [README.md#L534-L563](https://github.com/jina-ai/dev-gpt/blob/f6c151f93b02cc07fe6302e507927ea5f802a61e/README.md#L534-L563) (`clm_6db79062a171a2c4beeb8a509cd7728288648e8b2390173c24d6c8a35cd9f62d`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] Dev-GPT is a CLI tool with subcommands including generate, run, deploy, and configure, invoked as 'dev-gpt <command>' with flags like --description, --model, and --path. -- evidence: [README.md#L103-L107](https://github.com/jina-ai/dev-gpt/blob/f6c151f93b02cc07fe6302e507927ea5f802a61e/README.md#L103-L107), [README.md#L110-L115](https://github.com/jina-ai/dev-gpt/blob/f6c151f93b02cc07fe6302e507927ea5f802a61e/README.md#L110-L115), [README.md#L69-L77](https://github.com/jina-ai/dev-gpt/blob/f6c151f93b02cc07fe6302e507927ea5f802a61e/README.md#L69-L77), [README.md#L85-L95](https://github.com/jina-ai/dev-gpt/blob/f6c151f93b02cc07fe6302e507927ea5f802a61e/README.md#L85-L95), [README.md#L63-L66](https://github.com/jina-ai/dev-gpt/blob/f6c151f93b02cc07fe6302e507927ea5f802a61e/README.md#L63-L66) (`clm_00896d16911fa13278a20a73a998cf876e35e0d609573e3e072e59d46c78dba0`)
- [observation/documented] After a successful build the tool pushes the Docker image to a registry, deploys the microservice, and generates a Streamlit playground for testing it in the browser. -- evidence: [README.md#L103-L107](https://github.com/jina-ai/dev-gpt/blob/f6c151f93b02cc07fe6302e507927ea5f802a61e/README.md#L103-L107), [README.md#L505-L517](https://github.com/jina-ai/dev-gpt/blob/f6c151f93b02cc07fe6302e507927ea5f802a61e/README.md#L505-L517), [README.md#L497-L497](https://github.com/jina-ai/dev-gpt/blob/f6c151f93b02cc07fe6302e507927ea5f802a61e/README.md#L497-L497), [README.md#L499-L499](https://github.com/jina-ai/dev-gpt/blob/f6c151f93b02cc07fe6302e507927ea5f802a61e/README.md#L499-L499) (`clm_812e7cda94851aa9114e2ecc72cbc6b206da2fe6bde4a5ea226edf4a0a98e34c`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (1 claim(s))

- [observation/documented] Generation works by proposing multiple implementation strategies, generating code plus tests and a Dockerfile per strategy, building the image, and using build error messages to retry; after 10 consecutive failures it moves to the next strategy. -- evidence: [README.md#L505-L517](https://github.com/jina-ai/dev-gpt/blob/f6c151f93b02cc07fe6302e507927ea5f802a61e/README.md#L505-L517), [README.md#L485-L485](https://github.com/jina-ai/dev-gpt/blob/f6c151f93b02cc07fe6302e507927ea5f802a61e/README.md#L485-L485), [README.md#L491-L491](https://github.com/jina-ai/dev-gpt/blob/f6c151f93b02cc07fe6302e507927ea5f802a61e/README.md#L491-L491), [README.md#L473-L473](https://github.com/jina-ai/dev-gpt/blob/f6c151f93b02cc07fe6302e507927ea5f802a61e/README.md#L473-L473), [README.md#L493-L493](https://github.com/jina-ai/dev-gpt/blob/f6c151f93b02cc07fe6302e507927ea5f802a61e/README.md#L493-L493) (`clm_8ec997263490fac80df01d97630b5606cd6420398616fa52a91140365d325001`)

## tools-permissions (1 claim(s))

- [observation/documented] The product requires an OpenAI API key with gpt-4 access (gpt-3.5-turbo also accepted for generation), and optionally GOOGLE_API_KEY and GOOGLE_CSE_ID to enable web-content search. -- evidence: [README.md#L79-L81](https://github.com/jina-ai/dev-gpt/blob/f6c151f93b02cc07fe6302e507927ea5f802a61e/README.md#L79-L81), [README.md#L69-L77](https://github.com/jina-ai/dev-gpt/blob/f6c151f93b02cc07fe6302e507927ea5f802a61e/README.md#L69-L77), [README.md#L85-L95](https://github.com/jina-ai/dev-gpt/blob/f6c151f93b02cc07fe6302e507927ea5f802a61e/README.md#L85-L95) (`clm_d94335e85be3acf3c95ae3352c62319c54e8110b39a88dda20e55d18626f2861`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] Runtime dependencies include jina 3.15.1.dev14, openai>=0.27.5, langchain 0.0.153, streamlit 1.9.0, jcloud, jina-hubble-sdk, click, psutil, and pinned pydantic/typing packages. -- evidence: [requirements.txt#L1-L12](https://github.com/jina-ai/dev-gpt/blob/f6c151f93b02cc07fe6302e507927ea5f802a61e/requirements.txt#L1-L12) (`clm_8559396a59c34645883cfd92b96d9ab9a228d3c551116f6ea4f5d3388acb0cdc`)
- [observation/documented] Test dependencies are pytest and pytest-split, listed in requirements-test.txt. -- evidence: [requirements-test.txt#L1-L2](https://github.com/jina-ai/dev-gpt/blob/f6c151f93b02cc07fe6302e507927ea5f802a61e/requirements-test.txt#L1-L2) (`clm_732c881cdea996b29070c46aaac0c869d88cfaf28bac6908c1bd1d3b04104649`)

## limitations (2 claim(s))

- [observation/documented] The README marks the project as an experimental version, and notes a known bug where code generation can hang forever, requiring aborting and redoing the generation. -- evidence: [README.md#L5-L7](https://github.com/jina-ai/dev-gpt/blob/f6c151f93b02cc07fe6302e507927ea5f802a61e/README.md#L5-L7), [README.md#L527-L531](https://github.com/jina-ai/dev-gpt/blob/f6c151f93b02cc07fe6302e507927ea5f802a61e/README.md#L527-L531) (`clm_f56a3beb137933338722346b9f8dae0ec26e14a498605017c10d6c9dbcbabb96`)
- [observation/documented] Documented cost and time bounds: generation takes about 5–15 minutes and costs roughly $0.50–$3.00 per microservice on GPT-4 or $0.05–$0.30 on GPT-3.5-turbo. -- evidence: [README.md#L97-L98](https://github.com/jina-ai/dev-gpt/blob/f6c151f93b02cc07fe6302e507927ea5f802a61e/README.md#L97-L98), [README.md#L100-L100](https://github.com/jina-ai/dev-gpt/blob/f6c151f93b02cc07fe6302e507927ea5f802a61e/README.md#L100-L100) (`clm_0cc6a55a8446676b17aff36c276c71afda1ac001ec0d598273c945b93635f797`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

