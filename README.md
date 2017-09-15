# Tidepool Download

This is a Python script for downloading Type 1 Diabetes data from Tidepool.org.

## Prerequisites
Uses Python 3.

## Getting Started
Install the requirements:

`pip install -r requirements.txt`

Then run the command line. Have your Tidepool.org email and password ready.

`python3 tidepool_download.py <your_email_address> > /tmp/download.csv`


## Supported formats

| format  | description  |
|---|---|
| csv  | Comma-separated values  |
| json  | JSON array  |
| json_lines | One JSON object per line |
| flat_json | JSON array, but each top level array item is flattened |
| flat_json_lines | One flattened JSON object per line |

