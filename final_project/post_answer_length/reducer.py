#!/usr/bin/python
import sys

old_id = None
length_question = 0
answers = []

for line in sys.stdin:
    current_id, body, node_type = line.replace('\n', '').split('\t')
    if old_id and old_id != current_id:
        if node_type == "question":
            length_question = len(body)
        else:
            answers.append(len(body))
        mean = 0 if len(answers) == 0 else sum(answers)/len(answers)
        print("{0}\t{1}\t{2}".format(old_id, length_question, mean))
        length_question = 0
        answers = []

    old_id = current_id
    if node_type == "question":
        length_question = len(body)
    else:
        answers.append(len(body))


if old_id:
    if node_type == "question":
        lenght_question = len(body)
    else:
        answers.append(len(body))
    mean = 0 if len(answers) == 0 else sum(answers)/len(answers)
    print('{0}\t{1}\t{2}'.format(old_id, length_question, mean))