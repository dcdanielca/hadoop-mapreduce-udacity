#!/usr/bin/python
import sys

old_category = None
total_sales = 0.0

for line in sys.stdin:
    data = line.strip().split("\t")
    current_category, cost = data

    if old_category and old_category != current_category:
        print(old_category, '\t', total_sales)
        total_sales = 0.0
        old_category = current_category
    old_category = current_category
    total_sales += float(cost)
    
if old_category:    
    print(old_category, '\t', total_sales)
