#!/usr/bin/python
import sys

for line in sys.stdin:
    data = line.strip().split()
    if len(data) == 10:
        ip, identity, username, time, timezone, httpmethod, request, httpversion, status, size = data
        print(request.replace('http://www.the-associates.co.uk', ''))