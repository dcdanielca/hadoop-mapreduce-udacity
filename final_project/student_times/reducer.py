#!/usr/bin/python
import sys
import csv
import operator

old_user = None
hours = {h:0 for h in range(24)}

for line in sys.stdin:
    current_user, hour = line.split('\t')
    if old_user and old_user != current_user:
        hours = dict(sorted(hours.items(), key=operator.itemgetter(1), reverse = True))
        print(old_user, '\t', next(iter(hours)))
        old_user = current_user
        hours = {h:0 for h in range(24)}
    old_user = current_user
    hours[int(hour)] +=1

if old_user:
    hours = dict(sorted(hours.items(), key=operator.itemgetter(1), reverse = True))
    print(old_user, '\t', next(iter(hours)))