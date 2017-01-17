#!/usr/bin/env python
import os, sys

opCodes = { 
            '0':    '0101010',
            '1':    '0111111',
            '-1':   '0111010',
            'D':    '0001100',
            'A':    '0110000',
            'M':    '1110000',
            '!D':   '0001111',
            '!A':   '0110001',
            '!M':   '1110001',
            '-D':   '0001111',
            '-A':   '0110011',
            '-M':   '1110011',
            'D+1':  '0011111',
            'A+1':  '0110111',
            'M+1':  '1110111',
            'D-1':  '0001110',
            'A-1':  '0110010',
            'M-1':  '1110010',
            'D+A':  '0000010',
            'D+M':  '1000010',
            'D-A':  '0010011',
            'D-M':  '1010011',
            'A-D':  '0000111',
            'M-D':  '1000111',
            'D&A':  '0000000',
            'D&M':  '1000000',
            'D|A':  '0010101',
            'D|M':  '1010101',
        }

destCodes = {
                'null': '000',
                'M':    '001',
                'D':    '010',
                'MD':   '011',
                'A':    '100',
                'AM':   '101',
                'AD':   '110',
                'AMD':  '111',
            }

jumpCodes = {
                'null': '000',
                'JGT':  '001',
                'JEQ':  '010',
                'JGE':  '011',
                'JLT':  '100',
                'JNE':  '101',
                'JLE':  '110',
                'JMP':  '111',
            }

symbolTable =   { 
                'SP':      '0',
                'LCL':     '1',
                'ARG':     '2',
                'THIS':    '3',
                'THAT':    '4',
                'R0':      '0',
                'R1':      '1',
                'R2':      '2',
                'R3':      '3',
                'R4':      '4',
                'R5':      '5',
                'R6':      '6',
                'R7':      '7',
                'R8':      '8',
                'R9':      '9',
                'R10':     '10',
                'R11':     '11',
                'R12':     '12',
                'R13':     '13',
                'R14':     '14',
                'R15':     '15',
                'SCREEN':  '16384',
                'KBD':     '24576',
                }

def checkInstruction(instruction):
    """ Returns instruction type as a string (A, C, S) """
    if instruction.startswith('@'):
        return '{0:016b}'.format(int(instruction[1:]))
    elif instruction.startswith('('):
        return 'S'
    else:
        # Check for dest code, append if present or append null
        if '=' in instruction:
            dest = instruction.split('=', 1)[0]
        else:
            dest = 'null'

        # Check for op code and append 
        if '=' in instruction:
            op = instruction.split('=', 1)[1]
            if ';' in op:
                op = op.split(';', 1)[0]
        else:
            op = instruction.split(';', 1)[0]

        # Check for dest code and append
        if ';' in instruction:
            jump = instruction.split(';', 1)[1]
        else:
            jump = 'null'

        # return op, dest, jump values from dictionaries
        return '111' + opCodes[op] + destCodes[dest] + jumpCodes[jump]

def writeFile(array):
    """ Write an array to a file """
    name = sys.argv[1].split('.', 1)[0] + '.hack'
    hackFile = open(name, 'w')
    for line in asmArray:
        hackFile.write(line+'\n')

def removeWhiteSpace(string):
    """ Strip white space and comments from string """
    if string.rstrip() and not string.startswith('//'):
        return string

# Load assembly file
file = open(sys.argv[1], 'r')
# Copy assembly into a list and strip white space
asmArray = [ line.rstrip() for line in file if line.rstrip() and not line.startswith('//') ]
# Close file after copying to list
file.close()

# A-instructions: @value 
# C-instructions: dest = opcode;jump

# C-instructions can have either empty dest or jump codes.
# examples with binary translations:
# D=A       (dest = opcode)         1110110000010000
# D=A;JLT   (dest = opcode;jump)    1110110000010100
# A;JNE     (opcode;jump)           1110110000000101

# Map checkInstruction to asmArray to convert to binary
asmArray = [ checkInstruction(instruction) for instruction in asmArray ]
# write to a .hack file
writeFile(asmArray)
