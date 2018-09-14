	/* 1614246 */
grammar MP;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program		
	: declaration+ EOF
	;

declaration	
	: var_decl 
	| func_decl 
	| procedure_decl 
	;

var_decl	
	: VAR list_decls 
	;

list_decls	
	: decl+
	;

decl		
	: list_ID CL mptype SM 
	;

list_ID		
	: ID (CM ID)* 
	;

func_decl	
	: FUNCTION ID LB param_list RB CL mptype SM (var_decl)? compound_stmt 
	;

param_list	
	: param param_list1  
	| 
	;

param_list1	
	: SM param param_list1 
	| 
	;

param		
	: list_ID CL mptype 
	;

procedure_decl
	: PROCEDURE ID LB param_list RB SM (var_decl)? compound_stmt
	;

mptype
	: primitive_type 
	| compound_type
	;

primitive_type
	: BOOLEAN
	| INTEGER
	| REAL 
	| STRING
	;

compound_type
	: arraylit
	;

arraylit
	: ARRAY LSB (SUB? INTLIT) DDOT (SUB? INTLIT) RSB OF primitive_type
	;

expr		
	: expr AND THEN expr1
	| expr OR ELSE expr1
	| expr1
	;

expr1		
	: expr2 EQ  expr2
	| expr2 NEQ expr2
	| expr2 LESSTHAN  expr2
	| expr2 LESSEQ  expr2
	| expr2 GREATERTHAN expr2
	| expr2 GREATEREQ expr2 
	| expr2 
	;

expr2		
	: expr2 ADD expr3
	| expr2 SUB expr3
	| expr2 OR expr3 
	| expr3  
	;

expr3		
	: expr3 DIV_F expr4
	| expr3 MUL expr4
	| expr3 DIV expr4
	| expr3 MOD expr4
	| expr3 AND expr4
	| expr4
	;

expr4
	: SUB expr4
	| NOT expr4
	| expr5
	;

// array_elmt 
expr5 
	: expr5 LSB expr RSB
	| expr6
	;

expr6
	: LB expr RB
	| operand
	;

operand	
	: INTLIT 
	| REALLIT 
	| ID 
	| STRINGLIT
	| BOOLEANLIT
	| func_call 
	;  


array_elmt
	: expr5 LSB expr RSB
	;

func_call
	: ID LB list_expr RB
	;

list_expr
	: expr list_expr1
	| 
	;

list_expr1
	: CM expr list_expr1
	|
	;

statement
	: assignment_stmt 	SM
	| if_stmt
	| for_stmt
	| while_stmt
	| break_stmt 		SM
	| continue_stmt 	SM
	| return_stmt 		SM
	| call_stmt 		SM
	| compound_stmt 
	| with_stmt 
	;

assignment_stmt
	: ((ID | array_elmt) ASSIGN) assignment_stmt
	| (ID | array_elmt) ASSIGN expr
	;

if_stmt
	: IF expr THEN statement (ELSE statement)?
	;

while_stmt
	: WHILE expr DO statement
	;
			
for_stmt
	: FOR ID ASSIGN expr (TO|DOWNTO) expr DO statement
	;

break_stmt
	: 	BREAK
	;

continue_stmt
	: CONTINUE
	;

return_stmt
	: RETURN expr?
	;

compound_stmt
	: BEGIN list_stmt END
	;


list_stmt
	: statement list_stmt1
	|
	;

list_stmt1
	: statement list_stmt1
	| 
	;

call_stmt
	: ID LB list_expr RB
	;

with_stmt
	: WITH list_decls DO statement
	;


COMMENT1 
	: '(*' .*? '*)' -> skip 
	;

COMMENT2
	: '{' .*? '}' -> skip
	;

COMMENT3
	: '//' (~('\n'))* -> skip
	;

fragment LETTER 
	: A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z
	;

fragment UNDERSCORE
	: '_'
	;

fragment DIGIT
	: [0-9] 
	;

BREAK
	: B R E A K
	;

CONTINUE
	: C O N T I N U E
	;

FOR
	: F O R
	;

WHILE
	: W H I L E
	;

TO
	: T O
	;

DOWNTO
	: D O W N T O
	;

WITH
	: W I T H
	;

DO
	: D O
	;

IF
	: I F
	;

THEN
	: T H E N
	;

ELSE
	: E L S E
	;

VAR
	: V A R
	;

OF
	: O F
	;

BEGIN
	: B E G I N
	;

END
	: E N D
	;

RETURN
	: R E T U R N
	;

FUNCTION
	: F U N C T I O N
	;

PROCEDURE
	: P R O C E D U R E
	;

ARRAY
	: A R R A Y
	;

REAL
	: R E A L
	;

BOOLEAN
	: B O O L E A N
	;

INTEGER
	: I N T E G E R
	;

STRING
	: S T R I N G
	;

NOT
	: N O T
	;

AND
	: A N D
	;

OR
	: O R
	;

DIV
	: D I V
	;

MOD
	: M O D
	;


ADD
	: '+'
	;

SUB
	: '-'
	;

MUL
	: '*'
	;

DIV_F
	: '/'
	;

EQ
	: '='
	;

NEQ
	: '<>'
	;

LESSTHAN
	: '<'
	;

GREATERTHAN
	: '>'
	;

LESSEQ
	: '<='
	;

GREATEREQ
	: '>='
	;

ASSIGN
	: ':='
	;

LSB
	: '['
	;

RSB
	: ']'
	;

CL
	: ':'
	;

LB
	: '(' 
	;

RB
	: ')' 
	;

SM
	: ';'
	;

DDOT
	: '..'
	;

CM
	: ','
	;

fragment A
	: [Aa]
    ;
    
fragment B
	: [Bb]
    ;
    
fragment C
	: [Cc]
    ;
    
fragment D
	: [Dd]
    ;
    
fragment E
	: [Ee]
    ;
    
fragment F
	: [Ff]
    ;
    
fragment G
	: [Gg]
    ;
    
fragment H
	: [Hh]
    ;
    
fragment I
	: [Ii]
    ;
    
fragment J
	: [Jj]
    ;
    
fragment K
	: [Kk]
    ;
    
fragment L
	: [Ll]
    ;
    
fragment M
	: [Mm]
    ;
    
fragment N
	: [Nn]
    ;
    
fragment O
	: [Oo]
    ;
    
fragment P
	: [Pp]
    ;
    
fragment Q
	: [Qq]
    ;
    
fragment R
	: [Rr]
    ;
    
fragment S
	: [Ss]
    ;
    
fragment T
	: [Tt]
    ;
    
fragment U
	: [Uu]
    ;
    
fragment V
	: [Vv]
    ;
    
fragment W
	: [Ww]
    ;
    
fragment X
	: [Xx]
    ;
    
fragment Y
	: [Yy]
    ;
    
fragment Z
	: [Zz]
    ;

fragment BSP
	: '\\b'
	;

fragment FF 
	: '\\f'
	;

fragment CR 
	: '\\r'
	;

fragment NL 
	: '\\n'
	;

fragment TAB 
	: '\\t'
	;

fragment SQ 
	: '\\\''
	;

fragment DQ 
	: '\\"'
	;

fragment BSL
	: '\\''\\'
	;

fragment LEGAL_ESCAPE
	: BSP
    | FF
    | CR
    | NL
    | TAB
    | SQ
    | DQ
    | BSL
    ;

UNCLOSE_STRING
	: '"' (~[\n\r\\'"] | LEGAL_ESCAPE)* {
   		raise UncloseString(self.text[1:])
	}
	;

ILLEGAL_ESCAPE
//	: UNCLOSE_STRING [\b\f\t\\'] {
	: UNCLOSE_STRING ('\\' ~[nrbft'"] | '\'') {

 	   raise IllegalEscape(self.text[1:])
	}
	;

STRINGLIT
	: UNCLOSE_STRING '"' {
    	self.text = self.text[1:-1]
	}
	;

fragment Decimal_point
	: (DIGIT+'.'DIGIT*)|(DIGIT*'.'DIGIT+);

fragment Scientific_notation
	: [Ee]'-'?DIGIT+;
	
INTLIT		
	: DIGIT+
	;

REALLIT
	: (Decimal_point Scientific_notation ? ) | (DIGIT+ Scientific_notation);

BOOLEANLIT
	: TRUE | FALSE
	;

TRUE
	: T R U E
	;

FALSE
	: F A L S E
	;

ID
	: (LETTER | UNDERSCORE) (LETTER| UNDERSCORE | DIGIT )*
	;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

ERROR_CHAR
	: . {
  		 raise ErrorToken(self.text)
	}
	;