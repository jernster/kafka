# python delete-topics.py topics.txt
import os
import sys


file = sys.argv[1]

with open(file, 'r') as f:
    lines = f.readlines()

for line in lines:
    line = line.strip()
    print('Deleting topic {}'.format(line))
    os.system("kafka-topics --zookeeper zk-1:2181,zk-2:2181,zk-3:2181/kafka --delete --topic {}".format(line))
