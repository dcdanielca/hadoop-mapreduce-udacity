#! /usr/bin/python
import sys

old_answer = None
authors = []

for line in sys.stdin:
    current_answer, author = line.split('\t')
    if old_answer and old_answer != current_answer:
        print(int(old_answer.replace('"','')), authors)
        old_answer = current_answer
        authors =[]
    old_answer = current_answer
    authors.append(int(author.replace('\n','').replace('"','')))


