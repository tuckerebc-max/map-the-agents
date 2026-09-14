# openautocoder/live-swe-agent -- full detail

[Back to orientation](live-swe-agent.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/openautocoder/live-swe-agent/8d7dd8634580d1e09320b4c27d70380bc9ae74a8/f59c96dca85cc602.json](../../../wiki/dossiers/openautocoder/live-swe-agent/8d7dd8634580d1e09320b4c27d70380bc9ae74a8/f59c96dca85cc602.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] Complete trajectories, patches, and results for SWE-bench Verified and SWE-Bench Pro runs are published as release artifacts and Hugging Face datasets. -- evidence: [README.md#L71-L73](https://github.com/OpenAutoCoder/live-swe-agent/blob/8d7dd8634580d1e09320b4c27d70380bc9ae74a8/README.md#L71-L73), [README.md#L75-L75](https://github.com/OpenAutoCoder/live-swe-agent/blob/8d7dd8634580d1e09320b4c27d70380bc9ae74a8/README.md#L75-L75) (`clm_bdbbbe8ee4b35a8e3672751a527d69a008ced067b8bec7bf946c2bc25f55a0f0`)

## design-choices (1 claim(s))

- [observation/documented] The agent is described as a live, runtime self-evolving software engineering agent that expands and revises its own capabilities while working on a real-world issue. -- evidence: [README.md#L24-L25](https://github.com/OpenAutoCoder/live-swe-agent/blob/8d7dd8634580d1e09320b4c27d70380bc9ae74a8/README.md#L24-L25) (`clm_a61d2ead309ce6c68c7ac0f0068086f825f48df1ac2a9bac2672ffca33373592`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] The agent is run via the mini CLI with a custom config file, e.g. `mini --config config/livesweagent.yaml`, with additional details in the config folder. -- evidence: [README.md#L63-L65](https://github.com/OpenAutoCoder/live-swe-agent/blob/8d7dd8634580d1e09320b4c27d70380bc9ae74a8/README.md#L63-L65), [README.md#L67-L67](https://github.com/OpenAutoCoder/live-swe-agent/blob/8d7dd8634580d1e09320b4c27d70380bc9ae74a8/README.md#L67-L67) (`clm_7bc19d50be447dcbfa54b8ddebc365320b5f4934f5083d4b0c4f9d2447f7aee9`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (4 claim(s))

- [observation/documented] The README reports Claude Opus 4.5 with Live-SWE-agent scoring 79.2% on SWE-bench Verified, claimed to lead open-source scaffolds. -- evidence: [README.md#L29-L32](https://github.com/OpenAutoCoder/live-swe-agent/blob/8d7dd8634580d1e09320b4c27d70380bc9ae74a8/README.md#L29-L32) (`clm_f97403cc6d672a1b514a35357b067a8462650096440921437d47b2855ce28b00`)
- [observation/documented] The README reports a 45.8% solve rate on SWE-Bench Pro, described as a state-of-the-art result as of Nov 17, 2025. -- evidence: [README.md#L29-L32](https://github.com/OpenAutoCoder/live-swe-agent/blob/8d7dd8634580d1e09320b4c27d70380bc9ae74a8/README.md#L29-L32) (`clm_b79217b3d1b1768243712e81157a9a0ca75f2729cbb77e0e861834e3bc1c7d5c`)
- [observation/documented] The project maintains a leaderboard where models are evaluated with Live-SWE-agent to enable apples-to-apples comparison of model capabilities. -- evidence: [README.md#L38-L38](https://github.com/OpenAutoCoder/live-swe-agent/blob/8d7dd8634580d1e09320b4c27d70380bc9ae74a8/README.md#L38-L38), [README.md#L40-L40](https://github.com/OpenAutoCoder/live-swe-agent/blob/8d7dd8634580d1e09320b4c27d70380bc9ae74a8/README.md#L40-L40) (`clm_52a63a5bb611f6efa5da25183f53b9f82961beea8fb3f4ec728ce341f9d28174`)
- [observation/documented] Gemini 3 Pro with Live-SWE-agent reportedly scored 77.4% on SWE-bench Verified, outperforming other available models per the README news section. -- evidence: [README.md#L29-L32](https://github.com/OpenAutoCoder/live-swe-agent/blob/8d7dd8634580d1e09320b4c27d70380bc9ae74a8/README.md#L29-L32) (`clm_f364afc2bd420723a1c888fbc71bca542d1d96c458e873acf57a2d8fa7e0ddcb`)

## dependencies (1 claim(s))

- [observation/documented] Live-SWE-agent is built on top of the mini-swe-agent framework with very minimal modifications. -- evidence: [README.md#L59-L59](https://github.com/OpenAutoCoder/live-swe-agent/blob/8d7dd8634580d1e09320b4c27d70380bc9ae74a8/README.md#L59-L59) (`clm_0a0964473c8029930c56cab3cf8d8f7b28aecff9901d61a45cdf1e743fcc1f06`)

## limitations (1 claim(s))

- [inference/documented] The README's setup guide link for installing mini-swe-agent appears empty, so installation instructions may be incomplete in this snapshot. -- evidence: [README.md#L61-L61](https://github.com/OpenAutoCoder/live-swe-agent/blob/8d7dd8634580d1e09320b4c27d70380bc9ae74a8/README.md#L61-L61) (`clm_0bf04f289b51c69cc642d32f20cd6c4d86b624a11d5b3b6b703b3e603d5b59f1`)

## relevance (1 claim(s))

- [observation/documented] The project positions itself as an open scaffold for fair benchmarking of LLMs on software engineering tasks, contrasting with proprietary scaffolds. -- evidence: [README.md#L36-L36](https://github.com/OpenAutoCoder/live-swe-agent/blob/8d7dd8634580d1e09320b4c27d70380bc9ae74a8/README.md#L36-L36), [README.md#L38-L38](https://github.com/OpenAutoCoder/live-swe-agent/blob/8d7dd8634580d1e09320b4c27d70380bc9ae74a8/README.md#L38-L38) (`clm_708fdfd35af2be8823a0e18a2ab3e29a4369fc70a30341a35f437165b959857b`)

