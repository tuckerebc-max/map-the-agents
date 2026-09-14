---
access: public
aliases: []
claim_ids:
- clm_355ee9a63c09aa2bbd0936da238d7b4608c957eec306ff6d38f8030f93dc24e2
- clm_6454df724824f1fded497d67b5e2822690b27adaf8f7592cb68b7f3ce8799808
- clm_9975cef44d162449e3667bab2e857960a5f3f0067c2d73dc8d45273f3fc0363b
- clm_e2526cb2c7b5e71ed264664d8acbdbccc8729ecba1ebcbf46d808e521688ef37
- clm_ea839858e2cbf89826bfdd3e4335a033df6588116c527c9bbd1f81174867257b
- clm_f05c8e989e1830473c4af717d5b9f1145dfb9443af69d2277e17794f64e376b8
maturity: draft
page_id: pg_87f0c24259c4564ea93618d2eb387d6e
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_4b9b887ea1145735a14d7adc08f2ad9f
title: abhikt48/java-ai-sbus-test/README.md @ aa74eebe6809
updated_at: '2026-09-14T03:31:01Z'
---

# abhikt48/java-ai-sbus-test/README.md @ aa74eebe6809

<!-- rcw:begin owner=source:src_4b9b887ea1145735a14d7adc08f2ad9f block=evidence -->
- The project relies on the Application Insights Java agent version 3.5.2 jar, downloaded separately and attached via -javaagent. [@claim:clm_355ee9a63c09aa2bbd0936da238d7b4608c957eec306ff6d38f8030f93dc24e2]
- The 'codeless agent' naming and single -javaagent VM argument suggest the project uses agent-based (codeless) instrumentation rather than SDK code changes. [@claim:clm_6454df724824f1fded497d67b5e2822690b27adaf8f7592cb68b7f3ce8799808]
- The Service Bus configuration in TestCodelessAgentWithSbus.java is updated first, then the class is run with the single VM argument -javaagent pointing at the agent jar, which should start successfully. [@claim:clm_9975cef44d162449e3667bab2e857960a5f3f0067c2d73dc8d45273f3fc0363b]
- Setup involves updating the connection string in applicationinsights.json and downloading/copying applicationinsights-agent-3.5.2.jar into the agent directory. [@claim:clm_e2526cb2c7b5e71ed264664d8acbdbccc8729ecba1ebcbf46d808e521688ef37]
- The project is described as a test project for applicationinsights-agent. [@claim:clm_ea839858e2cbf89826bfdd3e4335a033df6588116c527c9bbd1f81174867257b]
- Per the README's final step, results are viewed by opening App Insight to inspect a dependency tree. [@claim:clm_f05c8e989e1830473c4af717d5b9f1145dfb9443af69d2277e17794f64e376b8]
<!-- rcw:end owner=source:src_4b9b887ea1145735a14d7adc08f2ad9f block=evidence -->

## Researcher notes

