#!/usr/bin/env python
import unittest
from assemblerFunctions import *


class testCheckPattern(unittest.TestCase):
    def setUp(self):
        pass

    def test_a_instruction(self):
        """ Should return a single element tuple """
        aRegex = '@([0-9]+)'
        aString = '@42'
        self.assertEqual(checkPattern(aString,aRegex), ('42',))

    def test_c_instruction(self):
        """ Should return a three element tuple """
        cRegex = '(?:([AMD]{1,3})=)?([AMD01\-+!&|]{1,3})(?:;([JGTEQLNMP]{3}))?'
        cString = 'D=D+M;JGT'
        self.assertEqual(checkPattern(cString,cRegex), ('D', 'D+M', 'JGT'))


class testCounter(unittest.TestCase):
    def setUp(self):
        self.symbolCounter = counter()
        self.symbolCounter['increment']()

    def test_counterIncrement(self):
        """ Should increment counter 2 two and return """
        self.assertEqual(self.symbolCounter['increment'](), 2)

    def test_counterPrints(self):
        """ Should print counter value without incrementing """
        self.assertEqual(self.symbolCounter['printVal'](), 1)


class testCheckLabels(unittest.TestCase):
    def setUp(self):
        self.symbolTable = {'foo': 1}

    def test_AddedSymbolToDict(self):
        """ Should add new symbol to dict """
        checkLabel('(baz)', 2, self.symbolTable)
        self.assertIs(self.symbolTable['baz'], 2)

class testCheckVariables(unittest.TestCase):
    def setUp(self):
        self.symbolTable = {'foo': 16, 'bar': 17}

    def test_VariableInDict(self):
        """ Should return address location from symbolTable """
        """ prepended with `@` """
        self.assertEqual(checkVariables('@foo', self.symbolTable), '@16')

    def test_VariableUpdatDict(self):
        """ Should add variable to symbolTable """
        checkVariables('@baz', self.symbolTable)
        self.assertIn('baz', self.symbolTable)

    def test_VariableReturnNewVariable(self):
        """ Should return address of variable """
        self.assertEqual(checkVariables('@baz', self.symbolTable), '@18')


class testCheckInstruction(unittest.TestCase):
    def setUp(self):
        self.opCodes = {'D':'0001100'}
        self.destCodes = {'MD':   '011'}
        self.jumpCodes = {'JGT':  '001'}

    def test_checkAInstruction(self):
        """ Should return 16 bit binary number """
        self.assertEqual(checkInstruction('@7', self.opCodes, self.destCodes, self.jumpCodes), '0000000000000111') 

    def test_checkCInstruction(self):
        """ Should return binary translation """
        self.assertEqual(checkInstruction('MD=D;JGT', self.destCodes, self.opCodes, self.jumpCodes), '1110001100011001')


if __name__ == '__main__':
    unittest.main()
