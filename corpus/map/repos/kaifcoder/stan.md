# kaifcoder/stan

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 405a8ef28139 @ 4afeb26cde73dea6

## Summary (orientation draft, not independently verified)

Selected evidence records: Stan is described as a text-analysis tool that summarizes long texts and answers questions about provided text, using a locally deployed language model. The README claims Stan works offline without an internet connection and does not store user data, framing privacy as a design goal.

## Source coverage

Source coverage (complete): 3 of 3 candidate file(s) selected; repository tree complete. Claims by basis: 9 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

9 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Stan is described as a text-analysis tool that summarizes long texts and answers questions about provided text, using a locally deployed language model. -- evidence: [README.md#L3-L3](https://github.com/kaifcoder/Stan/blob/405a8ef28139587adb813e05dbaaa5f040f8da60/README.md#L3-L3), [README.md#L20-L20](https://github.com/kaifcoder/Stan/blob/405a8ef28139587adb813e05dbaaa5f040f8da60/README.md#L20-L20), [README.md#L13-L16](https://github.com/kaifcoder/Stan/blob/405a8ef28139587adb813e05dbaaa5f040f8da60/README.md#L13-L16)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (2 claim(s)):
  - [observation/documented] The README claims Stan works offline without an internet connection and does not store user data, framing privacy as a design goal. -- evidence: [README.md#L13-L16](https://github.com/kaifcoder/Stan/blob/405a8ef28139587adb813e05dbaaa5f040f8da60/README.md#L13-L16), [README.md#L32-L32](https://github.com/kaifcoder/Stan/blob/405a8ef28139587adb813e05dbaaa5f040f8da60/README.md#L32-L32)
  - [observation/documented] Models are loaded with device_map='auto' and torch_dtype=torch.float32, allowing potential GPU utilization while computing in float32. -- evidence: [CODE_REVIEW.md#L95-L99](https://github.com/kaifcoder/Stan/blob/405a8ef28139587adb813e05dbaaa5f040f8da60/CODE_REVIEW.md#L95-L99), [CODE_REVIEW.md#L10-L12](https://github.com/kaifcoder/Stan/blob/405a8ef28139587adb813e05dbaaa5f040f8da60/CODE_REVIEW.md#L10-L12)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The main page UI offers a text area, checkboxes for 'Summarize Text' and 'Fix Grammatical Errors', and an Analyze button that triggers prompts like 'Summarize : {text}'. -- evidence: [CODE_REVIEW.md#L130-L132](https://github.com/kaifcoder/Stan/blob/405a8ef28139587adb813e05dbaaa5f040f8da60/CODE_REVIEW.md#L130-L132), [CODE_REVIEW.md#L135-L141](https://github.com/kaifcoder/Stan/blob/405a8ef28139587adb813e05dbaaa5f040f8da60/CODE_REVIEW.md#L135-L141), [CODE_REVIEW.md#L143-L148](https://github.com/kaifcoder/Stan/blob/405a8ef28139587adb813e05dbaaa5f040f8da60/CODE_REVIEW.md#L143-L148), [CODE_REVIEW.md#L126-L127](https://github.com/kaifcoder/Stan/blob/405a8ef28139587adb813e05dbaaa5f040f8da60/CODE_REVIEW.md#L126-L127)
  - [observation/documented] The PDF page embeds uploaded PDFs in an iframe via base64 encoding and shows the summary in a second column after a Summarize button click. -- evidence: [CODE_REVIEW.md#L308-L319](https://github.com/kaifcoder/Stan/blob/405a8ef28139587adb813e05dbaaa5f040f8da60/CODE_REVIEW.md#L308-L319), [CODE_REVIEW.md#L294-L295](https://github.com/kaifcoder/Stan/blob/405a8ef28139587adb813e05dbaaa5f040f8da60/CODE_REVIEW.md#L294-L295), [CODE_REVIEW.md#L289-L292](https://github.com/kaifcoder/Stan/blob/405a8ef28139587adb813e05dbaaa5f040f8da60/CODE_REVIEW.md#L289-L292), [CODE_REVIEW.md#L321-L324](https://github.com/kaifcoder/Stan/blob/405a8ef28139587adb813e05dbaaa5f040f8da60/CODE_REVIEW.md#L321-L324)
- memory-state (1 claim(s)):
  - [observation/documented] The chat page maintains conversation state in st.session_state.messages and caches the model with st.cache_resource to avoid reloading on each run. -- evidence: [CODE_REVIEW.md#L171-L185](https://github.com/kaifcoder/Stan/blob/405a8ef28139587adb813e05dbaaa5f040f8da60/CODE_REVIEW.md#L171-L185)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] requirements.txt pins streamlit 1.27.0, transformers 4.33.2, torch 2.0.1, langchain 0.0.301, ctransformers 0.2.27, and pypdf 3.16.2, among many pinned packages. -- evidence: [requirements.txt#L1-L95](https://github.com/kaifcoder/Stan/blob/405a8ef28139587adb813e05dbaaa5f040f8da60/requirements.txt#L1-L95)
- limitations (2 claim(s)):
  - [observation/documented] The code review notes the chatbot's model file 'codellama-7b.Q2_K.gguf' must be present in the expected directory or model loading will fail. -- evidence: [CODE_REVIEW.md#L189-L190](https://github.com/kaifcoder/Stan/blob/405a8ef28139587adb813e05dbaaa5f040f8da60/CODE_REVIEW.md#L189-L190)
  - [inference/documented] The review flags that the chat response generator rebuilds the full dialogue context each turn, which appears inefficient for long conversations. -- evidence: [CODE_REVIEW.md#L198-L199](https://github.com/kaifcoder/Stan/blob/405a8ef28139587adb813e05dbaaa5f040f8da60/CODE_REVIEW.md#L198-L199)
- relevance: unknown (no source-linked claim submitted for this facet)

Every claim for this repository is shown above and in [full detail](stan.detail.md).

Metadata and full claim list: [full detail](stan.detail.md)
Human notes ([notes](stan.notes.md), never overwritten by build)

[Back to map index](../../index.md)
