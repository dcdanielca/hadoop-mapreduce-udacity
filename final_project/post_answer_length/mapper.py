#!/usr/bin/python
import sys
import csv
import re

reader = csv.reader(sys.stdin, delimiter='\t')

for line in reader:
    try:
        words = re.sub(r'\n|<\w*>|</\w*>', '', line[4])
        if line[5] == "question":
            print("{0}\t{1}\t{2}".format(line[0], words, line[5]))
        else:
            print("{0}\t{1}\t{2}".format(line[6], words, line[5]))
    except ValueError:  
        continue
