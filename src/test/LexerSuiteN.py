import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    # ID
    def test_simple_ID(self):
        self.assertTrue(TestLexer.test("abc","abc,<EOF>",100))
    def test_case_ID(self):
        self.assertTrue(TestLexer.test("aCBbdc","aCBbdc,<EOF>",101))
    def test_ambigous_ID(self):
        self.assertTrue(TestLexer.test("5a7","5,a7,<EOF>",102))
    def test_ID_with_line_feed_between(self):
        self.assertTrue(TestLexer.test("abc\nbca","abc,bca,<EOF>",103))
    def test_ID_with_tab_between(self):
        self.assertTrue(TestLexer.test("abc\tbca","abc,bca,<EOF>",104))
    def test_ID_with_error_token_between(self):
        self.assertTrue(TestLexer.test("abc\wbca","abc,Error Token \\",105))

    # Program
    def test_assign_5_into_dash(self):
        self.assertTrue(TestLexer.test("_=5","_,=,5,<EOF>",106))
    def test_C_var_declare(self):
        self.assertTrue(TestLexer.test("int a=5","int,a,=,5,<EOF>",107))
    def test_MP_var_declare(self):
        self.assertTrue(TestLexer.test("var i:integer;","var,i,:,integer,;,<EOF>",108))
    def test_import_CRT_library(self):
        self.assertTrue(TestLexer.test("uses crt;","uses,crt,;,<EOF>",109))
    def test_simple_Pascal_program(self):
        self.assertTrue(TestLexer.test("uses crt;\nvar i:integer;\n\tst:string;\nbegin\n\tclrscr;\n\tst=\"abcx\\tyz\";\n\twriteln(st);\nend","uses,crt,;,var,i,:,integer,;,st,:,string,;,begin,clrscr,;,st,=,abcx\\tyz,;,writeln,(,st,),;,end,<EOF>",110))
    def test_unicode_character(self):
        self.assertTrue(TestLexer.test(str("var ◙=5;".encode("utf-8")),"b,Error Token '",111))
    def test_simple_MP_program(self):
        input = 'procedure foo (a,b:integer;c:real);\nvar x,y:real;\nbegin\n\t//abcxyz\n\tx=6;\n\ty=9*x+10000/3;\nend'
        self.assertTrue(TestLexer.test(input,"procedure,foo,(,a,,,b,:,integer,;,c,:,real,),;,var,x,,,y,:,real,;,begin,x,=,6,;,y,=,9,*,x,+,10000,/,3,;,end,<EOF>",112))
    def test_error_character_in_comment(self):
        self.assertTrue(TestLexer.test("3=5=r=10;{aAs\a\b\c\d\e\f\g\h\i\j\k\l\m\\q'N}i=5;","3,=,5,=,r,=,10,;,i,=,5,;,<EOF>",113))
    def test_dash_and_add_operator_between_IDs(self):
        self.assertTrue(TestLexer.test("askjdh_3497jasd+kjd","askjdh_3497jasd,+,kjd,<EOF>",114))
    def test_another_simple_MP_program(self):
        self.assertTrue(TestLexer.test("""
            pROCEDURE foo(c: real) ;
                BEGIN
                   a:=not b;
                END
            """ , "pROCEDURE,foo,(,c,:,real,),;,BEGIN,a,:=,not,b,;,END,<EOF>",115))
    def test_import_antlr4(self):
        self.assertTrue(TestLexer.test("import antlr4","import,antlr4,<EOF>",116))
    def test_built_in_procedure(self):
        self.assertTrue(TestLexer.test("procedure putIntLn(i:integer);","procedure,putIntLn,(,i,:,integer,),;,<EOF>",117))
    def test_return(self):
        self.assertTrue(TestLexer.test("return 5;","return,5,;,<EOF>",118))

    # Keyword
    def test_break_continue_for_to(self):
        self.assertTrue(TestLexer.test("break continue for to","break,continue,for,to,<EOF>",119))
    def test_downto_do_if_then_else(self):
        self.assertTrue(TestLexer.test("downto do if then else","downto,do,if,then,else,<EOF>",120))
    def test_else_return_while_begin(self):
        self.assertTrue(TestLexer.test("else return while begin","else,return,while,begin,<EOF>",121))
    def test_var_true_false_array_of(self):
        self.assertTrue(TestLexer.test("var true false array of ","var,true,false,array,of,<EOF>",122))
    def test_real_boolean_integer_string(self):
        self.assertTrue(TestLexer.test("real boolean integer string ","real,boolean,integer,string,<EOF>",123))
    def test_end_function_procedure(self):
        self.assertTrue(TestLexer.test("end function procedure ","end,function,procedure,<EOF>",124))
    def test_keyword_operator(self):
        self.assertTrue(TestLexer.test("not and or div mod ","not,and,or,div,mod,<EOF>",125))
    def test_symbol_operator(self):
        self.assertTrue(TestLexer.test("+-*/ <> = < > <= >= div","+,-,*,/,<>,=,<,>,<=,>=,div,<EOF>",126))
    def test_separator(self):
        self.assertTrue(TestLexer.test("[]();:..,","[,],(,),;,:,..,,,<EOF>",127))

    # String Literal
    def test_null_string_with_line_feed_both_side(self):
        self.assertTrue(TestLexer.test("\n\"\"\n",",<EOF>",128))
    def test_standard_string(self):
        self.assertTrue(TestLexer.test("  \"abc\"  ","abc,<EOF>",129))
    def test_standard_string_in_another_way(self):
        self.assertTrue(TestLexer.test('  "abc"  ',"abc,<EOF>",130))
    def test_standard_string_with_line_feed_right_side(self):
        self.assertTrue(TestLexer.test("  \"abc\"\n","abc,<EOF>",131))
    def test_standard_string_with_line_feed_left_side(self):
        self.assertTrue(TestLexer.test("\n\"abc\"  ","abc,<EOF>",132))
    def test_standard_string_with_line_feed_both_side(self):
        self.assertTrue(TestLexer.test("\n\"abc\"\n","abc,<EOF>",133))
    def test_standard_string_with_carriage_return_both_side(self):
        self.assertTrue(TestLexer.test("\r\"abc\"\r","abc,<EOF>",134))
    def test_standard_string_with_tab_both_side(self):
        self.assertTrue(TestLexer.test("\t\"abc\"\t","abc,<EOF>",135))
    def test_standard_string_with_form_feed_both_side(self):
        self.assertTrue(TestLexer.test("\f\"abc\"\f","abc,<EOF>",136))
    def test_standard_string_with_backspace_both_side(self):
        self.assertTrue(TestLexer.test("\b\"abc\"\b","Error Token ",137))
    def test_unclose_string(self):
        self.assertTrue(TestLexer.test("\"abc","Unclosed String: abc",138))

    def test_string_with_backslash_inside(self):
        self.assertTrue(TestLexer.test("\"abc\\nxyz\"","abc\\nxyz,<EOF>",139))
    def test_string_with_line_feed_inside(self):
        self.assertTrue(TestLexer.test("\"abc\nxyz\"","Unclosed String: abc",140))
    def test_unclose_string_with_line_feed_inside(self):
        self.assertTrue(TestLexer.test("\"abc\nxyz","Unclosed String: abc",141))
    def test_string_with_carriage_return_inside(self):
        self.assertTrue(TestLexer.test("\"abc\rxyz\"","Unclosed String: abc",142))
    def test_string_with_tab_inside(self):
        self.assertTrue(TestLexer.test("\"abc\txyz\"","Illegal Escape In String: abc\t",143))
    def test_string_with_form_feed_inside(self):
        self.assertTrue(TestLexer.test("\"abc\fxyz\"","Illegal Escape In String: abc\f",144))
    def test_string_with_backspace_inside(self):
        self.assertTrue(TestLexer.test("\"abc\bxyz\"","Illegal Escape In String: abc\b",145))
    def test_string_with_error_character_inside(self):
        self.assertTrue(TestLexer.test("\"abc\axyz\"","abcxyz,<EOF>",146))
    def test_nest_string(self):
        self.assertTrue(TestLexer.test("\"abc\\\"x\\\"yz\"uvt","abc\\\"x\\\"yz,uvt,<EOF>",147))
    def test_unclose_string_with_backslash_doublequote(self):
        self.assertTrue(TestLexer.test("\"abc\\\"xyz","Unclosed String: abc\\\"xyz",148))
    def test_unclose_string_missing_opening(self):
        self.assertTrue(TestLexer.test("abc\rxyz\"","abc,xyz,Unclosed String: ",149))
    def test_string_with_quote_inside(self):
        self.assertTrue(TestLexer.test("\"abc'xyz\"","Illegal Escape In String: abc'",150))
    def test_string_with_double_quote_inside(self):
        self.assertTrue(TestLexer.test("\"abc\"xyz\"","abc,xyz,Unclosed String: ",151))


    def test_using_line_feed_in_string(self):
        self.assertTrue(TestLexer.test("\"abc\\nxyz\"","abc\\nxyz,<EOF>",152))
    def test_using_carriage_return_in_string(self):
        self.assertTrue(TestLexer.test("\"abc\\rxyz\"","abc\\rxyz,<EOF>",153))
    def test_using_tab_in_string(self):
        self.assertTrue(TestLexer.test("\"abc\\txyz\"","abc\\txyz,<EOF>",154))
    def test_using_form_feed_in_string(self):
        self.assertTrue(TestLexer.test("\"abc\\fxyz\"","abc\\fxyz,<EOF>",155))
    def test_using_backspace_in_string(self):
        self.assertTrue(TestLexer.test("\"abc\\bxyz\"","abc\\bxyz,<EOF>",156))
    def test_using_quote_in_string(self):
        self.assertTrue(TestLexer.test("\"abc\\'xyz\"","abc\\'xyz,<EOF>",157))
    def test_using_doublequote_in_string(self):
        self.assertTrue(TestLexer.test("\"abc\\\"xyz\"","abc\\\"xyz,<EOF>",158))
    def test_using_a_random_character_in_string(self):
        self.assertTrue(TestLexer.test("\"abc\\wxyz\"","Illegal Escape In String: abc\\w",159))
    def test_using_another_random_character_in_string(self):
        self.assertTrue(TestLexer.test("\"abc\\axyz\"","Illegal Escape In String: abc\\a",160))
    def test_using_back_slash_in_string(self):
        self.assertTrue(TestLexer.test("\"\\\\abc\"","\\\\abc,<EOF>",161))

    # Comment
    def test_line_comment_to_EOF(self):
        self.assertTrue(TestLexer.test("testcomment//trutiliqtrlkdtt","testcomment,<EOF>",162))
    def test_block_comment(self):
        self.assertTrue(TestLexer.test("abc{wewe}ewe","abc,ewe,<EOF>",163))
    def test_block_comment_missing_close(self):
        self.assertTrue(TestLexer.test("abc{weeawa","abc,Error Token {",164))
    def test_block_comment_missing_open(self):
        self.assertTrue(TestLexer.test("abc}wekjasd","abc,Error Token }",165))
    def test_traditional_block_comment(self):
        self.assertTrue(TestLexer.test("abc(*wekhjsadasd*)","abc,<EOF>",166))
    def test_traditional_block_comment_missing_close(self):
        self.assertTrue(TestLexer.test("abc(*wekhjsadasd","abc,(,*,wekhjsadasd,<EOF>",167))
    def test_traditional_block_comment_missing_open(self):
        self.assertTrue(TestLexer.test("abcwekhjsadasd*)","abcwekhjsadasd,*,),<EOF>",168))

    # Integer Literal
    def test_digit_integer(self):
        self.assertTrue(TestLexer.test("1","1,<EOF>",169))
    def test_C_octa_integer(self):
        self.assertTrue(TestLexer.test("01","01,<EOF>",170))
    def test_binary_integer(self):
        self.assertTrue(TestLexer.test("0101","0101,<EOF>",171))
    def test_very_long_integer(self):
        self.assertTrue(TestLexer.test("2186541879610987968089679","2186541879610987968089679,<EOF>",172))
    def test_integer_add_string(self):
        self.assertTrue(TestLexer.test("230654894619+\"abc\"","230654894619,+,abc,<EOF>",173))
    
    # Real Literal
    def test_real_literal_with_whole_number_part_and_fractional_part(self):
        self.assertTrue(TestLexer.test("1.1","1.1,<EOF>",174))
    def test_real_literal_with_only_whole_number_part(self):
        self.assertTrue(TestLexer.test("1.","1.,<EOF>",175))
    def test_real_literal_with_only_fractional_part(self):
        self.assertTrue(TestLexer.test(".1",".1,<EOF>",176))
    def test_standard_real_literal(self):
        self.assertTrue(TestLexer.test("1.3E4","1.3E4,<EOF>",177))
    def test_real_literal_with_negation_before_and_negation_after_e(self):
        self.assertTrue(TestLexer.test("-.3E-9","-,.3E-9,<EOF>",178))
    def test_real_literal_with_only_exponent_part(self):
        self.assertTrue(TestLexer.test("E5","E5,<EOF>",179))
    def test_real_literal_without_digit_in_exponent_part(self):
        self.assertTrue(TestLexer.test("1.4e","1.4,e,<EOF>",180))
    def test_another_real_literal_without_digit_in_exponent_part(self):
        self.assertTrue(TestLexer.test("-8.e","-,8.,e,<EOF>",181))
    def test_real_literal_inside_exponent_part_of_real_literal(self):
        self.assertTrue(TestLexer.test("1.2e0.5","1.2e0,.5,<EOF>",182))

    # Boolean Literal
    def test_sign_a_into_true(self):
        self.assertTrue(TestLexer.test("true:=a","true,:=,a,<EOF>",183))
    def test_sign_false_into_b(self):
        self.assertTrue(TestLexer.test("b:=false","b,:=,false,<EOF>",184))
    def test_sign_not_false_into_true(self):
        self.assertTrue(TestLexer.test("true:= not false","true,:=,not,false,<EOF>",185))

    # Array Type
    def test_standard_index_expression(self):
        self.assertTrue(TestLexer.test("a[4]","a,[,4,],<EOF>",186))
    def test_a_more_complex_index_expression(self):
        self.assertTrue(TestLexer.test("1[1]","1,[,1,],<EOF>",187))
    def test_the_most_complex_index_expression_with_assign_statement(self):
        self.assertTrue(TestLexer.test("1[1]=1","1,[,1,],=,1,<EOF>",188))

    # Boolean Expression
    def test_a_simple_boolean_expression(self):
        self.assertTrue(TestLexer.test("a+b>4","a,+,b,>,4,<EOF>",189))
    def test_another_simple_boolean_expression(self):
        self.assertTrue(TestLexer.test("false < true ","false,<,true,<EOF>",190))
    def test_a_more_complex_boolean_expression(self):
        self.assertTrue(TestLexer.test("__a__ __add__ __b__ __eq__ __c__","__a__,__add__,__b__,__eq__,__c__,<EOF>",191))

    # Error Token
    def test_token_quote_in_program(self):
        self.assertTrue(TestLexer.test("a'sVN","a,Error Token '",192))
    def test_backslash_and_a_character_in_program(self):
        self.assertTrue(TestLexer.test("\a","Error Token \a",193))
    def test_comment_without_closing_in_program(self):
        self.assertTrue(TestLexer.test("ab//c{ad\ns}","ab,s,Error Token }",194))
    def test_exclamation_mark_in_program(self):
        self.assertTrue(TestLexer.test("!@#","Error Token !",195))
    def test_dot_in_program(self):
        self.assertTrue(TestLexer.test(".","Error Token .",196))
    def test_at_sign_in_program(self):
        self.assertTrue(TestLexer.test("@","Error Token @",197))
    def test_real_literal_without_digit_before_exponent_part(self):
        self.assertTrue(TestLexer.test(".e2","Error Token .",198))
    def test_percent_sign_in_program(self):
        self.assertTrue(TestLexer.test("%","Error Token %",199))