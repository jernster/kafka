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

lc_partitions = [ p['partition'] for p in output['partitions'] ]
lc_leader = [ l['leader'] for l in output['partitions'] ]
lc_replicas = [ r['replicas'] for r in output['partitions'] ]
#print(partitions)
#print(leader)
##print(len(replicas))
##print(broker)
#print(type(replicas))
#for k,v in replicas[0][0]['broker']:
#    print(k,v)
#print(replicas[0][0]['broker'],replicas[0][0]['leader'],replicas[0][0]['in_sync'],
#      replicas[1][1]['broker'],replicas[1][1]['leader'],replicas[1][1]['in_sync'])

##for item in replicas:
    #print(item[v][v]['broker'], item[v][v]['leader'], item[v][v]['in_sync'])
    #print(item[0],item[1])
    #print(item[0]['broker'])
##    print(item)

# TypeError: list indices must be integers or slices, not dict
# for index in range(len(replicas)):
#     for key in replicas[index]:
#         print(replicas[index][key])

# TypeError: unhashable type: 'dict'
# for dic in replicas:
#     for i,key in enumerate(dic):
#         print(dic[i][key])

# >>> for i in iter_list:
# ...     for x in range(3):
# ...         for key, value in i.iteritems():
# ...             print key, value[x]

# for i in replicas:
#     for x in (range(len(replicas))):
#         for key, value in i.iteritems():
#             print(key,value[x])

# for index in replicas:

#     #index = len(index)
#     print(index)

#result = [[replicas[i] for row in replicas] for i in range(2)]
#result = next(item for item in replicas)
#print(result)

#print(len(replicas))

#broker0 = [ x[0]['broker'] for x in lc_replicas ]
#leader0 = [ x[0]['leader'] for x in lc_replicas ]
#in_sync0 = [ x[0]['in_sync'] for x in lc_replicas ]
#print(broker0)
#print(leader0)
#print(in_sync0)
#print(end='\n')
#broker1 = [ x[1]['broker'] for x in lc_replicas ]
#leader1 = [ x[1]['leader'] for x in lc_replicas ]
#in_sync1 = [ x[1]['in_sync'] for x in lc_replicas ]
#print(broker1)
#print(leader1)
#print(in_sync1)

#for p,l in zip(partitions, leader):
    #print(p, l, r)
    #print(p, l, end=' ')
#    for b0,l0,i0,b1,l1,i1 in zip(broker0, leader0, in_sync0, broker1, leader1, in_sync1):
#        print(b0,l0,i0,b1,l1,i1, end='\n')


#for slice in lc_replicas:
    #print(len(slice))
#    slice = len(slice)

##for i in range(slice):
##    print(i)
##    broker = [ x[i]['broker'] for x in lc_replicas ]
##    leader = [ x[i]['leader'] for x in lc_replicas ]
##    in_sync = [ x[i]['in_sync'] for x in lc_replicas ]
    #print(broker)
    #print(leader)
    #print(in_sync)
##    for lc_p,lc_l,b,l,i in zip(lc_partitions, lc_leader, broker, leader, in_sync):
##        print('Partitions: Partition - {0} Leader - {1} Replicas: Broker - {2} Leader - {3} In_Sync - {4}'.format(lc_p, lc_l, b, l, i))
    #print(lc_p, lc_l, l, b, i, end=' ')

for p in output['partitions']:
  print(f"Partitions: Partition - {p['partition']} Leader - {p['leader']} Replicas:", end=" ")
  for r in p['replicas']:
    print(f"Broker - {r['broker']} Leader - {r['leader']} - In_Sync - {r['in_sync']}", end=" ")
  print()  # newline

#for b0,l0,i0,b1,l1,i1 in zip(broker0, leader0, in_sync0, broker1, leader1, in_sync1):
#    print(b0,l0,i0,b1,l1,i1)