# decron/whitebox-code-gpt

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit a5dbf33d4dd9 @ c6051f3e9be846f1

## Summary (orientation draft, not independently verified)

The repository documents a collection of open-source, ChatGPT-hosted programming assistants built from expert-maintained knowledge files, with a custodial governance model, contribution guidelines, and enterprise-safety caveats. Evidence is documentation-only (README, CONTRIBUTING, SECURITY, CODE_OF_CONDUCT); no runtime code is present in the snapshot.

## Source coverage

Source coverage (complete): 4 of 4 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications (2 claim(s)):
  - [observation/documented] The project produces programming assistants hosted on ChatGPT, built by open-sourcing instructions and knowledge files that experts and users collaboratively create and maintain. -- evidence: [README.md#L52-L55](https://github.com/Decron/Whitebox-Code-GPT/blob/a5dbf33d4dd90e901375e0eb1afe6b61e6c48873/README.md#L52-L55), [README.md#L6-L6](https://github.com/Decron/Whitebox-Code-GPT/blob/a5dbf33d4dd90e901375e0eb1afe6b61e6c48873/README.md#L6-L6)
  - [observation/documented] Assistants are listed for Python, Flutter, Git, Regex, Firebase, Node.js, C++, and a DeltaV controls-engineering assistant, with C# and bioinformatics marked as coming soon. -- evidence: [README.md#L29-L33](https://github.com/Decron/Whitebox-Code-GPT/blob/a5dbf33d4dd90e901375e0eb1afe6b61e6c48873/README.md#L29-L33), [README.md#L18-L27](https://github.com/Decron/Whitebox-Code-GPT/blob/a5dbf33d4dd90e901375e0eb1afe6b61e6c48873/README.md#L18-L27)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (1 claim(s)):
  - [observation/documented] Knowledge files are dedicated per topic and organized hierarchically or relationally to augment the LLM's knowledge base; per-flavor regex rule sets are cited as improving valid pattern generation. -- evidence: [README.md#L62-L66](https://github.com/Decron/Whitebox-Code-GPT/blob/a5dbf33d4dd90e901375e0eb1afe6b61e6c48873/README.md#L62-L66)
- workflows (4 claim(s)):
  - [observation/documented] Repository development practice: contributors fork the repository, clone it locally, and add assistant files via pull requests while updating the README index; solo maintainers may instead add their link to a partnered index. -- evidence: [CONTRIBUTING.md#L9-L9](https://github.com/Decron/Whitebox-Code-GPT/blob/a5dbf33d4dd90e901375e0eb1afe6b61e6c48873/CONTRIBUTING.md#L9-L9), [README.md#L8-L9](https://github.com/Decron/Whitebox-Code-GPT/blob/a5dbf33d4dd90e901375e0eb1afe6b61e6c48873/README.md#L8-L9), [CONTRIBUTING.md#L7-L7](https://github.com/Decron/Whitebox-Code-GPT/blob/a5dbf33d4dd90e901375e0eb1afe6b61e6c48873/CONTRIBUTING.md#L7-L7), [CONTRIBUTING.md#L11-L12](https://github.com/Decron/Whitebox-Code-GPT/blob/a5dbf33d4dd90e901375e0eb1afe6b61e6c48873/CONTRIBUTING.md#L11-L12)
  - [observation/documented] Repository development practice: each assistant has a custodian (sole decider of its content) assigned by an admin, who verifies the README directory is updated before merging; forfeiting custodians help find a replacement. -- evidence: [README.md#L83-L83](https://github.com/Decron/Whitebox-Code-GPT/blob/a5dbf33d4dd90e901375e0eb1afe6b61e6c48873/README.md#L83-L83), [README.md#L79-L79](https://github.com/Decron/Whitebox-Code-GPT/blob/a5dbf33d4dd90e901375e0eb1afe6b61e6c48873/README.md#L79-L79), [README.md#L85-L85](https://github.com/Decron/Whitebox-Code-GPT/blob/a5dbf33d4dd90e901375e0eb1afe6b61e6c48873/README.md#L85-L85), [README.md#L87-L87](https://github.com/Decron/Whitebox-Code-GPT/blob/a5dbf33d4dd90e901375e0eb1afe6b61e6c48873/README.md#L87-L87)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] Assistants are accessed via ChatGPT-hosted custom GPT links and require no installation; users without ChatGPT premium may copy the knowledge files to a different LLM. -- evidence: [README.md#L52-L55](https://github.com/Decron/Whitebox-Code-GPT/blob/a5dbf33d4dd90e901375e0eb1afe6b61e6c48873/README.md#L52-L55), [README.md#L18-L27](https://github.com/Decron/Whitebox-Code-GPT/blob/a5dbf33d4dd90e901375e0eb1afe6b61e6c48873/README.md#L18-L27)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation (1 claim(s)):
  - [observation/documented] The README claims assistants are quality-tested and rigorously checked, and states that developing automated testing to guarantee functionality is a secondary goal, implying it does not yet exist. -- evidence: [README.md#L68-L71](https://github.com/Decron/Whitebox-Code-GPT/blob/a5dbf33d4dd90e901375e0eb1afe6b61e6c48873/README.md#L68-L71), [README.md#L18-L27](https://github.com/Decron/Whitebox-Code-GPT/blob/a5dbf33d4dd90e901375e0eb1afe6b61e6c48873/README.md#L18-L27)
- dependencies: unknown (no source-linked claim submitted for this facet)
- limitations (2 claim(s)):
  - [observation/documented] The project warns that conversation-training settings cannot be truly verified and that knowledge-file/document training cannot be disabled in GPT builder, so users should avoid including sensitive material. -- evidence: [README.md#L101-L107](https://github.com/Decron/Whitebox-Code-GPT/blob/a5dbf33d4dd90e901375e0eb1afe6b61e6c48873/README.md#L101-L107)
More evidence: [full detail](whitebox-code-gpt.detail.md)

Metadata and full claim list: [full detail](whitebox-code-gpt.detail.md)
Human notes ([notes](whitebox-code-gpt.notes.md), never overwritten by build)

[Back to map index](../../index.md)
