# jina-ai/dev-gpt

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit f6c151f93b02 @ 065ec9400596f020

## Summary (orientation draft, not independently verified)

The evidence consists of README documentation for Dev-GPT, a CLI tool that generates, runs, and deploys Python microservices using OpenAI models, plus dependency lists. No source code slices are present, so all claims are documentation-based.

## Source coverage

Source coverage (complete): 3 of 3 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] For each strategy the generator produces microservice.py, test_microservice.py, requirements.txt, and a Dockerfile whose build also runs the tests. -- evidence: [README.md#L505-L517](https://github.com/jina-ai/dev-gpt/blob/f6c151f93b02cc07fe6302e507927ea5f802a61e/README.md#L505-L517)
- design-choices (2 claim(s)):
  - [observation/documented] The tool is framed as a virtual three-role team — Product Manager, Developer, and DevOps — that builds microservices from a natural-language description. -- evidence: [README.md#L9-L26](https://github.com/jina-ai/dev-gpt/blob/f6c151f93b02cc07fe6302e507927ea5f802a61e/README.md#L9-L26), [README.md#L28-L31](https://github.com/jina-ai/dev-gpt/blob/f6c151f93b02cc07fe6302e507927ea5f802a61e/README.md#L28-L31), [README.md#L57-L59](https://github.com/jina-ai/dev-gpt/blob/f6c151f93b02cc07fe6302e507927ea5f802a61e/README.md#L57-L59)
  - [observation/documented] The model choice is user-selectable between gpt-3.5-turbo and gpt-4, with gpt-3.5-turbo described as roughly 10x cheaper but less capable of complex microservices; default is the largest model the key can access. -- evidence: [README.md#L85-L95](https://github.com/jina-ai/dev-gpt/blob/f6c151f93b02cc07fe6302e507927ea5f802a61e/README.md#L85-L95)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributors are invited to open PRs or issues, and a checklist of next steps and nice-to-haves (e.g. verifying Windows/Linux support, adding tests, cleaning up duplicate code) is maintained in the README. -- evidence: [README.md#L524-L525](https://github.com/jina-ai/dev-gpt/blob/f6c151f93b02cc07fe6302e507927ea5f802a61e/README.md#L524-L525), [README.md#L527-L531](https://github.com/jina-ai/dev-gpt/blob/f6c151f93b02cc07fe6302e507927ea5f802a61e/README.md#L527-L531), [README.md#L534-L563](https://github.com/jina-ai/dev-gpt/blob/f6c151f93b02cc07fe6302e507927ea5f802a61e/README.md#L534-L563)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] Dev-GPT is a CLI tool with subcommands including generate, run, deploy, and configure, invoked as 'dev-gpt <command>' with flags like --description, --model, and --path. -- evidence: [README.md#L103-L107](https://github.com/jina-ai/dev-gpt/blob/f6c151f93b02cc07fe6302e507927ea5f802a61e/README.md#L103-L107), [README.md#L110-L115](https://github.com/jina-ai/dev-gpt/blob/f6c151f93b02cc07fe6302e507927ea5f802a61e/README.md#L110-L115), [README.md#L69-L77](https://github.com/jina-ai/dev-gpt/blob/f6c151f93b02cc07fe6302e507927ea5f802a61e/README.md#L69-L77), [README.md#L85-L95](https://github.com/jina-ai/dev-gpt/blob/f6c151f93b02cc07fe6302e507927ea5f802a61e/README.md#L85-L95), [README.md#L63-L66](https://github.com/jina-ai/dev-gpt/blob/f6c151f93b02cc07fe6302e507927ea5f802a61e/README.md#L63-L66)
  - [observation/documented] After a successful build the tool pushes the Docker image to a registry, deploys the microservice, and generates a Streamlit playground for testing it in the browser. -- evidence: [README.md#L103-L107](https://github.com/jina-ai/dev-gpt/blob/f6c151f93b02cc07fe6302e507927ea5f802a61e/README.md#L103-L107), [README.md#L505-L517](https://github.com/jina-ai/dev-gpt/blob/f6c151f93b02cc07fe6302e507927ea5f802a61e/README.md#L505-L517), [README.md#L497-L497](https://github.com/jina-ai/dev-gpt/blob/f6c151f93b02cc07fe6302e507927ea5f802a61e/README.md#L497-L497), [README.md#L499-L499](https://github.com/jina-ai/dev-gpt/blob/f6c151f93b02cc07fe6302e507927ea5f802a61e/README.md#L499-L499)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (1 claim(s)):
  - [observation/documented] Generation works by proposing multiple implementation strategies, generating code plus tests and a Dockerfile per strategy, building the image, and using build error messages to retry; after 10 consecutive failures it moves to the next strategy. -- evidence: [README.md#L505-L517](https://github.com/jina-ai/dev-gpt/blob/f6c151f93b02cc07fe6302e507927ea5f802a61e/README.md#L505-L517), [README.md#L485-L485](https://github.com/jina-ai/dev-gpt/blob/f6c151f93b02cc07fe6302e507927ea5f802a61e/README.md#L485-L485), [README.md#L491-L491](https://github.com/jina-ai/dev-gpt/blob/f6c151f93b02cc07fe6302e507927ea5f802a61e/README.md#L491-L491), [README.md#L473-L473](https://github.com/jina-ai/dev-gpt/blob/f6c151f93b02cc07fe6302e507927ea5f802a61e/README.md#L473-L473), [README.md#L493-L493](https://github.com/jina-ai/dev-gpt/blob/f6c151f93b02cc07fe6302e507927ea5f802a61e/README.md#L493-L493)
- tools-permissions (1 claim(s)):
  - [observation/documented] The product requires an OpenAI API key with gpt-4 access (gpt-3.5-turbo also accepted for generation), and optionally GOOGLE_API_KEY and GOOGLE_CSE_ID to enable web-content search. -- evidence: [README.md#L79-L81](https://github.com/jina-ai/dev-gpt/blob/f6c151f93b02cc07fe6302e507927ea5f802a61e/README.md#L79-L81), [README.md#L69-L77](https://github.com/jina-ai/dev-gpt/blob/f6c151f93b02cc07fe6302e507927ea5f802a61e/README.md#L69-L77), [README.md#L85-L95](https://github.com/jina-ai/dev-gpt/blob/f6c151f93b02cc07fe6302e507927ea5f802a61e/README.md#L85-L95)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
  - [observation/documented] Runtime dependencies include jina 3.15.1.dev14, openai>=0.27.5, langchain 0.0.153, streamlit 1.9.0, jcloud, jina-hubble-sdk, click, psutil, and pinned pydantic/typing packages. -- evidence: [requirements.txt#L1-L12](https://github.com/jina-ai/dev-gpt/blob/f6c151f93b02cc07fe6302e507927ea5f802a61e/requirements.txt#L1-L12)
More evidence: [full detail](dev-gpt.detail.md)

Metadata and full claim list: [full detail](dev-gpt.detail.md)
Human notes ([notes](dev-gpt.notes.md), never overwritten by build)

[Back to map index](../../index.md)
