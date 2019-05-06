#!/usr/bin/python
import sys

old_store = None
total_sales = 0.0
number_sales = 0

for line in sys.stdin:
    data = line.strip().split("\t")
    current_cost = data[1]
    number_sales += 1
    total_sales += float(current_cost)
print('number sales ', number_sales)
print('total sales ', total_sales)