import argparse
import requests

parser = argparse.ArgumentParser(description="Kafka Connector statuses")
parser.add_argument("--url", help="Kafka Connect URL", required=True) # http://localhost:8083/connectors 

args = parser.parse_args()

connect_url = args.url

r = requests.get(connect_url)

connectors = []
connectors = r.json()

for connector in connectors:
    connect_status_url = args.url + '/' + connector + '/status'
    
    r = requests.get(connect_status_url)

    connector_status = r.json()

    for k,v in connector_status.items():
        print("{0}: {1}".format(k,v))
    print('=' * 50)