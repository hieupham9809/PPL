import unittest
from TestUtils import TestParser

success = "successful"

def error(line, col, token):
    return "Error on line {} col {}: {}".format(line, col, token)

def simple_program(statements):
    return "procedure main();begin\n{}\nend\n".format(statements)
    
def format_input(input_str):
    lines = ""
    for line in input_str.split("\n"):
        lines += line.strip() + "\n"
    return lines

class ParserSuite(unittest.TestCase):
    '''
'########:'##:::'##:'########::'########:
... ##..::. ##:'##:: ##.... ##: ##.....::
::: ##:::::. ####::: ##:::: ##: ##:::::::
::: ##::::::. ##:::: ########:: ######:::
::: ##::::::: ##:::: ##.....::: ##...::::
::: ##::::::: ##:::: ##:::::::: ##:::::::
::: ##::::::: ##:::: ##:::::::: ########:
:::..::::::::..:::::..:::::::::........::
'''
    def test_type_primitive_integer(self):
        input = "var x: integer;"
        self.assertTrue(TestParser.test(input, success, 200))

    def test_type_primitive_boolean(self):
        input = "var x: boolean;"
        self.assertTrue(TestParser.test(input, success, 201))

    def test_type_primitive_real(self):
        input = "var x: real;"
        self.assertTrue(TestParser.test(input, success, 202))

    def test_type_primitive_string(self):
        input = "var x: string;"
        self.assertTrue(TestParser.test(input, success, 203))

    def test_type_error_primitive_type(self):
        input = "var x: char;"
        self.assertTrue(TestParser.test(input, error(1, 7, "char"), 204))

    def test_type_array(self):
        input = "var x: array [1 .. 2] of real;"
        self.assertTrue(TestParser.test(input, success, 205))

    def test_type_array_negative_index_left(self):
        input = "var x: array [-1 .. 2] of real;"
        self.assertTrue(TestParser.test(input, success, 206))

    def test_type_array_negative_index_right(self):
        input = "var x: array [1 .. -2] of real;"
        self.assertTrue(TestParser.test(input, success, 207))

    def test_type_array_negative_index_both(self):
        input = "var x: array [-1 .. -2] of real;"
        self.assertTrue(TestParser.test(input, success, 208))

    '''
'##::::'##::::'###::::'########:::::'########::'########::'######::'##::::::::::'###::::'########::'########:
 ##:::: ##:::'## ##::: ##.... ##:::: ##.... ##: ##.....::'##... ##: ##:::::::::'## ##::: ##.... ##: ##.....::
 ##:::: ##::'##:. ##:: ##:::: ##:::: ##:::: ##: ##::::::: ##:::..:: ##::::::::'##:. ##:: ##:::: ##: ##:::::::
 ##:::: ##:'##:::. ##: ########::::: ##:::: ##: ######::: ##::::::: ##:::::::'##:::. ##: ########:: ######:::
. ##:: ##:: #########: ##.. ##:::::: ##:::: ##: ##...:::: ##::::::: ##::::::: #########: ##.. ##::: ##...::::
:. ## ##::: ##.... ##: ##::. ##::::: ##:::: ##: ##::::::: ##::: ##: ##::::::: ##.... ##: ##::. ##:: ##:::::::
::. ###:::: ##:::: ##: ##:::. ##:::: ########:: ########:. ######:: ########: ##:::: ##: ##:::. ##: ########:
:::...:::::..:::::..::..:::::..:::::........:::........:::......:::........::..:::::..::..:::::..::........::
'''
    def test_var_declare_simple(self):
        input = "var a: integer;"
        self.assertTrue(TestParser.test(input, success, 209))

    def test_var_declare_array(self):
        input = "var a: array [1 .. 2] of string;"
        self.assertTrue(TestParser.test(input, success, 210))

    def test_var_declare_many_var(self):
        input = "var a, b, c: real;"
        self.assertTrue(TestParser.test(input, success, 211))

    def test_var_declare_many_declare(self):
        input = "var a, b, c: real; c, d: integer; f: boolean;"
        self.assertTrue(TestParser.test(input, success, 212))

    def test_var_declare_missing_semi(self):
        input = "var a: real"
        self.assertTrue(TestParser.test(input, error(1, 11, "<EOF>"), 213))

    def test_var_declare_missing_type(self):
        input = "var a: ;"
        self.assertTrue(TestParser.test(input, error(1, 7, ";"), 214))

    def test_var_declare_missing_id_1(self):
        input = "var : real;"
        self.assertTrue(TestParser.test(input, error(1, 4, ":"), 215))

    def test_var_declare_missing_id_2(self):
        input = "var a, :real;"
        self.assertTrue(TestParser.test(input, error(1, 7, ":"), 216))

    def test_var_declare_wrong_keyword(self):
        input = "vaz a, :real;"
        self.assertFalse(TestParser.test(input, success, 217))

    '''
'########:'##::::'##:'##::: ##::'######::'########:'####::'#######::'##::: ##:
 ##.....:: ##:::: ##: ###:: ##:'##... ##:... ##..::. ##::'##.... ##: ###:: ##:
 ##::::::: ##:::: ##: ####: ##: ##:::..::::: ##::::: ##:: ##:::: ##: ####: ##:
 ######::: ##:::: ##: ## ## ##: ##:::::::::: ##::::: ##:: ##:::: ##: ## ## ##:
 ##...:::: ##:::: ##: ##. ####: ##:::::::::: ##::::: ##:: ##:::: ##: ##. ####:
 ##::::::: ##:::: ##: ##:. ###: ##::: ##:::: ##::::: ##:: ##:::: ##: ##:. ###:
 ##:::::::. #######:: ##::. ##:. ######::::: ##::::'####:. #######:: ##::. ##:
..:::::::::.......:::..::::..:::......::::::..:::::....:::.......:::..::::..::
'''

    def test_function_simple_has_var_declare(self):
        input = """
        function foo():real;
        var a, b: boolean;
        begin
            print(hello());
        end"""
        self.assertTrue(TestParser.test(input, success, 218))

    def test_function_simple_no_var_declare(self):
        input = "function foo():real; begin end"
        self.assertTrue(TestParser.test(input, success, 219))

    def test_function_missing_name(self):
        input = "function():real; begin end"
        self.assertTrue(TestParser.test(input, error(1, 8, "("), 220))

    def test_function_err_no_return_type(self):
        input = "function foo(); begin end"
        self.assertFalse(TestParser.test(input, success, 221))

    def test_function_missing_semi_1(self):
        input = "function foo():real begin end"
        self.assertTrue(TestParser.test(input, error(1, 20, "begin"), 222))

    def test_function_missing_semi_2(self):
        input = "function foo(a:real;):real; begin end"
        self.assertTrue(TestParser.test(input, error(1, 20, ")"), 223))

    def test_function_missing_begin_end(self):
        input = "function foo(a:real):real; hello();"
        self.assertTrue(TestParser.test(input, error(1, 27, "hello"), 224))


        

    def test_function_nested_function(self):
        input = """
        procedure proc(); begin
            function(): real; begin
                return 1;
            end
        end
        """
        self.assertFalse(TestParser.test(input, success, 225))
    


    '''
'########::'########:::'#######:::'######::'########:'########::'##::::'##:'########::'########:
 ##.... ##: ##.... ##:'##.... ##:'##... ##: ##.....:: ##.... ##: ##:::: ##: ##.... ##: ##.....::
 ##:::: ##: ##:::: ##: ##:::: ##: ##:::..:: ##::::::: ##:::: ##: ##:::: ##: ##:::: ##: ##:::::::
 ########:: ########:: ##:::: ##: ##::::::: ######::: ##:::: ##: ##:::: ##: ########:: ######:::
 ##.....::: ##.. ##::: ##:::: ##: ##::::::: ##...:::: ##:::: ##: ##:::: ##: ##.. ##::: ##...::::
 ##:::::::: ##::. ##:: ##:::: ##: ##::: ##: ##::::::: ##:::: ##: ##:::: ##: ##::. ##:: ##:::::::
 ##:::::::: ##:::. ##:. #######::. ######:: ########: ########::. #######:: ##:::. ##: ########:
..:::::::::..:::::..:::.......::::......:::........::........::::.......:::..:::::..::........::
'''
    def test_procedure_simple(self):
        input = "procedure foo(); begin end"
        self.assertTrue(TestParser.test(input, success, 226))

    def test_procedure_missing_semi(self):
        input = "procedure foo() begin end"
        expect = "Error on line 1 col 16: begin"
        self.assertTrue(TestParser.test(input, expect, 227))

    def test_procedure_missing_name(self):
        input = "procedure(a:real); begin end;"
        self.assertTrue(TestParser.test(input, error(1, 9, "("), 228))

    def test_procedure_error_has_return_type(self):
        input = "procedure foo(a:real): boolean; begin end"
        self.assertTrue(TestParser.test(input, error(1, 21, ":"), 229))

    def test_procedure_one_param(self):
        input = "procedure foo(a:real); begin end"
        self.assertTrue(TestParser.test(input, success, 230))

    def test_procedure_error_param(self):
        input = "procedure foo(a:real;); begin end"
        expect = "Error on line 1 col 21: )"
        self.assertTrue(TestParser.test(input, expect, 231))

    def test_procedure_many_param(self):
        input = "procedure foo(a,b:real); begin end"
        self.assertTrue(TestParser.test(input, success, 232))

    def test_procedure_many_param_many_type(self):
        input = "procedure foo(a,b:real; c:boolean); begin end"
        self.assertTrue(TestParser.test(input, success, 233))

    def test_procedure_missing_begin_end(self):
        input = "procedure foo(a:real); hello();"
        self.assertTrue(TestParser.test(input, error(1, 23, "hello"), 234))

    def test_procedure_var_declare(self):
        input = """
        procedure foo(a:real);
        var b: real; c: boolean;
        begin
        end
        """
        self.assertTrue(TestParser.test(input, success, 235))


    '''
'####:'##::: ##:'########::'########:'##::::'##::::::::::'########:'##::::'##:'########::
. ##:: ###:: ##: ##.... ##: ##.....::. ##::'##::::::::::: ##.....::. ##::'##:: ##.... ##:
: ##:: ####: ##: ##:::: ##: ##::::::::. ##'##:::::::::::: ##::::::::. ##'##::: ##:::: ##:
: ##:: ## ## ##: ##:::: ##: ######:::::. ###::::::::::::: ######:::::. ###:::: ########::
: ##:: ##. ####: ##:::: ##: ##...:::::: ## ##:::::::::::: ##...:::::: ## ##::: ##.....:::
: ##:: ##:. ###: ##:::: ##: ##:::::::: ##:. ##::::::::::: ##:::::::: ##:. ##:: ##::::::::
'####: ##::. ##: ########:: ########: ##:::. ##:::::::::: ########: ##:::. ##: ##::::::::
....::..::::..::........:::........::..:::::..:::::::::::........::..:::::..::..:::::::::
'''
    def test_index_expression_simple(self):
        input = simple_program("x := a[1];")
        self.assertTrue(TestParser.test(input, success, 236))

    def test_index_expression_complex_1(self):
        input = simple_program("x := foo()[1];")
        self.assertTrue(TestParser.test(input, success, 237))

    def test_index_expression_complex_2(self):
        input = simple_program("x := (foo() + bar())[b[2] + 1*2];")
        self.assertTrue(TestParser.test(input, success, 238))

    def test_index_expression_complex_3(self):
        input = simple_program("x := a[b[c[1]]];")
        self.assertTrue(TestParser.test(input, success, 239))

    def test_index_expression_2_dimentions(self):
        input = simple_program("x := a[1][2];")
        self.assertFalse(TestParser.test(input, success, 240))

    '''
'########:'##::::'##:'########::
 ##.....::. ##::'##:: ##.... ##:
 ##::::::::. ##'##::: ##:::: ##:
 ######:::::. ###:::: ########::
 ##...:::::: ## ##::: ##.....:::
 ##:::::::: ##:. ##:: ##::::::::
 ########: ##:::. ##: ##::::::::
........::..:::::..::..:::::::::
'''
    def test_expression_1(self):
        input = simple_program("x:= foo() + a[2] * 2 /4 > --3 + -(2-3);")
        self.assertTrue(TestParser.test(input, success, 241))

    def test_expression_2(self):
        input = simple_program("x:= 1 < 2 < 3;")
        self.assertTrue(TestParser.test(input, error(2, 10, "<"), 242))

    def test_expression_minus(self):
        input = simple_program("x:= ---(---(a));")
        self.assertTrue(TestParser.test(input, success, 243))

    def test_expression_nested_group(self):
        input = simple_program("x:= ((((1))));")
        self.assertTrue(TestParser.test(input, success, 244))

    def test_expression_nested_group_missing_right_paren(self):
        input = simple_program("x:= ((((1)));")
        self.assertFalse(TestParser.test(input, success, 245))

    def test_expression_nested_group_missing_left_paren(self):
        input = simple_program("x:= (((1))));")
        self.assertFalse(TestParser.test(input, success, 246))

    def test_expression_string_simple(self):
        input = simple_program('x:= "This is a string";')
        self.assertTrue(TestParser.test(input, success, 247))

    def test_expression_string_complex(self):
        input = simple_program(r'x:= "String with \"quote\t\"" + "end" + "\n"; ')
        self.assertTrue(TestParser.test(input, success, 248))

    '''
:'######::'########:'##::::'##:'########:
'##... ##:... ##..:: ###::'###:... ##..::
 ##:::..::::: ##:::: ####'####:::: ##::::
. ######::::: ##:::: ## ### ##:::: ##::::
:..... ##:::: ##:::: ##. #: ##:::: ##::::
'##::: ##:::: ##:::: ##:.:: ##:::: ##::::
. ######::::: ##:::: ##:::: ##:::: ##::::
:......::::::..:::::..:::::..:::::..:::::
'''

    '''
'####:'########:
. ##:: ##.....::
: ##:: ##:::::::
: ##:: ######:::
: ##:: ##...::::
: ##:: ##:::::::
'####: ##:::::::
....::..::::::::
'''
    def test_if_simple_no_else(self):
        input = simple_program("""
        if 2 < 3 then
            print("ok");
        """)
        self.assertTrue(TestParser.test(input, success, 249))
    
    def test_if_simple_else(self):
        input = simple_program("""
        if 1 <> 0 then
            print("ok");
        else
            exit(0);
        """)
        self.assertTrue(TestParser.test(input, success, 250))

    def test_if_error_exp_1(self):
        input = simple_program("""
        if (x:=1) = 2 then
            print("ok");
        else
            exit(0);
        """)
        self.assertTrue(TestParser.test(format_input(input), error(3, 5, ":="), 251))

    def test_if_error_exp_2(self):
        input = simple_program("""
        if x:=1 then
            print("ok");
        else
            exit(0);
        """)
        self.assertTrue(TestParser.test(format_input(input), error(3, 4, ":="), 252))

    def test_if_nested_if_complete(self):
        input = simple_program("""
        if a < b then
            if b < c then
                foo();
            else
                bar();
        else
            foobar();
        """)
        self.assertTrue(TestParser.test(input, success, 253))

    def test_if_nested_if_half_1(self):
        input = simple_program("""
        if a < b then
            if b < c then
                foo();
            else
                bar();
        """)
        self.assertTrue(TestParser.test(input, success, 254))

    def test_if_nested_if_half_2(self):
        input = simple_program("""
        if a < b then
            noop();
        else
            if b < c then
                foo();
            else
                bar();
        """)
        self.assertTrue(TestParser.test(input, success, 255))

    def test_if_compound_statement(self):
        input = simple_program("""
        if a < b then
        begin 
            a := 1;
            b := foo(a);
        end
        """)
        self.assertTrue(TestParser.test(input, success, 256))

    '''
:::'###:::::'######:::'######:::'##::::'##:'##::: ##:'########:
::'## ##:::'##... ##:'##... ##:: ###::'###: ###:: ##:... ##..::
:'##:. ##:: ##:::..:: ##:::..::: ####'####: ####: ##:::: ##::::
'##:::. ##:. ######:: ##::'####: ## ### ##: ## ## ##:::: ##::::
 #########::..... ##: ##::: ##:: ##. #: ##: ##. ####:::: ##::::
 ##.... ##:'##::: ##: ##::: ##:: ##:.:: ##: ##:. ###:::: ##::::
 ##:::: ##:. ######::. ######::: ##:::: ##: ##::. ##:::: ##::::
..:::::..:::......::::......::::..:::::..::..::::..:::::..:::::
'''
    def test_assignment_statement_simple(self):
        input = simple_program("x := 1;")
        self.assertTrue(TestParser.test(input, success, 257))

    def test_assignment_statement_error_operator(self):
        input = simple_program("x : = 100;")
        self.assertFalse(TestParser.test(input, success, 258))

    def test_assignment_statement_error_operator(self):
        input = simple_program("x = 100;")
        self.assertTrue(TestParser.test(input, error(2, 2, "="), 259))

    def test_assignment_statement_error_lhs(self):
        input = simple_program("1 := 100;")
        self.assertFalse(TestParser.test(input, success, 260))

    def test_assignment_statement_simple_array(self):
        input = simple_program("x[1] := 1;")
        self.assertTrue(TestParser.test(input, success, 261))

    def test_assignment_statement_chain_simple(self):
        input = simple_program("x := y := z := foo(m);")
        self.assertTrue(TestParser.test(input, success, 262)) 

    def test_assignment_statement_chain_complex(self):
        input = simple_program("x := foo()[1] := arr[2] := (a + b)[3] := m + hello();")
        self.assertTrue(TestParser.test(input, success, 263))

    def test_assignment_statement_chain_error(self):
        input = simple_program("x := foo(m) := 1;  // error at foo(m)")
        self.assertFalse(TestParser.test(input, success, 264))



    '''
:'######:::'#######::'##::: ##:'########:'####:'##::: ##:'##::::'##:'########:
'##... ##:'##.... ##: ###:: ##:... ##..::. ##:: ###:: ##: ##:::: ##: ##.....::
 ##:::..:: ##:::: ##: ####: ##:::: ##::::: ##:: ####: ##: ##:::: ##: ##:::::::
 ##::::::: ##:::: ##: ## ## ##:::: ##::::: ##:: ## ## ##: ##:::: ##: ######:::
 ##::::::: ##:::: ##: ##. ####:::: ##::::: ##:: ##. ####: ##:::: ##: ##...::::
 ##::: ##: ##:::: ##: ##:. ###:::: ##::::: ##:: ##:. ###: ##:::: ##: ##:::::::
. ######::. #######:: ##::. ##:::: ##::::'####: ##::. ##:. #######:: ########:
:......::::.......:::..::::..:::::..:::::....::..::::..:::.......:::........::
'''
    def test_statement_continue(self):
        input = simple_program("continue;")
        self.assertTrue(TestParser.test(input, success, 265))

    ### break statement
    def test_statement_break(self):
        input = simple_program("break;")
        self.assertTrue(TestParser.test(input, success, 266))

    ### return statement
    def test_statement_return(self):
        input = simple_program("return;")
        self.assertTrue(TestParser.test(input, success, 267))

    def test_statement_return_expression(self):
        input = simple_program("return 0;")
        self.assertTrue(TestParser.test(input, success, 268))

    def test_statement_return_wrong_keyword(self):
        input = simple_program("creturn 0;")
        self.assertFalse(TestParser.test(input, success, 269))


    '''
:'######:::::'###::::'##:::::::'##:::::::
'##... ##:::'## ##::: ##::::::: ##:::::::
 ##:::..:::'##:. ##:: ##::::::: ##:::::::
 ##:::::::'##:::. ##: ##::::::: ##:::::::
 ##::::::: #########: ##::::::: ##:::::::
 ##::: ##: ##.... ##: ##::::::: ##:::::::
. ######:: ##:::: ##: ########: ########:
:......:::..:::::..::........::........::
'''
    def test_call_statement_no_input(self):
        input = simple_program("foo();")
        self.assertTrue(TestParser.test(input, success, 270))

    def test_call_statement_one_input(self):
        input = simple_program("foo(x);")
        self.assertTrue(TestParser.test(input, success, 271))

    def test_call_statement_input_string(self):
        input = simple_program('print("hello world");')
        self.assertTrue(TestParser.test(input, success, 272))

    def test_call_statement_many_input(self):
        input = simple_program("foo(x, bar(x), y, z);")
        self.assertTrue(TestParser.test(input, success, 273))

    def test_call_statement_one_missing_input_semi(self):
        input = simple_program("foo(x y);")
        self.assertTrue(TestParser.test(input, error(2, 6, "y"), 274))

    def test_call_statement_one_missing_last_semi(self):
        input = simple_program("foo()")
        self.assertTrue(TestParser.test(input, error(3, 0, "end"), 275))

    
    '''
:'######:::'#######::'##::::'##:'########:::'#######::'##::::'##:'##::: ##:'########::
'##... ##:'##.... ##: ###::'###: ##.... ##:'##.... ##: ##:::: ##: ###:: ##: ##.... ##:
 ##:::..:: ##:::: ##: ####'####: ##:::: ##: ##:::: ##: ##:::: ##: ####: ##: ##:::: ##:
 ##::::::: ##:::: ##: ## ### ##: ########:: ##:::: ##: ##:::: ##: ## ## ##: ##:::: ##:
 ##::::::: ##:::: ##: ##. #: ##: ##.....::: ##:::: ##: ##:::: ##: ##. ####: ##:::: ##:
 ##::: ##: ##:::: ##: ##:.:: ##: ##:::::::: ##:::: ##: ##:::: ##: ##:. ###: ##:::: ##:
. ######::. #######:: ##:::: ##: ##::::::::. #######::. #######:: ##::. ##: ########::
:......::::.......:::..:::::..::..::::::::::.......::::.......:::..::::..::........:::
'''
    def test_statement_compound(self):
        input = simple_program("""
        begin
            x := calc(10);
            return x;
        end
        """)
        self.assertTrue(TestParser.test(input, success, 276))

    def test_statement_compound_nested(self):
        input = simple_program("""
        begin
        x := calc(10);
            begin
                return x;
            end
        end
        """)
        self.assertTrue(TestParser.test(input, success, 277))

    def test_statement_compound_nested_error_missing_end(self):
        input = simple_program("""
        begin
            x := calc(10);
            begin
                return x;
        end
        """)
        self.assertFalse(TestParser.test(input, success, 278))

    '''
'########::'#######::'########::
 ##.....::'##.... ##: ##.... ##:
 ##::::::: ##:::: ##: ##:::: ##:
 ######::: ##:::: ##: ########::
 ##...:::: ##:::: ##: ##.. ##:::
 ##::::::: ##:::: ##: ##::. ##::
 ##:::::::. #######:: ##:::. ##:
..:::::::::.......:::..:::::..::
'''
    def test_statement_for(self):
        input = simple_program("""
        for i:= 1 to len(str) do
            print(str[i]);
        """)
        self.assertTrue(TestParser.test(input, success, 279))

    def test_statement_for_downto(self):
        input = simple_program("""
        for i:= 100 downto 1 do
            print(str[i]);
        """)
        self.assertTrue(TestParser.test(input, success, 280))

    '''
'##:::::'##:'##::::'##:'####:'##:::::::'########:
 ##:'##: ##: ##:::: ##:. ##:: ##::::::: ##.....::
 ##: ##: ##: ##:::: ##:: ##:: ##::::::: ##:::::::
 ##: ##: ##: #########:: ##:: ##::::::: ######:::
 ##: ##: ##: ##.... ##:: ##:: ##::::::: ##...::::
 ##: ##: ##: ##:::: ##:: ##:: ##::::::: ##:::::::
. ###. ###:: ##:::: ##:'####: ########: ########:
:...::...:::..:::::..::....::........::........::
'''
    def test_statement_while(self):
        input = simple_program("""
        while sqrt(x) < num do
            x := x + 1;
        """)
        self.assertTrue(TestParser.test(input, success, 281))

    '''
'##:::::'##:'####:'########:'##::::'##:
 ##:'##: ##:. ##::... ##..:: ##:::: ##:
 ##: ##: ##:: ##::::: ##:::: ##:::: ##:
 ##: ##: ##:: ##::::: ##:::: #########:
 ##: ##: ##:: ##::::: ##:::: ##.... ##:
 ##: ##: ##:: ##::::: ##:::: ##:::: ##:
. ###. ###::'####:::: ##:::: ##:::: ##:
:...::...:::....:::::..:::::..:::::..::
'''
    def test_statement_with(self):
        input = simple_program("""
        with i, j: integer; tmp: real; do
            print(i, j, tmp);
        """)
        self.assertTrue(TestParser.test(input, success, 282))

    def test_statement_with_missing_semi(self):
        input = simple_program("""
        with i, j: integer; tmp: real do
            print(i, j, real);
        """)
        self.assertTrue(TestParser.test(format_input(input), error(3, 30, "do"), 283))

    '''
:'######:::'#######::'##::::'##:'##::::'##:'########:'##::: ##:'########:
'##... ##:'##.... ##: ###::'###: ###::'###: ##.....:: ###:: ##:... ##..::
 ##:::..:: ##:::: ##: ####'####: ####'####: ##::::::: ####: ##:::: ##::::
 ##::::::: ##:::: ##: ## ### ##: ## ### ##: ######::: ## ## ##:::: ##::::
 ##::::::: ##:::: ##: ##. #: ##: ##. #: ##: ##...:::: ##. ####:::: ##::::
 ##::: ##: ##:::: ##: ##:.:: ##: ##:.:: ##: ##::::::: ##:. ###:::: ##::::
. ######::. #######:: ##:::: ##: ##:::: ##: ########: ##::. ##:::: ##::::
:......::::.......:::..:::::..::..:::::..::........::..::::..:::::..:::::
'''
    def test_comment_line(self):
        input = simple_program("hello(); // this is line comment {}")
        self.assertTrue(TestParser.test(input, success, 284))

    def test_comment_block_1(self):
        input = simple_program("""
        { block comment
            if then else
            // more
        }
        normal_function("hello");
        """)
        self.assertTrue(TestParser.test(input, success, 285))

    def test_comment_block_1_unclose(self):
        input = simple_program("""
        { block comment
            if then else
            // more
        
        normal_function("hello");
        """)
        self.assertFalse(TestParser.test(input, success, 286))

    def test_comment_block_1_no_open(self):
        input = simple_program("""
        block comment
            if then else
            // more
        
        normal_function("hello");
        """)
        self.assertFalse(TestParser.test(input, success, 287))

    def test_comment_block_2(self):
        input = simple_program("""
        (* block comment
            if then else
            // more
        *)
        normal_function("hello");
        """)
        self.assertTrue(TestParser.test(input, success, 288))

    def test_comment_block_2_unclose(self):
        input = simple_program("""
        (* block comment
            if then else
            // more
        
        normal_function("hello");
        """)
        self.assertFalse(TestParser.test(input, success, 289))

    def test_comment_block_2_no_open(self):
        input = simple_program("""
        block comment
            if then else
            // more
        
        normal_function("hello");
        """)
        self.assertFalse(TestParser.test(input, success, 290))

    def test_comment_mix(self):
        input = simple_program("""
        { block comment
            if then else
            // more
        }
        normal_function("hello");
        """)
        self.assertTrue(TestParser.test(input, success, 291))

    '''
'########::'########:::'#######:::'######:::'########:::::'###::::'##::::'##:
 ##.... ##: ##.... ##:'##.... ##:'##... ##:: ##.... ##:::'## ##::: ###::'###:
 ##:::: ##: ##:::: ##: ##:::: ##: ##:::..::: ##:::: ##::'##:. ##:: ####'####:
 ########:: ########:: ##:::: ##: ##::'####: ########::'##:::. ##: ## ### ##:
 ##.....::: ##.. ##::: ##:::: ##: ##::: ##:: ##.. ##::: #########: ##. #: ##:
 ##:::::::: ##::. ##:: ##:::: ##: ##::: ##:: ##::. ##:: ##.... ##: ##:.:: ##:
 ##:::::::: ##:::. ##:. #######::. ######::: ##:::. ##: ##:::: ##: ##:::: ##:
..:::::::::..:::::..:::.......::::......::::..:::::..::..:::::..::..:::::..::
'''

    def test_program_simple_error(self):
        input = "procedure main() begin end"
        self.assertTrue(TestParser.test(input, error(1, 17, "begin"), 292))
    
    def test_program_complex_1(self):
        input = """
        var x, y: real;
        function add(x, y: real): real;
        begin
            return x + y + random();
        end
        """
        self.assertTrue(TestParser.test(input, success, 293)) 

    def test_program_error_char(self):
        input = "var x, y, z: real; ^d2x"
        self.assertFalse(TestParser.test(input, success, 294))

    def test_program_error_id(self):
        input = simple_program("print(real);")
        self.assertTrue(TestParser.test(input, error(2, 6, "real"), 295))

    def test_program_error_2(self):
        input = """
        var a,b,c: real;
             d, e: string
        procedure foo()
        begin
        end
        """
        self.assertTrue(TestParser.test(format_input(input), error(4, 0, "procedure"), 296))
    
    def test_program_error_3(self):
        input = "(";
        self.assertTrue(TestParser.test(input, error(1, 0, "("), 297))

    def test_program_wrong_statement(self):
        input = simple_program("""
        if a < b then
        begin 
            a := 1;
            b = foo(a); // error here
        end
        """)
        self.assertTrue(TestParser.test(format_input(input), error(6, 2, "="), 298))

    def test_program_empty(self):
        input = ""
        self.assertTrue(TestParser.test(input, error(1, 0, "<EOF>"), 299))

