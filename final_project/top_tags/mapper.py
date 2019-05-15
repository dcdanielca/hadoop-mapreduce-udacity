#! /usr/bin/python
import sys

for line in sys.stdin:
    data = line.split('\t')

    if len(data) >= 6 :
        tags = data[2].replace('"','').split()
        node_type = data[5].replace('"','')
        for tag in tags:
            print('{0}\t{1}'.format(tag, node_type))
    