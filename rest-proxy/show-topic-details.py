import argparse
import requests

parser = argparse.ArgumentParser(description="Display topic details from REST Proxy")
parser.add_argument("--url", help="Provide URL to REST Proxy", required=True) # http://localhost:8082/topics/topicname 
parser.add_argument("--topic", help="Provide topic name", required=True)

args = parser.parse_args()

url = args.url
topic = args.topic

r = requests.get(url + topic)

#for topic in r.json():
#    print(topic)

output = r.json()

#print(output['name'])
#print(output['configs'])
#print(output['partitions'])
print(output['name'])

#for k,v in output['configs'].items():
#    print(k,v)

#for k in output['partitions'][0]:
#    print(k)

partitions = [ p['partition'] for p in output['partitions'] ]
leader = [ l['leader'] for l in output['partitions'] ]
replicas = [ r['replicas'] for r in output['partitions'] ]
##broker = [ b['broker'] for b in replicas ]
#print(partitions)
#print(leader)
#print(len(replicas))
##print(broker)
#print(type(replicas))
#for k,v in replicas[0][0]['broker']:
#    print(k,v)
#print(replicas[0][0]['broker'],replicas[0][0]['leader'],replicas[0][0]['in_sync'],
#      replicas[1][1]['broker'],replicas[1][1]['leader'],replicas[1][1]['in_sync'])

for item in replicas:
    #print(item[v][v]['broker'], item[v][v]['leader'], item[v][v]['in_sync'])
    print(item[0],item[1])

#for p,l,r in zip(partitions, leader, replicas):
#    print(p, l, r)