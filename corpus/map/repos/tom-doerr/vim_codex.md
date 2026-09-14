# tom-doerr/vim_codex

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit af12d5861cfb @ 2f9bcb3f39f6e821

## Summary (orientation draft, not independently verified)

The evidence consists solely of README content for vim_codex, a Vim plugin that calls OpenAI's Codex API to generate completions, including installation, configuration, and usage instructions.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 9 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

9 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Vim Codex is described as a simple Vim plugin that lets users use OpenAI Codex, requiring access to OpenAI's Codex API. -- evidence: [README.md#L29-L30](https://github.com/tom-doerr/vim_codex/blob/af12d5861cfbfb78d3ca6c6f680838a1449c52ee/README.md#L29-L30)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (1 claim(s)):
  - [inference/documented] The plugin appears to rely on a Python-based OpenAI client (pip-installed openai package and a config file under ~/.config) bridging Vim commands to the Codex API. -- evidence: [README.md#L56-L57](https://github.com/tom-doerr/vim_codex/blob/af12d5861cfbfb78d3ca6c6f680838a1449c52ee/README.md#L56-L57), [README.md#L51-L54](https://github.com/tom-doerr/vim_codex/blob/af12d5861cfbfb78d3ca6c6f680838a1449c52ee/README.md#L51-L54)
- workflows (2 claim(s)):
  - [observation/documented] Recommended installation is as a Vim bundle via Pathogen: install pathogen.vim, clone the repository into ~/.vim/bundle, and the README notes Vundle also works with bundle installs. -- evidence: [README.md#L42-L42](https://github.com/tom-doerr/vim_codex/blob/af12d5861cfbfb78d3ca6c6f680838a1449c52ee/README.md#L42-L42), [README.md#L39-L40](https://github.com/tom-doerr/vim_codex/blob/af12d5861cfbfb78d3ca6c6f680838a1449c52ee/README.md#L39-L40), [README.md#L46-L47](https://github.com/tom-doerr/vim_codex/blob/af12d5861cfbfb78d3ca6c6f680838a1449c52ee/README.md#L46-L47), [README.md#L44-L44](https://github.com/tom-doerr/vim_codex/blob/af12d5861cfbfb78d3ca6c6f680838a1449c52ee/README.md#L44-L44), [README.md#L36-L37](https://github.com/tom-doerr/vim_codex/blob/af12d5861cfbfb78d3ca6c6f680838a1449c52ee/README.md#L36-L37)
  - [observation/documented] Manual updates are done by cd-ing into the bundle directory and running git pull; Vundle users can update with :BundleUpdate. -- evidence: [README.md#L84-L84](https://github.com/tom-doerr/vim_codex/blob/af12d5861cfbfb78d3ca6c6f680838a1449c52ee/README.md#L84-L84), [README.md#L89-L93](https://github.com/tom-doerr/vim_codex/blob/af12d5861cfbfb78d3ca6c6f680838a1449c52ee/README.md#L89-L93), [README.md#L79-L80](https://github.com/tom-doerr/vim_codex/blob/af12d5861cfbfb78d3ca6c6f680838a1449c52ee/README.md#L79-L80), [README.md#L82-L82](https://github.com/tom-doerr/vim_codex/blob/af12d5861cfbfb78d3ca6c6f680838a1449c52ee/README.md#L82-L82)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The plugin exposes a CreateCompletion command, invoked by default via the <Leader>co mapping, which accepts a token-count argument such as 'CreateCompletion 1000'. -- evidence: [README.md#L62-L65](https://github.com/tom-doerr/vim_codex/blob/af12d5861cfbfb78d3ca6c6f680838a1449c52ee/README.md#L62-L65)
  - [observation/documented] A CreateCompletionLine command is provided for completing just the current line. -- evidence: [README.md#L62-L65](https://github.com/tom-doerr/vim_codex/blob/af12d5861cfbfb78d3ca6c6f680838a1449c52ee/README.md#L62-L65)
- memory-state (1 claim(s)):
  - [observation/documented] Running :CreateCompletion once creates ~/.config/openaiapirc, where the user must enter their OpenAI authentication information. -- evidence: [README.md#L56-L57](https://github.com/tom-doerr/vim_codex/blob/af12d5861cfbfb78d3ca6c6f680838a1449c52ee/README.md#L56-L57)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] After installing the plugin, the Python 'openai' package must be installed via pip3. -- evidence: [README.md#L51-L54](https://github.com/tom-doerr/vim_codex/blob/af12d5861cfbfb78d3ca6c6f680838a1449c52ee/README.md#L51-L54)
- limitations: unknown (no source-linked claim submitted for this facet)
- relevance: unknown (no source-linked claim submitted for this facet)

(1 additional claim(s) omitted for length; see [full detail](vim_codex.detail.md) for every claim.)

Metadata and full claim list: [full detail](vim_codex.detail.md)
Human notes ([notes](vim_codex.notes.md), never overwritten by build)

[Back to map index](../../index.md)
