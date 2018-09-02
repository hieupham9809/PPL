grammar MP;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program  : declaration+;

declaration:vardec|funcdec;

vardec: (INT | FLOAT) idlist SM;
idlist: ID CM idlist | ID;

funcdec: (INT | FLOAT) ID LP parameterdec? RP block SM;
parameterdec: parameter SM parameterdec | parameter;
parameter: (INT | FLOAT) parameter_list;
parameter_list: ID CM parameter_list | ID;
block: LB (vardec | statement)* RB;
statement: (assignment | call | return) SM;
assignment: ID EQ expression;
call: ID LP expr_list RP;
expr_list: ID CM expr_list | ID;
return: RETURN expression?;

expression: exp SM;
exp: exp1 ADD exp | exp1;
exp1: exp2 SUB exp2;
exp2: exp2 (MUL | DIV) exp3 | exp3;
exp3: LP exp RP | exp4;
exp4: operand|call;

operand: INTLIT|FLOATLIT|ID|exp3;








LP: '(' ;

RP: ')' ;

LB: '{';

RB: '}';

SM: ';' ;

CM: ',';

EQ: '=';

RETURN: 'return';

ADD: '+';

SUB: '-';

MUL: '*';

DIV: '/';

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

fragment LETTER: [a-z];

fragment DIGIT: [0-9];

ID: LETTER (LETTER | DIGIT)*;

FLOATLIT: DIGIT* '.' DIGIT+ | DIGIT* ('.'DIGIT+)? 'e' '-'? DIGIT+; 

INTLIT: [0-9]+;

INT: 'int';

FLOAT: 'float';

STRING: '\''(~'\'' | '\'''\'')+ '\'';

//STRING: (LETTER+ ('\'''\'')? )+;
//ERROR_CHAR: .;
//UNCLOSE_STRING: .;
//ILLEGAL_ESCAPE: .;