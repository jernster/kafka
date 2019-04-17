import argparse
import requests

parser = argparse.ArgumentParser(description="Kafka Connector status")
parser.add_argument("--url", "-u", help="Kafka Connect URL (http://localhost:8083/connectors/)", required=True) # http://localhost:8083/connectors/ 
parser.add_argument("--connector", "-c", help="Connector name", required=True) 

args = parser.parse_args()

connect_url = args.url
connector_name = args.connector

connect_status_url = args.url + connector_name + '/status'
   
r = requests.get(connect_status_url)

connector_status = r.json()

print("Connector Name: {0}".format(connector_status['name']))
print('=' * 50)

for k,v in connector_status['connector'].items():
    print("{0}: {1}".format(k,v), end=' ')
print()
print('=' * 50)

for c in connector_status['tasks']:
    print("Task: ", end=' ')
    print("state: {0}".format(c['state']), end=' ')
    print("id: {0}".format(c['id']), end=' ')
    print("worker_id: {0}".format(c['worker_id']), end='\n')
