#!/usr/bin/python
import sys
import csv
import re

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

for line in reader:
    try:
        words = re.split(r'\n| |\.|,|!|\?|:|;|"|\(|\)|<\w*>|</\w*>|\<|\>|\[|\]|#|$|=|-|/', line[4])

        for word in words:
            if word not in [None, '']:
                print(word.lower(),'\t', int(line[0]))
    except ValueError:  
        continue
