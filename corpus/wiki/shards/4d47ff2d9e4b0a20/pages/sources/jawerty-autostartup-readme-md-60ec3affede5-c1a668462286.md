---
access: public
aliases: []
claim_ids:
- clm_03f981cf2c902ccc1daffcf76bae77443a3f523f337e86d69440a7abc517f042
- clm_0ab916c3efe008be414fa2ccfd5278d9020c8eb71e177e005c353323f46a595c
- clm_1f99275eda3b8e236020dc3c1e82cd1b5226701781b1edbe829d5f0a48b057b7
- clm_38b485dc506ba15a8ba029d71bfdf5df6e1e021a484369752ec567cc79a63503
- clm_54e77c15b00d3c43644506d1fb6c9a1dc4fccf81154e07fe5415cfebc2a399a4
- clm_ba076d4464309fb6940ee9230e3fcd833970ecbee8d926fed397bcaf94a73e9c
- clm_da475bc54ded7368025a0f32fe5554efa950d538fad8b614274cf1a1f0e57725
- clm_e533d32d7e4c6dbf8d6c4aae136d494851c553afa76707031aa53b93c9a0cbba
maturity: draft
page_id: pg_e0507ef411425442a2f9c1a668462286
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_aa8758de49ac5a1c8536c34db7f58f23
title: jawerty/AutoStartup/README.md @ 60ec3affede5
updated_at: '2026-09-14T02:06:51Z'
---

# jawerty/AutoStartup/README.md @ 60ec3affede5

<!-- rcw:begin owner=source:src_aa8758de49ac5a1c8536c34db7f58f23 block=evidence -->
- The user-facing input is a free-text 'intuition' (e.g. 'I think a website for dogsitters would be cool'), and an optional final step applies pivots based on user feedback. [@claim:clm_03f981cf2c902ccc1daffcf76bae77443a3f523f337e86d69440a7abc517f042]
- Repository development practice: to run from source, install dependencies with pip3 install -r requirements.txt (after Llama 2 access and huggingface-cli login) and run the main loop with python3 main.py; a Google Colab notebook is offered for quick testing. [@claim:clm_0ab916c3efe008be414fa2ccfd5278d9020c8eb71e177e005c353323f46a595c]
- The project is described as a Llama 2 autonomous agent that devises a startup idea, business plans, and React codebases from a simple user 'intuition'. [@claim:clm_1f99275eda3b8e236020dc3c1e82cd1b5226701781b1edbe829d5f0a48b057b7]
- The agent runs an idea loop: it develops a business idea and plan, iterates via a criticism loop that regenerates the plan, and asks an 'investor' prompt for approval, restarting on disapproval. [@claim:clm_38b485dc506ba15a8ba029d71bfdf5df6e1e021a484369752ec567cc79a63503]
- The project advertises 100% Llama 2 inference with no OpenAI keys necessary, and applies lean startup concepts such as pivots and a tight MVP build loop. [@claim:clm_54e77c15b00d3c43644506d1fb6c9a1dc4fccf81154e07fe5415cfebc2a399a4]
- The author notes the model needs a quality GPU to load the Llama 2 13b chat model, and a TODO says the React coding output needs bug fixing more often than not. [@claim:clm_ba076d4464309fb6940ee9230e3fcd833970ecbee8d926fed397bcaf94a73e9c]
- The README claims memory via vector search over historically successful ideas paired with intuitions, and that previous criticisms are used for investor approvals. [@claim:clm_da475bc54ded7368025a0f32fe5554efa950d538fad8b614274cf1a1f0e57725]
- After plan approval, the agent generates a React codebase using the author's separate 10x-React-Engineer project. [@claim:clm_e533d32d7e4c6dbf8d6c4aae136d494851c553afa76707031aa53b93c9a0cbba]
<!-- rcw:end owner=source:src_aa8758de49ac5a1c8536c34db7f58f23 block=evidence -->

## Researcher notes

