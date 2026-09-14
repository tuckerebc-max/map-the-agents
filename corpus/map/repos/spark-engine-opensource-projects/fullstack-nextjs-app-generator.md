# spark-engine-opensource-projects/fullstack-nextjs-app-generator

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 671d03e7dfe0 @ 633c52b39575b645

## Summary (orientation draft, not independently verified)

The evidence is README-only documentation for a Next.js app generator that creates pages, APIs, and database schemas via a multi-step interface and deploys to Vercel with Supabase via a separate backend deployer. No code, tests, or agent evaluation are shown.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 10 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

10 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Next.js Builder is a tool for interactively generating pages, APIs, and database schemas for Next.js web applications through a multi-step interface. -- evidence: [README.md#L10-L10](https://github.com/spark-engine-opensource-projects/fullstack-nextjs-app-generator/blob/671d03e7dfe071ed103ab7d6647aba7bb83f0204/README.md#L10-L10)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (1 claim(s)):
  - [observation/documented] Project creation follows a multi-step form capturing name, page type (single or multiple), colors, logos, and purpose, followed by page/component definition, API generation, and schema review. -- evidence: [README.md#L87-L87](https://github.com/spark-engine-opensource-projects/fullstack-nextjs-app-generator/blob/671d03e7dfe071ed103ab7d6647aba7bb83f0204/README.md#L87-L87), [README.md#L89-L89](https://github.com/spark-engine-opensource-projects/fullstack-nextjs-app-generator/blob/671d03e7dfe071ed103ab7d6647aba7bb83f0204/README.md#L89-L89), [README.md#L85-L85](https://github.com/spark-engine-opensource-projects/fullstack-nextjs-app-generator/blob/671d03e7dfe071ed103ab7d6647aba7bb83f0204/README.md#L85-L85), [README.md#L91-L91](https://github.com/spark-engine-opensource-projects/fullstack-nextjs-app-generator/blob/671d03e7dfe071ed103ab7d6647aba7bb83f0204/README.md#L91-L91)
- workflows (2 claim(s)):
  - [observation/documented] Setup workflow: clone the repo, run npm/yarn install, deploy to Vercel via the Vercel CLI (vercel --prod), then configure SPARK_API_KEY and NGROK_DEPLOYER_URL in Vercel. -- evidence: [README.md#L65-L68](https://github.com/spark-engine-opensource-projects/fullstack-nextjs-app-generator/blob/671d03e7dfe071ed103ab7d6647aba7bb83f0204/README.md#L65-L68), [README.md#L55-L58](https://github.com/spark-engine-opensource-projects/fullstack-nextjs-app-generator/blob/671d03e7dfe071ed103ab7d6647aba7bb83f0204/README.md#L55-L58), [README.md#L38-L41](https://github.com/spark-engine-opensource-projects/fullstack-nextjs-app-generator/blob/671d03e7dfe071ed103ab7d6647aba7bb83f0204/README.md#L38-L41), [README.md#L74-L74](https://github.com/spark-engine-opensource-projects/fullstack-nextjs-app-generator/blob/671d03e7dfe071ed103ab7d6647aba7bb83f0204/README.md#L74-L74), [README.md#L76-L79](https://github.com/spark-engine-opensource-projects/fullstack-nextjs-app-generator/blob/671d03e7dfe071ed103ab7d6647aba7bb83f0204/README.md#L76-L79), [README.md#L45-L49](https://github.com/spark-engine-opensource-projects/fullstack-nextjs-app-generator/blob/671d03e7dfe071ed103ab7d6647aba7bb83f0204/README.md#L45-L49)
  - [observation/documented] After deployment, users monitor and update projects through the application's dashboard, with options to regenerate components and redeploy. -- evidence: [README.md#L106-L108](https://github.com/spark-engine-opensource-projects/fullstack-nextjs-app-generator/blob/671d03e7dfe071ed103ab7d6647aba7bb83f0204/README.md#L106-L108)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] The backend deployment server exposes a /deploy endpoint used to deploy projects to Vercel and manage the Supabase database, including environment variables and SQL script execution. -- evidence: [README.md#L106-L108](https://github.com/spark-engine-opensource-projects/fullstack-nextjs-app-generator/blob/671d03e7dfe071ed103ab7d6647aba7bb83f0204/README.md#L106-L108)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (1 claim(s)):
  - [observation/documented] Deployment is delegated to a separate backend server repository (Automated-NextJS-deployer-to-vercel-and-supabase) that users must clone and run themselves, with ngrok tunneling its URL. -- evidence: [README.md#L125-L126](https://github.com/spark-engine-opensource-projects/fullstack-nextjs-app-generator/blob/671d03e7dfe071ed103ab7d6647aba7bb83f0204/README.md#L125-L126), [README.md#L117-L120](https://github.com/spark-engine-opensource-projects/fullstack-nextjs-app-generator/blob/671d03e7dfe071ed103ab7d6647aba7bb83f0204/README.md#L117-L120), [README.md#L112-L113](https://github.com/spark-engine-opensource-projects/fullstack-nextjs-app-generator/blob/671d03e7dfe071ed103ab7d6647aba7bb83f0204/README.md#L112-L113)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (3 claim(s)):
  - [observation/documented] Prerequisites include Node.js v14.x or higher with npm/yarn, Vercel and Supabase accounts, an ngrok account for tunneling, and a Spark API Key from sparkengine.ai. -- evidence: [README.md#L27-L30](https://github.com/spark-engine-opensource-projects/fullstack-nextjs-app-generator/blob/671d03e7dfe071ed103ab7d6647aba7bb83f0204/README.md#L27-L30)
  - [observation/documented] The application depends on two environment variables: SPARK_API_KEY for code generation and NGROK_DEPLOYER_URL pointing at the ngrok-managed deployment server. -- evidence: [README.md#L99-L100](https://github.com/spark-engine-opensource-projects/fullstack-nextjs-app-generator/blob/671d03e7dfe071ed103ab7d6647aba7bb83f0204/README.md#L99-L100), [README.md#L76-L79](https://github.com/spark-engine-opensource-projects/fullstack-nextjs-app-generator/blob/671d03e7dfe071ed103ab7d6647aba7bb83f0204/README.md#L76-L79)
- limitations (1 claim(s)):
  - [observation/documented] The frontend Next.js Builder must be deployed to Vercel to function properly, since it relies on Vercel's infrastructure for dynamic API generation and hosting. -- evidence: [README.md#L53-L53](https://github.com/spark-engine-opensource-projects/fullstack-nextjs-app-generator/blob/671d03e7dfe071ed103ab7d6647aba7bb83f0204/README.md#L53-L53), [README.md#L128-L129](https://github.com/spark-engine-opensource-projects/fullstack-nextjs-app-generator/blob/671d03e7dfe071ed103ab7d6647aba7bb83f0204/README.md#L128-L129)
- relevance: unknown (no source-linked claim submitted for this facet)

(1 additional claim(s) omitted for length; see [full detail](fullstack-nextjs-app-generator.detail.md) for every claim.)

Metadata and full claim list: [full detail](fullstack-nextjs-app-generator.detail.md)
Human notes ([notes](fullstack-nextjs-app-generator.notes.md), never overwritten by build)

[Back to map index](../../index.md)
