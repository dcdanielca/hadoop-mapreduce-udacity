#!/usr/bin/python
import sys

old_store = None
cost_max = 0.0

for line in sys.stdin:
    data = line.strip().split("\t")
    current_store, current_cost = data

    if old_store and old_store != current_store:
        print(old_store, '\t', cost_max)
        old_store = current_store
        cost_max = 0.0
    old_store = current_store
    cost_max = max(float(current_cost), cost_max)
    
if old_store:    
    print(old_store, '\t', cost_max)

