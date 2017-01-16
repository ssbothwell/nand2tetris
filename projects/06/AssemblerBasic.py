#!/usr/bin/env python
import os, sys

file = open(sys.argv[1], 'r')
asmArray = []

# Load assembly file and iterate line by line
# removing all white space, comments, and linebreaks
# loading actual code into asmArray list.
for line in file:
    if line.rstrip() and not line.startswith('//'):
        asmArray.append(line.rstrip())

# A-instructions begin with `@` character
# C-instructions begin with an opcode, destcode
# jump code, or a semicolon


for index, instruction in enumerate(asmArray):
    # if it is an A-instruction then convert to a 16bit number
    if instruction.startswith('@'):
        asmArray[index] = ('{0:016b}'.format(int(instruction[1:])), 'A')
    else:
        asmArray[index] = (instruction, 'C')

print(asmArray)

