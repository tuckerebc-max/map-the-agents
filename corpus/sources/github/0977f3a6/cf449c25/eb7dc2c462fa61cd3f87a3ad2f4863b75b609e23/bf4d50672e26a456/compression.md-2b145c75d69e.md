The output gets automatically compressed (when the format supports that), based
on the extension that you use for the output.

The following uses Gzip to compress the CSV file generated from the 
[Alpaca JSON](https://github.com/gururise/AlpacaDataCleaned/blob/main/alpaca_data_cleaned.json) 
dataset:

```bash
llm-convert \
  from-alpaca \
    --input ./alpaca_data_cleaned.json \
  to-csv-pr \
    --output alpaca_data_cleaned.csv.gz
```

The input gets automatically decompressed based on its extension, provided 
the format supports that.
