import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_function_dec_1(self):
        """function foo(a: integer; c: real) : array [ 1 .. 2 ] of integer;
        var m, n : real;
        begin 
        end"""
        input = """function foo(a: integer; c: real) : array [ 1 .. 2 ] of integer;
        var m, n : real;
        begin 
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))

    def test_function_dec_2(self):
        """FUNcTioN foo(a, b: integer ; g: real):array [5 .. 7] of integer;
                  var x,y,z,k: real ;
                  BEGIN

                  END"""
        input = """FUNcTioN foo(a, b: integer ; g: real):array [5 .. 7] of integer;
                  var x,y,z,k: real ;
                  BEGIN

                  END"""
        expect = "successful"

        self.assertTrue(TestParser.test(input,expect,202))
    def test_statement_assign_1(self):
        """proCeduRE foo(m, n: integer; c: real) ;
                  var x,y,z: real ;
                  BEGIN
                    m := 12; n := c[2];
                  END"""
        input = """proCeduRE foo(m, n: integer; c: real) ;
                  var x,y,z: real ;
                  BEGIN
                    m := 12; n := c[2];
                  END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,203))

    def test_statement_assign_2(self):
        """function foo(c: real): real ; y:=a[0]"""
        input = """function foo(c: real): real ; y:=a[0]"""
        expect = ""

        self.assertTrue(TestParser.test(input,expect,204))
    def test_statement_assign_3(self):
        """PROCeduRe foo() ;
                  var x,y,z: real ;
                  BEGIN
                    a := "char";  b := func(1,a+1) ;
                  END"""
        input = """PROCeduRe foo() ;
                  var x,y,z: real ;
                  BEGIN
                    a := "char";  b := func(1,a+1) ;
                  END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,205))
    def test_statement_assign_4(self):
        """proCEDURE foo(c: real) ;
                   var x,y,z: real ;
                   BEGIN
                    2 := 1;
                    c := a[0] ;
                   END"""
        input = """proCEDURE foo(c: real) ;
                   var x,y,z: real ;
                   BEGIN
                    2 := 1;
                    c := a[0] ;
                   END"""
        expect = ""
        

        self.assertTrue(TestParser.test(input,expect,206))
    def test_statement_assign_5(self):
        """function foo(c: real): real ;
                   var x,y: array[m..n] of real;
                   BEGIN
                    a[m+n] := a[n+1] ;
                   END"""
        input = """function foo(c: real): real ;
                   var x,y: array[m..n] of real;
                   BEGIN
                    a[m+n] := a[n+1] ;
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,207))
    def test_statement_assign_6(self):
        """FUNCTION foo(c: integer): integer ;
                   var x,y: integer;
                   BEGIN
                    a[m+n] := a[m+1] := foo()[m*2] := a[2 div a] := (a>=m) and then (b<=n);
                   END"""
        input = """FUNCTION foo(c: integer): integer ;
                   var x,y: integer;
                   BEGIN
                    a[m+n] := a[m+1] := foo()[m*2] := a[2 div a] := (a>=m) and then (b<=n);
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,208))
    def test_statement_assign_7(self):
        """function foo(c: real): real ; x:=a[1]"""
        input = """function foo(c: real): real ; x:=a[1]"""
        expect = "Error on line 1 col 30: x"

        self.assertTrue(TestParser.test(input,expect,209))
    def test_statement_if_2(self):
        """function foo(c: integer): real ;
                   var y,z:real ;
                   BEGIN
                    if(a>=1) then a:=1 ;
                   END"""
        input = """function foo(c: integer): real ;
                   var y,z:real ;
                   BEGIN
                    if(a>=1) then a:=1 ;
                   END"""
        expect = "successful"

        self.assertTrue(TestParser.test(input,expect,210))
    def test_statement_if_3(self):
        """pROCEDURE foo(c: integer) ;
                   var y:real ;
                   BEGIN
                    if(a>=1) then a:=1 ;
                    else if (1<=2)<>(2<=3) 
                        then x:=2 ;
                    else foo(a+1,1);
                   END"""
        input = """pROCEDURE foo(c: integer) ;
                   var y:real ;
                   BEGIN
                    if(a>=1) then a:=1 ;
                    else if (1<=2)<>(2<=3) 
                        then x:=2 ;
                    else foo(a+1,1);
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,211))
    def test_statement_if_4(self):
        """pROCEDURE foo(c: real) ;
                   var x:real ;
                   BEGIN
                    if(a>=1) then a:=2 ;
                    if (1<=2) then beGIN x:=2 ; eND
                    else foo(a+1,2);
                   END"""
        input = """pROCEDURE foo(c: real) ;
                   var x:real ;
                   BEGIN
                    if(a>=1) then a:=2 ;
                    if (1<=2) then beGIN x:=2 ; eND
                    else foo(a+1,2);
                   END"""
        expect = "successful"

        self.assertTrue(TestParser.test(input,expect,212))
    def test_statement_if_5(self):
        """pROCEDURE foo(c: real) ;
                   var x:real ;
                   BEGIN
                    if(a>=1) then a:=0 ;
                    if (1<=2) then beGIN x:=1 ; enD
                    else foo(a+1,a);
                   END"""
        input = """pROCEDURE foo(c: real) ;
                   var x:real ;
                   BEGIN
                    if(a>=1) then a:=0 ;
                    if (1<=2) then beGIN x:=1 ; enD
                    else foo(a+1,a);
                   END"""
        expect = "successful"

        self.assertTrue(TestParser.test(input,expect,213))
    def test_statement_if_6(self):
        """pROCEDURE foo1(c: string) ;
                   var x:real ;
                   BEGIN
                    if(a>=1) then beGin
                        a:=1 ;
                        if(2=1) then a:= b[1];
                        else b:=a[1]:= 1;
                    ENd
                    END"""
        input = """pROCEDURE foo1(c: string) ;
                   var x:real ;
                   BEGIN
                    if(a>=1) then beGin
                        a:=1 ;
                        if(2=1) then a:= b[1];
                        else b:=a[1]:= 1;
                    ENd
                    END"""
        expect = "successful"

        self.assertTrue(TestParser.test(input,expect,214))
    def test_statement_with_1(self):
        """pROCEDURE foo(c: real) ;
                   BEGIN
                    with a , b : integer ; c : array [2 .. 4] of real ; dO
                    d := c[a] + b ;
                   END"""
        input = """pROCEDURE foo(c: real) ;
                   BEGIN
                    with a , b : integer ; c : array [2 .. 4] of real ; dO
                    d := c[a] + b ;
                   END"""
        expect = "successful"

        self.assertTrue(TestParser.test(input,expect,215))
    def test_statement_with_2(self):
        """pROCEDURE foo(c: real) ;
                   BEGIN
                    with a , b : integer ; c : array [1 .. 2] of real ; do begin
                    a := c[a] + b ;
                    foo();foo1(a,b,c);
                    end
                   END"""
        input = """pROCEDURE foo(c: real) ;
                   BEGIN
                    with a , b : integer ; c : array [1 .. 2] of real ; do begin
                    a := c[a] + b ;
                    foo();foo1(a,b,c);
                    end
                   END"""
        expect = "successful"

        self.assertTrue(TestParser.test(input,expect,216))
    def test_statement_with_3(self):
        """pROCEDURE foo(c: real) ;
                   BEGIN
                    with a ,b : integer ; c: array [1 .. 2] of real ; do
                    begin
                    d := c [a] + b ;
                    foo();foo1(a,b,c);
                    with a , b : integer ; do 
                    begin
                        foo2(a,b,"abc");
                    end
                    end
                   END"""
        input = """pROCEDURE foo(c: real) ;
                   BEGIN
                    with a ,b : integer ; c: array [1 .. 2] of real ; do
                    begin
                    d := c [a] + b ;
                    foo();foo1(a,b,c);
                    with a , b : integer ; do 
                    begin
                        foo2(a,b,"abc");
                    end
                    end
                   END"""
        expect = "successful"

        self.assertTrue(TestParser.test(input,expect,217))
    def test_statement_with_4(self):
        """function foo(d: real): sTRIng;
                   BEGIN
                    with c , d : integer ; c : array [1 .. 2] of real ; do
                    with a , b : integer ; 
                    do
                        foo2(a,b,"anc");
                   END"""
        input = """function foo(d: real): sTRIng;
                   BEGIN
                    with c , d : integer ; c : array [1 .. 2] of real ; do
                    with a , b : integer ; 
                    do
                        foo2(a,b,"anc");
                   END"""
        expect = "successful"

        self.assertTrue(TestParser.test(input,expect,218))
    def test_statement_for_7(self):
        """function foo(c: real): STRIng;
                   BEGIN
                    FOR i:=1 to m+10 
                    do 
                        s := s + 1;
                   END"""
        input = """function foo(c: real): STRIng;
                   BEGIN
                    FOR i:=1 to m+10 
                    do 
                        s := s + 1;
                   END"""
        expect = "successful"

        self.assertTrue(TestParser.test(input,expect,219))
    def test_statement_with_6(self):
        """function foo(c: real): STRIng;
                   BEGIN
                    with i, j: integer; tmp: real; do
                    print(i, j, tmp);
                    FOR i:=1 to m+10 
                    do 
                        s := s + 1;
                   END"""
        input = """function foo(c: real): STRIng;
                   BEGIN
                    with i, j: integer; tmp: real; do
                    print(i, j, tmp);
                    FOR i:=1 to m+10 
                    do 
                        s := s + 1;
                   END"""
        expect = "successful"

        self.assertTrue(TestParser.test(input,expect,220))
    def test_statement_while_1(self):
        """PROCEDURE foo(c: integer) ;
                   var x:real ;
                   BEGIN
                    WhILe(a<>1) do beGin end
                   END"""
        input = """PROCEDURE foo(c: integer) ;
                   var x:real ;
                   BEGIN
                    WhILe(a<>1) do beGin end
                   END"""
        expect = "successful"

        self.assertTrue(TestParser.test(input,expect,221))
    def test_statement_while_2(self):
        """pROCEDURE foo(c: real) ;
                   var x:real ;
                   BEGIN
                    whILe(a=1) do beGin
                        if(a=1) then x:=1;
                        foo();
                    end
                   END"""
        input = """pROCEDURE foo(c: real) ;
                   var x:real ;
                   BEGIN
                    whILe(a=1) do beGin
                        if(a=1) then x:=1;
                        foo();
                    end
                   END"""
        expect = "successful"

        self.assertTrue(TestParser.test(input,expect,222))
    def test_statement_while_3(self):
        """pROCEDURE foo(c: real) ;
                   var x:real ;
                   BEGIN
                    whILe(a<>1) do beGin
                        while(1) do x:=1;
                    end
                   END"""
        input = """pROCEDURE foo(c: real) ;
                   var x:real ;
                   BEGIN
                    whILe(a<>1) do beGin
                        while(1) do x:=1;
                    end
                   END"""
        expect = "successful"

        self.assertTrue(TestParser.test(input,expect,223))
    def test_statement_while_4(self):
        """pROCEDURE foo(d: real) ;
                   BEGIN
                    whILe(a<>1) do bEGin
                        while(1) do x:=1;
                        if(a=1) then 
                        begin end
                    end
                   END"""
        input = """pROCEDURE foo(d: real) ;
                   BEGIN
                    whILe(a<>1) do bEGin
                        while(1) do x:=1;
                        if(a=1) then 
                        begin end
                    end
                   END"""
        expect = "successful"

        self.assertTrue(TestParser.test(input,expect,224))
    def test_statement_while_5(self):
        """pROCEDURE foo(d: real) ;
                   BEGIN
                    whILe(1) do bEGin
                        while(1) do x:=1;
                        if(a=1) then 
                        begin end
                    end
                   END"""
        input = """pROCEDURE foo(d: real) ;
                   BEGIN
                    whILe(1) do bEGin
                        while(1) do x:=1;
                        if(a=1) then 
                        begin end
                    end
                   END"""
        expect = "successful"

        self.assertTrue(TestParser.test(input,expect,225))
    def test_statement_while_6(self):
        """pROCEDURE foo(c: real) ;
                   var x:real ;
                   BEGIN
                    whILe(a<>1) do BEGin
                        while(1) do x:=1;
                        x := x + 1;
                    end
                   END"""
        input = """pROCEDURE foo(c: real) ;
                   var x:real ;
                   BEGIN
                    whILe(a<>1) do BEGin
                        while(1) do x:=1;
                        x := x + 1;
                    end
                   END"""
        expect = "successful"

        self.assertTrue(TestParser.test(input,expect,226))
    def test_statement_for_1(self):
        """function foo(s: real): STRIng;
                   BEGIN
                    FOR i:=1 to m+10 
                    do 
                        s := s + 1;
                   END"""
        input = """function foo(s: real): STRIng;
                   BEGIN
                    FOR i:=1 to m+10 
                    do 
                        s := s + 1;
                   END"""
        expect = "successful"

        self.assertTrue(TestParser.test(input,expect,227))
    def test_statement_for_2(self):
        """function foo(c: real): sTRIng;
                   BEGIN
                    FOR i:=1 to m+10 do beGin
                        s := s + 1;
                        if(a=1) then begin s:=s-1; end
                    end
                   END"""
        input = """function foo(c: real): sTRIng;
                   BEGIN
                    FOR i:=1 to m+10 do beGin
                        s := s + 1;
                        if(a=1) then begin s:=s-1; end
                    end
                   END"""
        expect = "successful"

        self.assertTrue(TestParser.test(input,expect,228))
    def test_statement_for_3(self):
        """function foo(d: real): STRIng;
                   BEGIN
                    FOR i:=1 to m+10 do beGin
                        for j:=m+1 doWnTO 100 do bEGin
                            s := s + 3;
                            if(a=1) then s:=s-1;
                        eND
                    end
                   END"""
        input = """function foo(d: real): STRIng;
                   BEGIN
                    FOR i:=1 to m+10 do beGin
                        for j:=m+1 doWnTO 100 do bEGin
                            s := s + 3;
                            if(a=1) then s:=s-1;
                        eND
                    end
                   END"""
        expect = "successful"

        self.assertTrue(TestParser.test(input,expect,229))
    def test_statement_for_4(self):
        
        input = """PROCEDURE foo(c: real);
                   BEGIN
                    FOR i:=1 to m+10 do beGin
                        while i>1 do
                            FOR i:=m+1 doWnTO 10 do
                                while j>1 do x:=foo(10);
                    End
                   END"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,230))
    def test_statement_break_1(self):
        """pROCEDURE foo(c: real);
                   BEGIN
                    FOR i:=1 to m+10 do beGin
                        brEaK;
                    end
                   END"""
        input = """pROCEDURE foo(c: real);
                   BEGIN
                    FOR i:=1 to m+10 do beGin
                        brEaK;
                    end
                   END"""
        expect = "successful"

        self.assertTrue(TestParser.test(input,expect,231))
    def test_statement_break_2(self):
        """pROCEDURE foo(c: real);
                   BEGIN
                    FOR i:=1 to m+10 do beGin
                        brEaK;
                    end
                    break;
                   END"""
        input = """pROCEDURE foo(c: real);
                   BEGIN
                    FOR i:=1 to m+10 do beGin
                        brEaK;
                    end
                    break;
                   END"""
        expect = "successful"

        self.assertTrue(TestParser.test(input,expect,232))
    def test_statement_continue_1(self):
        """PROCEDURE foo(c: real);
                   BEGIN
                    while (1) do ContinuE ;
                   END"""
        input = """PROCEDURE foo(c: real);
                   BEGIN
                    while (1) do ContinuE ;
                   END"""
        expect = "successful"

        self.assertTrue(TestParser.test(input,expect,233))
    def test_statement_return_1(self):
        """pROCEDURE foo(c: real);
                   BEGIN
                    while (1) do RETURN ;
                   END"""
        input = """pROCEDURE foo(c: real);
                   BEGIN
                    while (1) do RETURN ;
                   END"""
        expect = "successful"

        self.assertTrue(TestParser.test(input,expect,234))
    def test_statement_call_1(self):
        """function foo(c: real): real;
                   BEGIN
                    foocall(3,a+1,a<>1,a[1]);
                    return 1;
                   END"""
        input = """function foo(c: real): real;
                   BEGIN
                    foocall(3,a+1,a<>1,a[1]);
                    return 1;
                   END"""
        expect = "successful"

        self.assertTrue(TestParser.test(input,expect,235))
    def test_statement_call_2(self):
        
        input = """function foo(c: real): integer;
                   BEGIN
                    foo(3,foo(foo1(foo(2,a+1))));
                    return func(a(1,2));
                   END"""
        expect = "successful"

        self.assertTrue(TestParser.test(input,expect,236))
    def test_statement_call_3(self):
        """function foo(c: real): integer;
                   BEGIN
                    foo (3,a+1);
                    foo1();
                    return;
                   END"""
        input = """function foo(c: real): integer;
                   BEGIN
                    foo (3,a+1);
                    foo1();
                    return;
                   END"""
        expect = "successful"

        self.assertTrue(TestParser.test(input,expect,237))
    def test_statement_call_4(self):
        """function foo(c: real): integer;
                   BEGIN
                    text(brown); { colour}
                	ClrScr(); {.d.}
                    return func(a(1,2));
                   END"""
        input = """function foo(c: real): integer;
                   BEGIN
                    text(brown); { colour}
                	ClrScr(); {.d.}
                    return func(a(1,2));
                   END"""
        expect = "successful"

        self.assertTrue(TestParser.test(input,expect,238))
    def test_statement_call_5(self):
        """function foo(c: real): integer;
                   BEGIN
                    foo(3,a+1,x and then y,a[1],foo(1,2)[m+1]);
                    return foo2() + foo();
                   END"""
        input = """function foo(c: real): integer;
                   BEGIN
                    foo(3,a+1,x and then y,a[1],foo(1,2)[m+1]);
                    return foo2() + foo();
                   END"""
        expect = "successful"

        self.assertTrue(TestParser.test(input,expect,239))
    def test_statement_mix_1(self):
        """
                procedure test1() ;
                begin
	               if a=b then
	               bEGin
		                 b := c := 6;
		                 if(e <> f) then foo(a,c) ;
	               end
                end
                """
        input = """
                procedure test1() ;
                begin
	               if a=b then
	               bEGin
		                 b := c := 6;
		                 if(e <> f) then foo(a,c) ;
	               end
                end
                """
        expect = "successful"

        self.assertTrue(TestParser.test(input,expect,240))
    def test_statement_mix_2(self):
        """
                procedure test2() ;
                begin
	               if a=b then if c=d then while (d=e) do
                   beGin
                   eND
               else c := 1;
                end
                """
        input = """
                procedure test2() ;
                begin
	               if a=b then if c=d then while (d=e) do
                   beGin
                   eND
               else c := 1;
                end
                """
        expect = "successful"

        self.assertTrue(TestParser.test(input,expect,241))
    def test_statement_mix_3(self):
        """
                VAR i: real ;
                FUNCTION f(): integer ;
                begin
	               return 100;
                end
                procedure main() ;
                var
	               main: integer ;
                begin
	               main := f() ;
	               putIntLn(main);
	               main := f := i:= 100;
                   with
                        i: integer;
	               do begin 
		                putIntLn (i);
	               end
	               putIntLn (main);
                end
                var g: real ;
                """
        input = """
                VAR i: real ;
                FUNCTION f(): integer ;
                begin
	               return 100;
                end
                procedure main() ;
                var
	               main: integer ;
                begin
	               main := f() ;
	               putIntLn(main);
	               main := f := i:= 100;
                   with
                        i: integer;
	               do begin 
		                putIntLn (i);
	               end
	               putIntLn (main);
                end
                var g: real ;
                """
        expect = "successful"

        self.assertTrue(TestParser.test(input,expect,242))
    def test_statement_mix_4(self):
        
        input = """
                proceDure Hello(b:integer);
                begin
                    a := b + c;
                end
                """
        expect = "successful"

        self.assertTrue(TestParser.test(input,expect,243))
    def test_statement_mix_5(self):
        """
        var x, y: real;
        function add(x, y: real): real;
        begin
            return x + y + random();
        end
        """
        input = """
        var x, y: real;
        function add(x, y: real): real;
        begin
            return x + y + random();
        end
        """
        expect = "successful"

        self.assertTrue(TestParser.test(input,expect,244))
    def test_statement_mix_6(self):
        """
        if a < b then
        begin 
            a := 1;
            b = foo(a); 
        end
        """
        input = """
        if a < b then
        begin 
            a := 1;
            b = foo(a); 
        end
        """
        expect = ""

        self.assertTrue(TestParser.test(input,expect,245))
    def test_statement_mix_7(self):
        """
                procedure mainfoo() ;
                beGin
                 a[b[2]] := 100;
                 foo(2);
                 return ;
                eND
                """
        input = """
                procedure mainfoo() ;
                beGin
                 a[b[2]] := 100;
                 foo(2);
                 return ;
                eND
                """
        expect = "successful"

        self.assertTrue(TestParser.test(input,expect,246))
    def test_statement_mix_8(self):
        """
                PROCEDURE main() ;
                beGin
                 if a=b then 
                 if c = d then e := f;
                 else i := 1;
                 else x := 2 ;
                eND
                """
        input = """
                PROCEDURE main() ;
                beGin
                 if a=b then 
                 if c = d then e := f;
                 else i := 1;
                 else x := 2 ;
                eND
                """
        expect = "successful"

        self.assertTrue(TestParser.test(input,expect,247))
    def test_statement_mix_9(self):
        """
                procedure swap() ;
                var a: array[0 .. m-1] of integer;
                 i,j,temp: integer;
                beGin
                    for i := 0 to n do
                        for j:= i+1 to n-1 do
                            if(a[i]>a[j]) then
                            beGin
                                temp := a[i];
                                a[i] := a[j];
                                a[j] := temp;
                            eND
                    print(a);
                eND
                """
        input = """
                procedure swap() ;
                var a: array[0 .. m-1] of integer;
                 i,j,temp: integer;
                beGin
                    for i := 0 to n do
                        for j:= i+1 to n-1 do
                            if(a[i]>a[j]) then
                            beGin
                                temp := a[i];
                                a[i] := a[j];
                                a[j] := temp;
                            eND
                    print(a);
                eND
                """
        expect = "successful"

        self.assertTrue(TestParser.test(input,expect,248))
    def test_statement_mix_10(self):
        """
        procedure swap() ;
        var a: array[0 .. m-1] of integer;
            i,j,temp: integer;
        beGin
        { 
            if then else
        }
        function("hello");
        eND
        """
        input = """
        { 
            if then else
        }
        function("hello");
        """
        expect = "successful"

        self.assertTrue(TestParser.test(input,expect,249))
    def test_statement_mix_11(self):
        """
        procedure swap() ;
        var a: array[0 .. m-1] of integer;
            i,j,temp: integer;
        beGin
        if (x:=1) = 2 then
            print("done");
        else
            exit(0);
        END
        """
        input = """
        procedure swap() ;
        var a: array[0 .. m-1] of integer;
            i,j,temp: integer;
        beGin
        if (x:=1) = 2 then
            print("done");
        else
            exit(0);
        END
        """
        expect = ""

        self.assertTrue(TestParser.test(input,expect,250))
    def test_statement_mix_12(self):
        """
                Function CountX(A:array[0 .. 100] of integer; N,X : Integer) : Integer;
                Var i , Count : Integer;
                Begin
                 Count := 0;
                 For i:=1 to N do
                  If ( A[i] = X ) then
                   Count := Count + 1;
                 return Count;
                End
                """
        input = """
                Function CountX(A:array[0 .. 100] of integer; N,X : Integer) : Integer;
                Var i , Count : Integer;
                Begin
                 Count := 0;
                 For i:=1 to N do
                  If ( A[i] = X ) then
                   Count := Count + 1;
                 return Count;
                End
                """
        expect = "successful"

        self.assertTrue(TestParser.test(input,expect,251))
    def test_statement_mix_13(self):
        """
                PROCEDURE replace (A:array[0 .. 100] of integer;N, x,y:Integer);
                Var i:Integer;
                Begin
                For i:=0 to N do
                If(A[i] = y) then { x ==> y }
                A[i] := x;
                return;
                End
                """
        input = """
                Procedure replace (A:array[0 .. 100] of integer;N, x,y:Integer);
                Var i:Integer;
                Begin
                 For i:=0 to N do
                  If(A[i] = x) then { x ==> y }
                  A[i] := y;
                  return;
                End
                """
        expect = "successful"

        self.assertTrue(TestParser.test(input,expect,252))
    def test_statement_mix_14(self):
        """
                function calc(i : integer): boolean;
                var k : integer;
                begin
                if copy(s,i-2*k+1,k) = copy(s,i-k+1,k) then
                   begin
                    exit();
                   end
                end
                """
        input = """
                function calc(i : integer): boolean;
                var k : integer;
                begin
                if copy(s,i-2*k+1,k) = copy(s,i-k+1,k) then
                   begin
                    exit();
                   end
                end
                """
        expect = "successful"

        self.assertTrue(TestParser.test(input,expect,253))
    def test_statement_mix_15(self):
        
        input = """
                Var R,S,P:real;
                pROCEDURE Scalc() ;
                Begin
                    Read(R);
                    S := 3.14 * R * R;
                    P := 2 * 3.14 * R;
                    return;
                End
                """
        expect = "successful"

        self.assertTrue(TestParser.test(input,expect,254))
    
    def test_statement_mix_16(self):
        input = """
                Var R,S,P:real;
                pROCEDURE Scalc() ;
                Begin
                    Read(R);
                    S := 3.14 * R * R;
                    P := 2 * 3.14 * R;
                    Mul := (S*P) / (S+P);
                    return Mul;
                End
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,255))
    
    def test_statement_mix_17(self):
        
    
        """ Test ... """
        input ="""
        var a, b, c: real;

        var x, y, z: Boolean;
        

        function n(): Real;
        var x, y, z: Integer;
        begin
            readLn();
            fs := readStdin();
            
            with i: integer; do begin
                for i := 6 downto -1 do h := 6 + i;
                if i > 6 then return 0;
            end
            return 1;
        end
        var w : integer;

        function bj(): Boolean;
        var a: string;
        begin 
            (*       
        end
        """
        expect ="Error on line 28 col 5: *"
        self.assertTrue(TestParser.test(input,expect,256))
       
    def test_statement_mix_18(self):
        """ Function Min(N:Integer) :Integer;
                Var x,y:Integer;
                Begin
                    if x <= y then i := x; else i := y;
                End"""
        input = """ Function Min(N:Integer) :Integer;
                Var x,y:Integer;
                Begin
                    if x <= y then i := x; else i := y;
                End"""
        expect = "successful"

        self.assertTrue(TestParser.test(input,expect,257))
    def test_statement_mix_19(self):
        """
                procedure main() ;
                beGin
                 a[b[2]] := 10;
                 foo();
                 if a=b then if c = d then e := f;
                 else i := 1;
                 else x := 2 ;
                 return ;
                eND
                """
        input = """
                procedure main() ;
                beGin
                 a[b[2]] := 10;
                 foo();
                 if a=b then if c = d then e := f;
                 else i := 1;
                 else x := 2 ;
                 return ;
                eND
                """
        expect = "successful"
        

        self.assertTrue(TestParser.test(input,expect,258))
    def test_statement_mix_20(self):
        """
                procedure test() ;
                begin
	               if a=b then
	               begin
		                 b := c ;
		                 if(e <> f) then foo(a,c) ;
                    if a=b then if c=d then while (d=e) do
                   beGin
                   eND
	               end
                end
                """
        input = """
                procedure test() ;
                begin
	               if a=b then
	               begin
		                 b := c ;
		                 if(e <> f) then foo(a,c) ;
                    if a=b then if c=d then while (d=e) do
                   beGin
                   eND
	               end
                end
                """
        expect = "successful"
        

        self.assertTrue(TestParser.test(input,expect,259))
    def test_statement_mix_21(self):
        
        input = """
                Var name: String;
                Procedure Main();
                Begin
	               (*this is line*)
	               writeln();//this is new line}
	               writeln(name);
	               readln();
                End
                """
        expect = "successful"
        

        self.assertTrue(TestParser.test(input,expect,260))

    def test_statement_mix_16(self):
        
        input = 
        

        self.assertTrue(TestParser.test(input,expect,261))
    def test_statement_mix_16(self):
        
        input = 
        

        self.assertTrue(TestParser.test(input,expect,262))
    def test_statement_mix_16(self):
        
        input = 
        

        self.assertTrue(TestParser.test(input,expect,263))
    def test_statement_mix_16(self):
        
        input = 
        

        self.assertTrue(TestParser.test(input,expect,264))
    
    def test_statement_mix_16(self):
        
        input = 
        

        self.assertTrue(TestParser.test(input,expect,265))
    def test_statement_mix_16(self):
        
        input = 
        

        self.assertTrue(TestParser.test(input,expect,266))
    def test_statement_mix_16(self):
        
        input = 
        

        self.assertTrue(TestParser.test(input,expect,267))
    def test_statement_mix_16(self):
        
        input = 
        

        self.assertTrue(TestParser.test(input,expect,268))
    def test_statement_mix_16(self):
        
        input = 
        

        self.assertTrue(TestParser.test(input,expect,269))
    def test_statement_mix_16(self):
        
        input = 
        

        self.assertTrue(TestParser.test(input,expect,270))
    def test_statement_mix_16(self):
        
        input = 
        

        self.assertTrue(TestParser.test(input,expect,271))
    def test_statement_mix_16(self):
        
        input = 
        

        self.assertTrue(TestParser.test(input,expect,272))
    def test_statement_mix_16(self):
        
        input = 
        

        self.assertTrue(TestParser.test(input,expect,273))
    def test_statement_mix_16(self):
        
        input = 
        

        self.assertTrue(TestParser.test(input,expect,274))
    def test_statement_mix_16(self):
        
        input = 
        

        self.assertTrue(TestParser.test(input,expect,275))
    def test_statement_mix_16(self):
        
        input = 
        

        self.assertTrue(TestParser.test(input,expect,276))
    def test_statement_mix_16(self):
        
        input = 
        

        self.assertTrue(TestParser.test(input,expect,277))
    def test_statement_mix_16(self):
        
        input = 
        

        self.assertTrue(TestParser.test(input,expect,278))
    def test_statement_mix_16(self):
        
        input = 
        

        self.assertTrue(TestParser.test(input,expect,279))
    def test_statement_mix_16(self):
        
        input = 
        

        self.assertTrue(TestParser.test(input,expect,280))
    def test_statement_mix_16(self):
        
        input = 
        

        self.assertTrue(TestParser.test(input,expect,281))
    def test_statement_mix_16(self):
        
        
        

        self.assertTrue(TestParser.test(input,expect,282))
    def test_statement_mix_16(self):
        
        
        

        self.assertTrue(TestParser.test(input,expect,283))
    def test_statement_mix_16(self):
        
        
        

        self.assertTrue(TestParser.test(input,expect,284))
    def test_statement_mix_16(self):
        
        input = 
        

        self.assertTrue(TestParser.test(input,expect,285))
      
    def test_statement_mix_42(self):
        input = """procedure foo(a,b:integer; c:real);
        var x,y: real;
        begin 
        x := y + 1;

        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,286))
    def test_statement_mix_43(self):
        input = """procedure foo(a,b:integer; c:real);
        var x,y: real;
        begin 
        a := b [10] := foo()[3] := x := 1 ;
        return;
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,287))
    def test_statement_mix_44(self): 
        input = """procedure foo(a,b:integer; c:real);
        var x,y: real;
        begin 
        a := b [10] := 3 := x := 1 ;

        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,288))
    def test_statement_mix_45(self): 
        input = """procedure foo(a,b:integer; c:real);
        var x,y: real;
            z: array[2 .. 3] of integer;
        begin 
        x := y + 1;
        y := z[2];
        y := y * y;
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,289))
    def test_statement_mix_46(self): 
        input = """procedure foo(a,b:integer; c:real);
        var x,y: real;
            z: array[2 .. 3] of integer;
        begin 
        x := y + 1;
        x := z[2];
        foo(x);
        foo(2)[3+x] := a[b[2]] +3;
        return foo(x);
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,290))

    def test_statement_mix_47(self):     
        input = """procedure foo(a,b:integer; c:real);
        var x,y: real;
            z: array[2 .. 3] of integer;
        begin 
        if 5>6 then x := y;
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,291))

    def test_statement_mix_48(self):       
        """procedure foo(a,b:integer; c:real);
        var x,y: real;
            z: array[2 .. 3] of integer;
        begin 
        if (5>6) then x := y; else y := x := 1;
        
        end"""
        input = """procedure foo(a,b:integer; c:real);
        var x,y: real;
            z: array[2 .. 3] of integer;
        begin 
        if (5>6) then x := y; else y := x := 1;
        
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,292))

       
    def test_statement_mix_49(self):    
        """procedure foo(a,b:integer; c:real);
        var x,y: real;
            z: array[2 .. 3] of integer;
        begin 
        if (5>6) then x := y; else 
            if (true) then y:=x;
        x := z[2];
        end"""
        input = """procedure foo(a,b:integer; c:real);
        var x,y: real;
            z: array[2 .. 3] of integer;
        begin 
        if (5>6) then x := y; else 
            if (true) then y:=x;
        x := z[2];
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,293))

    
    def test_statement_mix_50(self):
         """procedure foo(a,b:integer; c:real);
        var x,y: real;
            z: array[2 .. 3] of integer;
        begin 
        if (5>6) then x := y; else 
            if (true) then y:=x;
        
        end"""
        input = """procedure foo(a,b:integer; c:real);
        var x,y: real;
            z: array[2 .. 3] of integer;
        begin 
        if (5>6) then x := y; else 
            if (true) then y:=x;
        
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,294))
    def test_wrong_miss_close_1(self):
        """Miss ) """
        input = """procedure foo(a,b:integer; c:real;
        var x,y: real 
        begin
        end"""
        expect = "Error on line 2 col 8: var"
        self.assertTrue(TestParser.test(input,expect,295))
    def test_wrong_miss_close_2(self):
        """incorrect variable declaration 3"""
        input = """float a,c,d"""
        expect = "Error on line 1 col 0: float"
        self.assertTrue(TestParser.test(input,expect,296))

    def test_array_1(self):
        """array type"""
        input = """var d:array [ 1 .. 5 ] of integer;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,297))
    def test_array_2(self):        
        input = """var d:array [ 1 .. 5  of integer;"""
        expect = "Error on line 1 col 22: of"
        self.assertTrue(TestParser.test(input,expect,298))
    def test_array_3(self):    
        input = """var d:array [1 .. 5] of integer; a,b,c: integer; e,f: real;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,299))
    def test_array_4(self):
        input = """var d:array [1 .. 5] of integer;\n a,b,c: integer;\n e,f: real;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,300))

    #def test_expression(self):
'''