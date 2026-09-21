# anaconda-labs/building-intelligent-apps-with-anaconda

Status: distilled - Freshness: stale
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 88c74290e89c @ 8a7c504ab8ae2407

## Summary (orientation draft, not independently verified)

The repository is a README-documented hands-on curriculum for building intelligent apps with the Anaconda ecosystem, built around a WASP-18 b exoplanet light-curve pipeline spanning conda environments, agents, deployment, supply-chain security, and app delivery. Evidence is documentation-only; no source code slices are present. Evidence coverage: 174 of 192 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 14 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

14 claim(s) across 10 facet(s); 3 facet(s) unknown.

- specifications (2 claim(s)):
  - [observation/documented] The repo is a hands-on curriculum of self-contained modules, each under ~7 minutes, delivered as narrated demos with pre-run outputs or a run_demo.sh script. -- evidence: [README.md#L7-L7](https://github.com/Anaconda-Labs/building-intelligent-apps-with-anaconda/blob/e178c9baf99f325cf0fb79c58b2e22244fc636bf/README.md#L7-L7)
  - [observation/documented] All modules share one dataset: NASA TESS phase-folded light-curve data for exoplanet WASP-18 b, with the CSV bundled in each module that uses it. -- evidence: [README.md#L352-L352](https://github.com/Anaconda-Labs/building-intelligent-apps-with-anaconda/blob/e178c9baf99f325cf0fb79c58b2e22244fc636bf/README.md#L352-L352), [README.md#L9-L9](https://github.com/Anaconda-Labs/building-intelligent-apps-with-anaconda/blob/e178c9baf99f325cf0fb79c58b2e22244fc636bf/README.md#L9-L9), [README.md#L358-L358](https://github.com/Anaconda-Labs/building-intelligent-apps-with-anaconda/blob/e178c9baf99f325cf0fb79c58b2e22244fc636bf/README.md#L358-L358)
- components (2 claim(s)):
  - [observation/documented] Module 01 provides ingestion.py with load_lightcurve and validate_lightcurve functions, schema enforcement, and a typed, JSON-serialisable Pydantic ValidationReport consumed by later modules. -- evidence: [README.md#L79-L79](https://github.com/Anaconda-Labs/building-intelligent-apps-with-anaconda/blob/e178c9baf99f325cf0fb79c58b2e22244fc636bf/README.md#L79-L79), [README.md#L87-L90](https://github.com/Anaconda-Labs/building-intelligent-apps-with-anaconda/blob/e178c9baf99f325cf0fb79c58b2e22244fc636bf/README.md#L87-L90)
  - [observation/documented] Module 01 uses IsolationForest for unsupervised transit anomaly detection on the light curve, with Polars, scikit-learn, and Pydantic as its tools. -- evidence: [README.md#L92-L92](https://github.com/Anaconda-Labs/building-intelligent-apps-with-anaconda/blob/e178c9baf99f325cf0fb79c58b2e22244fc636bf/README.md#L92-L92), [README.md#L79-L79](https://github.com/Anaconda-Labs/building-intelligent-apps-with-anaconda/blob/e178c9baf99f325cf0fb79c58b2e22244fc636bf/README.md#L79-L79)
- design-choices (1 claim(s)):
  - [observation/documented] The pipeline payload (ingestion.py and ValidationReport) is deliberately invariant across modules; only where it runs and what reasons about it changes. -- evidence: [README.md#L366-L367](https://github.com/Anaconda-Labs/building-intelligent-apps-with-anaconda/blob/e178c9baf99f325cf0fb79c58b2e22244fc636bf/README.md#L366-L367), [README.md#L49-L49](https://github.com/Anaconda-Labs/building-intelligent-apps-with-anaconda/blob/e178c9baf99f325cf0fb79c58b2e22244fc636bf/README.md#L49-L49)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] Module 04 shows LLM backends (AI Navigator, self-hosted vLLM, Anaconda Platform) are swapped by changing a single base_url environment variable with no agent code changes. -- evidence: [README.md#L128-L128](https://github.com/Anaconda-Labs/building-intelligent-apps-with-anaconda/blob/e178c9baf99f325cf0fb79c58b2e22244fc636bf/README.md#L128-L128), [README.md#L320-L332](https://github.com/Anaconda-Labs/building-intelligent-apps-with-anaconda/blob/e178c9baf99f325cf0fb79c58b2e22244fc636bf/README.md#L320-L332), [README.md#L130-L134](https://github.com/Anaconda-Labs/building-intelligent-apps-with-anaconda/blob/e178c9baf99f325cf0fb79c58b2e22244fc636bf/README.md#L130-L134)
  - [observation/documented] Module -1 covers the Model Context Protocol via anaconda-mcp and Claude Desktop, letting an AI assistant manage environments, query packages, and inspect CVEs. -- evidence: [README.md#L61-L61](https://github.com/Anaconda-Labs/building-intelligent-apps-with-anaconda/blob/e178c9baf99f325cf0fb79c58b2e22244fc636bf/README.md#L61-L61), [README.md#L59-L59](https://github.com/Anaconda-Labs/building-intelligent-apps-with-anaconda/blob/e178c9baf99f325cf0fb79c58b2e22244fc636bf/README.md#L59-L59)
- memory-state (1 claim(s)):
  - [observation/documented] Module 06 adds a DuckDB embedded vector store as agent memory: past ValidationReport results are retrieved by cosine similarity and injected into the system prompt. -- evidence: [README.md#L180-L187](https://github.com/Anaconda-Labs/building-intelligent-apps-with-anaconda/blob/e178c9baf99f325cf0fb79c58b2e22244fc636bf/README.md#L180-L187), [README.md#L191-L191](https://github.com/Anaconda-Labs/building-intelligent-apps-with-anaconda/blob/e178c9baf99f325cf0fb79c58b2e22244fc636bf/README.md#L191-L191)
- orchestration (1 claim(s)):
  - [observation/documented] Module 03 coordinates DataAgent and AnalysisAgent via a LangGraph supervisor, wrapped in a Metaflow FlowSpec with per-agent-role isolated, lockable conda environments. -- evidence: [README.md#L112-L112](https://github.com/Anaconda-Labs/building-intelligent-apps-with-anaconda/blob/e178c9baf99f325cf0fb79c58b2e22244fc636bf/README.md#L112-L112), [README.md#L120-L120](https://github.com/Anaconda-Labs/building-intelligent-apps-with-anaconda/blob/e178c9baf99f325cf0fb79c58b2e22244fc636bf/README.md#L120-L120)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation (1 claim(s)):
  - [observation/documented] Module 06 implements eval-as-CI: an evaluate step runs assertion functions from evals/assertions.py on every execution, raising AssertionError on critical failures. -- evidence: [README.md#L189-L189](https://github.com/Anaconda-Labs/building-intelligent-apps-with-anaconda/blob/e178c9baf99f325cf0fb79c58b2e22244fc636bf/README.md#L189-L189), [README.md#L180-L187](https://github.com/Anaconda-Labs/building-intelligent-apps-with-anaconda/blob/e178c9baf99f325cf0fb79c58b2e22244fc636bf/README.md#L180-L187)
More evidence: [full detail](building-intelligent-apps-with-anaconda.detail.md)

Metadata and full claim list: [full detail](building-intelligent-apps-with-anaconda.detail.md)
Human notes ([notes](building-intelligent-apps-with-anaconda.notes.md), never overwritten by build)

[Back to map index](../../index.md)
