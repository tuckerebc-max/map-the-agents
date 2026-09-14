---
access: public
aliases: []
claim_ids:
- clm_015d9311a3c7d0f494195148097418c2e38216355fd50d2d9df6823d17301dd4
- clm_0d46e7893c507521421fae6db105bdf2cb65ba526029dfe820d8e16d8d61f972
- clm_47e0a3693cdf4b5803d63499e9b3b036fdc0155079da584746be22a3bae2f439
- clm_5bb8339a525f232b1789181de9300440f42109a223e51726b4ac71a3ab0c1c0b
- clm_71db020bbd3913059e2e39478ff3b91b20476bf96f50e9f47f41f691d3345d68
- clm_8507b87c0fbe5a1bea32b5da0b1b64a9e902ea5fc29da90240584449cc439107
- clm_8788b4ff918329fb1db305305d5e066e956a8b27f70667dc5de361a421a333ca
- clm_c42c0120ad210182b0a99d55f402b56119ddd26b3132858890aa43b95a634c2b
- clm_cc53973488d3af3a7d5ef5139cd7fa5f1176027f60bcd24e79fc937dd8d0fdcd
- clm_d864208656c219dba9bf6098875b0b273af5369e56538de528e888b4d34ff782
- clm_eaaa84747daa921a19272b09fbbaf34be6318692c9dbbee2d887a8b860f04ebc
- clm_f27c42c8ce85e6ab374d2c3e35cb02b98de5e69d2a04290925a6703d95af998a
- clm_f44125e1bc73a93e9e2034bd71bdcb86376fe7b3ccc3b5ccf612c2ab1f5f3f82
maturity: draft
page_id: pg_90c1922d4d65508a8b1633687960e4b6
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_e60d147462be5bbdbd24840007b0c4ef
title: maruakshay/miii-cli/README.md @ 0a712d9f2d68
updated_at: '2026-09-14T02:16:41Z'
---

# maruakshay/miii-cli/README.md @ 0a712d9f2d68

<!-- rcw:begin owner=source:src_e60d147462be5bbdbd24840007b0c4ef block=evidence -->
- The tool requires Node 18 or newer and Ollama, and is distributed as the npm package miii-agent. [@claim:clm_015d9311a3c7d0f494195148097418c2e38216355fd50d2d9df6823d17301dd4]
- The agent repairs malformed tool calls from small models and sizes its prompt to the model's context window, and a MIII.md file in the repo is read every turn to teach project conventions. [@claim:clm_0d46e7893c507521421fae6db105bdf2cb65ba526029dfe820d8e16d8d61f972]
- File tools reject ../ traversal and absolute paths outside the workspace, while run_bash is not path-confined and is bounded only by the permission prompt. [@claim:clm_47e0a3693cdf4b5803d63499e9b3b036fdc0155079da584746be22a3bae2f439]
- Saved approval rules live in .miii/permissions.json per project (with an optional global ~/.miii/permissions.json), and sessions can be saved and resumed via /new and /sessions. [@claim:clm_5bb8339a525f232b1789181de9300440f42109a223e51726b4ac71a3ab0c1c0b]
- The product includes `miii doctor`, which grades the user's installed local models on real engineering tasks to check whether they can drive an agent. [@claim:clm_71db020bbd3913059e2e39478ff3b91b20476bf96f50e9f47f41f691d3345d68]
- Four permission modes cycle via shift+tab: normal, plan (read-only), auto-accept edits, and bypass; 'always' approvals save exact commands plus globs that never span command boundaries or match destructive programs. [@claim:clm_8507b87c0fbe5a1bea32b5da0b1b64a9e902ea5fc29da90240584449cc439107]
- Tool output over ~10K bytes is spilled to ~/.miii/output/<id>.txt with a head/tail preview inline; the model pages through the file with ranged reads and spill files are garbage-collected after 24 hours. [@claim:clm_8788b4ff918329fb1db305305d5e066e956a8b27f70667dc5de361a421a333ca]
- Repository development practice: contributors clone the repo, run npm install && npm run dev, and use npm run build, npm run typecheck, npm test, and npm run eval (a regression gate powering miii doctor); npm run build && npm link runs the working tree as the global miii. [@claim:clm_c42c0120ad210182b0a99d55f402b56119ddd26b3132858890aa43b95a634c2b]
- The CLI exposes slash commands (/plan, /permissions, /models, /sessions, /compact, /copy, /clear, /exit), a command palette on '/', and keyboard shortcuts such as Shift+Tab for permission modes and Ctrl+V for image paste. [@claim:clm_cc53973488d3af3a7d5ef5139cd7fa5f1176027f60bcd24e79fc937dd8d0fdcd]
- miii is a local terminal AI coding agent that runs against Ollama with no API keys or cloud, positioned as an offline alternative to cloud coding assistants. [@claim:clm_d864208656c219dba9bf6098875b0b273af5369e56538de528e888b4d34ff782]
- Besides Ollama, miii can talk to any OpenAI-compatible local server such as llama.cpp, LM Studio, or vLLM, selected via config providers or --provider at launch. [@claim:clm_eaaa84747daa921a19272b09fbbaf34be6318692c9dbbee2d887a8b860f04ebc]
- Built-in agent tools include read_file, write_file, edit_file, glob, grep, run_bash, and write_todos for tracking multi-step work. [@claim:clm_f27c42c8ce85e6ab374d2c3e35cb02b98de5e69d2a04290925a6703d95af998a]
- Custom slash commands are Markdown files in .miii/commands/ (project scope) or ~/.miii/commands/ (personal), supporting $ARGUMENTS and $1-$9 substitution, with project commands shadowing personal ones but never built-ins. [@claim:clm_f44125e1bc73a93e9e2034bd71bdcb86376fe7b3ccc3b5ccf612c2ab1f5f3f82]
<!-- rcw:end owner=source:src_e60d147462be5bbdbd24840007b0c4ef block=evidence -->

## Researcher notes

