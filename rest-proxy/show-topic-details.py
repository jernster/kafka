import argparse
import requests

parser = argparse.ArgumentParser(description="Display topic details from REST Proxy")
parser.add_argument("--url", "-u", help="Provide URL to REST Proxy", required=True) # http://localhost:8082/topics/ 
parser.add_argument("--topic", "-t", help="Provide topic name", required=True)

args = parser.parse_args()

url = args.url
topic = args.topic

r = requests.get(url + topic)

output = r.json()

print("Topic Name:")
print('=' * 30)
print(output['name'])
print()


print("Topic Configuration:")
print('=' * 30)
for k,v in output['configs'].items():
    print(k,v)
print()

print("Partitions:")
print('=' * 30)
for p in output['partitions']:
  #print(f"Partitions: Partition - {p['partition']} Leader - {p['leader']} Replicas:", end=" ")
  print("Partitions: Partition - {0} Leader - {1} Replicas:".format(p['partition'], p['leader']), end=" ")
  for r in p['replicas']:
    #print(f"Broker - {r['broker']} Leader - {r['leader']} - In_Sync - {r['in_sync']}", end=" ")
    print("Broker - {0} Leader - {1} - In_Sync - {2}".format(r['broker'], r['leader'], r['in_sync']), end=" ")
  print()