#!/usr/bin/env python
# import sys

# old_day = None
# sales = 0

# for line in sys.stdin:
#     data = line.strip().split("\t")
#     current_day, current_cost = data

#     if old_day and old_day != current_day:
#         print(old_day, '\t', sales)
#         old_day = current_day
#         sales = 0
#     old_day = current_day
#     sales += float(current_cost)    

# if old_day:
#     print(old_day, '\t', sales)


import sys
from datetime import datetime

sales_for_each_day_of_the_week = [0] * 7
for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 2:
        weekday, sale = data
        sales_for_each_day_of_the_week[int(weekday)] += float(sale)

for weekday, sales_total in enumerate(sales_for_each_day_of_the_week):
    print("{0}\t{1}".format(weekday, sales_total))