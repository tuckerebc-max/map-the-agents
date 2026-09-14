---
access: public
aliases: []
claim_ids:
- clm_1e318b7f7c0a936b6e02535323d8fdf44258d2fa9f79256818bcbd9e5a3c48ec
- clm_6180aefa02712763c546bc0b570b9d9c7348b61f9ab2aef449ac7845977f0566
- clm_a22a0ce6b7cbcd7776363bf09bed70ec71149088007629f5f80fb8049c7af4b6
maturity: draft
page_id: pg_015249cc84f6531e80cadb0b8a1a11e9
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_dbd8de46135153a181a7426f96fb3645
title: DeadWaveWave/demo2apk/docs/API.md @ 1405c4405c96
updated_at: '2026-09-14T03:45:12Z'
---

# DeadWaveWave/demo2apk/docs/API.md @ 1405c4405c96

<!-- rcw:begin owner=source:src_dbd8de46135153a181a7426f96fb3645 block=evidence -->
- Build endpoints accept optional appName, appId, and publishPwa fields; appName defaults differ per endpoint (MyVibeApp for HTML, MyReactApp for ZIP). [@claim:clm_1e318b7f7c0a936b6e02535323d8fdf44258d2fa9f79256818bcbd9e5a3c48ec]
- Task status queries return pending, active, completed, or failed states, with progress including a message and percentage. [@claim:clm_6180aefa02712763c546bc0b570b9d9c7348b61f9ab2aef449ac7845977f0566]
- The REST API exposes GET /health, POST /api/build/html, POST /api/build/zip, GET /api/build/:taskId/status, GET /api/build/:taskId/download, and DELETE /api/build/:taskId, using multipart/form-data uploads and JSON responses. [@claim:clm_a22a0ce6b7cbcd7776363bf09bed70ec71149088007629f5f80fb8049c7af4b6]
<!-- rcw:end owner=source:src_dbd8de46135153a181a7426f96fb3645 block=evidence -->

## Researcher notes

