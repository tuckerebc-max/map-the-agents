# spark-engine-opensource-projects/fullstack-nextjs-app-generator -- full detail

[Back to orientation](fullstack-nextjs-app-generator.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/spark-engine-opensource-projects/fullstack-nextjs-app-generator/671d03e7dfe071ed103ab7d6647aba7bb83f0204/633c52b39575b645.json](../../../wiki/dossiers/spark-engine-opensource-projects/fullstack-nextjs-app-generator/671d03e7dfe071ed103ab7d6647aba7bb83f0204/633c52b39575b645.json)

## specifications (1 claim(s))

- [observation/documented] Next.js Builder is a tool for interactively generating pages, APIs, and database schemas for Next.js web applications through a multi-step interface. -- evidence: [README.md#L10-L10](https://github.com/spark-engine-opensource-projects/fullstack-nextjs-app-generator/blob/671d03e7dfe071ed103ab7d6647aba7bb83f0204/README.md#L10-L10) (`clm_20c11bca6bbd3e16275186c32987e307354f19fa18f3057a8217ac2fd23bad87`)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (1 claim(s))

- [observation/documented] Project creation follows a multi-step form capturing name, page type (single or multiple), colors, logos, and purpose, followed by page/component definition, API generation, and schema review. -- evidence: [README.md#L87-L87](https://github.com/spark-engine-opensource-projects/fullstack-nextjs-app-generator/blob/671d03e7dfe071ed103ab7d6647aba7bb83f0204/README.md#L87-L87), [README.md#L89-L89](https://github.com/spark-engine-opensource-projects/fullstack-nextjs-app-generator/blob/671d03e7dfe071ed103ab7d6647aba7bb83f0204/README.md#L89-L89), [README.md#L85-L85](https://github.com/spark-engine-opensource-projects/fullstack-nextjs-app-generator/blob/671d03e7dfe071ed103ab7d6647aba7bb83f0204/README.md#L85-L85), [README.md#L91-L91](https://github.com/spark-engine-opensource-projects/fullstack-nextjs-app-generator/blob/671d03e7dfe071ed103ab7d6647aba7bb83f0204/README.md#L91-L91) (`clm_d89cd2b72ac1933c93eef0076997bdc7a6d0d65c83f57a3a923b043c89e90257`)

## workflows (2 claim(s))

- [observation/documented] Setup workflow: clone the repo, run npm/yarn install, deploy to Vercel via the Vercel CLI (vercel --prod), then configure SPARK_API_KEY and NGROK_DEPLOYER_URL in Vercel. -- evidence: [README.md#L65-L68](https://github.com/spark-engine-opensource-projects/fullstack-nextjs-app-generator/blob/671d03e7dfe071ed103ab7d6647aba7bb83f0204/README.md#L65-L68), [README.md#L55-L58](https://github.com/spark-engine-opensource-projects/fullstack-nextjs-app-generator/blob/671d03e7dfe071ed103ab7d6647aba7bb83f0204/README.md#L55-L58), [README.md#L38-L41](https://github.com/spark-engine-opensource-projects/fullstack-nextjs-app-generator/blob/671d03e7dfe071ed103ab7d6647aba7bb83f0204/README.md#L38-L41), [README.md#L74-L74](https://github.com/spark-engine-opensource-projects/fullstack-nextjs-app-generator/blob/671d03e7dfe071ed103ab7d6647aba7bb83f0204/README.md#L74-L74), [README.md#L76-L79](https://github.com/spark-engine-opensource-projects/fullstack-nextjs-app-generator/blob/671d03e7dfe071ed103ab7d6647aba7bb83f0204/README.md#L76-L79), [README.md#L45-L49](https://github.com/spark-engine-opensource-projects/fullstack-nextjs-app-generator/blob/671d03e7dfe071ed103ab7d6647aba7bb83f0204/README.md#L45-L49) (`clm_0f7723c0fa7ccd28e337c72430144694d6ff002719620688cdb1443ae9aebe95`)
- [observation/documented] After deployment, users monitor and update projects through the application's dashboard, with options to regenerate components and redeploy. -- evidence: [README.md#L106-L108](https://github.com/spark-engine-opensource-projects/fullstack-nextjs-app-generator/blob/671d03e7dfe071ed103ab7d6647aba7bb83f0204/README.md#L106-L108) (`clm_9a5973c56edca7733195d3b628c6681c654efb0360d7b5cdcaf0ddc5018a6e0e`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] The backend deployment server exposes a /deploy endpoint used to deploy projects to Vercel and manage the Supabase database, including environment variables and SQL script execution. -- evidence: [README.md#L106-L108](https://github.com/spark-engine-opensource-projects/fullstack-nextjs-app-generator/blob/671d03e7dfe071ed103ab7d6647aba7bb83f0204/README.md#L106-L108) (`clm_7e068b4187c7baa8af022500356e3e30cddff641c2963fddc7b07048be4e9ca2`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (1 claim(s))

- [observation/documented] Deployment is delegated to a separate backend server repository (Automated-NextJS-deployer-to-vercel-and-supabase) that users must clone and run themselves, with ngrok tunneling its URL. -- evidence: [README.md#L125-L126](https://github.com/spark-engine-opensource-projects/fullstack-nextjs-app-generator/blob/671d03e7dfe071ed103ab7d6647aba7bb83f0204/README.md#L125-L126), [README.md#L117-L120](https://github.com/spark-engine-opensource-projects/fullstack-nextjs-app-generator/blob/671d03e7dfe071ed103ab7d6647aba7bb83f0204/README.md#L117-L120), [README.md#L112-L113](https://github.com/spark-engine-opensource-projects/fullstack-nextjs-app-generator/blob/671d03e7dfe071ed103ab7d6647aba7bb83f0204/README.md#L112-L113) (`clm_0d3d5a29632da449036b51e4b9662a8970906343a852723df7c6abe7c8d21840`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (3 claim(s))

- [observation/documented] Prerequisites include Node.js v14.x or higher with npm/yarn, Vercel and Supabase accounts, an ngrok account for tunneling, and a Spark API Key from sparkengine.ai. -- evidence: [README.md#L27-L30](https://github.com/spark-engine-opensource-projects/fullstack-nextjs-app-generator/blob/671d03e7dfe071ed103ab7d6647aba7bb83f0204/README.md#L27-L30) (`clm_bfcc8bf39d287cbdad6a4256750c2c4f2fbb054a38b2eea60856ef47bec5d80b`)
- [observation/documented] The application depends on two environment variables: SPARK_API_KEY for code generation and NGROK_DEPLOYER_URL pointing at the ngrok-managed deployment server. -- evidence: [README.md#L99-L100](https://github.com/spark-engine-opensource-projects/fullstack-nextjs-app-generator/blob/671d03e7dfe071ed103ab7d6647aba7bb83f0204/README.md#L99-L100), [README.md#L76-L79](https://github.com/spark-engine-opensource-projects/fullstack-nextjs-app-generator/blob/671d03e7dfe071ed103ab7d6647aba7bb83f0204/README.md#L76-L79) (`clm_d615e54e7e377b05b352d1801444a8bbce844b4e898648e0810ad977e549a07d`)
- [observation/documented] The project is licensed under the MIT License per the README. -- evidence: [README.md#L133-L133](https://github.com/spark-engine-opensource-projects/fullstack-nextjs-app-generator/blob/671d03e7dfe071ed103ab7d6647aba7bb83f0204/README.md#L133-L133) (`clm_698d046a567eccc1e45872c4a01239db1c25d9b5a197cd44ca37c4fcfe92bf25`)

## limitations (1 claim(s))

- [observation/documented] The frontend Next.js Builder must be deployed to Vercel to function properly, since it relies on Vercel's infrastructure for dynamic API generation and hosting. -- evidence: [README.md#L53-L53](https://github.com/spark-engine-opensource-projects/fullstack-nextjs-app-generator/blob/671d03e7dfe071ed103ab7d6647aba7bb83f0204/README.md#L53-L53), [README.md#L128-L129](https://github.com/spark-engine-opensource-projects/fullstack-nextjs-app-generator/blob/671d03e7dfe071ed103ab7d6647aba7bb83f0204/README.md#L128-L129) (`clm_c8f5dbc07406e87dfa52180e21cabc663535a050d840eae9b2b11c1e5bdce438`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

