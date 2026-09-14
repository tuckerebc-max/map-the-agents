# tom-doerr/vim_codex -- full detail

[Back to orientation](vim_codex.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/tom-doerr/vim_codex/af12d5861cfbfb78d3ca6c6f680838a1449c52ee/2f9bcb3f39f6e821.json](../../../wiki/dossiers/tom-doerr/vim_codex/af12d5861cfbfb78d3ca6c6f680838a1449c52ee/2f9bcb3f39f6e821.json)

## specifications (1 claim(s))

- [observation/documented] Vim Codex is described as a simple Vim plugin that lets users use OpenAI Codex, requiring access to OpenAI's Codex API. -- evidence: [README.md#L29-L30](https://github.com/tom-doerr/vim_codex/blob/af12d5861cfbfb78d3ca6c6f680838a1449c52ee/README.md#L29-L30) (`clm_f40f12b0a92ab1465857add29f7330bdcde7dede96b429380c3c543d13f0a730`)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (1 claim(s))

- [inference/documented] The plugin appears to rely on a Python-based OpenAI client (pip-installed openai package and a config file under ~/.config) bridging Vim commands to the Codex API. -- evidence: [README.md#L56-L57](https://github.com/tom-doerr/vim_codex/blob/af12d5861cfbfb78d3ca6c6f680838a1449c52ee/README.md#L56-L57), [README.md#L51-L54](https://github.com/tom-doerr/vim_codex/blob/af12d5861cfbfb78d3ca6c6f680838a1449c52ee/README.md#L51-L54) (`clm_9d9b193654ebef05d238a86e1e6cb298a3a81139b4d2ab703d764d0be214e26f`)

## workflows (2 claim(s))

- [observation/documented] Recommended installation is as a Vim bundle via Pathogen: install pathogen.vim, clone the repository into ~/.vim/bundle, and the README notes Vundle also works with bundle installs. -- evidence: [README.md#L42-L42](https://github.com/tom-doerr/vim_codex/blob/af12d5861cfbfb78d3ca6c6f680838a1449c52ee/README.md#L42-L42), [README.md#L39-L40](https://github.com/tom-doerr/vim_codex/blob/af12d5861cfbfb78d3ca6c6f680838a1449c52ee/README.md#L39-L40), [README.md#L46-L47](https://github.com/tom-doerr/vim_codex/blob/af12d5861cfbfb78d3ca6c6f680838a1449c52ee/README.md#L46-L47), [README.md#L44-L44](https://github.com/tom-doerr/vim_codex/blob/af12d5861cfbfb78d3ca6c6f680838a1449c52ee/README.md#L44-L44), [README.md#L36-L37](https://github.com/tom-doerr/vim_codex/blob/af12d5861cfbfb78d3ca6c6f680838a1449c52ee/README.md#L36-L37) (`clm_f567f46decfdad7c3b444dc452d69b4bef4adf1dbb70892e64ea2595912350e9`)
- [observation/documented] Manual updates are done by cd-ing into the bundle directory and running git pull; Vundle users can update with :BundleUpdate. -- evidence: [README.md#L84-L84](https://github.com/tom-doerr/vim_codex/blob/af12d5861cfbfb78d3ca6c6f680838a1449c52ee/README.md#L84-L84), [README.md#L89-L93](https://github.com/tom-doerr/vim_codex/blob/af12d5861cfbfb78d3ca6c6f680838a1449c52ee/README.md#L89-L93), [README.md#L79-L80](https://github.com/tom-doerr/vim_codex/blob/af12d5861cfbfb78d3ca6c6f680838a1449c52ee/README.md#L79-L80), [README.md#L82-L82](https://github.com/tom-doerr/vim_codex/blob/af12d5861cfbfb78d3ca6c6f680838a1449c52ee/README.md#L82-L82) (`clm_5bec571ebcb55112f2bbf8562f927a83a5f22420737a0c243f6566dd342e3677`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The plugin exposes a CreateCompletion command, invoked by default via the <Leader>co mapping, which accepts a token-count argument such as 'CreateCompletion 1000'. -- evidence: [README.md#L62-L65](https://github.com/tom-doerr/vim_codex/blob/af12d5861cfbfb78d3ca6c6f680838a1449c52ee/README.md#L62-L65) (`clm_e17213bab87db1f5317748c7a3944be5c4d435147cb29c05e662a3cdbb74c0b7`)
- [observation/documented] A CreateCompletionLine command is provided for completing just the current line. -- evidence: [README.md#L62-L65](https://github.com/tom-doerr/vim_codex/blob/af12d5861cfbfb78d3ca6c6f680838a1449c52ee/README.md#L62-L65) (`clm_e4070f02ccc1192f90d12af64f7b6fee59590471618bd15da06922d58fe41a3b`)
- [observation/documented] The README suggests optional .vimrc mappings that bind Ctrl+x in normal and insert mode to trigger CreateCompletion. -- evidence: [README.md#L67-L72](https://github.com/tom-doerr/vim_codex/blob/af12d5861cfbfb78d3ca6c6f680838a1449c52ee/README.md#L67-L72) (`clm_52e484e2f9080265fc7559ad952838817191443318ee1e2d3ba6b171a3806a86`)

## memory-state (1 claim(s))

- [observation/documented] Running :CreateCompletion once creates ~/.config/openaiapirc, where the user must enter their OpenAI authentication information. -- evidence: [README.md#L56-L57](https://github.com/tom-doerr/vim_codex/blob/af12d5861cfbfb78d3ca6c6f680838a1449c52ee/README.md#L56-L57) (`clm_631468f4d2a63d03fc58b7fe1060f7f75d14e8b1796ca75e7bd8188a7510ffa3`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] After installing the plugin, the Python 'openai' package must be installed via pip3. -- evidence: [README.md#L51-L54](https://github.com/tom-doerr/vim_codex/blob/af12d5861cfbfb78d3ca6c6f680838a1449c52ee/README.md#L51-L54) (`clm_2ca2caae6903491ca44337e87c7138aa31a614a2b859679db82aecc6cba143f9`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

