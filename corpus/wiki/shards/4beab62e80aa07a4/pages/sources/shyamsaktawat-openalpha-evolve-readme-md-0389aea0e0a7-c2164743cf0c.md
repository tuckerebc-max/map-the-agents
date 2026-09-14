---
access: public
aliases: []
claim_ids:
- clm_0470886912073b1ea830fb09cd8cfedfda1ccf6f349ad9204baa7357ea6a5c2c
- clm_2d17cbaacef4034af336c7036a360980cdfa1ba58a500159940345894d9b8286
- clm_48c202c3ce22f3b37976a2cd5e94b20d6485fcba6b40620d8ae663c32e614a9a
- clm_4dcb233eec2d76efe1d0c6d69be71ef878aa36f552b92a7b53e3b7a4b4076e5c
- clm_656ee61ec88e72d115cd2a81cab3dedc00b97cbb46480cc385bd7143abc55fff
- clm_6bf311b4dca724d03b43287b96a02a33c550507a14b64c2b6ee2cdb0e439e31c
- clm_710932ecc951899eeb3f531edcef1c32a113e5a202758f0c3d54086eb987e9bf
- clm_b79a1dc768c450e1c2cad875a871deee50bb57fb581b1e65bff04c336a67a628
- clm_ecaa41cd141de451dc72c16f4ca94312bbdb29e0e16e2a60f65b482eddce663b
- clm_f39c37f4e2d1eb652be0cdf29566f1a8b473f6d390ad233480d9fccf288da4b2
maturity: draft
page_id: pg_ee39fe3ef40f53579a4bc2164743cf0c
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_db862ace9ca35dd5b26d6662abfe9500
title: shyamsaktawat/OpenAlpha_Evolve/README.md @ 0389aea0e0a7
updated_at: '2026-09-14T02:40:11Z'
---

# shyamsaktawat/OpenAlpha_Evolve/README.md @ 0389aea0e0a7

<!-- rcw:begin owner=source:src_db862ace9ca35dd5b26d6662abfe9500 block=evidence -->
- The DatabaseAgent stores programs with code, fitness scores, generation, and lineage as a record of evolutionary history; the README notes this storage is currently in-memory. [@claim:clm_0470886912073b1ea830fb09cd8cfedfda1ccf6f349ad9204baa7357ea6a5c2c]
- The README's disclaimer states this is an experimental project whose generated code may not always be optimal, correct, or secure, and should be reviewed and tested thoroughly before production use. [@claim:clm_2d17cbaacef4034af336c7036a360980cdfa1ba58a500159940345894d9b8286]
- Per the README feature list, generated code is executed in Docker containers for sandboxed evaluation, with configurable timeout mechanisms. [@claim:clm_48c202c3ce22f3b37976a2cd5e94b20d6485fcba6b40620d8ae663c32e614a9a]
- The system uses a modular agent architecture with named agents: PromptDesignerAgent, CodeGeneratorAgent, EvaluatorAgent, DatabaseAgent, SelectionControllerAgent, and a task_manager agent that orchestrates the evolutionary loop and coordinates the others. [@claim:clm_4dcb233eec2d76efe1d0c6d69be71ef878aa36f552b92a7b53e3b7a4b4076e5c]
- The CLI entry point runs an evolutionary run via 'python -m main <task.yaml>' (e.g., examples/shortest_path.yaml), with logs also saved to alpha_evolve.log by default. [@claim:clm_656ee61ec88e72d115cd2a81cab3dedc00b97cbb46480cc385bd7143abc55fff]
- Mutation and bug-fix prompts often request changes in diff format, and the code generator attempts to apply received diffs to the parent code; the features list describes diff-based mutations for targeted modifications. [@claim:clm_6bf311b4dca724d03b43287b96a02a33c550507a14b64c2b6ee2cdb0e439e31c]
- Repository development practice: contributors are asked to report bugs or suggest features via GitHub issues, and to fork the repo, create a feature branch, write clean documented code, add tests if applicable, avoid breaking existing functionality, and submit pull requests with clear descriptions. [@claim:clm_710932ecc951899eeb3f531edcef1c32a113e5a202758f0c3d54086eb987e9bf]
- The EvaluatorAgent syntax-checks generated code, executes it in an isolated environment against task input/output examples, and scores fitness based on correctness (test cases passed), runtime efficiency, and other potential metrics. [@claim:clm_b79a1dc768c450e1c2cad875a871deee50bb57fb581b1e65bff04c336a67a628]
- A Gradio web interface is started with 'python app.py'; it displays a local URL (e.g., http://127.0.0.1:7860) and optionally a public share link, where users can define custom tasks and run evolution interactively. [@claim:clm_ecaa41cd141de451dc72c16f4ca94312bbdb29e0e16e2a60f65b482eddce663b]
- The README prerequisites require Python 3.10+, pip, git, and a running Docker installation (Docker Desktop on Windows/Mac or Docker Engine on Linux) for sandboxed code evaluation. [@claim:clm_f39c37f4e2d1eb652be0cdf29566f1a8b473f6d390ad233480d9fccf288da4b2]
<!-- rcw:end owner=source:src_db862ace9ca35dd5b26d6662abfe9500 block=evidence -->

## Researcher notes

