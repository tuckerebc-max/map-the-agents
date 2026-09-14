---
access: public
aliases: []
claim_ids:
- clm_061443f6fbf1666e09cfda538d1a84a9cb2c5d20e278ae97e2d59bd1f3f927b0
- clm_236a6b104b0c2ef259fc43c18298775faab59781d56b9d245b18c7f806c0381b
- clm_4231913bce16f44d08ad5cc9381a99f89a95b89b1301861908eaf115025b112d
- clm_5054a540a2958f92b04001626ddc40a1fc57bb37f1289c6648a91effc7d96024
- clm_5102e68f914185e003c7566a3af62d517a4211714ce5c1045ccf2964494bde09
- clm_55ec0cb49ccb596a6e6c9cf7fa93193b7b66f15ae139deafa884b724b3e4f767
- clm_5c83a36032a87160a57ebe51c5a24faf497ed9c07bf55b8e85838d2b6f5e9287
- clm_663a54f10b3b7e9a4e34c4a89a38bb19dab78ea3cfe61b0ff66ee623d748a05d
- clm_74863043154dcb90579b31103e2bdf12b9bef30309758e415a85a9b7f0b8033d
- clm_7883b608de9ae388fabb8bca6aaaa8f0ef0ed30cf7baa5a35b8f5fe38d42f0d8
- clm_862fd44c5f96d4486ac3fe20a6d718bb7990aa8ea2fe48d1beeae3b861d3e86d
- clm_88b02c1fc04f4f981b1da4b087de3f0d2a836d541e55d4e3b48d2e9e04f13ca8
- clm_b5d95599ba410e83664262048d3b919616e7a76222e8d7f37e4472ec8ccb4072
maturity: draft
page_id: pg_3cdd5ca9c6035b44a0f62361cc3e2f2b
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_ddebcc99b4b756009a9ebf0b6e3a06bd
title: iwangjian/Coding-Tutor/README.md @ d1fa15b50e09
updated_at: '2026-09-14T04:00:38Z'
---

# iwangjian/Coding-Tutor/README.md @ d1fa15b50e09

<!-- rcw:begin owner=source:src_ddebcc99b4b756009a9ebf0b6e3a06bd block=evidence -->
- Coding tests for simulated students run in three steps via dedicated scripts: pre-test, student code generation, and coding-test metrics. [@claim:clm_061443f6fbf1666e09cfda538d1a84a9cb2c5d20e278ae97e2d59bd1f3f927b0]
- A trained verifier checkpoint (Verifier-7B) is released for download on Hugging Face. [@claim:clm_236a6b104b0c2ef259fc43c18298775faab59781d56b9d245b18c7f806c0381b]
- Although coding tutoring is the example scenario, the authors state the method extends to other task-tutoring settings where content must adapt to users' varying background knowledge. [@claim:clm_4231913bce16f44d08ad5cc9381a99f89a95b89b1301861908eaf115025b112d]
- The work introduces DICT, an evaluation protocol combining student simulation with coding tests to assess tutoring performance. [@claim:clm_5054a540a2958f92b04001626ddc40a1fc57bb37f1289c6648a91effc7d96024]
- Released simulated dialogues are stored as JSON records containing a namespace field and a conversation list with alternating tutor and student entries. [@claim:clm_5102e68f914185e003c7566a3af62d517a4211714ce5c1045ccf2964494bde09]
- Users must configure their own Azure API key, data path, and model path based on files under scripts/run/ before use. [@claim:clm_55ec0cb49ccb596a6e6c9cf7fa93193b7b66f15ae139deafa884b724b3e4f767]
- The README reports that simulated students at different levels show distinct task-completion abilities, and presents DICT as a scalable, cost-effective proxy for human evaluation. [@claim:clm_5c83a36032a87160a57ebe51c5a24faf497ed9c07bf55b8e85838d2b6f5e9287]
- The README reports that the Traver workflow with the trained verifier exhibits inference-time scaling for coding tutoring. [@claim:clm_663a54f10b3b7e9a4e34c4a89a38bb19dab78ea3cfe61b0ff66ee623d748a05d]
- The project is installed via a Python 3.10 conda environment followed by pip install -r requirements.txt. [@claim:clm_74863043154dcb90579b31103e2bdf12b9bef30309758e415a85a9b7f0b8033d]
- The project proposes Traver (Trace-and-Verify), an agent workflow that incorporates knowledge tracing and turn-by-turn verification for coding tutoring. [@claim:clm_7883b608de9ae388fabb8bca6aaaa8f0ef0ed30cf7baa5a35b8f5fe38d42f0d8]
- Setup requires downloading EvoCodeBench-2403 and building its execution environment per that project's instructions, which the README notes can take a few hours. [@claim:clm_862fd44c5f96d4486ac3fe20a6d718bb7990aa8ea2fe48d1beeae3b861d3e86d]
- The work was accepted to ACL Findings 2025 and released on arXiv (2502.13311) in February 2025. [@claim:clm_88b02c1fc04f4f981b1da4b087de3f0d2a836d541e55d4e3b48d2e9e04f13ca8]
- Evaluation scripts cover pre-test performance, tutoring outcome (TOR) computed from pre- and post-test directories, and tutoring outcome curves (TOC). [@claim:clm_b5d95599ba410e83664262048d3b919616e7a76222e8d7f37e4472ec8ccb4072]
<!-- rcw:end owner=source:src_ddebcc99b4b756009a9ebf0b6e3a06bd block=evidence -->

## Researcher notes

