# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\39")
        buf.write("\7\4\2\t\2\3\2\3\2\3\2\2\2\3\2\2\2\2\5\2\4\3\2\2\2\4\5")
        buf.write("\3\2\2\2\5\3\3\2\2\2\2")
        return buf.getvalue()


class MPParser ( Parser ):

    grammarFileName = "MP.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'+'", "'*'", 
                     "'<>'", "'<'", "'<='", "'-'", "'/'", "'='", "'>'", 
                     "'>='", "<INVALID>", "<INVALID>", "'('", "')'", "'{'", 
                     "'}'", "';'", "','" ]

    symbolicNames = [ "<INVALID>", "BREAK", "CONTINUE", "FOR", "TO", "DOWNTO", 
                      "DO", "IF", "THEN", "ELSE", "RETURNS", "WHILE", "BEGIN", 
                      "END", "FUNCTION", "PROCEDURE", "VAR", "TRUE", "FALSE", 
                      "ARRAY", "OF", "REAL", "BOOLEAN", "INTEGER", "STRING", 
                      "NOT", "AND", "OR", "DIV", "MOD", "ID", "ADDOP", "MULOP", 
                      "NEQOP", "LTOP", "LTEOP", "SUBOP", "DIVOP", "EQOP", 
                      "GTOP", "GTEOP", "INTLIT", "REALIT", "LB", "RB", "LP", 
                      "RP", "SEMI", "COMMA", "WS", "BLOCKCOM_B", "BLOCKCOM_P", 
                      "LINECOM", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0

    ruleNames =  [ "program" ]

    EOF = Token.EOF
    BREAK=1
    CONTINUE=2
    FOR=3
    TO=4
    DOWNTO=5
    DO=6
    IF=7
    THEN=8
    ELSE=9
    RETURNS=10
    WHILE=11
    BEGIN=12
    END=13
    FUNCTION=14
    PROCEDURE=15
    VAR=16
    TRUE=17
    FALSE=18
    ARRAY=19
    OF=20
    REAL=21
    BOOLEAN=22
    INTEGER=23
    STRING=24
    NOT=25
    AND=26
    OR=27
    DIV=28
    MOD=29
    ID=30
    ADDOP=31
    MULOP=32
    NEQOP=33
    LTOP=34
    LTEOP=35
    SUBOP=36
    DIVOP=37
    EQOP=38
    GTOP=39
    GTEOP=40
    INTLIT=41
    REALIT=42
    LB=43
    RB=44
    LP=45
    RP=46
    SEMI=47
    COMMA=48
    WS=49
    BLOCKCOM_B=50
    BLOCKCOM_P=51
    LINECOM=52
    ERROR_CHAR=53
    UNCLOSE_STRING=54
    ILLEGAL_ESCAPE=55

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MPParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MPParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





