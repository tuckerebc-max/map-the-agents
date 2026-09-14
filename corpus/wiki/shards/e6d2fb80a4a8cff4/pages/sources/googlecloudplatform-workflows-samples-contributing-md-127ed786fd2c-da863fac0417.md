---
access: public
aliases: []
claim_ids:
- clm_0b24100abf9e594f4944619a4ae7487248d4ea57d6938014f66acb33f3225460
- clm_2cf134633820cf02cb1bc62db9f9ddba87d346a484cfbcfd39e3e23fe1b66142
- clm_5c645898148ccc13c6fac54dfa1a02e8509eeed24c1578a3c17a90db2731e551
- clm_682941e44292e0ab403cf09f369f238c3c26ad6640c089d819b086184bf11a44
- clm_f1b99d2648eddefb069cddbe9d7b6ae2ba821e5e7fa2a676ba850fdc51533bab
- clm_f6db60180fb99f069df002f3ae1e262da88eed098e71e1560723d714a8dc365e
maturity: draft
page_id: pg_3167ec4c48a1576695fbda863fac0417
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_997a23ef9ad65a3fabae4889d2c0cf6b
title: GoogleCloudPlatform/workflows-samples/CONTRIBUTING.md @ 127ed786fd2c
updated_at: '2026-09-14T03:54:33Z'
---

# GoogleCloudPlatform/workflows-samples/CONTRIBUTING.md @ 127ed786fd2c

<!-- rcw:begin owner=source:src_997a23ef9ad65a3fabae4889d2c0cf6b block=evidence -->
- Repository development practice: contributors can generate JSON files from YAML by running the ./tojson.sh script. [@claim:clm_0b24100abf9e594f4944619a4ae7487248d4ea57d6938014f66acb33f3225460]
- Repository development practice: schema authoring guidance prefers the lowest needed draft (Draft v4) for interoperability, always sets additionalProperties to false, and requires length/pattern constraints and consistent style. [@claim:clm_2cf134633820cf02cb1bc62db9f9ddba87d346a484cfbcfd39e3e23fe1b66142]
- Repository development practice: the schema covers workflow features including subworkflows, steps, assign/call/raise/try/except/retry, switch conditions, for loops, parallel branches with exception policy and concurrency limit, and HTTP call args with auth, timeout, and polling policy. [@claim:clm_5c645898148ccc13c6fac54dfa1a02e8509eeed24c1578a3c17a90db2731e551]
- Repository development practice: all submissions, including those from project members, require review via GitHub pull requests. [@claim:clm_682941e44292e0ab403cf09f369f238c3c26ad6640c089d819b086184bf11a44]
- Repository development practice: the repo's JSON Schema aims to give syntax support via IDE autocompletion and CI syntax validation, but will not catch all errors since the Workflows API does additional parsing. [@claim:clm_f1b99d2648eddefb069cddbe9d7b6ae2ba821e5e7fa2a676ba850fdc51533bab]
- Repository development practice: contributions require a Contributor License Agreement, generally signed once, with copyright retained by the contributor. [@claim:clm_f6db60180fb99f069df002f3ae1e262da88eed098e71e1560723d714a8dc365e]
<!-- rcw:end owner=source:src_997a23ef9ad65a3fabae4889d2c0cf6b block=evidence -->

## Researcher notes

