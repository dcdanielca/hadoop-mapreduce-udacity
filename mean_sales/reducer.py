#!/usr/bin/python
import sys

old_day = None
sales = []

for line in sys.stdin:
    data = line.strip().split("\t")
    current_day, current_cost = data

    if old_day and old_day != current_day:
        print(old_day, '\t', sum(sales)/len(sales))
        old_day = current_day
        sales = []
    old_day = current_day
    sales.append(float(current_cost))

if old_day:
    print(old_day, '\t', sum(sales)/len(sales))
