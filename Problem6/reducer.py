#!/usr/bin/python
import sys

old_file = None
hits = 0

for current_file in sys.stdin:
    current_file = current_file[:len(current_file)-1]
    if old_file and old_file != current_file:
        print(old_file, '\t', hits)
        old_file = current_file
        hits = 0
    old_file = current_file
    hits += 1

if old_file:  
    print(old_file, '\t', hits)
