---
access: public
aliases: []
claim_ids:
- clm_0d3d5a29632da449036b51e4b9662a8970906343a852723df7c6abe7c8d21840
- clm_0f7723c0fa7ccd28e337c72430144694d6ff002719620688cdb1443ae9aebe95
- clm_20c11bca6bbd3e16275186c32987e307354f19fa18f3057a8217ac2fd23bad87
- clm_698d046a567eccc1e45872c4a01239db1c25d9b5a197cd44ca37c4fcfe92bf25
- clm_7e068b4187c7baa8af022500356e3e30cddff641c2963fddc7b07048be4e9ca2
- clm_9a5973c56edca7733195d3b628c6681c654efb0360d7b5cdcaf0ddc5018a6e0e
- clm_bfcc8bf39d287cbdad6a4256750c2c4f2fbb054a38b2eea60856ef47bec5d80b
- clm_c8f5dbc07406e87dfa52180e21cabc663535a050d840eae9b2b11c1e5bdce438
- clm_d615e54e7e377b05b352d1801444a8bbce844b4e898648e0810ad977e549a07d
- clm_d89cd2b72ac1933c93eef0076997bdc7a6d0d65c83f57a3a923b043c89e90257
maturity: draft
page_id: pg_a514768c10335fc9b469b7aad7a6fd13
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_396507dbc5bf5b3a8ad7787d5f395826
title: spark-engine-opensource-projects/fullstack-nextjs-app-generator/README.md @
  671d03e7dfe0
updated_at: '2026-09-14T02:42:11Z'
---

# spark-engine-opensource-projects/fullstack-nextjs-app-generator/README.md @ 671d03e7dfe0

<!-- rcw:begin owner=source:src_396507dbc5bf5b3a8ad7787d5f395826 block=evidence -->
- Deployment is delegated to a separate backend server repository (Automated-NextJS-deployer-to-vercel-and-supabase) that users must clone and run themselves, with ngrok tunneling its URL. [@claim:clm_0d3d5a29632da449036b51e4b9662a8970906343a852723df7c6abe7c8d21840]
- Setup workflow: clone the repo, run npm/yarn install, deploy to Vercel via the Vercel CLI (vercel --prod), then configure SPARK_API_KEY and NGROK_DEPLOYER_URL in Vercel. [@claim:clm_0f7723c0fa7ccd28e337c72430144694d6ff002719620688cdb1443ae9aebe95]
- Next.js Builder is a tool for interactively generating pages, APIs, and database schemas for Next.js web applications through a multi-step interface. [@claim:clm_20c11bca6bbd3e16275186c32987e307354f19fa18f3057a8217ac2fd23bad87]
- The project is licensed under the MIT License per the README. [@claim:clm_698d046a567eccc1e45872c4a01239db1c25d9b5a197cd44ca37c4fcfe92bf25]
- The backend deployment server exposes a /deploy endpoint used to deploy projects to Vercel and manage the Supabase database, including environment variables and SQL script execution. [@claim:clm_7e068b4187c7baa8af022500356e3e30cddff641c2963fddc7b07048be4e9ca2]
- After deployment, users monitor and update projects through the application's dashboard, with options to regenerate components and redeploy. [@claim:clm_9a5973c56edca7733195d3b628c6681c654efb0360d7b5cdcaf0ddc5018a6e0e]
- Prerequisites include Node.js v14.x or higher with npm/yarn, Vercel and Supabase accounts, an ngrok account for tunneling, and a Spark API Key from sparkengine.ai. [@claim:clm_bfcc8bf39d287cbdad6a4256750c2c4f2fbb054a38b2eea60856ef47bec5d80b]
- The frontend Next.js Builder must be deployed to Vercel to function properly, since it relies on Vercel's infrastructure for dynamic API generation and hosting. [@claim:clm_c8f5dbc07406e87dfa52180e21cabc663535a050d840eae9b2b11c1e5bdce438]
- The application depends on two environment variables: SPARK_API_KEY for code generation and NGROK_DEPLOYER_URL pointing at the ngrok-managed deployment server. [@claim:clm_d615e54e7e377b05b352d1801444a8bbce844b4e898648e0810ad977e549a07d]
- Project creation follows a multi-step form capturing name, page type (single or multiple), colors, logos, and purpose, followed by page/component definition, API generation, and schema review. [@claim:clm_d89cd2b72ac1933c93eef0076997bdc7a6d0d65c83f57a3a923b043c89e90257]
<!-- rcw:end owner=source:src_396507dbc5bf5b3a8ad7787d5f395826 block=evidence -->

## Researcher notes

