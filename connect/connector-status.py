import argparse
import requests

parser = argparse.ArgumentParser(description="Kafka Connector statuses")
parser.add_argument("--url", help="Kafka Connect URL", required=True) # http://localhost:8083/connectors/ 

args = parser.parse_args()

connect_url = args.url

r = requests.get(connect_url)

# print(r) # <Response [200]>

#print(type(r.json))
connectors = []
connectors = r.json()
#print(type(connectors))
#print(r.json())
#print(connectors)

for connector in connectors:
    #print(connector)
    connect_status_url = args.url + '/' + connector + '/status'
    #print(connect_status_url)
    r = requests.get(connect_status_url)
    connector_status = r.json()
    #print(type(connector_status))
    #print(connector_status)
    for k,v in connector_status.items():
        #str = "{0}: {1}".format(k,v)
        #print(str)
        #if type(v) == dict:
            #print(k)
        #    for k,v in v.items():
        #        print(f"{k}: {v}")
            #print("{0} is a dict".format(v))
            #print(v.items())

        ##print(type(v))
        print(f"{k}: {v}")
    print('=' * 50)