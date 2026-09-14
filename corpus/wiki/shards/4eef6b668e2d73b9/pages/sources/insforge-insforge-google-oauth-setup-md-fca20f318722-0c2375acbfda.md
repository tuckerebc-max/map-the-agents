---
access: public
aliases: []
claim_ids:
- clm_7894865097da0a5b2acecb2cfd153df29f711987cc62fa75444943d9c5c69223
- clm_bd373b5f39446aff159818ab6d913fdb04971853d72ae498e94408d0a947609f
maturity: draft
page_id: pg_ccda7252678158a290d90c2375acbfda
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_f60fece758c35da9a6f66af656569fe0
title: InsForge/InsForge/GOOGLE_OAUTH_SETUP.md @ fca20f318722
updated_at: '2026-09-14T03:58:31Z'
---

# InsForge/InsForge/GOOGLE_OAUTH_SETUP.md @ fca20f318722

<!-- rcw:begin owner=source:src_f60fece758c35da9a6f66af656569fe0 block=evidence -->
- On first Google login the system creates records in auth, identifies, and profiles tables; returning users are looked up by provider and provider_id in the identifies table and have last_login_at updated. [@claim:clm_7894865097da0a5b2acecb2cfd153df29f711987cc62fa75444943d9c5c69223]
- Google OAuth is documented with endpoints GET /api/auth/v1/google-auth (returns an auth_url) and GET /api/auth/oauth/google/callback, which redirects with token (JWT), user_id, email, and name as URL parameters. [@claim:clm_bd373b5f39446aff159818ab6d913fdb04971853d72ae498e94408d0a947609f]
<!-- rcw:end owner=source:src_f60fece758c35da9a6f66af656569fe0 block=evidence -->

## Researcher notes

