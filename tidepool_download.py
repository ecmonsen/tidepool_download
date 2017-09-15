# Download data from tidepool
# See http://support.tidepool.org/article/37-export-your-account-data

import requests
from requests.auth import HTTPBasicAuth
import json, flatten_json, sys, csv

TIDEPOOL_LOGIN_URL="https://api.tidepool.org/auth/login"
TIDEPOOL_API_URL="https://api.tidepool.org/data/{userid}"
TIDEPOOL_TOKEN_HEADER="x-tidepool-session-token"
TIDEPOOL_CONTENT_ENCODING="utf-8" # assumed

def download_tidepool(email, password, fp=sys.stdout, login_url=TIDEPOOL_LOGIN_URL, format='json'):
    login_response = requests.post(login_url, auth=HTTPBasicAuth(email, password))
    token = login_response.headers[TIDEPOOL_TOKEN_HEADER]
    login_content = json.loads(login_response.content)
    userid = login_content["userid"]
    api_url = TIDEPOOL_API_URL.format(userid=userid)
    content_type="application/json"
    api_response = requests.get(api_url, headers={ TIDEPOOL_TOKEN_HEADER: token, "Content-Type": content_type})
    global ar
    ar = api_response
    if format == 'json':
        # Write JSON content as is
        fp.write(api_response.content.decode(TIDEPOOL_CONTENT_ENCODING))
    else:
        data = json.loads(api_response.content)

        if format == 'json_lines':
            for line in data:
                fp.write(json.dumps(line)+"\n")
        elif format in ['csv', 'flat_json', 'flat_json_lines']:
            # Flatten JSON objects
            flat_data = [flatten_json.flatten(i, separator=".") for i in data]
            if format == 'flat_json':
                json.dump(flat_data, fp)
            elif format == 'flat_json_lines':
                for line in flat_data:
                    fp.write(json.dumps(line)+"\n")
            else: # csv
                # get all possible keys
                allkeys = set([])
                for d in flat_data:
                    allkeys = allkeys.union(set(d.keys()))
                allkeys=sorted(allkeys)
                csvwriter = csv.writer(fp)
                csvwriter.writerow(allkeys)
                for f in flat_data:
                    to_write = [f.get(key) for key in allkeys]
                    csvwriter.writerow(to_write)
        else:
            raise Exception("Format not supported: {0}".format(format))

def main():
    import argparse, os, getpass
    parser = argparse.ArgumentParser(description="Download type 1 diabetes data from Tidepool.org")
    parser.add_argument("email")
    parser.add_argument("--format", default="csv")
    args = parser.parse_args()

    password = os.environ.get("TIDEPOOL_PASS")
    if not password:
        password = getpass.getpass(prompt="Enter your Tidepool.org password: ")
        print("Hint: you can also set the TIDEPOOL_PASS environment variable",file=sys.stderr)

    download_tidepool(args.email, password, sys.stdout, format=args.format)

if __name__=="__main__":
    main()
