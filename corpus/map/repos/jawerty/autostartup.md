# jawerty/autostartup

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 60ec3affede5 @ b2515a478e1e3939

## Summary (orientation draft, not independently verified)

AutoStartup is a Llama 2-based autonomous agent that turns a user 'intuition' into a business plan (with criticism/investor-approval loops) and then generates a React codebase via the author's 10x-React-Engineer project. Evidence is README-only; runtime behavior claims are documented, not code-inspected.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 9 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

9 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] The project is described as a Llama 2 autonomous agent that devises a startup idea, business plans, and React codebases from a simple user 'intuition'. -- evidence: [README.md#L5-L5](https://github.com/jawerty/AutoStartup/blob/60ec3affede5062345657a11b3bd020975b488d9/README.md#L5-L5)
- components (1 claim(s)):
  - [observation/documented] After plan approval, the agent generates a React codebase using the author's separate 10x-React-Engineer project. -- evidence: [README.md#L8-L8](https://github.com/jawerty/AutoStartup/blob/60ec3affede5062345657a11b3bd020975b488d9/README.md#L8-L8), [README.md#L10-L22](https://github.com/jawerty/AutoStartup/blob/60ec3affede5062345657a11b3bd020975b488d9/README.md#L10-L22)
- design-choices (1 claim(s)):
  - [observation/documented] The project advertises 100% Llama 2 inference with no OpenAI keys necessary, and applies lean startup concepts such as pivots and a tight MVP build loop. -- evidence: [README.md#L27-L34](https://github.com/jawerty/AutoStartup/blob/60ec3affede5062345657a11b3bd020975b488d9/README.md#L27-L34)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: to run from source, install dependencies with pip3 install -r requirements.txt (after Llama 2 access and huggingface-cli login) and run the main loop with python3 main.py; a Google Colab notebook is offered for quick testing. -- evidence: [README.md#L49-L52](https://github.com/jawerty/AutoStartup/blob/60ec3affede5062345657a11b3bd020975b488d9/README.md#L49-L52), [README.md#L44-L47](https://github.com/jawerty/AutoStartup/blob/60ec3affede5062345657a11b3bd020975b488d9/README.md#L44-L47), [README.md#L42-L42](https://github.com/jawerty/AutoStartup/blob/60ec3affede5062345657a11b3bd020975b488d9/README.md#L42-L42), [README.md#L55-L55](https://github.com/jawerty/AutoStartup/blob/60ec3affede5062345657a11b3bd020975b488d9/README.md#L55-L55)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] The user-facing input is a free-text 'intuition' (e.g. 'I think a website for dogsitters would be cool'), and an optional final step applies pivots based on user feedback. -- evidence: [README.md#L8-L8](https://github.com/jawerty/AutoStartup/blob/60ec3affede5062345657a11b3bd020975b488d9/README.md#L8-L8), [README.md#L10-L22](https://github.com/jawerty/AutoStartup/blob/60ec3affede5062345657a11b3bd020975b488d9/README.md#L10-L22)
- memory-state (1 claim(s)):
  - [observation/documented] The README claims memory via vector search over historically successful ideas paired with intuitions, and that previous criticisms are used for investor approvals. -- evidence: [README.md#L27-L34](https://github.com/jawerty/AutoStartup/blob/60ec3affede5062345657a11b3bd020975b488d9/README.md#L27-L34)
- orchestration (1 claim(s)):
  - [observation/documented] The agent runs an idea loop: it develops a business idea and plan, iterates via a criticism loop that regenerates the plan, and asks an 'investor' prompt for approval, restarting on disapproval. -- evidence: [README.md#L8-L8](https://github.com/jawerty/AutoStartup/blob/60ec3affede5062345657a11b3bd020975b488d9/README.md#L8-L8), [README.md#L10-L22](https://github.com/jawerty/AutoStartup/blob/60ec3affede5062345657a11b3bd020975b488d9/README.md#L10-L22)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] requirements.txt pins torch 2.0.1, transformers 4.31.0, sentence-transformers 2.2.2, scikit-learn 1.3.0, nltk, and huggingface-hub 0.16.4, among others. -- evidence: [requirements.txt#L1-L35](https://github.com/jawerty/AutoStartup/blob/60ec3affede5062345657a11b3bd020975b488d9/requirements.txt#L1-L35)
- limitations (1 claim(s)):
  - [observation/documented] The author notes the model needs a quality GPU to load the Llama 2 13b chat model, and a TODO says the React coding output needs bug fixing more often than not. -- evidence: [README.md#L58-L58](https://github.com/jawerty/AutoStartup/blob/60ec3affede5062345657a11b3bd020975b488d9/README.md#L58-L58), [README.md#L37-L37](https://github.com/jawerty/AutoStartup/blob/60ec3affede5062345657a11b3bd020975b488d9/README.md#L37-L37)
- relevance: unknown (no source-linked claim submitted for this facet)
More evidence: [full detail](autostartup.detail.md)

Metadata and full claim list: [full detail](autostartup.detail.md)
Human notes ([notes](autostartup.notes.md), never overwritten by build)

[Back to map index](../../index.md)
