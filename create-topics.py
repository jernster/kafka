# python create-topics.py topics.txt
import os
import sys


file = sys.argv[1]

with open(file, 'r') as f:
    lines = f.readlines()

for line in lines:
    line = line.strip()
    print('Creating topic {}'.format(line))
    os.system("kafka-topics --zookeeper zk-1:2181,zk-2:2181,zk-3:2181/kafka --create --topic {} --replication-factor 1 --config retention.ms=86400000 --config compression.type=gzip --partitions 12".format(line))
