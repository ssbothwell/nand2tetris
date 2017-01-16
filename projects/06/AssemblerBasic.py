#!/usr/bin/env python
import os, sys

file = open(sys.argv[1], 'r')
asmArray = []
for line in file:
    if not line.startswith('//') and line != '\n':
        asmArray.append(line.rstrip())

print(asmArray)
