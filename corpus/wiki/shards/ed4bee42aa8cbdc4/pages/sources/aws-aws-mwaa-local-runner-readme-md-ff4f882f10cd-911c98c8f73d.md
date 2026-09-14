---
access: public
aliases: []
claim_ids:
- clm_0b646d021d00d4712a6a8b0b2a8e77f8f91ea557f0eabdb8b5013ff9cdf7fb7b
- clm_10997f544553451b8020ca2a0bb1c0c6c0c8a8a98853f550f1446bf957ff5103
- clm_3de1753ba02f836eb6cfc614dd1a55d647c61824f665f31b19c48713461955d5
- clm_3e0c4488462571782f6f3de2b3c5ae2a8043083092bb36ea18723ef55c1c02cb
- clm_4ba7257c79bacb52c2fcef2073304f4ea44aee29f9218e70c19edaf84fffdada
- clm_622b2bb4dc29b616f6938903ba539d8f65b6d17bf906c47d51092b1a2fe7be0b
- clm_82f695c0e50ca5a8c60c61dc49ea74fda90242bc08ce3e50b7ae1e18e4fd14a9
- clm_9b4991308ef132f3a4ca30ce1da727fc6088e316f24b8c9432a397a4046e95d8
- clm_af216e731d51b4ee1cb64d23feb6063ef363704e45b96cf2f81d590e3c78bfad
- clm_e240bbab4f1daa94eda835bbe9639eb485cf8b6006507b7cc8dcb4923b6713a0
- clm_ea28c598da03b37109a02eaf8404de8288f7bd1ea684d76cf28062d62a4e1ffd
maturity: draft
page_id: pg_2652323d91ec552497ab911c98c8f73d
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_d0a6460b8baa5c73a3cdaa65dd011c03
title: aws/aws-mwaa-local-runner/README.md @ ff4f882f10cd
updated_at: '2026-09-14T03:37:08Z'
---

# aws/aws-mwaa-local-runner/README.md @ ff4f882f10cd

<!-- rcw:begin owner=source:src_d0a6460b8baa5c73a3cdaa65dd011c03 block=evidence -->
- The repository provides a CLI utility that replicates an Amazon MWAA environment locally. [@claim:clm_0b646d021d00d4712a6a8b0b2a8e77f8f91ea557f0eabdb8b5013ff9cdf7fb7b]
- Python dependencies are managed via requirements/requirements.txt, which can be tested or packaged into WHL files without running Airflow using dedicated CLI commands. [@claim:clm_10997f544553451b8020ca2a0bb1c0c6c0c8a8a98853f550f1446bf957ff5103]
- The local Airflow UI is served at http://localhost:8080, with default credentials admin/test created by bootstrap.sh. [@claim:clm_3de1753ba02f836eb6cfc614dd1a55d647c61824f665f31b19c48713461955d5]
- A Fernet key generated during image build encrypts connection passwords in the Airflow DB; rebuilding the image can produce a new key requiring a DB reset. [@claim:clm_3e0c4488462571782f6f3de2b3c5ae2a8043083092bb36ea18723ef55c1c02cb]
- The mwaa-local-env script supports subcommands including build-image, start, test-requirements, package-requirements, test-startup-script, and reset-db. [@claim:clm_4ba7257c79bacb52c2fcef2073304f4ea44aee29f9218e70c19edaf84fffdada]
- Repository development practice: the project uses the Amazon Open Source Code of Conduct and the MIT-0 license, with contributors asked to confirm licensing of their contributions. [@claim:clm_622b2bb4dc29b616f6938903ba539d8f65b6d17bf906c47d51092b1a2fe7be0b]
- The repo contains dags/, docker/ (config, scripts, compose files, Dockerfile), plugins/, requirements/, and a mwaa-local-env script, per its file listing. [@claim:clm_82f695c0e50ca5a8c60c61dc49ea74fda90242bc08ce3e50b7ae1e18e4fd14a9]
- For Airflow 2.9+, MWAA has open-sourced production images in amazon-mwaa-docker-images that can create a local environment identical to MWAA. [@claim:clm_9b4991308ef132f3a4ca30ce1da727fc6088e316f24b8c9432a397a4046e95d8]
- Dynamic configurations that depend on environment class are aligned with the Large MWAA environment class in this repository. [@claim:clm_af216e731d51b4ee1cb64d23feb6063ef363704e45b96cf2f81d590e3c78bfad]
- Airflow 3.x versions are to be supported via the separate amazon-mwaa-docker-images repository, not this local-runner repo. [@claim:clm_e240bbab4f1daa94eda835bbe9639eb485cf8b6006507b7cc8dcb4923b6713a0]
- The CLI builds a Docker container image locally similar to a MWAA production image, letting users develop and test DAGs, custom plugins, and dependencies before deploying to MWAA. [@claim:clm_ea28c598da03b37109a02eaf8404de8288f7bd1ea684d76cf28062d62a4e1ffd]
<!-- rcw:end owner=source:src_d0a6460b8baa5c73a3cdaa65dd011c03 block=evidence -->

## Researcher notes

