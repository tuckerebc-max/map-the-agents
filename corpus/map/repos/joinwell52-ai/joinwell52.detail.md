# joinwell52-ai/joinwell52 -- full detail

[Back to orientation](joinwell52.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/joinwell52-ai/joinwell52/6961492e9a46eb9b7e3cdd6e8148c336ce76b026/2a0fd4110d4ba967.json](../../../wiki/dossiers/joinwell52-ai/joinwell52/6961492e9a46eb9b7e3cdd6e8148c336ce76b026/2a0fd4110d4ba967.json)

## specifications (1 claim(s))

- [observation/documented] TMPA Core Specification S1.0 is presented as the normative layer defining objects, authority, lifecycle, Reader behavior, and conformance requirements, with criteria labeled C01–C14. -- evidence: [README.md#L52-L56](https://github.com/joinwell52-AI/joinwell52/blob/6961492e9a46eb9b7e3cdd6e8148c336ce76b026/README.md#L52-L56), [README.md#L231-L243](https://github.com/joinwell52-AI/joinwell52/blob/6961492e9a46eb9b7e3cdd6e8148c336ce76b026/README.md#L231-L243) (`clm_866b4b4f7b75c5f7860b091025bb21d4c2ba22ed03a016e840f5a8120308022c`)

## components (2 claim(s))

- [observation/documented] The repository ships TMPA Core S1.0 machine schemas, fixtures, profiles, an author-produced Reference Reader, and a C01–C14 conformance runner. -- evidence: [README.md#L258-L258](https://github.com/joinwell52-AI/joinwell52/blob/6961492e9a46eb9b7e3cdd6e8148c336ce76b026/README.md#L258-L258) (`clm_90d66051f1fe75e943e84d033e3295bacfcc16bab6bea98ff76ea82d9ba1a46f`)
- [observation/documented] CodeFlowMu is described as a local PM/DEV/QA/OPS AI development team with a PC control center and a mobile PWA, distributed as a proprietary free Windows x64 preview from a separate distribution repository. -- evidence: [README.md#L75-L75](https://github.com/joinwell52-AI/joinwell52/blob/6961492e9a46eb9b7e3cdd6e8148c336ce76b026/README.md#L75-L75), [README.md#L310-L310](https://github.com/joinwell52-AI/joinwell52/blob/6961492e9a46eb9b7e3cdd6e8148c336ce76b026/README.md#L310-L310) (`clm_4de9770974b0254a0a0ed211da8c8565f72ba084a182930944c608dd51275970`)

## design-choices (1 claim(s))

- [observation/documented] TMPA Core is described as storage-neutral: files, database rows, object-store items, or events may carry the same governance semantics, with durable state kept outside model sessions and a Reader reconstructing governance state. -- evidence: [README.md#L254-L254](https://github.com/joinwell52-AI/joinwell52/blob/6961492e9a46eb9b7e3cdd6e8148c336ce76b026/README.md#L254-L254), [README.md#L249-L252](https://github.com/joinwell52-AI/joinwell52/blob/6961492e9a46eb9b7e3cdd6e8148c336ce76b026/README.md#L249-L252) (`clm_84b61e56e5a2e09f7ee4db6a1f64e84f3cf2580df2558ecf091a600505aa1dff`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] The Reference Reader is run via npm commands: `npm run demo` for a demo delivery and `npm run tmpa:s1.0:conformance` for the conformance runner, after `npm ci`. -- evidence: [README.md#L262-L268](https://github.com/joinwell52-AI/joinwell52/blob/6961492e9a46eb9b7e3cdd6e8148c336ce76b026/README.md#L262-L268) (`clm_1e355114c7f4dddfb5ff7e443dc39b4cab3f8258f3d728e1b89f32bc479575ac`)

## memory-state (1 claim(s))

- [observation/documented] TMPA moves durable work facts out of volatile model memory so lifecycle, authority, conflict, and audit state can be reconstructed from inspectable evidence across asynchronous execution. -- evidence: [README.md#L172-L172](https://github.com/joinwell52-AI/joinwell52/blob/6961492e9a46eb9b7e3cdd6e8148c336ce76b026/README.md#L172-L172) (`clm_70f0d211a2a28b9d6d691a6f3a75fc2899ff1d96afde2b3540e15befcf9f94d7`)

## orchestration (1 claim(s))

- [inference/documented] The V0.3.1 draft architecture proposes a five-layer design (FCoP fact layer, TMPA Reader, Runtime, definition/deployment, instance) coordinated by asynchronous fact loops rather than a synchronous all-agents-online pipeline; it is explicitly a draft, not a stable specification. -- evidence: [docs/zh/digital-employee/architecture.md#L86-L92](https://github.com/joinwell52-AI/joinwell52/blob/6961492e9a46eb9b7e3cdd6e8148c336ce76b026/docs/zh/digital-employee/architecture.md#L86-L92), [docs/zh/digital-employee/architecture.md#L17-L17](https://github.com/joinwell52-AI/joinwell52/blob/6961492e9a46eb9b7e3cdd6e8148c336ce76b026/docs/zh/digital-employee/architecture.md#L17-L17), [docs/zh/digital-employee/architecture.md#L94-L94](https://github.com/joinwell52-AI/joinwell52/blob/6961492e9a46eb9b7e3cdd6e8148c336ce76b026/docs/zh/digital-employee/architecture.md#L94-L94) (`clm_4a97376aef4eefa62aeee9c2e99b5df6e46f3f6422599db7dfd9713e10998356`)

## tools-permissions (1 claim(s))

- [inference/documented] The draft proposes each execution role be bounded by a default-deny Capability Envelope/Sandbox Boundary limiting tools, paths, network, and credentials, plus a negative list of contextual business rules; as draft target language, this is not confirmed shipped behavior. -- evidence: [docs/zh/digital-employee/architecture.md#L149-L150](https://github.com/joinwell52-AI/joinwell52/blob/6961492e9a46eb9b7e3cdd6e8148c336ce76b026/docs/zh/digital-employee/architecture.md#L149-L150) (`clm_3e31c5f0a4bbea1e40c124148c226af688e9c08542ed25fee4498cb922070261`)

## evaluation (1 claim(s))

- [observation/documented] The recorded conformance result is 14 PASS / 0 PARTIAL / 0 NOT RUN / 0 FAIL for the S1.0 criteria, alongside reported suite results such as 71/71 mandatory assertions and a 1,522-pass CodeFlowMu runtime suite. -- evidence: [README.md#L274-L276](https://github.com/joinwell52-AI/joinwell52/blob/6961492e9a46eb9b7e3cdd6e8148c336ce76b026/README.md#L274-L276), [README.md#L284-L292](https://github.com/joinwell52-AI/joinwell52/blob/6961492e9a46eb9b7e3cdd6e8148c336ce76b026/README.md#L284-L292) (`clm_791a18214cb198bbbfee43aa9b7ee246f17004f7f906430224b8694d8328d89f`)

## dependencies (1 claim(s))

- [observation/documented] Running the Reference Reader requires Node.js 20 or later, per the README requirements line. -- evidence: [README.md#L260-L260](https://github.com/joinwell52-AI/joinwell52/blob/6961492e9a46eb9b7e3cdd6e8148c336ce76b026/README.md#L260-L260) (`clm_c42f452919fb08f1d0601108f6d3de836f2ac79504eb178e7ccfcadefb25ddce`)

## limitations (1 claim(s))

- [observation/documented] The README states the conformance evidence is author-run for one exact implementation revision and input bundle, and is not independent certification, universal conformance, or proof hallucinations are eliminated. -- evidence: [README.md#L296-L296](https://github.com/joinwell52-AI/joinwell52/blob/6961492e9a46eb9b7e3cdd6e8148c336ce76b026/README.md#L296-L296) (`clm_80fdef812d27637c00c822c5d8d81bdcff9109dbf0abffafa2ea65236e7c0205`)

## relevance (1 claim(s))

- [observation/documented] The repository targets builders of agents that must survive restarts, handoffs, disputes, review, and organizational accountability. -- evidence: [README.md#L176-L176](https://github.com/joinwell52-AI/joinwell52/blob/6961492e9a46eb9b7e3cdd6e8148c336ce76b026/README.md#L176-L176) (`clm_834005403dfe71f50664c41301ad6459f6d65624cda38da3dfe8091b58e833a4`)

