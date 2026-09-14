# anaconda-labs/building-intelligent-apps-with-anaconda -- full detail

[Back to orientation](building-intelligent-apps-with-anaconda.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/anaconda-labs/building-intelligent-apps-with-anaconda/e178c9baf99f325cf0fb79c58b2e22244fc636bf/33cc142722d4db88.json](../../../wiki/dossiers/anaconda-labs/building-intelligent-apps-with-anaconda/e178c9baf99f325cf0fb79c58b2e22244fc636bf/33cc142722d4db88.json)

## specifications (2 claim(s))

- [observation/documented] The repo is a hands-on curriculum of self-contained modules, each under ~7 minutes, delivered as narrated demos with pre-run outputs or a run_demo.sh script. -- evidence: [README.md#L7-L7](https://github.com/Anaconda-Labs/building-intelligent-apps-with-anaconda/blob/e178c9baf99f325cf0fb79c58b2e22244fc636bf/README.md#L7-L7) (`clm_0cc75a22024aad26e8453bee1a5cc33e8ed64977c296bd49f5a99b3a2fc3365b`)
- [observation/documented] All modules share one dataset: NASA TESS phase-folded light-curve data for exoplanet WASP-18 b, with the CSV bundled in each module that uses it. -- evidence: [README.md#L352-L352](https://github.com/Anaconda-Labs/building-intelligent-apps-with-anaconda/blob/e178c9baf99f325cf0fb79c58b2e22244fc636bf/README.md#L352-L352), [README.md#L9-L9](https://github.com/Anaconda-Labs/building-intelligent-apps-with-anaconda/blob/e178c9baf99f325cf0fb79c58b2e22244fc636bf/README.md#L9-L9), [README.md#L358-L358](https://github.com/Anaconda-Labs/building-intelligent-apps-with-anaconda/blob/e178c9baf99f325cf0fb79c58b2e22244fc636bf/README.md#L358-L358) (`clm_05c49c7f061f2577c264bfed044d9cf5699043cb7bfddeb4d99a52ce7f1cee4e`)

## components (2 claim(s))

- [observation/documented] Module 01 provides ingestion.py with load_lightcurve and validate_lightcurve functions, schema enforcement, and a typed, JSON-serialisable Pydantic ValidationReport consumed by later modules. -- evidence: [README.md#L79-L79](https://github.com/Anaconda-Labs/building-intelligent-apps-with-anaconda/blob/e178c9baf99f325cf0fb79c58b2e22244fc636bf/README.md#L79-L79), [README.md#L87-L90](https://github.com/Anaconda-Labs/building-intelligent-apps-with-anaconda/blob/e178c9baf99f325cf0fb79c58b2e22244fc636bf/README.md#L87-L90) (`clm_e6934df5417b0f87f2df25e5713839db5b8778cd40cd67c1192276f92595ee74`)
- [observation/documented] Module 01 uses IsolationForest for unsupervised transit anomaly detection on the light curve, with Polars, scikit-learn, and Pydantic as its tools. -- evidence: [README.md#L92-L92](https://github.com/Anaconda-Labs/building-intelligent-apps-with-anaconda/blob/e178c9baf99f325cf0fb79c58b2e22244fc636bf/README.md#L92-L92), [README.md#L79-L79](https://github.com/Anaconda-Labs/building-intelligent-apps-with-anaconda/blob/e178c9baf99f325cf0fb79c58b2e22244fc636bf/README.md#L79-L79) (`clm_b344a7464127cffa6abd53d81c9a7c4817f507c424c098f0d167cb985faba34a`)

## design-choices (1 claim(s))

- [observation/documented] The pipeline payload (ingestion.py and ValidationReport) is deliberately invariant across modules; only where it runs and what reasons about it changes. -- evidence: [README.md#L366-L367](https://github.com/Anaconda-Labs/building-intelligent-apps-with-anaconda/blob/e178c9baf99f325cf0fb79c58b2e22244fc636bf/README.md#L366-L367), [README.md#L49-L49](https://github.com/Anaconda-Labs/building-intelligent-apps-with-anaconda/blob/e178c9baf99f325cf0fb79c58b2e22244fc636bf/README.md#L49-L49) (`clm_5b235ada0b054a12ce2cf13e967dc354b11e830b1e3eb53c2007eeeff5817918`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] Module 04 shows LLM backends (AI Navigator, self-hosted vLLM, Anaconda Platform) are swapped by changing a single base_url environment variable with no agent code changes. -- evidence: [README.md#L128-L128](https://github.com/Anaconda-Labs/building-intelligent-apps-with-anaconda/blob/e178c9baf99f325cf0fb79c58b2e22244fc636bf/README.md#L128-L128), [README.md#L320-L332](https://github.com/Anaconda-Labs/building-intelligent-apps-with-anaconda/blob/e178c9baf99f325cf0fb79c58b2e22244fc636bf/README.md#L320-L332), [README.md#L130-L134](https://github.com/Anaconda-Labs/building-intelligent-apps-with-anaconda/blob/e178c9baf99f325cf0fb79c58b2e22244fc636bf/README.md#L130-L134) (`clm_7983e151a1f8bce73529748f71f650ca916d0b64a78b239a8c5a8da4b009d2ef`)
- [observation/documented] Module -1 covers the Model Context Protocol via anaconda-mcp and Claude Desktop, letting an AI assistant manage environments, query packages, and inspect CVEs. -- evidence: [README.md#L61-L61](https://github.com/Anaconda-Labs/building-intelligent-apps-with-anaconda/blob/e178c9baf99f325cf0fb79c58b2e22244fc636bf/README.md#L61-L61), [README.md#L59-L59](https://github.com/Anaconda-Labs/building-intelligent-apps-with-anaconda/blob/e178c9baf99f325cf0fb79c58b2e22244fc636bf/README.md#L59-L59) (`clm_4339294350734eaa18b2b393ea07acf402d37b655856e01e5a3c2e18a6bde4e8`)

## memory-state (1 claim(s))

- [observation/documented] Module 06 adds a DuckDB embedded vector store as agent memory: past ValidationReport results are retrieved by cosine similarity and injected into the system prompt. -- evidence: [README.md#L180-L187](https://github.com/Anaconda-Labs/building-intelligent-apps-with-anaconda/blob/e178c9baf99f325cf0fb79c58b2e22244fc636bf/README.md#L180-L187), [README.md#L191-L191](https://github.com/Anaconda-Labs/building-intelligent-apps-with-anaconda/blob/e178c9baf99f325cf0fb79c58b2e22244fc636bf/README.md#L191-L191) (`clm_8222af8f603c45275c6dd83c3cf5757b5f6763f95a0e357de8cbd6f91ba5f55c`)

## orchestration (1 claim(s))

- [observation/documented] Module 03 coordinates DataAgent and AnalysisAgent via a LangGraph supervisor, wrapped in a Metaflow FlowSpec with per-agent-role isolated, lockable conda environments. -- evidence: [README.md#L112-L112](https://github.com/Anaconda-Labs/building-intelligent-apps-with-anaconda/blob/e178c9baf99f325cf0fb79c58b2e22244fc636bf/README.md#L112-L112), [README.md#L120-L120](https://github.com/Anaconda-Labs/building-intelligent-apps-with-anaconda/blob/e178c9baf99f325cf0fb79c58b2e22244fc636bf/README.md#L120-L120) (`clm_d98cb2d625d1c5e6360346843fb38fa933fd5b4fb95dc6ff97017b7792b69b64`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (1 claim(s))

- [observation/documented] Module 06 implements eval-as-CI: an evaluate step runs assertion functions from evals/assertions.py on every execution, raising AssertionError on critical failures. -- evidence: [README.md#L189-L189](https://github.com/Anaconda-Labs/building-intelligent-apps-with-anaconda/blob/e178c9baf99f325cf0fb79c58b2e22244fc636bf/README.md#L189-L189), [README.md#L180-L187](https://github.com/Anaconda-Labs/building-intelligent-apps-with-anaconda/blob/e178c9baf99f325cf0fb79c58b2e22244fc636bf/README.md#L180-L187) (`clm_13e9b53afeb5b1ad5683251ca565c447384cb764940cdab88d9081fae6ba443c`)

## dependencies (2 claim(s))

- [observation/documented] Module 07 uses conda-lockfiles to pin environment.yml into a reproducible deployment contract, anaconda-audit for NVD/NIST CVE scanning, and conda-pack for offline deployment. -- evidence: [README.md#L202-L210](https://github.com/Anaconda-Labs/building-intelligent-apps-with-anaconda/blob/e178c9baf99f325cf0fb79c58b2e22244fc636bf/README.md#L202-L210), [README.md#L212-L216](https://github.com/Anaconda-Labs/building-intelligent-apps-with-anaconda/blob/e178c9baf99f325cf0fb79c58b2e22244fc636bf/README.md#L212-L216) (`clm_708e8213cbef4edeadd0e6bce91ab5690be99c80743a5c016f5248266cbcb0f8`)
- [observation/documented] The curriculum requires conda 26.5.x or later, and each module ships its own environment.yml intended to be created in module order. -- evidence: [README.md#L346-L346](https://github.com/Anaconda-Labs/building-intelligent-apps-with-anaconda/blob/e178c9baf99f325cf0fb79c58b2e22244fc636bf/README.md#L346-L346), [README.md#L340-L340](https://github.com/Anaconda-Labs/building-intelligent-apps-with-anaconda/blob/e178c9baf99f325cf0fb79c58b2e22244fc636bf/README.md#L340-L340) (`clm_3158b8cb060794bf05d52211b89716dc03385b2210d9fa9d05dfbc5b2252dc7f`)

## limitations (1 claim(s))

- [observation/documented] Modules 05 (GPU acceleration) and 08 (native apps) are labeled experimental with unknown duration, and NemoClaw is described as an alpha sandboxed agent runtime. -- evidence: [README.md#L23-L46](https://github.com/Anaconda-Labs/building-intelligent-apps-with-anaconda/blob/e178c9baf99f325cf0fb79c58b2e22244fc636bf/README.md#L23-L46), [README.md#L160-L164](https://github.com/Anaconda-Labs/building-intelligent-apps-with-anaconda/blob/e178c9baf99f325cf0fb79c58b2e22244fc636bf/README.md#L160-L164), [README.md#L145-L146](https://github.com/Anaconda-Labs/building-intelligent-apps-with-anaconda/blob/e178c9baf99f325cf0fb79c58b2e22244fc636bf/README.md#L145-L146) (`clm_951a8996036178eb825f1eb437f925b2e4931fc271d360103f429c358923e3ed`)

## relevance (1 claim(s))

- [observation/documented] The material targets software engineers, AI/ML engineers, and data scientists, and was built as Anaconda demos for PyCon US 2026 under an MIT license. -- evidence: [README.md#L364-L364](https://github.com/Anaconda-Labs/building-intelligent-apps-with-anaconda/blob/e178c9baf99f325cf0fb79c58b2e22244fc636bf/README.md#L364-L364), [README.md#L383-L383](https://github.com/Anaconda-Labs/building-intelligent-apps-with-anaconda/blob/e178c9baf99f325cf0fb79c58b2e22244fc636bf/README.md#L383-L383), [README.md#L369-L372](https://github.com/Anaconda-Labs/building-intelligent-apps-with-anaconda/blob/e178c9baf99f325cf0fb79c58b2e22244fc636bf/README.md#L369-L372) (`clm_31195ee357d60e1e935e1089b12926ea4413d7f06cc344ce6ff1c2d0ae05e2dd`)

