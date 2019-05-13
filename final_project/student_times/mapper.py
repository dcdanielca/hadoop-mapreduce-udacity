#!/usr/bin/python
from datetime import datetime

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

for line in reader:
    try:                
        if len(line) == 19:
            hour = datetime.strptime(line[8], "%Y-%m-%d %H:%M:%S.%f+00").strftime("%H")
            newLine = "{0}\t{1}".format(line[3], int(hour))
            print(newLine)
    except Exception as e:
        None