import json
import argparse
# import yaml
# import utils
import requests
import datetime
import argparse
import os

from dotenv import load_dotenv
load_dotenv()

parser = argparse.ArgumentParser()

parser.add_argument("type", help='items, collections, ..')
parser.add_argument("--start", help='page that starts from', default=1)
parser.add_argument("--debug", action='store_true')

args = parser.parse_args()

target = args.type

output_dir = os.environ['output_dir'] + "/api/" + target
os.makedirs(output_dir, exist_ok=True)

api_url = os.environ['api_url'] # settings["api_url"]

settings = os.environ

loop_flg = True
page = int(args.start)

query = ""
if "key" in settings and settings["key"] != None:
    query += "&key=" + settings["key"]

while loop_flg:

    url = api_url + "/"+target+"?page=" + str(
        page) + query

    if args.debug:
        print(datetime.datetime.now(), url)

    page += 1

    data = requests.get(url).json()
    
    if len(data) > 0 and "errors" not in data:
        for i in range(len(data)):
            obj = data[i]

            oid = str(obj["id"])

            with open(output_dir+"/"+oid+".json", 'w') as outfile:
                json.dump(obj, outfile, ensure_ascii=False,
                            indent=4, sort_keys=True, separators=(',', ': '))

    else:
        loop_flg = False
