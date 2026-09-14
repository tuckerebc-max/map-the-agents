---
access: public
aliases: []
claim_ids:
- clm_11771a83fd64612c8462414f77b531d486d54b8c7c1a7ad9a469a84af2d9e948
- clm_3a406f1e7d53169fdd03a29a6f057fce81f418c3194289a280cb76002b069a1f
- clm_4f93c94b63b119621611663f37aa538a468dca692ee504e0b547ff8c7613123a
- clm_54b58b6d0a5c1e945e0c146d8b7160eee06595aea930d4752cff47f2517f7bc9
- clm_62d63044e7ae160cd48c5226b94e6b0c112ccd1b515c44593097eac9278cff9d
- clm_71eef01b6fe735bbaf83a10d016d4575cce8f208b86fd730d209b726ba376965
- clm_826bdb0c3af275c202de633d42ee08bb9adbe977fd9e56fe71feb72d9537a628
- clm_ed1a5d4ac8f6de2bd175cbc529086c3d4096479c133a803f95cf4269a83966fd
- clm_fa5e491a027fb1098749bff86127bc7319c898af3ad5b9c4fbc881ab04f29652
maturity: draft
page_id: pg_72da27eea7c556b2883f3e3e2237cf14
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_8a22e0436f8c5d298ad5d60b68217ed2
title: kreneskyp/ix/README.md @ d5868fc1d56d
updated_at: '2026-09-14T03:09:30Z'
---

# kreneskyp/ix/README.md @ d5868fc1d56d

<!-- rcw:begin owner=source:src_8a22e0436f8c5d298ad5d60b68217ed2 block=evidence -->
- IX is described as a platform for designing and deploying autonomous and semi-autonomous LLM agents and workflows that can run in parallel and communicate with each other. [@claim:clm_11771a83fd64612c8462414f77b531d486d54b8c7c1a7ad9a469a84af2d9e948]
- Supported model providers are listed as OpenAI, with Google PaLM, Anthropic, and Llama marked experimental. [@claim:clm_3a406f1e7d53169fdd03a29a6f057fce81f418c3194289a280cb76002b069a1f]
- The agent-ix CLI starts a preconfigured docker-compose cluster, downloads required images, supports scaling workers (e.g. 'ix scale 5'), and can launch a dev version image. [@claim:clm_4f93c94b63b119621611663f37aa538a468dca692ee504e0b547ff8c7613123a]
- The product includes a no-code agent editor where users drop and connect nodes into a graph representing an agent's cognitive logic, with embedded chat for testing and debugging. [@claim:clm_54b58b6d0a5c1e945e0c146d8b7160eee06595aea930d4752cff47f2517f7bc9]
- Repository development practice: agent fixtures can be dumped with the dump_agent Django management command, which gathers the agent, chain, and component graph. [@claim:clm_62d63044e7ae160cd48c5226b94e6b0c112ccd1b515c44593097eac9278cff9d]
- A multi-agent chat interface lets users interact with teams of agents; a default IX moderator agent delegates tasks, and specific agents can be targeted via @mentions. [@claim:clm_71eef01b6fe735bbaf83a10d016d4575cce8f208b86fd730d209b726ba376965]
- The agent runner backend is dockerized and triggered via a celery message queue, allowing horizontal scaling of agents running in parallel. [@claim:clm_826bdb0c3af275c202de633d42ee08bb9adbe977fd9e56fe71feb72d9537a628]
- IX implements a component config layer mapping LangChain components to a configuration graph, which dynamically renders nodes and forms in the no-code editor. [@claim:clm_ed1a5d4ac8f6de2bd175cbc529086c3d4096479c133a803f95cf4269a83966fd]
- The smart input bar auto-completes agent @mentions and file/data artifacts created by tasks. [@claim:clm_fa5e491a027fb1098749bff86127bc7319c898af3ad5b9c4fbc881ab04f29652]
<!-- rcw:end owner=source:src_8a22e0436f8c5d298ad5d60b68217ed2 block=evidence -->

## Researcher notes

