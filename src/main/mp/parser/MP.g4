/* 
    NAME: Pham Minh Hieu
    ID: 1611046 
*/

grammar MP;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program  : declaration+;
declaration     : varDec | funcDec | procDec;

varDec          : VAR listOfDecls;
listOfDecls     : listOfType listOfDecls1;
listOfDecls1    : SEMI listOfType listOfDecls1 | SEMI;
listOfType      : listID COLON types ;
listID          : ID listID1;
listID1         : COMMA ID listID1 | ;

// type
types           : BOOLEAN | INTEGER | REAL | STRING | arraycp;
arraycp         : ARRAY LSB INTLIT DDOT INTLIT RSB OF arrayType;
arrayType       : BOOLEAN | INTEGER | REAL | STRING;

// funcDec
funcDec: ID;
/*funcDec         : FUNCTION ID LB paramList RB COLON types SEMI varDec? compound_st;
paramList       : paramDec paramList1 | ;
paramList1      : SEMI paramDec paramList1 | ;
paramDec        : listOfType;
compound_st     : BEGIN statement* END;

// statements
statement       : assign_st | if_st | for_st | while_st | break_st | continue_st | return_st | call_st | compound_st | with_st;
*/
// procDec
procDec         : ID;

//key insensitive
fragment A: [aA];
fragment B: [bB];
fragment C: [cC];
fragment D: [dD];
fragment E: [eE];
fragment F: [fF];
fragment G: [gG];
fragment H: [hH];
fragment I: [iI];
fragment J: [jJ];
fragment K: [kK];
fragment L: [lL];
fragment M: [mM];
fragment N: [nN];
fragment O: [oO];
fragment P: [pP];
fragment Q: [qQ];
fragment R: [rR];
fragment S: [sS];
fragment T: [tT];
fragment U: [uU];
fragment V: [vV];
fragment W: [wW];
fragment X: [xX];
fragment Y: [yY];
fragment Z: [zZ];

// keyword
BREAK       : B R E A K;
CONTINUE    : C O N T I N U E;
FOR         : F O R;
TO          : T O;
DOWNTO      : D O W N T O;
DO          : D O;
IF          : I F;
THEN        : T H E N;
ELSE        : E L S E;
RETURNS     : R E T U R N;
WHILE       : W H I L E;
BEGIN       : B E G I N;
END         : E N D;
FUNCTION    : F U N C T I O N;
PROCEDURE   : P R O C E D U R E;
VAR         : V A R;
TRUE        : T R U E;
FALSE       : F A L S E;
ARRAY       : A R R A Y;
OF          : O F;
REAL        : R E A L;
BOOLEAN     : B O O L E A N;
INTEGER     : I N T E G E R;
STRING      : S T R I N G;
NOT         : N O T;
AND         : A N D;
OR          : O R;
DIV         : D I V;
MOD         : M O D;



//ID: (A..Z|'_')(A..Z|'0'..'9'|'_')*;
fragment IDCHAR: (A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z);
ID  : (IDCHAR | '_')(IDCHAR | '_' | '0'..'9')*;
// Operators
ADDOP   : '+';
MULOP   : '*';
NEQOP   : '<>';
LTOP    : '<';
LTEOP   : '<=';
SUBOP   : '-';
DIVOP   : '/';
EQOP    : '=';
GTOP    : '>';
GTEOP   : '>=';



// Literals
fragment DIGIT:  [0-9];
INTLIT  : DIGIT+;
REALIT  : ((NUM_HAS_P | DIGIT+) EXPN) | NUM_HAS_P;


//ILLEGAL_ESCAPE: '"' .*? '\\' ~[bfrnt'"\\] ; ////// stuck here

STRLIT  : '"' ~[\n\b\f\r\t]* '"'
                        {
                            self.text = self.text[1:len(self.text)-1]
                        }

;
//fragment NUM_NP  :  NUM_P | ;
fragment NUM_HAS_P   :   DIGIT* '.' DIGIT+ | DIGIT+ '.' DIGIT*;   
fragment EXPN        :   (E '-'?) DIGIT+;




// Separators
LB      : '(' ;

RB      : ')' ;

SEMI    : ';' ;

COMMA   : ',';

LSB     : '[';

RSB     : ']';

COLON   : ':';

DDOT    : '..';

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

// Comments
BLOCKCOM_B: '(*'.*?'*)' ->skip;
BLOCKCOM_P: '{'.*?'}' -> skip;
LINECOM: '//'~[\r\n]* ->skip;

ERROR_CHAR: .;
//not already handle
UNCLOSE_STRING: '"' ~["]*               
            {
                self.text = self.text[1:]        
            };
//ILLEGAL_ESCAPE: .;