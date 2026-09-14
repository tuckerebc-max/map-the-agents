---
access: public
aliases: []
claim_ids:
- clm_00896d16911fa13278a20a73a998cf876e35e0d609573e3e072e59d46c78dba0
- clm_0cc6a55a8446676b17aff36c276c71afda1ac001ec0d598273c945b93635f797
- clm_3f5d7ef2d0ea6424c4bf23b0bef8e4debbef750a5ecb4f2fe813ac7f6629f93c
- clm_6db79062a171a2c4beeb8a509cd7728288648e8b2390173c24d6c8a35cd9f62d
- clm_812e7cda94851aa9114e2ecc72cbc6b206da2fe6bde4a5ea226edf4a0a98e34c
- clm_8ec997263490fac80df01d97630b5606cd6420398616fa52a91140365d325001
- clm_ad205eb121e6f371542b12f04732a09cc7950edbb017482e3ec9e37a77ad618c
- clm_d94335e85be3acf3c95ae3352c62319c54e8110b39a88dda20e55d18626f2861
- clm_e651c96b6ac8f9f80baa4703aafe8633dbcc081752a76433e266879463f0686d
- clm_f56a3beb137933338722346b9f8dae0ec26e14a498605017c10d6c9dbcbabb96
maturity: draft
page_id: pg_b4d25c5175145ccfb0e53a279afac327
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_88332432106155bc87df5a9423a67213
title: jina-ai/dev-gpt/README.md @ f6c151f93b02
updated_at: '2026-09-14T02:06:55Z'
---

# jina-ai/dev-gpt/README.md @ f6c151f93b02

<!-- rcw:begin owner=source:src_88332432106155bc87df5a9423a67213 block=evidence -->
- Dev-GPT is a CLI tool with subcommands including generate, run, deploy, and configure, invoked as 'dev-gpt <command>' with flags like --description, --model, and --path. [@claim:clm_00896d16911fa13278a20a73a998cf876e35e0d609573e3e072e59d46c78dba0]
- Documented cost and time bounds: generation takes about 5–15 minutes and costs roughly $0.50–$3.00 per microservice on GPT-4 or $0.05–$0.30 on GPT-3.5-turbo. [@claim:clm_0cc6a55a8446676b17aff36c276c71afda1ac001ec0d598273c945b93635f797]
- The tool is framed as a virtual three-role team — Product Manager, Developer, and DevOps — that builds microservices from a natural-language description. [@claim:clm_3f5d7ef2d0ea6424c4bf23b0bef8e4debbef750a5ecb4f2fe813ac7f6629f93c]
- Repository development practice: contributors are invited to open PRs or issues, and a checklist of next steps and nice-to-haves (e.g. verifying Windows/Linux support, adding tests, cleaning up duplicate code) is maintained in the README. [@claim:clm_6db79062a171a2c4beeb8a509cd7728288648e8b2390173c24d6c8a35cd9f62d]
- After a successful build the tool pushes the Docker image to a registry, deploys the microservice, and generates a Streamlit playground for testing it in the browser. [@claim:clm_812e7cda94851aa9114e2ecc72cbc6b206da2fe6bde4a5ea226edf4a0a98e34c]
- Generation works by proposing multiple implementation strategies, generating code plus tests and a Dockerfile per strategy, building the image, and using build error messages to retry; after 10 consecutive failures it moves to the next strategy. [@claim:clm_8ec997263490fac80df01d97630b5606cd6420398616fa52a91140365d325001]
- The model choice is user-selectable between gpt-3.5-turbo and gpt-4, with gpt-3.5-turbo described as roughly 10x cheaper but less capable of complex microservices; default is the largest model the key can access. [@claim:clm_ad205eb121e6f371542b12f04732a09cc7950edbb017482e3ec9e37a77ad618c]
- The product requires an OpenAI API key with gpt-4 access (gpt-3.5-turbo also accepted for generation), and optionally GOOGLE_API_KEY and GOOGLE_CSE_ID to enable web-content search. [@claim:clm_d94335e85be3acf3c95ae3352c62319c54e8110b39a88dda20e55d18626f2861]
- For each strategy the generator produces microservice.py, test_microservice.py, requirements.txt, and a Dockerfile whose build also runs the tests. [@claim:clm_e651c96b6ac8f9f80baa4703aafe8633dbcc081752a76433e266879463f0686d]
- The README marks the project as an experimental version, and notes a known bug where code generation can hang forever, requiring aborting and redoing the generation. [@claim:clm_f56a3beb137933338722346b9f8dae0ec26e14a498605017c10d6c9dbcbabb96]
<!-- rcw:end owner=source:src_88332432106155bc87df5a9423a67213 block=evidence -->

## Researcher notes

