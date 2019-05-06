#!/usr/bin/python
import sys

old_ip = None
hits = 0

for current_ip in sys.stdin:
    current_ip = current_ip[:len(current_ip)-1]
    if old_ip and old_ip != current_ip:
        print(old_ip, '\t', hits)
        old_ip = current_ip
        hits = 0
    old_ip = current_ip
    hits += 1

if old_ip:  
    print(old_ip, '\t', hits)