import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("A","A,<EOF>",101))
        self.assertTrue(TestLexer.test("a","a,<EOF>",102))
        self.assertTrue(TestLexer.test("AAAA","AAAA,<EOF>",103))
        self.assertTrue(TestLexer.test("aaaa","aaaa,<EOF>",104))
        self.assertTrue(TestLexer.test("Acbbdc","Acbbdc,<EOF>",105))
        self.assertTrue(TestLexer.test("aA","aA,<EOF>",106))
        self.assertTrue(TestLexer.test("1234aas45vn","1234,aas45vn,<EOF>",107))
        self.assertTrue(TestLexer.test("aas,uio","aas,,,uio,<EOF>",108))
        self.assertTrue(TestLexer.test("<=preOP","<=,preOP,<EOF>",109))
        self.assertTrue(TestLexer.test("< =9preOP","<,=,9,preOP,<EOF>",110))
        #self.assertTrue(TestLexer.test("'isn32''t'","'isn32''t',<EOF>",1001))
        
    #def test_integer(self):
        """test integers"""
        