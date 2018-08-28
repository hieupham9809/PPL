import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("abc","abc,<EOF>",101))
        self.assertTrue(TestLexer.test("aCBbdc","aCBbdc,<EOF>",102))
        self.assertTrue(TestLexer.test("aAsVN","aAsVN,<EOF>",103))
        self.assertTrue(TestLexer.test("1.0","1.0,<EOF>",1001))
    def test_integer(self):
        """test integers"""
        self.assertTrue(TestLexer.test("1.0e-1","1.0e-1,<EOF>",104))