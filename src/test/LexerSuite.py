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
        
    def test_integer(self):
        """test integers"""
        self.assertTrue(TestLexer.test("001","001,<EOF>",111))
        self.assertTrue(TestLexer.test("001A","001,A,<EOF>",112))
    def test_real(self):
        """test reals"""
        self.assertTrue(TestLexer.test("001","001,<EOF>",113))
        self.assertTrue(TestLexer.test("1.2","1.2,<EOF>",114))
        self.assertTrue(TestLexer.test("1.","1.,<EOF>",115))
        self.assertTrue(TestLexer.test(".1",".1,<EOF>",116))
        self.assertTrue(TestLexer.test("1e2","1e2,<EOF>",117))
        self.assertTrue(TestLexer.test("1.2E-2","1.2E-2,<EOF>",118))
        self.assertTrue(TestLexer.test("1.2e-2","1.2e-2,<EOF>",119))
        self.assertTrue(TestLexer.test(".1E2",".1E2,<EOF>",120))
        self.assertTrue(TestLexer.test("9.0","9.0,<EOF>",121))
        self.assertTrue(TestLexer.test("12e8","12e8,<EOF>",122))
        self.assertTrue(TestLexer.test("0.33E-3","0.33E-3,<EOF>",123))
        self.assertTrue(TestLexer.test("128e-42","128e-42,<EOF>",124))