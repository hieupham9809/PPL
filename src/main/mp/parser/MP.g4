grammar MP;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program  : mptype 'main' LB RB LP body? RP EOF ;

mptype: INTTYPE | VOIDTYPE ;

body: funcall SEMI;

exp: funcall | INTLIT ;

funcall: ID LB exp? RB ;

INTTYPE: 'int' ;

VOIDTYPE: 'void'  ;

ID: [a-zA-Z]+ ;

INTLIT: [0-9]+;

LB: '(' ;

RB: ')' ;

LP: '{';

RP: '}';

SEMI: ';' ;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

fragment LETTER: [a-z];

fragment DIGIT: [0-9];

CIDENTIFIER: LETTER (LETTER | DIGIT)*;

REAL: DIGIT* '.' DIGIT+ | DIGIT* ('.'DIGIT+)? 'e' '-'? DIGIT+; 

STRING: '\''(~'\'' | '\'''\'')+ '\'';

//STRING: (LETTER+ ('\'''\'')? )+;
ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;