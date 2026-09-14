# biati-digital/alfred-calculate-anything -- full detail

[Back to orientation](alfred-calculate-anything.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/biati-digital/alfred-calculate-anything/fb98d4a78069c5cf2ced4eea5dffbeef3d10c152/d59a15920312d7f7.json](../../../wiki/dossiers/biati-digital/alfred-calculate-anything/fb98d4a78069c5cf2ced4eea5dffbeef3d10c152/d59a15920312d7f7.json)

## specifications (2 claim(s))

- [observation/documented] Calculate Anything is an Alfred 5 workflow that uses natural language to calculate currency, cryptocurrency, time, VAT, px/em/rem, percentage and other conversions. -- evidence: [README.md#L3-L3](https://github.com/biati-digital/alfred-calculate-anything/blob/fb98d4a78069c5cf2ced4eea5dffbeef3d10c152/README.md#L3-L3) (`clm_448b506a80edc83e9d87017247d715dc013584dcfd39eaf567ff3c521709d43f`)
- [observation/documented] The workflow supports up to 168 fiat currencies, about 5,000 cryptocurrencies (with user-definable ones), and natural language in English, Spanish and Swedish. -- evidence: [README.md#L518-L522](https://github.com/biati-digital/alfred-calculate-anything/blob/fb98d4a78069c5cf2ced4eea5dffbeef3d10c152/README.md#L518-L522), [README.md#L131-L131](https://github.com/biati-digital/alfred-calculate-anything/blob/fb98d4a78069c5cf2ced4eea5dffbeef3d10c152/README.md#L131-L131), [README.md#L15-L26](https://github.com/biati-digital/alfred-calculate-anything/blob/fb98d4a78069c5cf2ced4eea5dffbeef3d10c152/README.md#L15-L26) (`clm_c28d84350b2e2644832d6b5c1d83c9e1583f1455b1170ef090ba349f401dbb14`)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (5 claim(s))

- [observation/documented] Data storage conversions follow the IEC standard: 1MB in KB yields 1000 KB while 1MiB in KiB yields 1024 KB, and a 1MB=1024KB preference is configurable. -- evidence: [README.md#L360-L360](https://github.com/biati-digital/alfred-calculate-anything/blob/fb98d4a78069c5cf2ced4eea5dffbeef3d10c152/README.md#L360-L360), [README.md#L362-L362](https://github.com/biati-digital/alfred-calculate-anything/blob/fb98d4a78069c5cf2ced4eea5dffbeef3d10c152/README.md#L362-L362) (`clm_060c083c22fc4690f8b113ce863e8c8dd8fa6a81288b2e5808dd1ffdfa500ab4`)
- [observation/documented] Users can configure base currencies so a bare query like '120 euros' automatically converts to all configured base currencies. -- evidence: [README.md#L44-L58](https://github.com/biati-digital/alfred-calculate-anything/blob/fb98d4a78069c5cf2ced4eea5dffbeef3d10c152/README.md#L44-L58), [README.md#L60-L60](https://github.com/biati-digital/alfred-calculate-anything/blob/fb98d4a78069c5cf2ced4eea5dffbeef3d10c152/README.md#L60-L60) (`clm_749b5aca3bb71a1620cb0b30a4bacf25c60fc2a75d34f8eb46aeb88e5bb9a60c`)
- [observation/documented] Custom keywords map natural words to units or codes (e.g. 'ounces' to 'oz'), and stop words like 'to' are stripped after processing so '100km to cm' is understood as '100km cm'. -- evidence: [README.md#L567-L567](https://github.com/biati-digital/alfred-calculate-anything/blob/fb98d4a78069c5cf2ced4eea5dffbeef3d10c152/README.md#L567-L567), [README.md#L534-L534](https://github.com/biati-digital/alfred-calculate-anything/blob/fb98d4a78069c5cf2ced4eea5dffbeef3d10c152/README.md#L534-L534), [README.md#L576-L578](https://github.com/biati-digital/alfred-calculate-anything/blob/fb98d4a78069c5cf2ced4eea5dffbeef3d10c152/README.md#L576-L578) (`clm_aa30e888dc10430fe8424b281e7199741e16096e627f450bfc01efa59913dfb4`)
- [observation/documented] For performance, currency, percentage and unit queries are only processed when they begin with a digit and contain at least three characters. -- evidence: [README.md#L584-L584](https://github.com/biati-digital/alfred-calculate-anything/blob/fb98d4a78069c5cf2ced4eea5dffbeef3d10c152/README.md#L584-L584) (`clm_1e459434c8680b9e564234c27facf88c0eb80be4e684d7cbfa63bd90f8e23fe1`)
- [inference/documented] Currency conversion is prioritized over cryptocurrency when codes collide (e.g. GBP), apparently because many cryptocurrencies share codes with fiat currencies; this is configurable. -- evidence: [CHANGELOG.md#L63-L64](https://github.com/biati-digital/alfred-calculate-anything/blob/fb98d4a78069c5cf2ced4eea5dffbeef3d10c152/CHANGELOG.md#L63-L64) (`clm_42f12d303d64f98d69d2e374aed1ce933ea6abf566e03c1b661f1cb729069391`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (4 claim(s))

- [observation/documented] Most conversions need no keywords or hotkeys: typing expressions like '100 + 16%', '100 euros to usd' or '100km in cm' directly in Alfred produces results. -- evidence: [README.md#L11-L11](https://github.com/biati-digital/alfred-calculate-anything/blob/fb98d4a78069c5cf2ced4eea5dffbeef3d10c152/README.md#L11-L11) (`clm_e75357727f2fc9e5a81ad07ce56cd31aebb4de40eaf5d166c55b44b0a10df3de`)
- [observation/documented] Time and VAT conversions are exceptions requiring a keyword ('time', and by default 'vat', which is changeable) because they are less frequently used. -- evidence: [README.md#L584-L584](https://github.com/biati-digital/alfred-calculate-anything/blob/fb98d4a78069c5cf2ced4eea5dffbeef3d10c152/README.md#L584-L584), [README.md#L496-L496](https://github.com/biati-digital/alfred-calculate-anything/blob/fb98d4a78069c5cf2ced4eea5dffbeef3d10c152/README.md#L496-L496), [README.md#L437-L437](https://github.com/biati-digital/alfred-calculate-anything/blob/fb98d4a78069c5cf2ced4eea5dffbeef3d10c152/README.md#L437-L437) (`clm_f7ee36dee66a62acb1edf1a6dc4b850d19ae94fc583582262fb223d760a70ad3`)
- [observation/documented] Result action modifiers copy values in different formats: Return copies formatted, Command+Return copies unformatted, and Option+Return copies a single-unit value. -- evidence: [README.md#L151-L156](https://github.com/biati-digital/alfred-calculate-anything/blob/fb98d4a78069c5cf2ced4eea5dffbeef3d10c152/README.md#L151-L156), [README.md#L72-L77](https://github.com/biati-digital/alfred-calculate-anything/blob/fb98d4a78069c5cf2ced4eea5dffbeef3d10c152/README.md#L72-L77), [README.md#L201-L206](https://github.com/biati-digital/alfred-calculate-anything/blob/fb98d4a78069c5cf2ced4eea5dffbeef3d10c152/README.md#L201-L206) (`clm_eb00516d9c20c621b336acdbe7666111a5fdc59019b868bbef82e710885096c6`)
- [observation/documented] For Alfred 4 installs, configuration is done through environment variables such as language, base_currency, fixer_apikey, coinmarket_apikey, time_format, time_zone and vat_percentage. -- evidence: [README-ALFRED4.md#L11-L17](https://github.com/biati-digital/alfred-calculate-anything/blob/fb98d4a78069c5cf2ced4eea5dffbeef3d10c152/README-ALFRED4.md#L11-L17), [README-ALFRED4.md#L5-L5](https://github.com/biati-digital/alfred-calculate-anything/blob/fb98d4a78069c5cf2ced4eea5dffbeef3d10c152/README-ALFRED4.md#L5-L5), [README-ALFRED4.md#L9-L9](https://github.com/biati-digital/alfred-calculate-anything/blob/fb98d4a78069c5cf2ced4eea5dffbeef3d10c152/README-ALFRED4.md#L9-L9) (`clm_b00b5d5764a480217a4f4cb89fe6641d81db6af8bbc7bd99b47429c75ed30239`)

## memory-state (1 claim(s))

- [observation/documented] The workflow caches currency and cryptocurrency rates; users can clear the cache by typing '_caclear' in Alfred, and a workflow variable can define the currencies cache duration. -- evidence: [CHANGELOG.md#L68-L76](https://github.com/biati-digital/alfred-calculate-anything/blob/fb98d4a78069c5cf2ced4eea5dffbeef3d10c152/CHANGELOG.md#L68-L76), [README.md#L588-L588](https://github.com/biati-digital/alfred-calculate-anything/blob/fb98d4a78069c5cf2ced4eea5dffbeef3d10c152/README.md#L588-L588) (`clm_a8119107a012c53f9622d00532fbb88a47e726e5ae671ee1b5a0cb6a5cd2a20a`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] Currency conversion requires a free Fixer.io API key and cryptocurrency conversion a free CoinMarketCap API key, both configurable in the workflow configuration window. -- evidence: [README.md#L160-L160](https://github.com/biati-digital/alfred-calculate-anything/blob/fb98d4a78069c5cf2ced4eea5dffbeef3d10c152/README.md#L160-L160), [README.md#L81-L81](https://github.com/biati-digital/alfred-calculate-anything/blob/fb98d4a78069c5cf2ced4eea5dffbeef3d10c152/README.md#L81-L81) (`clm_b836570795c854d9e2f36449aa17e08c74c91b1fe13fd543dabcc9f3d2b39e43`)
- [observation/documented] The workflow is written in PHP; installation notes mention manually installing PHP with 'brew install php' if Alfred does not install dependencies automatically. -- evidence: [README.md#L30-L30](https://github.com/biati-digital/alfred-calculate-anything/blob/fb98d4a78069c5cf2ced4eea5dffbeef3d10c152/README.md#L30-L30) (`clm_6157d523d8f65a6e5ed70f6de7b840861dc38b8b3708221f7e6a1520b7c97292`)

## limitations (1 claim(s))

- [observation/documented] The changelog notes the auto-updater was removed because Alfred 5 handles future updates, and the old 'ca' configuration keyword was removed. -- evidence: [CHANGELOG.md#L42-L59](https://github.com/biati-digital/alfred-calculate-anything/blob/fb98d4a78069c5cf2ced4eea5dffbeef3d10c152/CHANGELOG.md#L42-L59) (`clm_427c6c730d5ea8bb88b4a2300d9768e6d9d679c14d08bafdd006a85b8b7fa328`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

