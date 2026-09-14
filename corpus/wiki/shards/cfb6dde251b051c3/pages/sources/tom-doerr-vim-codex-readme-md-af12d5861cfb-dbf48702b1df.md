---
access: public
aliases: []
claim_ids:
- clm_2ca2caae6903491ca44337e87c7138aa31a614a2b859679db82aecc6cba143f9
- clm_52e484e2f9080265fc7559ad952838817191443318ee1e2d3ba6b171a3806a86
- clm_5bec571ebcb55112f2bbf8562f927a83a5f22420737a0c243f6566dd342e3677
- clm_631468f4d2a63d03fc58b7fe1060f7f75d14e8b1796ca75e7bd8188a7510ffa3
- clm_9d9b193654ebef05d238a86e1e6cb298a3a81139b4d2ab703d764d0be214e26f
- clm_e17213bab87db1f5317748c7a3944be5c4d435147cb29c05e662a3cdbb74c0b7
- clm_e4070f02ccc1192f90d12af64f7b6fee59590471618bd15da06922d58fe41a3b
- clm_f40f12b0a92ab1465857add29f7330bdcde7dede96b429380c3c543d13f0a730
- clm_f567f46decfdad7c3b444dc452d69b4bef4adf1dbb70892e64ea2595912350e9
maturity: draft
page_id: pg_98357e6643525e5b83fadbf48702b1df
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_d1f550e7c6fc5f62bd96f381f966105b
title: tom-doerr/vim_codex/README.md @ af12d5861cfb
updated_at: '2026-09-14T04:27:35Z'
---

# tom-doerr/vim_codex/README.md @ af12d5861cfb

<!-- rcw:begin owner=source:src_d1f550e7c6fc5f62bd96f381f966105b block=evidence -->
- After installing the plugin, the Python 'openai' package must be installed via pip3. [@claim:clm_2ca2caae6903491ca44337e87c7138aa31a614a2b859679db82aecc6cba143f9]
- The README suggests optional .vimrc mappings that bind Ctrl+x in normal and insert mode to trigger CreateCompletion. [@claim:clm_52e484e2f9080265fc7559ad952838817191443318ee1e2d3ba6b171a3806a86]
- Manual updates are done by cd-ing into the bundle directory and running git pull; Vundle users can update with :BundleUpdate. [@claim:clm_5bec571ebcb55112f2bbf8562f927a83a5f22420737a0c243f6566dd342e3677]
- Running :CreateCompletion once creates ~/.config/openaiapirc, where the user must enter their OpenAI authentication information. [@claim:clm_631468f4d2a63d03fc58b7fe1060f7f75d14e8b1796ca75e7bd8188a7510ffa3]
- The plugin appears to rely on a Python-based OpenAI client (pip-installed openai package and a config file under ~/.config) bridging Vim commands to the Codex API. [@claim:clm_9d9b193654ebef05d238a86e1e6cb298a3a81139b4d2ab703d764d0be214e26f]
- The plugin exposes a CreateCompletion command, invoked by default via the <Leader>co mapping, which accepts a token-count argument such as 'CreateCompletion 1000'. [@claim:clm_e17213bab87db1f5317748c7a3944be5c4d435147cb29c05e662a3cdbb74c0b7]
- A CreateCompletionLine command is provided for completing just the current line. [@claim:clm_e4070f02ccc1192f90d12af64f7b6fee59590471618bd15da06922d58fe41a3b]
- Vim Codex is described as a simple Vim plugin that lets users use OpenAI Codex, requiring access to OpenAI's Codex API. [@claim:clm_f40f12b0a92ab1465857add29f7330bdcde7dede96b429380c3c543d13f0a730]
- Recommended installation is as a Vim bundle via Pathogen: install pathogen.vim, clone the repository into ~/.vim/bundle, and the README notes Vundle also works with bundle installs. [@claim:clm_f567f46decfdad7c3b444dc452d69b4bef4adf1dbb70892e64ea2595912350e9]
<!-- rcw:end owner=source:src_d1f550e7c6fc5f62bd96f381f966105b block=evidence -->

## Researcher notes

