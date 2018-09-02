import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("a","a,<EOF>",101))
        self.assertTrue(TestLexer.test("Acbbdc","A,cbbdc,<EOF>",102))
        self.assertTrue(TestLexer.test("aas uio","aasuio,<EOF>",103))
        self.assertTrue(TestLexer.test("1234aas45vn","1234,aas45vn,<EOF>",105))
        self.assertTrue(TestLexer.test("'isn32''t'","'isn32''t',<EOF>",1001))
    def test_integer(self):
        """test integers"""
        self.assertTrue(TestLexer.test("1.0e-1","1.0e-1,<EOF>",104))