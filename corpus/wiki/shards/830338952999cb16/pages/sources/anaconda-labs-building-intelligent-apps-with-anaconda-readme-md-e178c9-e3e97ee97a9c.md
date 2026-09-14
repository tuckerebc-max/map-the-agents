---
access: public
aliases: []
claim_ids:
- clm_05c49c7f061f2577c264bfed044d9cf5699043cb7bfddeb4d99a52ce7f1cee4e
- clm_0cc75a22024aad26e8453bee1a5cc33e8ed64977c296bd49f5a99b3a2fc3365b
- clm_13e9b53afeb5b1ad5683251ca565c447384cb764940cdab88d9081fae6ba443c
- clm_31195ee357d60e1e935e1089b12926ea4413d7f06cc344ce6ff1c2d0ae05e2dd
- clm_3158b8cb060794bf05d52211b89716dc03385b2210d9fa9d05dfbc5b2252dc7f
- clm_4339294350734eaa18b2b393ea07acf402d37b655856e01e5a3c2e18a6bde4e8
- clm_5b235ada0b054a12ce2cf13e967dc354b11e830b1e3eb53c2007eeeff5817918
- clm_708e8213cbef4edeadd0e6bce91ab5690be99c80743a5c016f5248266cbcb0f8
- clm_7983e151a1f8bce73529748f71f650ca916d0b64a78b239a8c5a8da4b009d2ef
- clm_8222af8f603c45275c6dd83c3cf5757b5f6763f95a0e357de8cbd6f91ba5f55c
- clm_951a8996036178eb825f1eb437f925b2e4931fc271d360103f429c358923e3ed
- clm_b344a7464127cffa6abd53d81c9a7c4817f507c424c098f0d167cb985faba34a
- clm_d98cb2d625d1c5e6360346843fb38fa933fd5b4fb95dc6ff97017b7792b69b64
- clm_e6934df5417b0f87f2df25e5713839db5b8778cd40cd67c1192276f92595ee74
maturity: draft
page_id: pg_35c82857eaa45c9f8368e3e97ee97a9c
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_95f7dcd2167a521890fbe5f9549a96b4
title: Anaconda-Labs/building-intelligent-apps-with-anaconda/README.md @ e178c9baf99f
updated_at: '2026-09-14T03:33:51Z'
---

# Anaconda-Labs/building-intelligent-apps-with-anaconda/README.md @ e178c9baf99f

<!-- rcw:begin owner=source:src_95f7dcd2167a521890fbe5f9549a96b4 block=evidence -->
- All modules share one dataset: NASA TESS phase-folded light-curve data for exoplanet WASP-18 b, with the CSV bundled in each module that uses it. [@claim:clm_05c49c7f061f2577c264bfed044d9cf5699043cb7bfddeb4d99a52ce7f1cee4e]
- The repo is a hands-on curriculum of self-contained modules, each under ~7 minutes, delivered as narrated demos with pre-run outputs or a run_demo.sh script. [@claim:clm_0cc75a22024aad26e8453bee1a5cc33e8ed64977c296bd49f5a99b3a2fc3365b]
- Module 06 implements eval-as-CI: an evaluate step runs assertion functions from evals/assertions.py on every execution, raising AssertionError on critical failures. [@claim:clm_13e9b53afeb5b1ad5683251ca565c447384cb764940cdab88d9081fae6ba443c]
- The material targets software engineers, AI/ML engineers, and data scientists, and was built as Anaconda demos for PyCon US 2026 under an MIT license. [@claim:clm_31195ee357d60e1e935e1089b12926ea4413d7f06cc344ce6ff1c2d0ae05e2dd]
- The curriculum requires conda 26.5.x or later, and each module ships its own environment.yml intended to be created in module order. [@claim:clm_3158b8cb060794bf05d52211b89716dc03385b2210d9fa9d05dfbc5b2252dc7f]
- Module -1 covers the Model Context Protocol via anaconda-mcp and Claude Desktop, letting an AI assistant manage environments, query packages, and inspect CVEs. [@claim:clm_4339294350734eaa18b2b393ea07acf402d37b655856e01e5a3c2e18a6bde4e8]
- The pipeline payload (ingestion.py and ValidationReport) is deliberately invariant across modules; only where it runs and what reasons about it changes. [@claim:clm_5b235ada0b054a12ce2cf13e967dc354b11e830b1e3eb53c2007eeeff5817918]
- Module 07 uses conda-lockfiles to pin environment.yml into a reproducible deployment contract, anaconda-audit for NVD/NIST CVE scanning, and conda-pack for offline deployment. [@claim:clm_708e8213cbef4edeadd0e6bce91ab5690be99c80743a5c016f5248266cbcb0f8]
- Module 04 shows LLM backends (AI Navigator, self-hosted vLLM, Anaconda Platform) are swapped by changing a single base_url environment variable with no agent code changes. [@claim:clm_7983e151a1f8bce73529748f71f650ca916d0b64a78b239a8c5a8da4b009d2ef]
- Module 06 adds a DuckDB embedded vector store as agent memory: past ValidationReport results are retrieved by cosine similarity and injected into the system prompt. [@claim:clm_8222af8f603c45275c6dd83c3cf5757b5f6763f95a0e357de8cbd6f91ba5f55c]
- Modules 05 (GPU acceleration) and 08 (native apps) are labeled experimental with unknown duration, and NemoClaw is described as an alpha sandboxed agent runtime. [@claim:clm_951a8996036178eb825f1eb437f925b2e4931fc271d360103f429c358923e3ed]
- Module 01 uses IsolationForest for unsupervised transit anomaly detection on the light curve, with Polars, scikit-learn, and Pydantic as its tools. [@claim:clm_b344a7464127cffa6abd53d81c9a7c4817f507c424c098f0d167cb985faba34a]
- Module 03 coordinates DataAgent and AnalysisAgent via a LangGraph supervisor, wrapped in a Metaflow FlowSpec with per-agent-role isolated, lockable conda environments. [@claim:clm_d98cb2d625d1c5e6360346843fb38fa933fd5b4fb95dc6ff97017b7792b69b64]
- Module 01 provides ingestion.py with load_lightcurve and validate_lightcurve functions, schema enforcement, and a typed, JSON-serialisable Pydantic ValidationReport consumed by later modules. [@claim:clm_e6934df5417b0f87f2df25e5713839db5b8778cd40cd67c1192276f92595ee74]
<!-- rcw:end owner=source:src_95f7dcd2167a521890fbe5f9549a96b4 block=evidence -->

## Researcher notes

