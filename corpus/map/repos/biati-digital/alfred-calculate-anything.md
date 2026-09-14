# biati-digital/alfred-calculate-anything

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit fb98d4a78069 @ d59a15920312d7f7

## Summary (orientation draft, not independently verified)

Calculate Anything is a PHP-based Alfred 5 natural-language workflow for currency, cryptocurrency, unit, data-storage, percentage, px/em/rem, time and VAT conversions, configurable via the Alfred 5 configuration panel (or environment variables under Alfred 4) and dependent on Fixer.io and CoinMarketCap API keys. Evidence is documentation-only (README, README-ALFRED4, CHANGELOG); two prior claims were revised to drop uncited version numbers.

## Source coverage

Source coverage (complete): 3 of 3 candidate file(s) selected; repository tree complete. Claims by basis: 15 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

15 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications (2 claim(s)):
  - [observation/documented] Calculate Anything is an Alfred 5 workflow that uses natural language to calculate currency, cryptocurrency, time, VAT, px/em/rem, percentage and other conversions. -- evidence: [README.md#L3-L3](https://github.com/biati-digital/alfred-calculate-anything/blob/fb98d4a78069c5cf2ced4eea5dffbeef3d10c152/README.md#L3-L3)
  - [observation/documented] The workflow supports up to 168 fiat currencies, about 5,000 cryptocurrencies (with user-definable ones), and natural language in English, Spanish and Swedish. -- evidence: [README.md#L518-L522](https://github.com/biati-digital/alfred-calculate-anything/blob/fb98d4a78069c5cf2ced4eea5dffbeef3d10c152/README.md#L518-L522), [README.md#L131-L131](https://github.com/biati-digital/alfred-calculate-anything/blob/fb98d4a78069c5cf2ced4eea5dffbeef3d10c152/README.md#L131-L131), [README.md#L15-L26](https://github.com/biati-digital/alfred-calculate-anything/blob/fb98d4a78069c5cf2ced4eea5dffbeef3d10c152/README.md#L15-L26)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (5 claim(s)):
  - [observation/documented] Data storage conversions follow the IEC standard: 1MB in KB yields 1000 KB while 1MiB in KiB yields 1024 KB, and a 1MB=1024KB preference is configurable. -- evidence: [README.md#L360-L360](https://github.com/biati-digital/alfred-calculate-anything/blob/fb98d4a78069c5cf2ced4eea5dffbeef3d10c152/README.md#L360-L360), [README.md#L362-L362](https://github.com/biati-digital/alfred-calculate-anything/blob/fb98d4a78069c5cf2ced4eea5dffbeef3d10c152/README.md#L362-L362)
  - [observation/documented] Users can configure base currencies so a bare query like '120 euros' automatically converts to all configured base currencies. -- evidence: [README.md#L44-L58](https://github.com/biati-digital/alfred-calculate-anything/blob/fb98d4a78069c5cf2ced4eea5dffbeef3d10c152/README.md#L44-L58), [README.md#L60-L60](https://github.com/biati-digital/alfred-calculate-anything/blob/fb98d4a78069c5cf2ced4eea5dffbeef3d10c152/README.md#L60-L60)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (4 claim(s)):
  - [observation/documented] Most conversions need no keywords or hotkeys: typing expressions like '100 + 16%', '100 euros to usd' or '100km in cm' directly in Alfred produces results. -- evidence: [README.md#L11-L11](https://github.com/biati-digital/alfred-calculate-anything/blob/fb98d4a78069c5cf2ced4eea5dffbeef3d10c152/README.md#L11-L11)
  - [observation/documented] Time and VAT conversions are exceptions requiring a keyword ('time', and by default 'vat', which is changeable) because they are less frequently used. -- evidence: [README.md#L584-L584](https://github.com/biati-digital/alfred-calculate-anything/blob/fb98d4a78069c5cf2ced4eea5dffbeef3d10c152/README.md#L584-L584), [README.md#L496-L496](https://github.com/biati-digital/alfred-calculate-anything/blob/fb98d4a78069c5cf2ced4eea5dffbeef3d10c152/README.md#L496-L496), [README.md#L437-L437](https://github.com/biati-digital/alfred-calculate-anything/blob/fb98d4a78069c5cf2ced4eea5dffbeef3d10c152/README.md#L437-L437)
- memory-state (1 claim(s)):
  - [observation/documented] The workflow caches currency and cryptocurrency rates; users can clear the cache by typing '_caclear' in Alfred, and a workflow variable can define the currencies cache duration. -- evidence: [CHANGELOG.md#L68-L76](https://github.com/biati-digital/alfred-calculate-anything/blob/fb98d4a78069c5cf2ced4eea5dffbeef3d10c152/CHANGELOG.md#L68-L76), [README.md#L588-L588](https://github.com/biati-digital/alfred-calculate-anything/blob/fb98d4a78069c5cf2ced4eea5dffbeef3d10c152/README.md#L588-L588)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
  - [observation/documented] Currency conversion requires a free Fixer.io API key and cryptocurrency conversion a free CoinMarketCap API key, both configurable in the workflow configuration window. -- evidence: [README.md#L160-L160](https://github.com/biati-digital/alfred-calculate-anything/blob/fb98d4a78069c5cf2ced4eea5dffbeef3d10c152/README.md#L160-L160), [README.md#L81-L81](https://github.com/biati-digital/alfred-calculate-anything/blob/fb98d4a78069c5cf2ced4eea5dffbeef3d10c152/README.md#L81-L81)
  - [observation/documented] The workflow is written in PHP; installation notes mention manually installing PHP with 'brew install php' if Alfred does not install dependencies automatically. -- evidence: [README.md#L30-L30](https://github.com/biati-digital/alfred-calculate-anything/blob/fb98d4a78069c5cf2ced4eea5dffbeef3d10c152/README.md#L30-L30)
- limitations (1 claim(s)):
More evidence: [full detail](alfred-calculate-anything.detail.md)

Metadata and full claim list: [full detail](alfred-calculate-anything.detail.md)
Human notes ([notes](alfred-calculate-anything.notes.md), never overwritten by build)

[Back to map index](../../index.md)
