import argparse
import requests

parser = argparse.ArgumentParser(description="Kafka Connector statuses")
parser.add_argument("--url", help="Kafka Connect URL", required=True) # http://localhost:8083/connectors/ 

args = parser.parse_args()

connect_url = args.url

r = requests.get(connect_url)

# print(r) # <Response [200]>

print(type(r.json))
connectors = []
connectors = r.json()
print(type(connectors))
#print(r.json())
print(connectors)

for connector in connectors:
    print(connector)