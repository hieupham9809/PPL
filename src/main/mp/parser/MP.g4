grammar MP;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program  : manydeclr;
manydeclr: declaration manydeclr | declaration;

declaration:varDec|funcDec;

varDec: typeMP idList SM;
typeMP: INT | FLOAT;

idList: ID CM idList | ID;

funcDec: typeMP ID paramDec body;
paramDec: LP RP | LP smList RP;			

smList: typeMP idList SM smList | typeMP idList;
body: LB stmtType RB | LB RB;


stmtType: (varDec | statement) stmtType |  ;
statement: (assignment | call | returnMP) SM;
assignment: ID EQ expression;
call: ID LP expressionList? RP;
expressionList: expression (CM expression)*;
returnMP: RETURNS expression;

expression: exp;
exp: exp1 ADD exp | exp1;
exp1: exp2 SUB exp2 | exp2;

exp2: exp3 exp0;
exp0: ((MUL | DIV) exp3)?;
exp3: LP exp RP | exp4;
exp4: operand|call;

operand: INTLIT|FLOATLIT|ID;




INT: 'int';
FLOAT: 'float';
RETURNS: 'return';

fragment LETTER: [a-zA-Z];
fragment DIGIT: [0-9];

ID: LETTER (LETTER | DIGIT)*;
FLOATLIT: DIGIT* '.' DIGIT+ | DIGIT* ('.'DIGIT+)? 'e' '-'? DIGIT+; 
INTLIT: DIGIT+;

LP: '(' ;

RP: ')' ;

LB: '{';

RB: '}';

SM: ';' ;

CM: ',';

EQ: '=';

ADD: '+';

SUB: '-';

MUL: '*';

DIV: '/';


STRING: '\''(~'\'' | '\'''\'')+ '\'';

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines
//STRING: (LETTER+ ('\'''\'')? )+;
ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;
