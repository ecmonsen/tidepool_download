# Tidepool Download

This is a Python script for downloading Type 1 Diabetes data from Tidepool.org.

## Prerequisites
Uses Python 3.

## Getting Started
Install the requirements:

`pip install -r requirements.txt`

Then run the command line. Have your Tidepool.org email and password ready.

`python3 tidepool_download.py <your_email_address> --format csv > /tmp/download.csv`


## Supported formats

### csv
Comma-separated values

```
time,recommended.carb,recommended.correction,recommended.net
2016-10-30T14:24:57.000Z,0.9,0,0.9
2016-10-31T11:19:19.000Z,1.2,0.1,1.3
```

### json
JSON array

```
[
  {"time":"2016-10-30T14:24:57.000Z", "recommended": {"carb": 0.9, "correction": 0, "net": 0.9}}, 
  {"time":"2016-10-31T11:19:19.000Z", "recommended": {"carb": 1.2, "correction": 0.1, "net": 1.3}}
]
```

### json\_lines 
One JSON object per line

```
{"time":"2016-10-30T14:24:57.000Z", "recommended": {"carb": 0.9, "correction": 0, "net": 0.9}}, 
{"time":"2016-10-31T11:19:19.000Z", "recommended": {"carb": 1.2, "correction": 0.1, "net": 1.3}}
```


### flat\_json 
JSON array, but each top level array item is flattened

```
[
  {"time":"2016-10-30T14:24:57.000Z", "recommended.carb": 0.9, "recommended.correction": 0, "recommended.net": 0.9}, 
  {"time":"2016-10-31T11:19:19.000Z", "recommended.carb": 1.2, "recommended.correction": 0.1, "recommended.net": 1.3}
]
```

### flat\_json\_lines
One flattened JSON object per line

```
{"time":"2016-10-30T14:24:57.000Z", "recommended.carb": 0.9, "recommended.correction": 0, "recommended.net": 0.9}, 
{"time":"2016-10-31T11:19:19.000Z", "recommended.carb": 1.2, "recommended.correction": 0.1, "recommended.net": 1.3}
```

