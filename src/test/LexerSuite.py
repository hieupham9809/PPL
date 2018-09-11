import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def Atest_identifier(self):
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
        # add more tests with _
    def Atest_integer(self):
        """test integers"""
        self.assertTrue(TestLexer.test("001","001,<EOF>",111))
        self.assertTrue(TestLexer.test("001A","001,A,<EOF>",112))
    def Atest_real(self):
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
    def Atest_comment(self):
        """test comments"""
        self.assertTrue(TestLexer.test("//123","<EOF>",125))
        self.assertTrue(TestLexer.test("//(*abc*)","<EOF>",126))
        self.assertTrue(TestLexer.test("//\{abc\}","<EOF>",127))
        self.assertTrue(TestLexer.test("//(*abc","<EOF>",128))
        # add more

    def test_string(self):
        """test strings"""
        #self.assertTrue(TestLexer.test("\"abc\"","abc,<EOF>",135))
        #self.assertTrue(TestLexer.test("\"abc\\nabc\"","abc\\nabc,<EOF>",136))
        self.assertTrue(TestLexer.test("\"abc\\aabc","Illegal Escape In String: abc\\a",137))
        #self.assertTrue(TestLexer.test("\"abc\\nabc\"","abc\\nabc,<EOF>",138))
        #self.assertTrue(TestLexer.test("""abc""","abc,<EOF>",139))
        self.assertTrue(TestLexer.test("""a$bc""","a$bc,<EOF>",140))

    def Atest_array(self):
        """test array"""
        #self.assertTrue(TestLexer.test("array [ 1 .. 5 ] of integer","abc\\nabc\",<EOF>",150))
        #self.assertTrue(TestLexer.test("var d:array [ 1 .. 5  of integer","abc\\nabc\",<EOF>",151))
        self.assertTrue(TestLexer.test("var d:array [1..5] of integer;","var,d,:,array,[,1.,.5,],of,integer,;,<EOF>",152))
    def Atest_unclosed_string(self):
        """unclosed sring"""
        self.assertTrue(TestLexer.test("\"var d:array [1..5] of integer;","Unclosed String: var d:array [1..5] of integer;",153))
        self.assertTrue(TestLexer.test("\"var d:array [1..5] \n of integer;","Unclosed String: var d:array [1..5] of integer;",154))
    def Atest_simple_program(self):
        self.assertTrue(TestLexer.test("int main() {}","<EOF>",155))