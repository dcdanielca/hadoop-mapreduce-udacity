#! /usr/bin/python
import sys

old_tag = None
count = 0
for line in sys.stdin:
    current_tag, node_type = line.split('\t')
    if old_tag and old_tag != current_tag:
        print(old_tag, '\t', count, '\t', node_type, end='')
        old_tag = current_tag
        count = 0
    old_tag = current_tag
    count += 1
    
if old_tag:
    print(old_tag, '\t', count, '\t', node_type, end='')