## Quickstart Data Catalog API

This quickstart can be used as template.
It has calls for searching catalogs with organisation ids or project ids.

## Requirements

- Have a GCP project with the billing activated.

- In GCP console, API & Services > Library, search for Data Catalog, select Google Cloud Data Catalog API and click Enable.

- Have Google SDK (https://cloud.google.com/sdk)

- Python >= 3.6 (https://www.python.org/downloads/windows/)

- Python virtualenv and pip installed

- Update config file to search with project ids or organisation ids

## Setup

```bash
# Install Google Cloud CLI
sudo apt-get update && sudo apt-get install google-cloud-cli
gcloud init

# Create virtualenv
python3 -m venv venv

# Activate venv
source venv/bin/activate

# Install client library
pip install google-cloud-datacatalog
```

## Main

```bash
# Execute examples in main
python main.py
```

## Documentation

Link to the official Google Data Catalog documentation: https://cloud.google.com/data-catalog/docs/reference/rest
Search syntax for search_catalog(): https://cloud.google.com/data-catalog/docs/how-to/search-reference
Lookup entry target names: https://cloud.google.com/data-catalog/docs/reference/rest/v1/entries/lookup
GCP Full resource name: https://cloud.google.com/apis/design/resource_names#full_resource_name
