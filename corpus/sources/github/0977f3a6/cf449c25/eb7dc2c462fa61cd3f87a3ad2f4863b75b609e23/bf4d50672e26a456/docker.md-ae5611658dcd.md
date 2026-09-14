Below are examples for using the llm-dataset-converter library via its 
[Docker images](https://github.com/waikato-llm/llm-dataset-converter-all/tree/main/docker).


# Interactive session

The following command starts an interactive session, mapping the current working
directory to `/workspace`:

```bash
docker run --rm -u $(id -u):$(id -g) \
    -v `pwd`:/workspace \
    -it waikatodatamining/llm-dataset-converter:latest
```

# Conversion pipeline

The following converts the [Alpaca](https://github.com/gururise/AlpacaDataCleaned/blob/main/alpaca_data_cleaned.json) 
dataset from JSON into CSV format:

```bash
docker run --rm -u $(id -u):$(id -g) \
    -v `pwd`:/workspace \
    -it waikatodatamining/llm-dataset-converter:latest \
    llm-convert \
      -l INFO \
      from-alpaca \
        --input /workspace/alpaca_data_cleaned.json \
        -l INFO \
      to-csv-pr \
        --output /workspace/alpaca_data_cleaned.csv
        -l INFO
```

**NB:** The `input` and `output` directories are located below the current working directory (`pwd`).
