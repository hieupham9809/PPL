import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: """
        input = """function foo(a, b: integer; c: real) : array [ 1 .. 2 ] of integer;
        var x, y : real;
        begin 
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_more_complex_program(self):
        """More complex program"""
        input = """procedure foo(a,b:integer; c:real);
        var x,y: real;
        begin 
        
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,202))

        input = """procedure foo(a,b:integer; c:real);
        var x,y: real 
        begin
        end
        """
        expect = "Error on line 3 col 8: begin"
        self.assertTrue(TestParser.test(input,expect,204))

        input = """function foo():string;begin \n end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,205))

        input = """procedure foo(a,b:integer; c:real);
        var x,y: real;
        begin 
        x := y + 1;

        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,206))

        input = """procedure foo(a,b:integer; c:real);
        var x,y: real;
        begin 
        a := b [10] := foo()[3] := x := 1 ;

        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,213))

        input = """procedure foo(a,b:integer; c:real);
        var x,y: real;
        begin 
        a := b [10] := 3 := x := 1 ;

        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,214))

        input = """procedure foo(a,b:integer; c:real);
        var x,y: real;
            z: array[2 .. 3] of integer;
        begin 
        x := y + 1;
        x := z[2];
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,207))

        input = """procedure foo(a,b:integer; c:real);
        var x,y: real;
            z: array[2 .. 3] of integer;
        begin 
        x := y + 1;
        x := z[2];
        foo(x);
        foo(2)[3+x] := a[b[2]] +3;
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,208))

        # if then statement
        input = """procedure foo(a,b:integer; c:real);
        var x,y: real;
            z: array[2 .. 3] of integer;
        begin 
        if 5>6 then x := y;
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,209))

        #if then else statement
        input = """procedure foo(a,b:integer; c:real);
        var x,y: real;
            z: array[2 .. 3] of integer;
        begin 
        if (5>6) then x := y; else y := x;
        
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,210))

        # if then else nested statement
        input = """procedure foo(a,b:integer; c:real);
        var x,y: real;
            z: array[2 .. 3] of integer;
        begin 
        if (5>6) then x := y; else 
            if (true) then y:=x;
        
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,211))

        #  statement
        input = """procedure foo(a,b:integer; c:real);
        var x,y: real;
            z: array[2 .. 3] of integer;
        begin 
        if (5>6) then x := y; else 
            if (true) then y:=x;
        
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,212))
    def test_wrong_miss_close(self):
        """Miss ) """
        input = """procedure foo(a,b:integer; c:real;
        var x,y: real 
        begin
        end"""
        expect = "Error on line 2 col 8: var"
        self.assertTrue(TestParser.test(input,expect,203))

        """incorrect variable declaration 3"""
        input = """float a,c,d"""
        expect = "Error on line 1 col 0: float"
        self.assertTrue(TestParser.test(input,expect,303))

    def test_array(self):
        """array type"""
        input = """var d:array [ 1 .. 5 ] of integer;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,220))
        
        input = """var d:array [ 1 .. 5  of integer;"""
        expect = "Error on line 1 col 22: of"
        self.assertTrue(TestParser.test(input,expect,221))
        
        input = """var d:array [1 .. 5] of integer; a,b,c: integer; e,f: real;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,222))
        
        input = """var d:array [1 .. 5] of integer;\n a,b,c: integer;\n e,f: real;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,223))

    #def test_expression(self):
