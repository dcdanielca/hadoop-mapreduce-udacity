#!/usr/bin/python
import sys

old_request = None
hits = 0

for current_request in sys.stdin:
    current_request = current_request[:len(current_request)-1]
    if old_request and old_request != current_request:
        print(old_request, '\t', hits)
        old_request = current_request
        hits = 0
    old_request = current_request
    hits += 1
