#!/usr/bin/python
import sys

old_word = None
indexes = []

for line in sys.stdin:
    current_word, id = line.split('\t')
    if old_word and old_word != current_word:
        print('{0}\t{1}\t{2}'.format(old_word, sorted(indexes), len(indexes)))
        old_word = current_word
        indexes = []
    old_word = current_word
    indexes.append(int(id))

if old_word:
    print('{0}\t{1}\t{2}'.format(old_word, sorted(indexes), len(indexes)))
