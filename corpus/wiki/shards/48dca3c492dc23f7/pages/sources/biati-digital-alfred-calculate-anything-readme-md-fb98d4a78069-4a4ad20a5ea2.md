---
access: public
aliases: []
claim_ids:
- clm_060c083c22fc4690f8b113ce863e8c8dd8fa6a81288b2e5808dd1ffdfa500ab4
- clm_1e459434c8680b9e564234c27facf88c0eb80be4e684d7cbfa63bd90f8e23fe1
- clm_448b506a80edc83e9d87017247d715dc013584dcfd39eaf567ff3c521709d43f
- clm_6157d523d8f65a6e5ed70f6de7b840861dc38b8b3708221f7e6a1520b7c97292
- clm_749b5aca3bb71a1620cb0b30a4bacf25c60fc2a75d34f8eb46aeb88e5bb9a60c
- clm_a8119107a012c53f9622d00532fbb88a47e726e5ae671ee1b5a0cb6a5cd2a20a
- clm_aa30e888dc10430fe8424b281e7199741e16096e627f450bfc01efa59913dfb4
- clm_b836570795c854d9e2f36449aa17e08c74c91b1fe13fd543dabcc9f3d2b39e43
- clm_c28d84350b2e2644832d6b5c1d83c9e1583f1455b1170ef090ba349f401dbb14
- clm_e75357727f2fc9e5a81ad07ce56cd31aebb4de40eaf5d166c55b44b0a10df3de
- clm_eb00516d9c20c621b336acdbe7666111a5fdc59019b868bbef82e710885096c6
- clm_f7ee36dee66a62acb1edf1a6dc4b850d19ae94fc583582262fb223d760a70ad3
maturity: draft
page_id: pg_75a8ba1caa065401aed64a4ad20a5ea2
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_fe8c31fb77de54809a4fc3f0f0da5180
title: biati-digital/alfred-calculate-anything/README.md @ fb98d4a78069
updated_at: '2026-09-14T03:38:43Z'
---

# biati-digital/alfred-calculate-anything/README.md @ fb98d4a78069

<!-- rcw:begin owner=source:src_fe8c31fb77de54809a4fc3f0f0da5180 block=evidence -->
- Data storage conversions follow the IEC standard: 1MB in KB yields 1000 KB while 1MiB in KiB yields 1024 KB, and a 1MB=1024KB preference is configurable. [@claim:clm_060c083c22fc4690f8b113ce863e8c8dd8fa6a81288b2e5808dd1ffdfa500ab4]
- For performance, currency, percentage and unit queries are only processed when they begin with a digit and contain at least three characters. [@claim:clm_1e459434c8680b9e564234c27facf88c0eb80be4e684d7cbfa63bd90f8e23fe1]
- Calculate Anything is an Alfred 5 workflow that uses natural language to calculate currency, cryptocurrency, time, VAT, px/em/rem, percentage and other conversions. [@claim:clm_448b506a80edc83e9d87017247d715dc013584dcfd39eaf567ff3c521709d43f]
- The workflow is written in PHP; installation notes mention manually installing PHP with 'brew install php' if Alfred does not install dependencies automatically. [@claim:clm_6157d523d8f65a6e5ed70f6de7b840861dc38b8b3708221f7e6a1520b7c97292]
- Users can configure base currencies so a bare query like '120 euros' automatically converts to all configured base currencies. [@claim:clm_749b5aca3bb71a1620cb0b30a4bacf25c60fc2a75d34f8eb46aeb88e5bb9a60c]
- The workflow caches currency and cryptocurrency rates; users can clear the cache by typing '_caclear' in Alfred, and a workflow variable can define the currencies cache duration. [@claim:clm_a8119107a012c53f9622d00532fbb88a47e726e5ae671ee1b5a0cb6a5cd2a20a]
- Custom keywords map natural words to units or codes (e.g. 'ounces' to 'oz'), and stop words like 'to' are stripped after processing so '100km to cm' is understood as '100km cm'. [@claim:clm_aa30e888dc10430fe8424b281e7199741e16096e627f450bfc01efa59913dfb4]
- Currency conversion requires a free Fixer.io API key and cryptocurrency conversion a free CoinMarketCap API key, both configurable in the workflow configuration window. [@claim:clm_b836570795c854d9e2f36449aa17e08c74c91b1fe13fd543dabcc9f3d2b39e43]
- The workflow supports up to 168 fiat currencies, about 5,000 cryptocurrencies (with user-definable ones), and natural language in English, Spanish and Swedish. [@claim:clm_c28d84350b2e2644832d6b5c1d83c9e1583f1455b1170ef090ba349f401dbb14]
- Most conversions need no keywords or hotkeys: typing expressions like '100 + 16%', '100 euros to usd' or '100km in cm' directly in Alfred produces results. [@claim:clm_e75357727f2fc9e5a81ad07ce56cd31aebb4de40eaf5d166c55b44b0a10df3de]
- Result action modifiers copy values in different formats: Return copies formatted, Command+Return copies unformatted, and Option+Return copies a single-unit value. [@claim:clm_eb00516d9c20c621b336acdbe7666111a5fdc59019b868bbef82e710885096c6]
- Time and VAT conversions are exceptions requiring a keyword ('time', and by default 'vat', which is changeable) because they are less frequently used. [@claim:clm_f7ee36dee66a62acb1edf1a6dc4b850d19ae94fc583582262fb223d760a70ad3]
<!-- rcw:end owner=source:src_fe8c31fb77de54809a4fc3f0f0da5180 block=evidence -->

## Researcher notes

