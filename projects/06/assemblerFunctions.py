#!/bin/bin/env python
import os, sys, re

def checkPattern(string, pattern):
    """ Regex pattern checker abstraction """
    regexPattern = re.compile(pattern)
    result = regexPattern.search(string)

    if result:
        return result.groups()
    else:
        return

def counter():
    """ A closure for tracking labels """
    foo = {'bar': 0}
    def increment():
        foo['bar'] += 1
        return foo['bar']

    def printVal():
        return foo['bar']

    return { 'increment': increment, 'printVal': printVal }

symbolCounter = counter()

def checkLabel(instruction, index, table):
    """ Add labels to symbolTable referencing their index"""
    labelTable = table

    # Match label symbols
    labelRegex = '\(([a-zA-Z0-9_.$:]+)\)'
    labelResult = checkPattern(instruction, labelRegex)
    if labelResult:
        if labelResult[0] not in labelTable:
            labelTable[labelResult[0]] = index - symbolCounter['printVal']()
            symbolCounter['increment']()
    else:
        return instruction

def checkVariables(instruction, symbolTable, labelTable):
    """ If symbols then add them to the symbol table """
    """ and replace in instruction with memory location """

    symbolTable = symbolTable
    lableTable = labelTable

    # Match A-Instruction symbols
    variableRegex = '@([a-zA-Z_:.$][\w\d:.$]+)'
    variableResult = checkPattern(instruction, variableRegex)

    if variableResult:
        if variableResult[0] in labelTable:
            return '@' + str(labelTable[variableResult[0]])

        elif variableResult[0] in symbolTable: 
            return '@' + str(symbolTable[variableResult[0]])

        elif variableResult[0] not in symbolTable and variableResult not in labelTable:
            variableKey = max([ val for key, val in symbolTable.items() if val < 16384]) + 1
            symbolTable[variableResult[0]] = variableKey
            return '@' + str(symbolTable[variableResult[0]])

    else:
        return instruction

def checkInstruction(instruction, dest, op, jump):
    """ Convert instruction to binary """

    opCodes = op
    destCodes = dest
    jumpCodes = jump

    # Match instructions with no symbols
    aRegex = '@([0-9]+)'
    aResult = checkPattern(instruction, aRegex)
    cRegex = '(?:([AMD]{1,3})=)?([AMD01\-+!&|]{1,3})(?:;([JGTEQLNMP]{3}))?'
    cResult= checkPattern(instruction, cRegex)

    if aResult:
        # @1234
        return '{0:016b}'.format(int(aResult[0]))
    elif cResult:
        # dest=op;jump
        # Check for dest code, append if present or append null
        if cResult[0]:
            dest = cResult[0]
        else:
            dest = 'null'

        # Check for op code and append 
        if cResult[1]:
            op = cResult[1]

        # Check for dest code and append
        if cResult[2]:
            jump = cResult[2]
        else:
            jump = 'null'

        # return op, dest, jump values from dictionaries
        return '111' + opCodes[op] + destCodes[dest] + jumpCodes[jump]
    else:
        return

def writeFile(array):
    """ Write an array to a file """
    name = sys.argv[1].split('.', 1)[0] + '.hack'
    hackFile = open(name, 'w')
    for line in array:
        hackFile.write(line+'\n')
