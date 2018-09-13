import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):

    def test_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("a","a,<EOF>", 100))
        self.assertTrue(TestLexer.test("ab","ab,<EOF>", 101))
        self.assertTrue(TestLexer.test("aBc","aBc,<EOF>", 102))
        self.assertTrue(TestLexer.test("AbC","AbC,<EOF>", 103))

        self.assertTrue(TestLexer.test("a01","a01,<EOF>", 104))
        self.assertTrue(TestLexer.test("A1","A1,<EOF>", 105))
        self.assertTrue(TestLexer.test("a_","a_,<EOF>", 106))

        self.assertTrue(TestLexer.test("a_b","a_b,<EOF>", 107))
        self.assertTrue(TestLexer.test("a__","a__,<EOF>", 108))
        self.assertTrue(TestLexer.test("A_99", "A_99,<EOF>", 109))
        self.assertTrue(TestLexer.test("A_b_9_9", "A_b_9_9,<EOF>", 110))

        self.assertTrue(TestLexer.test("_aBc","_aBc,<EOF>", 111))
        self.assertTrue(TestLexer.test("__","__,<EOF>", 112))
        self.assertTrue(TestLexer.test("_0","_0,<EOF>", 113))
        self.assertTrue(TestLexer.test("_0A","_0A,<EOF>", 114))

        self.assertFalse(TestLexer.test("0x","0x,<EOF>", 115))
        self.assertFalse(TestLexer.test("-id","-id,<EOF>", 116))
        self.assertFalse(TestLexer.test("id.1","id.1,<EOF>", 117))
        self.assertFalse(TestLexer.test("id 2","id 2,<EOF>", 118))
        self.assertFalse(TestLexer.test("id-3","id-3,<EOF>", 119))

    def test_integer(self):
        """test integers"""
        self.assertTrue(TestLexer.test("1 2 3 4 5","1,2,3,4,5,<EOF>", 120))
        self.assertTrue(TestLexer.test("6 7 8 9 0","6,7,8,9,0,<EOF>", 121))
        self.assertTrue(TestLexer.test("12345","12345,<EOF>", 122))
        self.assertTrue(TestLexer.test("001","001,<EOF>", 123))
        self.assertTrue(TestLexer.test("123456789","123456789,<EOF>", 124))
        self.assertTrue(TestLexer.test("0","0,<EOF>", 125))

        self.assertFalse(TestLexer.test("-1", "-1,<EOF>", 126))
        self.assertFalse(TestLexer.test("+1", "+1,<EOF>", 127))

    def test_float(self):
        """test floats"""
        # Decimal
        self.assertTrue(TestLexer.test("1.1","1.1,<EOF>", 128))
        self.assertTrue(TestLexer.test("1.","1.,<EOF>", 129))
        self.assertTrue(TestLexer.test(".1",".1,<EOF>", 130))
        self.assertTrue(TestLexer.test("123.123","123.123,<EOF>", 131))
        self.assertTrue(TestLexer.test("1.0","1.0,<EOF>", 132))

        # Exponent
        self.assertTrue(TestLexer.test("133E1","133E1,<EOF>", 133))
        self.assertTrue(TestLexer.test("134e-1","134e-1,<EOF>", 134))
        self.assertTrue(TestLexer.test(".1E2",".1E2,<EOF>", 135))
        self.assertTrue(TestLexer.test(".1e-2",".1e-2,<EOF>", 136))
        self.assertTrue(TestLexer.test("10.E2","10.E2,<EOF>", 137))
        self.assertTrue(TestLexer.test("10.E-2","10.E-2,<EOF>", 138))
        self.assertTrue(TestLexer.test("1e2","1e2,<EOF>", 139))
        self.assertTrue(TestLexer.test("1e-2","1e-2,<EOF>", 140))

        # False
        self.assertFalse(TestLexer.test("e-12", "e-12,<EOF>", 141))
        self.assertFalse(TestLexer.test("e+12", "e+12,<EOF>", 142))

        self.assertFalse(TestLexer.test("12e", "12e,<EOF>", 143))
        self.assertFalse(TestLexer.test("+12e", "+12e,<EOF>", 144))

        self.assertFalse(TestLexer.test("+e2", "+e2,<EOF>", 145))
        self.assertFalse(TestLexer.test("-e2", "-e2,<EOF>", 146))
        self.assertFalse(TestLexer.test(".e2", ".e2,<EOF>", 147))

        self.assertFalse(TestLexer.test("1.1.1", "1.1.1,<EOF>", 148))
        self.assertFalse(TestLexer.test(".1.1", ".1.1,<EOF>", 149))
        self.assertFalse(TestLexer.test("1.1.1e1", "1.1.1e1,<EOF>", 150))
        self.assertFalse(TestLexer.test("1e1.1", "1e1.1,<EOF>", 151))

    def test_string(self):
        """test strings"""
        # Legal strings
        self.assertTrue(TestLexer.test('"---"', "---,<EOF>", 152))
        self.assertTrue(TestLexer.test('"  ---"', "  ---,<EOF>", 153))
        self.assertTrue(TestLexer.test('"---  "', "---  ,<EOF>", 154))
        self.assertTrue(TestLexer.test('"--- ---"', "--- ---,<EOF>", 155))
        self.assertTrue(TestLexer.test('"  --  "', "  --  ,<EOF>", 156))
        self.assertTrue(TestLexer.test('" - - "', " - - ,<EOF>", 157))
        self.assertTrue(TestLexer.test(r'"^@%#./"', r"^@%#./,<EOF>", 158))
        self.assertTrue(TestLexer.test('":))"', ":)),<EOF>", 159))
        self.assertTrue(TestLexer.test('""', ",<EOF>", 160))

        # Legal escapes
        self.assertTrue(TestLexer.test(r'"\b \f \r \n"', r'\b \f \r \n,<EOF>', 161))
        self.assertTrue(TestLexer.test(r'"\t--\'--\"--\\" ', r'\t--\'--\"--\\,<EOF>', 162))
        self.assertTrue(TestLexer.test(r'"-\"db quote\"-\t"', r'-\"db quote\"-\t,<EOF>', 163))
        self.assertTrue(TestLexer.test(r'"-\'sg quote\'-\t"', r'-\'sg quote\'-\t,<EOF>', 164))

        # Unclosed strings
        self.assertFalse(TestLexer.test('"---', "---,<EOF>", 165))
        self.assertFalse(TestLexer.test('"---\n"', "---,<EOF>", 166))
        self.assertFalse(TestLexer.test('"---\r\n"', "---\r\n,<EOF>", 167))

        # Illegal escapes
        self.assertFalse(TestLexer.test(r'"---\---"', r'---\---,<EOF>', 168))
        self.assertFalse(TestLexer.test(r'"---\---"', r'------,<EOF>', 169))
        self.assertFalse(TestLexer.test(r'"---\u---"', r'---\u---,<EOF>', 170))
        self.assertFalse(TestLexer.test(r'"---\u---"', r'---u---,<EOF>', 171))
        self.assertFalse(TestLexer.test(r'"---\ ---"', r'---\ ---,<EOF>', 172))
        self.assertFalse(TestLexer.test(r'"---\ ---"', r'--- ---,<EOF>', 173))
        self.assertFalse(TestLexer.test(r'"---\a"', r'---\a,<EOF>', 174))
        self.assertFalse(TestLexer.test(r'"---\a"', r'---a,<EOF>', 175))

    def test_keyword(self):
        """test keywords"""
        self.assertTrue(TestLexer.test("break continue for to downto do", "break,continue,for,to,downto,do,<EOF>", 176))
        self.assertTrue(TestLexer.test("if then else return while begin", "if,then,else,return,while,begin,<EOF>", 177))
        self.assertTrue(TestLexer.test("function procedure var true", "function,procedure,var,true,<EOF>", 178))
        self.assertTrue(TestLexer.test("false array of real boolean", "false,array,of,real,boolean,<EOF>", 179))
        self.assertTrue(TestLexer.test("integer string not and or div mod", "integer,string,not,and,or,div,mod,<EOF>", 180))

    def test_operator(self):
        """test operators"""
        self.assertTrue(TestLexer.test("<>", "<>,<EOF>", 181))
        self.assertTrue(TestLexer.test("< >", "<,>,<EOF>", 182))
        self.assertTrue(TestLexer.test(":=", ":=,<EOF>", 183))
        self.assertTrue(TestLexer.test(": =", ":,=,<EOF>", 184))
        self.assertTrue(TestLexer.test("<=", "<=,<EOF>", 185))
        self.assertTrue(TestLexer.test(">=", ">=,<EOF>", 186))
        self.assertTrue(TestLexer.test("..", "..,<EOF>", 187))

    def test_white_space(self):
        self.assertTrue(TestLexer.test(" ", "<EOF>", 188))
        self.assertTrue(TestLexer.test("  ", "<EOF>", 189))
        self.assertTrue(TestLexer.test("\n", "<EOF>", 190))
        self.assertTrue(TestLexer.test("\t", "<EOF>", 191))
        self.assertTrue(TestLexer.test("\r\n", "<EOF>", 192))
        self.assertTrue(TestLexer.test("\t\r\n", "<EOF>", 193))


    def test_mixed_tokens(self):
        self.assertTrue(TestLexer.test("1-2", "1,-,2,<EOF>", 194))
        self.assertTrue(TestLexer.test("e-2", "e,-,2,<EOF>", 195))
        self.assertTrue(TestLexer.test("2e", "2,e,<EOF>", 196))
        self.assertTrue(TestLexer.test("2*3", "2,*,3,<EOF>", 197))
        self.assertTrue(TestLexer.test("a[2]", "a,[,2,],<EOF>", 198))
        self.assertTrue(TestLexer.test("a>=2", "a,>=,2,<EOF>", 199))