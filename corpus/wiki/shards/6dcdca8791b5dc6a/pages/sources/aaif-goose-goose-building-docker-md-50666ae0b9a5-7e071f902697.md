---
access: public
aliases: []
claim_ids:
- clm_151f0ba04ec45bbfd9aaa4d4fcf3aee489ea7326f329d757729311ef827a3d6a
- clm_15490f3078da6e183c015211675e10a52eaafd70862b8b3efc917a6c4e2d3298
- clm_2c3e989bc28ce205ed545b9052e385e3a34da21cc423d6fa21e05995bbb9ffe8
- clm_a89211a7d43fa48df74a4fe55671a463eca887a2b9bbe563c8949f09fbf518e3
maturity: draft
page_id: pg_360a76c3e4ad5cef922e7e071f902697
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_7ddb8b523268544eb325b86d839f1db7
title: aaif-goose/goose/BUILDING_DOCKER.md @ 50666ae0b9a5
updated_at: '2026-09-14T04:51:09Z'
---

# aaif-goose/goose/BUILDING_DOCKER.md @ 50666ae0b9a5

<!-- rcw:begin owner=source:src_7ddb8b523268544eb325b86d839f1db7 block=evidence -->
- The Docker image is a multi-stage Debian Bookworm Slim build of about 340MB containing a 32MB goose binary at /usr/local/bin/goose, optimized with LTO, stripping, and size optimization. [@claim:clm_151f0ba04ec45bbfd9aaa4d4fcf3aee489ea7326f329d757729311ef827a3d6a]
- The Docker image runs as a non-root 'goose' user (UID 1000) by default and includes git, curl, ca-certificates, and basic shell utilities. [@claim:clm_15490f3078da6e183c015211675e10a52eaafd70862b8b3efc917a6c4e2d3298]
- Repository development practice: BUILDING_DOCKER.md asks contributors to Docker changes to test builds on amd64 and arm64, keep image size reasonable, update docs, and test with various LLM providers. [@claim:clm_2c3e989bc28ce205ed545b9052e385e3a34da21cc423d6fa21e05995bbb9ffe8]
- Docker usage is configured via environment variables such as GOOSE_PROVIDER, GOOSE_MODEL, and provider API keys, with CLI commands like 'goose run -t'. [@claim:clm_a89211a7d43fa48df74a4fe55671a463eca887a2b9bbe563c8949f09fbf518e3]
<!-- rcw:end owner=source:src_7ddb8b523268544eb325b86d839f1db7 block=evidence -->

## Researcher notes

