#! /usr/bin/python
import sys

for line in sys.stdin:
    data = line.split('\t')
    if len(data) >= 7:
        if data[5] == '"answer"':
            print(data[6], '\t', data[3])

