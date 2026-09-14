---
access: public
aliases: []
claim_ids:
- clm_20b52eef1310bf55368f6f1b7acd2292f9c40fd3f8c385435a3e7d0c2d602f10
- clm_3356cedc2c392015a1903969abd2211875595b366b0fea8f9c1efb85e133db11
- clm_48ece319dd7411e5aba9a40a7f598821b6a9f97f9ff17381afa5d83f655138cb
- clm_7cb9a634a81ce79c6efff62691b06f68e6fad3cdca737c8bd6ff5936a971d5e2
- clm_874efeb8ba599df9818e6ea9686a4cf07e09bde3f94b96a4a2668dfc30dc39f8
- clm_8b8c11e0f90c772d8a6f04fe9940b16036eaa472e117da586111bad4de7e2944
- clm_9e4a70ee6757a12d78cd40927186160e9035d26265a23461c111179c1a1ef49f
- clm_c39a83bed3162efa80da52bd60f3ff3ca51b55d2c1bde49d87410292ddaaf222
- clm_cd193e953ba7243a66661760226477581b0c1e6bbf78635b106dca39565da74c
- clm_e54c2dd25b98dd0aa553f1e55fc0aa6b47c1212c59cf2fbadc0ad26dc48d5e4d
- clm_e884a070fa37940e3ec288ba03154d10ae119a7122e781214fb0595def53ddb3
maturity: draft
page_id: pg_65f11e8c24375c59a69d699f1448c3e3
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_512178ef398450039e9334d0ee6da52e
title: khanzzirfan/TestAI-Agent/README.md @ d8b85ba11dc1
updated_at: '2026-09-14T02:09:23Z'
---

# khanzzirfan/TestAI-Agent/README.md @ d8b85ba11dc1

<!-- rcw:begin owner=source:src_512178ef398450039e9334d0ee6da52e block=evidence -->
- The repository appears to be a fork or copy of the actions/typescript-action template, since its README badges, headings, and instructions reference that upstream project. [@claim:clm_20b52eef1310bf55368f6f1b7acd2292f9c40fd3f8c385435a3e7d0c2d602f10]
- Repository development practice: the template's test suite is shown passing three checks in index.test.js, including invalid-number handling and a 500 ms wait test. [@claim:clm_3356cedc2c392015a1903969abd2211875595b366b0fea8f9c1efb85e133db11]
- The template's action code imports @actions/core from the GitHub Actions toolkit, and the README links to the toolkit documentation. [@claim:clm_48ece319dd7411e5aba9a40a7f598821b6a9f97f9ff17381afa5d83f655138cb]
- Repository development practice: the release helper script/script/release fetches the latest SemVer tag, prompts for and validates a new vX.X.X tag, syncs the major tag, creates releases/v# branches for prior majors, and pushes tags and branches. [@claim:clm_7cb9a634a81ce79c6efff62691b06f68e6fad3cdca737c8bd6ff5936a971d5e2]
- Repository development practice: Node.js 20.x or later is recommended for development, and a .node-version file pins the version for version managers and actions/setup-node. [@claim:clm_874efeb8ba599df9818e6ea9686a4cf07e09bde3f94b96a4a2668dfc30dc39f8]
- Repository development practice: the README describes local testing via the @github/local-action CLI (e.g. npx local-action . src/main.ts .env) or a VS Code debugger, with a .env file supplying inputs and event payloads. [@claim:clm_8b8c11e0f90c772d8a6f04fe9940b16036eaa472e117da586111bad4de7e2944]
- The example workflow invokes the action with a 'milliseconds' input of 1000 and reads a 'time' output from the step, illustrating the action's input/output interface. [@claim:clm_9e4a70ee6757a12d78cd40927186160e9035d26265a23461c111179c1a1ef49f]
- Repository development practice: contributors are told to update action.yml metadata (name, description, inputs, outputs) and to remove or update the CODEOWNERS file after copying the template. [@claim:clm_c39a83bed3162efa80da52bd60f3ff3ca51b55d2c1bde49d87410292ddaaf222]
- Repository development practice: the README walks through creating a branch (releases/v1), replacing src/ contents, adding tests under __tests__/, committing, pushing, and merging a pull request into main. [@claim:clm_cd193e953ba7243a66661760226477581b0c1e6bbf78635b106dca39565da74c]
- Repository development practice: the README instructs contributors to install dependencies with npm install, bundle with npm run bundle, and run tests with npm test. [@claim:clm_e54c2dd25b98dd0aa553f1e55fc0aa6b47c1212c59cf2fbadc0ad26dc48d5e4d]
- Repository development practice: contributors are told to run npm run all, which uses ncc to bundle the final JavaScript with dependencies and a license file; skipping it reportedly breaks the action in workflows. [@claim:clm_e884a070fa37940e3ec288ba03154d10ae119a7122e781214fb0595def53ddb3]
<!-- rcw:end owner=source:src_512178ef398450039e9334d0ee6da52e block=evidence -->

## Researcher notes

