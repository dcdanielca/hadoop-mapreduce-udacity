#!/usr/bin/python
import sys
import csv

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    for line in reader:
        if len(line) == 19:
            newLine = [line[3], "B"] + line
            writer.writerow(newLine)
            print()
		#if forum_users data
        elif len(line) == 5:
            newLine = [line[0], "A"] + line[1:]
            writer.writerow(newLine)
            

mapper()
        