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

program  : ;//mptype 'main' LB RB LP body? RP EOF ;

/*mptype: INTTYPE | VOIDTYPE ;

body: funcall SEMI;

exp: funcall | INTLIT ;

funcall: ID LB exp? RB ;
*/
//key insensitive
fragment A: [aA];
fragment B: [Bb];
fragment C: [Cc];
fragment D: [Dd];
fragment E: [Ee];
fragment F: [Ff];
fragment G: [Gg];
fragment H: [Hh];
fragment I: [Ii];
fragment J: [Jj];
fragment K: [Kk];
fragment L: [Ll];
fragment M: [Mm];
fragment N: [Nn];
fragment O: [Oo];
fragment P: [Pp];
fragment Q: [Qq];
fragment R: [Rr];
fragment S: [Ss];
fragment T: [Tt];
fragment U: [Uu];
fragment V: [Vv];
fragment W: [Ww];
fragment X: [Xx];
fragment Y: [Yy];
fragment Z: [Zz];

// keyword
BREAK: B R E A K;
CONTINUE: C O N T I N U E;
FOR: F O R;
TO: T O;
DOWNTO: D O W N T O;
DO: D O;
IF: I F;
THEN: T H E N;
ELSE: E L S E;
RETURNS: R E T U R N;
WHILE: W H I L E;
BEGIN: B E G I N;
END: E N D;
FUNCTION: F U N C T I O N;
PROCEDURE: P R O C E D U R E;
VAR: V A R;
TRUE: T R U E;
FALSE: F A L S E;
ARRAY: A R R A Y;
OF: O F;
REAL: R E A L;
BOOLEAN: B O O L E A N;
INTEGER: I N T E G E R;
STRING: S T R I N G;
NOT: N O T;
AND: A N D;
OR: O R;
DIV: D I V;
MOD: M O D;



//ID: (A..Z|'_')(A..Z|'0'..'9'|'_')*;
fragment IDCHAR: (A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z);
ID: (IDCHAR | '_')(IDCHAR | '_' | '0'..'9')*;
// Operators
ADDOP: '+';
MULOP: '*';
NEQOP: '<>';
LTOP: '<';
LTEOP: '<=';
SUBOP: '-';
DIVOP: '/';
EQOP: '=';
GTOP: '>';
GTEOP: '>=';





INTLIT: [0-9]+;

LB: '(' ;

RB: ')' ;

LP: '{';

RP: '}';

SEMI: ';' ;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

BLOCKCOM_B: '(*'.*?'*)' ->skip;
BLOCKCOM_P: '{'.*?'}' -> skip;
LINECOM: '//'~[\r\n]* ->skip;

ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;