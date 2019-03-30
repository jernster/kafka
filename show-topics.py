import argparse
import requests

parser = argparse.ArgumentParser(description="Display topics from REST Proxy")
parser.add_argument("--url", help="show topics", required=True) # http://localhost:8082/topics/ 

args = parser.parse_args()

url = args.url

r = requests.get(url)

for topic in r.json():
    print(topic)