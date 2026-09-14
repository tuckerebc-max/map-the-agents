# invariantlabs-ai/explorer -- full detail

[Back to orientation](explorer.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/invariantlabs-ai/explorer/e7b13b3f5fe5a461a8e87e8f103d608011f507bc/6c3b908ee9d5f97f.json](../../../wiki/dossiers/invariantlabs-ai/explorer/e7b13b3f5fe5a461a8e87e8f103d608011f507bc/6c3b908ee9d5f97f.json)

## specifications (1 claim(s))

- [observation/documented] Invariant Explorer is described as a tool for visualizing and exploring agent traces. -- evidence: [README.md#L5-L5](https://github.com/invariantlabs-ai/explorer/blob/e7b13b3f5fe5a461a8e87e8f103d608011f507bc/README.md#L5-L5) (`clm_7cc7caa57c341238c661ad1aba4bf1d9a7f4b759ef1be1f0b9d9f5adb075d002`)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (5 claim(s))

- [observation/documented] Repository development practice: local development setup uses ./run.sh up to launch the stack, with Docker Compose installed beforehand. -- evidence: [README.md#L31-L33](https://github.com/invariantlabs-ai/explorer/blob/e7b13b3f5fe5a461a8e87e8f103d608011f507bc/README.md#L31-L33), [README.md#L29-L29](https://github.com/invariantlabs-ai/explorer/blob/e7b13b3f5fe5a461a8e87e8f103d608011f507bc/README.md#L29-L29), [README.md#L27-L27](https://github.com/invariantlabs-ai/explorer/blob/e7b13b3f5fe5a461a8e87e8f103d608011f507bc/README.md#L27-L27) (`clm_88bc536582bf03b1f23ca67f925d5cf56daf06192ee724aa9962eadbd86ab315`)
- [observation/documented] Repository development practice: tests run via ./run.sh tests-local after stopping the app with ./run.sh down, and can target a folder, a file, or a single test. -- evidence: [README.md#L79-L81](https://github.com/invariantlabs-ai/explorer/blob/e7b13b3f5fe5a461a8e87e8f103d608011f507bc/README.md#L79-L81), [README.md#L50-L50](https://github.com/invariantlabs-ai/explorer/blob/e7b13b3f5fe5a461a8e87e8f103d608011f507bc/README.md#L50-L50), [README.md#L67-L69](https://github.com/invariantlabs-ai/explorer/blob/e7b13b3f5fe5a461a8e87e8f103d608011f507bc/README.md#L67-L69), [README.md#L58-L61](https://github.com/invariantlabs-ai/explorer/blob/e7b13b3f5fe5a461a8e87e8f103d608011f507bc/README.md#L58-L61), [README.md#L52-L54](https://github.com/invariantlabs-ai/explorer/blob/e7b13b3f5fe5a461a8e87e8f103d608011f507bc/README.md#L52-L54), [README.md#L73-L75](https://github.com/invariantlabs-ai/explorer/blob/e7b13b3f5fe5a461a8e87e8f103d608011f507bc/README.md#L73-L75) (`clm_f35060f240e2715cfaf9235c818b252df0e1296849aa90a23f2e4b80a1b77b78`)
- [observation/documented] Repository development practice: new api or tester dependencies go into app-api/requirements.in or tests/requirements.in, followed by ./run.sh compile-requirements. -- evidence: [README.md#L44-L46](https://github.com/invariantlabs-ai/explorer/blob/e7b13b3f5fe5a461a8e87e8f103d608011f507bc/README.md#L44-L46), [README.md#L42-L42](https://github.com/invariantlabs-ai/explorer/blob/e7b13b3f5fe5a461a8e87e8f103d608011f507bc/README.md#L42-L42) (`clm_417a3891df3e9767208a05851a534d42a3e4de8f27ac683cd675d510bc0ec739`)
- [observation/documented] Repository development practice: service logs can be streamed with ./run.sh logs and stopped with Ctrl+C. -- evidence: [README.md#L91-L91](https://github.com/invariantlabs-ai/explorer/blob/e7b13b3f5fe5a461a8e87e8f103d608011f507bc/README.md#L91-L91), [README.md#L85-L85](https://github.com/invariantlabs-ai/explorer/blob/e7b13b3f5fe5a461a8e87e8f103d608011f507bc/README.md#L85-L85), [README.md#L87-L89](https://github.com/invariantlabs-ai/explorer/blob/e7b13b3f5fe5a461a8e87e8f103d608011f507bc/README.md#L87-L89) (`clm_6da308e3d8a6cda59296bedbc282b04876accca9863d461dff7adb95c4ac6258`)
- [observation/documented] Repository development practice: ./run.sh down fully tears down the testing environment and is needed before ./run.sh up again, but can be skipped when rerunning tests consecutively. -- evidence: [README.md#L63-L63](https://github.com/invariantlabs-ai/explorer/blob/e7b13b3f5fe5a461a8e87e8f103d608011f507bc/README.md#L63-L63) (`clm_1c85fdf6c36a5259f4e726cee7559993bb9aab3434481831f2c7a46a77b5f774`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] Users install the invariant-ai pip package and launch Explorer with the 'invariant explorer' command, then access the instance at http://localhost. -- evidence: [README.md#L20-L21](https://github.com/invariantlabs-ai/explorer/blob/e7b13b3f5fe5a461a8e87e8f103d608011f507bc/README.md#L20-L21), [README.md#L17-L17](https://github.com/invariantlabs-ai/explorer/blob/e7b13b3f5fe5a461a8e87e8f103d608011f507bc/README.md#L17-L17), [README.md#L23-L23](https://github.com/invariantlabs-ai/explorer/blob/e7b13b3f5fe5a461a8e87e8f103d608011f507bc/README.md#L23-L23) (`clm_777bc9b958fe9c5967914d3a8c21d6cdfb0cb8da905ef8a0537dc70663c552d3`)

## memory-state (1 claim(s))

- [observation/documented] Explorer stores data in a ./data directory of the current working directory; deleting that directory resets the data. -- evidence: [README.md#L38-L38](https://github.com/invariantlabs-ai/explorer/blob/e7b13b3f5fe5a461a8e87e8f103d608011f507bc/README.md#L38-L38), [README.md#L23-L23](https://github.com/invariantlabs-ai/explorer/blob/e7b13b3f5fe5a461a8e87e8f103d608011f507bc/README.md#L23-L23) (`clm_af97723df7ee43bf1882f3967880c711a9f9cbd71f7000536a444870455c3572`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Docker Compose is listed as a prerequisite for running Explorer. -- evidence: [README.md#L11-L11](https://github.com/invariantlabs-ai/explorer/blob/e7b13b3f5fe5a461a8e87e8f103d608011f507bc/README.md#L11-L11) (`clm_dd283a1e9c2df971f001cdd557a1fc26ff01e47bb1231f3b4acd67b8485b2859`)

## limitations (1 claim(s))

- [observation/documented] The hosted version of Invariant Explorer was shut down in January 2026, with readers pointed to Snyk's AI Security offering for Invariant Labs' continued AI security work. -- evidence: [README.md#L3-L3](https://github.com/invariantlabs-ai/explorer/blob/e7b13b3f5fe5a461a8e87e8f103d608011f507bc/README.md#L3-L3) (`clm_17dcf28f7f6c0c5f4f06fbc57568236cb80d7613bc52c5625549ed7560812ad6`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

